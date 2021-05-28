#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'hdfilmcehennemi_com'
SITE_NAME = 'HDfilmcehennemi'

 
URL_MAIN = 'https://www.hdfilmcehennemi.net/'
				

TURK_SINEMA = (True, 'showGenre')

HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
 
 
def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://www.hdfilmcehennemi.net/?s=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        
       
         
   
def hdfilmcehennemi(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi.net/dil/turkce-dublajli-film-izleyin/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Türkçe dublaj', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi.net/dil/turkce-altyazili-film-izleme-sitesi/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Türkçe altyazılı', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi.net/diziler/')
    oGui.addDir(SITE_IDENTIFIER, 'showDIZI', 'DIZILER', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi.net/')
    oGui.addDir(SITE_IDENTIFIER, 'FilmT', 'Özel Kategoriler', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi.net/')
    oGui.addDir(SITE_IDENTIFIER, 'Yillar', 'Yillar', 'genres.png', oOutputParameterHandler)

    sUrl = 'https://www.hdfilmcehennemi.net/'

    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<a class="nav-link.*?href="?(?P<url>(?:|https?://[^/]+)/(?:dil|tur|yil)/[^"\s>]+)(?:|[^>]+)>(?P<title>[^<]+)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
           
            Link = aEntry[0]
           
            sTitle  = sTitle  + ' [COLOR skyblue]' + sTitle +'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sTitle, '', '', '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    
def showDIZI(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sHtmlContent=getHtml(sUrl) 
    sPattern = '<div class="col-6 col-sm-3 poster-container px-2 px-sm-1 mb-3 mb-sm-2">.*?<a href="(.*?)".*?<img.*?data-src="(.*?)" alt="(.*?)".*?<h2 class="title px-3">(.*?)</h2>'
    oParser = cParser()                  
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):                              
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[2]                                                                                             
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            dec = aEntry[3]
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'showDIZI2', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
 
           

        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
def showDIZI2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl) #               
                
    sPattern = '<div class="card-list-item no-image col-12 col-sm-3">.*?<a href="(.*?)" title="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            sTitle = aEntry[1]
            sUrl = (aEntry[0])
            
            sDisplayTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def FilmT():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl)  
    oParser = cParser()               
    sPattern = '<span>Özel Kategoriler</span>(.+?)</nav>'

    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                              
                
    sPattern = '<a class="nav-link text-truncate" href="(https://www.hdfilmcehennemi.net/.+?)" title=".+?">(.+?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showMovies',  sTitle, '', sThumbnail, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def Yillar():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<li class="nav-item dropdown">(.+?)<li class="nav-item ">'
                 
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" class="dropdown-item">(.+?)</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showMovies',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

 
    oGui.setEndOfDirectory()
def searchowMovies(sUrl):
    oGui = cGui()
   
    data = cRequestHandler(sUrl).request() 
                          
    sHtmlContent = re.findall('<img src="(.*?)" alt="(.*?)" width=".*?" height=".*?" class="afis">.*?<div class="dty">.*?<a href="(.*?)"', data, re.S)
         
    for sPicture,sTitle,sUrl in sHtmlContent:
             
                       
            sTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()   
def showMovies(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sHtmlContent=getHtml(sUrl) 
    sPattern = '<div class="col-6 col-sm-3 poster-container px-2 px-sm-1 mb-3 mb-sm-2">.*?<a href="(.*?)".*?<img.*?data-src="(.*?)" alt="(.*?)".*?<h2 class="title px-3">(.*?)</h2>'
    oParser = cParser()                  
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
    if not (aResult[0] == False):                              
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[2]                                                                                             
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            dec = aEntry[3]
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
                         
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster

            if 'hdfilmcehennemi.net/dizi/' in sUrl:
                oGui.addMovie(SITE_IDENTIFIER, 'showDIZI2', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
 
           

        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
 
         

def __checkForNextPage(sHtmlContent):
    sPattern = '<a class="page-link" href="#">.*?</a></li><li class="page-item"><a href="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl
    return False
def blmstreams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    name= oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    data = cRequestHandler(sUrl).request() 
    aaddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,data,'')          
def aaddLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")                                                                  	

        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok  


def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl) 
    sHtmlContent= sHtmlContent.replace('<i class="tr-flag"></i>','<svg xmlns="tr-flag"/></svg>').replace('href="#" data-bs-toggle="modal" data-bs-target="#videoModal" data-trailer="','href="')
    
    oParser = cParser()                  
    sPattern = '<a class="nav-link.*?href="(.*?)".*?<svg xmlns=".*?"/></svg>(.*?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
                                    
                
            Title = malfabekodla(aEntry[1]).replace('Sinema Modu','')
            logger.info("body : %s" % Title)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]).replace('#',''))
            oOutputParameterHandler.addParameter('sMovieTitle', str(Title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            if not 'http' in str(aEntry[0]):
                oGui.addTV('youtubecom_tr', 'YouTubeplay',  Title, '', sThumbnail, '', oOutputParameterHandler)
            else:
            
                oGui.addTV(SITE_IDENTIFIER, 'streams',  Title, '', sThumbnail, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def streams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumbnail')
     
    link =  getHtml(url)
    link= link.replace('\\','')
    Url =re.findall('<iframe class=".*?" data-src="(.*?)"',link,re.DOTALL)[0]
    data =GetvideoUrl(Url)
    if  'https://hdfilmcehennemi.download' in data:
        data =Getvideo(data)
        data =data+ '|Referer=https://www.hdfilmcehennemi.net/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,data,'')   

       
def Getvideo(url):
    page = getHtml(url)
    page= page.replace('\n','').replace('\t','')
    links_labels = re.findall('<a class="btn btn-primary ms-2 me-2" href="(.*?)">(.*?)</a>', page)
    for link in links_labels:
        qualitylist.append(link[1])
        videolist.append('https://hdfilmcehennemi.download'+ link[0])
    return select(qualitylist,videolist)
   
                          
def GetvideoUrl(sUrl):  # Recupere les liens des regex
    chain  =getHtml(sUrl)
    if  'initPlayer("https://hdfilmcehennemi.fun' in chain:
        r = re.search('<a href="(https://hdfilmcehennemi.download/download.+?)"', chain)
        if (r):
            url = r.group(1)
       # url = url + '|Referer=' + sUrl + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' 
            return url
    else:
        r = re.search('sources:.+?file:"(https://.+?)"', chain)
        if (r):
            url = r.group(1)
            url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36' 
            return url
