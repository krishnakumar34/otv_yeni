#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'diziizle_net'


SITE_NAME = 'diziizle.net'
URL_MAIN = 'https://www.diziizle.top'
URL_http = 'http:'
MOVIE_HD = (True, 'showGenre')
YURL_MAIN = 'http://www.youtube.com/embed/'



def turkdizi():
        oGui = cGui()
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'TRModules@http://www.bolumd.pw/tv@start@bolumd')
        oOutputParameterHandler.addParameter('sMovieTitle', 'BolumD dizi izle')
        oGui.addDir('turkvod_org', 'Liste', 'BolumD -Yabanci + Yerli Diziler ', 'dizibox.jpg', oOutputParameterHandler)

        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir('diziizlehdfull_net', 'diziizlehdfulltr','DiziBOX -Yabanci Diziler', 'Dizibox.png', oOutputParameterHandler)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir(SITE_IDENTIFIER, 'diziizle','Dizi izle Tüm Türk Dizileri', 'diziizle.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()

        oGui.addDir('koreanturk_com','koreanturk', 'Koreantürk Kore Film ve Dizileri', 'ktfooterlogo3.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.atv.com.tr/diziler')
        oGui.addDir('atv_com_tr', 'showSinema','ATV  YENİ DİZİLER', 'atv_com_tr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.atv.com.tr/klasik-diziler')
        oGui.addDir('atv_com_tr', 'ArshowSinema','ATV  Tüm Arşiv Dizileri A-Z', 'atv_com_tr.png', oOutputParameterHandler)

        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.kanald.com.tr/diziler')
        oGui.addDir('kanald_com_tr', 'showMovies', 'Kanal D Yeni DIZILER', 'kanald_com_tr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.kanald.com.tr/diziler/arsiv?page=1')
        oGui.addDir('kanald_com_tr', 'pageshowMovies', 'Kanal D Tüm Arşiv Dizileri', 'kanald_com_tr.png', oOutputParameterHandler)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.kanald.com.tr/diziler/arsiv?page=1')
        oGui.addDir('kanald_com_tr', 'showengelsiz', 'Kanal D Görme ve Işitme Engelliler için DIZILER', 'kanald_com_tr.png', oOutputParameterHandler)



        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.foxplay.com.tr/ajax/series/0/20/date')
        oGui.addDir('fox_com_tr', 'showdizim', 'FOX TV  Tüm  Dizileri ', 'fox_com_tr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.showtv.com.tr/diziler')
        oGui.addDir('showtv_com_tr', 'diziler','SHOW TV  YENI DIZILER', 'showtv_com_tr.png', oOutputParameterHandler)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.showtv.com.tr/diziler/arsivdeki-diziler')
        oGui.addDir('showtv_com_tr', 'showdizi','SHOW TV  Tüm Arşiv Dizileri', 'showtv_com_tr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.startv.com.tr/dizi')
        oGui.addDir('startv_com_tr', 'Diziler','STAR TV  YENI DIZILER', 'startv_com_tr.png', oOutputParameterHandler)
       
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.startv.com.tr/dizi')
        oGui.addDir('startv_com_tr', 'arsivdiziy','STAR TV  Tüm Arşiv Dizileri', 'startv_com_tr.png', oOutputParameterHandler)
       
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.trt1.com.tr/tv/diziler')
        oGui.addDir('trt_net_tr', 'trtvideo', 'TRT  YENI DIZILER', 'trt_net_tr.png', oOutputParameterHandler)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.trt1.com.tr/tv/arsiv')
        oGui.addDir('trt_net_tr', 'trtvideo', 'TRT  Tüm Arşiv Dizileri', 'trt_net_tr.png', oOutputParameterHandler)

        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.acunn.com/programlar')
        oGui.addDir('tv8_com_tr', 'programlar','TV 8  Diziler', 'tv8_com_tr.png', oOutputParameterHandler)

        
        oGui.setEndOfDirectory()  



def showSearch(): #affiche les genres
 oGui = cGui()
 sSearchText = oGui.showKeyBoard()
 if (sSearchText != False):
    sUrl = 'https://www.diziizle.top/?ara=' + sSearchText
    oRequestHandler = cRequestHandler(sUrl)
    data = oRequestHandler.request()
                         
    playlist = re.findall('<div class="resim">.*?<a href="(.*?)" title="(.*?)"><img src="(.*?)" ', data, re.S)
    for Url,sTitle,pic in playlist:
            
            sPicture ='https://www.diziizle.top'+ pic
            sUrl='https://www.diziizle.top'+ Url
            sTitle = malfabekodla(sTitle)    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addMovie(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

 oGui.setEndOfDirectory()  
         
def partnext(s):
    s=s
    if 'sayfa=1' in s:
        s=s.replace('sayfa=1','sayfa=1')
        return s 
    if 'sayfa=1' in s:
        s=s.replace('sayfa=1','sayfa=2')
        return s 
    if 'sayfa=2' in s:
        s=s.replace('sayfa=2','sayfa=3')
        return s 
    if 'sayfa=3' in s:	
        s=s.replace('sayfa=3','sayfa=4')
        return s 
    if 'sayfa=4' in s:	
        s=s.replace('sayfa=4','sayfa=5')
        return s 
    if 'sayfa=5' in s:	
        s=s.replace('sayfa=5','sayfa=6')
        return s 
    return False 

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

                       
                      

def diziizle():
    oGui = cGui()
                 
    tarzlistesi = []
    tarzlistesi.append(("ARAMA", "https://www.diziizle.top/diziler/"))
    tarzlistesi.append(("Son Eklenen Diziler", "https://www.diziizle.top/son-eklenen-diziler/"))
    tarzlistesi.append(("Son Eklenen Filmler", "https://www.diziizle.top/son-eklenen-filmler/"))

    
    
    tarzlistesi.append(("DIZILER", "https://www.diziizle.top/diziler/"))
    tarzlistesi.append(("DIZILER-ABC", "https://www.diziizle.top/diziler/"))
    tarzlistesi.append(("SINEMALAR", "https://www.diziizle.top/sinemalar/"))
    tarzlistesi.append(("SINEMALAR-ABC", "https://www.diziizle.top/sinemalar/"))
    tarzlistesi.append(("ANIMASYONLAR", "https://www.diziizle.top/sinemalar/?kategori=Animasyon"))
    tarzlistesi.append(("BELGESELLER", "https://www.diziizle.top/belgeseller/"))
    tarzlistesi.append(("BELGESELLER-ABC", "https://www.diziizle.top/belgeseller/"))
    for sTitle,sUrl in tarzlistesi:
       
        sPicture= 'http://www.diziizle.mobi/resimler/logo.png'
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == 'SINEMALAR-ABC':
             oGui.addDir(SITE_IDENTIFIER, 'SinemaABC',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'BELGESELLER-ABC':
             oGui.addDir(SITE_IDENTIFIER, 'belgeselABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DIZILER-ABC':
             oGui.addDir(SITE_IDENTIFIER, 'dizizleABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SINEMALAR':
             oGui.addDir(SITE_IDENTIFIER, 'sshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'BELGESELLER':
             oGui.addDir(SITE_IDENTIFIER, 'sshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Son Eklenen Filmler':
             oGui.addDir(SITE_IDENTIFIER, 'sshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Son Eklenen Diziler':
             oGui.addDir(SITE_IDENTIFIER, 'sshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'sshowSinema',  sTitle, 'genres.png', oOutputParameterHandler)

      
       
    oGui.setEndOfDirectory()
def belgeselABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []
    liste.append( ['A',sUrl+'?harf=a'] )
    liste.append( ['B',sUrl+'?harf=b'] )
    liste.append( ['C',sUrl+'?harf=c'] )
    liste.append( ['Ç',sUrl+'?harf=ç'] )
    liste.append( ['D',sUrl+'?harf=d'] )
    liste.append( ['E',sUrl+'?harf=e'] )
    liste.append( ['F',sUrl+'?harf=f'] )
    liste.append( ['G',sUrl+'?harf=g'] )
    liste.append( ['H',sUrl+'?harf=h'] )
    liste.append( ['I',sUrl+'?harf=i'] )
    liste.append( ['İ',sUrl+'?harf=i'] )
    liste.append( ['J',sUrl+'?harf=j'] )
    liste.append( ['K',sUrl+'?harf=k'] )
    liste.append( ['L',sUrl+'?harf=l'] )
    liste.append( ['M',sUrl+'?harf=m'] )
    liste.append( ['N',sUrl+'?harf=n'] )
    liste.append( ['O',sUrl+'?harf=o'] )
    liste.append( ['ö',sUrl+'?harf=ö'] )
    liste.append( ['P',sUrl+'?harf=p'] )
    liste.append( ['R',sUrl+'?harf=r'] )
    liste.append( ['S',sUrl+'?harf=s'] ) 
    liste.append( ['ş',sUrl+'?harf=ş'] ) 
    liste.append( ['T',sUrl+'?harf=t'] )
    liste.append( ['U',sUrl+'?harf=u'] )
    liste.append( ['Ü',sUrl+'?harf=Ü'] )
    liste.append( ['V',sUrl+'?harf=v'] )
    liste.append( ['W',sUrl+'?harf=w'] )
    liste.append( ['X',sUrl+'?harf=x'] )
    liste.append( ['Y',sUrl+'?harf=y'] )
    liste.append( ['Z',sUrl+'?harf=z'] )
    liste.append( ['0',sUrl+'?harf=0'] )
    liste.append( ['1',sUrl+'?harf=1'] )
    liste.append( ['2',sUrl+'?harf=2'] )
    liste.append( ['3',sUrl+'?harf=3'] )
    liste.append( ['4',sUrl+'?harf=4'] )
    liste.append( ['5',sUrl+'?harf=5'] )
    liste.append( ['6',sUrl+'?harf=6'] )
    liste.append( ['7',sUrl+'?harf=7'] )
    liste.append( ['8',sUrl+'?harf=8'] )
    liste.append( ['9',sUrl+'?harf=9'] )

               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'sshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def SinemaABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []
    liste.append( ['A',sUrl+'?harf=a'] )
    liste.append( ['B',sUrl+'?harf=b'] )
    liste.append( ['C',sUrl+'?harf=c'] )
    liste.append( ['Ç',sUrl+'?harf=ç'] )
    liste.append( ['D',sUrl+'?harf=d'] )
    liste.append( ['E',sUrl+'?harf=e'] )
    liste.append( ['F',sUrl+'?harf=f'] )
    liste.append( ['G',sUrl+'?harf=g'] )
    liste.append( ['H',sUrl+'?harf=h'] )
    liste.append( ['I',sUrl+'?harf=i'] )
    liste.append( ['İ',sUrl+'?harf=i'] )
    liste.append( ['J',sUrl+'?harf=j'] )
    liste.append( ['K',sUrl+'?harf=k'] )
    liste.append( ['L',sUrl+'?harf=l'] )
    liste.append( ['M',sUrl+'?harf=m'] )
    liste.append( ['N',sUrl+'?harf=n'] )
    liste.append( ['O',sUrl+'?harf=o'] )
    liste.append( ['ö',sUrl+'?harf=ö'] )
    liste.append( ['P',sUrl+'?harf=p'] )
    liste.append( ['R',sUrl+'?harf=r'] )
    liste.append( ['S',sUrl+'?harf=s'] ) 
    liste.append( ['ş',sUrl+'?harf=ş'] ) 
    liste.append( ['T',sUrl+'?harf=t'] )
    liste.append( ['U',sUrl+'?harf=u'] )
    liste.append( ['Ü',sUrl+'?harf=Ü'] )
    liste.append( ['V',sUrl+'?harf=v'] )
    liste.append( ['W',sUrl+'?harf=w'] )
    liste.append( ['X',sUrl+'?harf=x'] )
    liste.append( ['Y',sUrl+'?harf=y'] )
    liste.append( ['Z',sUrl+'?harf=z'] )
    liste.append( ['0',sUrl+'?harf=0'] )
    liste.append( ['1',sUrl+'?harf=1'] )
    liste.append( ['2',sUrl+'?harf=2'] )
    liste.append( ['3',sUrl+'?harf=3'] )
    liste.append( ['4',sUrl+'?harf=4'] )
    liste.append( ['5',sUrl+'?harf=5'] )
    liste.append( ['6',sUrl+'?harf=6'] )
    liste.append( ['7',sUrl+'?harf=7'] )
    liste.append( ['8',sUrl+'?harf=8'] )
    liste.append( ['9',sUrl+'?harf=9'] )

               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'sshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def dizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []
    liste.append( ['A',sUrl+'?harf=a'] )
    liste.append( ['B',sUrl+'?harf=b'] )
    liste.append( ['C',sUrl+'?harf=c'] )
    liste.append( ['Ç',sUrl+'?harf=ç'] )
    liste.append( ['D',sUrl+'?harf=d'] )
    liste.append( ['E',sUrl+'?harf=e'] )
    liste.append( ['F',sUrl+'?harf=f'] )
    liste.append( ['G',sUrl+'?harf=g'] )
    liste.append( ['H',sUrl+'?harf=h'] )
    liste.append( ['I',sUrl+'?harf=i'] )
    liste.append( ['İ',sUrl+'?harf=i'] )
    liste.append( ['J',sUrl+'?harf=j'] )
    liste.append( ['K',sUrl+'?harf=k'] )
    liste.append( ['L',sUrl+'?harf=l'] )
    liste.append( ['M',sUrl+'?harf=m'] )
    liste.append( ['N',sUrl+'?harf=n'] )
    liste.append( ['O',sUrl+'?harf=o'] )
    liste.append( ['ö',sUrl+'?harf=ö'] )
    liste.append( ['P',sUrl+'?harf=p'] )
    liste.append( ['R',sUrl+'?harf=r'] )
    liste.append( ['S',sUrl+'?harf=s'] ) 
    liste.append( ['ş',sUrl+'?harf=ş'] ) 
    liste.append( ['T',sUrl+'?harf=t'] )
    liste.append( ['U',sUrl+'?harf=u'] )
    liste.append( ['Ü',sUrl+'?harf=Ü'] )
    liste.append( ['V',sUrl+'?harf=v'] )
    liste.append( ['W',sUrl+'?harf=w'] )
    liste.append( ['X',sUrl+'?harf=x'] )
    liste.append( ['Y',sUrl+'?harf=y'] )
    liste.append( ['Z',sUrl+'?harf=z'] )
    liste.append( ['0',sUrl+'?harf=0'] )
    liste.append( ['1',sUrl+'?harf=1'] )
    liste.append( ['2',sUrl+'?harf=2'] )
    liste.append( ['3',sUrl+'?harf=3'] )
    liste.append( ['4',sUrl+'?harf=4'] )
    liste.append( ['5',sUrl+'?harf=5'] )
    liste.append( ['6',sUrl+'?harf=6'] )
    liste.append( ['7',sUrl+'?harf=7'] )
    liste.append( ['8',sUrl+'?harf=8'] )
    liste.append( ['9',sUrl+'?harf=9'] )

               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def sshowSinema(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
       #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="four-box"><div class="dizi-box2"><a title=".*?" href="(.*?)"><img src="(.*?)" width=".*?" height=".*?" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
       
        sHtmlContent = getHtml(Url)
                #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="resim">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width="100" height="140" alt="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
     
       
        for aEntry in aResult[1]:
           
            sTitle = malfabekodla(aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_http) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = 'https://www.diziizle.top' + sUrl
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'yenimp4canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
              
                logger.info("==sUrll: %s" %    sNextPage )
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl',Url + sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'sshowSinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def showSinema(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
       #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="four-box"><div class="dizi-box2"><a title=".*?" href="(.*?)"><img src="(.*?)" width=".*?" height=".*?" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
       
        sHtmlContent = getHtml(Url)
                #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="resim">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width="100" height="140" alt="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
          
    if not (aResult[0] == False):
        total = len(aResult[1])
     
       
        for aEntry in aResult[1]:
           
            sTitle = malfabekodla(aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_http) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = 'https://www.diziizle.top' + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
               # sUrll =  + str(Url) + sNextPage
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', Url + sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showSinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def FilmABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ssUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent = getHtml(ssUrl)
    oParser = cParser()
    sPattern = '<strong>(.+?)</strong>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    Pattern = '<a href="(.*?)">(.*?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = malfabekodla(aEntry[1])
                            
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(ssUrl) + sUrl 
           
            
            sThumbnail= 'http://www.diziizle.mobi/resimler/logo.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'showSinema', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
   
def pageshowMovies(sSearch = ''):
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
      
    Url = oInputParameterHandler.getValue('siteUrl')
   
    sHtmlContent = getHtml(Url)
        
                                                                                                                        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<div class="resim">.*?<a href="(.*?)" title="(.*?)"><img src="(.*?)"'
    
   
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
            Title = aEntry[1]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_http) + sPicture
                  
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = 'https://www.diziizle.top' + sUrl
           
                      
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addTV(SITE_IDENTIFIER, 'yenimp4canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        
           
        if not sSearch:
            sNextPage =__bolmcheckForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', Url + sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def __bolmcheckForNextPage(sHtmlContent):                     
    sPattern = 'class="aktifsyfno">.+?<a href="(.+?)"'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return  aResult[1][0].replace(' ','+')
    return False                        
                                                
              
def __mcheckForNextPage(sHtmlContent):                     
    urlan= re.findall('<link rel="canonical" href="(.+?)".+?<a href=".+?" class="aktifsyfno">.+?</a></span><a href="(.+?)"',sHtmlContent,  re.S)  
    for (url2),(url3) in urlan:
        ssUrl =''+url2+url3
        return ssUrl

    return False        
def yenimp4canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail= oInputParameterHandler.getValue('sThumbnail')
    data= gegetHtml(sUrl)
    if  data: 
        Url ='https://www.diziizle.top'+re.search('<iframe style="width:640px;height:360px" src="(.+?)"',  data).group(1)
        sHtmlContent = gegetHtml(Url)
        #logger.info("==text_name: %s" %    sHtmlContent )
        oParser = cParser()                                     
        sPattern1 = 'file: "(.+?)"'
        aResult = oParser.parse(sHtmlContent, sPattern1)
        if (aResult[0] == True):
            urli = aResult[1][0]               
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + sMovieTitle, urli , '')
        else:   
            sHosterUrl =re.search('<iframe src="(.+?)"', sHtmlContent).group(1)
            sHosterUrl=sHosterUrl.replace('&amp;','&').replace('?rel=0&showinfo=0','')
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
        
    oGui.setEndOfDirectory()





def enteraz(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content
                          
    playlist = re.findall('<option value="(.*?)">(.*?)</option>', data, re.S)
    for sUrl,sGenre in playlist:
            
            sGenre = malfabekodla(sGenre)    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox25', sGenre, '', '', '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()  







      



   
    
def __checkForNextPage(sHtmlContent):
    sHtmlContent= sHtmlContent.replace('amp;','')
        
    sPattern = 'class="aktifsyfno">.+?<a href="(.+?)"'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return  aResult[1][0].replace(' ','+')
    return False                        
    
    