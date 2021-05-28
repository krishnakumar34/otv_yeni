#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *

SITE_IDENTIFIER = 'trt_net_tr'
SITE_NAME = 'TRT_net_tr'


URL_MAIN = 'https://www.trt1.com.tr/'

icon = 'tv.png'        

videolist = []
qualitylist = []
linkler = []
kaynaklar = []

def sEcho(s):
    s=s
    if '0' in s:
       s=s.replace('0','1')
       return s 
    if '1' in s:
       s=s.replace('1','2')
       return s 
    if '2' in s:	
       s=s.replace('2','3')
       return s 
    if '3' in s:	
       s=s.replace('3','4')
       return s 
    if '4' in s:	
       s=s.replace('4','5')
       return s 
    if '5' in s:	
       s=s.replace('5','6')
       return s 
    if '6' in s:	
       s=s.replace('6','7')
       return s 
    if '7' in s:	
       s=s.replace('7','8')
       return s 
    if '8' in s:	
       s=s.replace('8','9')
       return s 
    if '9' in s:	
       s=s.replace('9','10')
       return s 
    if '10' in s:	
       s=s.replace('10','11')
       return s 
    if '11' in s:	
       s=s.replace('11','12')
       return s 
    if '12' in s:	
       s=s.replace('12','13')
       return s 
    if '13' in s:	
       s=s.replace('13','14')
       return s 
    if '14' in s:	
       s=s.replace('14','15')
       return s  
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

 
def trtnettr():
    oGui = cGui()
    
    tarzlistesi = []
                      
    tarzlistesi.append(("TRT TELEVIZYONLAR", "https://www.trtizle.com/api/live?path=/canli/tv/trt-1"))
    tarzlistesi.append(("TRT EBA", "https://www.trtizle.com/api/live?path=/canli/tv/trt-1"))
    tarzlistesi.append(("TRT RADYO", "https://www.trtizle.com/api/live?path=/canli/tv/trt-1"))
    tarzlistesi.append(("DIZILER", "https://www.trt1.com.tr/tv/diziler"))
    tarzlistesi.append(("DIZILER ARSIV", "https://www.trt1.com.tr/tv/arsiv"))
    for sTitle,sUrl2 in tarzlistesi:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'TRT TELEVIZYONLAR':
             oGui.addDir(SITE_IDENTIFIER, 'trttelevis',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'trtvideo', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DIZILER ARSIV':
             oGui.addDir(SITE_IDENTIFIER, 'trtvideo', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TRT EBA':
             oGui.addDir(SITE_IDENTIFIER, 'trttebaelevis', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TRT RADYO':
             oGui.addDir(SITE_IDENTIFIER, 'trtradyo', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()



def trtradyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
#    logger.info("sJson_auth: %s" % sJson )        
    aJson = json.loads(sJson)
    for cat in aJson["radioChannels"]:
            surl =cat['url']
            sTitle =cat['title']
            sPicture=cat['livestreamLogoUrl']
            cat=cat['description']
#            logger.info("sJson_blutv_d1: %s" % surl ) 
            sTitle = cUtil().CleanName(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',surl )
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'TRTRADYO', sTitle, sPicture, sPicture, cat, oOutputParameterHandler)
    oGui.setEndOfDirectory()       



def trttebaelevis():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
#    logger.info("sJson_auth: %s" % sJson )        
    aJson = json.loads(sJson)
    for cat in aJson["eduChannels"]:
            surl =cat['url']
            sTitle =cat['title']
            sPicture=cat['square_logo']
            cat=cat['description']
#            logger.info("sJson_blutv_d1: %s" % surl ) 
            sTitle = cUtil().CleanName(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',surl )
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'TRTcanli', sTitle, sPicture, sPicture, cat, oOutputParameterHandler)
    oGui.setEndOfDirectory()       

def trttelevis():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
#    logger.info("sJson_auth: %s" % sJson )        
    aJson = json.loads(sJson)
    for cat in aJson["tvChannels"]:
            surl =cat['url']
            sTitle =cat['title']
            sPicture=cat['square_logo']
            cat=cat['description']
#            logger.info("sJson_blutv_d1: %s" % surl ) 
            sTitle = malfabekodla(sTitle)
            sTitle = cUtil().CleanName(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',surl )
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'TRTcanli', sTitle, sPicture, sPicture, cat, oOutputParameterHandler)
    oGui.setEndOfDirectory()       




def Mtrttelevis():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')      
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
#    logger.info("sJson_auth: %s" % sJson ) 
    aJson = json.loads(sJson)                       
    for cat in aJson['metadata']:
    
       logger.info("sJson_auth: %s" % cat) 



def trtvideo(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sHtmlContent =getHtml(sUrl) 
    oParser = cParser()                                
    sPattern = '<li class="col-lg-3 col-sm-3 col-xs-6">.*?<div class="thumbnail"><a href="(.*?)">.*?<img class="img-responsive"  src="(.*?)" alt="(.*?)">'
    oParser = cParser()                                                                             
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle =aEntry[2]
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[0]
            sUrl ='https://www.trt1.com.tr/'+ sUrl#+'/bolum/1-bolum'
            #sUrl= str(sUrl).replace('/arsiv/','/diziler/')  
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) 
           
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'trtvideo2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
      


def bolumvideo2(sUrl):
    

    sHtmlContent =getHtml(sUrl) 
    oParser = cParser()                                                         
    sPattern1 = 'id="bolumler">.+?<li class="col-lg-3 col-sm-3 col-xs-6">.+?<a href="(.+?/.+?/.+?)/.+?"'
    aResult = oParser.parse(sHtmlContent, sPattern1)
    if (aResult[0] == True):
        sec = aResult[1][0]
        return  sec

def trtvideo2(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ssUrl = oInputParameterHandler.getValue('siteUrl')
    sUrll =bolumvideo2(ssUrl)
    sUrl ='https://www.trt1.com.tr/'+  sUrll+'/1-bolum'
    
    logger.info("sJson_auth: %s" % sUrl ) 
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('sMovieTitle', '1.Bölüm')
    oGui.addDir(SITE_IDENTIFIER, 'mp4canli', '1.Bölüm', 'filmkino.png', oOutputParameterHandler)

    oParser = cParser()
    sHtmlContent =getHtml(sUrl)     
    sPattern = '<div class="container list-content">(.+?)<!--//oyuncular end -->'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
         
    sPattern = '<a href="(.*?)" title="(.*?)">.*?<img src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)        
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle =aEntry[1]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'mp4canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
        
                    
def TRTcanli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
   
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')                                                                             
def TRTRADYO():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail= oInputParameterHandler.getValue('sThumbnail')
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,sThumbnail)                                                                             
def embed(url):
    page=getHtml(url)
    page=page.replace("\t",'').replace("\n",'').replace("[{",'')
    for match in re.finditer("src: '(.+?)'.+?label: '(.+?)'", page):
        qualitylist.append(match.group(2))
        videolist.append(match.group(1))
    if len(qualitylist) > 1:
        return select(qualitylist,videolist)
    else:
        return videolist[0]        
def mp4canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
       
    page=getHtml(Url)
    if '<iframe src="https://www.youtube.com/embed/' in  page:
        url = re.findall('<iframe src="(https://www.youtube.com/embed/.+?)"', page)[0]
        import parsers
        url = parsers.parse(url)
        subs = []
        is_array = lambda var: isinstance(var, (list))
        if is_array(url):
           subs =url[1]
           url = url[0]
           isArray = True
        url = url.replace("#", "|")
        url = url.strip()  # 

    else:
    
        #page=page.replace("\t",'').replace("\n",'').replace("[{",'')
        Urls =embed(Url)
        url = 'http:'+Urls   #re.findall("src: '(.+?)',", page)[0]
        logger.info("mt_auth: %s" % url ) 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')                                          
        
def __checkForNextPage(sHtmlContent):
    sPattern = "<li class='secili'><a href='javascript:void.+?'>+?<a href='(.+?)'"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False

					
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        