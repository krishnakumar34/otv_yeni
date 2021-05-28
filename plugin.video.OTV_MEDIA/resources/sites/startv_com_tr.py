#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'startv_com_tr'
SITE_NAME = 'startv_com_tr'

import xbmcplugin, xbmcgui
URL_MAIN = 'http://www.startv.com.tr'
#from xcanlitvzone import sshowBox19              

MOVIE_HD = (True, 'showGenre')
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        







def sEcho(s):
      if 'pageIndex=0' in s:
        s=s.replace('pageIndex=0','pageIndex=1')
        return s 
      if 'pageIndex=1' in s:
        s=s.replace('pageIndex=1','pageIndex=2')
        return s 
      if 'pageIndex=2' in s:
        s=s.replace('pageIndex=2','pageIndex=3')
        return s 
      if 'pageIndex=3' in s:	
        s=s.replace('pageIndex=3','pageIndex=4')
        return s 
      if 'pageIndex=4' in s:	
        s=s.replace('pageIndex=4','pageIndex=5')
        return s 
      if 'pageIndex=5' in s:	
        s=s.replace('pageIndex=5','pageIndex=6')
        return s 
      if 'pageIndex=6' in s:	
        s=s.replace('pageIndex=6','pageIndex=7')
        return s 
      if 'pageIndex=7' in s:	
        s=s.replace('pageIndex=7','pageIndex=8')
        return s 
      if 'pageIndex=8' in s:	
        s=s.replace('pageIndex=8','pageIndex=9')
        return s 
      if 'pageIndex=9' in s:	
        s=s.replace('pageIndex=9','pageIndex=10')
        return s 
      if 'pageIndex=10' in s:	
        s=s.replace('pageIndex=10','pageIndex=11')
        return s 
      if 'pageIndex=11' in s:	
        s=s.replace('pageIndex=11','pageIndex=12')
        return s 
      if 'pageIndex=12' in s:	
        s=s.replace('pageIndex=12','pageIndex=13')
        return s 
      if 'pageIndex=13' in s:	
        s=s.replace('pageIndex=13','pageIndex=14')
        return s 
      if 'pageIndex=14' in s:	
        s=s.replace('pageIndex=14','pageIndex=15')
        return s 
      if 'pageIndex=15' in s:	
        s=s.replace('pageIndex=15','pageIndex=16')
        return s 
      if 'pageIndex=16' in s:	
        s=s.replace('pageIndex=16','pageIndex=17')
        return s
      if 'pageIndex=17' in s:	
        s=s.replace('pageIndex=17','pageIndex=18')
        return s 
      if 'pageIndex=18' in s:	
        s=s.replace('pageIndex=18','pageIndex=19')
        return s 
      if 'pageIndex=19' in s:	
        s=s.replace('pageIndex=19','pageIndex=20')
        return s 
      if 'pageIndex=20' in s:	
        s=s.replace('pageIndex=20','pageIndex=21')
        return s 
      if 'pageIndex=21' in s:	
        s=s.replace('pageIndex=21','pageIndex=22')
        return s 
      if 'pageIndex=22' in s:	
        s=s.replace('pageIndex=22','pageIndex=23')
        return s 
      if 'pageIndex=23' in s:	
        s=s.replace('pageIndex=23','pageIndex=24')
        return s 
      if 'pageIndex=24' in s:	
        s=s.replace('pageIndex=24','pageIndex=25')
        return s 
      if 'pageIndex=25' in s:	
        s=s.replace('pageIndex=25','pageIndex=26')
        return s 
      if 'pageIndex=26' in s:	
        s=s.replace('pageIndex=26','pageIndex=27')
        return s 



 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

def startvcomtr():
    oGui = cGui()
    
    tarzlistesi = []                                  
    
    tarzlistesi.append(("Star TV Canli", "https://lcgid8xu.rocketcdn.com/startvhd.stream_720p/chunklist.m3u8"))
#    tarzlistesi.append(("Star TV YEDEK", "https://www.youtube.com/watch?v=jWP3ntl64I4&feature=youtu.be"))
    tarzlistesi.append(("NTV", "https://nt4p9nef.rocketcdn.com/ntvhd.stream_720p/chunklist-u30i93dth.m3u8"))
#    tarzlistesi.append(("NTV SPOR", "http://dz4qxz19.rocketcdn.com/ntvsporhd.stream_720p/chunklist_b2328000_sltur.m3u8"))
    tarzlistesi.append(("KRAL TV", "http://dz4qxz19.rocketcdn.com/kraltv_720/chunklist_b2328000_sltur.m3u8"))
    tarzlistesi.append(("KRAL POP", "http://dz4qxz19.rocketcdn.com/kralpop_720/chunklist_b2328000_sltur.m3u8"))
    tarzlistesi.append(("KRAL WORLD", "http://dz4qxz19.rocketcdn.com/kralworldtv_720/chunklist_b2328000_sltur.m3u8"))
    tarzlistesi.append(("TLC", "https://pa9agxjg.rocketcdn.com/tlctv.smil/chunklist_b2328000_sltur.m3u8"))

    tarzlistesi.append(("Diziler", "https://www.startv.com.tr/dizi"))
    tarzlistesi.append(("Arsiv Diziler", "https://www.startv.com.tr/dizi"))
    for sTitle,sUrl2 in tarzlistesi:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle',sTitle)
        if sTitle == 'Star TV Canli':
             oGui.addDir(SITE_IDENTIFIER, 'showshowHosters',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'NTV':
             oGui.addDir(SITE_IDENTIFIER, 'showshowHosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KRAL POP':
             oGui.addDir(SITE_IDENTIFIER, 'showshowHosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Diziler':
             oGui.addDir(SITE_IDENTIFIER, 'Diziler', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Arsiv Diziler':
             oGui.addDir(SITE_IDENTIFIER, 'arsivdiziy', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KRAL WORLD':
             oGui.addDir(SITE_IDENTIFIER, 'showshowHosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Star TV':
             oGui.addDir(SITE_IDENTIFIER, 'StarTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KRAL TV':
             oGui.addDir(SITE_IDENTIFIER, 'showshowHosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TLC':
             oGui.addDir(SITE_IDENTIFIER, 'showshowHosters', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()

def Diziler(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    data = getHtml(sUrl)




    playlist = re.findall('<li class="col-md-3 col-xs-6 col-sm-3 col-lg-2 ">.*?<a href="(.*?)".*?data-src="(.*?)".*?alt="(.*?)"', data, re.S)
    for aEntry,resim,sGenre in playlist:
            
            Url= str(URL_MAIN) + aEntry +'/bolumler?ord=1&filterRadio=Episode'

            sTitle=replaceHTMLCodes(sGenre)   
            sTitle = cUtil().CleanName(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'Diziler2', sTitle, '', resim, '', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
def Diziler2():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
          
        
        sHtmlContent= getHtml(Url)
        oParser = cParser()                       
        sPattern = 'col-xs-12 col-sm-4 col-md-3 col-lg-3 no-line">.*?<a href="(.*?)".*?data-src="(.*?)".*?alt="(.*?)"'
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
                                                                
                    
                    sTitle =replaceHTMLCodes(sTitle) 
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
                    if '/serie/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    elif '/anime/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    else:
                      oGui.addMovie(SITE_IDENTIFIER, 'starvideoplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                sNextPage =sEcho(str(Url.replace('?ord=1&filterRadio=Episode','?pageIndex=0&ord=1&filterRadio=Episode')))
                if (sNextPage != False):
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                        oGui.addDir(SITE_IDENTIFIER, 'Diziler2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    
                oGui.setEndOfDirectory()



def arsivdiziy(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    data = getHtml(sUrl)




    playlist = re.findall('<li class="col-md-3 col-xs-6 col-sm-3 col-lg-2">.*?<a href="(.*?)".*?data-src="(.*?)".*?alt="(.*?)"', data, re.S)
    for aEntry,resim,sGenre in playlist:
            
            Url= str(URL_MAIN) + aEntry +'?ord=1&filterRadio=Episode'

            #sGenre=replaceHTMLCodes(sGenre)   
            sGenre =malfabekodla(sGenre) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', sGenre)
            oGui.addTV(SITE_IDENTIFIER, 'arsivdiziy2', sGenre, '', resim, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()        
def arsivdiziy2():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
          
        
        sHtmlContent= getHtml(Url)
        oParser = cParser()                       

        sPattern = 'col-md-3 col-xs-6 col-sm-4">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)">'
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
                                                                
                    
                    sTitle =replaceHTMLCodes(sTitle) 
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
                    if '/serie/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    elif '/anime/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    else:
                      oGui.addMovie(SITE_IDENTIFIER, 'starvideoplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                sNextPage =sEcho(str(Url.replace('?ord=1&filterRadio=Episode','?pageIndex=0&ord=1&filterRadio=Episode')))
                if (sNextPage != False):
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                        oGui.addDir(SITE_IDENTIFIER, 'arsivdiziy2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    
                oGui.setEndOfDirectory()


                 
def starvideoplayer():
        oGui = cGui()
        oParser = cParser()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        sThumbnail = oInputParameterHandler.getValue('sThumbnail')
        sTitle = oInputParameterHandler.getValue('sMovieTitle')
       
        
        sHtmlContent =getHtml(Url) 
        sPattern1 = '"videoUrl": "(.*?)"'
        
        aResult = oParser.parse(sHtmlContent, sPattern1)
        if (aResult[0] == True):
            son = aResult[1][0]
            Json =getHtml(son) 
            #Json =str(page)
            page = json.loads(Json)
            pag = page['data']['flavors']
            sUrl=pag['hls']
       #     hls":"https:\/\/zyewxjau.rocketcdn.com\/Dizi\/iyigundekotugunde\/STAR_iyi_gunde_kotu_gunde_4_bolum.smil\/playlist.m3u8?token=t2YF70vvedGJN2VmmmzokQ&expires=1616069190&r=16"                        # data
            #logger.info("Good aJson:" + str(pag)) 
            sUrl=sUrl+'|Referer=https://www.startv.com.tr/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + sTitle,  sUrl,sThumbnail)


def showshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')+'|Referer=https://www.canlitv.today/'
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
#    sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    logger.info("Good aJson:" + sUrl) 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + sTitle,  sUrl,'')

