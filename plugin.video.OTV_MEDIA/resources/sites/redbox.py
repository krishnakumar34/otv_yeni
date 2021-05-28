# -*- coding: utf-8 -*-


from resources.sites.LIVETV2 import *
from resources.lib.config import cConfig
import requests
import re,xbmcgui,unicodedata              
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, VSlog
from resources.lib.player import cPlayer

from resources.lib.gui.guiElement import cGuiElement

import sys
from xbmcgui import ListItem
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from routing import Plugin

import os
import io
import time
import json
import requests
import datetime
from datetime import timedelta
from itertools import chain
from base64 import b64decode
from future.moves.urllib.parse import urlencode

from resources.lib.rbtv_config import rbtvConfig
from resources.lib.rbtv_channels import rbtvChannels

SITE_IDENTIFIER ='redbox' 
addon = xbmcaddon.Addon()
plugin = Plugin()
s = requests.Session()
plugin.name = addon.getAddonInfo("name")
user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)"

implemented = ["0", "38", "21", "48"]
try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

ADDON_DATA_DIR = translatePath(addon.getAddonInfo("path"))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, "resources")

app_config_file = os.path.join(RESOURCES_DIR , "config32.json")
channel_list_file = os.path.join(RESOURCES_DIR , "channels32.json")
if not os.path.exists(RESOURCES_DIR ):
    os.makedirs(RESOURCES_DIR )

data_time = int(addon.getSetting("data_time32") or "0")
cache_time = int(addon.getSetting("cache_time") or "0")
user_id = addon.getSetting("user_id32")


current_time = int(time.time())
if current_time - data_time > cache_time * 60 * 60:
    try:
        new_config = rbtvConfig()
        app_config = new_config.get_data()
        with io.open(app_config_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(app_config, indent=2, sort_keys=True, ensure_ascii=False))
    except:
        with io.open(app_config_file, "r", encoding="utf-8") as f:
            app_config = json.loads(f.read())
    try:
        new_channels = rbtvChannels(app_config, user_id)
        channel_list = new_channels.get_channel_list()
        addon.setSetting("user_id32", new_channels.user)
        with io.open(channel_list_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(channel_list, indent=2, sort_keys=True, ensure_ascii=False))
    except:
        with io.open(channel_list_file, "r", encoding="utf-8") as f:
            channel_list = json.loads(f.read())

    addon.setSetting("data_time32", str(int(time.time())))
else:
    try:
        with io.open(app_config_file, "r", encoding="utf-8") as f:
            app_config = json.loads(f.read())
    except IOError:
        app_config = ""
    try:
        with io.open(channel_list_file, "r", encoding="utf-8") as f:
            channel_list = json.loads(f.read())
    except IOError:
        channel_list = ""


def fix_auth_date(auth):
    now = datetime.datetime.utcnow()
    _in = list(auth)
    _in.pop(len(_in) + 2 - 3 - int(str(now.year)[:2]))
    _in.pop(len(_in) + 3 - 4 - int(str(now.year)[2:]))
    # java January = 0
    _in.pop(len(_in) + 4 - 5 - (now.month - 1 + 1 + 10))
    _in.pop(len(_in) + 5 - 6 - now.day)
    return "".join(_in)


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
    wms_url = "http://135.181.2.111:8800/rbtv/token21.php"
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
    wms_url = "http://135.181.2.111:8800/cip/4c.rbt/"
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



def root():
    oGui = cGui()
    categories = channel_list.get("categories_list")
    list_items = []
    for c in categories:
        sTitle = c.get("cat_name")
        sUrl=c.get("cat_id")
        
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
        oGui.addDir(SITE_IDENTIFIER, 'list_channels', sTitle, 'turkey-free-iptv.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()




def list_channels():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat = oInputParameterHandler.getValue('siteUrl')
    
    for channel in channel_list.get("eY2hhbm5lbHNfbGlzdA=="):
        if channel.get("cat_id") == cat:
           
            
            
            #title ="Good Auth :"            ZY19uYW1l
            title = b64decode(channel.get("ZY19uYW1l")[:-1]).decode("utf-8")
            icon = b64decode(channel.get("abG9nb191cmw=")[1:]).decode("utf-8")
            sPicture = "{0}|{1}".format(icon, urlencode({"User-Agent": user_agent}))
            sUrl = channel.get("rY19pZA==")

          
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'play', title, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()

def lplay():
    
    oInputParameterHandler = cInputParameterHandler()
    c_id = oInputParameterHandler.getValue('siteUrl')
    select_list.append(c_id )
    for channel in channel_list.get("eY2hhbm5lbHNfbGlzdA=="):
        if channel.get("rY19pZA==") == c_id:
           for stream in channel.get("Qc3RyZWFtX2xpc3Q="):
               for stream in channel:
                   select_list.append(b64decode(stream.get("Bc3RyZWFtX3VybA==")[1:]))

                   
       
       
                
    
def play():
    oInputParameterHandler = cInputParameterHandler()
    c_id = oInputParameterHandler.getValue('siteUrl')
    c_id =c_id.replace('%253d','=')
    logger.info("Good  c_id :" + c_id )
    for channel in channel_list.get("eY2hhbm5lbHNfbGlzdA=="):
        if channel.get("rY19pZA==") == c_id:
            selected_channel = channel
            break

    # stream_list = selected_channel.get("Qc3RyZWFtX2xpc3Q=")
    stream_list = selected_channel.get("Qc3RyZWFtX2xpc3Q=")
    if len(stream_list) > 1:
        select_list = []
        for stream in stream_list:
            select_list.append(stream.get("quality", "0"))
        dialog = xbmcgui.Dialog()
        ret = dialog.select("Choose Stream", select_list)
        selected_stream = stream_list[ret]
    else:
        selected_stream = stream_list[0]

    if "AdG9rZW4=" in selected_stream:
        if b64decode(selected_stream.get("AdG9rZW4=")[:-1]).decode("utf-8")  == "38":
            resolved_stream = b64decode(selected_stream.get("Bc3RyZWFtX3VybA==")[1:]).decode("utf-8")  + get_auth_token_38()
        elif b64decode(selected_stream.get("AdG9rZW4=")[:-1]).decode("utf-8")  == "21":
            resolved_stream =  b64decode(selected_stream.get("Bc3RyZWFtX3VybA==")[1:]).decode("utf-8")  + get_auth_token_21()
        elif b64decode(selected_stream.get("AdG9rZW4=")[:-1]).decode("utf-8")  == "48":
            resolved_stream =  b64decode(selected_stream.get("Bc3RyZWFtX3VybA==")[1:]).decode("utf-8")  + get_auth_token_48()
        elif b64decode(selected_stream.get("AdG9rZW4=")[:-1]).decode("utf-8")  == "0":
            resolved_stream =  b64decode(selected_stream.get("Bc3RyZWFtX3VybA==")[1:])
    else:
        resolved_stream = (
            b64decode(selected_stream.get("Bc3RyZWFtX3VybA==")[1:]).decode("utf-8"),
            {"User-Agent": user_agent},
        )

   

    title = b64decode(selected_channel.get("ZY19uYW1l")[:-1]).decode("utf-8")
    icon = b64decode(selected_channel.get("abG9nb191cmw=")[1:]).decode("utf-8")
    image = "{0}|{1}".format(icon, urlencode({"User-Agent": user_agent}))
    
    
    media_url = resolved_stream
    logger.info("Good  media_url :" + media_url  )
    media_headers = resolved_stream[1]
#    path="{0}|{1}".format(media_url, urlencode(media_headers))
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(title)
    oGuiElement.setMediaUrl(media_url)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
          
            
            