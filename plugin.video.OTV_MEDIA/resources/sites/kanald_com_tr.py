#-*- coding: utf-8 -*-

from resources.sites.LIVETV2 import *

# http://destek.korax.com.tr/UYDUSIS/CLOUD.txt
SITE_IDENTIFIER = 'kanald_com_tr'
SITE_NAME = 'KANAL D'
SITE_DESC = 'Replay TV'
NURL_MAIN= 'http://www.netd.com'
MOVIE_diziizle = 'https://www.kanald.com.tr'
URL_MAIN = 'http://www.netd.com/dizi'
URL_DMAIN = 'https://www.kanald.com.tr'
URL_PIC = 'http://assets.dogannet.tv/img/75/327x183/'
MOVIE_VIEWS = (True, 'showGenre')
MOVIE_HD = (True, 'showGenre')
URL_engelsiz = 'http://engelsiz.kanald.com.tr'
URL_engelsizpic = 'http://engelsiz.kanald.com.tr/'                  
def CleanTitle(title):
    title = cUtil().unescape(title)
    title = cUtil().removeHtmlTags(title)
    try:
        #title = unicode(title, 'utf-8')
        title = unicode(title, 'iso-8859-1')
    except:
        pass
    title = unicodedata.normalize('NFD', title).encode('ascii', 'ignore')
    
    return title.encode( "utf-8")
ua = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
linkler = []
kaynaklar = []
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
user_file = os.path.join(RESOURCES_DIR, 'channels_tr.m3u')
oParser = cParser()
s = requests.Session()
def BluEcho(s):
    s=s
    if '=0' in s:
        s=s.replace('=0','=24')
        return s 
    if '=24' in s:	
        s=s.replace('=24','=48')
        return s 
    if '=48' in s:	
        s=s.replace('=48','=72')
        return s 
    if '=72' in s:	
        s=s.replace('=72','=96')
        return s 
    if '=96' in s:	
        s=s.replace('=96','=120')
        return s 
    if '=120' in s:	
        s=s.replace('=120','=144')
        return s 
    if '=144' in s:	
        s=s.replace('=144','=168')
        return s 
    return False 

def partnext(s):
    s=s
    if 'part=1-6' in s:
        s=s.replace('part=1-6','part=1-6')
        return s 
    if 'part=1-6' in s:
        s=s.replace('part=1-6','part=2-6')
        return s 
    if 'part=2-6' in s:
        s=s.replace('part=2-6','part=3-6')
        return s 
    if 'part=3-6' in s:	
        s=s.replace('part=3-6','part=4-6')
        return s 
    if 'part=4-6' in s:	
        s=s.replace('part=4-6','part=5-6')
        return s 
    if 'part=5-6' in s:	
        s=s.replace('part=5-6','part=6-6')
        return s 
    return False
def sEcho(s):
    s=s
    if '=1' in s:
        s=s.replace('=1','=2')
        return s 
    if '=2' in s:
        s=s.replace('=2','=3')
        return s 
    if '=3' in s:	
        s=s.replace('=3','=4')
        return s 
    if '=4' in s:	
        s=s.replace('=4','=5')
        return s 
    if '=5' in s:	
        s=s.replace('=5','=6')
        return s 
    if '=6' in s:	
        s=s.replace('=6','=7')
        return s 
    if '=7' in s:	
        s=s.replace('=7','=8')
        return s 
    if '=8' in s:	
        s=s.replace('=8','=9')
        return s 
    if '=9' in s:	
        s=s.replace('=9','=10')
        return s 
    if '=10' in s:	
        s=s.replace('=10','=11')
        return s 
    if '=11' in s:	
        s=s.replace('=11','=12')
        return s 
    if '=12' in s:	
        s=s.replace('=12','=13')
        return s 
    if '=13' in s:	
        s=s.replace('=13','=14')
        return s 
    if '=14' in s:	
        s=s.replace('=14','=15')
        return s 
    if '=15' in s:	
        s=s.replace('=15','=16')
        return s 
    if '=16' in s:	
        s=s.replace('=16','=17')
        return s
    if '=17' in s:	
        s=s.replace('=17','=18')
        return s 
    if '=18' in s:	
        s=s.replace('=18','=19')
        return s 
    if '=19' in s:	
        s=s.replace('=19','=20')
        return s 
    if '=20' in s:	
        s=s.replace('=20','=21')
        return s 
    return False 



try:
    with io.open(user_file, 'r', encoding='utf-8') as f:
        user = f.read()
except IOError:
    user = ''


def turkTV():
        oGui = cGui()
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir('fox_com_tr', 'foxcomtr', 'FOX TV Sayfa', 'FOXLogo.jpg', oOutputParameterHandler)

        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir(SITE_IDENTIFIER, 'kanald', 'Kanal D Sayfa', 'kanald_com_tr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir('atv_com_tr', 'atvcomtr','ATV Sayfa', 'atv_com_tr.png', oOutputParameterHandler)


        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir('showtv_com_tr', 'showtvcomtr','SHOW TV Sayfa', 'showtv_com_tr.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir('tv8_com_tr', 'tv8comtr','TV 8 Sayfa', 'tv8_com_tr.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir('trt_net_tr', 'trtnettr', 'TRT Sayfa', 'trt_net_tr.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addDir('startv_com_tr', 'startvcomtr','STAR TV Sayfa', 'startv_com_tr.png', oOutputParameterHandler)
        
#        oOutputParameterHandler = cOutputParameterHandler()
#        oOutputParameterHandler.addParameter('siteUrl', 'http://')
#        oGui.addDir(SITE_IDENTIFIER, 'blutv', 'BluTV Sayfa', 'BluTV_Logo.png', oOutputParameterHandler)
          
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.kanald.com.tr/actions/content/media/542410a361361f36f4c3fcf1')
        oGui.addDir(SITE_IDENTIFIER, 'blutv_1','BLUTV Canli Yayin', 'BluTV_Logo.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://canlitv.gen.tl/tr?sayfa=1')
        oGui.addDir('xstreamcanlitv', 'iostreamcanlitv','HD Canli Yayin izle', 'logocanl.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://izle.canlitvlive.io')
        oGui.addDir('xizle_canlitvlive_io', 'Canlitvlive_io','Canlitvlive.io', 'canliio.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://www.canlitv.me/tv2?sayfa=1')
        oGui.addDir('xcanlitvzone', 'Canlitv','Canli TV zone', 'canlitvzone.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'https://canlitv.gen.tl/tr?sayfa=1')
       
        oGui.addDir('xCanLiTVlive', 'CanLiTVlive','Canli TV live', 'canlitvs.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        
        oOutputParameterHandler.addParameter('siteUrl', 'http://destek.korax.com.tr/UYDUSIS/CLOUD.txt')
        oGui.addDir(SITE_IDENTIFIER, 'turkom2','ULUSAL YEREL Canli TV ', 'canlitvs.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()
from collections import OrderedDict
from resources.lib.handler.requestHandler3 import cRequestHandler

                   
def mturkom2(): #affiche les genres
    oGui = cGui()
    url='http://destek.korax.com.tr/UYDUSIS/CLOUD.txt'    

    headers = OrderedDict(
        [
                    ("Host", "destek.korax.com.tr"),
                    ("User-Agent", "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"),
                    ("Connection", "Keep-Alive"),
                    ("Accept-Encoding", "gzip"),
                    ("Cookie", "__cfduid=d2be7a78ec3519e65c5a97340486b99ba1614805382"),
                ]
            )

    req = requests.Request("POST", url, data="")
    prepped = req.prepare()
    prepped.headers = headers
    r = s.send(prepped, timeout=15, verify=False)
    r.raise_for_status()
    html =r.text
    
    sHtmlContent = to_utf8(html)
    logger.info("sHtmlContent: %s" % sHtmlContent ) 
    sPattern = '(.*?),(.*?)\#'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            
            Link = aEntry[1]
            sTitle=  aEntry[0]                                                                     
                                        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'iptvturke2', sTitle, 'genres.png', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()        
def turkom2():
    oGui = cGui()
    
    import re
    url='http://destek.korax.com.tr/UYDUSIS/CLOUD.txt'    

    headers = OrderedDict(
        [
                    ("Host", "destek.korax.com.tr"),
                    ("User-Agent", "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"),
                    ("Connection", "Keep-Alive"),
                    ("Accept-Encoding", "gzip"),
                    ("Cookie", "__cfduid=d2be7a78ec3519e65c5a97340486b99ba1614805382"),
                ]
            )

    req = requests.Request("POST", url, data="")
    prepped = req.prepare()
    prepped.headers = headers
    r = s.send(prepped, timeout=15, verify=False)
    r.raise_for_status()
    html =r.text
    
    html = to_utf8(html)
    regex = re.compile('(.*?),(.*?)\n', re.MULTILINE | re.DOTALL).findall(html)
    for sTitle,Url in regex:
        sTitle = malfabekodla(sTitle)
        
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'iptvturke2', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()  

def iptvturke2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Urll=oInputParameterHandler.getValue('siteUrl')+'|User-Agent=Lavf/57.73.100'
 
    name=oInputParameterHandler.getValue('sMovieTitle')
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,Urll, '')


def blutv():
    oGui = cGui()
    tarzlistesi= []                                                                                                                                                  
    tarzlistesi.append(("Canli Yayin",  "https://www.kanald.com.tr/actions/content/media/542410a361361f36f4c3fcf1"))
                         #  surl ="https://www.blutv.com.tr/quark/content/getresults?category=%s&order=&platform=com.blu.lama&query=&segment=default&skip=0"%  sUrl
       
    tarzlistesi.append(("Dizi",  "https://www.blutv.com.tr/quark/content/getresults?category=Genres&order=&platform=com.blu.lama&query=&segment=default&skip=0"))
#    tarzlistesi.append(("Film",  "https://www.blutv.com.tr/quark/content/getresults?category=film&order=&platform=com.blu.lama&query=&segment=default&skip=0"))
    for sTitle,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if 'Canli Yayin' in sTitle:
            oGui.addDir(SITE_IDENTIFIER, 'blutv_1', '[COLOR FFAFEEEE] '+ sTitle +'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif 'Dizi' in sTitle:
            oGui.addDir(SITE_IDENTIFIER, 'Diziblutv', '[COLOR FFAFEEEE]  '+ sTitle +'[/COLOR]', 'genres.png', oOutputParameterHandler)
        else:                           #  blutv_d1
            oGui.addDir(SITE_IDENTIFIER, 'blutv_film', '[COLOR FFAFEEEE]'+ sTitle +'[/COLOR]', 'genres.png', oOutputParameterHandler)


       
    oGui.setEndOfDirectory()
def mmDiziblutv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')      
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
    logger.info("sJson_auth: %s" % sJson ) 
    aJson = json.loads(sJson)
    for cat in aJson["data"]:
    
       logger.info("sJson_auth: %s" % cat) 

def Diziblutv():
    oGui = cGui()
    tarzlistesi= []                                                                                                                                                  
    tarzlistesi.append(("Aile",  "tum-aile-dizileri"))
    tarzlistesi.append(("Aksiyon - Macera",  "tum-aksiyon-macera-dizileri"))
    tarzlistesi.append(("Drama",  "drama"))
    tarzlistesi.append(("Komedi",  "tum-komedi-dizileri"))
    tarzlistesi.append(("Polisiye - Suc -Macera",  "tum-polisiye-suc-dizileri"))
    tarzlistesi.append(("Romantik",  "tum-romantik-diziler"))

    for sTitle,sUrl in tarzlistesi:
        surl ="https://www.blutv.com.tr/quark/content/getresults?category=%s&order=&platform=com.blu.lama&query=&segment=default&skip=0"%  sUrl
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', surl)
        if 'Canli Yayin' in sTitle:
            oGui.addDir(SITE_IDENTIFIER, 'blutv_1', '[COLOR FFAFEEEE] '+ sTitle +'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif '/sinemalar/' in sTitle:
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR FFAFEEEE]  '+ sTitle +'[/COLOR]', 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'blutv_d1', '[COLOR FFAFEEEE]'+ sTitle +'[/COLOR]', 'genres.png', oOutputParameterHandler)


       
    oGui.setEndOfDirectory()
def blutv_d1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
    logger.info("sJson_auth: %s" % sJson )        
    aJson = json.loads(sJson)
    for cat in aJson["data"]["models"]:
            catid =cat['PlayUrl']
            sTitle =cat['Title']
            sPic=cat['Image']
            cat=cat['Description']
            
#            logger.info("sJson_blutv_d1: %s" % surl ) 
            surl ="https://www.blutv.com.tr/quark/content/getcontent?platform=com.blu.lama&segment=default&url="+   catid
            sPicture="https://blutv-images.mncdn.com/q/t/i/bluv2/80/600x338/"+sPic
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',surl )
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'blutv_d2', sTitle, sPicture, sPicture, cat, oOutputParameterHandler)
    oGui.setEndOfDirectory()       
def blutv_film():            
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = cRequestHandler(sUrl).request()    
    aJson = json.loads(sJson)
    
    for cat in aJson["data"]["models"]:
            catid =cat['PlayUrl']
            sTitle =cat['Title']
            sPic=cat['MediaId']
            cat=cat['Description']
#            sTitle = alfabekodla(sTitle)
            surl ="https://www.blutv.com.tr/quark/content/getcontent?platform=com.blu.lama&segment=default&url="+   catid
            
            sPicture="https://blutv-images.mncdn.com/q/t/i/bluv2/80/600x338/"+sPic
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',surl )
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'mblutv_d2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()  
def mblutv_d2():
    oGui = cGui()

    
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    
    sHtmlContent = getHtml(sUrl)

    
    sHtmlContent =sHtmlContent.replace('\\/', '/').replace('Url":null', 'Url"http://www.blutv.com.tr/media/5b4774c5866ac3040ce492ac.clear"')
    oParser = cParser()                                       
                                       
    sPattern = '"Poster":"(.*?)","Source":"(.*?)","Url"(.*?)".*?"SeasonNumber":(.*?),"StartDate":".*?","Title":"(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        for aEntry in aResult[1]:
                
            
            surl = aEntry[1]
            logger.info("sJson_auth: %s" % surl )
            if  'zamanlar-adanada/3-sezon' in aEntry[1]:
                 surl='https://blutv.akamaized.net/CHLS/SIFIR_BIR_SZN_'+ aEntry[3]+'_BLM_0'+ aEntry[4]+'_1080_RVZ/SIFIR_BIR_SZN_'+ aEntry[2]+'_BLM_0'+ aEntry[3]+'_1080_RVZ.m3u8'
                 #surl='https://apicache.blutv.com.tr/q/t/c/bluv2/5a00525dfbead333d44c1c3a.m3u8'
            elif  'zamanlar-adanada/1-sezon' in aEntry[1]:

                 surl='https://blutv.akamaized.net/CHLS/SIFIR_BIR_BIR_ZAMANLAR_ADANADA_S_1_B_1_2500_1_layer01/SIFIR_BIR_BIR_ZAMANLAR_ADANADA_S_1_B_1_2500_1_layer01.m3u8'
            
            
            sTitle ='Sezon-'+ aEntry[3]+' '+ aEntry[4]                                                           
            Referer = aEntry[2]
            logger.info("sJson_auth: %s" % surl )
            img = aEntry[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('Referer', Referer)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play_Dblutv', sTitle, '',img, '', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()     


def mDiziblutv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')      
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
    logger.info("sJson_auth: %s" % sJson ) 
    Json = json.loads(sJson)
    pag = Json['data']['model'] 
    pa =pag["Media"]
    url=pa['Url']
    name =pa['Title']
    logger.info("sJson_auth: %s" %name) 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def blutv_d2():            
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')      
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
#    logger.info("sJson_auth: %s" % sJson ) 
    Json = json.loads(sJson)
    pag = Json['data']['model']                                      
    paga =pag['Seasons']
    for cat  in paga:
            sTitle =cat['Title']
            sPic=cat['Image']
            cat=cat['Url']
            #sPic=pa['Poster']
            sPicture="https://blutv-images.mncdn.com/q/t/i/bluv2/80/600x338/"+ sPic
            surl ="https://www.blutv.com.tr/quark/content/getcontent?platform=com.blu.lama&segment=default&url="+   cat
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',surl )
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'blutv_d3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()       
   
def blutv_d3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')      
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sJson = getHtml(sUrl)    
    j = json.loads(sJson)
    pag = j['data']['model']
    for cat in  pag['Seasons']:  
         s1 = json.dumps(cat)
         d2 = json.loads(s1)
         d3 =d2['Episodes']
         for cata in  d3: 
              s1 = json.dumps(cata)
              d2 = json.loads(s1)
              pa = d2['Media']  
              sTitle =pa['Title']
              sPic=pa['Poster']
              #sPic=cat['Image']
              cat=pa['Url']
              surl=pa['Source']
              sPicture="https://blutv-images.mncdn.com/q/t/i/bluv2/80/600x338/"+ sPic
              logger.info("sJson_Source: %s" % surl )
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl',surl )
              oOutputParameterHandler.addParameter('Referer',cat )
              oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
              oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
              oGui.addMovie(SITE_IDENTIFIER, 'play_blutv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()       



def blutv_1():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_foxtv/smil:foxtv_sd.smil/playlist.m3u8')
    oGui.addDir(SITE_IDENTIFIER, 'blutv_2','FOX TV', 'fox_com_tr.png', oOutputParameterHandler)
        
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_kanald/smil:kanald_sd.smil/playlist.m3u8') 
    oOutputParameterHandler.addParameter('Referer', 'http://www.blutv.com.tr/media/569cafd6058d024688a14441.clear')
    oGui.addMovie(SITE_IDENTIFIER, 'blutv_2',  'Kanal D', 'https://upload.wikimedia.org/wikipedia/tr/thumb/c/ca/Kanal_D_logo.svg/943px-Kanal_D_logo.svg.png', 'https://upload.wikimedia.org/wikipedia/tr/thumb/c/ca/Kanal_D_logo.svg/943px-Kanal_D_logo.svg.png', '', oOutputParameterHandler)

    #rajout listage film nouveauté   
    oOutputParameterHandler = cOutputParameterHandler()
                                                     
    oOutputParameterHandler.addParameter('siteUrl', 'https://tv8.personamedia.tv/tv8hls?fmt=hls')
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/54773060f5ac7613f46f398b.clear')
    oGui.addMovie(SITE_IDENTIFIER, 'blutv_2',  'TV8 HD', 'https://img.tv8.com.tr/s/template/v2/img/tv8-logo.png', 'https://img.tv8.com.tr/s/template/v2/img/tv8-logo.png', '', oOutputParameterHandler)
      
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_tv8_5/smil:tv8_5_sd.smil/playlist.m3u8')
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oGui.addMovie(SITE_IDENTIFIER, 'blutv_2',  'TV 8,5', 'https://www.haberoran.com/files/uploads/news/default/26-nisan-carsamba-tv-eff9539d4cb9c7959f38.png', 'https://www.haberoran.com/files/uploads/news/default/26-nisan-carsamba-tv-eff9539d4cb9c7959f38.png', '', oOutputParameterHandler)

           
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_showtv/smil:show_sd.smil/playlist.m3u8')
    oGui.addDir(SITE_IDENTIFIER, 'blutv_2','SHOW TV', 'showtv_com_tr.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_sportstv/smil:sportstv_sd.smil/playlist.m3u8')
    oGui.addDir(SITE_IDENTIFIER, 'blutv_2','SPORTSTV', 'blutv_sportstv.png', oOutputParameterHandler)
                                                                                                    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oOutputParameterHandler.addParameter('siteUrl', 'https://mn-nl.mncdn.com/blutv_vuslattv/smil:vuslattv_sd.smil/playlist.m3u8')
    oGui.addDir(SITE_IDENTIFIER, 'blutv_2','VUSLATTV', 'blutv_vuslattv_tr.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oOutputParameterHandler.addParameter('siteUrl', 'https://d20aqhpvpegrs2.cloudfront.net/out/v1/d9da7879327241d3831f39b61016a353/master.m3u8')
    oOutputParameterHandler.addParameter('sMovieTitle', 'Blu TV Komedi')
    oGui.addDir(SITE_IDENTIFIER, 'play_blutv','Blu TV Komedi', 'blutv_komedi_tr.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('Referer','http://www.blutv.com.tr/media/589c1396058d02b288a8cf71.clear')
    oOutputParameterHandler.addParameter('siteUrl', 'https://d1vftv9up76vki.cloudfront.net/out/v1/6f27e3bde7274af6b06befa08cd839d7/master.m3u8')
    oOutputParameterHandler.addParameter('sMovieTitle', 'Blu TV Aksiyon')
    oGui.addDir(SITE_IDENTIFIER, 'play_blutv','Blu TV Aksiyon', 'blutv_aksion_tr.png', oOutputParameterHandler)



    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'https://www.blutv.com.tr/quark/content/getpage?platform=com.blu.lama&segment=default&url=%2Fcanli-yayin'
    
   
    sJson = getHtml(sUrl)    
#    logger.info("sJson_auth: %s" % sJson ) 
    Json = json.loads(sJson)
    pag = Json['data']['model']                                       
    for cat  in pag['Controls']:
        s1 = json.dumps(cat)
        d2 = json.loads(s1)
        d3=d2['Contents']
        for cata in  d3: 
            s1 = json.dumps(cata)
            d2 = json.loads(s1)
            pa = d2['Media']  
            sTitle =pa['Title']
            sPic=pa['Id']
            Referer=pa['Url']
            surl=pa['Source']
            
            img ="https://blutv-images.mncdn.com/q/t/i/bluv2/80/600x338/"+sPic
            sTitle = malfabekodla(sTitle)
            sTitle = cUtil().CleanName(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('Referer', Referer)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'blutv_2', sTitle, '',img, '', oOutputParameterHandler)
        
        
    oGui.setEndOfDirectory()     

def similarTitle(s):

    list_spe = ['&', '\'', ',', '.', ';', '!']

    s = s.strip()
    if ' ' in s:
        try:
            s = str(s).lower()
            sx = s.split(' ')
            snew = sx[0] + ' ' + sx[1]
            for spe in list_spe:
                snews = snew.replace(spe, '')
            return True, snews.lower()
        except:
            return False, False
    return False, False


def blutv_2():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    UrlL = oInputParameterHandler.getValue('siteUrl')
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
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

            


    
       

def kanald():
    oGui = cGui()
    tarzlistesi= []
    tarzlistesi.append(("KANAL D CANLI.TV", "http://orhantv"))
    
    
    tarzlistesi.append(("Yeni DIZILER", "https://www.kanald.com.tr/diziler"))
    tarzlistesi.append(("Tüm Arşiv Dizileri", "https://www.kanald.com.tr/diziler/arsiv?page=1"))
    tarzlistesi.append(("Görme ve Işitme Engelliler için DIZILER", "http://engelsiz.kanald.com.tr/"))
    for sTitle,sUrl2 in tarzlistesi:
          
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'KANAL D CANLI.TV':
             oGui.addDir(SITE_IDENTIFIER, 'kanaldTV', sTitle, 'genres.png', oOutputParameterHandler)

        elif sTitle == 'MUZIK':
             oGui.addDir(SITE_IDENTIFIER, 'showMUZIK', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Yeni DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Tüm Arşiv Dizileri':
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Görme ve Işitme Engelliler için DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'showengelsiz', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
  
def kanaldTV():
    oGui = cGui()
    tarzlistesi= []                                                                                                                                                  
    tarzlistesi.append(("Kanal D ", "https://upload.wikimedia.org/wikipedia/tr/thumb/c/ca/Kanal_D_logo.svg/522px-Kanal_D_logo.svg.png", "https://www.kanald.com.tr/actions/media?id=542410a361361f36f4c3fcf1&p=1&pc=1"))
    tarzlistesi.append(("CNN TURK ", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/CNN_T%C3%BCrk_logo.svg/1280px-CNN_T%C3%BCrk_logo.svg.png", "http://www.cnnturk.com/action/media/51cc1dbd32dc9f19b8bc77cf"))
    tarzlistesi.append(("TV2 ", "https://i.pinimg.com/originals/60/a1/00/60a100b9dc9c5bab1ed9c7442ea6acd0.png", "https://www.teve2.com.tr/action/media/564da04ef5ac761dbc5e0a13"))
    tarzlistesi.append(("Dream Turk ", "https://upload.wikimedia.org/wikipedia/tr/archive/b/bc/20200411150543%21Dream_T%C3%BCrk_logosu.png", "http://dreamturk.com.tr/actions/content/media/566ab958980ea810b4658d96"))
    tarzlistesi.append(("Dream TV ", "https://i.dreamturk.com.tr/i/dreamturk/100/600x315/f/5559eb1e9ebea45f62e626c9", "http://www.dreamtv.com.tr/actions/content/media/5565d197f5ac76262cb2bba5"))
    for sTitle,sPicture,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addMovie(SITE_IDENTIFIER, 'sshowBox2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

       
    oGui.setEndOfDirectory()
        
def showengelsiz(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sHtmlContent = reponse.read()
        sPattern = '<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl ='http://engelsiz.kanald.com.tr/'
        sHtmlContent = getHtml(sUrl)                    
        sPattern = '<li><a href="(.*?)" title="(.*?)">.*?<img src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = aEntry[1]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_engelsizpic) + sPicture
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_engelsiz) + sUrl
            
            sTitle = malfabekodla(sTitle)
            sTitle = sTitle.decode('ascii', errors='ignore')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sPicture))
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'engelsizparca', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'engelsizparca', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()


def engelsizparca():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPicture= oInputParameterHandler.getValue('sThumbnail')
    sHtmlContent = getHtml(sUrl)
    parse = re.search('<div class="list">(.*?)</select>', sHtmlContent, re.S)
    if parse:
       cats = re.findall('<option value="(.*?)".*?>(.*?)</option>', parse.group(1), re.S)
       for tagid,sTitle in cats:
            wq = 'http://engelsiz.kanald.com.tr/Video/Detail/'+tagid+'/1'
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', wq)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'engelsizBox', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        
    oGui.setEndOfDirectory()
def engelsizBox():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    
    urla  = "https://www.kanald.com.tr"
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    sUrl= re.findall("src: '(.*?)'", data)[0]   
    cookie = getUrl(sUrl, output='cookie').result
    logger.info("cookie: %s" % cookie)
    TIK='|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    sUrl=sUrl +'|Referer='+ Url +'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'

    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,sUrl,'')

def showMUZIK(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sPattern = '<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sHtmlContent = getHtml(sUrl)                      
        sPattern = '<noscript><img src="(.*?)".*?<a href="(.*?)">.*?<b>(.*?)</span>'
    sHtmlContent = sHtmlContent.replace('\n','')
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = aEntry[2]+' [COLOR lightblue]'
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_PIC) + sPicture
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('Picture', str(sTitle))
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showMovies', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMUZIK', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

def showMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = getHtml(Url)
    sPattern = '<div class="item col-6 col-md-4 col-lg-3"><a href="(.*?)" target="_self" class="poster-card" data-follow-id="(.*?)"><figure class="figure"><div class="img-wrap"><noscript><img src="(.*?)" alt="(.*?)">'
    sHtmlContent = sHtmlContent
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = aEntry[3]
            sPicture = str(aEntry[2])
            dataid=  aEntry[1]    
            sUrl =  str(URL_DMAIN) +str(aEntry[0])               
            bolumler=GetBolum(sUrl)                 #Pagen = aResult[1][0]
            Pagen = 'https://www.kanald.com.tr' +str(bolumler)+'?page=1'
             
            sTitle = malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Pagen))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'yeniDizi', sTitle, sPicture, sPicture,  sPicture, oOutputParameterHandler)
    oGui.setEndOfDirectory()

                    

 
def GetBolum(sUrl):  # Recupere les liens des regex
    chain  =getHtml(sUrl)
    r = re.search('<li class="breadcrumb-item"><a href=".+?" class="breadcrumb-link">B&#x130;LG&#x130;</a></li><li class="breadcrumb-item"><a href="(.+?/(?:bolum|bolumler))" class="breadcrumb-link">B&#xD6;L&#xDC;MLER</a></li>', chain)
    if (r):        
        url = r.group(1)                       
        url = url 
        return url
    r = re.search('<li class="breadcrumb-item"><a href=".*?" class="breadcrumb-link">YARI&#x15E;MA</a></li><li class="breadcrumb-item"><a href=".*?" class="breadcrumb-link">B&#x130;LG&#x130;</a></li><li class="breadcrumb-item"><a href="(.+?)"', chain)
    if (r):        
        url = r.group(1)
        url = url 
        return url
    r = re.search('<li class="breadcrumb-item"><a href="(.+?/(?:bolum|bolumler))"', chain)
    if (r):        
        url = r.group(1)
        url = url 
        return url
    r = re.search('</a></h1></li><li class="breadcrumb-item"><a href="(.+?/(?:bolum|bolumler))" class="breadcrumb-link">B&#xD6;L&#xDC;MLER</a></li>', chain)
    if (r):
        url = r.group(1)
        url = url 
        return url
    r = re.search('</a></h1></li><li class="breadcrumb-item"><a href=".+?" class="breadcrumb-link">B&#x130;LG&#x130;</a></li><li class="breadcrumb-item"><a href="(.+?/(?:bolum|bolumler)) class="breadcrumb-link">B&#xD6;L&#xDC;MLER</a>', chain)
    if (r):        
        url = r.group(1)                       
        url = url 
        return url

def yeniDizi(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ssUrl  = oInputParameterHandler.getValue('siteUrl')
    urla  = "https://www.kanald.com.tr/"
    referer=[('Referer',urla)]
    sHtmlContent=gegetUrl(ssUrl ,headers=referer)     
    sPattern = '<div class="item col-12 col-md-4 col-lg-3"><a href="(.*?)" target="_self" class="video-card mobile-horizontal" data-saved-id="(.*?)"><figure class="figure"><div class="img-wrap"><noscript><img src="(.*?)" alt="(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        for aEntry in aResult[1]:
            idi = aEntry[1]
            sTitle = aEntry[3]
            UUrl = "https://www.kanald.com.tr/actions/media?id=" +idi+ "&p=1&pc=1"                                   
            sPicture =  aEntry[2]
            sUrl =str(aEntry[0])
            if not 'http' in sUrl:
                sUrl ='https://www.kanald.com.tr'+ str(aEntry[1])
#              sGenre=replaceHTMLCodes(sGenre )
            sTitle = replaceHTMLCodes(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', UUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'DDizioynat', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
              
    if not sSearch:
            sNextPage =sEcho(str(ssUrl))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'yeniDizi','[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

def pageshowMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        sPattern = '<div class="film">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        ssUrl = oInputParameterHandler.getValue('siteUrl')
        #oRequestHandler = cRequestHandler(ssUrl)
        sHtmlContent = getHtml(ssUrl)         
        sPattern = '<div class="item col-6 col-md-4 col-lg-3"><a href="(.*?)" target="_self" class="wide-card" data-follow-id="(.*?)"><figure class="figure"><div class="img-wrap"><noscript><img src="(.*?)" alt="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = aEntry[3]
            sPicture =str(aEntry[2])
            dataid = aEntry[1]
            sUrl =  str(URL_DMAIN) +str(aEntry[0])
            bolumler=GetBolum(sUrl)                 
            Pagen = 'https://www.kanald.com.tr' +str(bolumler)+'?page=1'
            logger.info("Pagen_auth: %s" % Pagen) 
            sTitle = malfabekodla(sTitle)            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Pagen)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'pageshowDizi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        if not sSearch:
            sNextPage =sEcho(str(ssUrl))#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    if not sSearch:
        oGui.setEndOfDirectory()






def pageshowDizi(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sPattern = '<div class="film">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
    else:
        oInputParameterHandler = cInputParameterHandler()
        ssUrl  = oInputParameterHandler.getValue('siteUrl')
        sPicture = oInputParameterHandler.getValue('Picture')
        sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
        sHtmlContent =getHtml(ssUrl)      
        sPattern = '<div class="item col-12 col-md-4 col-lg-3"><a href="(.*?)" target="_self" class="video-card mobile-horizontal" data-saved-id="(.*?)"><figure class="figure"><div class="img-wrap"><noscript><img src="(.*?)" alt="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        for aEntry in aResult[1]:
            idi = aEntry[1]
            sTitle = aEntry[3]
            UUrl = "https://www.kanald.com.tr/actions/media?id=" +idi+ "&p=1&pc=1"                                   
            sPicture =  aEntry[2]
            sUrl =str(aEntry[0])
            if not 'http' in sUrl:
                sUrl ='https://www.kanald.com.tr'+ str(aEntry[1])
            sTitle = replaceHTMLCodes(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', UUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'DDizioynat', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
              
    if not sSearch:
            sNextPage =sEcho(str(ssUrl))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowDizi','[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

qualitylist = []
videolist = []


def m3u8oynat(url):
    urla  = "https://www.kanald.com.tr"
    referer=[('Referer',urla)]
    page=gegetUrl(url,headers=referer)
    url_main = '/'.join(url.split('/')[:-1]) + '/'
    values = re.findall('#.*?BANDWIDTH=(.*?)\n(.*?)\n', page)
    for value in values:
        logger.info("value_auth: %s" % value[0] ) 
        qualitylist.append(value[0])
        videolist.append(value[1])
        return  select(qualitylist,videolist)
  



def DDizioynat():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ua='Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    Urll = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    data=requests.get(Urll,headers={'Referer':Urll  ,'User-Agent':ua}).text
    TIK='|Referer='+Urll+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    urllkk= re.findall('"serviceUrl":"(.*?)","securePath":"(.*?)"', data)
    (serviceUrl,securePath)= urllkk[0]
    sUrl=serviceUrl+'/'+securePath  + TIK

    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,sUrl,'')

def __createDisplayStart(iPage):
    return (1 * int(iPage)) - 1
         
def pageshowDizi2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    urla  = "http://www.netd.com/"
    referer=[('Referer',urla)]
    sHtmlContent=gegetUrl(Url,headers=referer)     
    sPattern = '"video":."description":".*?","title":"(.*?)".*?"value":"(.*?)".*?"_id":"(.*?)"'
    sHtmlContent = sHtmlContent.replace('u002F', "")
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = aEntry[0]
            sPicture = 'http://assets.dogannet.tv/img/75/327x183/'+ str(aEntry[2])
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl ='http://media.netd.com.tr/'+ str(aEntry[1])
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
        sNextPage =sEcho(str(Url))
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowDizi2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()

def __checkForNextPage(sHtmlContent):
    
    sPattern = '<li class="active"><a href=".*?" class="nuxt-link-exact-active active">.*?</a></li><li><a href="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl ="http://www.netd.com"+ aResult[1][0] 
        return sUrl
               
 

 
def udizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    urla  = "http://www.netd.com/"
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    streamDaten = re.findall('<div class="col-md-3 col-sm-6"><div class="thumbnail thumbnail-play"><span><!----><a href="(.*?)"', data, re.S) 
    sUrl = "http://www.netd.com%s"  % (streamDaten[0])      
    oRequestHandler = cRequestHandler(sUrl)
    aResult= re.findall('"video":."description":".*?","title":"(.*?)".*?"value":"(.*?)"',Server, re.S|re.I)
    for name,sHosterUrl in aResult:
        url='http://media.netd.com.tr/' +sHosterUrl
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            
                               
def addLink(name,url,sThumbnail):
    ok=True
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title':name})
    liz.setArt({'thumb': sThumbnail, 'icon': sThumbnail, 'fanart': sThumbnail})
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 

       
def pageshowABC(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sPattern = '<div class="film">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sHtmlContent = getHtml(sUrl)
        sPattern = '"title":"(.*?)".*?"type":"applicationx-mpegURL","value":"(.*?)"'
    sHtmlContent = sHtmlContent
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle =aEntry[0]
            sPicture = picpic
            sUrl = aEntry[1]
            if not 'http' in sUrl:
                sUrl =URL_MAIN + sUrl
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle',sTitle)
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowDizi', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
 

def __NextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl =sUrl.replace('amp;', "")
    sPattern = 'data-url="(/actions/control/episodes.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_MAIN) + aResult[1][0]+'&skip=10'

    return False             


    return False
def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    ref = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',Url)
    Referer='https://' +ref
    #urla  = "https://www.kanald.com.tr"
    sUrl=GetRealUrl(Url)
    if not 'http' in sUrl:
       sUrl = "https://live.duhnet.tv/%s" %( sUrl)  
    sUrl=sUrl +'|Refererr='+ Referer +'&User-Agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    sUrl=sUrl.replace('//S2', '/S2')                                                                               
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)    
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()


def GetRealUrl(sUrl):  
    chain  =getHtml(sUrl)
    chain  =chain.replace('\u0026', "&").replace('/u0026', "&")
    r = re.search('"SecurePath":"(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('"SecurePath": "(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('"securePath":"(.*?)"', chain)            
    if (r):
        url = r.group(1)
        url =url.replace('\u0026', "&") 
        logger.info("url_auth: %s" % url )
        return url 

def partplay():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
     
    stream = re.findall("type: 'GET'.*?url: '/actions/control/player/(.*?)? ',", data, re.S)
    url = "http://www.netd.com/actions/content/media/" +stream[0]
    urla  = "http://www.netd.com/"
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer)
    tarzlistesi= []
    tarzlistesi.append(("part=1", ""+url.replace('</span> <b>','<OTV>')))
    tarzlistesi.append(("part=2", ""+url.replace('part=1-6','part=2-6')))
    tarzlistesi.append(("part=3", ""+url.replace('part=1-6','part=3-6')))
    tarzlistesi.append(("part=4", ""+url.replace('part=1-6','part=4-6')))
    tarzlistesi.append(("part=5", ""+url.replace('part=1-6','part=5-6')))
    tarzlistesi.append(("part=6", ""+url.replace('part=1-6','part=6-6')))
    for sTitle,sUrl in tarzlistesi:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'sshowBox3', sTitle, 'tv.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()


def play__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = sUrl+ '|User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    


def sshowBox3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    oInputParameterHandler = cInputParameterHandler()
    sUrl ='http://www.netd.com'+ oInputParameterHandler.getValue('siteUrl')
    sUrltit = oInputParameterHandler.getValue('sMovieTitle')
    ua='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'                                                                            
    urla= "http://www.netd.com/"
    referer=[('Referer',sUrl)]
    Server=gegetUrl(sUrl,headers=referer)          
    Server=Server.replace('/u002F', "")
    aResult= re.findall('"title":"'+sUrltit+'".*?"type":"applicationx-mpegURL","value":"(.*?)"', Server)
    for sTitle,url in aResult:
        sHosterUrl='http://media.netd.com.tr/' + url
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()  
        return False
