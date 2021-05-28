#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
#https://prod.radio-api.net/stations/local?count=10
#https://prod.radio-api.net/stations/now-playing?stationIds=1live,antennebayern,swr3,bayern3,wdr2,bigfm,swr1bw,wdr4,ndr2,ffn,n-joy,bayern1obb,swr1rp,rsh,ffh,dasding,absolutrelax,radiopsr,1livediggi,mdrjump,bremeneins,1046rtl,radiohamburg,antenne1,radiowmw,antenneniedersachsen,wdr2ruhrgebiet,hr3,bremenvier,radiobrsieg,mdrsputnik,antenneduesseldorf,ostseewellenord,radiorst,hr1,radiokoeln,bbradio,radiosaw,rs2,rpr1,dashitradio,berlinerrundfunk,antennemuenster,metropolfm,890rtl,youfm,antennethueringen,wdr2rheinruhr,oe3,radiobrocken
#https://prod.radio-api.net/stations/now-playing?stationIds=skylinethessaloniki,bignationfm,dimensionerelax
#https://prod.radio-api.net/stations/now-playing?stationIds=dkfm,loungefmterrace,inselradio
#https://prod.radio-api.net/stations/now-playing?stationIds=antennebayerndancexxl,hirschmilch-electronic,beautifulinstrumentalschannel
#https://prod.radio-api.net/stations/local?count=10


SITE_IDENTIFIER = 'radio_de'
SITE_NAME = 'radio_de'
SITE_DESC = 'Replay TV'


  
URL_SEARCH = ('', 'showMovies')
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


    oGui.setEndOfDirectory()  


def mradiode():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')                  
    oParser = cParser()
    sUrl = "https://www.radio.de/top-stations"  
    sHtmlContent = getHtml(sUrl)
    sHtmlContent = sHtmlContent.replace('\n','')
   # sHtmlContent =oParser.abParse(sHtmlContent, '"topTenStations":[')
   
                
    sPattern = '<a title=".*?" data-testid="list-item" target="_self" rel href="(.*?)">.*?</span>(.*?)</div>'
                                           

    
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
       
        
        for aEntry in aResult[1]:
           
          
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            tle =sUrl
            if not 'http' in sUrl:
                sUrl = 'https://www.radio.de/s/' + sUrl
            
             #sUrl =to_utf8(sUrl)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
       

    oGui.setEndOfDirectory()    




def radiode():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')                  
    oParser = cParser()
    sUrl = "https://www.radio.de/top-stations"  
    sHtmlContent = getHtml(sUrl)
    sHtmlContent = sHtmlContent.replace('\n','')
    sHtmlContent =oParser.abParse(sHtmlContent, '"topTenStations":[')
   
     
    sPattern = '"city":"(.*?)","country":".*?","genres":."(.*?)".,"id":"(.*?)","logo100x100":".*?","logo300x300":"(.*?)","logo630x630":"","name":"(.*?)","type":".*?"'
                                           

    
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
       
        
        for aEntry in aResult[1]:
            sPicture = aEntry[3]
            city = aEntry[0]
            genres= aEntry[1]
            sTitle = aEntry[4]
            sUrl = str(aEntry[2])
            tle =sUrl
            if not 'http' in sUrl:
                sUrl = 'https://www.radio.de/s/' + sUrl
            
             #sUrl =to_utf8(sUrl)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('Urlll', tle)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
       

    oGui.setEndOfDirectory()    


def showradyolist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '<div id="kanal_listesi">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    

    sPattern = '<a href="./(.*?)" title="(.*?)">.*?<div class="kanal_resim"><img src="../(.*?)"'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[0]+'-'+ aEntry[2]
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'shradyo', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    


def shradyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
     

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<td width=".*?"><a href="(.*?)">(.*?)</a></td>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    

def showradyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<tr class="sectiontableentry.*?" >.*?<a href="(.*?)">(.*?)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    
#"streams":[{"url":"https://addrad.io/4WRMN2"
def Auth(u):
  
   import time
  
   
       
   sUrl ='https://prod.radio-api.net/stations/now-playing?stationIds='+u
   

  
   while True:
       time.sleep(20)
      
      
       data=getHtml(sUrl)
       info("Good Auth :" + data)
       ign = re.search('"title":"(.*?)"', to_utf8(data)).group(1)
        #urll=urll.replace('[{"title":"','').replace('","stationId":"','=').replace('"}]','')
       info("Good Auth :" + ign)
       return  ign     

def expensive_(u):
    # ...
   time.sleep(5)
  
   return Auth(u)







def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sUr = oInputParameterHandler.getValue('Urlll')             
    data=getHtml(Url) 
#    logger.info('resolve: ' + data)
    Thumbnail = re.findall('"logo300x300":"(.*?)"', data, re.S)[0]        
    url = re.search('":"audio/aacp".,."url":"(.*?)"',data).group(1)                    
    addLink('[COLOR lightblue][B]OTV MEDIA RADYO >  [/B][/COLOR]'+name,url,Thumbnail)



  
