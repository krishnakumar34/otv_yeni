#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'bicaps_net'
SITE_NAME = 'Bicaps.net'
SITE_DESC = 'Films  streaming'

URL_MAIN = 'https://www.fullhdfilmizlesene.net/'







 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://www.fullhdfilmizlesene.net/arama?ara=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        
def AlphaSearch():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
   
    
    for i in range(0,27) :
        
        
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
   
def bicaps(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/yeni-filmler')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'YENI FILMLER', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/en-cok-begenilen')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'EN COK BEGENILENLER', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/en-cok-izlenen')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'EN COK IZLENENLER', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.com/filmler')
    oGui.addDir(SITE_IDENTIFIER, 'FilmT', 'Film Türleri-Genre', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/filmizle/turkce-dublaj-film-izle')
    oGui.addDir(SITE_IDENTIFIER, 'Yillar', 'Yillar', 'genres.png', oOutputParameterHandler)

    sUrl = 'https://www.fullhdfilmizlesene.net/filmizle/turkce-dublaj-film-izle'

    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<h2>Filtreler</h2></div>(.+?)<div class="clear">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" title="(.+?)">.+?</a></li>'
    
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

def FilmT():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl)  
    oParser = cParser()               
    sPattern = '<div class="sidebar-icerik">(.+?)<div class="temizle">'
 
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" title="(.+?)">'
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
    sPattern = '<ul class="yil">(.+?)<div class="clear">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" title="(.+?)">.+?</a></li>'
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
    sPattern = '<img src=".*?" data-src="(.*?)" alt="(.*?)".*?<h2><a href="(.*?)".*?<span class="trz-tda">(.*?)</span>'
    oParser = cParser()                  
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):                              
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[1]+'-'+ aEntry[3]
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[2])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            #not found better way
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
           

        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
 
def __checkForNextPage(sHtmlContent):
    sPattern = "<li class='secili'><a href='javascript:void.+?'>+?<a href='(.+?)'"
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
    oParser = cParser()
    sPattern = '"vidid":"(.*?)","name":"(.*?)","nameTxt":"(.*?)".*?"types":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            
            Title = malfabekodla(aEntry[1])
            sTitle = malfabekodla(aEntry[2])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(Title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            if  'tr,en' in  aEntry[3]:
            
                  oGui.addTV(SITE_IDENTIFIER, 'ddstreams',  sTitle, '', sThumbnail, '', oOutputParameterHandler)
            else:
                  oGui.addTV(SITE_IDENTIFIER, 'hHosters',  sTitle, '', sThumbnail, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
def ddstreams():
    oGui = cGui()                           
    oInputParameterHandler = cInputParameterHandler()
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    name = oInputParameterHandler.getValue('sMovieTitle')
    url = oInputParameterHandler.getValue('siteUrl')
    liste = []
    liste.append( ['TR Dublaj','tr'] ) 
    liste.append( ['Altyazi','en'] ) 

    for Title,sUrl2 in liste:
               # https://www.fullhdfilmizlesene.com/player/api.php?id=3447&type=t&name=vmol&get=video&format=json                                               
         urlm= 'https://www.fullhdfilmizlesene.com/player/api.php?id=%s&type=t&name=%s&get=video&pno=%s&format=json&ssl=true'%(url,name,sUrl2)
         sTitle=name+'-'+ Title
         oOutputParameterHandler = cOutputParameterHandler()
         oOutputParameterHandler.addParameter('siteUrl', urlm)
         oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
         oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
         oGui.addDir(SITE_IDENTIFIER, 'mHosters',  sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()  


def fullhdfilmizlesene(url):
  
    page = getHtml(url).replace('\/','/').replace('\\','')
    url3 = re.findall('src="(.*?)"', page)[0]

    if  'vidmoly.to' in url3:
        url3 = 'https:' +url3
        referer=[('Referer',url3)]                                      
        pagem=gegetUrl(url3,headers=referer)
        m3u8 = re.findall('sources: ..file:"(.*?)"',pagem)[0]
        return m3u8
    else:                  
        urla= "https://www.fullhdfilmizlesene.com/"
        referer=[('Referer',url3)]                                      
        pag=gegetUrl(url3,headers=referer)  
        if  '"file"' in pag:
            m3u8_raw = re.findall('"file"\s*:\s*"(.*?)"',pag)[0]
          
            m3u8 =malfabekodla(m3u8_raw)
            return m3u8
        if  'skin: {name:' in pag:     
            link2 = re.findall('skin:[\s\S]*?(eval[\s\S]*?}\)\));', pag)[0]
            lin1 =  cPacker().unpack(link2)
            lin1 = lin1.replace("\\'","'")
            lin2 =  cPacker().unpack(lin1)
            lin2 = lin2.replace("\\","").replace("x","")
            urll = re.findall('"file":"(.*?)"', lin2)[0]
            m3u8 =hexDecode(urll)
            return m3u8
        else:     
            
            return 'https:' + re.findall('"hls"\s*:\s*"(.*?)"',pag)[0].replace("\\/", "/")
def hHosters():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        name = oInputParameterHandler.getValue('sMovieTitle')
        urlm= 'https://www.fullhdfilmizlesene.com/player/api.php?id=%s&type=t&name=%s&get=video&format=json'%(Url,name)
               
        logger.info('Url >%s' % Url )
        url =fullhdfilmizlesene(urlm)
        url = url+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')                                          

def mHosters():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        name = oInputParameterHandler.getValue('sMovieTitle')
        logger.info('Url >%s' % Url )
        url =fullhdfilmizlesene(Url)
        url = url+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')                                          
def partstreams():
    oGui = cGui()                           
    oInputParameterHandler = cInputParameterHandler()
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    name = oInputParameterHandler.getValue('sMovieTitle')
    url = oInputParameterHandler.getValue('sitUrl')
    eTitle = oInputParameterHandler.getValue('MovieTitle')
    liste = []
    liste.append( ['part 1','1'] ) 
    liste.append( ['part 2','2'] ) 
    liste.append( ['part 3','3'] ) 
    for Title,sUrl2 in liste:
        
         urlm= 'https://www.fullhdfilmizlesene.net/player/api.php?id=%s&type=p&name=%s&get=video&pno=%s&format=json&ssl=true'%(url,name,sUrl2)
#        link =  cRequestHandler(urlm).request() 
#        link= link.replace('\\','')
#        urlll =re.findall('<ifram.+?[SRC|src]=["|\'](.*?)["|\']',link,re.DOTALL)[0]
         sTitle=eTitle+'-'+ Title
         oOutputParameterHandler = cOutputParameterHandler()
         oOutputParameterHandler.addParameter('siteUrl', urlm)
         oOutputParameterHandler.addParameter('MovieTitle', str(sTitle))
         oGui.addDir(SITE_IDENTIFIER, 'lmstreams',  sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

def mmlmstreams():         
        oGui = cGui()
        
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
#    Title = oInputParameterHandler.getValue('sMovieTitle')
        sThumb = oInputParameterHandler.getValue('sThumbnail')
        name = oInputParameterHandler.getValue('MovieTitle')
#        data = cRequestHandler(url).request()  
        data=requests.session().get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36","cookie": "pl=1; list_type=normal; _ga=GA1.2.716840295.1568547510; _gid=GA1.2.469201334.1568547510; __cfduid=dd457b4ae0b423872250a867deacb90401568547501; fullhd_source=fast; fullhd_sourceType=t; plok=1; plokk=1; plox=1; __ga_rc=18","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
        data=str(data)
        aaddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,data,'')
def lmstreams():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Title= oInputParameterHandler.getValue('sMovieTitle')
        sUrl = oInputParameterHandler.getValue('siteUrl')
        data = getHtml(sUrl) 
   
        data= data.replace('\\','')
        link = re.findall('src=\"(.*?)"', data)[0]
        if  '/player/okru/' in link:
            link= link.replace('https://www.fullhdfilmizlesene.net/player/okru/plysv2.php?id=','').replace('&','?')
            link ='https://ok.ru/videoembed/'+ link
        if  'turkakisi.com/movie' in link:
            line =  cRequestHandler(link).request() 
            line= line.replace('\/\/cdn0','https://cdn0').replace('\/','/')
            urll =re.findall('"hls":"(.*?)"',line,re.DOTALL)[0]
            playOTV2(urll,Title)
        if  'cdn.dochub' in link:
            line =  cRequestHandler(link).request()                         
	   
            urll =re.findall('"file":"(.*?)"',line,re.DOTALL)[0]+'|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            playOTV2(urll,Title)
            return
        if  'gofastv2.php' in link:
	    #from adult_eu import *    
            urla= "https://www.fullhdfilmizlesene.net/"
            referer=[('Referer',urla)]                                      
            lin=gegetUrl(link,headers=referer)       
	    
            link2 = re.findall('skin:[\s\S]*?(eval[\s\S]*?}\)\));', lin)[0]
            lin1 =  cPacker().unpack(link2)
            lin1 = lin1.replace("\\'","'")
            lin2 =  cPacker().unpack(lin1)
            lin2 = lin2.replace("\\","").replace("x","")
            urll = re.findall('"file":"(.*?)"', lin2)[0].decode('hex')
            playOTV2(urll,Title)
            return
        if  'awsbeta17.php' in link:
	    #from adult_eu import *    
            lin2= link
            urll =re.findall('https://.*?&f=(.*?)&ip=.*?', lin2)[0]
            if 'BluRay' in urll:
                urll = 'http://secourgeon.cf'+ urll
            else:
                urll = 'http://fillingham.ga'+ urll
            playOTV2(urll,Title)
            return
        sstreams(link)


def playOTV2(Url,name):         
        
      
      aaddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,Url,'')
	
def aaddLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")                                                                  	

        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok  
def sstreams(urlll):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sHosterUrl= urlll
            
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
          sMovieTitle = cUtil().DecoTitle(sMovieTitle)
          cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
    oGui.setEndOfDirectory()

def streams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumbnail')
    urlm= 'https://www.fullhdfilmizlesene.net/player/api.php?id=%s&type=t&name=%s&get=video&format=json&callback=jQuery111203512659266764322_1561399057691&_=1561399057695'%(url,sMovieTitle)
    
    link =  getHtml(url)
    link= link.replace('\\','')
    sHosterUrl =re.findall('<ifram.+?[SRC|src]=["|\'](.*?)["|\']',link,re.DOTALL)[0]
            
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()