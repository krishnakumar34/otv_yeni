# -*- coding: UTF-8 -*-
from resources.sites.LIVETV2 import *


user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTS Build/LVY48F)"
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
params = dict(parse_qsl(sys.argv[2][1:]))
addon = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
napisy = xbmc.translatePath('special://temp/napisyMOVIES365.txt')
napisyLos = xbmc.translatePath('special://temp/napisyLosMovies.txt')
PATH            = addon.getAddonInfo('path')
DATAPATH        = xbmc.translatePath(addon.getAddonInfo('profile'))
RESOURCES       = PATH+'/resources/'
SITE_IDENTIFIER = 'movies365'
SITE_NAME = 'Movies365'
SITE_DESC = 'Replay TV'
from bs4 import BeautifulSoup
import chardet
from bs4 import UnicodeDammit
from resources.modules import client, jscrypto, pyaes_new as pyAES
import magic_aes
def movies365():
    oGui = cGui()
   

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/new')
    oGui.addDir(SITE_IDENTIFIER, 'Canlitvlive2', 'New', 'mov365.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/top')
    oGui.addDir(SITE_IDENTIFIER, 'Canlitvlive2', 'Popular', 'mov365.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/movies')
    oGui.addDir(SITE_IDENTIFIER, 'Canlitvlive2', 'Movies', 'mov365.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/serials')
    oGui.addDir(SITE_IDENTIFIER, 'Canlitvlive2', 'Serials', 'mov365.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/year/2021')
    oGui.addDir(SITE_IDENTIFIER, 'Canlitvlive2', '2021', 'mov365.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.365movies.tv/en/year/2020')
    oGui.addDir(SITE_IDENTIFIER, 'Canlitvlive2', '2020', 'mov365.png', oOutputParameterHandler)
  
    
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    oParser = cParser()
    Uurl = "http://www.365movies.tv/" 

    sHtmlContent =getHtml(Uurl)
    
#    sHtmlContent = BeautifulSoup(sHtmlContent, 'html.parser')
    oParser = cParser()
#    sHtmlContent = oParser.abParse(sHtmlContent, "id='menu_container'", '<!-- Global')
    logger.info("sHtmlContent : %s" % sHtmlContent) 
    sPattern = 'onclick=.*?href="(.*?)".*?><b>(.*?)</b>'
                
    #sHtmlContent = malfabekodla(sHtmlContent)
#    sHtmlContent = unescape(sHtmlContent)
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            from chardet import detect
            sTitle = aEntry[1]
            sTitle =sTitle.replace('中文','Chinese').replace('日本語','Nihongo- Japan').replace('한국어 (韓國語)','hangug-eo(Korean)')
            sPicture = 'mov365.png'
            
            import random

                      
            sUrl = str(aEntry[0])
            logger.info("sTitle : %s" % sTitle)                          
           # sTitle =sTitle.encode('utf-8', 'ignore')
            #sTitle =unescape(sTitle)  hangug-eo  Nihongo Chinese
            #sTitle = unicodedata.normalize('NFD', sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            
            oGui.addMovie(SITE_IDENTIFIER, 'Canlitvlive2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
  
    oGui.setEndOfDirectory()
def allanguages():	
	
		myMode = 'sort'	
		label=['All','Dansk','Deutsch','English','Español','Français','Italiano','Lietuvių','Magyar','Nederlands, Vlaams','Norsk','Polski','Svenska','Русский','Українська','עברית','中文 (Zhōngwén)','日本語','한국어 (韓國語)']
		value=['-','da','de','en','es','fr','it','lt','hu','nl','no','pl','sv','ru','uk','he','hi','zh','ja']
		msg = 'Language'
		sel = xbmcgui.Dialog().select(msg,label)
		if sel>-1:
		
			addon.setSetting(myMode+'V',value[sel])
			addon.setSetting(myMode+'N',label[sel])		
			xbmc.executebuiltin("Container.Refresh") 
		else:
			pass	

def unescape(string):
    string = urllib2.unquote(string)
    quoted = HTMLParser().unescape(string).encode('utf-8')
    #????
    return re.sub(r'%u([a-fA-F0-9]{4}|[a-fA-F0-9]{2})', lambda m: unichr(int(m.group(1), 16)), quoted)


def makeAscii(data):
    #log(repr(data), 5)
    #if sys.hexversion >= 0x02050000:
    #        return data

    try:
        return data.encode('ascii', "ignore")
    except:
        #log("Hit except on : " + repr(data))
        s = u""
        for i in data:
            try:
                i.encode("ascii", "ignore")
            except:
                #log("Can't convert character", 4)
                continue
            else:
                s += i

        #log(repr(s), 5)
        return s

def makeUTF8(data):
    #log(repr(data), 5)
    #return data
    try:
        return data.decode('utf8', 'xmlcharrefreplace') # was 'ignore'
    except:
        #log("Hit except on : " + repr(data))
        s = u""
        for i in data:
            try:
                i.decode("utf8", "xmlcharrefreplace") 
            except:
                #log("Can't convert character", 4)
                continue
            else:
                s += i
        #log(repr(s), 5)
        return s
UA= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'

def getRequests(url):
	headers = {
		'User-Agent': UA,
		'Accept': 'text/html, */*; q=0.01',
		'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
		'Referer': 'http://www.365movies.tv/en/home',
		'X-Requested-With': 'XMLHttpRequest',
		'Connection': 'keep-alive',
	}
	content=s.get(url,headers=headers,verify=False).content
	return content
   					
def getUrl(url, data=None, header={}, usecookies=True):
    if usecookies:
        cj = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent': UA}
    req = urllib2.Request(url,data,headers=header)
    try:
        response = urllib2.urlopen(req, timeout=15)
        link  =to_utf8(response.read())
        response.close()
    except:
        link=''
    return link
	
	
		
def Canlitvlive2():
    oGui = cGui()
   
    
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    oParser = cParser()
  

    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {"User-Agent": UA}
    req = urllib2.Request(Url, None, headers)
    try:
       response = urllib2.urlopen(req)
    except UrlError as e:
       print(e.read())
       print(e.reason)

    sHtmlContent = to_utf8(response.read())
    head = response.headers
    response.close()
   
   
    sHtmlContent =to_utf8(sHtmlContent)
    sPattern = "<div id='info_.*?<a href='(.*?)' target='_blank'><image title='(.*?)' style='.*?' src='(.*?)' /></a><h2>(.*?)</h2><font style='.*?'>(.*?)</font>"
                
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])

        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
            sUrl= sUrl.replace(' ','%20')
            sTitle = aEntry[3]+ '-'+  '[COLOR skyblue]' + aEntry[4]+'[/COLOR]'
            sTitle =sTitle.replace('中文','Chinese').replace('日本語','Nihongo- Japan').replace('한국어 (韓國語)','hangug-eo(Korean)')

            sPicture = aEntry[2]
            tle = aEntry[1]
            tle =tle.replace('IMDb',' IMDb').replace('中文','Chinese').replace('日本語','Nihongo- Japan').replace('한국어 (韓國語)','hangug-eo(Korean)')
                                                       
            sTitle = malfabekodla(sTitle)
            sTitle =sTitle.replace('Ä±','ı').replace('Ã','Ç').replace('Ã¼','ü').replace('Å','ş').replace('Ã§','ç').replace('Ã¶','ö')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'streams', sTitle, sPicture, sPicture, tle, oOutputParameterHandler)
        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'Canlitvlive2', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
 
         

def __checkForNextPage(sHtmlContent):
    sPattern = "<div class='page-item-selected'>.*?</div><div class='page-item' onclick='javascript:location.href=\"(.*?)\"'>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl
    return False	

        
def _decode_char(c):
    array1 = ["0", "1", "2", "3", "4", "5", "6", "7", "9", "H", "M", "D", "X", "V", "J", "Q", "U", "G", "E", "T", "N", "o", "v", "y", "w", "k"]
    array2 = ["c", "I", "W", "m", "8", "L", "l", "g", "R", "B", "a", "u", "s", "p", "z", "Z", "e", "d", "=", "x", "Y", "t", "n", "f", "b", "i"]
    for i in range(0,len(array1)):
        if c == array1[i]: return array2[i][0]
        if c == array2[i]: return array1[i][0]
    return c
def decode_hls(file_url):
    def K12K(a, typ='b'):
        codec_a = ["p", "9", "U", "1", "b", "s", "y", "Z", "I", "H", "f", "8", "Y", "W", "g", "5", "G", "i", "J", "2", "T", "e", "k", "d", "7", "="]
        codec_b = ["0", "B", "w", "t", "x", "m", "c", "z", "u", "n", "M", "Q", "R", "6", "v", "V", "l", "N", "D", "3", "L", "X", "a", "4", "o", "A"]
        if 'd' == typ:
            tmp = codec_a
            codec_a = codec_b
            codec_b = tmp
        idx = 0
        while idx < len(codec_a):
            a = a.replace(codec_a[idx], "___")
            a = a.replace(codec_b[idx], codec_a[idx])
            a = a.replace("___", codec_b[idx])
            idx += 1
        return a
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


def getStreams():
    try:
        from resources.modules import cache

        past = '4fa52accfc2aee902c4de5210b64dc274bab148a377f5a1994cbc141829b8d0e28728efa6bd7fc6f1e503fe0569e8c218b0ea7fd41c629278a35d8085c78d9a8184bece7cfba75d05d51b69c37532982'.encode('utf-8')
        ret = xor2(past, 'sly6B89wqxt2N')
        logger.info("pastes : %s" %ret)
        ret = json.dumps(ret)
        ret = json.loads(ret)
        VSlog('HTMLSTREAMS-OUT: %s' % str(ret))
        info, key = ret['i7'], ret['k7']
    except BaseException:
        raise Exception()

def streams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    url= url.replace(' ','%20')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumbnail')
    logger.info("answ : %s" % url) 
    link =  getHtml(url)
    #link= link.replace('\\','')
    Url =re.findall("<noindex><a href='(.*?)'",link,re.DOTALL)[0]
    data =getHtml(Url)
    answ = re.search('<iframe.+?src="(.+?)"', data).group(1)
    
    body= requests.get(answ,  headers={'Referer': 'http://www.365movies.stream/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'Host': 'klas54edr1.ee74ad613570198.pw',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'}).text
    bod =to_utf8(body)     
    logger.info("key : %s" %  bod  ) 
    s = re.search('<input type="hidden" name="s" value="(.*?)">', bod).group(1)
    r= re.search('<input type="hidden" name="r" value="(.*?)">', bod).group(1)
    d= re.search('<input type="hidden" name="d" value="(.*?)"', bod).group(1)
    f= re.search('<input type="hidden" name="f" value="(.*?)"', bod).group(1)
                          
            
    token = "http://h6.adshell.net/peer5" 
            #token  = token+"&ul=de-de&de=UTF-8&dt=yabancidizi.org%20|%20yabanc%C4%B1%20dizi%20izle,%20yabanc%C4%B1%20film%20izle&sd=24-bit&sr=1536x864&vp=1163x750&je=0&ec=general&ea=HeartBeat&_u=CACAAUABAAAAAC~&jid=1778031460&gjid=1363167938&cid=484785676.1614953100&tid=UA-187930534-1&_gid=1363860594.1616864270&_r=1&gtm=2ou3h0&z=1324323876" 
    
           
                                
    post_data = {'s': s,'r': r,'d':d,'f':f}
    logger.info("ost_data : %s" %post_data ) 
    s = requests.Session()
    r = s.post(token, headers={'Host':'h6.adshell.net',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://klas54edr1.ee74ad613570198.pw/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept-Encoding': 'gzip'}, data=post_data)
    auth = to_utf8(r.text)                         
    kkey = 'NGZhNTJhY2NmYzJhZWU5MDJjNGRlNTIxMGI2NGRjMjc0YmFiMTQ4YTM3N2Y1YTE5OTRjYmMxNDE4MjliOGQwZTI4NzI4ZWZhNmJkN2ZjNmYxZTUwM2ZlMDU2OWU4YzIxOGIwZWE3ZmQ0MWM2MjkyNzhhMzVkODA4NWM3OGQ5YTgxODRiZWNlN2NmYmE3NWQwNWQ1MWI2OWMzNzUzMjk4Mg=='

    link = re.compile('\([\'"][^"\']+[\'"], [\'"][^"\']+[\'"], [\'"]([^"\']+)[\'"], 1\)').findall(auth)
    logger.info(" %s" %link[0])
    link =base64.b64decode(link[0])
    link = str(link).replace("b'",'').replace("'",'')
    link = json.dumps(link)
    logger.info("auth : %s" %link)
    #link = makeUTF8(link)
    enc_data = json.loads(link)
    
   # enc_data = makeAscii(enc_data)
    logger.info("enc_data : %s" %enc_data)
    #ciphertext =  base64.b64decode(enc_data)
    #logger.info("ciphertext : %s" %ciphertext)
    src = magic_aes.decrypt(kkey,link[0])
    src = src.replace('"','').replace('\\','').encode('utf-8')
    logger.info("auth : %s" %src)# -*- coding: utf-8 -*-
 
   # time.sleep(5)    
#    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,data,'')   
def xor_crypt_string(data, key, encode = False, decode = False):
    from itertools import  cycle
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(x ^ y) for (x,y) in zip(data, cycle(key)))
    if encode:
        # return base64.encodestring(xored).strip()
        return base64.encodestring(xored.encode('utf-8')).decode('utf-8').replace('\n', '').strip()
    return xored
def xor2(data, key):
    from itertools import  cycle
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    return xored
