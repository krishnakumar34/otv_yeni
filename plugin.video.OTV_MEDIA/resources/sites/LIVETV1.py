# -*- coding: utf-8 -*-
from resources.lib.otvhelper import *
SITE_IDENTIFIER = 'LIVETV1'
SITE_NAME = 'LIVE NET TV'
SPORT_SPORTS = (True, 'root')

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem
from routing import Plugin

import requests
import traceback
import urllib
import time
import json
import io
import os
import sys
import string
import random
import datetime
import uuid
from hashlib import md5
from base64 import b64encode, b64decode, urlsafe_b64encode
from itertools import chain
# https://dl.dropboxusercontent.com/s/mi6irkq6hcwptly/vod_channels.geojson?dl=0
addon = xbmcaddon.Addon()
plugin = Plugin()
plugin.name = addon.getAddonInfo("name")
s = requests.Session()
                                              
# plugin conf
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo("path")).decode("utf-8")
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, "resources")


RESOURCES_D = os.path.join(ADDON_DATA_DIR , "resources")
RESOURCES = os.path.join(RESOURCES_D, "livenettv")
amf_request_file = os.path.join(RESOURCES, "request.amf")
channel_list_file = os.path.join(RESOURCES , "live_streams.geojson")
app_config_file = os.path.join(RESOURCES , "config.json")
implemented = ["0", "23", "29", "32", "33", "38", "44", "48"]

if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

# apk secrets
user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTS Build/LVY48F)"
device_name = "Fire TV"
package_name = "com.int.androidnettv"
version_sub = "30"
version = "4.7 ({0})".format(version_sub)
apk_cert_sha1 = "EA:32:78:87:BF:88:8F:AD:C9:88:81:09:9A:31:69:F7:BE:E9:91:CE"
kinvey_app_id = "kid_rkUF38Fbz"
kinvey_app_secret = "5fef3dcf83b74eaba14d87f1fe15747b"
user = "EtSBR38Y"
passwd = "c63Chg986t"

kinvey_login_url = "https://baas.kinvey.com/user/{0}/login".format(kinvey_app_id)
kinvey_config_url = "https://baas.kinvey.com/appdata/{0}/AppConfigCharlie".format(kinvey_app_id)

adduser_url = "http://195.154.26.54:8080/data/1/adduserinfo.nettv/"
list_url = "https://echo-d.livenettv.io/data/1/data.nettv/"


def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


_reset = addon.getSetting("reset") or "0"
if int(_reset) < int(version_sub):
    addon.setSetting("user_id", "")
    addon.setSetting("kinvey_auth", "")
    addon.setSetting("kinvey_user", "")
    addon.setSetting("data_time", "")
    addon.setSetting("android_id", "")
    addon.setSetting("reset", version_sub)

android_id = addon.getSetting("android_id")
if not android_id:
    android_id = id_generator()
    addon.setSetting("android_id", android_id)


def kinvey_login():
    body = json.dumps({"username": user, "password": passwd})
    r = requests.post(
        kinvey_login_url, data=body, headers={"User-Agent": user_agent, "Content-Type": "application/json"}, auth=(kinvey_app_id, kinvey_app_secret)
    )
    kinvey_login_response = r.json()
    kinvey_user = kinvey_login_response.get("_id")
    kinvey_auth = kinvey_login_response["_kmd"].get("authtoken")
    addon.setSetting("kinvey_user", kinvey_user)
    addon.setSetting("kinvey_auth", kinvey_auth)
    return kinvey_auth


def kinvey_get_config():
    kinvey_auth = kinvey_login()
    r = requests.get(
        kinvey_config_url, headers={"User-Agent": user_agent, "Authorization": "Kinvey {0}".format(kinvey_auth), "Content-Type": "application/json"}
    )

    config = r.json()[0]
    with io.open(app_config_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(config, indent=2, sort_keys=True, ensure_ascii=False))
    return config


def backendless_get_config():
    from pyamf import remoting

    _url = "https://api.backendless.com/762F7A10-3072-016F-FF64-33280EE6EC00/E9A27666-CD62-10CD-FF05-ED45B12ABE00/binary"
    headers = {"User-Agent": user_agent, "Content-Type": "application/x-amf"}

    with io.open(amf_request_file, "rb") as f:
        r = requests.post(_url, headers=headers, data=f)

    dec = remoting.decode(r.content)

    config = dict(dec["null"].body.body)

    with io.open(app_config_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(config, default=lambda obj: obj.strftime("%H:%M:%S"), indent=2, sort_keys=True, ensure_ascii=False))

    return config


def get_channel_list(config):
    if config.get("_acl"):
        provider = "1"
    else:
        provider = "2"
    login_index_php = b64decode(config.get("YXBpS2V5TGluazAw")[1:])
    referer = b64decode(config.get("SXNpc2VrZWxvX3Nlc2lzdGltdV95ZXppbm9tYm9sbzAw")[1:])
    auth = b64decode(config.get("amFnX3Ryb3JfYXR0X2Vu")[1:])
    time_stamp = str(int(time.time() * 1000))
    allow = b64encode(
        bytes(
            "{time_md5}${package_name}${apk_cert_sha1}${time_stamp}$${provider}".format(
                time_md5=md5(bytes(time_stamp)).hexdigest(), package_name=package_name, apk_cert_sha1=apk_cert_sha1, time_stamp=time_stamp, provider=provider
            )
        )
    )

    data = {"ALLOW": allow}
    r = requests.post(login_index_php, headers={"User-Agent": user_agent}, data=data)
    funguo = r.json().get("funguo")
    meta = r.headers["etag"].split(":")[0]

    user_id = addon.getSetting("user_id")
    if not user_id:
        user_id = get_user_id(config, funguo)

    time_stamp = str(int(time.time() * 1000))

    data = {"provider": provider, "time": time_stamp, "user_id": user_id, "check": "11", "key": funguo, "version": version_sub}  # ????

    r = requests.post(list_url, headers={"User-Agent": user_agent, "Referer": referer, "Meta": meta, "Authorization": auth}, data=data)
    channel_list = r.json()

    with io.open(channel_list_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(channel_list, indent=2, sort_keys=True, ensure_ascii=False))

    return channel_list


def get_user_id(config, funguo):
    if config.get("_acl"):
        provider = "1"
    else:
        provider = "2"
    referer = b64decode(config.get("SXNpc2VrZWxvX3Nlc2lzdGltdV95ZXppbm9tYm9sbzAw")[1:])
    auth = b64decode(config.get("amFnX3Ryb3JfYXR0X2Vu")[1:])
    if provider == "1":
        kinvey_auth = addon.getSetting("kinvey_auth")
        kinvey_user = addon.getSetting("kinvey_user")
    elif provider == "2":
        kinvey_user = ""
        addon.setSetting("kinvey_user", kinvey_user)
        _new_id = uuid.uuid4()
        kinvey_auth = "{0}.{1}".format(str(_new_id), _new_id.hex)
        addon.setSetting("kinvey_auth", kinvey_auth)

    kinvey_pass = kinvey_auth.split(".")[0]
    time_stamp = str(int(time.time() * 1000))

    _string2 = b"|".join(
        [b"19", b64encode(version_sub.encode()), b64encode(time_stamp.encode()), b64encode("000000000000000".encode()), b64encode(kinvey_pass.encode())]
    )

    _id = b"|".join(
        [
            md5(time_stamp.encode()).hexdigest().encode(),
            b64encode(package_name.encode()),
            b64encode(apk_cert_sha1.encode()),
            b64encode(device_name.encode()),
            b64encode(_string2),
        ]
    )

    data = {
        "id": b64encode(_id),
        "api_level": "19",
        "android_id": android_id,
        "time": time_stamp,
        "device_name": device_name,
        "kinvey": kinvey_user,
        "provider": provider,
        "device_id": "unknown",
        "key": funguo,
        "version": version,
    }

    r = requests.post(adduser_url, headers={"User-Agent": user_agent, "Referer": referer, "Authorization": auth}, data=data)
    user_id = r.json().get("user_id")
    addon.setSetting("user_id", user_id)
    return user_id


data_time = int(addon.getSetting("data_time") or "0")
cache_time = int(addon.getSetting("cache_time") or "0")

current_time = int(time.time())
if current_time - data_time > cache_time * 60 * 60:
    try:
        try:
            app_config = kinvey_get_config()
        except Exception:
            app_config = backendless_get_config()

        channel_list = get_channel_list(app_config)
        addon.setSetting("data_time", str(int(time.time())))
    except Exception:
        with io.open(channel_list_file, "r", encoding="utf-8") as f:
            channel_list = json.loads(f.read())

        with io.open(app_config_file, "r", encoding="utf-8") as f:
            app_config = json.loads(f.read())
else:
    with io.open(channel_list_file, "r", encoding="utf-8") as f:
        channel_list = json.loads(f.read())

    with io.open(app_config_file, "r", encoding="utf-8") as f:
        app_config = json.loads(f.read())


def quote(s):
    return urllib.quote(s.encode("utf-8"), str(""))


def unquote(s):
    return urllib.unquote(s).decode("utf-8")


def fix_auth_date(auth):
    now = datetime.datetime.utcnow()
    _in = list(auth)
    _in.pop(len(_in) + 2 - 3 - int(str(now.year)[:2]))
    _in.pop(len(_in) + 3 - 4 - int(str(now.year)[2:]))
    # java January = 0
    _in.pop(len(_in) + 4 - 5 - (now.month - 1 + 1 + 10))
    _in.pop(len(_in) + 5 - 6 - now.day)
    return "".join(_in)


# star sports
def get_auth_token_33(referer):
    if referer == None:
        referer = ""
    wms_url = b64decode(app_config.get("ZmFtYW50YXJhbmFfdGF0aTAw")[1:])
    auth = b64decode(app_config.get("dGVydHRleWFj")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    fix_auth = lambda auth: "".join([auth[:-56], auth[-55:-50], auth[-49:-42], auth[-41:-34], auth[-33:]])
    req = requests.Request(
        "GET",
        wms_url,
        headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Referer": referer, "Modified": modified(mod_value), "Authorization": auth},
    )
    prq = req.prepare()
    r = s.send(prq)
    return fix_auth(r.text)


# eurosport
def get_auth_token_38(referer):
    if referer == None:
        referer = ""
    wms_url = "http://135.181.2.111:8800/fio/3b.rbt/"
    auth = b64decode(app_config.get("Z2Vsb29mc2JyaWVm")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    fix_auth = lambda auth: "".join([auth[:-66], auth[-65:-56], auth[-55:-46], auth[-45:-36], auth[-35:]])
    req = requests.Request(
        "GET",
        wms_url,
        headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Referer": referer, "Modified": modified(mod_value), "Authorization": auth},
    )
    prq = req.prepare()
    r = s.send(prq)
    return fix_auth(r.text)


# ane
def get_auth_token_44():
    wms_url = b64decode(app_config.get("YmVsa2lpdW1uXzk2")[1:])
    auth = b64decode(app_config.get("dGVydHRleWFj")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    req = requests.Request(
        "GET", wms_url, headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Modified": modified(mod_value), "Authorization": auth}
    )
    prq = req.prepare()
    r = s.send(prq)
    return fix_auth_date(r.text)


# canada
def get_auth_token_23():
    wms_url = b64decode(app_config.get("dGhlX3RlYXMw")[1:])
    auth = b64decode(app_config.get("TWVuX2Nob2Jpc18w")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    req = requests.Request(
        "GET", wms_url, headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Modified": modified(mod_value), "Authorization": auth}
    )
    prq = req.prepare()
    r = s.send(prq)
    return r.text


# bt sports 1
def get_auth_token_48(referer):
    if referer == None:
        referer = ""
    wms_url = b64decode(app_config.get("Ym9ya3lsd3VyXzQ4")[1:])
    auth = b64decode(app_config.get("dGVydHRleWFj")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    req = requests.Request(
        "GET",
        wms_url,
        headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Referer": referer, "Modified": modified(mod_value), "Authorization": auth},
    )
    prq = req.prepare()
    r = s.send(prq)
    return fix_auth_date(r.text)


# bein 1
def get_stream_32(stream):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
    api_url = b64decode(app_config.get("dWt1c3VzYV91a3ViaGFsYV9iYXRlczAw")[1:])
    auth = b64decode(app_config.get("amFnX3Ryb3JfYXR0X2Vu")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))

    response_body_api_url = b64decode(app_config.get("bWFya2llcmlzX2J0aXMw")[1:])
    response_body_auth = b64decode(app_config.get("bXdlbnRlcnR5")[1:])
    req = requests.Request("GET", response_body_api_url, headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Authorization": response_body_auth})
    prq = req.prepare()
    r = s.send(prq)
    response_body = r.text

    data = {"data": json.dumps({"token": 32, "response_body": response_body, "stream_url": stream})}
    req = requests.Request(
        "POST", api_url, headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Modified": modified(mod_value), "Authorization": auth}, data=data
    )
    prq = req.prepare()
    r = s.send(prq)
    return r.json().get("url")


# bt sports 1
def get_stream_29(stream):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
    api_url = b64decode(app_config.get("Y2hlaWxlYWRoIF9DZWFuZ2FsX29udGlz")[1:])
    auth = b64decode(app_config.get("amFnX3Ryb3JfYXR0X2Vu")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))

    data = {"data": json.dumps({"token": 29, "response_body": "f", "stream_url": stream})}
    req = requests.Request(
        "POST", api_url, headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Modified": modified(mod_value), "Authorization": auth}, data=data
    )
    prq = req.prepare()
    r = s.send(prq)
    return r.json().get("stream_url")
  

def fetcher48():
    wms_url = "http://212.83.158.140:6060/aves.nettv/"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Referer':'http://xyz,com','Authorization': 'Basic QDA3NzEyMSM6QDA3NzEyMSM=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text

def fetcher38():
    wms_url = "http://212.83.158.140:6060/temporary/def.php"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Referer':'http://xyz,com','Authorization': 'Basic eWFyYXBuYWthYW1rYXJvOnR1bmduYWtpYWthcm8=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text



def fetcher44():
    wms_url = "http://212.83.182.86:8080/chick.nettv/"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Authorization': 'Basic QDA3NzEyMSM6QDA3NzEyMSM=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text


def fetcher33():
    wms_url = "http://78.129.139.44:3030/duck.nettv/"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Authorization': 'Basic QDA3NzEyMSM6QDA3NzEyMSM=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text
def rbtv():
     
       Url='http://51.15.209.90:8800/3rd.rbtv'
       req = urllib2.Request(Url)
#       req.add_header('Modified','10514263348556648368')
       req.add_header('Host','51.15.209.90:8800') 
       req.add_header('Authorization','Basic eWFyYXBuYWthYW1rYXJvOnR1bmduYWtpYWthcm8=')
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1; P6 PRO Build/LMY47D)')
       son=  _get(req)       
       return son

def fetcher22():
     
       Url='http://212.47.231.14:8090/data/(~)/auth.nettv/'
       req = urllib2.Request(Url)
       req.add_header('Modified','10514263348556648368')
       req.add_header('Host','linenettv.net:8090') 
       req.add_header('Authorization','Basic QFN3aWZ0MTQjOkBTd2lmdDE0Iw==')
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)')
       son=  _get(req)       
       return son

def rooto():
  oGui = cGui()
  categories =  os.path.join(RESOURCES, "live_categories.geojson")
  with io.open(categories, "r", encoding="utf-8") as f:
      data = json.loads(f.read())
      
      categories = data.get('features')
      for c in categories:
          sTitle = c.get('catName')
          url = c.get('catPriority')
        
       
            
    
          oOutputParameterHandler = cOutputParameterHandler()
          oOutputParameterHandler.addParameter('siteUrl', url)
          oGui.addDir(SITE_IDENTIFIER, 'list_channels',  sTitle, 'genres.png', oOutputParameterHandler)
  oGui.setEndOfDirectory()          
        


def list_channels():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_title = oInputParameterHandler.getValue('siteUrl')
    ulk ='https://dl.dropboxusercontent.com/s/id9pbhzbcvvlp66/live_channels.geojson'
    sJson = cRequestHandler(ulk).request()    
    aJson = json.loads(sJson)
    for cat in aJson["features"]:
        if cat["catId"] == cat_title:   
            sTitle =cat['name']
            url=cat['recordId']
            sPicture=cat['imagePath']
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'play', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()  
def play():
  oGui = cGui()
  oInputParameterHandler = cInputParameterHandler()
  cat_title = oInputParameterHandler.getValue('siteUrl')
  ulk ='https://dl.dropboxusercontent.com/s/qds0l87phsfprwe/live_streams.geojson'
  sJson = cRequestHandler(ulk).request()    
  aJson = json.loads(sJson)
  for cat in aJson["features"]:
     if cat["recordId"] == cat_title:   
        token =cat['token']
        media_url=cat['url'].replace('$6','%s').replace('$5','%s').replace('$4','%s').replace('$3','%s').replace('$2','%s').replace('$1','%s').replace('$0','%s').replace('$','%s')  
        if '/hera/' in media_url:             
           iki='dyna.livenettv.sx:2086'
           media_url =media_url% iki
        if '/anax/' in media_url:             
           bir='did.off.li:7623'
           media_url =media_url% bir
        if '/cobra/' in media_url:             
           sifir='190.2.141.189'
           media_url =media_url% sifir
        if '/styx/' in media_url:             
           iki='80.243.180.72:5432'
           media_url =media_url% iki
        if '/grat/' in media_url:             
           iki='190.2.141.189:6185'
           media_url =media_url% iki
        if '/gwat/' in media_url:             
           iki='163.172.87.170:5432'
           media_url =media_url% iki
        if '/red/' in media_url:             
           media_url =media_url
           iki='mia.tru.io:63159'
           media_url =media_url% iki
        if '/gaia/' in media_url:             
           iki='190.2.141.189:6185'
           media_url =media_url% iki
        lplay(media_url,token)




def lplay(media,toke):
        
        Referer=""
        token=toke
        media_url =media
        if "0" in token:
           media_url = media_url 
        if "44" in token:
           media_url =  media_url+ get_auth_token_44()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
        if "23" in token:
           media_url =  media_url+ get_auth_token_23()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
        if "48" in token:
           media_url = media_url+ get_auth_token_48(Referer)+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
        if "33" in token:
           media_url = media_url+ get_auth_token_33(Referer)+"|User-Agent=stagefright/1.2 (Linux;Android 5.1.1"
                   

        name="mann"
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,media_url, '')

def addLink(name,url,iconimage):

        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")                                                                  	

        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok  