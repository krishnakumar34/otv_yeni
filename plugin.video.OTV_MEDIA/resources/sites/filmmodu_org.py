#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'filmmodu_org'
SITE_NAME = 'FullFilm.org'

URL_SEARCH ='https://www.filmmodu.org/film-ara?term=' 
URL_MAIN = 'https://www.filmmodu.org/'
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'https://www.filmmodu.org/film-ara?term='+sSearchText  
            sUrl= sUrl.replace(' ','%20')
            showMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
def filmmodu():                                
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'YENI FILMLER', 'fimmodu.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/turkce-dublaj-izle')
    oGui.addDir(SITE_IDENTIFIER, 'Movies', 'Türkçe Dublaj Filmler ', 'fimmodu.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/altyazili-film-izle')
    oGui.addDir(SITE_IDENTIFIER, 'Movies', 'Altyazili Filmler ', 'fimmodu.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/boxset-filmler')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'EN COK BEGENILENLER', 'fimmodu.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/en-cok-izlenen-filmler')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'EN COK IZLENENLER', 'fimmodu.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/')
    oGui.addDir(SITE_IDENTIFIER, 'FilmT', 'Film Türleri-Genre', 'fimmodu.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/film-arsivi')
    oGui.addDir(SITE_IDENTIFIER, 'Movies', 'Arşiv Filmler', 'fimmodu.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/film-arsivi')
    oGui.addDir(SITE_IDENTIFIER, 'Yillar', 'Yila göre Türkçe Dublaj Filmler', 'fimmodu.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.filmmodu.org/film-arsivi')
    oGui.addDir(SITE_IDENTIFIER, '', '-----------------------------------------------------------------------', '', oOutputParameterHandler)

    sUrl = 'https://www.filmmodu.org/'

    sHtmlContent=getHtml(sUrl) 
    sPattern = '<div class="col-md-2 col-xs-6 movie">.+?<a href="(.+?)">.+?<img class="img-responsive" src="(.+?)".+?<p><span class="turkish-name">(.+?)</span></p>'
                                                      
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):                                                               
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
                                                                                               
#          language= aEntry[0]
#          if  'en' in language:
#            en ='Enlish'
#          if  'tr' in language:
#            tr ='TURKISH'
             
            
            sTitle = malfabekodla(aEntry[2])
            Link = aEntry[0]
            sPicture = str(aEntry[1])
            sTitle  = sTitle  + ' [COLOR skyblue]' + sTitle +'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oOutputParameterHandler.addParameter('sThumbnail', str(sPicture))
            oGui.addMovie(SITE_IDENTIFIER, 'Moviehost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()    

def FilmT():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    
    sHtmlContent=getHtml(sUrl)  
    oParser = cParser()               
#    sPattern = '<div class="col-lg-12">(.+?)div class="watch-page"'
     
#    aResult = oParser.parse(sHtmlContent, sPattern)
#    sHtmlContent = aResult
    sPattern = '<li><a title="(.+?)" href="(.+?)">.+?</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[0])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[1]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def Yillar():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
            
    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<select name="publish_year"(.+?)<div class="col-md-12 col-xs-6">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<option value="(.+?)">(.+?)</option>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
            sUrl = 'https://www.filmmodu.org/film-arsivi?genre=&publish_year='+aEntry[0]+'&language=turkce-dublaj&quality=&imdb=&order=created_at'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'Movies',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

 
    oGui.setEndOfDirectory()
def MsearchowMovies(sUrl):
    oGui = cGui()
   
    data = cRequestHandler(sUrl).request() 
    sHtmlContent = re.findall('<a href="(.*?)" type="button" class="btn btn-white dropdown-toggle">(.*?)</a>', data, re.S)
         
    for sPicture,sTitle,sUrl in sHtmlContent:
             
                       
            sTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()   
def showMovies(sUrl=False):
    logger.info("==entryUrl: %s" %   sUrl)
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    if not sUrl: sUrl = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent=getHtml(sUrl) 
    sPattern = '<div class="col-md-2 col-xs-6 movie">.+?<a href="(.+?)">.+?<img class="img-responsive" src="(.+?)".+?<p><span class="turkish-name">(.+?)</span></p>'
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
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'Moviehost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                sUrll ='https://www.filmmodu.org/'+sNextPage 
                logger.info("==sNextPage: %s" %  sUrll)
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrll)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()


def Movies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent=getHtml(Url) 
    sPattern = '<div class="col-md-3 col-xs-6 movie">.+?<a href="(.+?)">.+?<img class="img-responsive" src="(.+?)".+?<p><span class="turkish-name">(.+?)</span></p>'
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
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'Moviehost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                sUrll ='https://www.filmmodu.org'+sNextPage 
                logger.info("==sNextPage: %s" %  sUrll)
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrll)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()


def MshowMovies(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent=getHtml(Url) 
    sPattern = '<div class="col-md-2 col-xs-6 movie">.+?<a href="(.+?)">.+?<img class="img-responsive" src="(.+?)".+?<p><span class="turkish-name">(.+?)</span></p>'
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
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'Moviehost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                sUrll ='https://www.filmmodu.org/'+sNextPage 
                logger.info("==sNextPage: %s" %  sUrll)
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrll)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()



def Moviehost():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sHtmlContent =getHtml(sUrl)                                               
    
    oParser = cParser()
    sPattern = '<div class="col-md-5 col-xs-12 alternates">(.+?)<div class="col-md-12 col-xs-12">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)".*?">(.*?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
     
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])           
            sTitle = malfabekodla(sTitle)
                
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail', sThumbnail) 
            oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)

         
    oGui.setEndOfDirectory()   
                                                     
def __checkForNextPage(sHtmlContent):
    sPattern = "<li class='page'>.+?<a rel=\"next\" href=\"(.+?)\">"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl
    return False 
def gegetHtml(sUrl, data=None):  # S'occupe des requetes
        ref = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',sUrl)
        Referer='https://' +ref
        s = requests.Session()
        cookie_string = "; ".join([str(x) + "=" + str(y) for x, y in s.cookies.items()])

        oRequestHandler = cRequestHandler(sUrl)
        oRequestHandler.addHeaderEntry('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
        oRequestHandler.addHeaderEntry('Host',ref)
        oRequestHandler.addHeaderEntry('Referer',Referer)
        oRequestHandler.addHeaderEntry('If-None-Match',' W/"6a0ab883bee2a83697e97ea1f173d852"')
        oRequestHandler.addHeaderEntry('Cookie', cookie_string)
        data = oRequestHandler.request()
        return to_utf8(data )

                            

def Hosters():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        tum = oInputParameterHandler.getValue('sThumbnail')
        tum = tum.replace("https://s1.filmmodu.org/uploads/movie/poster", "").replace("https://s2.filmmodu.org/uploads/movie/poster", "")
        videoId  = re.findall('/(.*?)/thumb_.*?', tum)[0]
        name = oInputParameterHandler.getValue('sMovieTitle')
        if 'Türkçe Altyazılı' in name:                                  
            videoType ='en' 
            urli ='https://www.filmmodu.org/get-source?movie_id='+videoId+'&type='+videoType 
        
        if 'Türkçe Dublaj' in name:
            videoType ='tr' 
            urli ='https://www.filmmodu.org/get-source?movie_id='+videoId+'&type='+videoType
        if 'Fragman' in name: 
             
            sHoster = gegetHtml(Url)
            urli = re.findall('<iframe src="(.*?)" frameborder="0" allowfullscreen></iframe>',  sHoster)[0]
        import parsers        
        logger.info("==text_name: %s" %   name )
        logger.info("==text_videoId: %s" %   videoId )
        logger.info("==text_pattern: %s" %   urli)
        url = parsers.parse(urli)
        subs = []
        is_array = lambda var: isinstance(var, (list))
        if is_array(url):
           subs =url[1]
           url = url[0]
           isArray = True
        url = url.replace("#", "|")
        url = url.strip()  # 
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')    

def mHosters():
   oGui = cGui()     
   oInputParameterHandler = cInputParameterHandler()
   Url = oInputParameterHandler.getValue('siteUrl')
   if 'dublaj'in Url:
      videoType = 'tr' 
   else:  
      videoType = 'en'   
      if videoType:  
        name = oInputParameterHandler.getValue('sMovieTitle')
        sHtmlContent = gegetHtml(Url)
        import parsers
        oParser = cParser()
        sPattern1 = "<script>var videoId = '(.+?)'</script>.+?<script>var videoType = '(.+?)'</script>"
       # sPattern1 = "<script>var videoId = '(.+?)'</script>"
        aResult = oParser.parse(sHtmlContent, sPattern1)
        if (aResult[0] == True):
           for aEntry in aResult[1]:
     
            videoType  = aEntry[1]
            videoId  = str(aEntry[0])  
                   
            logger.info("==text_pattern: %s" %   videoType)
            sUrl='https://www.filmmodu.org/get-source?movie_id='+videoId+'&type='+videoType 
            
            url = parsers.parse(sUrl)
            subs = []
            is_array = lambda var: isinstance(var, (list))
            if is_array(url):
                subs =url[1]
                url = url[0]
                isArray = True
            url = url.replace("#", "|")
            url = url.strip()  # 
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')    




def mshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<iframe src="//www.facebook.com/','')


    sPattern = '<div id="movie" style="z-index: auto;"><p><iframe.+?src=[\'|"](.+?)[\'|"]'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:

            sHosterUrl = str(aEntry)
            if 'mail.ru' in sHosterUrl:
                       id_raw = re.findall('mail.ru/.*?mail/(.*?)/.*?/(\d*)\.html',  sHosterUrl)
                       if id_raw:
                           (m_user, m_id) = id_raw[0]
                       Url = "https://my.mail.ru/mail/%s/video/embed/_myvideo/%s?" % (m_user, m_id)
                       oOutputParameterHandler = cOutputParameterHandler()
                       oOutputParameterHandler.addParameter('siteUrl', str(Url))
                       oGui.addTV(SITE_IDENTIFIER, 'mailru', sMovieTitle, '', '', '', oOutputParameterHandler)	     

            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
              
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
         
       

    oGui.setEndOfDirectory()
