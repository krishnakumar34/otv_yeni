#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *

SITE_IDENTIFIER = 'filmon_com'
SITE_NAME = 'Filmon TV'
SITE_DESC = 'Replay TV'

MOVIE_diziizle = 'http://www.tv8.com.tr'
URL_MAIN = 'http://www.filmon.com'
URL_PIC = 'http://s.dogannet.tv/'

MOVIE_GENRES = (True, 'showGenre')
MozillaAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
SERIE_SERIES = ('http://www.full-film.org/series/alphabet/', 'AlphaSearch')
SERIE_NEWS = ('http://www.full-film.org/series/page-1', 'showMovies')
  
ANIM_ANIMS = ('http://www.full-film.org/animes/alphabet/', 'AlphaSearch')
ANIM_NEWS = ('http://www.full-film.org/animes/page-1', 'showMovies')

URL_SEARCH = ('', 'showMovies')
def geetUrl(url, cookieJar=None,post=None, timeout=20, headers=None):

    cookieJar = CookieJar()     #opener = urllib2.install_opener(opener)
    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;



def load():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/') 
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler) 
    
    #rajout listage film nouveauté   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films Nouveautés', 'news.png', oOutputParameterHandler)
  
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_MOVIE[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_MOVIE[1], 'Films', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films Genres', 'genres.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'DIZILER-harfler', 'series.png', oOutputParameterHandler)
            
    oGui.setEndOfDirectory()

def sEcho(s):
    s=s
    if 'max_results=16&no_episode=true&start_index=16' in s:
       s=s.replace('max_results=16&no_episode=true&start_index=16','max_results=32&no_episode=true&start_index=32')
       return s 
    if 'max_results=32&no_episode=true&start_index=32' in s:
       s=s.replace('max_results=32&no_episode=true&start_index=32','max_results=64&no_episode=true&start_index=64')
       return s 
    if 'max_results=64&no_episode=true&start_index=64' in s:	
       s=s.replace('max_results=64&no_episode=true&start_index=64','max_results=128&no_episode=true&start_index=128')
       return s 
    if 'max_results=128&no_episode=true&start_index=128' in s:	
       s=s.replace('max_results=128&no_episode=true&start_index=128','max_results=266&no_episode=true&start_index=266')
       return s 
    if 'max_results=266&no_episode=true&start_index=266' in s:	
       s=s.replace('max_results=266&no_episode=true&start_index=266','max_results=522&no_episode=true&start_index=522')
       return s 
    if 'max_results=522&no_episode=true&start_index=522' in s:	
       s=s.replace('max_results=522&no_episode=true&start_index=522','max_results=800&no_episode=true&start_index=800')
       return s 
    return False  
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'https://www.youtube.com/results?search_query='+sSearchText  
            showMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
    

    
def FILMON():
    oGui = cGui()
    
    tarzlistesi = []
    
    tarzlistesi.append(("Filmon TV", "http://www.filmon.com/tv/live"))
#    tarzlistesi.append(("Filmon VOD", "http://www.filmon.com/vod/documentary"))
    for sTitle,sUrl2 in tarzlistesi:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Filmon VOD':
             oGui.addDir(SITE_IDENTIFIER, 'Filmonvod',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'Hosterster',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def Hosterster():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'http://miplayer.net/embed.php?id=ligtv1&width=650&height=480&autoplay=true', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    url = requests.get(url, headers = headers).text
#    url = unicode(url, 'latin-1')#converti en unicode
#    url= unicodedata.normalize('NFD',url).encode('ascii', 'ignore')#vire accent
  
    parse = re.search('var groups = \[(.*?)groups\[i\]', url, re.S)
    if parse:
       datarange = parse.group(1)
       Pattern = '\{"group_id":"(\d+)","id":"(\d+)","title":"(.*?)"'
       oParser = cParser()
       aResult = oParser.parse(datarange, Pattern)
       if (aResult[0] == True):
          total = len(aResult[1])
          for aEntry in aResult[1]:
             id= aEntry[0]
             sThumbnail = "http://static.filmon.com/couch/groups/%s/big_logo.png" % id
             sTitle = malfabekodla(aEntry[2])
             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteid',  id)
             oGui.addTV(SITE_IDENTIFIER, 'sshow3Filmon',  sTitle, '', sThumbnail, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()  
def showFilmon(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = 'class="group-item">.*?<a href="(.*?)">.*?<img class="logo" src="(.*?)" title="(.*?)"'
    
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
            oGui.addMovie(SITE_IDENTIFIER, 'show2Filmon', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
           
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()
def show2Filmon(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sUrll= sUrl
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = 'class="channel i-box-sizing".*?channel_id="(.*?)">.*?src="(.*?)".*?<strong class="channel_title">(.*?)</strong>'
    
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
                
            sUrl = aEntry[0]
            
           
            sTitle = malfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('Url', sUrll)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'show3Filmon', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                                       
           
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def sshow3Filmon():
   oGui = cGui()
   url="http://www.filmon.com/tv/live"
    
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'http://miplayer.net/embed.php?id=ligtv1&width=650&height=480&autoplay=true', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
   url = requests.get(url, headers = headers).text
   oInputParameterHandler = cInputParameterHandler()
	   
   id = oInputParameterHandler.getValue('siteid')
   parse = re.search('var groups = \[(.*?)groups\[i\]', url, re.S)
  
   datarange = parse.group(1)     
   data = re.findall('\{"id":(.*?)\}', datarange, re.S)
   logger.info("data : %s" %data ) 
   for sublink in data:
      sublink = sublink.replace('\\','')
      data1 = re.findall('^(.*?)group_id":%s,' % id, sublink, re.S)
      sPattern = '"big_logo":"https://static.filmon.com/assets/channels/(.*?)/big_logo.png".*?"title":"(.*?)","alias":".*?","description":"(.*?)"'
                                          
      oParser = cParser()
      aResult = oParser.parse(data1,sPattern)
    #print aResult
      if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            #sPic = str(aEntry[0])
            Url = aEntry[0]
            sTitle = malfabekodla( aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addDir(SITE_IDENTIFIER, 'Filmonvod33', sTitle, 'search.png', oOutputParameterHandler)
         
           
   oGui.setEndOfDirectory() 
                
                         
                             
      
               #am_url = re.findall('file: "(.*?)"', data)                                                                                                                                             
    #url =stream_url[0]                                                                                                                                                                           Referer:http://www.filmon.com/tv/
#    sHosterUrl = re.findall('serverURL:"(.*?)"', data, re.S)
 
  

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok

def Filmonvod(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="moviefilm">.*?<img src="(.*?)".*?<a href="(.*?)">(.*?)</a>'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '"id":".*?","vendorka_id":".*?","name":"(.*?)","slug":"(.*?)","position":".*?","content_count":".*?","updated_at":".*?","description":null,"images":"url":"(.*?)","width":.*?,"height":.*?,"type":"logo"'
    
    sHtmlContent = sHtmlContent.replace('\/','/').replace('[{','').replace('}]},{',',').replace('},{',',').replace('}]}]);',',') 
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[0]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[1]
            
            #not found better way
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            urlveri="http://www.filmon.com/api/vod/search?genre=%s&max_results=100&start_index=16" % sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', urlveri)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if 'Hotties' in sTitle:
                oGui.addMovie(SITE_IDENTIFIER, 'Filmonvodtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Comedy' in sTitle:
                oGui.addMovie(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'International' in sTitle:
                oGui.addMovie(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Podcast' in sTitle:
                oGui.addMovie(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'FilmonvodFilmon', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                           #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def Filmonvodtv():
    oGui = cGui()                         
    liste = []
    liste.append( ['Bikini','http://www.filmon.com/api/vod/search?from=tvguide&term=bikini&max_results=159'] ) 
    liste.append( ['Babes','http://www.filmon.com/api/vod/search?from=tvguide&term=babes&max_results=159'] ) 
    liste.append( ['Hotties','http://www.filmon.com/api/vod/search?genre=hotties&max_results=16&no_episode=true&start_index=0'] )
    liste.append( ['Girls','http://www.filmon.com/api/vod/search?from=tvguide&term=girls&max_results=159']) 
    liste.append( ['Beach','http://www.filmon.com/api/vod/search?from=tvguide&term=beach&max_results=159']) 
    for sTitle,sUrl2 in liste:
                   
#        urlveri  = "http://www.filmon.com/api/vod/search?from=tvguide&term=bikini&max_results=159" % sUrl2              
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'PROGRAMLAR':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLASİK DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'ArshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ATV YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'canlitvzoneBox', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'Filmonvod5',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()   



def Filmonvod5(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =sHtmlContent.replace('\/','/').replace('[]}','').replace('[{','').replace('}]},{',',').replace('},{',',').replace('}]}]);',',').replace('[','').replace(']','')
    sPattern = '"id":(.*?)".*?"title":"(.*?)".*?"image_id":(.*?),"'
                                          
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #print aResult
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
           
            sPic = str(aEntry[2])
            
               
            Url = aEntry[0]
                       
            sTitle = malfabekodla( aEntry[1])
            sPicture = "http://static.filmon.com/couch/channels/%s/big_logo.png" %sPic
            urlveri  = "http://www.filmon.com/api/vod/movie?id=%s" % Url.replace('","',',')  
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',urlveri)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'Filmonvod3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory() 


def Filmonvod2(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =sHtmlContent.replace('\/','/').replace('[]}','').replace('[{','').replace('}]},{',',').replace('},{',',').replace('}]}]);',',').replace('[','').replace(']','')
    sPattern = '"id":(.*?),".*?"title":"(.*?)".*?"image_id":(.*?),"'
                                          
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #print aResult
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
           
            sPic = str(aEntry[2])
            
               
            Url = aEntry[0]
                       
            sTitle = malfabekodla( aEntry[1])
            sPicture = "http://static.filmon.com/couch/channels/%s/big_logo.png" %sPic
            urlveri  = "http://www.filmon.com/api/vod/movie?id=%s" % Url.replace('","',',')  
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', urlveri)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'Filmonvod3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
           
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory() 
def FilmonvodFilmon():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    page = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =sHtmlContent.replace('\/','/').replace('[{','').replace('}]},{',',').replace('},{',',').replace('}]}]);',',')
    sPattern = 'id":(.*?),".*?title":"(.*?)","slug".*?"high","url":"(.*?)"'
                                                                       
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #print aResult
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle =aEntry[1]
            sPic = str(aEntry[0])
                            
            Url = aEntry[2]
                       
            sTitle = alfabekodla(sTitle)
            
            urlveri  = "http://www.filmon.com/api/vod/movie?id=%s" % sPic.replace('","',',')  
                        
            sPicture ='https://static.filmon.com/assets/vod_content/%s/thumb_220px.png'% sPic
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',urlveri)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'Filmonvod3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        sNextPage =sEcho(str(page))
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl',sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'FilmonvodFilmon', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def show3Filmon():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteid')
 
   
    
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

def Filmonvod3():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
	   
    Url = oInputParameterHandler.getValue('siteUrl')
    
    
 #   cookie = getUrl(url, output='cookie').result
#    headers = {'cookie': cookie,'X-Requested-With': 'XMLHttpRequest'}

   
    
    oRequest = cRequestHandler(Url)
    oRequest.addHeaderEntry('Referer', 'http://www.filmon.com/group/')
    oRequest.addHeaderEntry('Accept-Language', 'en-US,en;q=0.5')
    oRequest.addHeaderEntry('Host', 'www.filmon.com')
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    oRequest.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    sHtmlContent = oRequest.request()
  
#    sHtmlContent  = getUrl(url, cookie=cookie, headers=headers)
    sHtmlContent = str(sHtmlContent).replace('\/','/')                 
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
   
    sPattern = '"quality":"(.*?)","url":"(.*?)"'
    
    
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[0]
            h =  '|Referer=' + Url + '&User-Agent=Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
            sUrl = aEntry[1]+h
            sPicture='https://static.filmon.com/theme/img/watch-hd-without-ads.png'
           
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if 'Hotties' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Comedy' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'International' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Podcast' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

            else:
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
           
         
    oGui.setEndOfDirectory()
def Filmonvod33():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
	   
    url = oInputParameterHandler.getValue('siteUrl')
    
    Url='http://www.filmon.com/channel/' + url
 #   cookie = getUrl(url, output='cookie').result
#    headers = {'cookie': cookie,'X-Requested-With': 'XMLHttpRequest'}

   
    
    oRequest = cRequestHandler(Url)
    oRequest.addHeaderEntry('Referer', 'http://www.filmon.com/group/')
    oRequest.addHeaderEntry('Accept-Language', 'en-US,en;q=0.5')
    oRequest.addHeaderEntry('Host', 'www.filmon.com')
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    oRequest.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    sHtmlContent = oRequest.request()
  
#    sHtmlContent  = getUrl(url, cookie=cookie, headers=headers)
    sHtmlContent = str(sHtmlContent).replace('\/','/')                 
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '"quality":"(.*?)","url":"(.*?)"'
    
    
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            
            sTitle = aEntry[0]
            h =  '|Referer=' + Url + '&User-Agent=Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
            sUrl = aEntry[1]+h
            sPicture='https://static.filmon.com/theme/img/watch-hd-without-ads.png'
           
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if 'Hotties' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Comedy' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'International' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Podcast' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

            else:
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
           
         
    oGui.setEndOfDirectory()
   
   
def mFilmonvod33():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
	   
    url = oInputParameterHandler.getValue('siteUrl')
    logger.info("url: %s" % url )
    Url='https://www.filmon.com/api-v2/tvguide/' + url
    sHtmlContent =gegetHtml(Url)
    logger.info("sHtmlContent: %s" % str(sHtmlContent) )     

def mFilmonvod33():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
	   
    url = oInputParameterHandler.getValue('siteUrl')
    
    Url='https://www.filmon.com/api-v2/tvguide/' + url
    sHtmlContent =gegetHtml(Url)
    logger.info("sHtmlContent: %s" %sHtmlContent )     
    sPattern = '"quality":"(.*?)","url":"(.*?)"'
    
    
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
           
            sTitle = aEntry[0]
            h =  '|Referer=' + Url + '&User-Agent=Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
            sUrl = aEntry[1]+h
            sPicture='https://static.filmon.com/theme/img/watch-hd-without-ads.png'
           
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if 'Hotties' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Comedy' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'International' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Podcast' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'Filmonvod2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

            else:
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
           
         
    oGui.setEndOfDirectory()
   

def __NextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl =sUrl.replace('amp;', "")
    sPattern = 'data-url="(/actions/control/episodes.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_MAIN) + aResult[1][0]+'&skip=10'

    return False             
def __checkForNextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '</a> <a href="(/actions/control/episodes.*?)" class="syfno">Sonraki Sayfa &raquo;</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sUrl) + aResult[1][0]

    return False

def tv8canli():
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

def partplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
       
    stream = re.findall("type: 'GET'.*?url: '(.*?)',", data, re.S)
    url = "http://www.netd.com%s" %(stream[0])
    tarzlistesi= []
    tarzlistesi.append(("part=1", ""+url.replace('</span> <b>','<OTV>')))
    tarzlistesi.append(("part=2", ""+url.replace('part=1-6','part=2-6')))
    tarzlistesi.append(("part=3", ""+url.replace('part=1-6','part=3-6')))
    tarzlistesi.append(("part=4", ""+url.replace('part=1-6','part=4-6')))
    tarzlistesi.append(("part=5", ""+url.replace('part=1-6','part=5-6')))
    tarzlistesi.append(("part=6", ""+url.replace('part=1-6','part=6-6')))
        
    for sTitle,sUrl in tarzlistesi:
           
         
         
        sTitle = malfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'sshowBox3', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()




def sshowBox3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = malfabekodla(sTitle)
    
    
    
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
