#-*- coding: utf-8 -*-
import sys,re,os
from urlparse import parse_qsl
import base64
import urllib
import urllib2
import urllib3
import requests
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmc

from HTMLParser import HTMLParser
import json
import cookielib
import traceback
import urlparse
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import Parser as cParser
from resources.lib.comaddon import progress
from resources.lib.util import cUtil
from resources.lib.config import cConfig
from core import scrapertools
from core import httptools
from datetime import timedelta
from requests_cache import CachedSession

user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTS Build/LVY48F)"
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
params = dict(parse_qsl(sys.argv[2][1:]))
addon = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
napisy = xbmc.translatePath('special://temp/napisyMOVIES365.txt')
napisyLos = xbmc.translatePath('special://temp/napisyLosMovies.txt')
PATH            = addon.getAddonInfo('path')
DATAPATH        = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
RESOURCES       = PATH+'/resources/'
SITE_IDENTIFIER = 'movies365'
SITE_NAME = 'Movies365'
SITE_DESC = 'Replay TV'
from core import jsontools
from resources.lib import jscrypto
FANART=RESOURCES+'fanart.jpg'
from routing import Plugin
plugin = Plugin()
import magic_aes
exlink = params.get('url', None)
name= params.get('name', None)
movie= movie=True
mcount= moviescount=0
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
params = dict(parse_qsl(sys.argv[2][1:]))
rys= params.get('image', None)


 
UA= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
TIMEOUT=15
def refresh():
    S.cache.clear()
    xbmc.executebuiltin("Container.Refresh")

s = requests.Session()
def alfabekodla(text):
        text = (str(text)).replace('\\x','')
        text = (str(text)).replace('&auml;','ä')
	text = (str(text)).replace('\u00e4','ä')
	text = (str(text)).replace('&#228;','ä')
	text = (str(text)).replace('&Auml;','Ä')
	text = (str(text)).replace('\u00c4','Ä')
	text = (str(text)).replace('&#196;','Ä')
	text = (str(text)).replace('&ouml;','ö')
	text = (str(text)).replace('\u00f6','ö')
	text = (str(text)).replace('&#246;','ö')
	text = (str(text)).replace('&ouml;','Ö')
	text = (str(text)).replace('&Ouml;','Ö')
	text = (str(text)).replace('\u00d6','Ö')
	text = (str(text)).replace('&#214;','Ö')
	text = (str(text)).replace('&uuml;','ü')
	text = (str(text)).replace('\u00fc','ü')
	text = (str(text)).replace('&#252;','ü')
	text = (str(text)).replace('&Uuml;','Ü')
	text = (str(text)).replace('\u00dc','Ü')
	text = (str(text)).replace('&#220;','Ü')
        text = (str(text)).replace('tv_','player')
	text = (str(text)).replace('&szlig;','ß')
	text = (str(text)).replace('\u00df','ß')
	text = (str(text)).replace('&#223;','ß')
	text = (str(text)).replace('&amp;','&')
	text = (str(text)).replace('&quot;','\"')
	text = (str(text)).replace('&gt;','>')
	text = (str(text)).replace('&apos;',"'")
	text = (str(text)).replace('&acute;','\'')
	text = (str(text)).replace('&ndash;','-')
	text = (str(text)).replace('&bdquo;','"')
	text = (str(text)).replace('&rdquo;','"')
	text = (str(text)).replace('&ldquo;','"')
	text = (str(text)).replace('&lsquo;','\'')
	text = (str(text)).replace('&rsquo;','\'')
	text = (str(text)).replace('&#034;','\'')
	text = (str(text)).replace('&#038;','&')
	text = (str(text)).replace('&#039;','\'')
	text = (str(text)).replace('&#39;','\'')
	text = (str(text)).replace('&#160;',' ')
	text = (str(text)).replace('\u00a0',' ')
	text = (str(text)).replace('\u00b4','\'')
	text = (str(text)).replace('&#174;','')
	text = (str(text)).replace('&#225;','a')
	text = (str(text)).replace('&#233;','e')
	text = (str(text)).replace('&#243;','o')
	text = (str(text)).replace('&#8211;',"-")
	text = (str(text)).replace('\u2013',"-")
	text = (str(text)).replace('&#8216;',"'")
	text = (str(text)).replace('&#8217;',"'")
	text = (str(text)).replace('&#8220;',"'")
	text = (str(text)).replace('&#8221;','"')
	text = (str(text)).replace('&#8222;',',')
	text = (str(text)).replace('\u201e','\"')
	text = (str(text)).replace('\u201c','\"')
	text = (str(text)).replace('\u201d','\'')
	text = (str(text)).replace('\u2019s','\'')
	text = (str(text)).replace('\u00e0','à')
	text = (str(text)).replace('\u00e7','ç')
	text = (str(text)).replace('\u00e9','é')
	text = (str(text)).replace('&#xC4;','Ä')
	text = (str(text)).replace('&#xD6;','Ö')
	text = (str(text)).replace('&#xDC;','Ü')
	text = (str(text)).replace('&#xE4;','ä')
	text = (str(text)).replace('&#xF6;','ö')
	text = (str(text)).replace('&#xFC;','ü')
	text = (str(text)).replace('&#xDF;','ß')
	text = (str(text)).replace('&#xE9;','é')
	text = (str(text)).replace('&#xB7;','·')
	text = (str(text)).replace("&#x27;","'")
	text = (str(text)).replace("&#x26;","&")
	text = (str(text)).replace("&#xFB;","û")
	text = (str(text)).replace("&#xF8;","ø")   
	text = (str(text)).replace("&#x21;","!")                          
	text = (str(text)).replace("&#x3f;","?")
        text = (str(text)).replace("&#304;",  "I")       
        text = (str(text)).replace("&#304;",  "I")
        text = (str(text)).replace("&#39;", "'")
        text = (str(text)).replace('&#39;',"ş")
	text = (str(text)).replace('&#8230;','...')
	text = (str(text)).replace('\u2026','...')  
	text = (str(text)).replace('c59f','ş')
	text = (str(text)).replace('c4b1','ı')
        text = (str(text)).replace('c3b6','ö')
        text = (str(text)).replace('c3bc','ü')                    
        text = (str(text)).replace('c387','Ç')
        text = (str(text)).replace('c3a7','ç')
        text = (str(text)).replace('c396','Ö')
        text = (str(text)).replace('&#8234;','')
	text = (str(text)).replace("&#39;", "'")
        text = (str(text)).replace('&#39;',"ş")
	text = (str(text)).replace('&#8230;','...')
	text = (str(text)).replace('\u2026','...')
	text = (str(text)).replace('&hellip;','...')
	text = (str(text)).replace('&#8234;','')
        text = (str(text)).replace("&#231;", "ç")
        text = (str(text)).replace('&#351;',"ş")
	text = (str(text)).replace('&#350;','ş')
	text = (str(text)).replace('&#246;','ö')
	text = (str(text)).replace('&#214;','Ö')
	text = (str(text)).replace('&#199;','Ç')
        text = (str(text)).replace("0x99","?")
        text = (str(text)).replace('&#220;','Ü')
        text = (str(text)).replace('0xb8','')
        return text

                        
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def homeMovies365():                                                                                                                
    oGui = cGui()
    getKey()              
    tarzlistesi= []                
    tarzlistesi.append(("[B][COLOR khaki]Movies[/COLOR][/B]", "movlanguages",  "http://www.365movies.tv/en/movies/-/1/-/-/-/", "mov365.png"))
    tarzlistesi.append(("[B][COLOR khaki]Serials[/COLOR][/B]", "showlanguages","http://www.365movies.tv/en/movies/-/1/-/-/-/", "mov365.pn"))
    tarzlistesi.append(("[B][COLOR khaki]Search[/COLOR][/B]", "listSearch", "http://www.365movies.tv/en/movies/-/1/-/-/-/", "mov365.png"))

              
    for sTitle,mode,sUrl,sPicture in tarzlistesi:
        page=1
        Title ="You can change language ... Audio setting ..\xd0\x92\xd1\x8b \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x82\xd0\xb5 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x82\xd1\x8c \xd1\x8f\xd0\xb7\xd1\x8b\xd0\xba \x2e\x2e\x2e \xd0\x9d\xd0\xb0\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb9\xd0\xba\xd0\xb8 \xd0\xb7\xd0\xb2\xd1\x83\xd0\xba\xd0\xb0 \x2e\x2e"
	sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        
        oOutputParameterHandler.addParameter('page', page)
        if sTitle == 'sortn':
             oGui.addMovie(SITE_IDENTIFIER, 'filtr', sTitle, sPicture, sPicture, Title, oOutputParameterHandler)
 
        else:
             oGui.addMovie(SITE_IDENTIFIER, mode, sTitle, sPicture, sPicture, Title, oOutputParameterHandler)
    oGui.setEndOfDirectory()
def showlanguages():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    ttitl = oInputParameterHandler.getValue('siteUrl')
    url = "http://www.365movies.tv/en/sidebar" 
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)     
                                                       
    matches = scrapertools.find_multiple_matches(data, "<img alt='(.*?)' width='.*?' style='.*?' src='http://m1.medianetworkinternational.com/.*?' /></span></td><td><span id='span_link_sidebar' onClick=.*?pdateContent.document.getElementById.'track-genres-(.*?)'")
    for sTitle,value  in matches:
        sUrl = "http://www.365movies.tv/en/sidebar" 
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sitem', value)
        oOutputParameterHandler.addParameter('siteUrl', sTitle)
        if sTitle == "sortv":
            oGui.addDir(SITE_IDENTIFIER, 'tickets', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'showcatlanguages', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 
def showcatlanguages():
    oGui = cGui()
    itemlist = []
    page=1 
    oInputParameterHandler = cInputParameterHandler()
    katv= oInputParameterHandler.getValue('sitem')
    ttitl = oInputParameterHandler.getValue('siteUrl')
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/movies/-/1/-/-/-/')
    oOutputParameterHandler.addParameter('page', page)
    oOutputParameterHandler.addParameter('sortv', '-')
    oOutputParameterHandler.addParameter('katv', katv)
    
    oGui.addDir(SITE_IDENTIFIER, 'listserials365','[B][COLOR khaki]'+ttitl+'-All[/COLOR][/B]', 'search.png', oOutputParameterHandler)
    url = "http://www.365movies.tv/en/sidebar" 
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)    
    matches = scrapertools.find_multiple_matches(data, "<option value='(.+?)'>"+ttitl+" /(.+?)</option>")
    for value, sTitle in matches:
        #katv = scrapertools.find_single_match(data, "'track-genres-(.*?)'.*?<img alt='"+ttitl+"'")
        
        page=1        
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/movies/-/1/-/-/-/')
        oOutputParameterHandler.addParameter('page', page)
        oOutputParameterHandler.addParameter('sortv', value)
        oOutputParameterHandler.addParameter('katv', katv)
        if ttitl== "mmmmm":
            oGui.addDir(SITE_IDENTIFIER, 'listserials365', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'listserials365', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory()    
def movlanguages():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    ttitl = oInputParameterHandler.getValue('siteUrl')
    url = "http://www.365movies.tv/en/sidebar" 
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)     
                                                       
    matches = scrapertools.find_multiple_matches(data, "<img alt='(.*?)' width='.*?' style='.*?' src='http://m1.medianetworkinternational.com/.*?' /></span></td><td><span id='span_link_sidebar' onClick=.*?pdateContent.document.getElementById.'track-genres-(.*?)'")
    for sTitle,value  in matches:
        sUrl = "http://www.365movies.tv/en/sidebar" 
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sitem', value)
        oOutputParameterHandler.addParameter('siteUrl', sTitle)
        if sTitle == "sortv":
            oGui.addDir(SITE_IDENTIFIER, 'tickets', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'movcatlanguages', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 
def movcatlanguages():
    oGui = cGui()
    itemlist = []
    page=1 
    oInputParameterHandler = cInputParameterHandler()
    katv= oInputParameterHandler.getValue('sitem')
    ttitl = oInputParameterHandler.getValue('siteUrl')
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/movies/-/1/-/-/-/')
    oOutputParameterHandler.addParameter('page', page)
    oOutputParameterHandler.addParameter('sortv', '-')
    oOutputParameterHandler.addParameter('katv', katv)
    
    oGui.addDir(SITE_IDENTIFIER, 'listmovies365','[B][COLOR khaki]'+ttitl+'-All[/COLOR][/B]', 'search.png', oOutputParameterHandler)
    url = "http://www.365movies.tv/en/sidebar" 
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)    
    matches = scrapertools.find_multiple_matches(data, "<option value='(.+?)'>"+ttitl+" /(.+?)</option>")
    for value, sTitle in matches:
        #katv = scrapertools.find_single_match(data, "'track-genres-(.*?)'.*?<img alt='"+ttitl+"'")
        
        page=1        
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/movies/-/1/-/-/-/')
        oOutputParameterHandler.addParameter('page', page)
        oOutputParameterHandler.addParameter('sortv', value)
        oOutputParameterHandler.addParameter('katv', katv)
        if ttitl== "Serials":
            oGui.addDir(SITE_IDENTIFIER, 'listserials365', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'listmovies365', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 

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
    
def listmovies365():
	oGui = cGui()
       
	oInputParameterHandler = cInputParameterHandler()
        katv = oInputParameterHandler.getValue('katv')
        sortv = oInputParameterHandler.getValue('sortv')
        url = oInputParameterHandler.getValue('siteUrl')
	pg = oInputParameterHandler.getValue('page')
        page = int(pg) 
	links,pagin=getMovies365(url,page,katv,sortv)	
	itemz=links
	items = len(links)
	fold=False
	for f in itemz:    
             sTitle=f.get('title')
             url=f.get('href')
             sPicture=f.get('img')
             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteUrl',url )
             oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
             oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
	     oGui.addMovie(SITE_IDENTIFIER, 'getLinks365', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
	if pagin:
	   for f in pagin:	
                page=f.get('page')
                url=f.get('href')
                name=f.get('title')
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', url)            
                oOutputParameterHandler.addParameter('page', page) 
                oGui.addDir(SITE_IDENTIFIER, 'listmovies365',name, 'genres.png', oOutputParameterHandler)
            
        
	oGui.setEndOfDirectory()

def listserials365():
	oGui = cGui()

        oInputParameterHandler = cInputParameterHandler()
        katv = oInputParameterHandler.getValue('katv')
        sortv = oInputParameterHandler.getValue('sortv')

        url = oInputParameterHandler.getValue('siteUrl')
	pg = oInputParameterHandler.getValue('page')
        page = int(pg)
	links,pagin=getSerials365(url,page,katv,sortv)	
	itemz=links
	items = len(links)
	fold=False
	for f in itemz:    
             sTitle=f.get('title')
             url=f.get('href')
             sPicture=f.get('img')
             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteUrl',url )
             oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
             oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
	     oGui.addMovie(SITE_IDENTIFIER, 'ListEpisodes365', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
	if pagin:
	   for f in pagin:	
                page=f.get('page')
                url=f.get('href')
                name=f.get('title')
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', url)            
                oOutputParameterHandler.addParameter('page', page) 
                oGui.addDir(SITE_IDENTIFIER, 'listserials365',name, 'genres.png', oOutputParameterHandler)
 	oGui.setEndOfDirectory()           	
		



def getSerials365(url,page,katg,lang):

	out=[]
	npout=[]   
	    
        url='http://www.365movies.tv/en/movies/-/-/%s/%s/-/%d'%(katg,lang,page)
	url2='http://www.365movies.tv/en/pages/-/-/%s/%s/-/%d'%(katg,lang,page)
	html=getRequests(url)
	html=html.replace("\'",'"')
	html2=getRequests(url2)	
	
	lastpage=re.findall('>(.+?)</div>',html2,re.DOTALL)
	if lastpage:
		if page<int(lastpage[-1]):
			npout.append({'title':'[COLOR teal]Next_Page >>>[/COLOR]','href':'','img':'','plot':'','page':page+1}) 
		
	links=re.findall('<tr style="background: #EEEBDA;(.+?)"More info"',html,re.DOTALL)
	for link in links:
		t=re.findall('>([^<]+)<',link,re.DOTALL)
		imag=re.findall('src="([^"]+poster.+?png)"',link)[0]
		links=re.findall('\("([^"]+)", "([^"]+)", "[^"]+", 1\)',link)
		if t and links:
			event,urlenc=links[0]	
			title,x1,x2,qual= t[:4]
			qual=qual.replace('&nbsp;|&nbsp;','')
			ftitle='%s (%s)'%(title,qual)
			plot=re.findall('Story: </b>(.+?)<br>',link)[0]
			href=re.findall('href="(\/[^"]+)"',link)[0]
			href=re.findall('(\w+$)',href)[0]
			
			href='http://www.365movies.tv/en/links/'+href 

			out.append({'title':ftitle,'href':href,'img':imag,'plot':PLchar(plot),'code':qual})
	return out,npout	
def ListEpisodes365():
	oGui = cGui()
	
	oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        title = oInputParameterHandler.getValue('sMovieTitle')
        links=getEpisodes365(url,title)
	itemz=links
	items = len(links)

	fold=False
	for f in itemz:
	     sTitle=f.get('title')
             url=f.get('href')
             sPicture=f.get('img')
             sPicture =alfabekodla(sPicture)
             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteUrl',url )
             oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
             oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
	     oGui.addMovie(SITE_IDENTIFIER, 'getLinks365', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

	oGui.setEndOfDirectory()	



def getLinks365():
	oGui = cGui()
	import movies365 as s
        movie= movie=True
	oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        nme = oInputParameterHandler.getValue('sMovieTitle')
        rys = oInputParameterHandler.getValue('sThumbnail')
        links=getVideos365(url,movie,rys,nme)
	itemz=links
	items = len(links)

	fold=False
	for f in itemz:
	     sTitle=f.get('title')
             url=f.get('href')
             sPicture=f.get('img')
             sPicture =alfabekodla(sPicture)
             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteUrl',url )
             oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
             oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
	     oGui.addMovie(SITE_IDENTIFIER, 'Play365', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

	oGui.setEndOfDirectory()	



def listSearch():
	oGui = cGui()
       
	oInputParameterHandler = cInputParameterHandler()
	pg = oInputParameterHandler.getValue('page')
  	d = xbmcgui.Dialog().input(u'Search...', type=xbmcgui.INPUT_ALPHANUM)
	if d:
	   pg = int(pg)
	   movies,serials,pagin=getSearch(pg,d)
	   if movies:
	      itemz=movies
	      items = len(movies)
	      for f in itemz:
                  sTitle=f.get('title')
                  url=f.get('href')
                  sPicture=f.get('img')
                  oOutputParameterHandler = cOutputParameterHandler()
                  oOutputParameterHandler.addParameter('siteUrl',url )
                  oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
                  oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
	          oGui.addMovie(SITE_IDENTIFIER, 'getLinks365', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
	      if serials:
		itemz=serials
		items = len(serials)

		for f in itemz:
                    image=f.get('img')
                    url=f.get('href')
                    name=f.get('title')
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', url)            
                     
                    oGui.addDir(SITE_IDENTIFIER, 'listEpisodes365',name, image, oOutputParameterHandler)
            
        
	oGui.setEndOfDirectory()



	
def getEpisodes365(url,title):
	out=[]
	html=getRequests(url)
	links=re.findall("""onclick="showEpisode\('.+?', '(.+?)', '.+?', '.+?'\)"><b>(.+?)</b>""",html)
	for epi,num in links:
		
		urlk= parseDOM(html, 'div', attrs={'id': epi})[0]
		urlk=urlk.replace("\'",'"')	
		urlk=urlk.encode('utf-8')

		href=urllib.quote(str(urlk))
		title=re.findall('^(.+?Episode\s*)',title)[0]		
		ftitle='%s%02d'%(title,int(num))
		out.append({'title':ftitle,'href':href,'img':rys,'plot':'','code':''})
	return out
	

	
def getMovies365(url,page,katg,lang):
	out=[]
	npout=[]
	url='http://www.365movies.tv/en/movies/-/1/%s/%s/-/%d'%(katg,lang,page)
	url2='http://www.365movies.tv/en/pages/-/1/%s/%s/-/%d'%(katg,lang,page)
	html=getRequests(url)
	html=html.replace("\'",'"')
	html2=getRequests(url2)	
	
	lastpage=re.findall('>(.+?)</div>',html2,re.DOTALL)
	if lastpage:
		if page<int(lastpage[-1]):
			npout.append({'title':'[COLOR teal]Next_Page >>>[/COLOR]','href':'','img':'','plot':'','page':page+1}) 
		
	links=re.findall('<tr style="background: #EEEBDA;(.+?)"More info"',html,re.DOTALL)
	for link in links:
		t=re.findall('>([^<]+)<',link,re.DOTALL)
		imag=re.findall('src="([^"]+poster.+?png)"',link)[0]
		links=re.findall('\("([^"]+)", "([^"]+)", "[^"]+", 1\)',link)
		if t and links:
			event,urlenc=links[0]	
			title,x1,x2,qual= t[:4]
			qual=qual.replace('&nbsp;|&nbsp;','')
			ftitle='%s (%s)'%(title,qual)
			plot=re.findall('Story: </b>(.+?)<br>',link)[0]
			href=re.findall('href="(\/[^"]+)"',link)[0]
			href=re.findall('(\w+$)',href)[0]
			href='http://www.365movies.tv/en/links/'+href 
			out.append({'title':ftitle,'href':href,'img':imag,'plot':PLchar(plot),'code':qual})
	return out,npout

def getSearch(pg,d):
	fout=[]
	sout=[]
	npout=[]
	url='http://www.365movies.tv/en/movies/-/-/-/-/%s/%d'%(d,pg)
	url2='http://www.365movies.tv/en/pages/-/-/-/-/%s/%d'%(d,pg)
	html=getRequests(url)
	html=html.replace("\'",'"')
	html2=getRequests(url2)	
	
	lastpage=re.findall('>(.+?)</div>',html2,re.DOTALL)

	if lastpage:
		ab=int(lastpage[-1])
		if pg<int(lastpage[-1]):
			npout.append({'title':'[COLOR teal]Next_Page >>>[/COLOR]','href':'','img':'','plot':'','page':pg+1}) 
	links=re.findall('<tr style="background: #EEEBDA;(.+?)"More info"',html,re.DOTALL)
	for link in links:
		link=link.replace('<span style="background-color:yellow;"><font color="red">','[COLOR orange]').replace('</font></span>','[/COLOR]')
		
		t=re.findall('>([^<]+)<',link,re.DOTALL)
		imag=re.findall('src="([^"]+poster.+?png)"',link)[0]
		links=re.findall('\("([^"]+)", "([^"]+)", "[^"]+", 1\)',link)
		if t and links:
			event,urlenc=links[0]	
			title,x1,x2,qual= t[:4]
			if 'IMDb' not in x1:
				qual=x1
			qual=qual.replace('&nbsp;|&nbsp;','')
			ftitle='%s (%s)'%(title,qual)
			plot=re.findall('Story: </b>(.+?)<br>',link)[0]
			href=re.findall('href="(\/[^"]+)"',link)[0]
			href=re.findall('(\w+$)',href)[0]
			href='http://www.365movies.tv/en/links/'+href 
			typ=re.findall('href=".+?">([^>]+)</a>',link)[0]
			if 'serial' in typ.lower():
				sout.append({'title':ftitle,'href':href,'img':imag,'plot':PLchar(plot),'code':qual})
			else:
				fout.append({'title':ftitle,'href':href,'img':imag,'plot':PLchar(plot),'code':qual})
	return fout,sout,npout
					
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
#	addon.setSetting('keyk',ret)
	return ret	
	
		
	
def MgetLinks365():
	oGui = cGui()
	import movies365 as s
        movie= movie=True
	oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        nme = oInputParameterHandler.getValue('sMovieTitle')
        rys = oInputParameterHandler.getValue('sThumbnail')


        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+nme,url,'')
                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok    



def getVideos365(url,movie,rys,nme):
	out=[]
	if '<div' in url:
		html= urllib.unquote(url)
	else:
		html=getRequests(url)
		html=html.replace("\'",'"')
	links=re.findall('onClick=.*?,\s*"([^"]+)".',html,re.DOTALL)
	co=1
	for link in links:
		try:
			url=json.loads(base64.b64decode(link))    
			key = getKey()
                        src = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
			src=src.strip('"').replace('\\','')	
			src=re.findall("""src=['"](.+?)['"]""",src)[0]
			ftitle='[COLOR blue]%s - [/COLOR]Link %s'%(nme, co)
			out.append({'title':ftitle,'href':src,'image':rys})
			co+=1
		except:
			pass
	return out
	
def SgetVideos365(url,movie,rys,nme):
	out=[]

	html= urllib.unquote(url)
	links=re.findall('onClick=.*?,\s*"([^"]+)".',html,re.DOTALL)
	co=1
	for link in links:
		try:
			url=json.loads(base64.b64decode(link))    
			key = getKey()
                        src = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
			src=src.strip('"').replace('\\','')	
			src=re.findall("""src=['"](.+?)['"]""",src)[0]
			ftitle='[COLOR blue]%s - [/COLOR]Link %s'%(nme, co)
			out.append({'title':ftitle,'href':src,'image':rys})
			co+=1
		except:
			pass
	return out
	
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
	
	
			
def EnterVidSub(link):
	content,c =getUrlc(link)
	
	sout=[]
	hrefsubt=re.findall('<[^<]+src="(.+?)".+?label="(.+?)">',content)
	for uri,subtitle in hrefsubt:

		sout.append((subtitle,uri))
	if len(sout)>0:
		
		label = [x[0].strip() for x in sout]
		stream = [x[1].strip() for x in sout]
		sel = xbmcgui.Dialog().select('Select subtitle',label)
		
		if sel>-1:
			napis=stream[sel]
			content , c = getUrlc(napis)
			poprawiony=vtttostrLos(content)
			open(napisyLos, 'w').write(poprawiony)		
			nap=True
		else:
			nap=False
	else:
		nap=False
	return nap

	
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
		url = json.loads(base64.b64decode(link[0]))
		key = getKey()
                src= jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
		src =alfabekodla(src).replace('\\/', '/').replace("\\", "").replace('"', "").encode('utf-8')
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

def PLchar(char):
	if type(char) is not str:
		char=char.encode('utf-8')
	char = char.replace('\\u0105','\xc4\x85').replace('\\u0104','\xc4\x84')
	char = char.replace('\\u0107','\xc4\x87').replace('\\u0106','\xc4\x86')
	char = char.replace('\\u0119','\xc4\x99').replace('\\u0118','\xc4\x98')
	char = char.replace('\\u0142','\xc5\x82').replace('\\u0141','\xc5\x81')
	char = char.replace('\\u0144','\xc5\x84').replace('\\u0144','\xc5\x83')
	char = char.replace('\\u00f3','\xc3\xb3').replace('\\u00d3','\xc3\x93')
	char = char.replace('\\u015b','\xc5\x9b').replace('\\u015a','\xc5\x9a')
	char = char.replace('\\u017a','\xc5\xba').replace('\\u0179','\xc5\xb9')
	char = char.replace('\\u017c','\xc5\xbc').replace('\\u017b','\xc5\xbb')
	char = char.replace('&#8217;',"'")
	char = char.replace('&#8211;',"-")	
	char = char.replace('&#8230;',"...")	
	char = char.replace('&#8222;','"').replace('&#8221;','"')	
	char = char.replace('[&hellip;]',"...")
	char = char.replace('&#038;',"&")	
	char = char.replace('&#039;',"'")
	char = char.replace('&quot;','"')
	char = char.replace('&nbsp;',".").replace('&amp;','&')
	return char	


class JsUnwiser:
    def unwiseAll(self, data):
        try:
            in_data=data
            sPattern = 'eval\\(function\\(w,i,s,e\\).*?}\\((.*?)\\)'
            wise_data=re.compile(sPattern).findall(in_data)
            for wise_val in wise_data:
                unpack_val=self.unwise(wise_val)
                in_data=in_data.replace(wise_val,unpack_val)
            return re.sub(re.compile("eval\(function\(w,i,s,e\).*?join\(''\);}", re.DOTALL), "", in_data, count=1)
        except: 
            traceback.print_exc(file=sys.stdout)
            return data
        
    def containsWise(self, data):
        return 'w,i,s,e' in data
        
    def unwise(self, sJavascript):
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
            
        lI1l = ''.join(ll1l)
        I1lI = ''.join(l1lI)
        ll1I = 0;
        l1ll = [];
        for lIll in range(0,len(ll1l),2):
            ll11 = -1;
            if ( ord(I1lI[ll1I]) % 2):
                ll11 = 1;
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
			
def Play365():	
        import movies365 as s	
        oInputParameterHandler = cInputParameterHandler()
        nme = oInputParameterHandler.getValue('sMovieTitle')
        url = oInputParameterHandler.getValue('siteUrl')
        stream_url,napis = Play3651st(url)	
	play_item = xbmcgui.ListItem(path=stream_url)
	stream_url,napis = Play3651st(url)	
	if stream_url:
	        playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO);
                playlist.clear();
                listitem = xbmcgui.ListItem(nme)
                playlist.add(stream_url,listitem);
                player_type = sPlayerType()
                xbmcPlayer = xbmc.Player (player_type); 
                xbmcPlayer.play (playlist)  




       
def sPlayerType():
        oConfig = cConfig()
        sPlayerType = oConfig.getSetting('playerType')
        
        try:
            if (sPlayerType == '0'):
                cConfig().log("playertype from config: auto")
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                cConfig().log("playertype from config: mplayer")
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                cConfig().log("playertype from config: dvdplayer")
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False



def getSort(mv='film',sc='category'):
	label=[]
	value=[]
	
	if mv=='film':
		
		if sc=='category':
			url = 'http://losmovies.pro/movie-genres'
		elif sc=='country': 
			url = 'http://losmovies.pro/countries'
		elif sc=='language': 
			url = 'http://losmovies.pro/watch-movies-with-subtitles'
			
		content,c =getUrlc(url)
		result=parseDOM(content,'div', attrs={'class': "showEntities.+?"})[0]
		result=result.replace('&nbsp;',' ').replace('With ','')
		label=re.findall('showRowText">([^>]+)</div>',result) 
		value=re.findall('href="([^"]+)"\s*class="showRow showRowLinkMovies">',result)
		
	elif mv=='serial':
		if sc=='category':
			url = 'http://losmovies.pro/movie-genres'
		elif sc=='country': 
			url = 'http://losmovies.pro/countries'
		elif sc=='language': 
			url = 'http://losmovies.pro/watch-movies-with-subtitles'

		content,c =getUrlc(url)
		result=parseDOM(content,'div', attrs={'class': "showEntities.+?"})[0]
		result=result.replace('&nbsp;',' ').replace('With ','')
		label=re.findall('showRowText">([^>]+)</div>',result)
		value=re.findall('href="([^"]+)"\s*class="showRow showRowLinkTvShows">',result)
	return (label,value)	
