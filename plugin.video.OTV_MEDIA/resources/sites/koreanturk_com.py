#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *  





                
SITE_IDENTIFIER = 'koreanturk_com'
SITE_NAME = 'koreanturk_com'
SITE_DESC = 'Films streaming'

TURK_SINEMA= (True, 'showGenre') 
URL_MAIN = 'https://www.koreanturk.com/'

MOVIE_COMMENTS = (True, 'showGenre')
def encode_for_logging(c, encoding='ascii'):
    if isinstance(c, basestring):
        return c.encode(encoding, 'replace')
    elif isinstance(c, Iterable):
        c_ = []
        for v in c:
            c_.append(encode_for_logging(v, encoding))
        return c_
    else:
        return encode_for_logging(unicode(c))
url = '' 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://filmakinesi.net/?s=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        
def AlphaSearch():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    dialog = cConfig().createDialog(SITE_NAME)
    
    for i in range(0,27) :
        cConfig().updateDialog(dialog, 36)
        
        if (i > 0):
            sTitle = chr(64+i)
        else:
            sTitle = '09'
            
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl + sTitle.upper() )
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR azure] Lettre [COLOR teal]'+ sTitle +'[/COLOR][/COLOR]', 'genres.png', oOutputParameterHandler)
        
    cConfig().finishDialog(dialog)
    
    oGui.setEndOfDirectory()           
    
def koreanturk(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.koreanturk.com/kore-filmleri')
    oGui.addDir(SITE_IDENTIFIER, 'koreanturksin', 'Kore Filmleri', 'ktfooterlogo3.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.koreanturk.com/#')
    oGui.addDir(SITE_IDENTIFIER, 'koreanturkdiz', 'Kore Dizileri', 'ktfooterlogo3.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()  

def koreanturkdiz(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    sHtmlContent= getHtml(sUrl)
    
    
    
    oParser = cParser()

            
    sPattern = '<li class="cat-item cat-item-.*?"><a href="(.*?)" title="(.*?)">(.*?)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            
#            sGenre = alfabekodla(aEntry[1])
            
            Link =aEntry[0]
            logger.info("koreanturkdiz : %s" %Link ) 
            sThumbnail='https://www.koreanturk.com/wp-content/uploads/2015/05/ktfooterlogo3.png'
            des = malfabekodla(aEntry[1])
            sTitle = malfabekodla(aEntry[2])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oOutputParameterHandler.addParameter('sThumbnail', sThumbnail) 
            oGui.addTV(SITE_IDENTIFIER, 'koreanturkdiz1', sTitle, '', sThumbnail,des, oOutputParameterHandler)



    oGui.setEndOfDirectory()    
def koreanturkdiz1():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    sHtmlContent= getHtml(sUrl)

    sPattern = '<div class="col-sm-3 col-xs-6 col-md-4 nopadr">.*?<a class=".*?" href="(.*?)".*?<img class=".*?" src="(.*?)".*?alt="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)                 
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
           
            sThumbnail= str(aEntry[1]) 
            sTitle =aEntry[2] 
          
            sTitle = malfabekodla(sTitle)
             
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'koreanturkdiz12', sTitle, '', sThumbnail, '', oOutputParameterHandler)

 
    oGui.setEndOfDirectory()
   
def koreanturkdiz12():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sHtmlContent= getHtml(sUrl)       
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<tr class="odd gradeX">.*?<a href="(.*?)">(.*?)</a></td>'
    
    
  
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
            sTitle =str(aEntry[1])
            
            sTitle = malfabekodla(sTitle)
             
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

 
    oGui.setEndOfDirectory()


def koreanturksin(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    sHtmlContent= getHtml(sUrl)
    
    
    
    oParser = cParser()
            
    sPattern = '<li class="cat-item cat-item-.*?"><a href="(.*?)" title=".*?">(.*?)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            
#            sGenre = alfabekodla(aEntry[1])
            
            Link =aEntry[0]
           
            sTitle = malfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
#            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sGenre, '', '', '', oOutputParameterHandler)
            oGui.addDir(SITE_IDENTIFIER, 'koreanturksin1', sTitle, 'genres.png', oOutputParameterHandler)
    Content = re.findall('<div class="col-sm-3 col-xs-6 col-md-4.*?<a class=".*?" href="(.*?)".*?<img class=".*?" src="(.*?)".*?alt="(.*?)"', sHtmlContent, re.S)
    for sUrl,sPicture,sTitle in Content:                              
             
                       
            sTitle = malfabekodla(sTitle)                                                                                       
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         

    
    oGui.setEndOfDirectory()    

def koreanturksin1():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sHtmlContent= getHtml(sUrl)
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<div class="col-sm-3 col-xs-6 col-md-4.*?<a class=".*?" href="(.*?)".*?<img class=".*?" src="(.*?)".*?alt="(.*?)"'
    
    
  
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
            sThumbnail = str(aEntry[1])
            
            sTitle =aEntry[2] 
          
            sTitle = malfabekodla(sTitle)
             
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

           
 
    oGui.setEndOfDirectory()

   
def Hosters():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            urll = oInputParameterHandler.getValue('siteUrl')
            name = oInputParameterHandler.getValue('sMovieTitle')
            from resources.lib.gui import parsers
            url = parsers.parse(urll)
            subs = []
            is_array = lambda var: isinstance(var, (list))
            if is_array(url):
                subs =url[1]
                url = url[0]
                isArray = True
            url = str(url).replace("#", "|")
            url = url.strip()  # 
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')    




