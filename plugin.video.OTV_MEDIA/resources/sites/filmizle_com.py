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

SITE_IDENTIFIER = 'filmizle_com'
SITE_NAME = 'filmozu2.com'
SITE_DESC = 'Films streaming'

TURK_SINEMA= (True, 'showGenre') 
URL_MAIN = 'http://filmozu2.com/'
UA ='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'

MOVIE_COMMENTS = (True, 'showGenre')
def encode_for_logging(c, encoding='ascii'):
    if isinstance(c, basestring):
        return c.encode(encoding, 'replace')
    elif isinstance(c, Iterable):
        c_ = []
        for v in c:
            c_.append(encode_for_logging(v, encoding))
        return c_
    else:
        return encode_for_logging(unicode(c))
      
def turksinema():
    oGui = cGui()
    liste = []
    liste.append( ['Film Izle','http://filmozu2.com/wp-content/themes/keremiya/logo/logo.png'] ) 

    liste.append( ['FilMakinesi','http://filmakinesi.org/wp-content/wptouch-data/uploads/mobil_logom.png'] ) 
    liste.append( ['Bicaps','http://www.bicaps.net/wp-content/uploads/bicapslogo31.png'])
    liste.append( ['Hdfilmcehennemi','https://www.hdfilmcehennemi.com/wp-content/themes/cehennem/img/logo-hdfilm.png']) 
    liste.append( ['FilmiFullizle','http://filmifullizle.co/_css/filmifullizle.png?v=1.8']) 
    liste.append( ['Jetfilmizle','https://s-media-cache-ak0.pinimg.com/originals/14/7b/2e/147b2e26bc8c2d86d8b38c7fb81ac744.png']) 
    liste.append( ['Türk Filmleri','https://fullonlinefilmizle.net/wp-content/uploads/turk-filmi-izle-turk-filmleri-full-hd-izle.png']) 
    liste.append( ['FullFilm','http://www.filmi-izle.org/wp-content/themes/KralFilm/logo/logo.png'])

    for sTitle,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sPicture)
        if sTitle == 'Türk Filmleri':
             oGui.addMovie(SITE_IDENTIFIER, 'turkfilmleri',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FilmiFullizle':
             oGui.addMovie(SITE_IDENTIFIER, 'filmifullizle',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Hdfilmcehennemi':
             oGui.addMovie(SITE_IDENTIFIER, 'hdfilmcehennemi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Bicaps':
             oGui.addMovie(SITE_IDENTIFIER, 'bicaps', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FilMakinesi':
             oGui.addMovie(SITE_IDENTIFIER, 'filmakinesi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FullFilm':
             oGui.addMovie(SITE_IDENTIFIER, 'fullfilm', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Jetfilmizle':
             oGui.addMovie(SITE_IDENTIFIER, 'jetfilmizle', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Film Izle':
             oGui.addMovie(SITE_IDENTIFIER, 'FilmIZLE', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

               
                    
                    
    oGui.setEndOfDirectory()                    

 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'http://filmozu2.com/?s=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        
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
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR azure] Lettre [COLOR teal]'+ sTitle +'[/COLOR][/COLOR]', 'genres.png', oOutputParameterHandler)
        
    cConfig().finishDialog(dialog)
    
    oGui.setEndOfDirectory()           
    
def FilmIZLE(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://filmozu2.com/')
    oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', 'Yeni Filmler', 'genres.png', oOutputParameterHandler)

    sUrl='http://filmozu2.com/'
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    
    
    oParser = cParser()
                
    sPattern = '<li class="cat-item cat-item-.*?"><a href="(.*?)" >(.*?)</a>'
    
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
            
            Link =aEntry[0]
            sPicture='http://files.softicons.com/download/business-icons/pretty-office-iv-icons-by-custom-icon-design/png/128/addressbook-search.png'

            sTitle = alfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addMovie(SITE_IDENTIFIER, 'sshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                  
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    

def searchowMovies(sUrl):
    oGui = cGui()
    oRequestHandler = cRequestHandler(sUrl)
    data = oRequestHandler.request()
                                
    sHtmlContent = re.findall('"titleNoFormatting":"(.*?)","unescapedUrl":".*?","url":"(.*?)"', data, re.S)
         
    for sTitle,sUrl in sHtmlContent:
             
                       
            sTitle = alfabekodla(sTitle)
            sPicture='http://files.softicons.com/download/business-icons/pretty-office-iv-icons-by-custom-icon-design/png/128/addressbook-search.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()  
def sshowMovies():
    oGui = cGui()
   

#        oInputParameterHandler = cInputParameterHandler()
#        Url = filmozu2.com/category/turk-filmleri/
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
#        sHtmlContent = sHtmlContent.replace('.html','.html/9')
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
                                                                                         

    sPattern = '<div class="moviefilm">.*?<img src="(.*?)".*?<div class="movief"><a href="(.*?)">(.*?)</a></div>'
    
      

  
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
            
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sThumbnail = str(aEntry[0])
            if not 'http' in  sThumbnail:
                 sThumbnail = str(URL_MAIN) +  sThumbnail
                
            
            sTitle =aEntry[2]
          
            sTitle = alfabekodla(sTitle)
             
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
           
      
        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
 
        oGui.setEndOfDirectory()
   




def wshowMovies():
#    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
#    Url='http://filmozu2.com/'
#    cookie = getUrl(Url, output='cookie').result
    headers={'User-Agent':UA,'Upgrade-Insecure-requests':'1','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate, br'}
    url  = requests.get(Url, headers = headers).text 

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
def mshowMovies():
#        sHtmlContent = sHtmlContent.replace('.html','.html/9')
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"'
                              
 
       
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
            
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sThumbnail = str(aEntry[1])
            if not 'http' in  sThumbnail:
                 sThumbnail = str(URL_MAIN) +  sThumbnail
                
            
           
          
            sTitle = aEntry[2]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
           

        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
   
                    
   
def __checkForNextPage(sHtmlContent):                     
    sPattern = '<a class="nextpostslink" rel="next" href="(.+?)">&raquo;</a>'
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
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="keremiya_part">(.+?)<div class="clear">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)"><span>(.*?)</span></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            urls = aEntry[0]
            sTitle = alfabekodla(aEntry[1])
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(urls))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'streams', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
    
def ODKosters():
    oGui = cGui()       
             
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
    sPattern = '<p><!--baslik:(.*?)--><iframe width="640" height="360" allowfullscreen src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

           
            Url = str(aEntry[1])            
            Title = str(aEntry[0])
             
            referer=[('Referer',sUrl)]
            streamurl=gegetUrl(Url,headers=referer)                    
            sHoster = re.findall(',path:"/videoembed/(.*?)"', streamurl)              
            
                
           
            Title = alfabekodla(Title)
            HosterUrl= "https://m.ok.ru/video/%s" % sHoster[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',HosterUrl)
            oGui.addTV(SITE_IDENTIFIER, 'mokru', Title, '', '', '', oOutputParameterHandler)   
                               
        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()


def MAKNEHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
    sPattern = '<!--baslik:Tek MAKİNE--><iframe src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            #si url cryptee mangacity algo
            Url = str(aEntry)            
           
           
            referer=[('Referer',sUrl)]
            streamurl=gegetUrl(Url,headers=referer)                    
            sHosterUrl = re.findall('src="(https://drive.google.com.*?)"', streamurl)
            sMovieTitle = alfabekodla(sMovieTitle) 
            
            oHoster = cHosterGui().checkHoster(sHosterUrl[0])

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

                
    sPattern = '<!--baslik:.*?--><.*?[SRC|src]=["|\'](.*?)["|\']'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            #si url cryptee mangacity algo
            sHosterUrl = str(aEntry)            
            if not 'http' in sHosterUrl:
                sHosterUrl ='http:' + sHosterUrl                    
            #xbmc.log( 'fini :' + str(sHosterUrl)) 
            
            #oHoster = __checkHoster(sHosterUrl)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sHosterUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle )
            oOutputParameterHandler.addParameter('sThumbnail', sThumbnail)
            oGui.addTV(SITE_IDENTIFIER, 'streams', sMovieTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()

   

def terscevir(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku        


def streams():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
    
    sPattern = '<!--baslik:.*?<.*?[SRC|src]=["|\'](.*?)["|\']'
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
            sHosterUrl = str(sHosterUrl).replace('.mkv.mp4','').replace('.avi.mp4','')
            if not 'http' in sHosterUrl:
                sHosterUrl ='https:' + sHosterUrl  
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            
            if (oHoster != False):
        
                sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        
        
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()

def showHostersRR():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = '<!--baslik:.*?--><.*?[SRC|src]=["|\'](.*?)["|\']'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            #si url cryptee mangacity algo
 
    sHoster =  aEntry
    sHoster=sHoster.replace("https://filmakinesi.org/player/url/","")
                
                        
                        
    url1=sHoster
              
    url2 = base64.b64decode(url1)
               
    url3 = terscevir(url2)            
    url3 =url3
    streamurl=base64.b64decode(url3)
    streamurl=streamurl.replace('g�',"")  
    streamurl=streamurl.replace("openload/","") 
                                      
    sHosterUrl= "https://openload.co/embed/%s" % (streamurl)

    sMovieTitle = alfabekodla(sMovieTitle) 
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
def kshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
   
    sHosterUrl = sUrl
 
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
  