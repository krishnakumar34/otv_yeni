#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
from routing import Plugin
from requests.exceptions import RequestException
from resources.lib.swift import SwiftStream
SITE_IDENTIFIER = 'Swift'
addon = xbmcaddon.Addon()


USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo("profile"))
data_time = int(addon.getSetting("data_time") or "0")
cache_time = int(addon.getSetting("cache_time") or "0") * 60 * 60
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)
from future.moves.urllib.parse import urlencode
from resources.lib.swift import SwiftStream
from routing import Plugin
try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

addon = xbmcaddon.Addon()
plugin = Plugin()
plugin.name = addon.getAddonInfo("name")
USER_DATA_DIR = translatePath(addon.getAddonInfo("profile"))
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)
def log(msg, level=xbmc.LOGDEBUG):
    xbmc.log("[{0}] {1}".format(plugin.name, msg), level=level)

def xbmc_curl_encode(url):
    return "{0}|{1}".format(url[0], urlencode(url[1]))

TV = SwiftStream(USER_DATA_DIR)
current_time = int(time.time())
if current_time - data_time > cache_time:
    try:
        TV.update_categories()
        addon.setSetting("data_time", str(current_time))
        log("[{0}] Categories updated".format(current_time))
    except (ValueError, RequestException) as e:
        if data_time == 0:
            """ No data """
            dialog = xbmcgui.Dialog()
            dialog.notification(plugin.name, e.message, xbmcgui.NOTIFICATION_ERROR)
            xbmcplugin.endOfDirectory(plugin.handle, False)
        else:
            """ Data update failed """
            log("[{0}] Categories update fail, data age: {1}".format(current_time, data_time))
            log(e.message)


def root():
    oGui = cGui()
    for cat in TV.get_categories():
        sTitle =cat.c_name
        sPicture=cat.c_image
        url =cat.c_id
      
        sUrl=url
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
        oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
        oGui.addMovie(SITE_IDENTIFIER, 'list_channels', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    
    
    oGui.setEndOfDirectory()



def list_channels():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        cat_id = oInputParameterHandler.getValue('siteUrl')
  
        
        for channel in TV.get_category(cat_id):
            title = channel.title
            sPicture = channel.thumbnail
            sUrl =channel.c_id
            channel_id=channel._id
           
           
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('channelUrl', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'play', title, sPicture, sPicture, '', oOutputParameterHandler)
        oGui.setEndOfDirectory()



def mplay():
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    channel_id = oInputParameterHandler.getValue('channelUrl')
    mplay(cat_id, channel_id)



def pplay():
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    channel_id = oInputParameterHandler.getValue('channelUrl')
    channel = TV.get_channel_by_id(cat_id, channel_id)
    try:
        if len(channel.streams) > 1:
            dialog = xbmcgui.Dialog()
            ret = dialog.select("Choose Stream", [s.name for s in channel.streams])
            stream = channel.streams[ret]
        else:
            stream = channel.streams[0]
        media_url = TV.get_stream_link(stream)

        image = xbmc_curl_encode((channel.thumbnail, {"User-Agent": "okhttp/3.12.1"}))
        li = ListItem(channel.title, path=xbmc_curl_encode(media_url))
        li.setArt({"thumb": image, "icon": image})
        if "playlist.m3u8" in media_url[0]:
            li.setContentLookup(False)
            li.setMimeType("application/vnd.apple.mpegurl")
            if addon.getSetting("inputstream") == "true":
                if sys.version_info[0] == 2:
                    li.setProperty("inputstreamaddon", "inputstream.adaptive")
                else:
                    li.setProperty("inputstream", "inputstream.adaptive")
                li.setProperty("inputstream.adaptive.manifest_type", "hls")
                li.setProperty("inputstream.adaptive.stream_headers", urlencode(media_url[1]))
                li.setProperty("inputstream.adaptive.license_key", "|" + urlencode(media_url[1]))
        xbmcplugin.setResolvedUrl(plugin.handle, True, li)
    except (ValueError, RequestException) as e:
        log(e.message)
        dialog = xbmcgui.Dialog()
        dialog.notification(plugin.name, "Remote Server Error", xbmcgui.NOTIFICATION_ERROR)
        xbmcplugin.setResolvedUrl(plugin.handle, False, ListItem())

def play():
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    channel_id = oInputParameterHandler.getValue('channelUrl')
    channel= TV.get_channel_by_id(cat_id, channel_id)
    if len(channel.streams) > 1:
            dialog = xbmcgui.Dialog()
            ret = dialog.select("Choose Stream", [s.name for s in channel.streams])
            stream = channel.streams[ret]
    else:
            stream = channel.streams[0]
    resolved_stream = TV.get_stream_link(stream)
    image = xbmc_curl_encode((channel.thumbnail, {"User-Agent": "okhttp/3.12.1"}))
    title = channel.title
    
    media_url = resolved_stream[0]
    media_headers = resolved_stream[1]
    path="{0}|Cookie=PHPSESSID=deuvts0iqt4bnrg5k2aallje73&{1}".format(media_url, urlencode(media_headers))    
    liz = xbmcgui.ListItem(title)
    liz.setInfo(type='video', infoLabels={'Title':title})
    liz.setArt({'thumb': image, 'icon': image, 'fanart': image})
    liz.setProperty('Fanart_Image', image)
    xbmc.Player().play(path,liz)

        
        
def addLink(name, url, iconimage):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=str(url), listitem=liz)
    xbmc.Player().play(url, liz)
    sys.exit()
    return ok

