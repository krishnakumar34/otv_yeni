#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'canlifm_com'
SITE_NAME = 'RADYO-canlifm.com '
SITE_DESC = 'Replay TV'

MOVIE_diziizle = 'http://www.diziizle.net/sinemalar/'
URL_MAIN = 'http://canlifm.com'

#TIK='|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

RADYO_GENRES = (True, 'showGenre')
Header = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'

UA = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36'



  
URL_SEARCH = ('', 'showMovies')
 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

def Radyo():
    oGui = cGui()
    tarzlistesi= []
    tarzlistesi.append(("Gecen Ay Top20", "http://canlifm.com/karisikmuzik/banaz-dostfm"))
    tarzlistesi.append(("ILLERE GORE RADYOLAR", "http://canlifm.com/karisikmuzik/banaz-dostfm"))
    tarzlistesi.append(("Slow Müzik", "http://canlifm.com/slowradyolar/"))
    tarzlistesi.append(("Arabesk Fantazi", "http://canlifm.com/arabeskfantezi/"))
    tarzlistesi.append(("Yabanci Müzik", "http://canlifm.com/yabanci/"))
    tarzlistesi.append(("Sanat Müzigi", "http://canlifm.com/sanat/"))
    tarzlistesi.append(("Pop Müzik", "http://canlifm.com/popmuzik/"))
    tarzlistesi.append(("Turku Radyolari", "http://canlifm.com/turku/"))
    tarzlistesi.append(("Özgün Müzik", "http://canlifm.com/ozgun/"))
    tarzlistesi.append(("Karma Müzik", "http://canlifm.com/karisikmuzik/"))
    tarzlistesi.append(("Caz-Klasik-Rock", "http://canlifm.com/klasik/"))
    tarzlistesi.append(("Haber Radyolari", "http://canlifm.com/haber/"))
    tarzlistesi.append(("Spor Radyolari", "http://canlifm.com/spor/"))
    tarzlistesi.append(("Dini Radyolar", "http://canlifm.com/dini/"))
               
    for sTitle,sUrl2 in tarzlistesi:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'DIZILER-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'dizizleABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SINEMALAR-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'sinemaABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Gecen Ay Top20':
             oGui.addDir(SITE_IDENTIFIER, 'top20radyo', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ILLERE GORE RADYOLAR':
             oGui.addDir(SITE_IDENTIFIER, 'showradyolist', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showradyo', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def top20radyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    sHtmlContent  =getHtml(sUrl)
#    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<ul>.*?<li class="sayi">.*?<li><a href="(.*?)"><span>(.*?)</span></a></li>'
                                           

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            #sTitle =  alfabekodla(sTitle)
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        progress_.VSclose(progress_)

    oGui.setEndOfDirectory() 


def showradyolist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    sHtmlContent  =getHtml(sUrl)

        
           



    sPattern = "<li class=\"rakam\">(.*?)</li>.*?<li><a href='(.*?)'><span>(.*?)</span></a></li>"
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            
            sTitle =aEntry[0]+'-'+ aEntry[2]
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            #sTitle =  alfabekodla(sTitle)
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'shradyo', sTitle, '', '', '', oOutputParameterHandler)
        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()    


def shradyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    sHtmlContent  =getHtml(sUrl)
#    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<td width=".*?"><a href="(.*?)">(.*?)</a></td>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

           # sTitle =  alfabekodla(sTitle)
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()    

def showradyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    sHtmlContent  =getHtml(sUrl)
#    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<tr class="sectiontableentry.*?" >.*?<a href="(.*?)">(.*?)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            #sTitle =  alfabekodla(sTitle)
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()    

def sshowBox2():  # Lancer les liens
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    url = GetRealUrl(Url)
    url=str(url).replace('/index.html','').replace('/;stream.nsv','/;stream')
    chain  =getHtml(Url)
    Thumbnail ='http://canlifm.com'+ re.findall('<center><img src="(.*?)"', chain, re.S)[0]
    addLink('[COLOR lightblue][B]OTV MEDIA RADYO >  [/B][/COLOR]'+name,url,Thumbnail)


def GetRealUrl(sUrl):  # Recupere les liens des regex
    chain  =getHtml(sUrl)
    r = re.search('<audio rel="nofollow" src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36' 
        return url
    r = re.search("hls.loadSource.'(.*?)'", chain)
    if (r):
        url = r.group(1)
        url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36' 
        return url
    r = re.search('rd_yayincomtr_v3_1="(.+?)"', chain)
    if (r):
        url = r.group(1)
        url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36' 
        return url
    r = re.search('<audio src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36' 
        return url
                 
def msshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')

#    name =  alfabekodla(name)
     

    urla  = "http://canlifm.com/"
                                                                 
    name=str(name)                                                                                                        
    referer=[('Referer',urla)]       
    data=cRequestHandler(Url).request()                                                                                     
    data=data.replace('<audio rel="nofollow" src="','<audio src="').replace('hls.loadSource.','<audio src=').replace('rd_yayincomtr_v3_1="','<audio src="').replace("'",'"').replace('<source rel="nofollow" src="','<audio src="')                                                                                                  
#    TIK='Referer=http%3a%2f%2fcanlifm.com%2farabeskfantezi%2fkralfm&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    Thumb = re.findall('<center><img src="(.*?)"', data, re.S)
   
    url = re.findall("<audio.*?src=[\"'](.*?)[\"']", data, re.S)
                                                                                                                                                
    url =  url[0]  +'|Accept-Encoding=identity;q=1, *;q=0&Connection=keep-alive&Range=bytes=0-&Referer=http://canlifm.com/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
    url=url=str(url).replace('/index.html','').replace('/;stream.nsv','/;stream')
    Thumbnail = "http://canlifm.com"+ Thumb[0]                                                                              
    addLink('[COLOR lightblue][B]OTV MEDIA RADYO >  [/B][/COLOR]'+name,url,Thumbnail)
   
                              
def maddLink(sTitle,sUrl,sThumbnail):
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

