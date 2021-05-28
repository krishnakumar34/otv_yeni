#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *   
SITE_IDENTIFIER = 'fox_com_tr'
SITE_NAME = 'FOXTV_com_tr'
SITE_DESC = 'télévision'
MOVIE_HD = (True, 'showGenre')
URL_MAIN = 'https://www.fox.com.tr'
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        


useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
class track():
    def __init__(self,page,data=''):
        self.page=page
        self.page =0
        self.page += 1
        self.data=data

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    if PY3:    
        data = base64.b64decode(data)
        data = to_utf8(data)
        return data
    else:    
        return base64.decodestring(data)
def yaz64(data):
        data = base64.b64decode(data)
        data = to_utf8(data)
        return data
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
user_file = os.path.join(RESOURCES_DIR, 'iptvchannels.json')
try:
    with io.open(user_file, 'r', encoding='utf-8') as f:
        user = f.read()
except IOError:
    user = ''
user_filem = os.path.join(RESOURCES_DIR, 'iptvchannels2.json')
try:
    with io.open(user_filem, 'r', encoding='utf-8') as f:
        user2 = f.read()
except IOError:
    user2 = ''

def orhatvturk():
    oGui = cGui()
                     

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('kanald_com_tr', 'turkTV', 'Türk TV', 'diziler.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '28')
    oGui.addDir('Swift', 'list_channels', 'Türk IPTV', 'turkey-free-iptv.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.sporizle1.pw')
    oGui.addDir(SITE_IDENTIFIER, 'tviptv', 'Türk IPTV 2', 'turkey-free-iptv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.sporizle1.pw')
    oGui.addDir(SITE_IDENTIFIER, 'rakiptv', 'Türk IPTV 3', 'turkey-free-iptv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'rmootatam', 'Türk VE AZ TV HD', 'turkazeri.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('diziizle_net', 'turkdizi', 'Türk  Dizi', 'diziler.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir('turkvod_org', 'TUrKVod', 'Türk Sinema', 'turksiemalar.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('canlifm_com', 'Radyo', 'Türk Radyo', 'trradyo.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def tviptv():
    oGui = cGui()
#    logger.info("user2 :" +user2) 
    sPattern = '<favourite name="(.*?)" thumb="(.*?)".*?unction=(.*?)&sMovieTitle=.*?&site=(.*?)&siteUrl=(.*?)&'
    oParser = cParser()
    aResult = oParser.parse(user2 , sPattern)                                                                  
    if not aResult[0] == False:
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            sTitle = aEntry[0]
            sPicture = aEntry[1]
            sUrl = str(aEntry[4])
            sitem = aEntry[3]
            site = aEntry[2]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('Url', site)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            if sTitle =='TR-LIVE CHANNELS':
               hurl='http://ostv.site:8080/panel_api.php?username=zero&password=zero&type=m3u'
               stream='ts'
               oOutputParameterHandler.addParameter('sitem', hurl)
               oOutputParameterHandler.addParameter('stream', stream)
               oGui.addMovie(sitem, site, sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
            
               oGui.addMovie(sitem, site, sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        
    oGui.setEndOfDirectory()    
                  
def rakiptv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = 'https://www.sporizle1.pw'
    sHtmlContent = getHtml(Url)
    sHtmlContent=sHtmlContent.replace("xxx",'').replace("XXX",'').replace("ADULT",'Çalışmiyor').replace("11084",'')
    sPattern = '<a href="/live/.+?/(.*?)" title=".*?" class="list-group-item"> <div class="row"> <div class="col-xs-4 col-sm-2 col-md-4"> <img src="(.*?)" alt=".*?"> </div> <div class="col-xs-20 col-sm-22 col-md-20"> <div class="sidenavChannel"><strong style="color:red">.+?</strong> - (.+?)</div> <div class="sidenavShortdesc">.+?</div>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = aEntry[2]
            sPicture = 'https://www.sporizle1.pw'+aEntry[1]
            sUrl = str(aEntry[0])
            
            sTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'rakip23', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'



                


def rakip23():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        sUrl = 'https://www.sporizle1.pw/live/turkish/' + Url 
        sThumbnail = oInputParameterHandler.getValue('sThumbnail')
        name = oInputParameterHandler.getValue('sMovieTitle')
        Urluu = 'https://www.sporizle1.pw/embed/' + Url + '?web'
        cf = getHtml(Urluu)
        ata= re.search('data-i="(.+?)"', cf).group(1)        
        url1 = 'https://www.sporizle1.pw/cdn/js/ads.php?'+ata+'&www.sporizle1.pw' 
        Cookie =fullcookie(url1)
        
        headers1 = {'user-agent':UA,
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Content-Type':'text/javascript charset=utf-8',
               'Referer':'https://www.sporizle1.pw/',
               'Cookie': Cookie 
                }

        
       
        req = s.get(url1, headers=headers1)
        data = req.text
        logger.info("Cookie : %s" % Cookie)
        sec= re.search('sec:"(.+?)"', data).group(1) 
        
        
        post_data = {"e": captoken(),"sec": sec,"id": ata}
        r = s.post(Urluu , headers={"Referer": sUrl,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": UA,"Connection": "Keep-Alive","x-requested-with": "XMLHttpRequest"}, data=post_data, timeout=10)
        suby = r.text                                                                                                   

        suby =to_utf8(suby)                                                                                          
        sub =suby[::-1]+'=='               
        m3u8=yaz64(sub)
        m3u8=m3u8.replace('c3.xcxc.cf','c6.xcxc.cf').replace('cl.izletv.xyz','c6.xcxc.cf').replace('https:///web','https://c6.xcxc.cf/web').replace('https://c6.xcxc.cf/web/1/www.sporizle1.pw//','https://c6.xcxc.cf/web/1/www.sporizle1.pw/')
        logger.info("m3u8 : %s" % m3u8)
        ref ='|한국어=éåèª\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e/&Access-Control-Allow-Origin=https://www.sporizle1.pw&Referer=https://www.sporizle1.pw/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,m3u8+ref,'')           

#                                          
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

def deCFEmail(fp):                                                                                          
        try:
            r = int(fp[:2],16)
            email = ''.join([chr(int(fp[i:i+2], 16) ^ r) for i in range(2, len(fp), 2)])
            return email
        except (ValueError):
            pass
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'   
def captoken():
    site_key = "6LeII50UAAAAAA5jiKIwKnJ_iDc9uVuc7qzYi8-_"
    co = "aHR0cHM6Ly93d3cuc3Bvcml6bGUxLnB3OjQ0Mw.."
    sa = ''
    cb = 's5kxgdpbca0j'
    headers1 = {'user-agent':UA,
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
               'Referer':'https://www.sporizle1.pw/'
                }

    url1 = 'https://www.google.com/recaptcha/api.js'
    s = requests.session()
    req = s.get(url1, headers=headers1)
    data = req.text

    aresult = re.findall("releases\/(.*?)\/", data)
    if aresult:
        v = aresult[0]
    else:
        return False, False

#hash=jB00ch8EbFUZZ1%2Bl2ElRRsRs1WokrapBkT5ugVg7bCsX7nrrlrXX2GA%2BP%2BHm04O%2FVKVmiBrgpUHnST6XKRp1Dw%3D%3D&e=03AGdBq25CZ2R0y_iWyw0Ujrw0h8kLVi0yA61FqZ4NU8GmNMwGAHg9sLvbgHPhWT2WroRkb0WPsx6JYwqibwc6MZgfkD5P_ryWQveBGRJ4a86aufn17H58LcnwCDdSTuXtezNcelNICIucthehRrxEaWA0Kl1GRhOHQ5o3teYcnoWfM8x_1sVPMMh76jadEuuDl5aawWvHwzskfm4j87ljn9PpXGa4XyIRh0YvirI94oaI7wzeAjIXe8XSh9hqOM7GuNAo9iPHcweF1mVbus9LMA-JhTrjq7fHTvNqpYeLt69OsFgQ15uxAyeSRcFU9fqc69uzOWZPcOl_O6cA1jxP-cQJXvR37WHydh1ehZwV60P610JAEG78c_bshQh5CJ9he7tX0yYQLZW-g_21CpK8_c47aCHIgU5BKvDtQvlUkXU1WybBijs8Ks4DBO0Q-iwq7TxaWdt1ImA8&id=10723
#https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeII50UAAAAAA5jiKIwKnJ_iDc9uVuc7qzYi8-_&co=aHR0cHM6Ly93d3cuMjRkZXR2LmRlOjQ0Mw..&hl=de&v=f-bnnOuahiYKuei7dmAd3kgv&size=invisible&cb=s5kxgdpbca0j
    url2 = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=" + site_key + "&co=" + co + "&hl=ro&v=" + v + "&size=invisible&cb=" + cb
    logger.info("body : %s" % url2)
    req = s.get(url2)
    data = req.text
    data = data.replace('\x22', '')
    aresult = re.findall("recaptcha-token.*?=(.*?)>", data)
    
    if aresult:
        c = aresult[0]
    else:
        return False, False

    url3 = "https://www.google.com/recaptcha/api2/reload?k=" + site_key
    post_data = {'v':v, 'reason':'q', 'k':site_key, 'c':c, 'sa':sa, 'co':co}

    headers2 = {'user-agent':UA,
               'Accept':'*/*',
               'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
               'Referer':url2
                }

    req_url3 = s.post(url3, data=post_data, headers=headers2)
    data = req_url3.text
    aresult = re.findall("resp\",\"(.*?)\"", data)
    if aresult:
        token  = aresult[0]
        return  token
    return False, False




def mplay__():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl=sUrl+'|Referer=http://apim.livetv.az/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'

    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + sTitle,sUrl,  '')


        
ulkeLists = 'http://85.132.71.12/channels'
def rmootatam():
    oGui = cGui()
    sJson = cRequestHandler(ulkeLists).request()
    aJson = json.loads(sJson)
    for cat in aJson:
        sPic = cat['logo_file_name']
        sPicture = 'http://apim.livetv.az/images/medium/' + sPic
        catid = cat['stream']
        if  'http' in catid:
            sTitle = cat['name']
            catid = cat['stream']
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('siteUrl', catid)
            oGui.addMovie(SITE_IDENTIFIER, 'mplay__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        sTitle = cat['name']
        sTitle ='stream-2-'+ sTitle
        cati= cat['streams2']
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', cati)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
        oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory()

      
def sEcho2(s):
    if 'movies/0' in s:
         s=s.replace('movies/0','movies/1')
         return s 
    
    if 'movies/1' in s:
         s=s.replace('movies/1','movies/2')
         return s 
    if 'movies/2' in s:
         s=s.replace('movies/2','movies/3')
         return s 
    if 'movies/3' in s:	
         s=s.replace('movies/3','movies/4')
         return s 
    if 'movies/4' in s:	
         s=s.replace('movies/4','movies/5')
         return s 
    if 'movies/5' in s:	
         s=s.replace('movies/5','movies/6')
         return s 
    if 'movies/6' in s:	
         s=s.replace('movies/6','movies/7')
         return s 
    if 'movies/7' in s:	
         s=s.replace('movies/7','movies/8')
         return s 
    if 'movies/8' in s:	
         s=s.replace('movies/8','movies/9')
         return s 
    if 'movies/9' in s:	
         s=s.replace('movies/9','movies/10')
         return s 
    if 'movies/10' in s:	
        s=s.replace('movies/10','movies/11')
        return s 
    if 'movies/11' in s:	
        s=s.replace('movies/11','movies/12')
        return s 
    if 'movies/12' in s:	
        s=s.replace('movies/12','movies/13')
        return s 
    if 'movies/13' in s:	
        s=s.replace('movies/13','movies/14')
        return s 
    if 'movies/14' in s:	
        s=s.replace('movies/14','movies/15')
        return s 
    if 'movies/15' in s:	
        s=s.replace('movies/15','movies/16')
        return s 
    if 'movies/16' in s:	
        s=s.replace('movies/16','movies/17')
        return s
    if 'movies/17' in s:	
        s=s.replace('movies/17','movies/18')
        return s 
    if 'movies/18' in s:	
        s=s.replace('movies/18','movies/19')
        return s 
    if 'movies/19' in s:	
        s=s.replace('movies/19','movies/20')
        return s 
    if 'movies/20' in s:	
        s=s.replace('movies/20','movies/21')
        return s 
    
def sEcho(s):
    if 'series/0' in s:
         s=s.replace('series/0','series/1')
         return s 
    
    if 'series/1' in s:
         s=s.replace('series/1','series/2')
         return s 
    if 'series/2' in s:
         s=s.replace('series/2','series/3')
         return s 
    if 'series/3' in s:	
         s=s.replace('series/3','series/4')
         return s 
    if 'series/4' in s:	
         s=s.replace('series/4','series/5')
         return s 
    if 'series/5' in s:	
         s=s.replace('series/5','series/6')
         return s 
    if 'series/6' in s:	
         s=s.replace('series/6','series/7')
         return s 
    if 'series/7' in s:	
         s=s.replace('series/7','series/8')
         return s 
    if 'series/8' in s:	
         s=s.replace('series/8','series/9')
         return s 
    if 'series/9' in s:	
         s=s.replace('series/9','series/10')
         return s 
    if 'series/10' in s:	
        s=s.replace('series/10','series/11')
        return s 
    if 'series/11' in s:	
        s=s.replace('series/11','series/12')
        return s 
    if 'series/12' in s:	
        s=s.replace('series/12','series/13')
        return s 
    if 'series/13' in s:	
        s=s.replace('series/13','series/14')
        return s 
    if 'series/14' in s:	
        s=s.replace('series/14','series/15')
        return s 
    if 'series/15' in s:	
        s=s.replace('series/15','series/16')
        return s 
    if 'series/16' in s:	
        s=s.replace('series/16','series/17')
        return s
    if 'series/17' in s:	
        s=s.replace('series/17','series/18')
        return s 
    if 'series/18' in s:	
        s=s.replace('series/18','series/19')
        return s 
    if 'series/19' in s:	
        s=s.replace('series/19','series/20')
        return s 
    if 'series/20' in s:	
        s=s.replace('series/20','series/21')
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
      
          
def foxcomtr():
    oGui = cGui()
    liste = []
    liste.append( ['FOX_TV CANLI YAYIN','https://www.fox.com.tr/canli-yayin'] ) 
    liste.append( ['FOX_TV Yedek','https://www.canlitv.me/fox-canli-izle'] ) 
    liste.append( ['DİZİLER','https://www.foxplay.com.tr/ajax/series/0/20/date'] )
#    liste.append( ['FILMLER','https://www.foxplay.com.tr/ajax/movies/1/20/date'] )

    for sTitle,sUrl2 in liste:
                                
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'FILMLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showdizim', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER Arsiv':
             oGui.addDir(SITE_IDENTIFIER, 'showdizim', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'FOX_TV Yedek':
             oGui.addDir('xCanLiTVlive', 'sshowBox19', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'sshowBox3',  sTitle, 'genres.png', oOutputParameterHandler)
                  
                    
    oGui.setEndOfDirectory()

def showSinema():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
                                                                                     

    sHtmlContent =getHtml(Url) 
                                                                     
                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<div class="foxplay--grid-view-item">.*?<a href="(.+?)">.*?<img data-src="(.+?)".+?<span>(.+?)</span>'

                                                                                                     
    sHtmlContent = sHtmlContent
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[2]
            sPicture =aEntry[1]
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
                                                                    

            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle =malfabekodla(sTitle)        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'showtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
           
        
        sNextPage =sEcho2(str(Url))
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showdizim', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
        
        
           
        
             
  
    oGui.setEndOfDirectory()
def showdizim():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
                                                                                     

    sHtmlContent =getHtml(Url) 
                                                                     
                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<div class="foxplay--grid-view-item">.*?<a href="(.+?)">.*?<img data-src="(.+?)".+?<span>(.+?)</span>'

                                                                                                     
    sHtmlContent = sHtmlContent
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[2]
            sPicture =aEntry[1]
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            sUrl=sUrl.replace('/detaylar','/bolumler').replace('/izle','/bolumler')                                                          

            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle =malfabekodla(sTitle)        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'dataseason', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
           
        
        sNextPage =sEcho(str(Url))
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showdizim', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
        
        
           
        
             
  
    oGui.setEndOfDirectory()


def dataseason():
    oGui = cGui()
   

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    logger.info("Good sUrl :" +sUrl)        
    sHtmlContent =getHtml(sUrl) 
                     
                                                                                                                                                                                  
    sPattern = '<a class=".+?jax-video-loader" data-program-id="(.+?)" data-type="(.+?)" data-season="(.+?)" data-page="(.+?)" data-count="(.+?)" href="#">(.+?)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)                                                  
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
       
        for aEntry in aResult[1]:
            
            sTitle= aEntry[5]
            count = str(aEntry[4])
            page = str(aEntry[3])
            season = str(aEntry[2])
            datype = str(aEntry[1])    
            proid = str(aEntry[0])
                    
                  # https://www.foxplay.com.tr/ajax/videos/1167/2/1/0/10
            sUrl ='https://www.foxplay.com.tr/ajax/videos/%s/%s/%s/%s/40'%(proid ,datype,season,page)
            sTitle =malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addDir(SITE_IDENTIFIER, 'showdizi2',  sTitle, 'genres.png', oOutputParameterHandler)
             
 
  
    oGui.setEndOfDirectory()



def showdizi2():
    oGui = cGui()
   

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
           
    sHtmlContent =getHtml(sUrl) 
                     
                                                                                                                                                                                    
    sPattern = ' <div class="foxplay--grid-view-item">.*?<a href="(.+?)">.*?<img data-src="(.+?)".+?<i>(.+?)</i>'
    
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
                oGui.addMovie(SITE_IDENTIFIER, 'showtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        sNextPage = __ccheckForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showdizi', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
  
    oGui.setEndOfDirectory()

def __ccheckForNextPage(sHtmlContent):
    url = re.findall('<a class="more-button" rel="(.*?)" href="#" data-page="(.*?)">',sHtmlContent, re.S)
    for  aEn ,trye  in url:
        URL = 'https://www.fox.com.tr'+aEn+'&page='+trye
        return str(URL)
    return False   
                                                                                            


 
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


def play__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oGuiElement.setThumbnail(sThumbnail)

    #cConfig().log("Hoster - play " + str(sTitle))
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    #tout repetter
    #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
    
    oPlayer.startPlayer()
    return
        
    oGui.setEndOfDirectory()

def sshowBox20():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
  
    import uuid
     
    
    # 1 seul resultat et sur leur propre hebergeur
    
        
        
            
    rest= 'http://mn-i.mncdn.com/foxtv_iphone/smil:foxtv_iphone.smil/playlist.m3u8?token=' + uuid.uuid4()
                                    
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    sHosterUrl= rest + '|' + Header  
    
                           
                  



    

   

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
def Auth():
    url  = "https://www.fox.com.tr/canli-yayin"                   
    data=getHtml(url) 
    data = str(data).replace("' + '","").replace("'+'","") 
    sHosterUrl = re.findall("videoSrc : mobilechec.*?'.*?st=(.*?)'", data, re.S)[0]
    return sHosterUrl        
 
def sshowBox3():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
   
    
    
    url  = "https://www.fox.com.tr/canli-yayin"                   
    data=getHtml(url) 
    data = str(data).replace("' + '","").replace("'+'","") 
    rUrl = re.findall("videoSrc : mobilechec.*?'.*?st=(.*?)'", data, re.S)[0]
    logger.info("Good ata :" +rUrl)
    rUrl = rUrl.replace("\\","")
    url = 'https://foxtv-live-ad.ercdn.net/foxtv/playlist.m3u8?st='+ rUrl
    Header = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    #+ '|' + Header                          
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def playnext(url):
    urla  = "http://www.fox.com.tr/"          
                       
    referer=[('Referer',urla)]
    data=gegetUrl(url,headers=referer) 
    data = data.replace("' + '","").replace("'+'","") 
    sHosterUrl = re.findall("desktopUrl = '(.*?)'", data, re.S)[0]
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    sHosterUrl= sHosterUrl + '|' + Header            
    return sHosterUrl   


def addLink(name,url,pic):
        ok=True
        liz = xbmcgui.ListItem(name)
        liz.setArt({'thumb': pic, 'icon': pic, 'fanart': pic})
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok 


def foxparca():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sHtmlContent=requests.get(url,headers={'User-Agent':ua,'Referer':'http://www.showtv.com.tr/','Accept':'/*','Connection':'keep-alive'}).text
    sHtmlContent = sHtmlContent.replace("\/",'/').replace("\u0130",'I')          
    urll='http://www.showtv.com.tr'+re.findall('<li class="selected"><a href="(.*?)">',sHtmlContent)[0]
    
   
      

   
    
   
   
    sUrl =playnext(urll.replace("/part/1",'/part/1'))
    sUrl1 =playnext(urll.replace("/part/1",'/part/2'))
    sUrl2 =playnext(urll.replace("/part/2",'/part/3'))
    sUrl3 =playnext(urll.replace("/part/3",'/part/4'))
    sUrl4 =playnext(urll.replace("/part/4",'/part/5'))
    sUrl5 =playnext(urll.replace("/part/5",'/part/6'))
    sUrl6 =playnext(urll.replace("/part/6",'/part/7'))
   
    
    playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
    
    playlist.clear();
    listitem1 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl,listitem1);
    listitem2 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl1,listitem2);
    listitem3 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl2,listitem3);
    listitem4 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl3,listitem4);
    listitem5 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl4,listitem5);                                                                         
    listitem6 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl5,listitem6);
    listitem7 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl6,listitem7);                                                                         
    listitem8 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl7,listitem8);
    player_type = sPlayerType()
    xbmcPlayer = xbmc.Player (player_type); 
    xbmcPlayer.play (playlist)    

def int_to_str( n, b, symbols='0123456789abcdefghijklmnopqrstuvwxyz'):
		return (int_to_str(n/b, b, symbols) if n >= b else "") + symbols[n%b]

def make_hash( s):
		return ''.join((int_to_str(int(s[lb:lb + 8], 16), 36) for lb in range(0, 32, 8)))   

def showtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
   
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer)                         
    data= data.replace("\/",'/').replace("&quot;",'"').replace('var videoUrl = "','ht_stream_m3u8":"')    
       
    sUrll  = re.findall("videoSrc : '(.*?)'", data, re.S)[0]
    #cookie =SetCookie(sUrll)
    #logger.info("cookie:" +cookie) 
    Header = '&Referer=https://www.foxplay.com.tr/&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= sUrll+ '|Cookie=FoxLightboxV00921025=true; _ym_uid=16160666723565406; _ym_d=1620636209; _ga=GA1.3.1146736301.1620636209; _gid=GA1.3.1852494557.1620636209; __gfp_64b=.3fL4ET5a0pIy6hpdhxZ_KUASwCQlzLClpx.zQ8RkqH.f7|1615066190; _ym_isad=2; _ym_visorc=w; __gads=ID=072a207f78c40d34:T=1620636209:S=ALNI_MYarpQqTZKAlLs7rSYeqY2aGqqdqA; NSC_gpyqmbz.dpn.us_zfoj=ffffffffc3a01e1a45525d5f4f58455e445a4a423660; _gat_gtag_UA_131766576_1=1; _gat=1; ins-storage-version=36; XSRF-TOKEN=eyJpdiI6IlhrWUg1eXd1bHY1TTdmRFZDY0tTRVE9PSIsInZhbHVlIjoib1wvZjFVVzJyNWRITjU3SGh3dWxCMGFxVmptODJMRzVzU2VpUGtxb2FlNjdTVTJCSGo5dU1rYlJ3XC9idkhUTjRLIiwibWFjIjoiNjBjZThiN2M4OTIxY2E1Njk4NjI5NmRiOTAyYTUwM2U0MWY0ZTg4N2I2YjQ5NjlmNjNmOTMwMGY2MmQ1NDNhNyJ9; foxplay_session=eyJpdiI6ImJCUUpCSkYzT0c3dWh2ZEc1ZDcxYVE9PSIsInZhbHVlIjoiek5HanBLZnBMSlwvcDJ3QTVzeUpwNjB0UFc4UFpSRUxXRXFsWEhOdThVUHBXQlc4eW1KRFNJd1pWMUttSFljakUiLCJtYWMiOiJmN2RiNmI5N2Q2ODE2MmU3ZDY2YjM1NzlmODM4YWI0MDY5YjBhNmViZDIwZTExMmZmYmQ1MWRjZTQ2Y2VlYzFkIn0=' + Header 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'') 