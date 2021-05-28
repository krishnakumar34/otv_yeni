#-*- coding: utf-8 -*-
import urllib2, urllib,cookielib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
from resources.lib.otvhelper import  gegetUrl,getUrl ,alfabekodla
from resources.lib.config import cConfig
import requests
import re,xbmcgui,unicodedata              
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import Parser as cParser
from resources.lib.comaddon import progress, VSlog
from resources.lib.player import cPlayer

from resources.lib.gui.guiElement import cGuiElement



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
SPORTS ='https://dl.dropboxusercontent.com/s/k2jz15prgor015u/dcc12.html'

import httplib,itertools
def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)

import threading
SITE_IDENTIFIER = 'liveonlinetv247'
SITE_NAME = 'liveonlinetv247'
s = requests.Session()
user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)"
SITE_DESC = 'Replay TV'
UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69'    
Player_User_Agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
SPORT_SPORTS = (True, 'liveonlinetv247')
def _downloadUrl(url):
        headers = {'User-Agent': UA ,
                   #'Host' : 'hqq.tv',
                   'Referer': 'https://ajanspor7.tv',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   #'Accept-Encoding':'gzip, deflate, br',
                   #'Content-Type': 'text/html; charset=utf-8'
                   }
        
        req = urllib2.Request(url,None,headers)

        response = urllib2.urlopen(req)
        html = response.read()
        response.close()

        return  html

def idle():

    if float(xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')[:4]) > 17.6:
        xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
    else:
        xbmc.executebuiltin('Dialog.Close(busydialog)')


def busy():

    if float(xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')[:4]) > 17.6:
        xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    else:
        xbmc.executebuiltin('ActivateWindow(busydialog)')

def sport356Thread(url):
    import ssport365 as s
    from time import gmtime, strftime
    href,headers=url.split('|')
    header={}
    header['Referer']=urllib.unquote(re.compile('Referer=(.*?)&').findall(headers)[0])
    header['User-Agent']=urllib.unquote(re.compile('User-Agent=(.*?)&').findall(headers)[0])
    header['Origin']='http://h5.adshell.net'
    header['If-Modified-Since']=strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    header['Connection']='keep-alive'
    header['etag']='"5820cda8-2b9"'
    print '#'*25
    print '#'*25
    xbmc.sleep(2000)    # speep
    player = xbmc.Player()
    player.pause()
    print 'sport356Thread: passed url: [%s] '%href
    #print header
    h=header
    while player.isPlaying():
        print 'sport356Thread: KODI IS PLAYING, sleeping 1s'
        a,hret=s.getUrlrh(href,header=header)
        header['etag'] = hret.get('etag','')
        header['date'] = hret.get('date','')
       
        #h.update(header)
        print a,hret
        xbmc.sleep(1000)
    print 'sport356Thread: KODI STOPPED, OUTSIDE WHILE LOOP ... EXITING'

def TurkishTV ( s ) :
 kem = [ s [ HEM : HEM + 3 ] for HEM in range ( 0 , len ( s ) , 3 ) ]
 return '' . join ( chr ( int ( val ) ) for val in kem )
def sport356Thread2(url,header):
    import ssport365 as s
    import re
    
    player = xbmc.Player()
    xbmc.sleep(2000)    # speep
    print 'sport356Thread: passed url: [%s] '%url
    #print header
    player.pause()
    
    while player.isPlaying():
        print 'sport356Thread: KODI IS PLAYING, sleeping 4s'
        a,c=s.getUrlc(url,header=header,useCookies=True)
        banner =  re.compile('url:["\'](.*?)[\'"]').findall(a)[0]
        xbmc.log(banner)
        xbmc.sleep(2000)
        s.getUrlc(banner)
        xbmc.sleep(2000)
    print 'sport356Thread: KODI STOPED, OUTSIDE WHILE LOOP ... EXITING'
def MediaHeaders(chann,cookie,ref):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                                    
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'Cookie':cookie,'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4; Nexus 7 Build/KRT16M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Safari/537.36','Referer':ref ,'X-Requested-With': 'ShockwaveFlash/27.0.0.183',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann  

def mediaHeaders(chann,ref):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)','Referer':ref ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann  


 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

def Sport():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/') 
    oGui.addDir(SITE_IDENTIFIER, 'sporHosters', 'SPOR TV Türk', 'sport.jpg', oOutputParameterHandler) 
    
    #rajout listage film nouveauté   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir('sport365', 'mainlist', 'sport365', 'Sport_365_logo.png', oOutputParameterHandler)
  
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'ssport365', 'sport365 Schedule new', 'Sport_365_logo.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '1')
    oGui.addDir('LIVETV', 'list_channels', 'LIVE SPORT TV_int', 'sport.jpg', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir('livescore', 'futbolozet', 'WORLD FUTBOOL Live Scores  Özet', 'sport.jpg', oOutputParameterHandler)
            
    oGui.setEndOfDirectory()




def ssport365():
    oGui = cGui()
    import ssport365 as s
    items = s.getChannels()                
    for one in items:        
            
            surl =one['url']
            sTitle = one.get('title','')
            sTitle = alfabekodla(sTitle)
            img = 'https://upload.wikimedia.org/wikipedia/fr/9/9f/Sport_365_logo_2012.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('Url', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            if  'NSFW'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'pincode', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Scores'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'mainlist', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Schedule'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'schedulelivemobiletv247', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'More Channels'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'MoreChannels', sTitle, '',img, '', oOutputParameterHandler)        

            else:
               oGui.addTV(SITE_IDENTIFIER, 'playssport365', sTitle, '',img, '', oOutputParameterHandler)
       
        
    oGui.setEndOfDirectory()   

def sssport365():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ex_link = oInputParameterHandler.getValue('siteUrl')
    link = oInputParameterHandler.getValue('Url')
    import ssport365 as s
    items = s.getStreams(ex_link)                
    for one in items: 
            url =one['url']
            sTitle = one.get('title')
            sTitle = alfabekodla(sTitle)
            key = one.get('key')
            stream_url = s.getChannelVideo(url,key)
            thread = threading.Thread(name='sport356Thread', target = sport356Thread2, args=[url,header])
            thread.start()
            img = 'https://upload.wikimedia.org/wikipedia/fr/9/9f/Sport_365_logo_2012.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', one)
            oOutputParameterHandler.addParameter('Url', stream_url)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            if  'NSFW'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'pincode', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Scores'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'mainlist', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Schedule'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'schedulelivemobiletv247', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'More Channels'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'MoreChannels', sTitle, '',img, '', oOutputParameterHandler)        

            else:
               oGui.addTV(SITE_IDENTIFIER, 'playssport365', sTitle, '',img, '', oOutputParameterHandler)
       
        
    oGui.setEndOfDirectory()   
def playssport365():
    oInputParameterHandler = cInputParameterHandler()
    ex_link = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle') 
    import ssport365 as mod
    streams = mod.getStreams(ex_link)
    if streams:
      t = [stream.get('title') for stream in streams]
      s = xbmcgui.Dialog().select("Stream", t)
      if s>-1: stream_url,url,header = mod.getChannelVideo(streams[s])
      else: stream_url=''
      stream_url = stream_url.replace('/i', '/master.m3u8')
      if stream_url:
        liz = xbmcgui.ListItem(label=sTitle)
        liz.setArt({"fanart": FANART, "icon": ICON})
        liz.setInfo(type="Video", infoLabels={"title": sTitle})
        liz.setProperty("IsPlayable", "true")
        idle()
        if my_addon.getSetting('play') == 'Inputstream':
            stream_url = stream_url.replace('/i', '/master.m3u8')
            liz.setPath(stream_url)
            if float(xbmc.getInfoLabel('System.BuildVersion')[0:4]) >= 17.5:
                liz.setMimeType('application/vnd.apple.mpegurl')
                liz.setProperty('inputstream.adaptive.manifest_type', 'hls')
                liz.setProperty('inputstream.adaptive.stream_headers', str(header))
            else:
                liz.setProperty('inputstreamaddon', None)
                liz.setContentLookup(True)


            try:
                import threading
                thread = threading.Thread(name='sport356Thread', target=sport356Thread2, args=[url, header])
                thread.start()
                #xbmc.Player().play(stream_url, liz)
                #addLinkItem(orig_title, stream_url, '', '', ICON, liz, True, FANART)
                ok = xbmcplugin.setResolvedUrl(addon_handle, False, liz)
                #ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream_url, listitem=liz, isFolder=False)
                return ok
            except BaseException:
                pass

        elif my_addon.getSetting('play') == 'Streamlink':
            # stream_url = 'hls://' + stream_url.replace('/i', '/master.m3u8')
            import streamlink.session
            session = streamlink.session.Streamlink()
            stream_url, hdrs = stream_url.split('|')
            stream_url = 'hls://' + stream_url.replace('/i', '/master.m3u8')
            hdrs += '&Origin=http://h5.adshell.net'
            session.set_option("http-headers", hdrs)

            streams = session.streams(stream_url)
            stream_url = streams['best'].to_url() + '|' + hdrs

            liz.setPath(stream_url)
            idle()
            ok = xbmcplugin.setResolvedUrl(addon_handle, False, liz)
            return ok

        else:
            stream_url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&url={0}&name={1}'.format(
                urllib.quote_plus(stream_url), urllib.quote_plus(sTitle))
            liz.setPath(stream_url)
            idle()
            try:
                xbmc.executebuiltin('RunPlugin(' + stream_url + ')')
            except BaseException:
                pass

        # xbmcplugin.setResolvedUrl(addon_handle, False, liz)
    else:
        xbmcgui.Dialog().ok("Sorry for that", 'plz contact Dev')


def f4mTest(name,url):
    from resources.lib.hlsplayer import hlsproxy
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    xbmc.sleep(2000)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played

def livemobiletv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = url_all_products
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('\/','/')                                                                                                   
    oParser = cParser()
    sPattern = '"id":"(.*?)","category":"(.*?)","channel_name":"(.*?)","channel_link":"(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            id =aEntry[0]
            surl =aEntry[3]
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://pic.accessify.com/thumbnails/777x423/l/liveonlinetv247.com.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            if  'NSFW'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'pincode', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Scores'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'mainlist', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Schedule'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'schedulelivemobiletv247', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'More Channels'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'MoreChannels', sTitle, '',img, '', oOutputParameterHandler)        

            else:
               oGui.addTV(SITE_IDENTIFIER, 'HOSTlivemobiletv247', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()   
def MoreChannels():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                
    oParser = cParser()
    sPattern = '<li><a href="(.*?php)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            sTitle = aEntry[1]
          
            
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDir(SITE_IDENTIFIER, 'MoreMoreChannels', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def schedulelivemobiletv247():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                 
    oParser = cParser()
    sPattern = 'datetime="(.*?)">(.*?)</time>.*?<div class="entry-content">.*?<p>(.*?)<a href="(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[3]
            sTitle = aEntry[2]+ ' :'+ 'Schedule Timezone: Europe/London :'+ aEntry[0]+ ' :'+ aEntry[1] 
            img ='http://pic.accessify.com/thumbnails/777x423/l/liveonlinetv247.com.png'
            
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDir(SITE_IDENTIFIER, 'play__liveonlinetv24', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def MoreMoreChannels():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                
    oParser = cParser()
    sPattern = '<li><a href="(.*?php)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            sTitle = aEntry[1]
          
            
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDir(SITE_IDENTIFIER, 'HOSTlivemobiletv247', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def HOSTlivemobiletv247():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':sUrl, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    sHtmlContent = requests.get(sUrl, headers = headers).text
    
                 
    oParser = cParser()
    sPattern = '<li><a target="_top" href="(.*?)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            img ='http://pic.accessify.com/thumbnails/777x423/l/liveonlinetv247.com.png'
            sTitle = aEntry[1]
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__livemobiletv247', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()

def play__livemobiletv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    name = alfabekodla(sTitle)
    
                              
                     
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':Url, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    url = requests.get(Url, headers = headers).text               
#    url = re.findall('src=.*[",\'](.*m3u8.*?)[",\']', data, re.S)[0]#+'|User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'  
#    url =url.replace('vlc://','')+'|Referer='+Url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')    
def lvegoltv2():    
     
    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played      
def vegoltv2():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '<div class="active in tab-pane" id="t-5-7-24-tv">(.+?)</tbody'
               
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                 
    oParser = cParser()
    sPattern = '<td><a href="(.*?)" title="(.*?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl ='http://vegoltv2.com'+ aEntry[0]
            img ='http://vegoltv2.com/wp-content/uploads/2017/08/vegoltv-logo.png'
            sTitle = aEntry[1]
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__vegoltv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def play__vegoltv2():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    urla  = "http://vegoltv2.com/"
    name = oInputParameterHandler.getValue('sMovieTitle')                  
    referer=[('Referer',urla)]
    datam=gegetUrl(sUrl,headers=referer) 
  
    sUrll= re.findall('<iframe allowfullscreen class="embed-responsive-item" src="(.*?)"></iframe>', datam, re.S)[0]   
    sUrlkk='http://vegoltv2.com'+ sUrll 
    tam=gegetUrl(sUrlkk,headers=referer)     
    url= re.findall('poster:".*?",source:"(.*?)"', tam, re.S)[0]
    url =url+'|Referer='+sUrlkk+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    
    
   
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')


def betexpertv():
    oGui = cGui()
    liste = []
    liste.append( ['7/24 Canli TV','item live'] )
    liste.append( ['FUTBOL','item football'] )
    liste.append( ['BASKETBOL','item basketball'] )
    liste.append( ['TENIS','item tennis'] )
    for sTitle,sUrl2 in liste:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == '7/24 Canli TV':
             oGui.addDir(SITE_IDENTIFIER, 'betexpertv3',sTitle, 'genres.png', oOutputParameterHandler)
        else:
             oGui.addDir(SITE_IDENTIFIER, 'betexpertv2', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def golnettv():
    oGui = cGui()
    liste = []
    liste.append( ['7/24 Canli TV','item live'] )
    liste.append( ['FUTBOL','item football'] )
    liste.append( ['BASKETBOL','item basketball'] )
    liste.append( ['TENIS','item tennis'] )
    for sTitle,sUrl2 in liste:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == '7/24 Canli TV':
             oGui.addDir(SITE_IDENTIFIER, 'golnettv3',sTitle, 'genres.png', oOutputParameterHandler)
        else:
             oGui.addDir(SITE_IDENTIFIER, 'golnettv2', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def laklak(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku  
def betexpertv3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.betexpertv.com/'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="live">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.betexpertv.com/assets/uploads/settings/main_logo_739.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__betexpertv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()     
def betexpertv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.betexpertv.com/'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="time">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                              
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.betexpertv.com/assets/uploads/settings/main_logo_739.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__betexpertv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def play__betexpertv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urlk='http://www.betexpertv.com/'
    Urll='http://www.betexpertv.com/tr/izle/'+ Url
    referer=[('Referer',Urlk)]
    adata=gegetUrl(Urll,headers=referer) 
    fida= re.findall('<iframe src="(.*?)"',adata, re.S)[0]
                    
    referer=[('Referer',fida)]
    adat=gegetUrl(fida,headers=referer) 
    if not 'eval' in adat:
        sUrl="http://www.betexpertv.com/assets/images/nosignal.jpg"
    fid= re.findall('eval.atob."(.*?)"',adat, re.S)[0]
    
    bit=base64.b64decode(fid)     
   
    sUrlk = re.findall('poster:".*?",source:"(.*?)"',bit, re.S)[0]   
    sUrl =sUrlk+'|Referer='+Urll+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()

def golnettv3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.golnet.tv/tr/izle/bein-sport-2'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="live">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.golnet.tv/assets/uploads/settings/main_logo_660.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__golnettv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()     
def golnettv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.golnet.tv/tr/izle/bein-sport-2'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="time">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                              
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.golnet.tv/assets/uploads/settings/main_logo_660.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__golnettv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def play__golnettv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urlk='http://www.golnet2.tv/'
    
    Urll='http://www.golnet2.tv/tr/izle/'+ Url
    referer=[('Referer',Urlk)]
    adata=gegetUrl(Urll,headers=referer) 
    fida= re.findall('<iframe src="(.*?)"',adata, re.S)[0]
                    
    referer=[('Referer',fida)]
    adat=gegetUrl(fida,headers=referer) 
    if not 'eval' in adat:
        sUrl="http://www.golnet.tv/assets/images/nosignal.jpg"
    fid= re.findall('eval.atob."(.*?)"',adat, re.S)[0]
    bit=base64.b64decode(fid)     
                           
    sUrlk = re.findall('source:"(https://.*?.tvcdn.co/live/.*?/index.m3u8.*?)"',bit, re.S)[0]   
    sUrl =sUrlk+'|Referer='+fida+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  


def showsport():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi.com/')
    oGui.addDir(SITE_IDENTIFIER, 'showsportSchedule', 'Schedule', 'genres.png', oOutputParameterHandler)

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()                          
    sPattern = '<a href="(/channel/watch.*?)"><img width="120" title="(.*?)" src="(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl ='http://showsport-tv.com'+ aEntry[0]
            img ='http://showsport-tv.com'+ aEntry[2]
            sTitle = aEntry[1]
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'pplay__showsport', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def showsportSchedule():
    oGui = cGui()
         
    Urlo = "http://showsport-tv.com/" 
    oRequestHandler = cRequestHandler(Urlo )
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =sHtmlContent.replace('<div class="startdate date"','<img src="/img/Sonra.gif">')
    oParser = cParser()
    sPattern = '<div class="table-responsive">(.*?)</table>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult

                                                             
    sPattern = '<img width="20" title=".*?" src="(.*?)".*?class="time">(.*?)</span>.*?<td width="20"><a class="btn btn-success btn-xs" href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):                                     
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sThumbnail= "http://showsport-tv.com" +aEntry[0]
            Url="http://showsport-tv.com" +aEntry[2]
                                
            name= re.findall('/live/(.*?).html',aEntry[2])[0]
            sTitle = "%s - %s" %(name,aEntry[1]) 
            
            sTitle = alfabekodla(sTitle)
            if "live" in sTitle:
               sTitle =  '[COLOR  lime]'+sTitle+'[/COLOR]'
               sThumbnail= "http://mareeg.com/wp-content/uploads/2017/02/LIVE.png"
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Url))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'pplay__showsport',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()



def pplay__showsport():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    urla  = "http://showsport-tv.com/"
    referer=[('Referer',urla)]
    datam=gegetUrl(sUrl,headers=referer) 
    sUrll=re.findall('<div id="ch_box" class="tab-content">.*?<iframe src="(/embedplayer.php.*?)&server=.*?"', datam, re.S)[0]   
    urll='http://showsport-tv.com'+ sUrll                                            
        
      
    liste = []
    liste.append( ['Server 1',urll+'&server=1'] )
    liste.append( ['Server 2',urll+'&server=2'] )
   
    for sTitle,sUrl2 in liste:
        sTitle = alfabekodla(sTitle)   
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Server 2':
             oGui.addDir(SITE_IDENTIFIER, 'playshowsport',sTitle, 'genres.png', oOutputParameterHandler)
        else:
             oGui.addDir(SITE_IDENTIFIER, 'play__showsport', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
def playshowsport():
    oGui = cGui()
              
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    name = oInputParameterHandler.getValue('sMovieTitle')  
    name = alfabekodla(name)
    urla  = "http://showsport-tv.com/"
    referer=[('Referer',urla)]
    tam=requests.get(sUrl,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04','Referer':sUrl,'Accept':'/*','Connection':'keep-alive'}).text
   
    Urll= re.findall("<script type='text/javascript'>id='(.*?)'", tam, re.S)[0]
    ref='http://bro.adca.st/stream.php?id='+ Urll    
    data=gegetUrl(ref,headers=referer)  
    tokenLink = re.findall('fass = "(.*?)"', data, re.S)[0]
    if  'token2.php' in tokenLink: 
          Link = re.findall('trap2 = "(.*?)"', data, re.S)[0] 
    
    if  'token.php' in tokenLink:
          Link = re.findall('trap = "(.*?)"', data, re.S)[0] 
    
    
    tokenurl='http://bro.adca.st/'+tokenLink+'?id='+ Urll 
    urlan=gegetUrl(tokenurl,headers=referer) 
    token = re.findall('"rumba":"(.*?)"',urlan, re.S)[0]
    
    
    
    urll = base64.b64decode(Link)
    sUrlkk  =mediaHeaders(urll,ref)
    url =sUrlkk+token+'|Referer='+ref+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
     

    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played

def play__showsport():
    oGui = cGui()
              
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    name = oInputParameterHandler.getValue('sMovieTitle')  
    name = alfabekodla(name)
    urla  = "http://showsport-tv.com/"
    referer=[('Referer',urla)]
    tam=requests.get(sUrl,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04','Referer':sUrl,'Accept':'/*','Connection':'keep-alive'}).text
   
    Urll= re.findall("<script type='text/javascript'>id='(.*?)'", tam, re.S)[0]
    ref='http://www.allcast.is/stream.php?id='+ Urll    
    data=gegetUrl(ref,headers=referer)  
                  
    Link = re.findall('curl = "(.*?)"', data, re.S)[0] 
    urll = base64.b64decode(Link)
    sUrlkk  =mediaHeaders(urll,ref)
    url =sUrlkk+'|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    

    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played

def liveonlinetv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://www.liveonlinetv247.info/tvchannels.php'
    sOrder = oInputParameterHandler.getValue('sOrder')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                  
    oParser = cParser()
    sPattern = '<li><a href="(/watch.*?)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            sTitle = aEntry[1].replace('<b>','')
            surl ='http://www.liveonlinetv247.info'+ aEntry[0]
            surl =surl.replace(' ','%20')
            sDisplayTitle = cUtil().DecoTitle(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDirectTV(SITE_IDENTIFIER, 'play__liveonlinetv24', sDisplayTitle, 'libretv.png' , '', oOutputParameterHandler)    
        
        cConfig().finishDialog(dialog)
        
        oGui.setEndOfDirectory()

def play__liveonlinetv24():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    name = alfabekodla(sTitle)
    
                              
 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':urll, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    datam = requests.get(urll, headers = headers).text
    Ur= re.findall('target="_blank" style="color:white">.*?<a href="(http://www.liveonlinetv247.info/.*?.php)"', datam, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer': Ur, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    tam = requests.get(Ur, headers = headers).text
    Url= re.findall('<p><iframe src="(.*?)"', tam, re.S)[0]
                    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':Url, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    data = requests.get(Url, headers = headers).text               
    urll = re.findall('src=.*[",\'](.*m3u8.*?)[",\']', data, re.S)[0]  
    sUrlkk  =mediaHeaders(urll,Url)
    url =sUrlkk+'|Referer='+Url+'&User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'
    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played
class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 



def _m3u8Exit(self):
     import otv_kuresel
     otv_kuresel.yt_tmp_storage_dirty = True    


    
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="film_part">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?.html.*?)"><span>(.*?)</span></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = alfabekodla(aEntry[1])

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'streams', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
    
def sshowBox5():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
                                               
        
    resp = net.http_GET(url)
    data = resp.content	                
    data =data.replace('\n','')
    channels = re.findall('<video controls height="480" width="650" src="(.*?)"', data, re.S)                                    
    for sUrl in channels:              
	                                                                           
                        
            sThumbnail ='http://www.liveonlinetv247.info/images/livesports.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showotvplayer', sTitle, '', sThumbnail, '', oOutputParameterHandler)

       

    oGui.setEndOfDirectory()
 
def sporHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sHtmlContent= cRequestHandler(SPORTS).request()
    
    oParser = cParser()
    sPattern = '<div class="spor">(.+?)<div class="sporson">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="resent-grid-img recommended-grid-img"><a href="(.*?)" title="(.*?)"><img src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = alfabekodla(aEntry[1])
            Thumbnail =aEntry[2]
            if not 'http' in Thumbnail:
                 Thumbnail ='https://www.izletv1.tk/'+ Thumbnail
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            if  'playlist.m3u8' in aEntry[0]:
                 oGui.addTV(SITE_IDENTIFIER, 'playplaylist', sTitle, '', Thumbnail, '', oOutputParameterHandler)
       
            else:

                 oGui.addTV(SITE_IDENTIFIER, 'play__tvizle', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def fix_auth_date(auth):
    now = datetime.datetime.utcnow()
    _in = list(auth)
    _in.pop(len(_in) + 2 - 3 - int(str(now.year)[:2]))
    _in.pop(len(_in) + 3 - 4 - int(str(now.year)[2:]))
    # java January = 0
    _in.pop(len(_in) + 4 - 5 - (now.month - 1 + 1 + 10))
    _in.pop(len(_in) + 5 - 6 - now.day)
    return "".join(_in)
              
def getauthtoken():
    wms_url = "http://163.172.181.152:8030/rbtv/token21.php"
    auth = "Basic QFN3aWZ0MTIjOkBTd2lmdDEyIw=="
    mod_value = int("6154838")
    modified = lambda value: "".join(chain(*zip(str(int(time.time()) ^ value), "0123456789")))
#    fix_auth = lambda auth: "".join([auth[:-59], auth[-58:-52], auth[-51:-43], auth[-42:-34], auth[-33:]])
    req = requests.Request(
        "GET", wms_url, headers={"User-Agent": user_agent, "Accept-Encoding": "gzip", "Modified": modified(mod_value), "Authorization": auth}
    )
    prq = req.prepare()
    r = s.send(prq)
    return r.text
def playplaylist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    name= oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
#    urll='http://51.15.209.90:8800/fio/3b.rbt/'
    der = '|User-Agent=stagefright/1.2 (Linux;Android 4.4.2)'
#    headers = {'Authorization': 'eWFyYXBuYWthYW1rYXJvOnR1bmduYWtpYWthcm8='}
#    Html= requests.get(urll, headers = headers).text
    url=sUrl+ getauthtoken() +der
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')


def turktvHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(SPORTS)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="turktv">(.*?)<div class="turktvson">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="resent-grid-img recommended-grid-img"><a href="(.*?)" title="(.*?)"><img src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = alfabekodla(aEntry[1])
            Thumbnail =aEntry[2]
            if not 'http' in Thumbnail:
                 Thumbnail ='https://www.izletv.us/'+ Thumbnail
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            if  '%3d%3dw' in aEntry[0]:
                 oGui.addTV(SITE_IDENTIFIER, 'play', sTitle, '', Thumbnail, '', oOutputParameterHandler)
       
            else:

                 oGui.addTV(SITE_IDENTIFIER, 'play__tvizle', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
from LINETV import LINETV2list
from LIVETV import list_channels
def Almanlivestream(): #affiche les genres
    oGui = cGui()              
    tarzlistesi= []                
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '25')
    oGui.addDir(SITE_IDENTIFIER, 'list_channels', 'Sky_Deutschland', 'genres.png', oOutputParameterHandler) 
   
    tarzlistesi.append(("Deutsche TV new", "26", "http://swiftstreamz.com/SwiftPanel/images/77155_germany.jpg"))
#    tarzlistesi.append(("Sky_Deutschland", "23", "https://upload.wikimedia.org/wikipedia/de/f/f4/Sky_Deutschland.png"))
    tarzlistesi.append(("Deutsche TV 4K ", "http://tv.kostenloshdtv.com/10691", "http://www.kostenloshdtv.com/wp-content/uploads/2017/09/rtl-144x96.png"))
    
    for sTitle,sUrl,sPicture in tarzlistesi:
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == 'Sky_Deutschland':
            oGui.addMovie(SITE_IDENTIFIER, 'list_channels', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Deutsche TV new':
            oGui.addMovie('Swift', 'list_channels', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        else:
            oGui.addMovie(SITE_IDENTIFIER, 'livestreamtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()
def livestreamtv():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'https://gitlab.com/aosconfig/channel-data/raw/master/world-iptv/data/German.json?incat=German'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
#    sPattern = 'class="list-group sidebarActive">(.+?)<div id="sidenavTwitter"'
#    aResult = oParser.parse(sHtmlContent, sPattern)
#    sHtmlContent = aResult                                
    
    sPattern = '"link":"(.*?)".*?"link_name":"(.*?)"'
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()                                                               
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = alfabekodla(aEntry[1])
                                               
            sPicture = 'https://www.aostv.me/wp-content/uploads/2019/03/aos-tv-logo.png'
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
                
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'livesPL', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
         
    oGui.setEndOfDirectory()
def livesPL():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
#    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    
    url =Url+ '|User-Agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; LGLS992 Build/MMB29M)'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
  
from resources.lib import  unwise    
def PLAYlivestreamtv():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    
                                
    dat= requests.get(Url).content
                  
    urll = re.findall('<iframe src="(.*?)"',dat, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36','Referer': referer  }
    urlm= requests.get(urll, headers = headers).text
    urlm=urlm.replace('\r',"").replace('\s',"").replace('\n',"").replace(';eval',"eval").replace(';</script>',"</script>")
                                                                     
    
    TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'

    urlh = re.findall('<script type="text/javascript">(eval.function.w,i,s,e.*?)</script>',urlm, re.S)[0]                       
       
    urlk =unwise.unwise_process(urlh) 
    urlk = urlk.replace('//',"").replace('\r',"").replace('\s',"").replace('\n',"").replace('; eval',"eval")
    urln = re.findall('(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))',urlk, re.S)[0]                       
    
    urlw =  cPacker().unpack(urln)
    urlw = urlw.replace('\\',"")
    baseUrl = re.findall('baseUrl:"(.*?)"',urlw, re.S)[0] 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25&Referer='+referer
            
    url = re.findall("source:'(.*?)'",urlw, re.S)[0]
    url = url.replace('https:',"https://").replace('http:',"http://")
    cookie = getUrl(urll, output='cookie').result 
    if url.find('akamaihd') > -1:      
         url =url +'|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&X-Forwarded-For=62.75.128.93' 
    else:
         url =url+ '|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&Referer='+ urll
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')

def SkyDeutschland():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'https://www.tata.to/channels'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()                         
                                                                                     
    sPattern = '<div class="ml-item-content">.*?<a href="https://www.tata.to/channel/(.*?)" class="ml-image">.*?<img src="(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl ='https://www.tata.to/channel/'+aEntry[0]    
                                                              
            img = aEntry[1]
            sTitle = aEntry[0]
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumbnail', str(img))
            oGui.addTV(SITE_IDENTIFIER, 'PLAYSkyDeutschland', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory() 
         
def PLAYSkyDeutschland():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    ref = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Thumbnail = oInputParameterHandler.getValue('sThumbnail')                                                                                       
    url='https://www.tata.to/'                                                                                                                                    
    cookie = getUrl(url, output='cookie').result
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','Referer': url }
    dat = requests.get(Url, headers = headers).text                                  
    oRequestHandler = cRequestHandler(Url)
    dat = oRequestHandler.request()
    chann=re.findall('<div class="tv-play" data-src="(.*?)"', dat, re.S)[0]                                    
    chann =chann.replace('embed.html','playlist.m3u8')#.replace('dvr=false&','')
    oRequestHandler = cRequestHandler(chann)
    data = oRequestHandler.request()
    status= urlencode(headers)      
#    referer=[('Referer',Url)]
#    data=gegetUrl(chann,headers=referer) 
    urlm= re.findall('#EXT-X-STREAM-INF:RESOLUTION=.*?,FRAME-RATE=.*?,AVERAGE-BANDWIDTH=.*?,BANDWIDTH=.*?\n(.*?)\n',data, re.S)[0] 
    channels = re.findall('https://(.*?)/playlist.m3u8.*?', chann, re.S)[0] 
    url ='https://'+channels+'/'+urlm +'|'+status                 
#    sUrlkk  =mediaHeaders(urll,Url)
   
#    status =status.replace('index.m3u8','status.json')
#    urlm= re.findall('#EXT-X-STREAM-INF:RESOLUTION=.*?,FRAME-RATE=.*?,CODECS=".*?",BANDWIDTH=.*?,CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)[0] 
#    channels = re.findall('https://(.*?)/index.m3u8.*?', chann, re.S)[0] 
#    url =dat+'|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'            
    
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 
        
class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 



def _m3u8Exit(self):
     import otv_kuresel
     otv_kuresel.yt_tmp_storage_dirty = True                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok
def almantvHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
#    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl="http://www.pro7livestream.com/rnf/"
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="filmborder">(.*?)<div class="bireklam4">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="moviefilm">.*?<img src="(.*?)" alt="(.*?)".*?<div class="movief"><a href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = alfabekodla(aEntry[1])
            Thumbnail =aEntry[0]
          
            
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', aEntry[2])
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            if  'kostenlos' in aEntry[0]:
                 oGui.addTV(SITE_IDENTIFIER, 'play__kostenlos', sTitle, '', Thumbnail, '', oOutputParameterHandler)
            elif  'live-stream.tv' in aEntry[0]:
                 oGui.addTV(SITE_IDENTIFIER, 'PLAYlivestreamtv', sTitle, '', Thumbnail, '', oOutputParameterHandler)

            else:

                 oGui.addTV(SITE_IDENTIFIER, 'play__kostenlos', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def play__kostenlos():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
   
       
       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','Referer': sUrl }
    dat = requests.get(sUrl, headers = headers).text
    if re.search('var player = new Clappr.Player' , dat): 
         sUrlm = re.findall("source: '(http.*?)'", dat, re.S)[0]
    else:     
         Urll = re.findall('<p><iframe src="(http.*?.php)"', dat, re.S)[0]
         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','Referer': sUrl }
         datt = requests.get(Urll, headers = headers).text
         sUrlm = re.findall('file: "(.*?)"', datt, re.S)[0]
        
         
         
       
               
    name = alfabekodla(name)
    
    
   
    
#    headers = {'Referer':sUrl,'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)', 'Upgrade-Insecure-Requests': '1'}
    
       
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' }
   
    url =sUrlm +'|' +urlencode(header)  
    
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok                               
def amddLink(name,url,iconimage):

    sterUrl = re.findall('https://(.*?.webhdiptv.com)/.*?', chann, re.S)[0]
    TIK='|Host='+sterUrl+'&Range=bytes=0-&Referer='+sUrl+'&User-Agent=Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13' 
    
    linka =mediaHeaders(chann)        
    url  =linka +TIK             
            
     

    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played

class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 



def adultHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(SPORTS)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="adult">(.+?)<div class="adultson">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="resent-grid-img recommended-grid-img"><a href="(.*?)" title="(.*?)"><img src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = alfabekodla(aEntry[1])
            Thumbnail ='https://www.ulantv.com/'+ aEntry[2]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'play__tvizle', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def Turkish():
	oGui = cGui()
        ata='https://addoncloud.org/ukturk/UKTurk/TurkishTV.txt'
	ta = HTTPKIR(ata)
        link= TurkishTV(ta)
	 
        link =link.replace('sportsdevil','link')
        
        
	
	
	
	
	
	
	         

	imgArray=[]
	nameArray=[]


	serverArray=[]
	

	
	


	name=(re.compile('<title>(.+?)</title>').findall(link))	
	for itemName in name: 
		nameArray.append(itemName) 
	serverchannel=(re.compile('<link>(.+?)</link>').findall(link))	
	for itemserver in serverchannel: 
		serverArray.append(itemserver) 
	
	
        image=(re.compile('<thumbnail>(.+?)</thumbnail>').findall(link))
	for itemsImg in  image:

		imgArray.append(itemsImg) 
	
        for (names,server) in itertools.izip (nameArray,serverArray):	
	


    
    

		oOutputParameterHandler = cOutputParameterHandler()
		oOutputParameterHandler.addParameter('siteUrl', str(server))
		oOutputParameterHandler.addParameter('sMovieTitle', str(names))
		oOutputParameterHandler.addParameter('sThumbnail', str(itemsImg))
		oGui.addTV(SITE_IDENTIFIER, 'otvplay__',names, '', itemsImg, '', oOutputParameterHandler)

	oGui.setEndOfDirectory()



def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok    

def play__tvizle():
    oGui = cGui()
    gerutl= 'https://www.izletv2.tk/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36','Upgrade-Insecure-Requests': '1'}
    datam = cRequestHandler(gerutl).request()
    festurl = re.findall('<link rel="canonical" href="(.*?)"', datam, re.S)[0]
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url= 'https://www.izletv2.tk'
    lka= 'https://www.izletv2.tk'+sUrl
    if  lka:
                    html= cRequestHandler(lka).request()
                    hash, id = re.findall('(?:watch|live)\("([^"]+)","([^"]+)"', html, re.IGNORECASE)[0]
                    data = urllib.urlencode({'hash': hash, 'id': id, 'e': '03BSTMTRKLR'})
                    req = urllib2.Request(lka, data, headers) 
                    response = urllib2.urlopen(req)
                    link = response.read()
                    response.close()
                    link1 = link [::-1]
                    #link1 = link1.replace('_','=') + '=='
                    #first64, second64 = re.findall('(.*?=)(.*?==)', link1, re.IGNORECASE)[0]
                    #son_url1 = base64.b64decode(first64)+'?'+base64.b64decode(second64)
                    son_url1 = decode_base64(link1)
                    Header = '|Referer='+lka+'&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
                    url = son_url1 + Header
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def otvplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl =sUrl+'|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    