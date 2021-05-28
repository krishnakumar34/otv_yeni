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
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, VSlog
from resources.lib.player import cPlayer

from resources.lib.gui.guiElement import cGuiElement

 
SITE_IDENTIFIER = 'filmifullizle_org'
SITE_NAME = 'FilmiFullizle.org'
SITE_DESC = 'Films streaming'
 
URL_MAIN = 'http://www.filmifullizle.tv/'

TURK_SINEMA = (True, 'showGenre')
        
import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
def sEcho(s):
    if not 'page/' in s:
        s = s +'page/1'
    if 'page/1' in s:
        s = s.replace('page/1', 'page/2')
        return s
    if 'page/2' in s:
        s = s.replace('page/2', 'page/3')
        return s
    if 'page/3' in s:
        s = s.replace('page/3', 'page/4')
        return s
    if 'page/4' in s:
        s = s.replace('page/4', 'page/5')
        return s
    if 'page/5' in s:
        s = s.replace('page/5', 'page/6')
        return s
    if 'page/6' in s:
        s = s.replace('page/6', 'page/7')
        return s
    if 'page/7' in s:
        s = s.replace('page/7', 'page/8')
        return s
    if 'page/8' in s:
        s = s.replace('page/8', 'page/9')
        return s
    if 'page/9' in s:
        s = s.replace('page/9', 'page/10')
        return s
    if 'page/10' in s:
        s = s.replace('page/10', 'page/11')
        return s
    if 'page/11' in s:
        s = s.replace('page/11', 'page/12')
        return s
    if 'page/12' in s:
        s = s.replace('page/12', 'page/13')
        return s
    if 'page/13' in s:
        s = s.replace('page/13', 'page/14')
        return s
    if 'page/14' in s:
        s = s.replace('page/14', 'page/15')
        return s
    if 'page/15' in s:
        s = s.replace('page/15', 'page/16')
        return s
    if 'page/16' in s:
        s = s.replace('page/16', 'page/17')
        return s
    if 'page/17' in s:
        s = s.replace('page/17', 'page/18')
        return s
    if 'page/18' in s:
        s = s.replace('page/18', 'page/19')
        return s
    if 'page/19' in s:
        s = s.replace('page/19', 'page/20')
        return s
    if 'page/20' in s:
        s = s.replace('page/20', 'page/21')
        return s
    if 'page/21' in s:
        s = s.replace('page/21', 'page/22')
        return s
    if 'page/22' in s:
        s = s.replace('page/22', 'page/23')
        return s
    if 'page/23' in s:
        s = s.replace('page/23', 'page/24')
        return s
    if 'page/24' in s:
        s = s.replace('page/24', 'page/25')
        return s
    if 'page/25' in s:
        s = s.replace('page/25', 'page/26')
        return s
    if 'page/26' in s:
        s = s.replace('page/26', 'page/27')
        return s
    if 'page/27' in s:
        s = s.replace('page/27', 'page/28')
        return s
    if 'page/28' in s:
        s = s.replace('page/28', 'page/29')
        return s
    if 'page/29' in s:
        s = s.replace('page/29', 'page/30')
        return s
    if 'page/30' in s:
        s = s.replace('page/30', 'page/31')
        return s
    if 'page/31' in s:
        s = s.replace('page/31', 'page/32')
        return s
    if 'page/32' in s:
        s = s.replace('page/32', 'page/33')
        return s
    if 'page/33' in s:
        s = s.replace('page/33', 'page/34')
        return s
    if 'page/34' in s:
        s = s.replace('page/34', 'page/35')
        return s
    if 'page/35' in s:
        s = s.replace('page/35', 'page/36')
        return s
    if 'page/36' in s:
        s = s.replace('page/36', 'page/37')
        return s
    if 'page/37' in s:
        s = s.replace('page/37', 'page/38')
        return s
    if 'page/38' in s:
        s = s.replace('page/38', 'page/39')
        return s
    if 'page/39' in s:
        s = s.replace('page/39', 'page/40')
        return s
    if 'page/40' in s:
        s = s.replace('page/40', 'page/41')
        return s
    if 'page/41' in s:
        s = s.replace('page/41', 'page/42')
        return s
    if 'page/42' in s:
        s = s.replace('page/42', 'page/43')
        return s
    if 'page/43' in s:
        s = s.replace('page/43', 'page/44')
        return s
    if 'page/44' in s:
        s = s.replace('page/44', 'page/45')
        return s
    if 'page/45' in s:
        s = s.replace('page/45', 'page/46')
        return s
    if 'page/46' in s:
        s = s.replace('page/46', 'page/47')
        return s
    if 'page/47' in s:
        s = s.replace('page/47', 'page/48')
        return s
    if 'page/48' in s:
        s = s.replace('page/48', 'page/49')
        return s
    if 'page/49' in s:
        s = s.replace('page/49', 'page/50')
        return s 
    return False   

def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://www.filmifullizle.tv/i.php?s=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return

def searchowMovies(sUrl):
    oGui = cGui()
    resp = net.http_GET(sUrl)
    data = resp.content                   
                               
    sHtmlContent = re.findall('<div class="list-item">.*?<a href="(.*?)"><img src="(.*?)" width=".*?" height=".*?" alt="(.*?)" /></a>', data, re.S)
         
    for sUrl,sPicture,sTitle in sHtmlContent:
             
            sPicture='https:'+ sPicture          
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()          
def AlphaSearch():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    dialog = cConfig().createDialog(SITE_NAME)
    
    for i in range(0,27) :
        cConfig().updateDialog(dialog, 36)
        
        if (i > 0):
            sTitle = chr(64+i)
        else:
            sTitle = '09'
            
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl + sTitle.upper() )
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal] Lettre [COLOR red]'+ sTitle +'[/COLOR][/COLOR]', 'genres.png', oOutputParameterHandler)
        
    cConfig().finishDialog(dialog)
    
    oGui.setEndOfDirectory()           
   
def filmifullizle(): 
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhan/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)

	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmifullizle.org')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Yeni Filmler', 'genres.png', oOutputParameterHandler)

    
    sUrl = 'http://www.filmifullizle.org/'

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
                 
    sPattern = '<li><a href="(https://www.filmifullizle.tv/kategori/filmler/.*?)">(.*?)</a></li>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sGenre = alfabekodla(aEntry[1])
            Link =aEntry[0] +'/page/1'
            sTitle = aEntry[1].decode("latin-1").encode("utf-8")
            sTitle = alfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sGenre, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    




 
def showMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.voirfilms.org/rechercher'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()

        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div style="float: left;">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        ssUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(ssUrl)
        sHtmlContent = oRequestHandler.request()
         
        
        sPattern = '<div class="list-item">.*?<a href="(.*?)"><img src="(.*?)".*?alt="(.*?)"'
    
    sHtmlContent = sHtmlContent.replace('.html','.html/6').replace('&#8211;','&').replace('&#8217;','')
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)                                             
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = alfabekodla(aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = sEcho(str(ssUrl))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()   
def __checkForNextPage(sHtmlContent):
    sPattern = '<ul><li class="page_info">.+?">.+?</a></li>.+?<li><a href="(.+?)">.+?</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False
 

def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    link =  cRequestHandler(sUrl).request()         
    ret =re.findall('<div class="part">.+?<span>(.+?)</span></a> <a href=',link,re.DOTALL)[0]
                                          
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('sMovieTitle', str(ret) )
    oGui.addDir(SITE_IDENTIFIER, 'showHosters', ret, 'genres.png', oOutputParameterHandler)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
     
    sPattern = '<div class="part">(.*?)<div class="player">' 
    oParser = cParser()
    sult = oParser.parse(sHtmlContent, sPattern)
    Pattern = '<a href="(.*?)" class="post-page-numbers"><span>(.*?)</span>'
    oParser = cParser()
    aResult = oParser.parse(sult, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[1]
            
            sDisplayTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()


def mshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sMovieTitle = alfabekodla(sMovieTitle)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('//ok.ru','http://ok.ru')
    sPattern = '<!--pagetitle:.+?<iframe.+?src=[\'|"](.+?)[\'|"]'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            sHosterUrl = str(aEntry)
            if "http://ok.ru/" in sHosterUrl:
                  sHosterUrl=sHosterUrl.replace('http://ok.ru/videoembed/',"")  
                  Url= "http://m.ok.ru/video/%s" % sHosterUrl
                  oOutputParameterHandler = cOutputParameterHandler()
                  oOutputParameterHandler.addParameter('siteUrl', Url)
                  oGui.addTV(SITE_IDENTIFIER, 'mokru', sMovieTitle, '', '', '', oOutputParameterHandler)     
            
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
               
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    oRequestHandler = cRequestHandler(sUrl)
    data = oRequestHandler.request();  
    Url = re.findall('<!--pagetitle:.+?<iframe.+?src=[\'|"](.+?)[\'|"]',  data)[0]
    if  'aHR0cHM6Ly93d3cueW91dHViZS' in Url:
	     Url = Url.replace('https://www.filmifullizle.tv/player/embed.php?vid=','')
	     Url = b64decode(Url)
    if  'www.filmifullizle.tv' in Url:
	    Url = Url.replace('https://www.filmifullizle.tv/player/embed.php?vid=','').replace('https://www.filmifullizle.tv/player/play.php?vid=','')
	    fembedvideo(Url,Title)
    if not 'http' in Url:
	   Url ='http:'+ Url
    oHoster = cHosterGui().checkHoster(Url)
    if (oHoster != False):
        cHosterGui().showHoster(oGui, oHoster, Url, sThumbnail)
    oGui.setEndOfDirectory()  
def  fembedvideo(Url,Title):
        oGui = cGui()
        player_url='https://www.filmifullizle.tv/player/ajax_sources.php'
        req = urllib2.Request(player_url)
       
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        req.add_header('Referer','https://www.filmifullizle.tv')
        req.add_header('X-Requested-With',' XMLHttpRequest')
        post={'vid':Url,'alternative':Title}

        post = urllib.urlencode(post)
        sJson=_get(req,post)
        aJson =re.findall('"file":"(.+?)","label":"(.+?)"',sJson,re.DOTALL)
        for catid,tid in aJson:                                 
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',  catid.replace('\/','/') )
            oOutputParameterHandler.addParameter('sMovieTitle', str(tid ) )
	    oGui.addDir(SITE_IDENTIFIER, 'PLAYPLAY', tid, 'genres.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()          
        
def PLAYPLAY():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = sUrl+"|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
         
        
        