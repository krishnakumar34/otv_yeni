# -*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'livenettv'
import sys
from xbmcgui import ListItem
from kodi_six import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from routing import Plugin

import os
import json
from future.moves.urllib.parse import urlencode

from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import gettz, tzlocal
from resources.lib.logger import logger 
from resources.lib.lntv import LnTv, LiveStream

try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

addon = xbmcaddon.Addon()
user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)"
USER_DATA_DIR = translatePath(addon.getAddonInfo("profile"))
ADDON_DATA_DIR = translatePath(addon.getAddonInfo("path"))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, "resources")
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)
plugin = Plugin()
plugin.name = addon.getAddonInfo("name")

cert_file = os.path.join(RESOURCES_DIR, "com.playnet.androidtv.ads.crt")
cert_key_file = os.path.join(RESOURCES_DIR, "com.playnet.androidtv.ads.key")

mytv = LnTv(USER_DATA_DIR, cert_file, cert_key_file)


try:
    locale_timezone = json.loads(
        xbmc.executeJSONRPC(
            '{"jsonrpc": "2.0", "method": "Settings.GetSettingValue", "params": {"setting": "locale.timezone"}, "id": 1}'
        )
    )
    if "result" in locale_timezone:
        if locale_timezone["result"]["value"]:
            local_tzinfo = gettz(locale_timezone["result"]["value"])
        else:
            local_tzinfo = tzlocal()
    else:
        local_tzinfo = tzlocal()
except:
    local_tzinfo = ""


def xbmc_curl_encode(url):
    return "{0}|{1}".format(url[0], urlencode(url[1]))


def time_from_zone(timestring, newfrmt="default", in_zone="UTC"):
    try:
        if newfrmt == "default":
            newfrmt = xbmc.getRegion("time").replace(":%S", "")
        in_time = parse(timestring)
        in_time_with_timezone = in_time.replace(tzinfo=gettz(in_zone))
        local_time = in_time_with_timezone.astimezone(local_tzinfo)
        return local_time.strftime(newfrmt)
    except:
        return timestring


def root():
    mytv.update_live_channels()
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir(SITE_IDENTIFIER, 'vod', 'VOD', 'turkey-free-iptv.png', oOutputParameterHandler)
#    oOutputParameterHandler = cOutputParameterHandler()
#    oOutputParameterHandler.addParameter('siteUrl', '8')
#    oGui.addDir(SITE_IDENTIFIER, 'list_live', 'Turkish', 'turkey-free-iptv.png', oOutputParameterHandler)

    mytv.update_live_channels()
    for category in mytv.get_live_categories():
        sTitle =category.cat_name
        sUrl=category.cat_id
        

    
        oOutputParameterHandler = cOutputParameterHandler()
        
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
        oGui.addDir(SITE_IDENTIFIER, 'list_channels', sTitle, 'turkey-free-iptv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def mlist_live():
    oGui = cGui()
    live_data = mytv.get_live_events()
    for day, events in live_data.items():
       for event in events:
           if len(event["channel_list"]) == 0:
               continue
           event_time = time_from_zone(datetime.utcfromtimestamp(int(event["start"])).strftime("%c"), "%Y-%m-%d %H:%M")
           sTitle ="[{0}] {1}".format(event_time, event["title"])
           cat=category.cat_id
        

    
           oOutputParameterHandler = cOutputParameterHandler()
        
           oOutputParameterHandler.addParameter('siteUrl', cat)
           oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
           oGui.addDir(SITE_IDENTIFIER, 'vod_list', sTitle, 'turkey-free-iptv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def vod():
    oGui = cGui()
    mytv.update_vod_channels()
    for category in mytv.get_vod_categories():
        
        sTitle =category.cat_name
        cat=category.cat_id
        

    
        oOutputParameterHandler = cOutputParameterHandler()
        
        oOutputParameterHandler.addParameter('siteUrl', cat)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
        oGui.addDir(SITE_IDENTIFIER, 'vod_list', sTitle, 'turkey-free-iptv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()




def vod_list():
    mytv.update_vod_channels()
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat = oInputParameterHandler.getValue('siteUrl')
    for channel in mytv.get_vod_channels_by_category(int(cat)):
            title=channel.name
            sPicture=channel.image_path
            c_id=channel=channel.channel_id
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', c_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'play_vod', title, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
    


@plugin.route("resources/sites/livenettv/list_live")
def mlist_live():
    live_data = mytv.get_live_events()
    list_items = []
    for day, events in live_data.items():
        for event in events:
            if len(event["channel_list"]) == 0:
                continue
            event_time = time_from_zone(datetime.utcfromtimestamp(int(event["start"])).strftime("%c"), "%Y-%m-%d %H:%M")
            title = "[{0}] {1}".format(event_time, event["title"])
            li = ListItem(title, offscreen=True)
            li.setProperty("IsPlayable", "true")
            li.setInfo(type="Video", infoLabels={"Title": title, "mediatype": "video"})
            url = event_resolve( event["title"].encode("utf-8"))
            list_items.append((url, li, False))

    xbmcplugin.addSortMethod(plugin.handle, xbmcplugin.SORT_METHOD_LABEL)
    xbmcplugin.addDirectoryItems(plugin.handle, list_items)
    xbmcplugin.setContent(plugin.handle, "videos")
    xbmcplugin.endOfDirectory(plugin.handle)


@plugin.route("resources/sites/livenettv/event_resolve.pvr")
def mevent_resolve(title):
    def find_event(data, title):
        for day, events in live_data.items():
            for event in events:
                if event["title"] == title:
                    logger.info("event: %s" %    event)
                    return event

    live_data = mytv.get_live_events()

    live_event = find_event(live_data, title)
    logger.info("live_event: %s" %    live_event)
    if len(live_event["channel_list"]) > 1:
        select_list = []
        for channel in live_event["channel_list"]:
            select_list.append(channel["c_name"])
        dialog = xbmcgui.Dialog()
        ret = dialog.select("Choose Stream", select_list)
        selected_channel = live_event["channel_list"][ret]
    else:
        selected_channel = live_event["channel_list"][0]

    resolved_stream = ()
    link = selected_channel["links"][0]
    logger.info("live_event: %s" %    link)
    stream = mytv.get_live_link(link)
    new_stream = LiveStream(
        url=stream.get("link"),
        token=stream.get("token"),
        user_agent=stream.get("user_agent"),
        referer=stream.get("referer"),
        player_referer=stream.get("player_referer"),
        player_user_agent=stream.get("player_user_agent"),
    )

    resolved_stream = mytv.resolve_stream(new_stream)
    li = ListItem(path=xbmc_curl_encode(resolved_stream))
    if "playlist.m3u8" in resolved_stream[0]:
        li.setContentLookup(False)
        li.setMimeType("application/vnd.apple.mpegurl")
        if addon.getSetting("inputstream") == "true":
            if sys.version_info[0] == 2:
                li.setProperty("inputstreamaddon", "inputstream.adaptive")
            else:
                li.setProperty("inputstream", "inputstream.adaptive")
            li.setProperty("inputstream.adaptive.manifest_type", "hls")
            li.setProperty("inputstream.adaptive.stream_headers", urlencode(resolved_stream[1]))
    xbmcplugin.setResolvedUrl(plugin.handle, True, li)



@plugin.route("/list_live")
def list_live():
    oGui = cGui()
    live_data = mytv.get_live_events()
    list_items = []
    for day, events in live_data.items():
        for event in events:
            if len(event["channel_list"]) == 0:
                continue
            event_time = time_from_zone(datetime.utcfromtimestamp(int(event["start"])).strftime("%c"), "%Y-%m-%d %H:%M")
            title = "[{0}] {1}".format(event_time, event["title"])
            titl=event["title"]#.encode("utf-8")

            oOutputParameterHandler = cOutputParameterHandler()
            #oOutputParameterHandler.addParameter('siteUrl', titl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(titl))            
           
            oGui.addDir(SITE_IDENTIFIER, 'event_resolve', title, 'turkey-free-iptv.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()



@plugin.route("resources/sites/livenettv/event_resolve.pvr")
def event_resolve():
    def find_event(data, title):
        for day, events in live_data.items():
            for event in events:
                if event["title"] == title:
                    return event

    live_data = mytv.get_live_events()
    oInputParameterHandler = cInputParameterHandler()
    title = oInputParameterHandler.getValue('sMovieTitle')
    #title = str(title,'utf-8')
    logger.info("title: %s" %   title)
    live_event = find_event(live_data, title)
    logger.info("live_event: %s" %   live_event)
    if len(live_event["channel_list"]) > 1:
        select_list = []
        for channel in live_event["channel_list"]:
            select_list.append(channel["c_name"])
        dialog = xbmcgui.Dialog()
        ret = dialog.select("Choose Stream", select_list)
        selected_channel = live_event["channel_list"][ret]
    else:
        selected_channel = live_event["channel_list"][0]

    resolved_stream = ()
    link = selected_channel["links"][0]
    stream = mytv.get_live_link(link)
    new_stream = LiveStream(
        url=stream.get("link"),
        token=stream.get("token"),
        user_agent=stream.get("user_agent"),
        referer=stream.get("referer"),
        player_referer=stream.get("player_referer"),
        player_user_agent=stream.get("player_user_agent"),
    )

    resolved_stream = mytv.resolve_stream(new_stream)
#    mage =xbmc_curl_encode(resolved_stream)
    path=xbmc_curl_encode(resolved_stream)
    image = xbmc_curl_encode(resolved_stream)
    li = xbmcgui.ListItem(title)
    li.setInfo(type='video', infoLabels={'Title':title})
    li.setArt({'thumb': image, 'icon': image, 'fanart': image})
    li.setProperty('Fanart_Image', image)
    xbmc.Player().play(path,li)


def list_channels():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat = oInputParameterHandler.getValue('siteUrl')
    mytv.update_live_channels()
    for channel in mytv.get_live_channels_by_category(int(cat)):


            title = channel.name
            icon = channel.image_path
            sPicture = "{0}|{1}".format(icon, urlencode({"User-Agent": user_agent}))
            c_id = channel.channel_id

          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', c_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'play', title, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
    

@plugin.route("/play/<c_id>/play.pvr")
def play():
    oInputParameterHandler = cInputParameterHandler()
    c_id = oInputParameterHandler.getValue('siteUrl')
    mytv.update_live_channels()
    image_headers = {"User-Agent": mytv.user_agent}
    stream_list = mytv.get_streams_by_channel_id(int(c_id))
    if stream_list.count() > 1:
        select_list = []
        for stream in stream_list:
            select_list.append("Stream {0} {1}".format(stream.token, stream.stream_id))
        dialog = xbmcgui.Dialog()
        ret = dialog.select("Choose Stream", select_list)
        # if not
        selected_stream = stream_list[ret]
    else:
        selected_stream = stream_list[0]

    resolved_stream = mytv.resolve_stream(selected_stream)
    image = xbmc_curl_encode((selected_stream.livechannel.image_path, image_headers))
    title = selected_stream.livechannel.name
    
    media_url = resolved_stream[0]
    media_headers = resolved_stream[1]
    path=xbmc_curl_encode(resolved_stream) 
    liz = xbmcgui.ListItem(title)

    liz.setInfo(type='video', infoLabels={'Title':title})
    liz.setArt({'thumb': image, 'icon': image, 'fanart': image})
    liz.setProperty('Fanart_Image', image)
    xbmc.Player().play(path,liz)
@plugin.route("/play_vod")
def play_vod():
    mytv.update_vod_channels()
    
    oInputParameterHandler = cInputParameterHandler()
    c_id = oInputParameterHandler.getValue('siteUrl')
    image_headers = {"User-Agent": mytv.user_agent}
    channel = int(c_id)
    stream_list = mytv.get_vodstreams_by_channel_id(channel)
    if stream_list.count() > 1:
        select_list = []
        for stream in stream_list:
            select_list.append(stream.quality)
        dialog = xbmcgui.Dialog()
        ret = dialog.select("Choose Stream", select_list)
        # if not
        selected_stream = stream_list[ret]
    else:
        selected_stream = stream_list[0]

    resolved_stream = mytv.resolve_stream(selected_stream)
    image = xbmc_curl_encode((selected_stream.vodchannel.image_path, image_headers))
    title = selected_stream.vodchannel.name
    path=xbmc_curl_encode(resolved_stream)
    #li.setArt({"thumb": image, "icon": image})
    li = xbmcgui.ListItem(title)
    li.setInfo(type='video', infoLabels={'Title':title})
    li.setArt({'thumb': image, 'icon': image, 'fanart': image})
    li.setProperty('Fanart_Image', image)
    xbmc.Player().play(path,li)
@plugin.route("/play_vod/<c_id>/play.pvr")
def Pplay_vod():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    c_id = oInputParameterHandler.getValue('siteUrl')
    with io.open(vod_list_file, "r", encoding="utf-8") as f:
        vod_data = json.loads(f.read())

    for channel in vod_data.get("eY2hhbm5lbHNfbGlzdA=="):
        if channel.get("rY19pZA==") == c_id:
            selected_channel = channel
            break

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

    # [ "0", "21", "127"]
    if "AdG9rZW4=" in selected_stream:
        if b64decode(selected_stream.get("AdG9rZW4=")[:-1]).decode("utf-8") == "21":
            resolved_stream = new_channels.get_stream_21(selected_stream)
        elif b64decode(selected_stream.get("AdG9rZW4=")[:-1]).decode("utf-8") == "127":
            resolved_stream = new_channels.get_stream_21(selected_stream)
    else:
        resolved_stream = (
            b64decode(selected_stream.get("Bc3RyZWFtX3VybA==")[1:]).decode("utf-8"),
            {"User-Agent": user_agent},
        )

    title = b64decode(selected_channel.get("ZY19uYW1l")[:-1]).decode("utf-8")
    icon = b64decode(selected_channel.get("abG9nb191cmw=")[1:]).decode("utf-8")
    image = "{0}|{1}".format(icon, urlencode({"User-Agent": user_agent}))

    media_url = resolved_stream[0]
    media_headers = resolved_stream[1]
    path="{0}|{1}".format(media_url, urlencode(media_headers))
    liz = xbmcgui.ListItem(title)
    liz.setInfo(type='video', infoLabels={'Title':title})
    liz.setArt({'thumb': image, 'icon': image, 'fanart': image})
    liz.setProperty('Fanart_Image', image)
    xbmc.Player().play(media_url,liz)

if __name__ == "__main__":
    plugin.run(sys.argv)
