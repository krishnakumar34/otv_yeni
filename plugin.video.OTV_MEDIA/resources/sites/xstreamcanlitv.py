#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
from resources.lib.player import cPlayer

SITE_NAME = 'streamcanlitv' 
SITE_IDENTIFIER = 'xstreamcanlitv'

MOVIE_VIEWS = (True, 'streamcanlitv')


def iostreamcanlitv():
      oGui = cGui()
      oInputParameterHandler = cInputParameterHandler()
      sUrl = 'https://www.canlitv.vin'
   
      oRequestHandler = cRequestHandler(sUrl)
      sHtmlContent = oRequestHandler.request()
  
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
      sPattern = '<a href="(https://www.canlitv.vin/kanallar.*?)" title=".+?">(.+?)</a></li>'
                                                                 
#      sHtmlContent = sHtmlContent
   
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
      sHtmlContent =to_utf8(sHtmlContent)
      oParser = cParser()
      aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
      if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[1]
            
                
            sUrl = str(aEntry[0])
            
            sTitle = malfabekodla(sTitle)
            sPicture = "https://www.canlitv.vin/resim/logo.png"
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'streamcanlitv2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
      oGui.setEndOfDirectory()
def streamcanlitv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    logger.info("cfkkk : %s" %sUrl)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =to_utf8(sHtmlContent)
    oParser = cParser()
    sHtmlContent = oParser.abParse(sHtmlContent, '<ul class="kanallar">', '<div class="clear">')
    sPattern = '<a href="(.*?)" title=".*?".*?<div class="kanallarlogo"><img class="lazy" src=".*?" data-original="(.*?)" alt="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
                                                                             
            sTitle = aEntry[2]
            sPicture = aEntry[1] 
            sUrl = str(aEntry[0])
                       
            sTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'sshowBox19', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
       
    oGui.setEndOfDirectory()







def sshowBox19():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    logger.info("Url : %s" %Url)
    oParser = cParser()                   
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'https://www.canlitv.zone/' , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(Url, headers = headers).text
    
    url = re.findall('<iframe width="100%" height="100%" rel="nofollow" src="(.*?)"',data, re.S)[0]                 
    logger.info("url : %s" %url) 
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
        m3u8=m3u8
        if 'tv8' in m3u8 or 'foxtv'in m3u8  or 'halktv' in m3u8:
           m3u8=m3u8.replace('.m3u8', '720.m3u8')
        Host = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',m3u8)
        ref ='|Host='+Host+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,m3u8+ref,'')           