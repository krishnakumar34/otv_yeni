#-*- coding: utf-8 -*-
import urllib2, urllib,cookielib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
from resources.lib.otvhelper import  gegetUrl,getUrl ,alfabekodla
from resources.lib.config import cConfig
import requests
import re,xbmcgui,unicodedata              
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, VSlog
from resources.lib.player import cPlayer

from resources.lib.gui.guiElement import cGuiElement

SITE_IDENTIFIER = 'fullhd4kfilmizle'
SITE_NAME = 'Fullhd4kfilmizle'
SITE_DESC = 'Films streaming'
import cookielib 
URL_MAIN = 'https://www.filmifullizle.tv'
from resources.lib.comaddon import VSlog

TURK_SINEMA = (True, 'showGenre')

kukz=''        

import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()


UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'https://www.indirmedenfilmizle.pw/?s='+sSearchText  
            sUrl= sUrl.replace(' ','%20')
            searchowMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
def rrequest(url, headers={}):
        print('request: %s' % url)
        req = urllib2.Request(url, headers=headers)
        try:
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
        except urllib2.HTTPError, error:
            data=error.read()
        print('len(data) %s' % len(data))
        return data
        
   
def hd4kfilmizle(): #affiche les genres
 
    oGui = cGui()
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.indirmedenfilmizle.pw/?s=')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.indirmedenfilmizle.pw/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'En son eklenen filmler', 'genres.png', oOutputParameterHandler)

    url = 'https://www.indirmedenfilmizle.pw'                 
    oRequest = cRequestHandler(url)
    oRequest.addHeaderEntry('Referer', ''+url)
    sHtmlContent = oRequest.request()
    oParser = cParser()
    sPattern = '<div class="tags scroll home">(.*?)<div class="container">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li class="cat-item cat-item-.+?"><a href="(.+?)">(.+?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)  
            if dialog.iscanceled():
                break
                               
           
            sTitle =  aEntry[1]
            
            sUrl = aEntry[0]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()   
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()
def showMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        url = 'https://www.indirmedenfilmizle.pw/'
        request = urllib2.Request(url,None,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()

        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="movie-box">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('Referer', 'https://www.fullhd4kfilmizle.com/')
        oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
        sHtmlContent = oRequest.request()
        

        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="movie-box">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"'
    
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sUrl = str(aEntry[0])
            
            sThumbnail = str(aEntry[1])
            sTitle = aEntry[2]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
   
def searchowMovies(sUrl):
    oGui = cGui()
   
    data = cRequestHandler(sUrl).request() 
                          
    sHtmlContent = re.findall('<div class="movie-box">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"', data, re.S)
         
    for sUrl,sPicture,sTitle in sHtmlContent:
             
                       
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()     
   
def __checkForNextPage(sHtmlContent):                     
    sPattern = '<span class="current">.+?</span><a href="(.+?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False

def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
     
    link =  cRequestHandler(sUrl).request()         
    ret =re.findall('<div class="keremiya_part"> <span>(.+?)</span>',link,re.DOTALL)[0]
  
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('sMovieTitle', str(ret) )
    oGui.addDir(SITE_IDENTIFIER, 'streams', ret, 'genres.png', oOutputParameterHandler)

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="keremiya_part">(.+?)<div class="views">'
 
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)" class="post-page-numbers"><span>(.*?)</span></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    for urlm in aResult[1]:
        sUrl2 = urlm[0]                         
                
        sTitle = urlm[1]
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle) )
        if sTitle == 'PROGRAMLAR':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLASİK DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'ArshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLASİK DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'klasikdizizleABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ATV YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'canlitvzoneBox', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'streams',  sTitle, 'genres.png', oOutputParameterHandler)
           

    oGui.setEndOfDirectory()
    

            
def streams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    link =  cRequestHandler(url).request() 
    sHosterUrl =re.findall('<!--baslik:.+?-->.+?<ifram.+?src="(.+?)"',link,re.DOTALL)[0]
    if not 'http' in  sHosterUrl:
         sHosterUrl='http:'+ sHosterUrl
    if ('indirfilmvideo' in sHosterUrl):
         
         
         indirfilmvideo(sHosterUrl,Title)
    if   '/fireplayer/' in sHosterUrl:                   
         
         hcwatchingvideo(sHosterUrl,url)
    
    if   'www.ffilmizle.org' in sHosterUrl:                   
         
         fembedvideo(sHosterUrl,url)
    if   'www.fembed.net' in sHosterUrl:                   
         
         fembedvideo(sHosterUrl,url)
    if   'cwatching.live' in sHosterUrl:                   
         
         cwatchingvideo(sHosterUrl)

   
      
         
          
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
                sMovieTitle = cUtil().DecoTitle(Title)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
    oGui.setEndOfDirectory()
UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
def GetIp():
    if (False):
        oRequest = cRequestHandler('http://hqq.tv/player/ip.php?type=json')
        oRequest.addHeaderEntry
        sHtmlContent = oRequest.request()
        ip = re.search('"ip":"([^"]+)"', sHtmlContent, re.DOTALL).group(1)
    else:
        import random
        for x in xrange(1,100):
            ip = "192.168."
            ip += ".".join(map(str, (random.randint(0, 255) for _ in range(2))))
        ip = base64.b64encode(ip)

    return ip



def terscevir(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku        
import codecs
def ASCIIDecode(string):

    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i + 2)] == '\\x':
            c = chr(int(string[(i + 2):(i + 4)], 16))
            i+= 3
        if string[i:(i + 2)] == '\\u':
            cc = int(string[(i + 2):(i + 6)], 16)
            if cc > 256:
                #ok c'est de l'unicode, pas du ascii
                return ''
            c = chr(cc)
            i+= 5
        ret = ret + c
        i = i + 1

    return ret
                  
def  hcwatchingvideo(sHosterUrl,url):
        oGui = cGui()
        sUrl= sHosterUrl+ '?do=getVideo'
        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('Cookie','__cfduid=d380a1c01d0065e770d1062b117bd3be01561378177; PHPSESSID=24trlnlmrqq6b4r4ksu837fo73')
	oRequest.addHeaderEntry('Referer',  sHosterUrl)
        oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
	string = oRequest.request()
	tring=ASCIIDecode(string)
	sHoster =re.findall('atob."(.+?)"',tring)[0]	
        tle = b64decode(sHoster)
	name = 'sMovieTitle'
	addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,tle, '')

def  cwatchingvideo(sHosterUrl):
        oGui = cGui()
        
        rUrl= 'https:'+ sHosterUrl
       
        urll=  cRequestHandler(rUrl).request()         

        sPattern = "<script type='text/javascript'>(eval.function.p,a,c,k,e,d.*?)</script>"
        aResult = re.findall(sPattern,urll)
        sUnpacked = cPacker().unpack(aResult[0])

        aJson =re.findall('file:"(.+?)",label:"(.+?)"',sUnpacked,re.DOTALL)
        for catid,tid in aJson:                                 
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',  catid.replace('\/','/') )
            oOutputParameterHandler.addParameter('sMovieTitle', str(tid ) )
	    oGui.addDir(SITE_IDENTIFIER, 'PLAYPLAY', tid, 'genres.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()   

        #Host = 'https://' + self.GetHost(player_url) + '/'
def  fembedvideo(sHosterUrl,url):
        oGui = cGui()
        player_url=sHosterUrl.replace('/v/','/api/source/')
        req = urllib2.Request(player_url)
       
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        req.add_header('Referer',sHosterUrl)
        req.add_header('X-Requested-With',' XMLHttpRequest')
        post={'r':url,'d':' www.fembed.net'}

        post = urllib.urlencode(post)
        sJson=_get(req,post)
        aJson =re.findall('"file":"(.+?)","label":"(.+?)"',sJson,re.DOTALL)
        for catid,tid in aJson:                                 
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',  catid.replace('\/','/') )
            oOutputParameterHandler.addParameter('sMovieTitle', str(tid ) )
	    oGui.addDir(SITE_IDENTIFIER, 'PLAYPLAY', tid, 'genres.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()          
import string
import random
def id_generator(size=10, chars=string.digits + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))
#
#var pa = document.createElement('script'); 
#var s = document.getElementsByTagName('script')[0]; 
#    pa.src = 'https://storage.googleapis.com/loadermain.appspot.com/main.js';
#    s.parentNode.insertBefore(pa, s);

def reduce( aFunction, aSequence, init= 0 ):
    r= init
    for s in aSequence:
        r= aFunction( r, s )
    return r

def mmindirfilmvideo(player_url,sMovieTitle):
        
        
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+sMovieTitle,player_url,'')
def indirfilmvideo(sHosterUrl,name):
            import string, random
            sHosterUrl = 'https:'+ sHosterUrl
	    player_url=sHosterUrl.replace('/iframe/','/ajax/')
            token =''   
            import random             
            time_stamp = str(int(time.time() * 1000 ))
            url = 'https://www.indirfilmvideo.com/video.js?'#+ time_stamp
            link =  cRequestHandler(url).request()
            
            
            rete =re.findall("window,'(.+?)','(.+?)'",link,re.DOTALL)
            (Ref,Refer)=rete[0]
            
            url9=player_url+'?'+ time_stamp
            req = urllib2.Request(player_url)
       
            req.add_header(Ref, Refer)
            req.add_header('Referer',sHosterUrl)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
      
            sJson=_get(req)
			
			
            aJson = json.loads(sJson)
                                         
            tid =aJson['hash']
            catid =aJson['file']
            urll=catid+'?'+tid 
            
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,urll ,'')
def vidmoly(url,sTitle):                    
    oGui = cGui()	
    if not 'http' in url:
       url = 'http:'+ url
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    html = response.read()
    if re.search("type='text/javascript'>(eval\\(function.*?)\\n", html):
        packed = re.findall("type='text/javascript'>(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
        html = cPacker().unpack(packed)
    for match in re.finditer('"([^"]+(m3u8|mp4))"', html):
       linko = match.group(1)
       if linko.startswith("//"):
          sUrl = "http:" + linko       
  
    
                                              
          TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

          sUrl= sUrl+TIK
          sTitle = "vidmoly"
          sTitle = alfabekodla(sTitle)         
          oOutputParameterHandler = cOutputParameterHandler()
          oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
          oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
          oGui.addDir(SITE_IDENTIFIER , 'PLAYPLAY', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
       

def PLAYPLAY():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = sUrl+"|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
          
def aaddLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")                                                                  	

        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok  

#*******************************************************************************
def decodeUN(a):
    a = a[1:]
    s2 = ""

    i = 0
    while i < len(a):
      s2 += ('\u0' + a[i:i+3])
      i = i + 3

    s3 = s2.decode('unicode-escape')
    if not s3.startswith('http'):
        s3 = 'http:' + s3

    return s3

def DecodeAllThePage(html):

    #html = urllib.unquote(html)

    Maxloop = 10

    #unescape
    while (Maxloop > 0):
        Maxloop = Maxloop - 1

        r = re.search(r'unescape\("([^"]+)"\)', html, re.DOTALL | re.UNICODE)
        if not r:
            break

        tmp = cUtil().unescape(r.group(1))
        html = html[:r.start()] + tmp + html[r.end():]

    #unwise
    while (Maxloop > 0):
        Maxloop = Maxloop - 1

        r = re.search(r'(;eval\(function\(w,i,s,e\){.+?\)\);)\s*<', html, re.DOTALL | re.UNICODE)
        if not r:
            break

        tmp = data = unwise.unwise_process(r.group(1))
        html = html[:r.start()] + tmp + html[r.end():]

    return html
        





def getURLFromObfJs(js):
	js = js.replace("eval", "fnRes=")
	print "return" in js
	js = str(js2py.eval_js(js))

	# First let's decode the javascript
	searchObj = re.search("var _escape='[%u\\d\\w]+';", js)
	if searchObj:
		escapeCode = searchObj.group().replace("var _escape='", "")[:-2]
		escapeCode = escapeCode.replace("%", "\\")
		escapeCode = escapeCode.decode("unicode-escape").replace("'+autoplay+'","no")
		print "escape code: " + escapeCode
	else:
		return False
	
	if re.search(r'<form(.+?)action="[^"]*(hqq|netu)\.tv/player/embed_player\.php"[^>]*>', escapeCode):
		return escapeCode
	# Second let's find the iframes src
	iframes = re.findall('<iframe [\\w\\d"=:\\/.?&\'+ %-;><]*<\\/iframe>', escapeCode)
	return '-'.join(iframes)









class JsUnwiser:
    def unwiseAll(self, data):
        try:
            in_data=data
            sPattern = 'eval\\(function\\(w,i,s,e\\).*?}\\((.*?)\\)'
            wise_data=re.compile(sPattern).findall(in_data)
            for wise_val in wise_data:
                unpack_val=self.unwise(wise_val)
                in_data=in_data.replace(wise_val,unpack_val)
            return re.sub(re.compile("eval\(function\(w,i,s,e\).*?join\(''\);}", re.DOTALL), "", in_data, count=1)
        except: 
            traceback.print_exc(file=sys.stdout)
            return data
        
    def containsWise(self, data):
        return 'w,i,s,e' in data
        
    def unwise(self, sJavascript):
        page_value=""
        try:        
            ss="w,i,s,e=("+sJavascript+')' 
            exec (ss)
            page_value=self.__unpack(w,i,s,e)
        except: traceback.print_exc(file=sys.stdout)
        return page_value
        
    def __unpack( self,w, i, s, e):
        lIll = 0;
        ll1I = 0;
        Il1l = 0;
        ll1l = [];
        l1lI = [];
        while True:
            if (lIll < 5):
                l1lI.append(w[lIll])
            elif (lIll < len(w)):
                ll1l.append(w[lIll]);
            lIll+=1;
            if (ll1I < 5):
                l1lI.append(i[ll1I])
            elif (ll1I < len(i)):
                ll1l.append(i[ll1I])
            ll1I+=1;
            if (Il1l < 5):
                l1lI.append(s[Il1l])
            elif (Il1l < len(s)):
                ll1l.append(s[Il1l]);
            Il1l+=1;
            if (len(w) + len(i) + len(s) + len(e) == len(ll1l) + len(l1lI) + len(e)):
                break;
            
        lI1l = ''.join(ll1l)
        I1lI = ''.join(l1lI)
        ll1I = 0;
        l1ll = [];
        for lIll in range(0,len(ll1l),2):
            ll11 = -1;
            if ( ord(I1lI[ll1I]) % 2):
                ll11 = 1;
            l1ll.append(chr(    int(lI1l[lIll: lIll+2], 36) - ll11));
            ll1I+=1;
            if (ll1I >= len(l1lI)):
                ll1I = 0;
        ret=''.join(l1ll)
        if 'eval(function(w,i,s,e)' in ret:
            ret=re.compile('eval\(function\(w,i,s,e\).*}\((.*?)\)').findall(ret)[0] 
            return self.unwise(ret)
        else:
            return ret

