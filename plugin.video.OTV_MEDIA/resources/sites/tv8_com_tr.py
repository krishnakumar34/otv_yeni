#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'tv8_com_tr'
SITE_NAME = 'TV8_com_tr'
SITE_DESC = 'Replay TV'
             
from base64 import b64decode, urlsafe_b64encode
MOVIE_diziizle = 'http://www.tv8.com.tr'
URL_MAIN = 'https://video.acunn.com'
URL_PIC = 'https://video.acunn.com'
MOVIE_HD = (True, 'showGenre')
MOVIE_VIEWS = (True, 'showGenre')
def sEcho(s):
    s=s
    if '/1' in s:
       s=s.replace('/1','/2')
       return s 
    if '/2' in s:
       s=s.replace('/2','/3')
       return s 
    if '/3' in s:	
       s=s.replace('/3','/4')
       return s 
    if '/4' in s:	
       s=s.replace('/4','/5')
       return s 
    if '/5' in s:	
       s=s.replace('/5','/6')
       return s 
    if '/6' in s:	
       s=s.replace('/6','/7')
       return s 
    if '/7' in s:	
       s=s.replace('/7','/8')
       return s 
    if '/8' in s:	
       s=s.replace('/8','/9')
       return s 
    if '/9' in s:	
       s=s.replace('/9','/10')
       return s 
    if '/10' in s:	
       s=s.replace('/10','/11')
       return s 
    if '/11' in s:	
       s=s.replace('/11','/12')
       return s 
    if '/12' in s:	
       s=s.replace('/12','/13')
       return s 
    if '/13' in s:	
       s=s.replace('/13','/14')
       return s 
    if '/14' in s:	
       s=s.replace('/14','/15')
       return s 
    if '/15' in s:	
       s=s.replace('/15','/16')
       return s 
    if '/16' in s:	
       s=s.replace('/16','/17')
       return s
    if '/17' in s:	
       s=s.replace('/17','/18')
       return s 
    if '/18' in s:	
       s=s.replace('/18','/19')
       return s 
    if '/19' in s:	
       s=s.replace('/19','/20')
       return s 
    if '/20' in s:	
       s=s.replace('/20','/21')
       return s 
    return False 

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  
          
def tv8comtr():                              
    oGui = cGui()        
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_tv8/smil:tv8_hd.smil/playlist.m3u8')
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/54773060f5ac7613f46f398b.clear')
    oGui.addMovie(SITE_IDENTIFIER, 'tv8canli',  'TV8 HD CANLI YAYIN', 'https://img.tv8.com.tr/s/template/v2/img/tv8-logo.png', 'https://img.tv8.com.tr/s/template/v2/img/tv8-logo.png', '', oOutputParameterHandler)
       
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_tv8_5/smil:tv8_5_sd.smil/playlist.m3u8')
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oGui.addMovie('kanald_com_tr', 'blutv_2',  'TV 8,5', 'https://www.haberoran.com/files/uploads/news/default/26-nisan-carsamba-tv-eff9539d4cb9c7959f38.png', 'https://www.haberoran.com/files/uploads/news/default/26-nisan-carsamba-tv-eff9539d4cb9c7959f38.png', '', oOutputParameterHandler)
    
    tarzlistesi = []                        
    tarzlistesi.append(("TV8 int", "https://www.tv8.com.tr/canli-yayin"))
    tarzlistesi.append(("Acun Medya", "https://www.acunn.com/programlar"))
    tarzlistesi.append(("Acun Medya 1", "https://www.acunn.com/"))
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'TV8 CANLI YAYIN':
             oGui.addDir(SITE_IDENTIFIER, 'tv8canli', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TV8 int':
             oGui.addDir(SITE_IDENTIFIER, 'tv85Box', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TV8int CANLI YAYIN':
             oGui.addDir(SITE_IDENTIFIER, 'tv85Box', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Acun Medya 1':
             oGui.addDir(SITE_IDENTIFIER, 'program', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'programlar', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
  


from random import randint
def showmGenre(): #affiche les genres
    oGui = cGui()
      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl =sUrl.replace('/videolar/survivor-ekstra','').replace('/videolar/survivor-konusalim','')
    sHtmlContent =getHtml(sUrl) 

           
    oParser = cParser()
                
    sPattern = '<div class="programs-main-item"><div class="programs-main-title"><span>(.*?)</span><a class="play-all" href="(.*?)" title="">'
        
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            
            
            Url = aEntry[1]
            
            sTitle = aEntry[0]
         
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url )
            oOutputParameterHandler.addParameter('iPage', Url )
            oGui.addDir(SITE_IDENTIFIER, 'videokato1', sTitle, 'genres.png', oOutputParameterHandler)
           
        

    oGui.setEndOfDirectory()  
def videokato1():
    
    iPage = 1
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
             
   
    sHtmlContent =getHtml(sUrl) 
    sPattern = '<div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 infinite-content".*?<a href="(.*?)" target="_blank" title="(.*?)".*?<img src=".*?" data-src="(.*?)"' 
                             
    sHtmlContent = sHtmlContent
   
    oParser = cParser()                                                               

    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = aEntry[1]
           
            sPicture = aEntry[2]
            #sPicture = alfabekodla(sPicture)
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = str(aEntry[0])
            if not 'http' in Url:
                Url = str(URL_MAIN) + sUrl            
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui = cGui()
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'videoacunn', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
       
                                                        
        sNextPage = __checkForNextPag(sUrl,iPage,sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
               oOutputParameterHandler = cOutputParameterHandler()
               oOutputParameterHandler.addParameter('siteUrl', sNextPage)
               oGui.addDir(SITE_IDENTIFIER, 'videokato1', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
        oGui.setEndOfDirectory()
def __checkForNextPag(sUrl, iCurrentPage,sHtmlContent):
    Urlu =re.search('<a class="pagination__next" href="(.+?)">',  sHtmlContent).group(1)
    iNextPage = int(iCurrentPage) + 1
    iNextPage = str(iNextPage) + ''
    ssUrl = sUrl+'/' + iNextPage 
    return Urlu  
     

def showmGenre2(): #affiche les genres
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    
    sHtmlContent =getHtml(sUrl)
           
    oParser = cParser()
    sPattern = '<div class="programs-main-title"><span>(.*?)</span><a class="play-all" href="(.*?)" title="">'
        
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            
            
            Url = aEntry[1]
            
            sTitle = aEntry[0] 
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url )
            oOutputParameterHandler.addParameter('iPage', Url )
            oGui.addDir(SITE_IDENTIFIER, 'videokato', sTitle, 'genres.png', oOutputParameterHandler)
           
       

    oGui.setEndOfDirectory()  


def blutv_2():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    UrlL = oInputParameterHandler.getValue('siteUrl')
    cooki = getUrl(UrlL, output='cookie').result
    Referer = oInputParameterHandler.getValue('Referer')
#    urllm = re.findall('(https.*?)/', urll[0])
    h = '|Referer=https://hdfilme.tv&User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69'
    ua='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    Content=requests.get(UrlL,headers={'Cookie':cooki,'User-Agent':ua,'Referer':' https://www.blutv.com.tr/int/','Accept':'/*','Connection':'keep-alive','Origin': 'https://hdfilme.tv','Accept-Language': 'de,en-US;q=0.7,en;q=0.3'}).text
    
#   hi = '|Host=2s1d0z.stream&User-Agent=Mozilla/5.0 (Windows NT 10.0; rv:62.0) Gecko/20100101&Referer=https://hdfilme.tv/&Accept=/*&Connection=keep-alive&Origin=https://hdfilme.tv&Accept-Language=de,en-US;q=0.7,en;q=0.3'
    
#    sPattern = '#EXT-X-STREAM-INF:BANDWIDTH=(.*?),RESOLUTION=(.*?)\n(.*?)\n'           
#    sPattern = '"file":"(.*?)".*?"label":"(.*?)"'             
    sHtmlContent = re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,RESOLUTION=.*?x(.*?)\n(.*?)\n', Content, re.S)
    for sTitle,Url  in sHtmlContent:          
                              

            
           
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', Title)
            oOutputParameterHandler.addParameter('Referer', Referer)
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('UrlL', UrlL)
            oGui.addTV(SITE_IDENTIFIER, 'play_blutv', Title, '', '', '', oOutputParameterHandler)

        
    oGui.setEndOfDirectory()
def play_blutv():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        h = '|User-Agent=Mozilla/5.0 (Windows NT 10.0; rv:62.0) Gecko/20100101&Referer=https://hdfilme.tv/&Accept=/*&Connection=keep-alive&Origin=https://hdfilme.tv&Accept-Language=de,en-US;q=0.7,en;q=0.3'
        Referer = oInputParameterHandler.getValue('Referer')
        sUrl = oInputParameterHandler.getValue('UrlL')
        sUrl =sUrl.replace('playlist.m3u8','')
        Url = oInputParameterHandler.getValue('siteUrl')#Referer:'+ Referer +'&User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
#    ua='Mozilla/5.0 (Windows NT 10.0; rv:62.0) Gecko/20100101'
#    url=requests.get(urll,headers={'User-Agent':ua,'Referer':'https://hdfilme.tv/','Accept':'/*','Connection':'keep-alive','Origin': 'https://hdfilme.tv','Accept-Language': 'de,en-US;q=0.7,en;q=0.3'}).text
                                  
        sHosterUrl =sUrl+Url+'|Refererr='+ Referer +'&User-Agentr=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/'+Url
        sTitle = oInputParameterHandler.getValue('sMovieTitle')
              
       
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()  

def Survivor(): #affiche les genres
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    
    sHtmlContent =getHtml(sUrl)
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
             
    sPattern = '<li ><h3><a href="(.*?)" title=".*?">(.*?)</a></h3></li>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            
            
            Link = aEntry[0]
           
            sTitle = aEntry[1]
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'program', sTitle, '', '', '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()  
def mvideokato():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    iPage= 0 
    if (oInputParameterHandler.exist('iPage')):
        iPage = oInputParameterHandler.getValue('iPage')+'/' 
    
    if (oInputParameterHandler.exist('siteUrl')):
        sUrl = oInputParameterHandler.getValue('siteUrl')
              
        
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        iPage += 1
        __parseMovieSimpleList(sHtmlContent, iPage)

def videokato():
    
    iPage = 1
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
             
   
    sHtmlContent =getHtml(sUrl)
    sPattern = '<div class="list-type-one-content"><a data-icerik-id=".*?" href="(.*?)" title="(.*?)" target="_blank"><div class="list-type-one-img"><img src=".*?" data-original="(.*?)".*?<span class="video-img-over-time">(.*?)</span>' 
                                
    sHtmlContent = sHtmlContent
   
    oParser = cParser()                                                               

    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = aEntry[1]+' '+ aEntry[3] +' Dakika'
           
            sPicture = str(aEntry[2])
            
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = str(aEntry[0])
            if not 'http' in Url:
                Url = str(URL_MAIN) + sUrl            
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui = cGui()
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'videoacunn', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
                        
        sNextPage = __checkForNextPage(sUrl,iPage)#cherche la page suivante
        if (sNextPage != False):
               oOutputParameterHandler = cOutputParameterHandler()
               oOutputParameterHandler.addParameter('siteUrl', sNextPage)
               oGui.addDir(SITE_IDENTIFIER, 'videokato', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
        oGui.setEndOfDirectory()



def program():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    
    sHtmlContent =getHtml(sUrl)
        


                                                                             
                                                                          
                   
                    
    sPattern = '<div class="col-md-12 col-lg-12"><a href="(.*?)" title="(.*?)">' 
                                 
    sHtmlContent = sHtmlContent
    
    oParser = cParser()                                                               

    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = aEntry[1]
           
                 
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
                
            sTitle =malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            
            oGui.addDir(SITE_IDENTIFIER, 'showmGenre', sTitle, 'genres.png', oOutputParameterHandler)
            

    oGui.setEndOfDirectory()

def programlar():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    
    sHtmlContent =getHtml(sUrl)
        


                                                                             
                                                                          

    oParser = cParser()
    sPattern = '<div class="row video-list">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                                
    sPattern = '<div class="col-xs-12 col-sm-6 col-md-4 col-lg-4"><a href="(.*?)" title="(.*?)" class="box type-.*?"><em><img src=".*?"  data-src="(.*?)"'
                               
    oParser = cParser()                                                               

    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        
       
        for aEntry in aResult[1]:
            sTitle = aEntry[1]
                                               
            sPicture = str(aEntry[2].replace('/70x40/', "/980x400/"))
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if  'survivor-ekstra' in sUrl:
                sUrl = 'https://www.acunn.com/survivor-ekstra/videolar/survivor-ekstra' 
            elif  'survivor-konusalim' in sUrl:
                sUrl = 'https://www.acunn.com/survivor-konusalim/videolar/survivor-konusalim' 
   
            #not found better way                                                                                                   
            #sTitle = unicode(sTitle, errors='replace')                                                             
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'showmGenre', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
      
        
         
    oGui.setEndOfDirectory()




def videoacunn():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
  
    
    
    urla  = "https://www.acunn.com/"
                     
#    referer=[('Referer',urla)]
    data=getHtml(Url) 
    if   "contentURL" in  data:                       
        sHosterUrl = re.findall('"contentURL": "(https://.*?.mp4)"', data, re.S)[0]
        sHosterUrl =sHosterUrl.replace("-240p.mp4","-720p.mp4").replace("-360p.mp4","-720p.mp4").replace("-480p.mp4","-720p.mp4")
        cookie = getUrl(sHosterUrl, output='cookie').result 
    else:      
        haberId = re.findall("var haberId             =   '(.*?)'", data, re.S)[0] 
        hab='https://www.acunn.com/embed_video.html?id='+haberId+'&comscore=1'
        referer=[('Referer',urla)]
        dat=gegetUrl(hab,headers=referer) 
        
        sHosterUrl= re.findall('"file": "(.*?)"', dat, re.S)[0]  
        cookie = getUrl(sHosterUrl, output='cookie').result          
                       
   
    Header = 'Referer='+ urla
    sHosterUrl=  sHosterUrl+ '|' + Header                                      
    sHosterUrl=sHosterUrl.replace('-720p.mp4','.smil/playlist.m3u8')
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False
def kinox(Link):
     url2 = base64.b64encode(Link)
    
     url=TURKIYE+url2
     return url      
from hashlib import md5

SECRET = ""

def tv8canli():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    UrlL = "https://tv8.personamedia.tv/tv8hls?fmt=hls" 
    cooki = getUrl(UrlL, output='cookie').result
    Referer = oInputParameterHandler.getValue('Referer')
    
    h = '|Referer=http://www.blutv.com.tr&User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69'
    ua='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    Content=requests.get(UrlL,headers={'User-Agent': ua,'Referer': 'https://www.blutv.com.tr/','Accept':'/*','Connection':'keep-alive','Origin': 'https://www.blutv.com.tr','Accept-Language': 'de,en-US;q=0.7,en;q=0.3'}).text
    sHtmlContent = re.findall('#EXT-X-STREAM.*?,RESOLUTION=.*?x(.*?)\n(.*?)\n', Content, re.S)
    for sTitle,Url  in sHtmlContent:          
                              

            
            UrlL =UrlL.replace('playlist.m3u8','').replace('https://blutv-beta.akamaized.net/','https://mn-nl.mncdn.com/blutv_live/')
            Uurl= UrlL+ Url
            sTitle=sTitle.replace(',CODECS="avc1.64e00a,mp4a.40.2"','')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('Referer', Referer)
            oOutputParameterHandler.addParameter('siteUrl', Uurl)
            oOutputParameterHandler.addParameter('UrlL', UrlL)
            oGui.addTV(SITE_IDENTIFIER, 'play_blutv', sTitle, '', '', '', oOutputParameterHandler)

        
    oGui.setEndOfDirectory()
        
              
def play_blutv():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Referer =oInputParameterHandler.getValue('Referer')
        sUrl = oInputParameterHandler.getValue('UrlL')
        Url = oInputParameterHandler.getValue('siteUrl')#Referer:'+ Referer +'&User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
                                  
        url =Url+'|Referer='+ Referer +'&User-Agentr=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        name = oInputParameterHandler.getValue('sMovieTitle')
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')#    url= getUrl(osta).result 
#    url=url[0]
#    url=url.replace('tv8hd_720p', 'https://tv8-tb-live.ercdn.net/tv8-geo/tv8hd_720p')
        
#    url=sHosterUrl+ '|' + Header 


def tv85Box():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
  
    
                      
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': 'http://www.canlitvlive.co/[makelist.param1]', 'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    data= requests.get(url, headers = headers).text                      
    playlist =  re.findall('file: "(.*?)"', data)                    
    Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    
    sHosterUrl = playlist[0]  + '|' + Header
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
    return False     

def sshowBox3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    
   
    
    urla  = "http://www.tv8.com.tr/"                   
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer)                      
    streamDaten = re.findall("src:\".*?\", type:'application/x-mpegURL'.*?src:\"(.*?)\", type:'video/mp4'", data, re.S)	
    if streamDaten:
                  (serviceUrl )= streamDaten[0]                                                                         
                       
                          
    sHosterUrl = "%s"  % (serviceUrl.replace("-240p.mp4","-720p.mp4").replace("-360p.mp4","-720p.mp4").replace("-480p.mp4","-720p.mp4").replace(".mp4","-720p.mp4").replace("-720p-720p.mp4","-720p.mp4"))    
 
    



    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False