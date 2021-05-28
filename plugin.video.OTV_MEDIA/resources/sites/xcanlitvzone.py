#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'xcanlitvzone'
SITE_NAME = 'Canlitvzone'
MOVIE_VIEWS = (True, 'Canlitvzone')


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
     
def Canlitvzone():
    #linktv = cConfig().getSetting('pvr-view')
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.canlitv.me/tv2?sayfa=1')
    oGui.addDir(SITE_IDENTIFIER, 'Canlitv', '[COLOR khaki] CANLI TV[/COLOR]', 'https://www.canlitv.me/resim/logo.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()

def Canlitv():
    oGui = cGui()
   
    
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(Url)
    sHtmlContent = oRequestHandler.request()
    
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<li class="canlitvlist"><a href="(.*?)" title="(.*?)">.*?<img src="(.*?)"'
            
                                                     
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #prisNextPagent aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
           
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
 
        
        sNextPage =sEcho(str(Url))
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sNextPage)
        oGui.addDir(SITE_IDENTIFIER, 'Canlitv', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
  
    oGui.setEndOfDirectory()
UA ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
def ksshowBox19():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'https://izle.canlitvlive.io/tv8-canli-izle-210316'
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    from resources.lib import librecaptcha
    test = librecaptcha.get_token(api_key="6LcZ-dcZAAAAACzLqWbA3IrTSEG6gaPgDH22DpvO", site_url=sUrl,
                                  user_agent=UA, gui=False, debug=False)

    data = 'subform=unlock&g-recaptcha-response=' + test
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.setRequestType(1)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    oRequestHandler.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
    oRequestHandler.addHeaderEntry('Accept-Encoding', 'gzip')
    oRequestHandler.addHeaderEntry('Referer', sUrl)
    oRequestHandler.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
    oRequestHandler.addHeaderEntry('Content-Length', len(str(data)))
    oRequestHandler.addParametersLine(data)
    sHtmlContent = oRequestHandler.request()
    logger.info("Good sUnpacked :" +sHtmlContent)
    sPattern = '<a href="(.+?)" rel="external nofollow">'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):

        for aEntry in aResult[1]:
            sHosterUrl = aEntry
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
    oGui.setEndOfDirectory()

def s_Box19(Url,name):
    oGui = cGui()
   # name = alfabekodla(name)
    oParser = cParser()                   
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'https://www.canlitv.zone/' , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(Url, headers = headers).text
    url = re.findall('<iframe width="100%" height="100%" src="(.*?)"',data, re.S)[0]                 
     
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('Referer', Url)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
    oRequestHandler.addHeaderEntry('Accept-Language', 'en-US,en;q=0.9,de;q=0.8')
    
     

    oRequestHandler.addHeaderEntry('Upgrade-Insecure-Requests', '1')
 
    oRequestHandler.setRequestType(1)
    
    html = oRequestHandler.request()
    if PY3:
        html = to_utf8(html)
    sPattern = 'script type="text/javascript">(.*?)</script></body>'
    aResult = oParser.parse( html, sPattern)
    if (aResult[0] == True):
        content= unwise_process(aResult[1][0])
        m3u8 = re.findall("file: '(.*?)'",content, re.S)[0]
        logger.info("Good sUnpacked :" +m3u8 )
        m3u8=m3u8+ '|Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9&Host=ls2.livex.to&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        return  m3u8
#        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,m3u8,'')     


def sshowBox19():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
   # name = alfabekodla(name)
    oParser = cParser()                   
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'https://www.canlitv.zone/' , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(Url, headers = headers).text
    url = re.findall('<iframe width="100%" height="100%" src="(.*?)"',data, re.S)[0]                 
     
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('Referer', Url)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
    oRequestHandler.addHeaderEntry('Accept-Language', 'en-US,en;q=0.9,de;q=0.8')
    
     

    oRequestHandler.addHeaderEntry('Upgrade-Insecure-Requests', '1')
 
    oRequestHandler.setRequestType(1)
    
    html = oRequestHandler.request()
    if PY3:
        html = to_utf8(html)
    sPattern = 'script type="text/javascript">(.*?)</script></body>'
    aResult = oParser.parse( html, sPattern)
    if (aResult[0] == True):
        content= unwise_process(aResult[1][0])
        m3u8 = re.findall("file: '(.*?)'",content, re.S)[0]
        logger.info("Good sUnpacked :" +m3u8 )
        m3u8=m3u8+ '|Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9&Host=ls2.livex.to&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
      
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
			