# Embedded file name: C:\Users\orhan\AppData\Roaming\Kodi\addons\plugin.video.OTV_MEDIA\resources\sayfalar\LIVETV.py

SITE_IDENTIFIER = 'LIVETV'
SITE_NAME = 'LIVE NET TV'
SPORT_SPORTS = (True, 'root')
from pyDes import des, PAD_PKCS5
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem
from routing import Plugin
from requests_cache import CachedSession
import  requests_cache
#-*- coding: utf-8 -*-
from resources.lib.config import cConfig
import requests
import re,xbmcgui,unicodedata              
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import  cParser

from resources.lib.player import cPlayer
from resources.lib.backtothefuture import PY2, PY3, unichr
from resources.lib.gui.guiElement import cGuiElement
from resources.sites.LIVETV2 import *
import sys
import os
import io
import time
import json
import requests
import datetime
from datetime import timedelta
from base64 import b64decode, urlsafe_b64encode
from itertools import chain
from routing import Plugin
try:
    from urllib.parse import quote as orig_quote
except ImportError:
    from urllib import quote as orig_quote
#from resources.lib.lntv_config import lntvConfig
from resources.lib.rbtv_config import rbtvConfig
from resources.lib.rbtv_channels import rbtvChannels
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
plugin = Plugin()
s = requests.Session()
plugin.name = addon.getAddonInfo('name')
user_agent = 'stagefright/1.2 (Linux;Android 4.4.2)'
implemented = ['0',
 '38',
 '21',
 '48']
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('profile'))
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
user_file = os.path.join(RESOURCES_DIR, 'user.json')
user_file = to_utf8(user_file)

channel_list_file = os.path.join(RESOURCES_DIR, 'channels.json')
channel_list_file = to_utf8(channel_list_file)
app_config_file = os.path.join(RESOURCES_DIR, 'config.json')
app_config_file = to_utf8(app_config_file)
implemented = ["0", "38", "21", "48"]


data_time = int(addon.getSetting("data_time") or "0")
cache_time = int(addon.getSetting("cache_time") or "0")
user_id = addon.getSetting("user_id")

player_user_agent = 'mediaPlayerhttp/2.4 (Linux;Android 5.1) ExoPlayerLib/2.6.1'
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

def quote(s, safe = ''):
    return orig_quote(s.encode('utf-8'), safe.encode('utf-8'))


try:
    with io.open(user_file, 'r', encoding='utf-8') as f:
        
        user = json.loads(f.read())
except IOError:
    user = ''

current_time = int(time.time())
if current_time - data_time > cache_time * 60 * 60:
    try:
        new_config = rbtvConfig(user=user)
        app_config = new_config.get_data()
        with io.open(user_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(new_config.user, indent=2, sort_keys=True, ensure_ascii=False))
        with io.open(app_config_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(app_config, indent=2, sort_keys=True, ensure_ascii=False))
    except:
        with io.open(app_config_file, 'r', encoding='utf-8') as f:
            app_config = json.loads(f.read())

    try:
        new_channels = rbtvChannels(app_config, user_id)
        channel_list = new_channels.get_channel_list()
        addon.setSetting('user_id', new_channels.user)
        with io.open(channel_list_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(channel_list, indent=2, sort_keys=True, ensure_ascii=False))
    except:
        with io.open(channel_list_file, 'r', encoding='utf-8') as f:
            channel_list = json.loads(f.read())

    addon.setSetting('data_time', str(int(time.time())))
else:
    try:
        with io.open(app_config_file, 'r', encoding='utf-8') as f:
            app_config = json.loads(f.read())
    except IOError:
        app_config = ''

    try:
        with io.open(channel_list_file, 'r', encoding='utf-8') as f:
            channel_list = json.loads(f.read())
    except IOError:
        channel_list = ''

def fix_auth_date(auth):
    now = datetime.datetime.utcnow()
    _in = list(auth)
    _in.pop(len(_in) + 2 - 3 - int(str(now.year)[:2]))
    _in.pop(len(_in) + 3 - 4 - int(str(now.year)[2:]))
    _in.pop(len(_in) + 4 - 5 - (now.month - 1 + 1 + 10))
    _in.pop(len(_in) + 5 - 6 - now.day)
    return ''.join(_in)


def get_auth_token_38():
    wms_url = "http://135.181.2.111:8800/fio/3b.rbt/"
    auth = b64decode(app_config.get("Z2Vsb29mc2JyaWVm")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    fix_auth = lambda auth: "".join([auth[:-59], auth[-58:-52], auth[-51:-43], auth[-42:-34], auth[-33:]])
    req = requests.Request(
        "GET",
        wms_url,
        headers={
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip",
            "Modified": modified(mod_value),
            "Authorization": auth,
        },
    )
    prq = req.prepare()
    r = s.send(prq)
    return fix_auth(r.text)


def get_auth_token_21():
    wms_url = b64decode(app_config.get("Y2FsYWFtb19pa3Mw")[1:])
    auth = b64decode(app_config.get("WXJfd3lmX3luX2JhaXMw")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    req = requests.Request(
        "GET",
        wms_url,
        headers={
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip",
            "Modified": modified(mod_value),
            "Authorization": auth,
        },
    )
    prq = req.prepare()
    r = s.send(prq)
    return r.text


def get_auth_token_48():
    wms_url = b64decode(app_config.get("Ym9ya3lsd3VyXzQ4")[1:])
    auth = b64decode(app_config.get("dGVydHRleWFj")[1:])
    mod_value = int(b64decode(app_config.get("TW9vbl9oaWsx")[1:]))
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
    req = requests.Request(
        "GET",
        wms_url,
        headers={
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip",
            "Modified": modified(mod_value),
            "Authorization": auth,
        },
    )
    prq = req.prepare()
    r = s.send(prq)
    return fix_auth_date(r.text)

def roootom():
    oGui = cGui()
    categories = channel_list.get('categories_list')
    for c in categories:
        sTitle = c.get('cat_name')
        url = c.get('cat_id')
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url)
        oGui.addDir(SITE_IDENTIFIER, 'list_channels', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def list_channels():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat = oInputParameterHandler.getValue('siteUrl')
    logger.info("Good cat:" +cat )
    list_items = []
    for channel in channel_list.get("eY2hhbm5lbHNfbGlzdA=="):
        if channel.get("cat_id") == cat:
          for stream in channel.get("Qc3RyZWFtX2xpc3Q="):
               
      
            
               
            title = b64decode(channel.get("ZY19uYW1l")[:-1]).decode("utf-8") 
            icon = b64decode(channel.get("abG9nb191cmw=")[1:]).decode("utf-8")        
            image = "{0}|User-Agent={1}".format(icon, quote(user_agent))
#            c_id = channel.get("rY19pZA==")
            media_url = b64decode(stream.get("Bc3RyZWFtX3VybA==")[1:])
            c_id =b64decode(stream.get("AdG9rZW4=")[:-1])
           # title  = alfabekodla(title)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('token', c_id)
            oOutputParameterHandler.addParameter('siteUrl', media_url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))
            oOutputParameterHandler.addParameter('sThumbnail', image) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'play', title , image, image, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()

def mlist_channels():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat = oInputParameterHandler.getValue('siteUrl').decode("utf-8") 
    list_items = []
    for channel in channel_list.get('eY2hhbm5lbHNfbGlzdA=='):
        if channel.get('cat_id') == cat:
            title = b64decode(channel.get('ZY19uYW1l')[:-1])
            icon = b64decode(channel.get('abG9nb191cmw=')[1:])
            image = '{0}|User-Agent={1}'.format(icon, quote(user_agent))
#            stream_ur = b64decode(channel.get('Bc3RyZWFtX3VybA==')[:-1])
            token = channel.get('AdG9rZW4=')
            media_url =channel.get("Bc3RyZWFtX3VybA==").replace("b'",'').replace("'",'')                                 
            #title = alfabekodla(title)
            if media_url=="www.canlitvlive.io":
                iossshowBox1(media_url,title)
            logger.info("Good token1:" +token )
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', media_url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))
            oOutputParameterHandler.addParameter('token', token)
            oOutputParameterHandler.addParameter('sThumbnail', image)
            oGui.addMovie(SITE_IDENTIFIER, 'play', title, image, image, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def play():                               
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    media_url = oInputParameterHandler.getValue('siteUrl')
    media_url=media_url.replace("b'",'').replace("'",'')
    name = oInputParameterHandler.getValue('sMovieTitle')
    token = oInputParameterHandler.getValue('token') 
    token=token.replace('b%2527','').replace('%2527','').replace("b'",'').replace("'",'')
    logger.info("==token: %s" %   token)
    if  token=="18":
        Url = media_url.replace("'b'",'').replace("''",'').replace("http://www.canlitvlive.io/izle/",'https://www.canlitv.me/').replace(".html",'').replace("sky-turk",'tv-360').replace("https://izle.canlitvlive.io/atv-hd-canli-izle-210314",'https://www.canlitv.me/a2-tv-1')     
        logger.info("==media_url: %s" %   Url)
        import xcanlitvzone
        url =xcanlitvzone.s_Box19(Url,name)
                                                                                                                                                               
       #  logger.info("==media_url: %s" %   calc)
        
       #  url = link[0]+ '|Referer='+url1+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
   
    elif token== "48":
        url =  media_url+ get_auth_token_48()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
    elif  token== "21":
        url =  media_url+ get_auth_token_21()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
    elif  token== "38":
        url = media_url+ get_auth_token_38()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
        logger.info("==url_url: %s" %   url)            
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')
   

def kshowHosters(url):
    name = 'true'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def addLink(name,url,pic):
        ok=True
        liz = xbmcgui.ListItem(name)
        liz.setArt({'thumb': pic, 'icon': pic, 'fanart': pic})
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok 

def iossshowBox1(Url,name):

                       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': Url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    dat = cRequestHandler(Url).request()  

                     

    Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    playlist= re.findall('file:.*?"(.*?)"', dat, re.S)[0] 
    url= playlist + '|' + Header

    
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'') 


