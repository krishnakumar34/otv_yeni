#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
#from resources.lib.gui.guiElement import cGuiElement
import traceback 
SITE_IDENTIFIER = 'xCanLiTVlive'
SITE_NAME = 'CanLiTVlive.co'
MOVIE_VIEWS = (True, 'CanLiTVlive')
def sEcho(s):
    s=s
    if '=1' in s:
        s=s.replace('=1','=2')
        return s 
    if '=2' in s:
        s=s.replace('=2','=3')
        return s 
    if '=3' in s:	
        s=s.replace('=3','=4')
        return s 
    if '=4' in s:	
        s=s.replace('=4','=5')
        return s 
    if '=5' in s:	
        s=s.replace('=5','=6')
        return s 
  
def CanLiTVlive():
    oGui = cGui()
   
    
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
   

    sHtmlContent = getHtml(Url)
#    sHtmlContent =to_utf8(sHtmlContent)
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
           
            sTitle = aEntry[1]
            sPicture = aEntry[2]
            if not 'http' in sPicture:
                sPicture = str(urlkkmm) + sPicture   
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(urlkkmm) + sUrl
           
            #sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'sshowBox19', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        progress_.VSclose(progress_)
        sNextPage =sEcho(str(Url))
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sNextPage)
        oGui.addDir(SITE_IDENTIFIER, 'CanLiTVlive', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
  
    oGui.setEndOfDirectory()



def nunwise1(w):
    int1 = 0
    result = ""
    while int1 < len(w):
        result = result + chr(int(w[int1:int1 + 2], 36))
        int1 += 2
    return result

def sshowBox19():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
#    name = alfabekodla(name)
    oParser = cParser()                   
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'https://www.canlitv.zone/' , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(Url, headers = headers).text
    url = re.findall('<iframe width="100%" height="100%" src="(.*?)"',data, re.S)[0]                 
    url =url.replace('amp;','')
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('Referer', Url)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
    oRequestHandler.addHeaderEntry('Accept-Language', 'en-US,en;q=0.9,de;q=0.8')
    
                     

    oRequestHandler.addHeaderEntry('Upgrade-Insecure-Requests', '1')
 
    oRequestHandler.setRequestType(1)
    
    html = oRequestHandler.request()
    if PY3:
        html = to_utf8(html)
    logger.info("aEntry _auth: %s" % html)
#    content=JsUnwiser().unwiseAll(wc)
#    logger.info("Good Auth :" + content)
    sPattern = '<script type="text/javascript">;(.*?)</script></body>'
    aResult = oParser.parse(html, sPattern)
    if (aResult[0] == True):
       #aResult =str(aResult).replace("\\","")
       content= unwise_process(aResult[1][0])
       
      
        #logger.info("aEntry _auth: %s" % content )
       streams = re.search("file: '(.*?)'", content).group(1)
      # logger.info("Good sUnpacked :" +m3u8 )
       m3u8=streams + '|Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9&Host=ls2.livex.to&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
      
       addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,m3u8,'')     
 
      
def addLink(sTitle,sUrl,sThumbnail):
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    sUrl = sUrl.replace(' ', '%20')
    oGuiElement.setMediaUrl(sUrl)
    oGuiElement.setIcon(sThumbnail)
    oGuiElement.setThumbnail(sThumbnail)

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
        # tout repeter
    xbmc.executebuiltin('xbmc.playercontrol(RepeatAll)')

    oPlayer.startPlayer()
    return



