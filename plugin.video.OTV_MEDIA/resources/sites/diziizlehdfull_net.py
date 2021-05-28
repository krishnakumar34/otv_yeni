#-*- coding: utf-8 -*-

from resources.sites.LIVETV2 import *  

HOST = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'


def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)


TIK='|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

def showMessage(heading='seyirTURK', message = '', times = 2000, pics = ''):
                try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
                except Exception as e:
                        xbmc.log( '[%s]: showMessage: exec failed [%s]' % ('', e), 1 )

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
SITE_IDENTIFIER = 'diziizlehdfull_net'
SITE_NAME = 'diziizlehdfull.org'
MOVIE_HD = (True, 'showGenre')
def diziizlehdfulltr():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'TRModules@https://www.dizibox.vip/@start@dizibox')
    oOutputParameterHandler.addParameter('sMovieTitle', 'BolumD dizi izle')
    oGui.addDir('turkvod_org', 'Liste', 'DIZILER-ABC', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.vip/tum-bolumler/')
    oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', 'Tüm Bölümler', 'search.png', oOutputParameterHandler)
                                              
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.vip/tum-bolumler/?tip=populer')
    oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', 'Popüler Bölümler', 'search.png', oOutputParameterHandler)
                                               
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.vip/efsane-diziler/')
    oGui.addDir(SITE_IDENTIFIER, 'ssshowMovies', 'Efsane Diziler', 'search.png', oOutputParameterHandler)
    
        
    oInputParameterHandler = cInputParameterHandler()
                 
    oGui.setEndOfDirectory()

def showSearch(): #affiche les genres
 oGui = cGui()
 sSearchText = oGui.showKeyBoard()
 if (sSearchText != False):
    sUrl = 'https://www.dizibox.pw/?s=' + sSearchText
    from resources.lib.handler.requestHandler3 import cRequestHandler
    oRequestHandler = cRequestHandler(sUrl)
    data = oRequestHandler.request()  
    VSlog('Good cookie :' + data )
                                  

    playlist = re.findall('<figure class="figure big-cover pull-left m-r-1">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"', data, re.S)
    for sUrl,sPicture,sTitle in playlist:
            
           
            sTitle = malfabekodla(sTitle)    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addMovie(SITE_IDENTIFIER, 'FilmABCD', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

 oGui.setEndOfDirectory()  



def ssshowMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
     
        sHtmlContent = reponse.read()
        sPattern = '<div class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        sHtmlContent =getHtml(sUrl)                                                                                                                             
                          
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<a class="thumbnail-gradien.*?" href="(.*?)".*?<img src=\'(.*?)\' alt=\'(.*?)\''

                                                                  
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
        
               
            sThumbnail = str(aEntry[1])
          
              
                
            
            sTitle =aEntry[2] 
          
            sTitle = malfabekodla(sTitle)
            Url ='TRModules@'+sUrl+'@category3@'+ sTitle
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV('turkvod_org', 'Liste', sTitle, '', sThumbnail, '', oOutputParameterHandler)

           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def sshowMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
       sPattern = '<div class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        sHtmlContent =getHtml(sUrl)                                                                                                                              
       
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<a class="thumbnail-gradien.*?" href="(.*?)".*?<img src=\'(.*?)\' alt=\'(.*?)\''
                  
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
        
               
            sThumbnail = str(aEntry[1])
          
              
                
            
            sTitle =aEntry[2] 
          
            sTitle = malfabekodla(sTitle)
            Url ='TRModules@'+sUrl+'@category3@'+ sTitle 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV('turkvod_org', 'Liste', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def diziabc():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    abc = oInputParameterHandler.getValue('ksiteUrl')
    
    oRequestHandler = cRequestHandler(Url)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="alphabetical-category-index">(.+?)</div> </div>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                
    
    Pattern = '<a href="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
          
                            
            sUrl = str(aEntry)
            sTitle = sUrl.replace('#','')
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('ksiteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'FilmABC', sTitle, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()


   



def FilmABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    abc = oInputParameterHandler.getValue('ksiteUrl')
    
   
    

    Url = 'https://www.dizibox.pw/'+ abc 
    req = urllib2.Request(Url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')
    post= {'alphabetical-category-link active-letter': abc,}
    post = urllib.urlencode(post)
    sHtmlContent =_get(req,post)
    
    oParser = cParser()
    sPattern = "<ul class='alphabetical-category-list list-unstyled' data-index='"+abc+"'>(.+?)<ul class='alphabetical-category-list list-unstyled'"
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                
    
    Pattern = '<a title="(.*?)" href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
           
            sTitle = malfabekodla(aEntry[0])
                            
            sUrl = str(aEntry[1])
            
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'FilmABCD', sTitle, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def FilmABCD():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                      
    oRequestHandler = cRequestHandler(Url)
    sHtmlContent = oRequestHandler.request();
    sPicture= re.search('<i class="icon icon-youtube">.+?<img src="(.+?)"', sHtmlContent).group(1)+ TIK
    BILGI=re.search('<div class="tv-story-wrapper m-t-2">.+?<p>(.+?)</p>', sHtmlContent).group(1)
    if '<div class="post-title">' in sHtmlContent:
         oParser = cParser()
         Pattern = '<div class="post-title">.*?<a href="([^"]+)" class="season-episode link-unstyled full-width">([^<]+)</a>'
         oParser = cParser()
         aResult = oParser.parse(sHtmlContent, Pattern)
    else:
         Pattern2 = "<a href='([^']+)' class='btn btn-s btn-default-ligh.*?'>([^<]+)</a>"
         oParser = cParser()
         aResult = oParser.parse(sHtmlContent, Pattern2) 
    
    
    
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
                            
            sUrl = str(aEntry[0])
            
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
#            oGui.addTV(SITE_IDENTIFIER, 'Hosters',sTitle, '', '', '', oOutputParameterHandler)
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, BILGI, oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def ASCIIDecode(string):

    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i+2)] == '\\x':
            c = chr(int(string[(i+2):(i+4)], 16))
            i+=3
        if string[i:(i+2)] == '\\u':
            cc = int(string[(i+2):(i+6)], 16)
            if cc > 256:
                #ok c'est de l'unicode, pas du ascii
                return ''
            c = chr(cc)
            i+= 5
        ret = ret + c
        i = i + 1

    return ret
 
        

     



def hextranslate(s):
        res = ""
        for i in range(len(s)/2):
                realIdx = i*2
                res = res + chr(int(s[realIdx:realIdx+2],16))
        return res    
     



  
def __checkForNextPage(sHtmlContent):
    sPattern = '<span class="current">.+?</span> <a href="(.+?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]                              

    return False

def mHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
      
 

def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(Url)
    sHtmlContent = oRequestHandler.request();
    if not "<option class='woca-current-page'" in sHtmlContent:
         dizibox2(Url) 
#               
    
    sPattern = "<option value='(.*?)'>(.*?)</option>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            sTitle = sMovieTitle+' - '+aEntry[1]
            sUrl = (aEntry[0])
            
            sDisplayTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'dizibox', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
  
def dizibox2(url):  
  data= requests.session().get(url ,headers={"Referer": "https://www.dizibox.pw/","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Host": "www.dizibox.pw","Connection": "Keep-Alive","Upgrade-Insecure-Requests": "1"}).text
  return data



def MakeToken(sLoc):
        
        def base36encode(number):
            if not isinstance(number, (int, long)):
                raise TypeError('number must be an integer')
            if number < 0:
                raise ValueError('number must be positive')
            alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            base36 = ''
            while number:
                number, i = divmod(number, 36)
                base36 = alphabet[i] + base36
            return base36 or alphabet[0]
            
        #oRequest = cRequestHandler('http://www.wat.tv/servertime2')
        #stime = oRequest.request()
        #stime = base36encode(int(stime))
            
        stime = base36encode(int(time.time()))

        timesec = hex(int(stime, 36))[2:]
        while(len(timesec)<8):
            timesec = "0" + timesec

        key = '9b673b13fa4682ed14c3cfa5af5310274b514c4133e9b3a81e6e3aba009l2564'
        token = md5.new(key + sLoc + timesec).hexdigest() + '/' + timesec
        return token