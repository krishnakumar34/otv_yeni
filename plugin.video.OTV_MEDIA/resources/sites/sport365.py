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

SITE_IDENTIFIER = 'sport365'
from resources.lib.gui.guiElement import cGuiElement
import cookielib,aes,os
import os
import re
import sys
import base64
import re
import datetime
import urllib
from HTMLParser import HTMLParser
import json
import sys
import re
import os
import urllib
import urlparse
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
dialog = xbmcgui.Dialog()  
from core import httptools

from core import scrapertools
from platformcode import logger
from core import config
from platformcode import platformtools
from resources.lib import jscrypto
from core.item import Item
import magic_aes
s = requests.Session()
item = Item().fromurl(sys.argv[2])
addon = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
napisy = xbmc.translatePath('special://temp/napisyMOVIES365.txt')
napisyLos = xbmc.translatePath('special://temp/napisyLosMovies.txt')

BASEURL='http://www.sport365.live/en/main'
UA='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
header='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
movie = "http://www.365movies.tv/en/main"
host = "http://www.sport365.live/en/main"
	
def getRequests(url):
	headers = {
		'User-Agent': UA,
		'Accept': 'text/html, */*; q=0.01',
		'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
		'Referer': 'http://www.365movies.tv/en/home',
		'X-Requested-With': 'XMLHttpRequest',
		'Connection': 'keep-alive',
	}
	content=s.get(url,headers=headers,verify=False).content
	return content

def vtttostrLos(vtt):
    subs=re.findall('^(.+?-->\s+.+)',vtt,re.MULTILINE)
    row=0
    for sub in subs:
        row = row + 1
        d=re.findall('(\d+:\d+:\d+.\d+ -->)',sub) 
        if not d:
            sub2='%02d:%s'%(0,sub)
        else:
            d=re.findall('(\d+):\d+:\d+.\d+ -->',sub)
            sub2='%02d:%s'%(int(d[0]),sub)
        p1=re.findall('(\d+:\d+:\d+.\d+ -->)',sub2)
        p2=re.findall('--> (.+?)$',sub)
        d=re.findall('(\d+:\d+:\d+.\d+)',p2[0])
        if not d:
            sub2='%s%02d:%s'%(p1[0],0,p2[0])       
        else:
            p2ok=re.findall('-->\s*\d+:(.+?)$',sub)[0]
            d=re.findall('(\d+):\d+:\d+.\d+',p2[0])
            d=int(d[0])
            sub2='%s %02d:%s'%(p1[0],d,p2ok)
        nx=sub2
        nx=nx.replace(".",',')

        vtt=vtt.replace(sub,nx)
    vtt = re.sub(r'WEBVTT\n\n', '', vtt)
	
	
    vtt = re.sub(r'WEBVTT FILE\r\n\r\n', '', vtt)
	
	
    vtt = re.sub(r'WEBVTT FILE\n', '', vtt)
    vtt = re.sub(r'Kind:[ \-\w]+\n', '', vtt)
    vtt = re.sub(r'Language:[ \-\w]+\n', '', vtt)
    vtt = re.sub(r'<c[.\w\d]*>', '', vtt)
    vtt = re.sub(r'</c>', '', vtt)
    vtt = re.sub(r'<\d\d:\d\d:\d\d.\d\d\d>', '', vtt)
    vtt = re.sub(r'::[\-\w]+\([\-.\w\d]+\)[ ]*{[.,:;\(\) \-\w\d]+\n }\n', '', vtt)
    vtt = re.sub(r'Style:\n##\n', '', vtt)    
    return vtt


def vtttostr(vtt):
    subs=re.findall('^(.+?-->\s+.+)',vtt,re.MULTILINE)
    row=0
    for sub in subs:
        row = row + 1
        d=re.findall('(\d+:\d+:\d+.\d+ -->)',sub) 
        if not d:
            sub2='%02d:%s'%(0,sub)
        else:
            d=re.findall('(\d+):\d+:\d+.\d+ -->',sub)
            sub2='%02d:%s'%(int(d[0]),sub)
        p1=re.findall('(\d+:\d+:\d+.\d+ -->)',sub2)
        p2=re.findall('--> (.+?)$',sub)
        d=re.findall('(\d+:\d+:\d+.\d+)',p2[0]) 
        if not d:
            sub2='%s%02d:%s'%(p1[0],0,p2[0])       
        else:
            p2ok=re.findall('-->\s*\d+:(.+?)$',sub)[0]
            d=re.findall('(\d+):\d+:\d+.\d+',p2[0])
            d=int(d[0])
            sub2='%s %02d:%s'%(p1[0],d,p2ok)
        nx=str(row) +'\n'+sub2
        nx=nx.replace(".",',')

        vtt=vtt.replace(sub,nx)
    vtt = re.sub(r'WEBVTT\n\n', '', vtt)
    vtt = re.sub(r'Kind:[ \-\w]+\n', '', vtt)
    vtt = re.sub(r'Language:[ \-\w]+\n', '', vtt)
    vtt = re.sub(r'<c[.\w\d]*>', '', vtt)
    vtt = re.sub(r'</c>', '', vtt)
    vtt = re.sub(r'<\d\d:\d\d:\d\d.\d\d\d>', '', vtt)
    vtt = re.sub(r'::[\-\w]+\([\-.\w\d]+\)[ ]*{[.,:;\(\) \-\w\d]+\n }\n', '', vtt)
    vtt = re.sub(r'Style:\n##\n', '', vtt)    
    return vtt


def getUrl(url, data=None, header={}, usecookies=True):
    if usecookies:
        cj = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent': UA}
    req = urllib2.Request(url,data,headers=header)
    try:
        response = urllib2.urlopen(req, timeout=15)
        link = response.read()
        response.close()
    except:
        link=''
    return link

def getUrlc(url, data=None, header={}, usecookies=True):
    cj = cookielib.LWPCookieJar()
    if usecookies:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent': UA}
    req = urllib2.Request(url, data, headers=header)
    try:
        response = urllib2.urlopen(req, timeout=15)
        link = response.read()
        response.close()
    except:
        link=''
    c = ''.join(['%s=%s' % (c.name, c.value) for c in cj]) if cj else ''
    return link, c
base_url        = sys.argv[0]
addon_handle    = int(sys.argv[1])
args            = urlparse.parse_qs(sys.argv[2][1:])
my_addon        = xbmcaddon.Addon()
addonName       = my_addon.getAddonInfo('name')
my_addon_id     = my_addon.getAddonInfo('id')
PATH            = my_addon.getAddonInfo('path')
VERSION         = my_addon.getAddonInfo('version')
DATAPATH        = xbmc.translatePath(my_addon.getAddonInfo('profile')).decode('utf-8')
RESOURCES       = PATH+'/resources/'

sys.path.append(os.path.join(RESOURCES, "lib"))

FANART = my_addon.getAddonInfo('fanart')
ICON = my_addon.getAddonInfo('icon')

kukz=''
kkey = addon.getSetting('keyk')
sortv = addon.getSetting('sortV')
sortn = addon.getSetting('sortN') if sortv else 'All'

katv = addon.getSetting('katV')
katn = addon.getSetting('katN') if katv else 'All'

UA= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
TIMEOUT=15


def mainlist():
    oGui = cGui()
                
    tarzlistesi= []                
    tarzlistesi.append(("Schedule", "http://www.sport365.live/en/events/-/1/-/-/60", "http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg"))
    tarzlistesi.append(("Live", "http://www.sport365.live/en/events/-/1/-/-/120", "http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg"))
    tarzlistesi.append(("Schedule by language", "http://www.sport365.live/en/sidebar", "http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg"))
    
               
    for sTitle,sUrl,sPicture in tarzlistesi:
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == 'Schedule by language':
             oGui.addMovie(SITE_IDENTIFIER, 'languages', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'MOVIE':              
             oGui.addMovie(SITE_IDENTIFIER, 'alanguages', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        else:
             oGui.addMovie(SITE_IDENTIFIER, 'tickets', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()

   
    
def getUrl(url,data=None,header={},useCookies=True):
    if useCookies:
        cj = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent':UA}
    req = urllib2.Request(url,data,headers=header)
    try:
        response = urllib2.urlopen(req, timeout=15)
        link = response.read()
        response.close()
    except:
        link=''
    return link

def getUrlc(url, data=None, header={}, usecookies=True):
    cj = cookielib.LWPCookieJar()
    if usecookies:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent': UA}
    req = urllib2.Request(url, data, headers=header)
    try:
        response = urllib2.urlopen(req, timeout=15)
        link = response.read()
        response.close()
    except:
        link=''
    c = ';'.join(['%s=%s' % (c.name, c.value) for c in cj]) if cj else ''
    return link, c	
                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok    



def agendaglobal(item):
    itemlist = []    
    try:
        item.channel = "sport365"
        item.url = "http://www.sport365.live/en/events/-/1/-/-/60"
        item.thumbnail="http://i.imgur.com/hJ2vhip.png"
        item.fanart="http://i.imgur.com/bCn8lHB.jpg?1"
        itemlist = tickets(item)
        for item_global in itemlist:
            if item_global.action == "":
                itemlist.remove(item_global)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []

    return itemlist


def tickets():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)

    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save:
        key = getkey()
    else:
        key = base64.b64decode(key_save)

    color = 'blue'

    fechas = scrapertools.find_multiple_matches(data, '<td colspan=9[^>]+>(\d+\.\d+\.\d+)<')
    if "Redifusiones" in item.title and not fechas:
        itemlist.append(item.clone(action="", title="No currently scheduled"))
        return itemlist

    for i, f in enumerate(fechas):
        delimit = '</table>'
        if i != len(fechas) - 1:
            delimit = fechas[i+1]
        bloque = scrapertools.find_single_match(data, '%s<(.*?)%s' % (f, delimit))
        patron = 'onClick=.*?,\s*"([^"]+)".*?<td rowspan=2.*?src="([^"]+)".*?<td rowspan=2.*?>(\d+:\d+)<' \
                 '.*?<td.*?>([^<]+)<.*?<td.*?>(.*?)/td>.*?<tr.*?<td colspan=2.*?>([^<]+)<'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for url, thum, hora, title, datos, deporte in matches:
            evento = title.replace("-", "vs")
            text_color = "red"
            thumb= "http://www.realstream.cc/images/matras.jpg"
            if "green-big.png" in thum:
                thumb= "http://mareeg.com/wp-content/uploads/2017/02/LIVE.png"
                text_color = "lime"
                
            if "/" in deporte:
                deporte = deporte.split(" /", 1)[0]
            if "<span" in datos:
                calidad, idioma = scrapertools.find_single_match(datos, '>([^<]+)</span>([^<]+)<')
                datos = "%s/%s/%s" % (deporte, calidad.replace("HQ", "HD"), idioma)
                if idioma == "Dutch" and color:
                    text_color = color
            else:
                datos = "%s/%s" % (deporte, datos[:-1])
                if "Dutch" in datos and color:
                    text_color = color


            fecha = f.replace(".", "/")

            url = json.loads(base64.b64decode(url))
            try:
                url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
            except:
                key = getkey(True)
                url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
            sUrl = "http://www.sport365.live" + url.replace('\\/','/').replace('"',"").replace("'></iframe>","")
            horas, minutos = hora.split(":")
            dia, mes, year = fecha.split("/")
            fecha_evento = datetime.datetime(int(year), int(mes), int(dia),
                                             int(horas), int(minutos))
            fecha_evento = fecha_evento + datetime.timedelta(hours=1)
            hora = fecha_evento.strftime("%H:%M")
            date = fecha_evento.strftime("%d/%m")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))
            if len(fechas) == 1:
                sTitle = "[COLOR %s]%s - %s [/COLOR][COLOR darkorange](%s)[/COLOR]" % (text_color, hora, title, datos)
                
                oGui.addTV(SITE_IDENTIFIER, 'findvideos',  sTitle, '', thumb, '', oOutputParameterHandler)
            else:
                sTitle = "[COLOR %s][%s] %s - %s[/COLOR] [COLOR darkorange](%s)[/COLOR]" % (text_color, date, hora, title, datos)
                
                oGui.addTV(SITE_IDENTIFIER, 'findvideos',  sTitle, '', thumb, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()                         


def allanguages():	
	
		myMode = 'sort'	
		label=['All','Bahasa Indonesia','Dansk','Deutsch','English','Español','Français','Italiano','Lietuvių','Magyar','Nederlands, Vlaams','Norsk','Polski','Svenska','Русский','Українська','עברית','हिन्दी, हिंदी','中文 (Zhōngwén)','日本語']
		value=['-','id','da','de','en','es','fr','it','lt','hu','nl','no','pl','sv','ru','uk','he','hi','zh','ja']
		msg = 'Language'
		sel = xbmcgui.Dialog().select(msg,label)
		if sel>-1:
		
			addon.setSetting(myMode+'V',value[sel])
			addon.setSetting(myMode+'N',label[sel])		
			xbmc.executebuiltin("Container.Refresh") 
		else:
			pass	



def languages():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)
    
    matches = scrapertools.find_multiple_matches(data, "<option value='([0-9]+)'>.*?\/\s*(.*?)<")
    for value, sTitle in matches:
        sUrl = "http://www.sport365.live/en/events/-/1/-/%s/60" % value
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == "Dutch":
            oGui.addDir(SITE_IDENTIFIER, 'tickets', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'tickets', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 

def movietickets():
    oGui = cGui()
    ret=''
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)
    sources=re.compile(".*?><b>(.*?)</td><td nowrap style.*?href='/en/movie/(.*?)'>.*?<image.*?src='(.*?)'.*?<b>Audio</b>(.*?)<br>").findall(data)
    for  title,url, thumb,ses in sources:
            sUrl ='http://www.365movies.tv/en/links/'+ url
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))
#            if len(fechas) == 1:
#                sTitle = "[COLOR %s]%s - %s [/COLOR][COLOR darkorange](%s)[/COLOR]" % (text_color, ses, title, datos)
                
            oGui.addTV(SITE_IDENTIFIER, 'mofindvideos',  title, '', thumb, ses, oOutputParameterHandler)
#            else:
#                sTitle = "[COLOR %s][%s] %s - %s[/COLOR] [COLOR darkorange](%s)[/COLOR]" % (text_color, date, ses, title, datos)
                
#                oGui.addTV(SITE_IDENTIFIER, 'findvideos',  sTitle, '', thumb, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()                         

def mmovietickets():
    oGui = cGui()
 
    itemlist = []
   
    key_save = config.get_setting("key_cryp", "365movies")
    if not key_save:
        key = mgetkey()
    else:
        key = base64.b64decode(key_save)
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data) 
   
    sources=re.compile("onClick=.*?'(.*?)'.*?>Link(.*?)</span>").findall(data)
    for s ,title  in sources:
         
         
            data = base64.b64decode(s)
            ces=re.compile('"ct":"(.*?)","iv":".*?","s":"(.*?)"').findall(data)       
            (ct,s)=ces[0]
         
            key = mgetkey()
            url = jscrypto.decode(ct, key, s.decode("hex"))

            data = url.replace('\/','/').replace('"',"").replace("'></iframe>","")
           
            title = 'Link-%s '%(title)
            thumb= "http://m1.medianetworkinternational.com/images/icons/apple-touch-icon-114x114.png"
            data = data.replace('\\/', '/').replace("\\", "").replace('"',"").replace("'></iframe>","")
            sUrl= scrapertools.find_single_match(data, "src='([^']+)'")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))
#            if len(fechas) == 1:
#                sTitle = "[COLOR %s]%s - %s [/COLOR][COLOR darkorange](%s)[/COLOR]" % (text_color, ses, title, datos)
                
            oGui.addTV(SITE_IDENTIFIER, 'movieplay',  title, '', thumb, '', oOutputParameterHandler)
#            else:
#                sTitle = "[COLOR %s][%s] %s - %s[/COLOR] [COLOR darkorange](%s)[/COLOR]" % (text_color, date, ses, title, datos)
                
#                oGui.addTV(SITE_IDENTIFIER, 'findvideos',  sTitle, '', thumb, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()                   
def movieplay():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle= oInputParameterHandler.getValue('sMovieTitle')
    data = httptools.downloadpage(url).data
    url = scrapertools.find_single_match(data, '<iframe.*?src="([^"]+)"')
    if not url:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []
    elif "/matras.jpg" in data:
        platformtools.dialog_notification("Stream error", "Try again after a few minutes")
        return []
    
    h = HTMLParser()
    url = h.unescape(url)
    data = httptools.downloadpage(url).data
    f = scrapertools.find_single_match(data, 'name="f" value="([^"]+)"')
    d = scrapertools.find_single_match(data, 'name="d" value="([^"]+)"')
    r = scrapertools.find_single_match(data, 'name="r" value="([^"]+)"')
    url_post = scrapertools.find_single_match(data, "'action',\s*'([^']+)'")
    if not url_post:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []

    post = {'r': r, 'd':d, 'f':f}
    post = urllib.urlencode(post)
    data = httptools.downloadpage(url_post, post).data
    try:
        get_links(data)
    except:
        pass

    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save:
        key = mgetkey()
    else:
        key = base64.b64decode(key_save)
    data_crypto = scrapertools.find_single_match(data, "\};[A-z0-9]{43}\(.*?,.*?,\s*'([^']+)'")
    url = json.loads(base64.b64decode(data_crypto))
    try:
        url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
    except:
        key = mgetkey()
        url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))  
        
    url = url.replace('\\/', '/').replace("\\", "").replace('"', "")
    headers_test = {'Referer': url_post, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    response = httptools.downloadpage(url, headers=headers_test, follow_redirects=False, only_headers=True, replace_headers=True)
    if response.code == 406:
        response = httptools.downloadpage(url, headers=headers_test, follow_redirects=False, only_headers=True, replace_headers=True, cookies=False)
    if response.code == 406:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []
   
    sUrl=url+ "ndex.m3u8"                 
    data = httptools.downloadpage(url).data                                 
    channels = re.findall('",NAME=".*?.(.*?)",FORCED=NO,DEFAULT=.*?,URI="(.*?)"', data, re.S)            
    for sTitle,Link in channels:         
           Url = re.compile('(.*?)index.m3u8').findall(sUrl)                          
              #sUrl=url.replace('index.m3u8', '/').replace('ndex.m3u8', '/')#Referer=%s&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36' % url_post
          
           sTitle =alfabekodla(sTitle) 
           oOutputParameterHandler = cOutputParameterHandler()
           oOutputParameterHandler.addParameter('siteUrl', Url[0])
           oOutputParameterHandler.addParameter('link', Link)
           oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
           oGui.addDir(SITE_IDENTIFIER, 'playovietickets', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()
def mofindvideos():                             
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    info= oInputParameterHandler.getValue('sMovieTitle')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)

    if "The references of the transmission will be published" in data:
        itemlist.append(item.clone(title="The links will be available between 5-10 minutes before it starts.", action=""))
        return itemlist

    key_save = config.get_setting("key_cryp", "365movies")
    if not key_save:
        key = getkey()
    else:
        key = base64.b64decode(key_save)

    matches = scrapertools.find_multiple_matches(data, "<span id='span_watch_links'.*?, '([^']+)'")
    if not matches:
        matches = scrapertools.find_multiple_matches(data, '<span id=["\']span_link_links[\'"] onClick="\w+\(\'(.*?)\'')
    h = HTMLParser()
    for i, url in enumerate(matches):
        url = json.loads(base64.b64decode(url))
        try:
            url = jscrypto.decode(url["ct"], kkey, url["s"].decode("hex"))
        except:
            key = getkey(True)
            url = jscrypto.decode(url["ct"], kkey, url["s"].decode("hex"))
        data_url = url.replace('\\/','/').replace("\\", "").replace("'></iframe>","")
        data_url = h.unescape(data_url)

        sUrl = scrapertools.find_single_match(data_url, "<iframe.*?src='([^']+)'")
        sTitle = "[COLOR green]Stream %s - [/COLOR][COLOR darkorange](%s)[/COLOR]" % (i+1, info)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, 'gChannels', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 
                                                      








def findvideos():                             
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    info= oInputParameterHandler.getValue('sMovieTitle')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)

    if "The references of the transmission will be published" in data:
        itemlist.append(item.clone(title="The links will be available between 5-10 minutes before it starts.", action=""))
        return itemlist

    key_save = config.get_setting("key_cryp", "365movies")
    if not key_save:
        key = getkey()
    else:
        key = base64.b64decode(key_save)

    matches = scrapertools.find_multiple_matches(data, "<span id='span_watch_links'.*?, '([^']+)'")
    if not matches:
        matches = scrapertools.find_multiple_matches(data, "<span id='span_code_links'.*?, '([^']+)'")
    h = HTMLParser()
    for i, url in enumerate(matches):
        url = json.loads(base64.b64decode(url))
        try:
            url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
        except:
            key = getkey(True)
            url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
        data_url = url.replace('\\/','/').replace("\\", "").replace("'></iframe>","")
        data_url = h.unescape(data_url)

        sUrl = scrapertools.find_single_match(data_url, "<iframe.*?src='([^']+)'")
        sTitle = "[COLOR green]Stream %s - [/COLOR][COLOR darkorange](%s)[/COLOR]" % (i+1, info)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, 'play', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 
                                                      
    

def play():
 
  oInputParameterHandler = cInputParameterHandler()
  url = oInputParameterHandler.getValue('siteUrl')
  sTitle= oInputParameterHandler.getValue('sMovieTitle')    

  itemlist = []
  oInputParameterHandler = cInputParameterHandler()
  url = oInputParameterHandler.getValue('siteUrl')
  sTitle= oInputParameterHandler.getValue('sMovieTitle')
  import xbmc
    #xbmc.log('@#@CHANNEL-VIDEO-ITEM: %s' % item, xbmc.LOGNOTICE)
  s = requests.Session()
  header = {'User-Agent': UA,
              'Referer': url}
  content = s.get(url, headers=header).content
  import uuid
  hash = uuid.uuid4().hex

  uri = url + hash

  links = re.compile('(http://www.[^\.]+.pw/(?!&#)[^"]+)',
                       re.IGNORECASE + re.DOTALL + re.MULTILINE + re.UNICODE).findall(content)
  link = [x for x in links if '&#' in x]
  if link:
    link = re.sub(r'&#(\d+);', lambda x: chr(int(x.group(1))), link[0])
    data = s.get(link, headers=header).content
    f = scrapertools.find_single_match(data, 'name="f" value="([^"]+)"')
    d = scrapertools.find_single_match(data, 'name="d" value="([^"]+)"')
    r = scrapertools.find_single_match(data, 'name="r" value="([^"]+)"')
    b = scrapertools.find_single_match(data, 'name="b" value="([^"]+)"')
    bul = scrapertools.find_single_match(data, 'src=[\'"](.*?)[\'"]')
    url_post = scrapertools.find_single_match(data, "'action',\s*'([^']+)'")
    if not url_post:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []

    post = {'b': b,'r': r, 'd':d, 'f':f}
    post = urllib.urlencode(post)
    data = httptools.downloadpage(url_post, post).data
    try:
        get_links(data)
    except:
        pass

    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save:
        key = getkey()
    else:
        key = base64.b64decode(key_save)
    data_crypto = scrapertools.find_single_match(data, "\};[A-z0-9]{43}\(.*?,.*?,\s*'([^']+)'")
    url = json.loads(base64.b64decode(data_crypto))
    try:
        url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
    except:
        key = getkey(True)
        url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))  
        
    url = url.replace('\\/', '/').replace("\\", "").replace('"', "")
    headers_test = {'Referer': bul, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    response = httptools.downloadpage(url, headers=headers_test, follow_redirects=False, only_headers=True, replace_headers=True)
    if response.code == 406:
        response = httptools.downloadpage(url, headers=headers_test, follow_redirects=False, only_headers=True, replace_headers=True, cookies=False)
    if response.code == 406:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []
    url += "ndex.m3u8|Referer=%s&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36" % url_post
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(url)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()

     
                                                      


def gChannels(url,response):
		subtitles=selM3U8(url,response)
		if subtitles:
				label = [x[0].strip() for x in subtitles]
				stream = [x[1].strip() for x in subtitles]
				sel = xbmcgui.Dialog().select('Select subtitle',label)
				if sel>-1:
					napis=stream[sel].split('|')
					
					dla=napis[1]
					content , c = getUrlc(napis[0], header=header, usecookies=True)
					nxturl=re.findall('(.+?)',content,re.DOTALL)[0]
					content , c = getUrlc(dla+nxturl, header=header, usecookies=True)
					
					poprawiony=vtttostr(content)
					open(napisy, 'w').write(poprawiony)		
					nap=True
				else:
					nap=False	
		else:
			nap=False
		playlist=''		

		if src.startswith('http'):
			stream_url = src + '|Referer=%s&User-Agent=%s&Cookie=%s' % (action[0],UA,c)
			return stream_url,nap
		else:
			stream_url = magic_aes.decode_hls(src)
			if stream_url:
				stream_url += '|Origin=http://h6.adshell.net&Referer=%s&User-Agent=%s&Cookie=%s' % (action[0],UA,c)
				return stream_url,nap


def mgetkey(overwrite=False):
    data = httptools.downloadpage(movie).data

    js = scrapertools.find_multiple_matches(data, 'src="(http://m1.medianetworkinternational.com/js/[A-z0-9]{32}.js)')
    data_js = httptools.downloadpage(js[-1]).data

    str_wise = scrapertools.find_single_match(data_js, ".join\(''\);\}\('(.*?)\)\);")
    while True:
        result = decrypt(str_wise)
        if not "w,i,s,e" in result:
            break
        str_wise = scrapertools.find_single_match(result, ".join\(''\);\}\('(.*?)\)\);")

    
    key = scrapertools.find_single_match(result, 'return "([^"]+)"')
    key_save = config.get_setting("key_cryp", "365movies")
    if not key_save or overwrite:
        key_save = config.set_setting("key_cryp", base64.b64encode(key), "365movies")    

    return key

def getkey(overwrite=False):
    data = httptools.downloadpage(host).data

    js = scrapertools.find_multiple_matches(data, 'src="(http://s1.medianetworkinternational.com/js/[A-z0-9]{32}.js)')
    data_js = httptools.downloadpage(js[-1]).data

    str_wise = scrapertools.find_single_match(data_js, ".join\(''\);\}\('(.*?)\)\);")
    while True:
        result = decrypt(str_wise)
        if not "w,i,s,e" in result:
            break
        str_wise = scrapertools.find_single_match(result, ".join\(''\);\}\('(.*?)\)\);")

    
    key = scrapertools.find_single_match(result, 'return "([^"]+)"')
    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save or overwrite:
        key_save = config.set_setting("key_cryp", base64.b64encode(key), "sport365")    

    return key


def decrypt(data):
    cadena1, cadena2, cadena3, cadena4 = data.split("','")
    cadena4 = cadena4.replace("'", "")
    j = 0
    c = 0
    i = 0
    list1 = []
    list2 = []
    while True:
        if j < 5:
            list2.append(cadena1[j])
        else:
            if j < len(cadena1):
                list1.append(cadena1[j])
        j += 1
        if c < 5:
            list2.append(cadena2[c])
        else:
            if c < len(cadena2):
                list1.append(cadena2[c])
        c += 1
        if i < 5:
            list2.append(cadena3[i])
        else:
            if i < len(cadena3):
                list1.append(cadena3[i])
        i += 1
        if (len(cadena1) + len(cadena2) + len(cadena3) + len(cadena4)) == (len(list1) + len(list2) + len(cadena4)):
            break
    cadena5 = "".join(list1)
    cadena6 = "".join(list2)
    c = 0
    resultado = []
    j = 0
    for j in range(0, len(list1), 2):
        operando = -1
        if (ord(cadena6[c]) % 2):
            operando = 1

        try:
            resultado.append(chr(int(cadena5[j:j+2], 36) - operando))
        except:
            pass
        c += 1
        if c >= len(list2):
            c = 0
    result = "".join(resultado)

    return result


def get_links(data):
    adshell = scrapertools.find_single_match(data, "<script src=[\"'](http://tags2.adshell.net.*?)['\"]")
    data_shell = httptools.downloadpage(adshell).data

    url = scrapertools.find_single_match(data_shell, ",url:'([^']+)'")
    headers = {'Referer': adshell}
    data = httptools.downloadpage(url, headers=headers).data
def mplay():
 
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle= oInputParameterHandler.getValue('sMovieTitle')    
    
#    data = httptools.downloadpage(url).data
    name ='test'
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

class JsUnwiser:
    def unwiseAll(self, data):
        try:
            in_data=data
            sPattern = 'eval\\(function\\(w,i,s,e\\).*?}\\((.*?)\\)'
            wise_data=re.compile(sPattern).findall(in_data)
            for wise_val in wise_data:
                unpack_val=self.unwise(wise_val)
                #print '\nunpack_val',unpack_val
                in_data=in_data.replace(wise_val,unpack_val)
            return re.sub(re.compile("eval\(function\(w,i,s,e\).*?join\(''\);}", re.DOTALL), "", in_data, count=1)
        except: 
            traceback.print_exc(file=sys.stdout)
            return data
        
    def containsWise(self, data):
        return 'w,i,s,e' in data
        
    def unwise(self, sJavascript):
        #print 'sJavascript',sJavascript
        page_value=""
        try:        
            ss="w,i,s,e=("+sJavascript+')' 
            exec (ss)
            page_value=self.__unpack(w,i,s,e)
        except: traceback.print_exc(file=sys.stdout)
        return page_value
        
    def __unpack( self,w, i, s, e):
        lIll = 0;
        ll1I = 0;
        Il1l = 0;
        ll1l = [];
        l1lI = [];
        while True:
            if (lIll < 5):
                l1lI.append(w[lIll])
            elif (lIll < len(w)):
                ll1l.append(w[lIll]);
            lIll+=1;
            if (ll1I < 5):
                l1lI.append(i[ll1I])
            elif (ll1I < len(i)):
                ll1l.append(i[ll1I])
            ll1I+=1;
            if (Il1l < 5):
                l1lI.append(s[Il1l])
            elif (Il1l < len(s)):
                ll1l.append(s[Il1l]);
            Il1l+=1;
            if (len(w) + len(i) + len(s) + len(e) == len(ll1l) + len(l1lI) + len(e)):
                break;
            
        lI1l = ''.join(ll1l)#.join('');
        I1lI = ''.join(l1lI)#.join('');
        ll1I = 0;
        l1ll = [];
        for lIll in range(0,len(ll1l),2):
            #print 'array i',lIll,len(ll1l)
            ll11 = -1;
            if ( ord(I1lI[ll1I]) % 2):
                ll11 = 1;
            #print 'val is ', lI1l[lIll: lIll+2]
            l1ll.append(chr(    int(lI1l[lIll: lIll+2], 36) - ll11));
            ll1I+=1;
            if (ll1I >= len(l1lI)):
                ll1I = 0;
        ret=''.join(l1ll)
        if 'eval(function(w,i,s,e)' in ret:
            ret=re.compile('eval\(function\(w,i,s,e\).*}\((.*?)\)').findall(ret)[0] 
            return self.unwise(ret)
        else:
            return ret
def getkey(overwrite=False):
    data = httptools.downloadpage(host).data

    js = scrapertools.find_multiple_matches(data, 'src="(http://s1.medianetworkinternational.com/js/[A-z0-9]{32}.js)')
    data_js = httptools.downloadpage(js[-1]).data

    str_wise = scrapertools.find_single_match(data_js, ".join\(''\);\}\('(.*?)\)\);")
    while True:
        result = decrypt(str_wise)
        if not "w,i,s,e" in result:
            break
        str_wise = scrapertools.find_single_match(result, ".join\(''\);\}\('(.*?)\)\);")

    
    key = scrapertools.find_single_match(result, 'return "([^"]+)"')
    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save or overwrite:
        key_save = config.set_setting("key_cryp", base64.b64encode(key), "sport365")    

    return key


def decrypt(data):
    cadena1, cadena2, cadena3, cadena4 = data.split("','")
    cadena4 = cadena4.replace("'", "")
    j = 0
    c = 0
    i = 0
    list1 = []
    list2 = []
    while True:
        if j < 5:
            list2.append(cadena1[j])
        else:
            if j < len(cadena1):
                list1.append(cadena1[j])
        j += 1
        if c < 5:
            list2.append(cadena2[c])
        else:
            if c < len(cadena2):
                list1.append(cadena2[c])
        c += 1
        if i < 5:
            list2.append(cadena3[i])
        else:
            if i < len(cadena3):
                list1.append(cadena3[i])
        i += 1
        if (len(cadena1) + len(cadena2) + len(cadena3) + len(cadena4)) == (len(list1) + len(list2) + len(cadena4)):
            break
    cadena5 = "".join(list1)
    cadena6 = "".join(list2)
    c = 0
    resultado = []
    j = 0
    for j in range(0, len(list1), 2):
        operando = -1
        if (ord(cadena6[c]) % 2):
            operando = 1

        try:
            resultado.append(chr(int(cadena5[j:j+2], 36) - operando))
        except:
            pass
        c += 1
        if c >= len(list2):
            c = 0
    result = "".join(resultado)

    return result
def pplayovietickets(url):

    
       
                                                
    

    name =''
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')

def selM3U8(stream_url,playlist):
	lout=[]
	sout=[]
	o = urlparse.urlparse(stream_url).query
	kk2=stream_url.replace('index.m3u8?','').replace(o,'')
	lektors=re.findall('TYPE=AUDIO.+?NAME="(.+?)".+?URI="(.+?)"',playlist,re.DOTALL)
	subtitles=re.findall('TYPE=SUBTITLE.+?NAME="(.+?)".+?URI="(.+?)"',playlist,re.DOTALL)

	for lektor,uri in lektors:
		m3u8=kk2+uri
		lout.append((lektor,m3u8))
	for subtitle,uri2 in subtitles:
		m3u82=kk2+uri2+'|'+kk2
		sout.append((subtitle,m3u82))	
	return lout,sout	

def Play365(url):	
	stream_url,napis = Play3651st(url)	
	play_item = xbmcgui.ListItem(path=stream_url)
	if napis:
		play_item.setSubtitles([napisy])
	if stream_url:
		xbmcplugin.setResolvedUrl(addon_handle, True, play_item)	
	else:
		xbmcplugin.setResolvedUrl(addon_handle, False,  xbmcgui.ListItem(path=''))	

def Play3651st(url):
	header = {'User-Agent': UA,
			'Referer': url}
		
	html = s.get(url, headers=header).content
	import uuid
	hash = uuid.uuid4().hex
	url = re.findall(r'<iframe.*?src="([^"]+)"', html)[0]
	uri = url 
	data = s.get(uri, headers=header).content

	
	f = re.compile('.*?name="f"\s*value=["\']([^"\']+)["\']').findall(data)
	d = re.compile('.*?name="d"\s*value=["\']([^"\']+)["\']').findall(data)
	r = re.compile('.*?name="r"\s*value=["\']([^"\']+)["\']').findall(data)
	action = re.compile('[\'"]action[\'"][,\s]*[\'"](http.*?)[\'"]').findall(data)
	srcs = re.compile('src=[\'"](.*?)[\'"]').findall(data)
	if f and r and d and action:
	
	
		head = {
			'Host': 'h6.adshell.net',
			'User-Agent': UA,
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
			'Referer': url,
			'Upgrade-Insecure-Requests': '1',}
		
		data = {'r': r[0],'d': d[0],'f': f[0]}

		data2 = s.post(action[0], headers=head, cookies=s.cookies, data=data).content
	
		bheaders = header
		bheaders['Referer'] = action[0]
		banner = re.findall(r'videojs.*?script\s+src="([^"]+)', data2)[0]
		bsrc = s.get(banner, headers=bheaders).content
		
		banner = re.findall(r"url:'([^']+)", bsrc)[0]
		bsrc = s.get(banner, headers=bheaders).content
		bheaders['Referer'] = banner
		banner = re.findall(r'window.location.replace\("([^"]+)"\);\s*}\)<\/script><div', bsrc)[0]
		bsrc = s.get(banner,verify=False).content
		bsrc=bsrc.replace("\'",'"')
		try:
			hh, c = getUrlc("https://adbetnet.advertserve.com/servlet/view/dynamic/javascript/zone?zid=281&pid=4&resolution=1920x1080&random=11965377&millis=1473441350879&referrer=http%3A%2F%2Fwww.365movies.tv%2Fen%2Fhome", header=header, usecookies=True)
			hh=hh.replace('\\"',"'")
			nxturl=re.findall("var URL\s*=\s*'(.+?)'",hh)[0]
			datax, c2 = getUrlc(nxturl, header=header, usecookies=True)	
		except:
			pass
		
		link = re.compile('\([\'"][^"\']+[\'"], [\'"][^"\']+[\'"], [\'"]([^"\']+)[\'"], 1\)').findall(data2)
		enc_data = json.loads(base64.b64decode(link[0]))
		ciphertext = 'Salted__' + enc_data['s'].decode('hex') + base64.b64decode(enc_data['ct'])
		src = magic_aes.decrypt(kkey,base64.b64encode(ciphertext))
		src = src.replace('"','').replace('\\','').encode('utf-8')
		a, c = getUrlc(srcs[-1], header=header, usecookies=True) if srcs else '', ''
		a, c = getUrlc(src, header=header, usecookies=True)
		lektors,subtitles=selM3U8(src,a)
		if len(subtitles)>0:
			if subtitles:
				label = [x[0].strip() for x in subtitles]
				stream = [x[1].strip() for x in subtitles]
				sel = xbmcgui.Dialog().select('Select subtitle',label)
				if sel>-1:
					napis=stream[sel].split('|')
					
					dla=napis[1]
					content , c = getUrlc(napis[0], header=header, usecookies=True)
					nxturl=re.findall('(.+?)',content,re.DOTALL)[0]
					content , c = getUrlc(dla+nxturl, header=header, usecookies=True)
					
					poprawiony=vtttostr(content)
					open(napisy, 'w').write(poprawiony)		
					nap=True
				else:
					nap=False	
		else:
			nap=False
		playlist=''		

		if src.startswith('http'):
			stream_url = src + '|Referer=%s&User-Agent=%s&Cookie=%s' % (action[0],UA,c)
			return stream_url,nap
		else:
			stream_url = magic_aes.decode_hls(src)
			if stream_url:
				stream_url += '|Origin=http://h6.adshell.net&Referer=%s&User-Agent=%s&Cookie=%s' % (action[0],UA,c)
				return stream_url,nap
def getKey():	
	ret =''
	content = getRequests('http://www.365movies.tv/en/')
	wrapper = re.compile('(http[^"]+/advertisement.js\?\d+)').findall(content)
	wrappers = re.compile('<script type="text/javascript" src="(http://m1.medianetworkinternational.com/js/\w+.js)"').findall(content)
	for wrapper in wrappers:
		wc = getRequests(wrapper)
		content=JsUnwiser().unwiseAll(wc)
		ret = content
		ret = re.compile('return "(.*?)"').findall(content)
		if ret:
			ret = ret[0]
	addon.setSetting('keyk',ret)
	return ret	
	                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok
       