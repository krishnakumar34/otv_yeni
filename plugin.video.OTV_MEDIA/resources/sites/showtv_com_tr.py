#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding:cp1254 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'showtv_com_tr'
SITE_NAME= 'showtv_com_tr'
SITE_DESC = 'télévision'

URL_MAIN = 'https://www.showtv.com.tr'
from xcanlitvzone import sshowBox19              

MOVIE_HD = (True, 'showGenre')
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        
URL_MAINA = "http://www.showtv.com.tr/dizi/pagination/%s/%s/%s"
class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data
ua = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
def load():
    linktv = cConfig().getSetting('pvr-view')
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Pour Modifier ou  Ajouter des chaînes à FramaPad https://annuel.framapad.org/p/vstream [/COLOR]', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_FREE)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'FramaPad (Bêta)', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_SFR)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Sfr TV', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_ORANGE)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Orange TV', 'tv.png', oOutputParameterHandler)
    
    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_BG)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Bouygues TV', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_WEB)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Tv du web', 'tv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Tu veux voir ta chaîne sur Libretv.me alors partage ta chaîne![/COLOR]', 'libretv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_LIBRETV)
    oGui.addDir(SITE_IDENTIFIER, 'showLibreMenu', 'Libretv.me', 'libretv.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()

 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

def decodeHtml(data):

	
		data = data.decode('unicode-escape').encode('UTF-8') 
		return data
 
def showtvcomtr():
    oGui = cGui()
                
    tarzlistesi = []           
    tarzlistesi.append(("SHOWTV", "https://showtv.com.tr/canli-yayin"))
    tarzlistesi.append(("SHOWTV YEDEK", "https://www.canlitv.online/show-tv-canli"))
    
    tarzlistesi.append(("SHOWTURK", "http://www.showturk.com.tr/canli-yayin/showturk"))
    tarzlistesi.append(("SHOWMAX", "http://www.showmax.com.tr/canliyayin"))
    tarzlistesi.append(("HABERTURK", "https://www.haberturk.com/canliyayin"))
    tarzlistesi.append(("BLOOMBERGHT", "https://www.bloomberght.com/tv"))
    tarzlistesi.append(("Business HT", "https://businessht.bloomberght.com/canli-yayin"))
    tarzlistesi.append(("YENI DIZILER", "https://www.showtv.com.tr/diziler"))
    tarzlistesi.append(("ARSIVDEKI DIZILER", "https://www.showtv.com.tr/diziler/arsivdeki-diziler"))
    for sTitle,sUrl2 in tarzlistesi:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'YENI DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'diziler',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SHOWTV YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'sshowBox19', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ARSIVDEKI DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'showdizi', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SHOWMAX':
             oGui.addDir(SITE_IDENTIFIER, 'showtv2', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'HABERTURK':
             oGui.addDir(SITE_IDENTIFIER, 'showtv2', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showtv2',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
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
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()


def diziler(sSearch = ''):
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
 
    sHtmlContent =getHtml(sUrl) 
    oParser = cParser()
    sPattern = ' <div class="secondary-wrapper">(.+?)<li class="primary sub-item">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult

                                                                             
                                                                          

                    
    sPattern = '<li class="secondary">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)">'
                                                                                     

    sHtmlContent = sHtmlContent
  
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
                
            #not found better way
          
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'diziler2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        
        oGui.setEndOfDirectory()


def diziler2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    

    sHtmlContent =getHtml(sUrl) 
                    
#    sThumbnail  =re.search('<meta itemprop="image" content="(.+?)"/>', sHtmlContent).group(1) 
    oParser = cParser()
    sPattern = '</option>(.+?)<span class="link">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                
               
    Pattern = '<option value="" data-href="(.*?)" data-season-id="(.*?)" >(.*?)</option>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl 
           
                             
            sTitle =aEntry[1]+ '.Season-'+ aEntry[2]
            sTitle =malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'showplayer', sTitle, '', sThumbnail, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def mdiziler(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
          
      
        sPattern = '<li class="secondary">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)">'                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent= sHtmlContent.replace('<li class="white">','<li class="black">')


                                                                             
                                                                          

                    
        sPattern = '<li class="secondary">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)">'
                                                                                     

    sHtmlContent = sHtmlContent
    
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
                
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showdizi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        
        
           
        if not sSearch:
            sNextPage = __ccheckForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def mHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
     
    Pattern = '<a href="(/diziler?sw=.*?)">(.*?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            sTitle = sMovieTitle+' - '+aEntry[1]
            
            sDisplayTitle = cUtil().DecoTitle(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

       

    oGui.setEndOfDirectory()

def dizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
                      
    referer=[('Referer',Url)]
    url=gegetUrl(Url,headers=referer) 
       
            
    name ='test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            

def showplayer():
          oGui = cGui()
          oInputParameterHandler = cInputParameterHandler()
          rUrl  = oInputParameterHandler.getValue('siteUrl')
          name = oInputParameterHandler.getValue('sMovieTitle')
        
          UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    #+ '&User-Agent='+UA
                               
          referer=[('Referer', rUrl )]       
          auth  = gegetUrl(rUrl ,headers=referer)              
          auth =auth.replace('\/','/').replace('\u002D','-')
          url =re.search('"name":"Standart","file":"(.*?)"', auth).group(1)
          Url ='https://www.showtv.com.tr/cbgplayer/showtv/init.js'      
          referer=[('Referer', rUrl )]        
          data  = gegetUrl(Url ,headers=referer)
          logger.info('dataTOKEN >%s' % data  ) 
          token  = re.findall("TOKEN = '(.*?)'", data, re.S)[0]
          logger.info('TOKEN >%s' % token ) 
          url = url+ '?' +token+ '|Referer='+  rUrl  +'&User-Agent='+UA  
          
         

          logger.info('TOKEN >url %s' % url )  
          addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')



def addLink(name, url, iconimage):
    ok = True
    
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 

def showdizi(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>(.*?)</strong>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl= oInputParameterHandler.getValue('siteUrl')
#        urla  = "http://www.showtv.com.tr/"
                                                    
#        referer=[('Referer',urla)]
#        data=gegetUrl(Url,headers=referer) 
                                                 
#        streamDaten = re.findall('<div class="swiper-wrapper">.*?<a href="(/dizi/tum_bolumler.*?)"', data, re.S) 
#        sUrl = "http://www.showtv.com.tr%s"  % (streamDaten[0])     
      
        sHtmlContent =getHtml(sUrl) 
        



                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                      
                                                                                                                                                                                    
        sPattern = '<div class="box box-xs-3 mb-20 ">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)">'
                                 
    sHtmlContent = sHtmlContent                                               
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
#            sTitle = cUtil().unescape(aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            #not found better way
          
            sTitle =aEntry[2]
           
            sTitle =malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'showdizim', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
       
        
    oGui.setEndOfDirectory()

def showdizim():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    
    sHtmlContent =getHtml(sUrl)
                    
#    sThumbnail  =re.search('<meta itemprop="image" content="(.+?)"/>', sHtmlContent).group(1) 
    oParser = cParser()
    sPattern = '</option>(.+?)<span class="link">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                
               
    Pattern = '<option value="" data-href="(.*?)" data-season-id="(.*?)" >(.*?)</option>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl 
           
                             
            sTitle =aEntry[1]+ '.Season-'+ aEntry[2]
            sTitle =malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()

def partnext(s):
    s=s
    if '-parca-1-izle/' in s:
       s=s.replace('-parca-1-izle/','-parca-1-izle/')
       return s 
    if '-parca-1-izle/' in s:
       s=s.replace('-parca-1-izle/','-parca-2-izle/')
       return s 
    if '-parca-2-izle/' in s:
       s=s.replace('-parca-2-izle/','-parca-3-izle/')
       return s 
    if '-parca-3-izle/' in s:	
       s=s.replace('-parca-3-izle/','-parca-4-izle/')
       return s 
    if '-parca-4-izle/' in s:	
       s=s.replace('-parca-4-izle/','-parca-5-izle/')
       return s 
    if '-parca-5-izle/' in s:	
       s=s.replace('-parca-5-izle/','-parca-6-izle/')
       return s 
    if '-parca-6-izle/' in s:	
       s=s.replace('-parca-4-izle/','-parca-7-izle/')
       return s 
    if '-parca-7-izle/' in s:	
       s=s.replace('-parca-5-izle/','-parca-8-izle/')
       return s 
    return False 
         
def playnext(url):
    sHtmlContent=requests.get(url,headers={'User-Agent':ua,'Referer':'[makelist.param3]','Accept':'/*','Connection':'keep-alive'}).text
              
    Url=re.findall('<meta name="popcorn:stream" content="(.*?)"',sHtmlContent)[0]
    
    return Url    
       

def Genreparca():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sHtmlContent=requests.get(url,headers={'User-Agent':ua,'Referer':'http://www.showtv.com.tr/','Accept':'/*','Connection':'keep-alive'}).text
              
    if  '<li class="selected"><a href="' in  sHtmlContent:
          
    
          r = '|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
         
          urll='http://www.showtv.com.tr'+re.findall('<li class="selected"><a href="(.*?)">',sHtmlContent)[0]
          sUrl =playnext(urll.replace("-parca-1-izle/",'-parca-1-izle/'))
          sUrl1 =playnext(urll.replace("-parca-1-izle/",'-parca-2-izle/'))
          sUrl2 =playnext(urll.replace("-parca-1-izle/",'-parca-3-izle/'))
          sUrl3 =playnext(urll.replace("-parca-1-izle/",'-parca-4-izle/'))
          sUrl4 =playnext(urll.replace("-parca-1-izle/",'-parca-5-izle/'))
          sUrl5 =playnext(urll.replace("-parca-1-izle/",'-parca-6-izle/'))
          sUrl6 =playnext(urll.replace("-parca-1-izle/",'-parca-7-izle/'))
          sUrl7 =playnext(urll.replace("-parca-1-izle/",'-parca-8-izle/'))
    
          playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
    
          playlist.clear();
          listitem1 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl+r,listitem1);
          listitem2 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl1+r,listitem2);
          listitem3 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl2+r,listitem3);
          listitem4 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl3+r,listitem4);
          listitem5 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl4+r,listitem5);                                                                         
          listitem6 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl5+r,listitem6);
          listitem7 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl6+r,listitem7);                                                                         
          listitem8 = xbmcgui.ListItem(''+name)
          playlist.add(sUrl7+r,listitem8);
          player_type = sPlayerType()
          xbmcPlayer = xbmc.Player (player_type); 
          xbmcPlayer.play (playlist)    
    else: 
          diziplay(url,name)

def showdizi2(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
         
       #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>(.*?)</strong>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
           
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        


                                                          
                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                      
                                                                                                                                                                                     
        sPattern = '"title":"(.*?)".*?"image":"(.*?)".*?"link":"(.*?)"'
                                    
                                                  
  
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
#            sTitle = cUtil().unescape(aEntry[0])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[2])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl 
           
            #not found better way
          
            sTitle =aEntry[0]
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        
           
        if not sSearch:
            sNextPage = __ccheckForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showdizi', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
                
def __ccheckForNextPage(sHtmlContent):

    url = re.findall('<div class="center">.*?<a href="javascript:void.*?" class="load-more-button" id="loadMoreItem" data-serie="(.*?)" data-type="(.*?)" data-page="(.*?)">',sHtmlContent, re.S)
    for bir,iki,uc in url:
        URL= "http://www.showtv.com.tr/dizi/pagination/%s/%s/%s"% (bir,iki,uc)
        return str(URL)
    return False    
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ssUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sHtmlContent =getHtml(ssUrl)     
    sHtmlContent = sHtmlContent.replace("\/",'/').replace("x-mpegURL",'m3u8')
    rUrl = re.findall('"ht_video_id":"(.*?)"', sHtmlContent, re.S)[0]
     
    oParser = cParser()
    sPattern = '"ht_files":(.+?)"ht_next_video_url_second"'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult

    
    
    logger.info('EpisodeTOKEN >%s' % rUrl) 
                
             
    Pattern = '"name":"(.*?)","file":"(.*?)","type":".*?/(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
           
#            sTitle = cUtil().unescape(aEntry[0])
            
                
                                                      

           
            sTitle = aEntry[0]+'.'+aEntry[2]
            Url ='https://www.showtv.com.tr/cbgplayer/showtv/init.js'
            stamp = str(int(time.time() * 1000)) 
            referer=[('Referer', rUrl )]       
            data  = gegetUrl(Url ,headers=referer)
            Header = 'if-none-match=KXHOOMECLDNMMPQXX'
            token  = re.findall("TOKEN = '(.*?)'", data, re.S)[0]
            sUrl = aEntry[1]+ '?'+token
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('Url', rUrl)
            oOutputParameterHandler.addParameter('siteurl', ssUrl)
            oOutputParameterHandler.addParameter('videoid', rUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'sshow', sTitle, '', sThumbnail, '', oOutputParameterHandler)

                                                     

    oGui.setEndOfDirectory()   
def showshowHosters():
        oGui = cGui()
    
        oInputParameterHandler = cInputParameterHandler()
        sHosterUrl = oInputParameterHandler.getValue('siteUrl')
        sTitle = oInputParameterHandler.getValue('sMovieTitle')
        sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    
    
       
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
        return False
def showtv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    ref = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',Url)
    urla='https://' +ref                
                                            
    referer=[('Referer','http://www.showtv.com.tr/')]
    data=gegetUrl(Url ,headers=referer) 
    data= data.replace("\/","/").replace('showtv-aes_720p','playlist.m3u8')
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    url  = re.findall('"ht_stream_m3u8":"(.*?)"', data, re.S)[0]                                      
#    url= url.replace("chunklist_b848000.m3u8",'showtv-aes_720p.m3u8')
                                          
    Header = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    sHosterUrl= url+'|' + Header 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        
                          
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()

def Auth():
    Url ='https://www.showtv.com.tr/cbgplayer/showtv/init.js'
    data =getHtml(Url)
    token  = re.findall("TOKEN = '(.*?)'", data, re.S)[0]
    return token
def tokenEcho():
      s=str(time.strftime('%M'))
      if '00' in s:	
        s=Auth()
        return s 
      if '01' in s:
        s=Auth()
        return s 
      if '02' in s:
        s=Auth()
        return s 
      if '03' in s:	
        s=Auth()
        return s 
      if '04' in s:	
        s=Auth()
        return s 
      if '05' in s:	
        s=Auth()
        return s 
      if '06' in s:	
        s=Auth()
        return s 
      if '07' in s:	
        s=Auth()
        return s 
      if '08' in s:	
        s=Auth()
        return s 
      if '09' in s:	
        s=Auth()
        return s 
      if '10' in s:	
        s=Auth()
        return s 
      if '11' in s:	
        s=Auth()
        return s 
      if '12' in s:	
        s=Auth()
        return s 
      if '13' in s:	
        s=Auth()
        return s 
      if '14' in s:	
        s=Auth()
        return s 
      if '15' in s:	
        s=Auth()
        return s 
      if '16' in s:	
        s=Auth()
        return s
      if '17' in s:	
        s=Auth()
        return s 
      if '18' in s:	
        s=Auth()
        return s 
      if '19' in s:	
        s=Auth()
        return s 
      if '20' in s:	
        s=Auth()
        return s 
      if '21' in s:	
        s=Auth()
        return s 
      if '22' in s:	
        s=Auth()
        return s 
      if '23' in s:	
        s=Auth()
        return s 
      if '24' in s:	
        s=Auth()
        return s 
      if '25' in s:	
        s=Auth()
        return s 
      if '26' in s:	
        s=Auth()
        return s 
      if '27' in s:	
        s=Auth()
        return s 
      if '28' in s:	
        s=Auth()
        return s 
      if '29' in s:	
        s=Auth()
        return s 
      if '30' in s:	
        s=Auth()
        return s 
      if '31' in s:	
        s=Auth()
        return s 
      if '32' in s:	
        s=Auth()
        return s 
      if '33' in s:	
        s=Auth()
        return s 
      if '34' in s:	
        s=Auth()
        return s 
      if '35' in s:	
        s=Auth()
        return s 
      if '36' in s:	
        s=Auth()
        return s 
      if '37' in s:	
        s=Auth()
        return s 
      if '38' in s:	
        s=Auth()
        return s 
      if '39' in s:	
        s=Auth()
        return s 
      if '40' in s:	
        s=Auth()
        return s 
      if '41' in s:	
        s=Auth()
        return s 
      if '42' in s:	
        s=Auth()
        return s 
      if '43' in s:	
        s=Auth()
        return s 
      if '44' in s:	
        s=Auth()
        return s 
      if '45' in s:	
        s=Auth()
        return s 
      if '46' in s:	
        s=Auth()
        return s 
      if '47' in s:	
        s=Auth()
        return s 
      if '48' in s:	
        s=Auth()
        return s 
      if '49' in s:	
        s=Auth()
        return s 
      if '50' in s:	
        s=Auth()
        return s 
      if '51' in s:	
        s=Auth()
        return s 
      if '52' in s:	
        s=Auth()
        return s 
      if '53' in s:	
        s=Auth()
        return s 
      if '54' in s:	
        s=Auth()
        return s 
      if '55' in s:	
        s=Auth()
        return s 
      if '56' in s:	
        s=Auth()
        return s 
      if '57' in s:	
        s=Auth()
        return s 
      if '58' in s:	
        s=Auth()
        return s 
      if '59' in s:	
        s=Auth()
        return s 
     
      return False

def sshow():                                 
    oGui = cGui()             
    UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    #+ '&User-Agent='+UA
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl = oInputParameterHandler.getValue('Url')
    name= oInputParameterHandler.getValue('sMovieTitle')
    siteurl = oInputParameterHandler.getValue('siteurl')
    videoid = oInputParameterHandler.getValue('videoid')
    Urlu='https://log.haberturk.com/video'                                                                                                                                                                                                              # , timeout=10
    post_data = {"device":"Chrome","player":"HTPLAY","uid":"null","videoid":videoid ,"success":"true","status":200,"platform":"Web Desktop","videourl": sHosterUrl,"siteurl":siteurl,"repeat_count":1,"error_code":0,"hls":"false","message_type":"video"}
    r = s.post(Urlu , headers={"Referer": siteurl,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": UA,"Connection": "Keep-Alive","x-requested-with": "XMLHttpRequest"}, data=post_data)
    suby = r.text                                                                                                   
 
    time.sleep(5)
    logger.info('EpisodeTOKEN >%s' % suby ) 
    url =sHosterUrl.replace("_1920x1080.mp4",'.m3u8').replace("_1280x720.mp4",'.m3u8').replace("_854x480.mp4",'.m3u8').replace("_720x540.mp4",'.m3u8').replace("_c.mp4",'.m3u8')+'|Referer='+siteurl+'&range=bytes=0-'#+sHosterUrl
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')
def diziplay(url,name):
    oGui = cGui()
   
    sTitle = name
    
                                                                                                                            
    
   
    sHtmlContent=requests.get(url,headers={'User-Agent':ua,'Referer':'[makelist.param3]','Accept':'/*','Connection':'keep-alive'}).text
              
    url=re.findall('<meta name="popcorn:stream" content="(.*?)"',sHtmlContent)[0]
#    URL = "http://www.showtv.com.tr/"
#    referer=[('Referer',url)]
#    Content=gegetUrl(Url,headers=referer)     
#    link=re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1217000,RESOLUTION=1280x720,LANGUAGE="tr"\n(.*?m3u8)\n',Content, re.S) 
#    linko=re.findall('(https://vmcdn.ciner.com.tr/ht/.*?/.*?/.*?/).*?.m3u8',Url)[0]
#    url='%s%s'%(linko,link[0])
      

                      
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(url)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False