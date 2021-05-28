#	-*-	coding:	utf-8	-*-
import urllib2, urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64

import re,xbmcgui,unicodedata

import re

UPDATE = False  
def okuoku(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku 
from resources.lib.config import cConfig
from binascii import b2a_hex

from resources.lib.player import cPlayer
import string
import random
from resources.lib.util import cUtil

def id_generator(size=32, chars=string.digits + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))
def gget_post_data():
    _key = b"cLt3Gp39O3yvW7Gw"
    _iv = b"bRRhl2H2j7yXmuk4"
    cipher = AES.new(_key, AES.MODE_CBC, iv=_iv)
    _time = str(int(time.time()))
    _hash = md5("23".format().encode("utf-8")).hexdigest()
    _plain = "{0}&{1}".format(_time, _hash).ljust(48).encode("utf-8")
    cry = cipher.encrypt(_plain)
    return b2a_hex(cry).decode("utf-8")

def kget_post_data():
    _key = 'cLt3Gp39O3yvW7Gw'
    _iv = 'bRRhl2H2j7yXmuk4'
                
#1561570680     
    cipher = AES.new(_key, AES.MODE_CBC, iv=_iv)
    _time = str(int(time.time()))
#    h2=md5("66726563636D30746E70716D6F6C6468".format().encode("utf-8")).hexdigest() 
    _plain = "1561570680&fc2f07372982634c95b93371e44ef76c".format().ljust(48).encode("utf-8")
    cry = cipher.encrypt(_plain)
    return b2a_hex(cry).decode("utf-8")

stopEvent=None
g_stopEvent=None
g_downloader=None
g_currentprocessor=None
proxy=None
use_proxy_for_chunks=False
maxbitrate=0
simpleDownloader=False 
auth=None 
streamtype='HLSRETRY'
setResolved=False
swf=None  
callbackpath=""
callbackparam="" 
iconImage="DefaultVideo.png"
setDisplayName = []
SITE_IDENTIFIER = 'filmakinesi_org'
AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path')
res_lib = os.path.join(addonDir, 'resources', 'lib')
f4mProxy = os.path.join(addonDir, 'f4mProxy')        
player_agent = None
def CheckCpacker(str):
    oParser = cParser()
    sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>'
    aResult = oParser.parse(str, sPattern)
    if (aResult[0]):
        
        str2 = aResult[1][0]
        if not str2.endswith(';'):
            str2 = str2 + ';'
            
        return cPacker().unpack(str2)

    return str
def getCookiesString(cookieJar):
    try:
        cookieString=""
        for index, cookie in enumerate(cookieJar):
            cookieString+=cookie.name + "=" + cookie.value +";"
    except: pass
    #print 'cookieString',cookieString
    return cookieString
REMOTE_DBG = False
# append pydev remote debugger
if REMOTE_DBG:
	# Make pydev debugger works for auto reload.
	# Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
	try:
		import pysrc.pydevd as pydevd  # with the addon script.module.pydevd, only use `import pydevd`
	# stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
		#pydevd.settrace('localhost', stdoutToServer=True, stderrToServer=True, suspend=False)
		pydevd.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
	except ImportError:
		sys.stderr.write("Error: You must add org.python.pydev.debug.pysrc to your PYTHONPATH.")
		sys.exit(1)
def aes_encrypt(result):
            result = binascii.a2b_hex(result)
            from resources.lib import pyaes
            counter = pyaes.Counter(initial_value = 100)
            aes = pyaes.AESModeOfOperationCTR(control.key)
            result = aes.encrypt(result)
            return result


def player_type():
        oConfig = cConfig()
        sPlayerType = oConfig.getSetting('playerType')
        
        try:
            if (sPlayerType == '0'):
                cConfig().log("playertype from config: auto")
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                cConfig().log("playertype from config: mplayer")
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                cConfig().log("playertype from config: dvdplayer")
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False
def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)

def canlitvzoneBox():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
  
                       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'https://www.canlitv.zone/' , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    dat = requests.get(Url, headers = headers).text

   

   
    urlk = re.findall('<iframe width="100%" height="100%"  src="(.*?)"', dat, re.S) 
             
    sUrl = 'https://www.canlitv.zone/'+urlk[0] 
     
      

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': Url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    source = requests.get(sUrl, headers = headers).text
    
    rUrl = re.findall("file: '(.*?)'",source, re.S)[0]
    sPicture ="https://www.canlitv.zone/logo/tivibu-spor_9147556.png"
    Header = '|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    sHosterUrl= rUrl + Header
     
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
    return False


def GetEncodeString(string):
    try:
        import chardet
        string = string.decode(chardet.detect(string)["encoding"]).encode("utf-8")
    except:
        pass
    return string

def TurkishTV ( s ) :
 kem = [ s [ HEM : HEM + 3 ] for HEM in range ( 0 , len ( s ) , 3 ) ]
 return '' . join ( chr ( int ( val ) ) for val in kem )
def getCookieJar():
    cookieJar=None
    try:
        cookieJar = cookielib.LWPCookieJar()
        cookieJar.load(COOKIEFILE,ignore_discard=True)
    except: 
        cookieJar=None

    if not cookieJar:
        cookieJar = cookielib.LWPCookieJar()

    return cookieJar       
def playOTV2(sUrl,sTitle,iconimage):
    name =  alfabekodla(sTitle)
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    Player().play(sUrl,liz)
           

def playOTV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
#    sUrl = sUrl+"|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    iconimage= oInputParameterHandler.getValue('sThumbnail')
    name =  alfabekodla(sTitle)
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    Player().play(sUrl,liz)

            
def mediaHeaders(chann):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13' ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann            
         
       			

def ozel():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    tarzlistesi= []                 
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
       
    stream = re.findall('<!--baslik:.*?--><.*?src=[\'|"](.*?)[\'|"]', data, re.S)
    Url = str(stream[0])
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    

        #cookie = getUrl(url, output='cookie').result
    tarzlistesi = re.findall('"file":"(.*?)".*?"label":"(.*?)"', data, re.S)
    for sUrl,sTitle in tarzlistesi:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()   
def showBoxxx():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    track = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    
    
        
    sHosterUrl = track

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
def showotvplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    url =url
    StreamType='HLS'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
         
def showhlsetryplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    TIK='User-Agent=User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    url =url
    StreamType='HLSRETRY'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
    
def showotsplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    url =url
    StreamType='TSDOWNLOADER'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
def laklak(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku      
def showHDSplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    url =url
    StreamType='HDS'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
    



            
        
       
def sPlayerType():
        oConfig = cConfig()
        sPlayerType = oConfig.getSetting('playerType')
        
        try:
            if (sPlayerType == '0'):
                cConfig().log("playertype from config: auto")
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                cConfig().log("playertype from config: mplayer")
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                cConfig().log("playertype from config: dvdplayer")
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False
def play__():
    oGui = cGui()

    TIK='|User-Agent=User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    if '.ts' in sUrl:
            sUrl = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(sUrl)+'&amp;streamtype=TSDOWNLOADER&name='+urllib.quote(sTitle)+ TIK
  
    playlist=xbmc.PlayList(xbmc.PLAYER_CORE_DVDPLAYER); 
    playlist.clear();
    listitem1 = xbmcgui.ListItem(''+sTitle)
    playlist.add(sUrl,listitem1);
    player_type = sPlayerType()
    xbmcPlayer = xbmc.Player (player_type); 
    xbmcPlayer.play (playlist)
    return
        
    oGui.setEndOfDirectory()
         
def make_closing(base, **attrs):
    """
    Needed for BZ2File with Python (2.6), which otherwise raise "AttributeError: BZ2File instance has no attribute '__exit__'".
    """
    if not hasattr(base, '__enter__'):
        attrs['__enter__'] = lambda self: self
    if not hasattr(base, '__exit__'):
        attrs['__exit__'] = lambda self, type, value, traceback: self.close()
    return type('Closing' + base.__name__, (base, object), attrs)
    
useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0'
SPORTS ='https://dl.dropboxusercontent.com/s/k2jz15prgor015u/dcc12.html'
headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Connection', 'keep-alive']
]
def urllibrequest(url, postfields = {}, headers = {}, cookie = 'cookie.lpw', loc = None):
    """
        url = 'http://www.diziizleyin.net/index.php?x=isyan'
        postfields = {'pid' : 'p2x29464a434'}
        txheaders = {'X-Requested-With':'XMLHttpRequest'}
        myrequest(url, postfields, headers, loc)
    """
    url = url if url.startswith('http://') else 'http://' + url
    req = urllib2.Request(url)
    cj = cookielib.LWPCookieJar()
    if os.path.isfile('cookie.lpw'):
        cj.load('cookie.lpw')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    if postfields:
        postfields = urllib.urlencode(postfields)
        req = urllib2.Request(url, postfields)
    req.add_header('User-Agent', useragent)
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)

    response = urllib2.urlopen(req)
    if loc:
        data = response.geturl()
        response.close()
    else:
        data = response.read()
        response.close()
        cj.save('cookie.lpw')
    return data
def get_post_data():
    Url = 'http://139.59.68.238/stm-v3/api/def2.php?id=340&quality=1&type=0'
    data=requests.session().get(Url,headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)","Host": "139.59.68.238","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
    liste = re.findall('"token": "VL(.*?)"',data, re.S)[0]    
    datam = b64decode(liste)
    listem = re.findall('"swt",".*?","1","aY(.*?)"',datam, re.S)[0] 
    datama= b64decode(listem)

    return datama

def Play_f4mProxy(url, name, iconimage):
    
    streamtype='TSDOWNLOADER'
    maxbitrate = Addon.getSetting('BitRateMax')
    if Addon.getSetting('use_simple') == "true":
        simpledownloader = True
    else:
        simpledownloader = False
    
    sys.path.insert(0, f4mProxy)
    from F4mProxy import f4mProxyHelper
    player=f4mProxyHelper()
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
    if streamtype == "TSDOWNLOADER":
        
        maxbitrate=0
        player.playF4mLink(url, name, None, True, maxbitrate, simpledownloader, None, streamtype, False, None, iconimage)    
    

import sys,traceback,urllib2,re, urllib



import sys,traceback,urllib2,re, urllib
    
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvNDdoeTFteTA3Zjh0b3dkL3BsdWdpbi5waHA="
HOSsT =base64.b64decode(yen)
urlHOST = 'https://dl.dropboxusercontent.com/s/vjykn4jlza4yo32/saved_resource.html'
def TURKIYE(url):
    resp = net.http_GET(url)
    sHtmlContent = resp.content  
    sPattern = 'action="(.+?)"'
    aResult = re.findall(sPattern,sHtmlContent)
    return  aResult[0]  

                    
def TURKEY(url):
    resp = net.http_GET(url)
    sHtmlContent = resp.content  
    sPattern = 'Paction="(.+?)"'
    aResult = re.findall(sPattern,sHtmlContent)
    return  aResult[0]  

                    

HOSTO='PT1nQ05zMVBsOVRYcmd5UFU5VEtyQUNLbzh6UC9rQ0lyQUNLL1ExUHBreUtnZ3lZZTlsWHZseUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJb01tWGY1MWJwc0NJbzh6UC9reVcvVTJQZHRDS284elAva0NJckFDS3Y1MVhlOVdLcHNDSW9neWJlOWxYdmxDSXRBQ0svUTFQcGt5S2dneVAvOFRLYjlUWi8wMUtvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0tvOHpQL2tDSXJBQ0t2NTFYZTlXS3BzQ0lvOHpQL2t5Vy9VMlBkdENLbzh6UC9rQ0lyQUNLL1ExUHBreUtnZ0NLLzh6UHBBeUtnZ3liZTlsWHZsU0tyQUNLLzh6UHBzMVBsOVRYcmd5UFU5VEtyQUNLLzh6UHBzQ0lvOHpQL2t5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW84elAva3lLZ2d5UC84VEtiOVRaLzAxS29neVAvOFRLZ3NDSW84RFYva1NLckFDS284bVhmNTFicEF5S284bVhmNTFicGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dneVAvOFRLckFDSy84elBwc0NJbzh6UC9reVcvVTJQZHRDSy9RMVBwc0NJb2d5YmU5bFh2bENJcmd5YmU5bFh2bFNLckFDS284bVhmNTFicEFTTGdneVBVOVRLcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neVAvOFRLZ3NDSW84RFYva1NLckFDS284elAva0NJckFDS3Y1MVhlOVdLcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0tqNTFYZTlXS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0svOHpQcHNDSW9neWJlOWxYdmxDSXRBQ0svUTFQcGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neVAvOFRLZ3NDSW84bVhmNTFicGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneWJlOWxYdmxTS3JBQ0tqNTFYZTlXS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ0NLLzh6UHBBeUtnZ3lQVTlUS3BzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3liZTlsWHZsQ0lyZ3liZTlsWHZsU0tyQUNLdjUxWGU5V0tyQUNLLzh6UHBzMVBsOVRYcmd5UFU5VEtyQUNLLzh6UHBzQ0lvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ0NLdjUxWGU5V0tnMENJbzhEVi9rU0tyQUNLLzh6UHBzMVBsOVRYcmd5UFU5VEtyQUNLLzh6UHBzQ0lvOG1YZjUxYnBzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0tvOHpQL2tDSXJBQ0t2NTFYZTlXS3BzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ3lQLzhUS3JBQ0tvOHpQL2tDSXJBQ0svUTFQcGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ3lQLzhUS3JBQ0svOHpQcDR5Vy9VMlBkdENLL1ExUHBzQ0lvOHpQL2t5S2dneWJlOWxYdmx5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neVAvOFRLZ3NDSW84bVhmNTFicGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neVAvOFRLZ3NDSW84RFYva1NLckFDSy84elBwOHlXL1UyUGR0Q0svUTFQcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0t2NTFYZTlXS3JBQ0svOHpQcDh5Vy84elBkdENLbzh6UC9rQ0lyQUNLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLLzh6UHBBeUtnZ3liZTlsWHZsU0tyQUNLL1ExUHBzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3liZTlsWHZsQ0lyZ3liZTlsWHZsU0tyQUNLbzh6UC9rQ0lyQUNLL1ExUHBreUtnZ3lQLzhUS2p0MVBsOVRYcmdDSy84elBwQXlLZ2d5YmU5bFh2bFNLckFDS2o1MVhlOVdLckFDSy84elBwUTJXL1UyUGR0Q0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ3lQVTlUS3JBQ0svOHpQcGszVy84elBkdENLbzhtWGY1MWJwQXlLbzhtWGY1MWJwa3lLZ2d5WWU5bFh2bHlLZ2d5UC84VEtsdDFQbDlUWHJneVBVOVRLckFDSy84elBwc0NJbzhEVi9reUtnZ3lQLzhUS3R0MVBsOVRYcmd5UFU5VEtyQUNLbzhtWGY1MWJwQXlLbzhtWGY1MWJwa3lLZ2dDSy84elBwQXlLZ2d5UFU5VEtwc0NJbzh6UC9rQ2ViOVRaLzAxS29neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0t2NTFYZTlXS3JBQ0svOHpQcHMxUGw5VFhyZ0NLLzh6UHBBeUtnZ3lQVTlUS3BzQ0lvZ3lQLzhUS2dzQ0lvOG1YZjUxYnBreUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ3lQLzhUS3JBQ0svOHpQcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW84elAva3lLZ2d5YmU5bFh2bHlLZ2d5UC84VEtiOVRaLzAxS284RFYva3lLZ2d5UC84VEtyQUNLdjUxWGU5V0tyQUNLLzh6UHBzMVBsOVRYcmdDS3Y1MVhlOVdLZ3NDS3Y1MVhlOVdLcHNDSW84RFYva3lLZ2d5UC84VEtiOVRaLzAxS29neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0svUTFQcHNDSW84elAva2lMYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9NbVhmNTFicHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0svOHpQcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neVAvOFRLZ3NDSW84RFYva1NLckFDS284elAva0NJckFDSy9RMVBwa3lLZ2d5UC84VEtiOVRaLzAxS284RFYva3lLZ2dDSy84elBwQXlLZ2d5UFU5VEtwc0NJbzh6UC9reUtnZ3lQLzhUSw'


class getUrl(object):
    def __init__(self, url, close=True, proxy=None, post=None, headers=None, mobile=False, referer=None, cookie=None, output='', timeout='10'):
        handlers = []
        if not proxy == None:
            handlers += [urllib2.ProxyHandler({'http':'%s' % (proxy)}), urllib2.HTTPHandler]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or not close == True:
            import cookielib
            cookies = cookielib.LWPCookieJar()
            handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        try:
            if sys.version_info < (2, 7, 9): raise Exception()
            import ssl; ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            handlers += [urllib2.HTTPSHandler(context=ssl_context)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        except:
            pass
        try: headers.update(headers)
        except: headers = {}
        if 'User-Agent' in headers:
            pass
        elif not mobile == True:
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0'
        else:
            headers['User-Agent'] = 'Apple-iPhone/701.341'
        if 'referer' in headers:
            pass
        elif referer == None:
            headers['referer'] = url
        else:
            headers['referer'] = referer
        if not 'Accept-Language' in headers:
            headers['Accept-Language'] = 'en-US'
        if 'cookie' in headers:
            pass
        elif not cookie == None:
            headers['cookie'] = cookie
        request = urllib2.Request(url, data=post, headers=headers)
        response = urllib2.urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = []
            for c in cookies: result.append('%s=%s' % (c.name, c.value))
            result = "; ".join(result)
        elif output == 'geturl':
            result = response.geturl()
        else:
            result = response.read()
        if close == True:
            response.close()
        self.result = result
def ggegetUrl(url, cookieJar=None,post=None, timeout=20, headers=None):
    
    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
#    opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;
  
def gegetUrl(url, cookieJar=None,post=None, timeout=20, headers=None):
    if not 'http' in url:
        url = 'http:' + url
    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
#    opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;
           
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvMDZvb3pwd2poc3VzMXAxL3BsYXlsaXN0X29yaGFudHYubTN1"
IPTVHOST =base64.b64decode(yen)
url_all_products = "http://www.livemobiletv247.com/android_app/webservice/get_channels.php"
def ABCkodla(sMovieTitle):
    sMovieTitle = unicode(sMovieTitle, 'utf-8')#converti en unicode pour aider aux convertions
    sMovieTitle = unicodedata.normalize('NFD', sMovieTitle).encode('ascii', 'ignore').decode("unicode_escape")#vire accent et '\'
    sMovieTitle = sMovieTitle.encode("utf-8").lower() #on repasse en utf-8
 
    return sMovieTitle
def malfabekodla(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
                    
def lalfabekodla(text):
   return text if isinstance(text, unicode) else text.decode('utf8')                      
def alfabekodla(text):

        reload(sys)
        sys.setdefaultencoding("utf-8")
        return text                           
                                          
def georgiadecode( data):                             
                        data = (str(data)).replace('%e1%83%90','a')
                        data = (str(data)).replace('\u10d1','b')
                        data = (str(data)).replace("\u10e9" , "ch")
                        data = (str(data)).replace('\u10d3',"d")
                        data = (str(data)).replace('%e1%83%94',"e")
                        data = (str(data)).replace(" %e1%83%96" , "sh")
                        data = (str(data)).replace('\u10d2',"g")
                        data = (str(data)).replace("\u10e7" , "q'")
                        data = (str(data)).replace('%e1%83%98','i')
                        data = (str(data)).replace("\u10e6" , "gh")
                        data = (str(data)).replace("\u10d9" , "k'")
                        data = (str(data)).replace('%e1%83%94','l')
                        data = (str(data)).replace('%e1%83%9b','m')
                        data = (str(data)).replace('%e1%83%9c','n')
                        data = (str(data)).replace('\u10dd','o')
                        data = (str(data)).replace('%e1%83%94','p')
                        data = (str(data)).replace("%e1%83%a5" , "k")
                        data = (str(data)).replace('%e1%83%ac','r')
                        data = (str(data)).replace('%e1%83%98','s')
                        data = (str(data)).replace('%e1%83%a2',"t'")
                        data = (str(data)).replace('%e1%83%a3','u')
                        data = (str(data)).replace('%e1%83%95','v')
                        data = (str(data)).replace('\u10e2',"t'")
                        data = (str(data)).replace("\u10df" , "zh")
                        data = (str(data)).replace("\u10ea" , "ts")
                        data = (str(data)).replace("\u10eb" , "dz")
                        data = (str(data)).replace("\u10ec" , "ts'")
                        data = (str(data)).replace("\u10ed" , "ch'")
                        data = (str(data)).replace("\u10ee" , "kh")
                        data = (str(data)).replace("\u10ef" , "j" )
                        data = (str(data)).replace("%e1%83%99" , "k'")
                        data = (str(data)).replace('%e1%83%9c','z')
                        return data



def fs(s):
	s=str(repr(s))[1:-1]
	s=s.replace('\\xb8','ё')
	s=s.replace('\\xe0','a')
	s=s.replace('\\xe1','б')
	s=s.replace('\\xe2','в')
	s=s.replace('\\xe3','г')
	s=s.replace('\\xe4','д')
	s=s.replace('\\xe5','е')
	s=s.replace('\\xe6','ж')
	s=s.replace('\\xe7','з')
	s=s.replace('\\xe8','и')
	s=s.replace('\\xe9','й')
	s=s.replace('\\xea','к')
	s=s.replace('\\xeb','л')
	s=s.replace('\\xec','м')
	s=s.replace('\\xed','н')
	s=s.replace('\\xee','о')
	s=s.replace('\\xef','п')
	s=s.replace('\\xf0','р')
	s=s.replace('\\xf1','с')
	s=s.replace('\\xf2','т')
	s=s.replace('\\xf3','у')
	s=s.replace('\\xf4','ф')
	s=s.replace('\\xf5','х')
	s=s.replace('\\xf6','ц')
	s=s.replace('\\xf7','ч')
	s=s.replace('\\xf8','ш')
	s=s.replace('\\xf9','щ')
	s=s.replace('\\xfa','ъ')
	s=s.replace('\\xfb','ы')
	s=s.replace('\\xfc','ь')
	s=s.replace('\\xfd','э')
	s=s.replace('\\xfe','ю')
	s=s.replace('\\xff','я')
	
	s=s.replace('\\xa8','Ё')
	s=s.replace('\\xc0','А')
	s=s.replace('\\xc1','Б')
	s=s.replace('\\xc2','В')
	s=s.replace('\\xc3','Г')
	s=s.replace('\\xc4','Д')
	s=s.replace('\\xc5','Е')
	s=s.replace('\\xc6','Ж')
	s=s.replace('\\xc7','З')
	s=s.replace('\\xc8','И')
	s=s.replace('\\xc9','Й')
	s=s.replace('\\xca','К')
	s=s.replace('\\xcb','Л')
	s=s.replace('\\xcc','М')
	s=s.replace('\\xcd','Н')
	s=s.replace('\\xce','О')
	s=s.replace('\\xcf','П')
	s=s.replace('\\xd0','Р')
	s=s.replace('\\xd1','С')
	s=s.replace('\\xd2','Т')
	s=s.replace('\\xd3','У')
	s=s.replace('\\xd4','Ф')
	s=s.replace('\\xd5','Х')
	s=s.replace('\\xd6','Ц')
	s=s.replace('\\xd7','Ч')
	s=s.replace('\\xd8','Ш')
	s=s.replace('\\xd9','Щ')
	s=s.replace('\\xda','Ъ')
	s=s.replace('\\xdb','Ы')
	s=s.replace('\\xdc','Ь')
	s=s.replace('\\xdd','Э')
	s=s.replace('\\xde','Ю')
	s=s.replace('\\xdf','Я')
	
	s=s.replace('\\xab','"')
	s=s.replace('\\xbb','"')
	s=s.replace('\\r','')
	s=s.replace('\\n','\n')
	s=s.replace('\\t','\t')
	s=s.replace("\\x85",'...')
	s=s.replace("\\x97",'-')
	s=s.replace("\\xb7","·")
	s=s.replace("\\x96",'-')
	s=s.replace("\\x92",'')
	s=s.replace("\\xb9",'№')
	s=s.replace("\\xa0",' ')
	s=s.replace('&laquo;','"')
	s=s.replace('&raquo;','"')
	s=s.replace('&#38;','&')
	s=s.replace('&#233;','é')
	s=s.replace('&#232;','è')
	s=s.replace('&#224;','à')
	s=s.replace('&#244;','ô')
	s=s.replace('&#246;','ö')
	return s


def otvdecode( data):   
	                
                        data = (str(data)).replace("xFFFD","?") 
                        data = (str(data)).replace('x201E','"')
                        data = (str(data)).replace('x214B','&')
                        data = (str(data)).replace('x002C',"'")
                        data = (str(data)).replace('x0029',"(")
                        data = (str(data)).replace('x0028',")")
                        data = (str(data)).replace('x0027',",")
                        data = (str(data)).replace('x02D9',".")
                        data = (str(data)).replace('x061B',';')
                        data = (str(data)).replace('x003E','<')
                        data = (str(data)).replace('x003C','>')
                        data = (str(data)).replace('x061A','/')
                        data = (str(data)).replace('x007D','{')
                        data = (str(data)).replace('x007B','}')
                        data = (str(data)).replace('x0255','_')
                        data = (str(data)).replace('x02HG','-')
                        data = (str(data)).replace('x005D','[')
                        data = (str(data)).replace('x005B',']')
                        
                        data = (str(data)).replace("61","=") 
                        data = (str(data)).replace('x0250','a')
                        data = (str(data)).replace('x0071','b')
                        data = (str(data)).replace('x0254',"c")
                        data = (str(data)).replace('x0070',"d")
                        data = (str(data)).replace('x01DD',"e")
                        data = (str(data)).replace('x025F',"f")
                        data = (str(data)).replace('x0183',"g")
                        data = (str(data)).replace('x0265','h')
                        data = (str(data)).replace('x0131','i')
                        data = (str(data)).replace('x027E','j')
                        data = (str(data)).replace('x029E','k')
                        data = (str(data)).replace('x0283','l')
                        data = (str(data)).replace('x026F','m')
                        data = (str(data)).replace('x0075','n')
                        data = (str(data)).replace('x006F','o')
                        data = (str(data)).replace('x0064','p')
                        data = (str(data)).replace('x0062','q')
                        data = (str(data)).replace('x0279','r')
                        data = (str(data)).replace('x0073','s')
                        data = (str(data)).replace('x0287','t')
                        data = (str(data)).replace('x006E','u')
                        data = (str(data)).replace('x028C','v')
                        data = (str(data)).replace('x028D','w')
                        data = (str(data)).replace('x0078','x')
                        data = (str(data)).replace('x028E','y')
                        data = (str(data)).replace('x007A','z')
                        data = (str(data)).replace('x0030','0')
                        data = (str(data)).replace('x21C2','1')
                        data = (str(data)).replace('x1105','2')
                        data = (str(data)).replace('x0190','3')
                        data = (str(data)).replace('x3123','4')
                        data = (str(data)).replace('x078E','5')
                        data = (str(data)).replace('x0039','6')
                        data = (str(data)).replace('x3125','7')
                        data = (str(data)).replace('x0038','8')
                        data = (str(data)).replace('x0036','9')

                        data = (str(data)).replace('x2200','A')
                        data = (str(data)).replace('x10412','B')
                        data = (str(data)).replace('x0186',"C")
                        data = (str(data)).replace('x25D6',"D")
                        data = (str(data)).replace('x018E',"E")
                        data = (str(data)).replace('x2132',"F")
                        data = (str(data)).replace('x2141',"G")
                        data = (str(data)).replace('x0048','H')
                        data = (str(data)).replace('x0049','I')
                        data = (str(data)).replace('x017F','J')
                        data = (str(data)).replace('x22CA','K')
                        data = (str(data)).replace('x02E5','L')
                        data = (str(data)).replace('x0057','M')
                        data = (str(data)).replace('x004E','N')
                        data = (str(data)).replace('x004F','O')
                        data = (str(data)).replace('x0500','P')
                        data = (str(data)).replace('x2141','G')
                        data = (str(data)).replace('x038C','Q')
                        data = (str(data)).replace('x1D1A','R')
                        data = (str(data)).replace('x0053','S')
                        data = (str(data)).replace('x22A5','T')
                        data = (str(data)).replace('x2229','U')
                        data = (str(data)).replace('x039B','V')
                        data = (str(data)).replace('x004D','W')
                        data = (str(data)).replace('x0058','X')
                        data = (str(data)).replace('x2144','Y')
                        data = (str(data)).replace('x005A','Z')
                                               
                        data = (str(data)).replace("&amp;#","&")
                        data = (str(data)).replace(";<otv/>",":")
                        return data
import re,sys,urllib2,HTMLParser, time, urlparse, gzip, StringIO



      


ADULT_PIN="7686"
def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = txt.replace('&#8236;','')
    txt = HTMLParser.HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    return txt

def getVideoID(url):
    try :
        return re.compile('(id|url|v|si|sim|data-config|file)=(.+?)/').findall(url + '/')[0][1]
    except:
        return




def HTTizletv(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:57.0) Gecko/20100101 Firefox/57.0','upgrade-insecure-requests': '1'}
    url = requests.get(url, headers = headers).text
    url= unicodedata.normalize('NFD', url).encode('ascii', 'ignore')#vire accent
    url = url.encode( "utf-8")                                                                                                                                                   
    url = urllib.unquote_plus(url) 
    url = url.replace('','')
    return url
            
   
def play__tvizle():
    oGui = cGui()
    gerutl= 'https://www.izletv2.tk/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36','Upgrade-Insecure-Requests': '1'}
    datam = cRequestHandler(gerutl).request()
    festurl = re.findall('<link rel="canonical" href="(.*?)"', datam, re.S)[0]
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url= 'https://www.izletv2.tk'
    lka= 'https://www.izletv2.tk'+sUrl
    if  lka:
                    html= cRequestHandler(lka).request()
                    hash, id = re.findall('(?:watch|live)\("([^"]+)","([^"]+)"', html, re.IGNORECASE)[0]
                    data = urllib.urlencode({'hash': hash, 'id': id, 'e': '03BSTMTRKLR'})
                    req = urllib2.Request(lka, data, headers) 
                    response = urllib2.urlopen(req)
                    link = response.read()
                    response.close()
                    link1 = link [::-1]
                    #link1 = link1.replace('_','=') + '=='
                    #first64, second64 = re.findall('(.*?=)(.*?==)', link1, re.IGNORECASE)[0]
                    #son_url1 = base64.b64decode(first64)+'?'+base64.b64decode(second64)
                    son_url1 = decode_base64(link1)
                    Header = '|Referer='+lka+'&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
                    url = son_url1 + Header
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def agent():
    return 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'


def host(url):
    host = re.findall('([\w]+[.][\w]+)$', urlparse.urlparse(url.strip().lower()).netloc)[0]
    return str(host)
def IPTVdep( gobble ) :
        gobble= gobble.replace('get.php',"panel_api.php")
        return gobble


def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok






class mOTVye():

 def OTVgir(self,url):

    Url =url[1]+url[2]+url[3]+url[4]+url[5]+url[6]+url[7]+url[8]+url[9]+url[10]+url[11]+url[12]+url[13]+url[14]+url[15]+url[16]+url[17]+url[18]+url[19]+url[20]+url[21]+url[22]+url[23]+url[24]+url[25]+url[26]+url[27]+url[28]+url[29]+url[30]+url[31]+url[32]+url[33]+url[34]+url[35]+url[36]+url[37]+url[38]+url[39]+url[40]+url[41]+url[42]+url[43]+url[44]+url[45]+url[46]+url[47]+url[48]+url[49]+url[50]+url[51]+url[52]+url[53]+url[54]+url[55]+url[56]+url[57]+url[58]+url[59]+url[60]+url[61]+url[62]+url[63]+url[64]+url[65]+url[66]+url[67]+url[68]+url[69]+url[70]+url[71]+url[72]+url[73]+url[74]+url[75]+url[76]+url[77]+url[78]+url[79]+url[80]+url[81]+url[82]+url[83]+url[84]+url[85]+url[86]+url[87]+url[88]+url[89]+url[90]+url[91]+url[92]+url[93]+url[94]+url[95]+url[96]+url[97]+url[98]+url[99]+url[100]+url[101]+url[102]+url[103]+url[104]+url[105]+url[106]+url[107]+url[108]+url[109]+url[110]+url[111]+url[112]+url[113]+url[114]+url[115]+url[116]+url[117]+url[118]+url[119]+url[120]+url[121]+url[122]+url[123]+url[124]+\
    url[125]+\
    url[126]+url[127]+url[128]+url[129]+url[130]+url[131]+url[132]+url[133]+url[134]+url[135]+url[136]+url[137]+url[138]+url[139]+url[140]+url[141]+url[142]+url[143]+url[144]+url[145]+url[146]+url[147]+url[148]+url[149]+url[150]+url[151]+url[152]+url[153]+url[154]+url[155]+url[156]+url[157]+url[158]+url[159]+url[160]+url[161]+url[162]+url[163]+url[164]+url[165]+url[166]+url[167]+url[168]+url[169]+url[170]+url[171]+url[172]+url[173]+url[174]+url[175]+url[176]+url[177]+url[178]+url[179]+url[180]+url[181]+url[182]+url[183]+url[184]+url[185]+url[186]+url[187]+url[188]+url[189]+url[190]+url[191]+url[192]+url[193]+url[194]+url[195]+url[196]+url[197]+url[198]+url[199]+url[200]+url[201]+url[202]+url[203]+url[204]+url[205]+url[206]+url[207]+url[208]+url[209]+url[210]+url[211]+url[212]+url[213]+url[214]+url[215]+url[216]+url[217]+url[218]+url[219]+url[220]+url[221]+url[222]+url[223]+url[224]+url[225]+url[226]+url[227]+url[228]+url[229]+url[230]+url[231]+url[232]+url[233]+url[234]+url[235]+url[236]+url[237]+url[238]+\
    url[239]+url[240]+url[241]+url[242]+url[243]+url[244]+url[245]+url[246]+url[247]+url[248]+url[249]+url[250]+url[251]+url[252]+url[253]+url[254]+url[255]+url[256]+url[257]+url[258]+url[259]+url[260]+url[261]+url[262]+url[263]+url[264]+url[265]+url[266]+url[267]+url[268]+url[269]+url[270]+url[271]+url[272]+url[273]+url[274]+url[275]+url[276]+url[277]+url[278]+url[279]+url[280]+url[281]+url[282]+url[283]+url[284]+url[285]+url[286]+url[287]+url[288]+url[289]+url[290]+url[291]+url[292]+url[293]+url[294]+url[295]+url[296]+url[297]+url[298]+url[299]+url[300]+url[301]+url[302]+url[303]+url[304]+url[305]+url[306]+url[307]+url[308]+url[309]+url[310]+url[311]+url[312]+url[313]+url[314]+url[315]+url[316]+url[317]+url[318]+url[319]+url[320]+url[321]+url[322]+url[323]+url[324]+url[325]+url[326]+url[327]+url[328]+url[329]+url[330]+url[331]+url[332]+url[333]+url[334]+url[335]+url[336]+url[337]+url[338]+url[339]+url[340]+url[341]+url[342]+url[343]+url[344]+url[345]+url[346]+url[347]+url[348]+url[349]+url[350]+url[351]+\
    url[352]+url[353]+url[354]+url[355]+url[356]+url[357]+url[358]+url[359]+url[360]+url[361]+url[362]+url[363]+url[364]+url[365]+url[366]+url[367]+url[368]+url[369]+url[370]+url[371]+url[372]+url[373]+url[374]+url[375]+url[376]+url[377]+url[378]+url[379]+url[380]+url[381]+url[382]+url[383]+url[384]+url[385]+url[386]+url[387]+url[388]+url[389]+url[390]+url[391]+url[392]+url[393]+url[394]+url[395]+url[396]+url[397]+url[398]+url[399]+url[400]+url[401]+url[402]+url[403]+url[404]+url[405]+url[406]+url[407]+url[408]+url[409]+url[410]+url[411]+url[412]+url[413]+url[414]+url[415]+url[416]+url[417]+url[418]+url[419]+url[420]+url[421]+url[422]+url[423]+url[424]+url[425]+url[426]+url[427]+url[428]+url[429]+url[430]+url[431]+url[432]+url[433]+url[434]+url[435]+url[436]+url[437]+url[438]+url[439]+url[440]+url[441]+url[442]+url[443]+url[444]+url[445]+url[446]+url[447]+url[448]+url[449]+url[450]+url[451]+url[452]+url[453]+url[454]+url[455]+url[456]+url[457]+url[458]+url[459]+url[460]+url[461]+url[462]+url[463]+url[464]+\
    url[465]+url[466]+url[467]+url[468]+url[469]+url[470]+url[471]+url[472]+url[473]+url[474]+url[475]+url[476]+url[477]+url[478]+url[479]+url[480]+url[481]+url[482]+url[483]+url[484]+url[485]+url[486]+url[487]+url[488]+url[489]+url[490]+url[491]+url[492]+url[493]+url[494]+url[495]+url[496]+url[497]+url[498]+url[499]+url[500]+url[501]+url[502]+url[503]+url[504]+url[505]+url[506]+url[507]+url[508]+url[509]+url[510]+url[511]+url[512]+url[513]+url[514]+url[515]+url[516]+url[517]+url[518]+url[519]+url[520]+url[521]+url[522]+url[523]+url[524]+url[525]+url[526]+url[527]+url[528]+url[529]+url[530]+url[531]+url[532]+url[533]+url[534]+url[535]+url[536]+url[537]+url[538]+url[539]+url[540]+url[541]+url[542]+url[543]+url[544]+url[545]+url[546]+url[547]+url[548]+url[549]+url[550]+url[551]+url[552]+url[553]+url[554]+url[555]+url[556]+url[557]+url[558]+url[559]+url[560]+url[561]+url[562]+url[563]+url[564]+url[565]+url[566]+url[567]+url[568]+url[569]+url[570]+url[571]+url[572]+url[573]+url[574]+url[575]+url[576]+url[577]+\
    url[578]+url[579]+url[580]+url[581]+url[582]+url[583]+url[584]+url[585]+url[586]+url[587]+url[588]+url[589]+url[590]+url[591]+url[592]+url[593]+url[594]+url[595]+url[596]+url[597]+url[598]+url[599]+url[600]+url[601]+url[602]+url[603]+url[604]+url[605]+url[606]+url[607]+url[608]+url[609]+url[610]+url[611]+url[612]+url[613]+url[614]+url[615]+url[616]+url[617]+url[618]+url[619]+url[620]+url[621]+url[622]+url[623]+url[624]+url[625]+url[626]+url[627]+url[628]+url[629]+url[630]+url[631]+url[632]+url[633]+url[634]+url[635]+url[636]+url[637]+url[638]+url[639]+url[640]+url[641]+url[642]+url[643]+url[644]+url[645]+url[646]+url[647]+url[648]+url[649]+url[650]+url[651]+url[652]+url[653]+url[654]+url[655]+url[656]+url[657]+url[658]+url[659]+url[660]+url[661]+url[662]+url[663]+url[664]+url[665]+url[666]+url[667]+url[668]+url[669]+url[670]+url[671]+url[672]+url[673]+url[674]+url[675]+url[676]+url[677]+url[678]+url[679]+url[680]+url[681]+url[682]+url[683]+url[684]+url[685]+url[686]+url[687]+url[688]+url[689]+url[690]+\
    url[691]+url[692]+url[693]+url[694]+url[695]+url[696]+url[697]+url[698]+url[699]+url[700]+url[701]+url[702]+url[703]+url[704]+url[705]+url[706]+url[707]+url[708]+url[709]+url[710]+url[711]+url[712]+url[713]+url[714]+url[715]+url[716]+url[717]+url[718]+url[719]+url[720]+url[721]+url[722]+url[723]+url[724]+url[725]+url[726]+url[727]+url[728]+url[729]+url[730]+url[731]+url[732]+url[733]+url[734]+url[735]+url[736]+url[737]+url[738]+url[739]+url[740]+url[741]+url[742]+url[743]+url[744]+url[745]+url[746]+url[747]+url[748]+url[749]+url[750]+url[751]+url[752]+url[753]+url[754]+url[755]+url[756]+url[757]+url[758]+url[759]+url[760]+url[761]+url[762]+url[763]+url[764]+url[765]+url[766]+url[767]+url[768]+url[769]+url[770]+url[771]+url[772]+url[773]+url[774]+url[775]+url[776]+url[777]+url[778]+url[779]+url[780]+url[781]+url[782]+url[783]+url[784]+url[785]+url[786]+url[787]+url[788]+url[789]+url[790]+url[791]+url[792]+url[793]+url[794]+url[795]+url[796]+url[797]+url[798]+url[799]+url[800]+url[801]+url[802]+url[803]+\
    url[804]+url[805]+url[806]+url[807]+url[808]+url[809]+url[810]+url[811]+url[812]+url[813]+url[814]+url[815]+url[816]+url[817]+url[818]+url[819]+url[820]+url[821]+url[822]+url[823]+url[824]+url[825]+url[826]+url[827]+url[828]+url[829]+url[830]+url[831]+url[832]+url[833]+url[834]+url[835]+url[836]+url[837]+url[838]+url[839]+url[840]+url[841]+url[842]+url[843]+url[844]+url[845]+url[846]+url[847]+url[848]+url[849]+url[850]+url[851]+url[852]+url[853]+url[854]+url[855]+url[856]+url[857]+url[858]+url[859]+url[860]+url[861]+url[862]+url[863]+url[864]+url[865]+url[866]+url[867]+url[868]+url[869]+url[870]+url[871]+url[872]+url[873]+url[874]+url[875]+url[876]+url[877]+url[878]+url[879]+url[880]+url[881]+url[882]+url[883]+url[884]+url[885]+url[886]+url[887]+url[888]+url[889]+url[890]+url[891]+url[892]+url[893]+url[894]+url[895]+url[896]+url[897]+url[898]+url[899]+url[900]+url[901]+url[902]+url[903]+url[904]+url[905]+url[906]+url[907]+url[908]+url[909]+url[910]+url[911]+url[912]+url[913]+url[914]+url[915]+url[916]+\
    url[917]+url[918]+url[919]+url[920]+url[921]+url[922]+url[923]+url[924]+url[925]+url[926]+url[927]+url[928]+url[929]+url[930]+url[931]+url[932]+url[933]+url[934]+url[935]+url[936]+url[937]+url[938]+url[939]+url[940]+url[941]+url[942]+url[943]+url[944]+url[945]+url[946]+url[947]+url[948]+url[949]+url[950]+url[951]+url[952]+url[953]+url[954]+url[955]+url[956]+url[957]+url[958]+url[959]+url[960]+url[961]+url[962]+url[963]+url[964]+url[965]+url[966]+url[967]+url[968]+url[969]+url[970]+url[971]+url[972]+url[973]+url[974]+url[975]+url[976]+url[977]+url[978]+url[979]+url[980]+url[981]+url[982]+url[983]+url[984]+url[985]+url[986]+url[987]+url[988]+url[989]+url[990]+url[991]+url[992]+url[993]+url[994]+url[995]+url[996]+url[997]+url[998]+url[999]+url[1000]+url[1001]+url[1002]+url[1003]+url[1004]+url[1005]+url[1006]+url[1007]+url[1008]+url[1009]+url[1010]+url[1011]+url[1012]+url[1013]+url[1014]+url[1015]+url[1016]+url[1017]+url[1018]+url[1019]+url[1020]+url[1021]+url[1022]+url[1023]+url[1024]+url[1025]+url[1026]+\
    url[1027]+url[1028]+url[1029]+url[1030]+url[1031]+url[1032]+url[1033]+url[1034]+url[1035]+url[1036]+url[1037]+url[1038]+url[1039]+url[1040]+url[1041]+url[1042]+url[1043]+url[1044]+url[1045]+url[1046]+url[1047]+url[1048]+url[1049]+url[1050]+url[1051]+url[1052]+url[1053]+url[1054]+url[1055]+url[1056]+url[1057]+url[1058]+url[1059]+url[1060]+url[1061]+url[1062]+url[1063]+url[1064]+url[1065]+url[1066]+url[1067]+url[1068]+url[1069]+url[1070]+url[1071]+url[1072]+url[1073]+url[1074]+url[1075]+url[1076]+url[1077]+url[1078]+url[1079]+url[1080]+url[1081]+url[1082]+url[1083]+url[1084]+url[1085]+url[1086]+url[1087]+url[1088]+url[1089]+url[1090]+url[1091]+url[1092]+url[1093]+url[1094]+url[1095]+url[1096]+url[1097]+url[1098]+url[1099]+url[1100]+url[1101]+url[1102]+url[1103]+url[1104]+url[1105]+url[1106]+url[1107]+url[1108]+url[1109]+url[1110]+url[1111]+url[1112]+url[1113]+url[1114]+url[1115]+url[1116]+url[1117]+url[1118]+url[1119]+url[1120]+url[1121]+url[1122]+url[1123]+url[1124]+url[1125]+url[1126]+url[1127]+\
    url[1128]+url[1129]+url[1130]+url[1131]+url[1132]+url[1133]+url[1134]+url[1135]+url[1136]+url[1137]+url[1138]+url[1139]+url[1140]+url[1141]+url[1142]+url[1143]+url[1144]+url[1145]+url[1146]+url[1147]+url[1148]+url[1149]+url[1150]+url[1151]+url[1152]+url[1153]+url[1154]+url[1155]+url[1156]+url[1157]+url[1158]+url[1159]+url[1160]+url[1161]+url[1162]+url[1163]+url[1164]+url[1165]+url[1166]+url[1167]+url[1168]+url[1169]+url[1170]+url[1171]+url[1172]+url[1173]+url[1174]+url[1175]+url[1176]+url[1177]+url[1178]+url[1179]+url[1180]+url[1181]+url[1182]+url[1183]+url[1184]+url[1185]+url[1186]+url[1187]+url[1188]+url[1189]+url[1190]+url[1191]+url[1192]+url[1193]+url[1194]+url[1195]+url[1196]+url[1197]+url[1198]+url[1199]+url[1200]+url[1201]+url[1202]+url[1203]+url[1204]+url[1205]+url[1206]+url[1207]+url[1208]+url[1209]+url[1210]+url[1211]+url[1212]+url[1213]+url[1214]+url[1215]+url[1216]+url[1217]+url[1218]+url[1219]+url[1220]+url[1221]+url[1222]+url[1223]+url[1224]+url[1225]+url[1226]+url[1227]+url[1228]+url[1229]+\
    url[1230]+url[1231]+url[1232]+url[1233]+url[1234]+url[1235]+url[1236]+url[1237]+url[1238]+url[1239]+url[1240]+url[1241]+url[1242]+url[1243]+url[1244]+url[1245]+url[1246]+url[1247]+url[1248]+url[1249]+url[1250]+url[1251]+url[1252]+url[1253]+url[1254]+url[1255]+url[1256]+url[1257]+url[1258]+url[1259]+url[1260]+url[1261]+url[1262]+url[1263]+url[1264]+url[1265]+url[1266]+url[1267]+url[1268]+url[1269]+url[1270]+url[1271]+url[1272]+url[1273]+url[1274]+url[1275]+url[1276]+url[1277]+url[1278]+url[1279]+url[1280]+url[1281]+url[1282]+url[1283]+url[1284]+url[1285]+url[1286]+url[1287]+url[1288]+url[1289]+url[1290]+url[1291]+url[1292]+url[1293]+url[1294]+url[1295]+url[1296]+url[1297]+url[1298]+url[1299]+url[1300]+url[1301]+url[1302]+url[1303]+url[1304]+url[1305]+url[1306]+url[1307]+url[1308]+url[1309]+url[1310]+url[1311]+url[1312]+url[1313]+url[1314]+url[1315]+url[1316]+url[1317]+url[1318]+url[1319]+url[1320]+url[1321]+url[1322]+url[1323]+url[1324]+url[1325]+url[1326]+url[1327]+url[1328]+url[1329]+url[1330]+\
    url[1331]+url[1332]+url[1333]+url[1334]+url[1335]+url[1336]+url[1337]+url[1338]+url[1339]+url[1340]+url[1341]+url[1342]+url[1343]+url[1344]+url[1345]+url[1346]+url[1347]+url[1348]+url[1349]+url[1350]+url[1351]+url[1352]+url[1353]+url[1354]+url[1355]+url[1356]+url[1357]+url[1358]+url[1359]+url[1360]+url[1361]+url[1362]+url[1363]+url[1364]+url[1365]+url[1366]+url[1367]+url[1368]+url[1369]+url[1370]+url[1371]+url[1372]+url[1373]+url[1374]+url[1375]+url[1376]+url[1377]+url[1378]+url[1379]+url[1380]+url[1381]+url[1382]+url[1383]+url[1384]+url[1385]+url[1386]+url[1387]+url[1388]+url[1389]+url[1390]+url[1391]+url[1392]+url[1393]+url[1394]+url[1395]+url[1396]+url[1397]+url[1398]+url[1399]+url[1400]+url[1401]+url[1402]+url[1403]+url[1404]+url[1405]+url[1406]+url[1407]+url[1408]+url[1409]+url[1410]+url[1411]+url[1412]+url[1413]+url[1414]+url[1415]+url[1416]+url[1417]+url[1418]+url[1419]+url[1420]+url[1421]+url[1422]+url[1423]+url[1424]+url[1425]+url[1426]+url[1427]+url[1428]+url[1429]+url[1430]+url[1431]+\
    url[1432]+url[1433]+url[1434]+url[1435]+url[1436]+url[1437]+url[1438]+url[1439]+url[1440]+url[1441]+url[1442]+url[1443]+url[1444]+url[1445]+url[1446]+url[1447]+url[1448]+url[1449]+url[1450]+url[1451]+url[1452]+url[1453]+url[1454]+url[1455]+url[1456]+url[1457]+url[1458]+url[1459]+url[1460]+url[1461]+url[1462]+url[1463]+url[1464]+url[1465]+url[1466]+url[1467]+url[1468]+url[1469]+url[1470]+url[1471]+url[1472]+url[1473]+url[1474]+url[1475]+url[1476]+url[1477]+url[1478]+url[1479]+url[1480]+url[1481]+url[1482]+url[1483]+url[1484]+url[1485]+url[1486]+url[1487]+url[1488]+url[1489]+url[1490]+url[1491]+url[1492]+url[1493]+url[1494]+url[1495]+url[1496]+url[1497]+url[1498]+url[1499]+url[1500]+url[1501]+url[1502]+url[1503]+url[1504]+url[1505]+url[1506]+url[1507]+url[1508]+url[1509]+url[1510]+url[1511]+url[1512]+url[1513]+url[1514]+url[1515]+url[1516]+url[1517]+url[1518]+url[1519]+url[1520]+url[1521]+url[1522]+url[1523]+url[1524]+url[1525]+url[1526]+url[1527]+url[1528]+url[1529]+url[1530]+url[1531]+url[1532]+\
    url[1533]+url[1534]+url[1535]+url[1536]+url[1537]+url[1538]+url[1539]+url[1540]+url[1541]+url[1542]+url[1543]+url[1544]+url[1545]+url[1546]+url[1547]+url[1548]+url[1549]+url[1550]+url[1551]+url[1552]+url[1553]+url[1554]+url[1555]+url[1556]+url[1557]+url[1558]+url[1559]+url[1560]+url[1561]+url[1562]+url[1563]+url[1564]+url[1565]+url[1566]+url[1567]+url[1568]+url[1569]+url[1570]+url[1571]+url[1572]+url[1573]+url[1574]+url[1575]+url[1576]+url[1577]+url[1578]+url[1579]+url[1580]+url[1581]+url[1582]+url[1583]+url[1584]+url[1585]+url[1586]+url[1587]+url[1588]+url[1589]+url[1590]+url[1591]+url[1592]+url[1593]+url[1594]+url[1595]+url[1596]+url[1597]+url[1598]+url[1599]+url[1600]+url[1601]+url[1602]+url[1603]+url[1604]+url[1605]+url[1606]+url[1607]+url[1608]+url[1609]+url[1610]+url[1611]+url[1612]+url[1613]+url[1614]+url[1615]+url[1616]+url[1617]+url[1618]+url[1619]+url[1620]+url[1621]+url[1622]+url[1623]+url[1624]+url[1625]+url[1626]+url[1627]+url[1628]+url[1629]+url[1630]+url[1631]+url[1632]+url[1633]+\
    url[1634]+url[1635]+url[1636]+url[1637]+url[1638]+url[1639]+url[1640]+url[1641]+url[1642]+url[1643]+url[1644]+url[1645]+url[1646]+url[1647]+url[1648]+url[1649]+url[1650]+url[1651]+url[1652]+url[1653]+url[1654]+url[1655]+url[1656]+url[1657]+url[1658]+url[1659]+url[1660]+url[1661]+url[1662]+url[1663]+url[1664]+url[1665]+url[1666]+url[1667]+url[1668]+url[1669]+url[1670]+url[1671]+url[1672]+url[1673]+url[1674]+url[1675]+url[1676]+url[1677]+url[1678]+url[1679]+url[1680]+url[1681]+url[1682]+url[1683]+url[1684]+url[1685]+url[1686]+url[1687]+url[1688]+url[1689]+url[1690]+url[1691]+url[1692]+url[1693]+url[1694]+url[1695]+url[1696]+url[1697]+url[1698]+url[1699]+url[1700]+url[1701]+url[1702]+url[1703]+url[1704]+url[1705]+url[1706]+url[1707]+url[1708]+url[1709]+url[1710]+url[1711]+url[1712]+url[1713]+url[1714]+url[1715]+url[1716]+url[1717]+url[1718]+url[1719]+url[1720]+url[1721]+url[1722]+url[1723]+url[1724]+url[1725]+url[1726]+url[1727]+url[1728]+url[1729]+url[1730]+url[1731]+url[1732]+url[1733]+url[1734]+\
    url[1735]+url[1736]+url[1737]+url[1738]+url[1739]+url[1740]+url[1741]+url[1742]+url[1743]+url[1744]+url[1745]+url[1746]+url[1747]+url[1748]+url[1749]+url[1750]+url[1751]+url[1752]+url[1753]+url[1754]+url[1755]+url[1756]+url[1757]+url[1758]+url[1759]+url[1760]+url[1761]+url[1762]+url[1763]+url[1764]+url[1765]+url[1766]+url[1767]+url[1768]+url[1769]+url[1770]+url[1771]+url[1772]+url[1773]+url[1774]+url[1775]+url[1776]+url[1777]+url[1778]+url[1779]+url[1780]+url[1781]+url[1782]+url[1783]+url[1784]+url[1785]+url[1786]+url[1787]+url[1788]+url[1789]+url[1790]+url[1791]+url[1792]+url[1793]+url[1794]+url[1795]+url[1796]+url[1797]+url[1798]+url[1799]+url[1800]+url[1801]+url[1802]+url[1803]+url[1804]+url[1805]+url[1806]+url[1807]+url[1808]+url[1809]+url[1810]+url[1811]+url[1812]+url[1813]+url[1814]+url[1815]+url[1816]+url[1817]+url[1818]+url[1819]+url[1820]+url[1821]+url[1822]+url[1823]+url[1824]+url[1825]+url[1826]+url[1827]+url[1828]+url[1829]+url[1830]+url[1831]+url[1832]+url[1833]+url[1834]+url[1835]+\
    url[1836]+url[1837]+url[1838]+url[1839]+url[1840]+url[1841]+url[1842]+url[1843]+url[1844]+url[1845]+url[1846]+url[1847]+url[1848]+url[1849]+url[1850]+url[1851]+url[1852]+url[1853]+url[1854]+url[1855]+url[1856]+url[1857]+url[1858]+url[1859]+url[1860]+url[1861]+url[1862]+url[1863]+url[1864]+url[1865]+url[1866]+url[1867]+url[1868]+url[1869]+url[1870]+url[1871]+url[1872]+url[1873]+url[1874]+url[1875]+url[1876]+url[1877]+url[1878]+url[1879]+url[1880]+url[1881]+url[1882]+url[1883]+url[1884]+url[1885]+url[1886]+url[1887]+url[1888]+url[1889]+url[1890]+url[1891]+url[1892]+url[1893]+url[1894]+url[1895]+url[1896]+url[1897]+url[1898]+url[1899]+url[1900]+url[1901]+url[1902]+url[1903]+url[1904]+url[1905]+url[1906]+url[1907]+url[1908]+url[1909]+url[1910]+url[1911]+url[1912]+url[1913]+url[1914]+url[1915]+url[1916]+url[1917]+url[1918]+url[1919]+url[1920]+url[1921]+url[1922]+url[1923]+url[1924]+url[1925]+url[1926]+url[1927]+url[1928]+url[1929]+url[1930]+url[1931]+url[1932]+url[1933]+url[1934]+url[1935]+url[1936]
  
    return Url
    return  False



class mOTVye():

 def mOTVgir(self,url):

    Url =url[1]+url[2]+url[3]+url[4]+url[5]+url[6]+url[7]+url[8]+url[9]+url[10]+url[11]+url[12]+url[13]+url[14]+url[15]+url[16]+url[17]+url[18]+url[19]+url[20]+url[21]+url[22]+url[23]+url[24]+url[25]+url[26]+url[27]+url[28]+url[29]+url[30]+url[31]+url[32]+url[33]+url[34]+url[35]+url[36]+url[37]+url[38]+url[39]+url[40]+url[41]+url[42]+url[43]+url[44]+url[45]+url[46]+url[47]+url[48]+url[49]+url[50]+url[51]+url[52]+url[53]+url[54]+url[55]+url[56]+url[57]+url[58]+url[59]+url[60]+url[61]+url[62]+url[63]+url[64]+url[65]+url[66]+url[67]+url[68]+url[69]+url[70]+url[71]+url[72]+url[73]+url[74]+url[75]+url[76]+url[77]+url[78]+url[79]+url[80]+url[81]+url[82]+url[83]+url[84]+url[85]+url[86]+url[87]+url[88]+url[89]+url[90]+url[91]+url[92]+url[93]+url[94]+url[95]+url[96]+url[97]+url[98]+url[99]+url[100]+url[101]+url[102]+url[103]+url[104]+url[105]+url[106]+url[107]+url[108]+url[109]+url[110]+url[111]+url[112]+url[113]+url[114]+url[115]+url[116]+url[117]+url[118]+url[119]+url[120]+url[121]+url[122]+url[123]+url[124]+\
    url[125]+\
    url[126]+url[127]+url[128]+url[129]+url[130]+url[131]+url[132]+url[133]+url[134]+url[135]+url[136]+url[137]+url[138]+url[139]+url[140]+url[141]+url[142]+url[143]+url[144]+url[145]+url[146]+url[147]+url[148]+url[149]+url[150]+url[151]+url[152]+url[153]+url[154]+url[155]+url[156]+url[157]+url[158]+url[159]+url[160]+url[161]+url[162]+url[163]+url[164]+url[165]+url[166]+url[167]+url[168]+url[169]+url[170]+url[171]+url[172]+url[173]+url[174]+url[175]+url[176]+url[177]+url[178]+url[179]+url[180]+url[181]+url[182]+url[183]+url[184]+url[185]+url[186]+url[187]+url[188]+url[189]+url[190]+url[191]+url[192]+url[193]+url[194]+url[195]+url[196]+url[197]+url[198]+url[199]+url[200]+url[201]+url[202]+url[203]+url[204]+url[205]+url[206]+url[207]+url[208]+url[209]+url[210]+url[211]+url[212]+url[213]+url[214]+url[215]+url[216]+url[217]+url[218]+url[219]+url[220]+url[221]+url[222]+url[223]+url[224]+url[225]+url[226]+url[227]+url[228]+url[229]+url[230]+url[231]+url[232]+url[233]+url[234]+url[235]+url[236]+url[237]+url[238]+\
    url[239]+url[240]+url[241]+url[242]+url[243]+url[244]+url[245]+url[246]+url[247]+url[248]+url[249]+url[250]+url[251]+url[252]+url[253]+url[254]+url[255]+url[256]+url[257]+url[258]+url[259]+url[260]+url[261]+url[262]+url[263]+url[264]+url[265]+url[266]+url[267]+url[268]+url[269]+url[270]+url[271]+url[272]+url[273]+url[274]+url[275]+url[276]+url[277]+url[278]+url[279]+url[280]+url[281]+url[282]+url[283]+url[284]+url[285]+url[286]+url[287]+url[288]+url[289]+url[290]+url[291]+url[292]+url[293]+url[294]+url[295]+url[296]+url[297]+url[298]+url[299]+url[300]+url[301]+url[302]+url[303]+url[304]+url[305]+url[306]+url[307]+url[308]+url[309]+url[310]+url[311]+url[312]+url[313]+url[314]+url[315]+url[316]+url[317]+url[318]+url[319]+url[320]+url[321]+url[322]+url[323]+url[324]+url[325]+url[326]+url[327]+url[328]+url[329]+url[330]+url[331]+url[332]+url[333]+url[334]+url[335]+url[336]+url[337]+url[338]+url[339]+url[340]+url[341]+url[342]+url[343]+url[344]+url[345]+url[346]+url[347]+url[348]+url[349]+url[350]+url[351]+\
    url[352]+url[353]+url[354]+url[355]+url[356]+url[357]+url[358]+url[359]+url[360]+url[361]+url[362]+url[363]+url[364]+url[365]+url[366]+url[367]+url[368]+url[369]+url[370]+url[371]+url[372]+url[373]+url[374]+url[375]+url[376]+url[377]+url[378]+url[379]+url[380]+url[381]+url[382]+url[383]+url[384]+url[385]+url[386]+url[387]+url[388]+url[389]+url[390]+url[391]+url[392]+url[393]+url[394]+url[395]+url[396]+url[397]+url[398]+url[399]+url[400]+url[401]+url[402]+url[403]+url[404]+url[405]+url[406]+url[407]+url[408]+url[409]+url[410]+url[411]+url[412]+url[413]+url[414]+url[415]+url[416]+url[417]+url[418]+url[419]+url[420]+url[421]+url[422]+url[423]+url[424]+url[425]+url[426]+url[427]+url[428]+url[429]+url[430]+url[431]+url[432]+url[433]+url[434]+url[435]+url[436]+url[437]+url[438]+url[439]+url[440]+url[441]+url[442]+url[443]+url[444]+url[445]+url[446]+url[447]+url[448]+url[449]+url[450]+url[451]+url[452]+url[453]+url[454]+url[455]+url[456]+url[457]+url[458]+url[459]+url[460]+url[461]+url[462]+url[463]+url[464]+\
    url[465]+url[466]+url[467]+url[468]+url[469]+url[470]+url[471]+url[472]+url[473]+url[474]+url[475]+url[476]+url[477]+url[478]+url[479]+url[480]+url[481]+url[482]+url[483]+url[484]+url[485]+url[486]+url[487]+url[488]+url[489]+url[490]+url[491]+url[492]+url[493]+url[494]+url[495]+url[496]+url[497]+url[498]+url[499]+url[500]+url[501]+url[502]+url[503]+url[504]+url[505]+url[506]+url[507]+url[508]+url[509]+url[510]+url[511]+url[512]+url[513]+url[514]+url[515]+url[516]+url[517]+url[518]+url[519]+url[520]+url[521]+url[522]+url[523]+url[524]+url[525]+url[526]+url[527]+url[528]+url[529]+url[530]+url[531]+url[532]+url[533]+url[534]+url[535]+url[536]+url[537]+url[538]+url[539]+url[540]+url[541]+url[542]+url[543]+url[544]+url[545]+url[546]+url[547]+url[548]+url[549]+url[550]+url[551]+url[552]+url[553]+url[554]+url[555]+url[556]+url[557]+url[558]+url[559]+url[560]+url[561]+url[562]+url[563]+url[564]+url[565]+url[566]+url[567]+url[568]+url[569]+url[570]+url[571]+url[572]+url[573]+url[574]+url[575]+url[576]+url[577]+\
    url[578]+url[579]+url[580]+url[581]+url[582]+url[583]+url[584]+url[585]+url[586]+url[587]+url[588]+url[589]+url[590]+url[591]+url[592]+url[593]+url[594]+url[595]+url[596]+url[597]+url[598]+url[599]+url[600]+url[601]+url[602]+url[603]+url[604]+url[605]+url[606]+url[607]+url[608]+url[609]+url[610]+url[611]+url[612]+url[613]+url[614]+url[615]+url[616]+url[617]+url[618]+url[619]+url[620]+url[621]+url[622]+url[623]+url[624]+url[625]+url[626]+url[627]+url[628]+url[629]+url[630]+url[631]+url[632]+url[633]+url[634]+url[635]+url[636]+url[637]+url[638]+url[639]+url[640]+url[641]+url[642]+url[643]+url[644]+url[645]+url[646]+url[647]+url[648]+url[649]+url[650]+url[651]+url[652]+url[653]+url[654]+url[655]+url[656]+url[657]+url[658]+url[659]+url[660]+url[661]+url[662]+url[663]+url[664]+url[665]+url[666]+url[667]+url[668]+url[669]+url[670]+url[671]+url[672]+url[673]+url[674]+url[675]+url[676]+url[677]+url[678]+url[679]+url[680]+url[681]+url[682]+url[683]+url[684]+url[685]+url[686]+url[687]+url[688]+url[689]+url[690]+\
    url[691]+url[692]+url[693]+url[694]+url[695]+url[696]+url[697]+url[698]+url[699]+url[700]+url[701]+url[702]+url[703]+url[704]+url[705]+url[706]+url[707]+url[708]+url[709]+url[710]+url[711]+url[712]+url[713]+url[714]+url[715]+url[716]+url[717]+url[718]+url[719]+url[720]+url[721]+url[722]+url[723]+url[724]+url[725]+url[726]+url[727]+url[728]+url[729]+url[730]+url[731]+url[732]+url[733]+url[734]+url[735]+url[736]+url[737]+url[738]+url[739]+url[740]+url[741]+url[742]+url[743]+url[744]+url[745]+url[746]+url[747]+url[748]+url[749]+url[750]+url[751]+url[752]+url[753]+url[754]+url[755]+url[756]+url[757]+url[758]+url[759]+url[760]+url[761]+url[762]+url[763]+url[764]+url[765]+url[766]+url[767]+url[768]+url[769]+url[770]+url[771]+url[772]+url[773]+url[774]+url[775]+url[776]+url[777]+url[778]+url[779]+url[780]+url[781]+url[782]+url[783]+url[784]+url[785]+url[786]+url[787]+url[788]+url[789]+url[790]+url[791]+url[792]+url[793]+url[794]+url[795]+url[796]+url[797]+url[798]+url[799]+url[800]+url[801]+url[802]+url[803]+\
    url[804]+url[805]+url[806]+url[807]+url[808]+url[809]+url[810]+url[811]+url[812]+url[813]+url[814]+url[815]+url[816]+url[817]+url[818]+url[819]+url[820]+url[821]+url[822]+url[823]+url[824]+url[825]+url[826]+url[827]+url[828]+url[829]+url[830]+url[831]+url[832]+url[833]+url[834]+url[835]+url[836]+url[837]+url[838]+url[839]+url[840]+url[841]+url[842]+url[843]+url[844]+url[845]+url[846]+url[847]+url[848]+url[849]+url[850]+url[851]+url[852]+url[853]+url[854]+url[855]+url[856]+url[857]+url[858]+url[859]+url[860]+url[861]+url[862]+url[863]+url[864]+url[865]+url[866]+url[867]+url[868]+url[869]+url[870]+url[871]+url[872]+url[873]+url[874]+url[875]+url[876]+url[877]+url[878]+url[879]+url[880]+url[881]+url[882]+url[883]+url[884]+url[885]+url[886]+url[887]+url[888]+url[889]+url[890]+url[891]+url[892]+url[893]+url[894]+url[895]+url[896]+url[897]+url[898]+url[899]+url[900]+url[901]+url[902]+url[903]+url[904]+url[905]+url[906]+url[907]+url[908]+url[909]+url[910]+url[911]+url[912]+url[913]+url[914]+url[915]+url[916]+\
    url[917]+url[918]+url[919]+url[920]+url[921]+url[922]+url[923]+url[924]+url[925]+url[926]+url[927]+url[928]+url[929]+url[930]+url[931]+url[932]+url[933]+url[934]+url[935]+url[936]+url[937]+url[938]+url[939]+url[940]+url[941]+url[942]+url[943]+url[944]+url[945]+url[946]+url[947]+url[948]+url[949]+url[950]+url[951]+url[952]+url[953]+url[954]+url[955]+url[956]+url[957]+url[958]+url[959]+url[960]+url[961]+url[962]+url[963]+url[964]+url[965]+url[966]+url[967]+url[968]+url[969]+url[970]+url[971]+url[972]+url[973]+url[974]+url[975]+url[976]+url[977]+url[978]+url[979]+url[980]+url[981]+url[982]+url[983]+url[984]+url[985]+url[986]+url[987]+url[988]+url[989]+url[990]+url[991]+url[992]+url[993]+url[994]+url[995]+url[996]+url[997]+url[998]+url[999]+url[1000]+url[1001]+url[1002]+url[1003]+url[1004]+url[1005]+url[1006]+url[1007]+url[1008]+url[1009]+url[1010]+url[1011]+url[1012]+url[1013]+url[1014]+url[1015]+url[1016]+url[1017]+url[1018]+url[1019]+url[1020]+url[1021]+url[1022]+url[1023]+url[1024]+url[1025]+url[1026]+\
    url[1027]+url[1028]+url[1029]+url[1030]+url[1031]+url[1032]+url[1033]+url[1034]+url[1035]+url[1036]+url[1037]+url[1038]+url[1039]+url[1040]+url[1041]+url[1042]+url[1043]+url[1044]+url[1045]+url[1046]+url[1047]+url[1048]+url[1049]+url[1050]+url[1051]+url[1052]+url[1053]+url[1054]+url[1055]+url[1056]+url[1057]+url[1058]+url[1059]+url[1060]+url[1061]+url[1062]+url[1063]+url[1064]+url[1065]+url[1066]+url[1067]+url[1068]+url[1069]+url[1070]+url[1071]+url[1072]+url[1073]+url[1074]+url[1075]+url[1076]+url[1077]+url[1078]+url[1079]+url[1080]+url[1081]+url[1082]+url[1083]+url[1084]+url[1085]+url[1086]+url[1087]+url[1088]+url[1089]+url[1090]+url[1091]+url[1092]+url[1093]+url[1094]+url[1095]+url[1096]+url[1097]+url[1098]+url[1099]+url[1100]+url[1101]+url[1102]+url[1103]+url[1104]+url[1105]+url[1106]+url[1107]+url[1108]+url[1109]+url[1110]+url[1111]+url[1112]+url[1113]+url[1114]+url[1115]+url[1116]+url[1117]+url[1118]+url[1119]+url[1120]+url[1121]+url[1122]+url[1123]+url[1124]+url[1125]+url[1126]+url[1127]+\
    url[1128]+url[1129]+url[1130]+url[1131]+url[1132]+url[1133]+url[1134]+url[1135]+url[1136]+url[1137]+url[1138]+url[1139]+url[1140]+url[1141]+url[1142]+url[1143]+url[1144]+url[1145]+url[1146]+url[1147]+url[1148]+url[1149]+url[1150]+url[1151]+url[1152]+url[1153]+url[1154]+url[1155]+url[1156]+url[1157]+url[1158]+url[1159]+url[1160]+url[1161]+url[1162]+url[1163]+url[1164]+url[1165]+url[1166]+url[1167]+url[1168]+url[1169]+url[1170]+url[1171]+url[1172]+url[1173]+url[1174]+url[1175]+url[1176]+url[1177]+url[1178]+url[1179]+url[1180]+url[1181]+url[1182]+url[1183]+url[1184]+url[1185]+url[1186]+url[1187]+url[1188]+url[1189]+url[1190]+url[1191]+url[1192]+url[1193]+url[1194]+url[1195]+url[1196]+url[1197]+url[1198]+url[1199]+url[1200]+url[1201]+url[1202]+url[1203]+url[1204]+url[1205]+url[1206]+url[1207]+url[1208]+url[1209]+url[1210]+url[1211]+url[1212]+url[1213]+url[1214]+url[1215]+url[1216]+url[1217]+url[1218]+url[1219]+url[1220]+url[1221]+url[1222]+url[1223]+url[1224]+url[1225]+url[1226]+url[1227]+url[1228]+url[1229]+\
    url[1230]+url[1231]+url[1232]+url[1233]+url[1234]+url[1235]+url[1236]+url[1237]+url[1238]+url[1239]+url[1240]+url[1241]+url[1242]+url[1243]+url[1244]+url[1245]+url[1246]+url[1247]+url[1248]+url[1249]+url[1250]+url[1251]+url[1252]+url[1253]+url[1254]+url[1255]+url[1256]+url[1257]+url[1258]+url[1259]+url[1260]+url[1261]+url[1262]+url[1263]+url[1264]+url[1265]+url[1266]+url[1267]+url[1268]+url[1269]+url[1270]+url[1271]+url[1272]+url[1273]+url[1274]+url[1275]+url[1276]+url[1277]+url[1278]+url[1279]+url[1280]+url[1281]+url[1282]+url[1283]+url[1284]+url[1285]+url[1286]+url[1287]+url[1288]+url[1289]+url[1290]+url[1291]+url[1292]+url[1293]+url[1294]+url[1295]+url[1296]+url[1297]+url[1298]+url[1299]+url[1300]+url[1301]+url[1302]+url[1303]+url[1304]+url[1305]+url[1306]+url[1307]+url[1308]+url[1309]+url[1310]+url[1311]+url[1312]+url[1313]+url[1314]+url[1315]+url[1316]+url[1317]+url[1318]+url[1319]+url[1320]+url[1321]+url[1322]+url[1323]+url[1324]+url[1325]+url[1326]+url[1327]+url[1328]+url[1329]+url[1330]+\
    url[1331]+url[1332]+url[1333]+url[1334]+url[1335]+url[1336]+url[1337]+url[1338]+url[1339]+url[1340]+url[1341]+url[1342]+url[1343]+url[1344]+url[1345]+url[1346]+url[1347]+url[1348]+url[1349]+url[1350]+url[1351]+url[1352]+url[1353]+url[1354]+url[1355]+url[1356]+url[1357]+url[1358]+url[1359]+url[1360]+url[1361]+url[1362]+url[1363]+url[1364]+url[1365]+url[1366]+url[1367]+url[1368]+url[1369]+url[1370]+url[1371]+url[1372]+url[1373]+url[1374]+url[1375]+url[1376]+url[1377]+url[1378]+url[1379]+url[1380]+url[1381]+url[1382]+url[1383]+url[1384]+url[1385]+url[1386]+url[1387]+url[1388]+url[1389]+url[1390]+url[1391]+url[1392]+url[1393]+url[1394]+url[1395]+url[1396]+url[1397]+url[1398]+url[1399]+url[1400]+url[1401]+url[1402]+url[1403]+url[1404]+url[1405]+url[1406]+url[1407]+url[1408]+url[1409]+url[1410]+url[1411]+url[1412]+url[1413]+url[1414]+url[1415]+url[1416]+url[1417]+url[1418]+url[1419]+url[1420]+url[1421]+url[1422]+url[1423]+url[1424]+url[1425]+url[1426]+url[1427]+url[1428]+url[1429]+url[1430]+url[1431]+\
    url[1432]+url[1433]+url[1434]+url[1435]+url[1436]+url[1437]+url[1438]+url[1439]+url[1440]+url[1441]+url[1442]+url[1443]+url[1444]+url[1445]+url[1446]+url[1447]+url[1448]+url[1449]+url[1450]+url[1451]+url[1452]+url[1453]+url[1454]+url[1455]+url[1456]+url[1457]+url[1458]+url[1459]+url[1460]+url[1461]+url[1462]+url[1463]+url[1464]+url[1465]+url[1466]+url[1467]+url[1468]+url[1469]+url[1470]+url[1471]+url[1472]+url[1473]+url[1474]+url[1475]+url[1476]+url[1477]+url[1478]+url[1479]+url[1480]+url[1481]+url[1482]+url[1483]+url[1484]+url[1485]+url[1486]+url[1487]+url[1488]+url[1489]+url[1490]+url[1491]+url[1492]+url[1493]+url[1494]+url[1495]+url[1496]+url[1497]+url[1498]+url[1499]+url[1500]+url[1501]+url[1502]+url[1503]+url[1504]+url[1505]+url[1506]+url[1507]+url[1508]+url[1509]+url[1510]+url[1511]+url[1512]+url[1513]+url[1514]+url[1515]+url[1516]+url[1517]+url[1518]+url[1519]+url[1520]+url[1521]+url[1522]+url[1523]+url[1524]+url[1525]+url[1526]+url[1527]+url[1528]+url[1529]+url[1530]+url[1531]+url[1532]+\
    url[1533]+url[1534]+url[1535]+url[1536]+url[1537]+url[1538]+url[1539]+url[1540]+url[1541]+url[1542]+url[1543]+url[1544]+url[1545]+url[1546]+url[1547]+url[1548]+url[1549]+url[1550]+url[1551]+url[1552]+url[1553]+url[1554]+url[1555]+url[1556]+url[1557]+url[1558]+url[1559]+url[1560]+url[1561]+url[1562]+url[1563]+url[1564]+url[1565]+url[1566]+url[1567]+url[1568]+url[1569]+url[1570]+url[1571]+url[1572]+url[1573]+url[1574]+url[1575]+url[1576]+url[1577]+url[1578]+url[1579]+url[1580]+url[1581]+url[1582]+url[1583]+url[1584]+url[1585]+url[1586]+url[1587]+url[1588]+url[1589]+url[1590]+url[1591]+url[1592]+url[1593]+url[1594]+url[1595]+url[1596]+url[1597]+url[1598]+url[1599]+url[1600]+url[1601]+url[1602]+url[1603]+url[1604]+url[1605]+url[1606]+url[1607]+url[1608]+url[1609]+url[1610]+url[1611]+url[1612]+url[1613]+url[1614]+url[1615]+url[1616]+url[1617]+url[1618]+url[1619]+url[1620]+url[1621]+url[1622]+url[1623]+url[1624]+url[1625]+url[1626]+url[1627]+url[1628]+url[1629]+url[1630]+url[1631]+url[1632]+url[1633]+\
    url[1634]+url[1635]+url[1636]+url[1637]+url[1638]+url[1639]+url[1640]+url[1641]+url[1642]+url[1643]+url[1644]+url[1645]+url[1646]+url[1647]+url[1648]+url[1649]+url[1650]+url[1651]+url[1652]+url[1653]+url[1654]+url[1655]+url[1656]+url[1657]+url[1658]+url[1659]+url[1660]+url[1661]+url[1662]+url[1663]+url[1664]+url[1665]+url[1666]+url[1667]+url[1668]+url[1669]+url[1670]+url[1671]+url[1672]+url[1673]+url[1674]+url[1675]+url[1676]+url[1677]+url[1678]+url[1679]+url[1680]+url[1681]+url[1682]+url[1683]+url[1684]+url[1685]+url[1686]+url[1687]+url[1688]+url[1689]+url[1690]+url[1691]+url[1692]+url[1693]+url[1694]+url[1695]+url[1696]+url[1697]+url[1698]+url[1699]+url[1700]+url[1701]+url[1702]+url[1703]+url[1704]+url[1705]+url[1706]+url[1707]+url[1708]+url[1709]+url[1710]+url[1711]+url[1712]+url[1713]+url[1714]+url[1715]+url[1716]+url[1717]+url[1718]+url[1719]+url[1720]+url[1721]+url[1722]+url[1723]+url[1724]+url[1725]+url[1726]+url[1727]+url[1728]+url[1729]+url[1730]+url[1731]+url[1732]+url[1733]+url[1734]+\
    url[1735]+url[1736]+url[1737]+url[1738]+url[1739]+url[1740]+url[1741]+url[1742]+url[1743]+url[1744]+url[1745]+url[1746]+url[1747]+url[1748]+url[1749]+url[1750]+url[1751]+url[1752]+url[1753]+url[1754]+url[1755]+url[1756]+url[1757]+url[1758]+url[1759]+url[1760]+url[1761]+url[1762]+url[1763]+url[1764]+url[1765]+url[1766]+url[1767]+url[1768]+url[1769]+url[1770]+url[1771]+url[1772]+url[1773]+url[1774]+url[1775]+url[1776]+url[1777]+url[1778]+url[1779]+url[1780]+url[1781]+url[1782]+url[1783]+url[1784]+url[1785]+url[1786]+url[1787]+url[1788]+url[1789]+url[1790]+url[1791]+url[1792]+url[1793]+url[1794]+url[1795]+url[1796]+url[1797]+url[1798]+url[1799]+url[1800]+url[1801]+url[1802]+url[1803]+url[1804]+url[1805]+url[1806]+url[1807]+url[1808]+url[1809]+url[1810]+url[1811]+url[1812]+url[1813]+url[1814]+url[1815]+url[1816]+url[1817]+url[1818]+url[1819]+url[1820]+url[1821]+url[1822]+url[1823]+url[1824]+url[1825]+url[1826]+url[1827]+url[1828]+url[1829]+url[1830]+url[1831]+url[1832]+url[1833]+url[1834]+url[1835]+\
    url[1836]+url[1837]+url[1838]+url[1839]+url[1840]+url[1841]+url[1842]+url[1843]+url[1844]+url[1845]+url[1846]+url[1847]+url[1848]+url[1849]+url[1850]+url[1851]+url[1852]+url[1853]+url[1854]+url[1855]+url[1856]+url[1857]+url[1858]+url[1859]+url[1860]+url[1861]+url[1862]+url[1863]+url[1864]+url[1865]+url[1866]+url[1867]+url[1868]+url[1869]+url[1870]+url[1871]+url[1872]+url[1873]+url[1874]+url[1875]+url[1876]+url[1877]+url[1878]+url[1879]+url[1880]+url[1881]+url[1882]+url[1883]+url[1884]+url[1885]+url[1886]+url[1887]+url[1888]+url[1889]+url[1890]+url[1891]+url[1892]+url[1893]+url[1894]+url[1895]+url[1896]+url[1897]+url[1898]+url[1899]+url[1900]+url[1901]+url[1902]+url[1903]+url[1904]+url[1905]+url[1906]+url[1907]+url[1908]+url[1909]+url[1910]+url[1911]+url[1912]+url[1913]+url[1914]+url[1915]+url[1916]+url[1917]+url[1918]+url[1919]+url[1920]+url[1921]+url[1922]+url[1923]+url[1924]+url[1925]+url[1926]+url[1927]+url[1928]+url[1929]+url[1930]+url[1931]+url[1932]+url[1933]+url[1934]+url[1935]+url[1936]+\
    url[1937]+url[1938]+url[1939]+url[1940]+url[1941]+url[1942]+url[1943]+url[1944]+url[1945]+url[1946]+url[1947]+url[1948]+url[1949]+url[1950]+url[1951]+url[1952]+url[1953]+url[1954]+url[1955]+url[1956]+url[1957]+url[1958]+url[1959]+url[1960]+url[1961]+url[1962]+url[1963]+url[1964]+url[1965]+url[1966]+url[1967]+url[1968]+url[1969]+url[1970]+url[1971]+url[1972]+url[1973]+url[1974]+url[1975]+url[1976]+url[1977]+url[1978]+url[1979]+url[1980]+url[1981]+url[1982]+url[1983]+url[1984]+url[1985]+url[1986]+url[1987]+url[1988]+url[1989]+url[1990]+url[1991]+url[1992]+url[1993]+url[1994]+url[1995]+url[1996]+url[1997]+url[1998]+url[1999]+url[2000]+url[2001]+url[2002]+url[2003]+url[2004]+url[2005]+url[2006]+url[2007]+url[2008]+url[2009]+url[2010]+url[2011]+url[2012]+url[2013]+url[2014]+url[2015]+url[2016]+url[2017]+url[2018]+url[2019]+url[2020]+url[2021]+url[2022]+url[2023]+url[2024]+url[2025]+url[2026]+url[2027]+url[2028]+url[2029]+url[2030]+url[2031]+url[2032]+url[2033]+url[2034]+url[2035]+url[2036]+url[2037]+\
    url[2038]+url[2039]+url[2040]+url[2041]+url[2042]+url[2043]+url[2044]+url[2045]+url[2046]+url[2047]+url[2048]+url[2049]+url[2050]+url[2051]+url[2052]+url[2053]+url[2054]+url[2055]+url[2056]+url[2057]+url[2058]+url[2059]+url[2060]+url[2061]+url[2062]+url[2063]+url[2064]+url[2065]+url[2066]+url[2067]+url[2068]+url[2069]+url[2070]+url[2071]+url[2072]+url[2073]+url[2074]+url[2075]+url[2076]+url[2077]+url[2078]+url[2079]+url[2080]+url[2081]+url[2082]+url[2083]+url[2084]+url[2085]+url[2086]+url[2087]+url[2088]+url[2089]+url[2090]+url[2091]+url[2092]+url[2093]+url[2094]+url[2095]+url[2096]+url[2097]+url[2098]+url[2099]+url[2100]+url[2101]+url[2102]+url[2103]+url[2104]+url[2105]+url[2106]+url[2107]+url[2108]+url[2109]+url[2110]+url[2111]+url[2112]+url[2113]+url[2114]+url[2115]+url[2116]+url[2117]+url[2118]+url[2119]+url[2120]+url[2121]+url[2122]+url[2123]+url[2124]+url[2125]+url[2126]+url[2127]+url[2128]+url[2129]+url[2130]+url[2131]+url[2132]+url[2133]+url[2134]+url[2135]+url[2136]+url[2137]+url[2138]+\
    url[2139]+url[2140]+url[2141]+url[2142]+url[2143]+url[2144]+url[2145]+url[2146]+url[2147]+url[2148]+url[2149]+url[2150]+url[2151]+url[2152]+url[2153]+url[2154]+url[2155]+url[2156]+url[2157]+url[2158]+url[2159]+url[2160]+url[2161]+url[2162]+url[2163]+url[2164]+url[2165]+url[2166]+url[2167]+url[2168]+url[2169]+url[2170]+url[2171]+url[2172]+url[2173]+url[2174]+url[2175]+url[2176]+url[2177]+url[2178]+url[2179]+url[2180]+url[2181]+url[2182]+url[2183]+url[2184]+url[2185]+url[2186]+url[2187]+url[2188]+url[2189]+url[2190]+url[2191]+url[2192]+url[2193]+url[2194]+url[2195]+url[2196]+url[2197]+url[2198]+url[2199]+url[2200]+url[2201]+url[2202]+url[2203]+url[2204]+url[2205]+url[2206]+url[2207]+url[2208]+url[2209]+url[2210]+url[2211]+url[2212]+url[2213]+url[2214]+url[2215]+url[2216]+url[2217]+url[2218]+url[2219]+url[2220]+url[2221]+url[2222]+url[2223]+url[2224]+url[2225]+url[2226]+url[2227]+url[2228]+url[2229]+url[2230]+url[2231]+url[2232]+url[2233]+url[2234]+url[2235]+url[2236]+url[2237]+url[2238]+url[2239]+\
    url[2240]+url[2241]+url[2242]+url[2243]+url[2244]+url[2245]+url[2246]+url[2247]+url[2248]+url[2249]+url[2250]+url[2251]+url[2252]+url[2253]+url[2254]+url[2255]+url[2256]+url[2257]+url[2258]+url[2259]+url[2260]+url[2261]+url[2262]+url[2263]+url[2264]+url[2265]+url[2266]+url[2267]+url[2268]+url[2269]+url[2270]+url[2271]+url[2272]+url[2273]+url[2274]+url[2275]+url[2276]+url[2277]+url[2278]+url[2279]+url[2280]+url[2281]+url[2282]+url[2283]+url[2284]+url[2285]+url[2286]+url[2287]+url[2288]+url[2289]+url[2290]+url[2291]+url[2292]+url[2293]+url[2294]+url[2295]+url[2296]+url[2297]+url[2298]+url[2299]+url[2300]+url[2301]+url[2302]+url[2303]+url[2304]+url[2305]+url[2306]+url[2307]+url[2308]+url[2309]+url[2310]+url[2311]+url[2312]+url[2313]+url[2314]+url[2315]+url[2316]+url[2317]+url[2318]+url[2319]+url[2320]+url[2321]+url[2322]+url[2323]+url[2324]+url[2325]+url[2326]+url[2327]+url[2328]+url[2329]+url[2330]+url[2331]+url[2332]+url[2333]+url[2334]+url[2335]+url[2336]+url[2337]+url[2338]+url[2339]+url[2340]+\
    url[2341]+url[2342]+url[2343]+url[2344]+url[2345]+url[2346]+url[2347]+url[2348]+url[2349]+url[2350]+url[2351]+url[2352]+url[2353]+url[2354]+url[2355]+url[2356]+url[2357]+url[2358]+url[2359]+url[2360]+url[2361]+url[2362]+url[2363]+url[2364]+url[2365]+url[2366]+url[2367]+url[2368]+url[2369]+url[2370]+url[2371]+url[2372]+url[2373]+url[2374]+url[2375]+url[2376]+url[2377]+url[2378]+url[2379]+url[2380]+url[2381]+url[2382]+url[2383]+url[2384]+url[2385]+url[2386]+url[2387]+url[2388]+url[2389]+url[2390]+url[2391]+url[2392]+url[2393]+url[2394]+url[2395]+url[2396]+url[2397]+url[2398]+url[2399]+url[2400]+url[2401]+url[2402]+url[2403]+url[2404]+url[2405]+url[2406]+url[2407]+url[2408]+url[2409]+url[2410]+url[2411]+url[2412]+url[2413]+url[2414]+url[2415]+url[2416]+url[2417]+url[2418]+url[2419]+url[2420]+url[2421]+url[2422]+url[2423]+url[2424]+url[2425]+url[2426]+url[2427]+url[2428]+url[2429]+url[2430]+url[2431]+url[2432]+url[2433]+url[2434]+url[2435]+url[2436]+url[2437]+url[2438]+url[2439]+url[2440]+url[2441]+\
    url[2442]+url[2443]+url[2444]+url[2445]+url[2446]+url[2447]+url[2448]+url[2449]+url[2450]+url[2451]+url[2452]+url[2453]+url[2454]+url[2455]+url[2456]+url[2457]+url[2458]+url[2459]+url[2460]+url[2461]+url[2462]+url[2463]+url[2464]+url[2465]+url[2466]+url[2467]+url[2468]+url[2469]+url[2470]+url[2471]+url[2472]+url[2473]+url[2474]+url[2475]+url[2476]+url[2477]+url[2478]+url[2479]+url[2480]+url[2481]+url[2482]+url[2483]+url[2484]+url[2485]+url[2486]+url[2487]+url[2488]+url[2489]+url[2490]+url[2491]+url[2492]+url[2493]+url[2494]+url[2495]+url[2496]+url[2497]+url[2498]+url[2499]+url[2500]+url[2501]+url[2502]+url[2503]+url[2504]+url[2505]+url[2506]+url[2507]+url[2508]+url[2509]+url[2510]+url[2511]+url[2512]+url[2513]+url[2514]+url[2515]+url[2516]+url[2517]+url[2518]+url[2519]+url[2520]+url[2521]+url[2522]+url[2523]+url[2524]+url[2525]+url[2526]+url[2527]+url[2528]+url[2529]+url[2530]+url[2531]+url[2532]+url[2533]+url[2534]+url[2535]+url[2536]+url[2537]+url[2538]+url[2539]+url[2540]+url[2541]+url[2542]+\
    url[2543]+url[2544]+url[2545]+url[2546]+url[2547]+url[2548]+url[2549]+url[2550]+url[2551]+url[2552]+url[2553]+url[2554]+url[2555]+url[2556]+url[2557]+url[2558]+url[2559]+url[2560]+url[2561]+url[2562]+url[2563]+url[2564]+url[2565]+url[2566]+url[2567]+url[2568]+url[2569]+url[2570]+url[2571]+url[2572]+url[2573]+url[2574]+url[2575]+url[2576]+url[2577]+url[2578]+url[2579]+url[2580]+url[2581]+url[2582]+url[2583]+url[2584]+url[2585]+url[2586]+url[2587]+url[2588]+url[2589]+url[2590]+url[2591]+url[2592]+url[2593]+url[2594]+url[2595]+url[2596]+url[2597]+url[2598]+url[2599]+url[2600]+url[2601]+url[2602]+url[2603]+url[2604]+url[2605]+url[2606]+url[2607]+url[2608]+url[2609]+url[2610]+url[2611]+url[2612]+url[2613]+url[2614]+url[2615]+url[2616]+url[2617]+url[2618]+url[2619]+url[2620]+url[2621]+url[2622]+url[2623]+url[2624]+url[2625]+url[2626]+url[2627]+url[2628]+url[2629]+url[2630]+url[2631]+url[2632]+url[2633]+url[2634]+url[2635]+url[2636]+url[2637]+url[2638]+url[2639]+url[2640]+url[2641]+url[2642]+url[2643]+\
    url[2644]+url[2645]+url[2646]+url[2647]+url[2648]+url[2649]+url[2650]+url[2651]+url[2652]+url[2653]+url[2654]+url[2655]+url[2656]+url[2657]+url[2658]+url[2659]+url[2660]+url[2661]+url[2662]+url[2663]+url[2664]+url[2665]+url[2666]+url[2667]+url[2668]+url[2669]+url[2670]+url[2671]+url[2672]+url[2673]+url[2674]+url[2675]+url[2676]+url[2677]+url[2678]+url[2679]+url[2680]+url[2681]+url[2682]+url[2683]+url[2684]+url[2685]+url[2686]+url[2687]+url[2688]+url[2689]+url[2690]+url[2691]+url[2692]+url[2693]+url[2694]+url[2695]+url[2696]+url[2697]+url[2698]+url[2699]+url[2700]+url[2701]+url[2702]+url[2703]+url[2704]+url[2705]+url[2706]+url[2707]+url[2708]+url[2709]+url[2710]+url[2711]+url[2712]+url[2713]+url[2714]+url[2715]+url[2716]+url[2717]+url[2718]+url[2719]+url[2720]+url[2721]+url[2722]+url[2723]+url[2724]+url[2725]+url[2726]+url[2727]+url[2728]+url[2729]+url[2730]+url[2731]+url[2732]+url[2733]+url[2734]+url[2735]+url[2736]+url[2737]+url[2738]+url[2739]+url[2740]+url[2741]+url[2742]+url[2743]+url[2744]+\
    url[2745]+url[2746]+url[2747]+url[2748]+url[2749]+url[2750]+url[2751]+url[2752]+url[2753]+url[2754]+url[2755]+url[2756]+url[2757]+url[2758]+url[2759]+url[2760]+url[2761]+url[2762]+url[2763]+url[2764]+url[2765]+url[2766]+url[2767]+url[2768]+url[2769]+url[2770]+url[2771]+url[2772]+url[2773]+url[2774]+url[2775]+url[2776]+url[2777]+url[2778]+url[2779]+url[2780]+url[2781]+url[2782]+url[2783]+url[2784]+url[2785]+url[2786]+url[2787]+url[2788]+url[2789]+url[2790]+url[2791]+url[2792]+url[2793]+url[2794]+url[2795]+url[2796]+url[2797]+url[2798]+url[2799]+url[2800]+url[2801]+url[2802]+url[2803]+url[2804]+url[2805]+url[2806]+url[2807]+url[2808]+url[2809]+url[2810]+url[2811]+url[2812]+url[2813]+url[2814]+url[2815]+url[2816]+url[2817]+url[2818]+url[2819]+url[2820]+url[2821]+url[2822]+url[2823]+url[2824]+url[2825]+url[2826]+url[2827]+url[2828]+url[2829]+url[2830]+url[2831]+url[2832]+url[2833]+url[2834]+url[2835]+url[2836]+url[2837]+url[2838]+url[2839]+url[2840]+url[2841]+url[2842]+url[2843]+url[2844]+url[2845]+\
    url[2846]+url[2847]+url[2848]+url[2849]+url[2850]+url[2851]+url[2852]+url[2853]+url[2854]+url[2855]+url[2856]+url[2857]+url[2858]+url[2859]+url[2860]+url[2861]+url[2862]+url[2863]+url[2864]+url[2865]+url[2866]+url[2867]+url[2868]+url[2869]+url[2870]+url[2871]+url[2872]+url[2873]+url[2874]+url[2875]+url[2876]+url[2877]+url[2878]+url[2879]+url[2880]+url[2881]+url[2882]+url[2883]+url[2884]+url[2885]+url[2886]+url[2887]+url[2888]+url[2889]+url[2890]+url[2891]+url[2892]+url[2893]+url[2894]+url[2895]+url[2896]+url[2897]+url[2898]+url[2899]+url[2900]+url[2901]+url[2902]+url[2903]+url[2904]+url[2905]+url[2906]+url[2907]+url[2908]+url[2909]+url[2910]+url[2911]+url[2912]+url[2913]+url[2914]+url[2915]+url[2916]+url[2917]+url[2918]+url[2919]+url[2920]+url[2921]+url[2922]+url[2923]+url[2924]+url[2925]+url[2926]+url[2927]+url[2928]+url[2929]+url[2930]+url[2931]+url[2932]+url[2933]+url[2934]+url[2935]+url[2936]+url[2937]+url[2938]+url[2939]+url[2940]+url[2941]+url[2942]+url[2943]+url[2944]+url[2945]+url[2946]+\
    url[2947]+url[2948]+url[2949]+url[2950]+url[2951]+url[2952]+url[2953]+url[2954]+url[2955]+url[2956]+url[2957]+url[2958]+url[2959]+url[2960]+url[2961]+url[2962]+url[2963]+url[2964]+url[2965]+url[2966]+url[2967]+url[2968]+url[2969]+url[2970]+url[2971]+url[2972]+url[2973]+url[2974]+url[2975]+url[2976]+url[2977]+url[2978]+url[2979]+url[2980]+url[2981]+url[2982]+url[2983]+url[2984]+url[2985]+url[2986]+url[2987]+url[2988]+url[2989]+url[2990]+url[2991]+url[2992]+url[2993]+url[2994]+url[2995]+url[2996]+url[2997]+url[2998]+url[2999]+url[3000]+url[3001]+url[3002]+url[3003]+url[3004]+url[3005]+url[3006]+url[3007]+url[3008]+url[3009]+url[3010]+url[3011]+url[3012]+url[3013]+url[3014]+url[3015]+url[3016]+url[3017]+url[3018]+url[3019]+url[3020]+url[3021]+url[3022]+url[3023]+url[3024]+url[3025]+url[3026]+url[3027]+url[3028]+url[3029]+url[3030]+url[3031]+url[3032]+url[3033]+url[3034]+url[3035]+url[3036]+url[3037]+url[3038]+url[3039]+url[3040]+url[3041]+url[3042]+url[3043]+url[3044]+url[3045]+url[3046]+url[3047]+\
    url[3048]+url[3049]+url[3050]+url[3051]+url[3052]+url[3053]+url[3054]+url[3055]+url[3056]+url[3057]+url[3058]+url[3059]+url[3060]+url[3061]+url[3062]+url[3063]+url[3064]+url[3065]+url[3066]+url[3067]+url[3068]+url[3069]+url[3070]+url[3071]+url[3072]+url[3073]+url[3074]+url[3075]+url[3076]+url[3077]+url[3078]+url[3079]+url[3080]+url[3081]+url[3082]+url[3083]+url[3084]+url[3085]+url[3086]+url[3087]+url[3088]+url[3089]+url[3090]+url[3091]+url[3092]+url[3093]+url[3094]+url[3095]+url[3096]+url[3097]+url[3098]+url[3099]+url[3100]+url[3101]+url[3102]+url[3103]+url[3104]+url[3105]+url[3106]+url[3107]+url[3108]+url[3109]+url[3110]+url[3111]+url[3112]+url[3113]+url[3114]+url[3115]+url[3116]+url[3117]+url[3118]+url[3119]+url[3120]+url[3121]+url[3122]+url[3123]+url[3124]+url[3125]+url[3126]+url[3127]+url[3128]+url[3129]+url[3130]+url[3131]+url[3132]+url[3133]+url[3134]+url[3135]+url[3136]+url[3137]+url[3138]+url[3139]+url[3140]+url[3141]+url[3142]+url[3143]+url[3144]+url[3145]+url[3146]+url[3147]+url[3148]+\
    url[3149]+url[3150]+url[3151]+url[3152]+url[3153]+url[3154]+url[3155]+url[3156]+url[3157]+url[3158]+url[3159]+url[3160]+url[3161]+url[3162]+url[3163]+url[3164]+url[3165]+url[3166]+url[3167]+url[3168]+url[3169]+url[3170]+url[3171]+url[3172]+url[3173]+url[3174]+url[3175]+url[3176]+url[3177]+url[3178]+url[3179]+url[3180]+url[3181]+url[3182]+url[3183]+url[3184]+url[3185]+url[3186]+url[3187]+url[3188]+url[3189]+url[3190]+url[3191]+url[3192]+url[3193]+url[3194]+url[3195]+url[3196]+url[3197]+url[3198]+url[3199]+url[3200]+url[3201]+url[3202]+url[3203]+url[3204]+url[3205]+url[3206]+url[3207]+url[3208]+url[3209]+url[3210]+url[3211]+url[3212]+url[3213]+url[3214]+url[3215]+url[3216]+url[3217]+url[3218]+url[3219]+url[3220]+url[3221]+url[3222]+url[3223]+url[3224]+url[3225]+url[3226]+url[3227]+url[3228]+url[3229]+url[3230]+url[3231]+url[3232]+url[3233]+url[3234]+url[3235]+url[3236]+url[3237]+url[3238]+url[3239]+url[3240]+url[3241]+url[3242]+url[3243]+url[3244]+url[3245]+url[3246]+url[3247]+url[3248]+url[3249]+\
    url[3250]+url[3251]+url[3252]+url[3253]+url[3254]+url[3255]+url[3256]+url[3257]+url[3258]+url[3259]+url[3260]+url[3261]+url[3262]+url[3263]+url[3264]+url[3265]+url[3266]+url[3267]+url[3268]+url[3269]+url[3270]+url[3271]+url[3272]+url[3273]+url[3274]+url[3275]+url[3276]+url[3277]+url[3278]+url[3279]+url[3280]+url[3281]+url[3282]+url[3283]+url[3284]+url[3285]+url[3286]+url[3287]+url[3288]+url[3289]+url[3290]+url[3291]+url[3292]+url[3293]+url[3294]+url[3295]+url[3296]+url[3297]+url[3298]+url[3299]+url[3300]+url[3301]+url[3302]+url[3303]+url[3304]+url[3305]+url[3306]+url[3307]+url[3308]+url[3309]+url[3310]+url[3311]+url[3312]+url[3313]+url[3314]+url[3315]+url[3316]+url[3317]+url[3318]+url[3319]+url[3320]+url[3321]+url[3322]+url[3323]+url[3324]+url[3325]+url[3326]+url[3327]+url[3328]+url[3329]+url[3330]+url[3331]+url[3332]+url[3333]+url[3334]+url[3335]+url[3336]+url[3337]+url[3338]+url[3339]+url[3340]+url[3341]+url[3342]+url[3343]+url[3344]+url[3345]+url[3346]+url[3347]+url[3348]+url[3349]+url[3350]+\
    url[3351]+url[3352]+url[3353]+url[3354]+url[3355]+url[3356]+url[3357]+url[3358]+url[3359]+url[3360]+url[3361]+url[3362]+url[3363]+url[3364]+url[3365]+url[3366]+url[3367]+url[3368]+url[3369]+url[3370]+url[3371]+url[3372]+url[3373]+url[3374]+url[3375]+url[3376]+url[3377]+url[3378]+url[3379]+url[3380]+url[3381]+url[3382]+url[3383]+url[3384]+url[3385]+url[3386]+url[3387]+url[3388]+url[3389]+url[3390]+url[3391]+url[3392]+url[3393]+url[3394]+url[3395]+url[3396]+url[3397]+url[3398]+url[3399]+url[3400]+url[3401]+url[3402]+url[3403]+url[3404]+url[3405]+url[3406]+url[3407]+url[3408]+url[3409]+url[3410]+url[3411]+url[3412]+url[3413]+url[3414]+url[3415]+url[3416]+url[3417]+url[3418]+url[3419]+url[3420]+url[3421]+url[3422]+url[3423]+url[3424]+url[3425]+url[3426]+url[3427]+url[3428]+url[3429]+url[3430]+url[3431]+url[3432]+url[3433]+url[3434]+url[3435]+url[3436]+url[3437]+url[3438]+url[3439]+url[3440]+url[3441]+url[3442]+url[3443]+url[3444]+url[3445]+url[3446]+url[3447]+url[3448]+url[3449]+url[3450]+url[3451]+\
    url[3452]+url[3453]+url[3454]+url[3455]+url[3456]+url[3457]+url[3458]+url[3459]+url[3460]+url[3461]+url[3462]+url[3463]+url[3464]+url[3465]+url[3466]+url[3467]+url[3468]+url[3469]+url[3470]+url[3471]+url[3472]+url[3473]+url[3474]+url[3475]+url[3476]+url[3477]+url[3478]+url[3479]+url[3480]+url[3481]+url[3482]+url[3483]+url[3484]+url[3485]+url[3486]+url[3487]+url[3488]+url[3489]+url[3490]+url[3491]+url[3492]+url[3493]+url[3494]+url[3495]+url[3496]+url[3497]+url[3498]+url[3499]+url[3500]+url[3501]+url[3502]+url[3503]+url[3504]+url[3505]+url[3506]+url[3507]+url[3508]+url[3509]+url[3510]+url[3511]+url[3512]+url[3513]+url[3514]+url[3515]+url[3516]+url[3517]+url[3518]+url[3519]+url[3520]+url[3521]+url[3522]+url[3523]+url[3524]+url[3525]+url[3526]+url[3527]+url[3528]+url[3529]+url[3530]+url[3531]+url[3532]+url[3533]+url[3534]+url[3535]+url[3536]+url[3537]+url[3538]+url[3539]+url[3540]+url[3541]+url[3542]+url[3543]+url[3544]+url[3545]+url[3546]+url[3547]+url[3548]+url[3549]+url[3550]+url[3551]+url[3552]+\
    url[3553]+url[3554]+url[3555]+url[3556]+url[3557]+url[3558]+url[3559]+url[3560]+url[3561]+url[3562]+url[3563]+url[3564]+url[3565]+url[3566]+url[3567]+url[3568]+url[3569]+url[3570]+url[3571]+url[3572]+url[3573]+url[3574]+url[3575]+url[3576]+url[3577]+url[3578]+url[3579]+url[3580]+url[3581]+url[3582]+url[3583]+url[3584]+url[3585]+url[3586]+url[3587]+url[3588]+url[3589]+url[3590]+url[3591]+url[3592]+url[3593]+url[3594]+url[3595]+url[3596]+url[3597]+url[3598]+url[3599]+url[3600]+url[3601]+url[3602]+url[3603]+url[3604]+url[3605]+url[3606]+url[3607]+url[3608]+url[3609]+url[3610]+url[3611]+url[3612]+url[3613]+url[3614]+url[3615]+url[3616]+url[3617]+url[3618]+url[3619]+url[3620]+url[3621]+url[3622]+url[3623]+url[3624]+url[3625]+url[3626]+url[3627]+url[3628]+url[3629]+url[3630]+url[3631]+url[3632]+url[3633]+url[3634]+url[3635]+url[3636]+url[3637]+url[3638]+url[3639]+url[3640]+url[3641]+url[3642]+url[3643]+url[3644]+url[3645]+url[3646]+url[3647]+url[3648]+url[3649]+url[3650]+url[3651]+url[3652]+url[3653]+\
    url[3654]+url[3655]+url[3656]+url[3657]+url[3658]+url[3659]+url[3660]+url[3661]+url[3662]+url[3663]+url[3664]+url[3665]+url[3666]+url[3667]+url[3668]+url[3669]+url[3670]+url[3671]+url[3672]+url[3673]+url[3674]+url[3675]+url[3676]+url[3677]+url[3678]+url[3679]+url[3680]+url[3681]+url[3682]+url[3683]+url[3684]+url[3685]+url[3686]+url[3687]+url[3688]+url[3689]+url[3690]+url[3691]+url[3692]+url[3693]+url[3694]+url[3695]+url[3696]+url[3697]+url[3698]+url[3699]+url[3700]+url[3701]+url[3702]+url[3703]+url[3704]+url[3705]+url[3706]+url[3707]+url[3708]+url[3709]+url[3710]+url[3711]+url[3712]+url[3713]+url[3714]+url[3715]+url[3716]+url[3717]+url[3718]+url[3719]+url[3720]+url[3721]+url[3722]+url[3723]+url[3724]+url[3725]+url[3726]+url[3727]+url[3728]+url[3729]+url[3730]+url[3731]+url[3732]+url[3733]+url[3734]+url[3735]+url[3736]+url[3737]+url[3738]+url[3739]+url[3740]+url[3741]+url[3742]+url[3743]+url[3744]+url[3745]+url[3746]+url[3747]+url[3748]+url[3749]+url[3750]+url[3751]+url[3752]+url[3753]+url[3754]+\
    url[3755]+url[3756]+url[3757]+url[3758]+url[3759]+url[3760]+url[3761]+url[3762]+url[3763]+url[3764]+url[3765]+url[3766]+url[3767]+url[3768]+url[3769]+url[3770]+url[3771]+url[3772]+url[3773]+url[3774]+url[3775]+url[3776]+url[3777]+url[3778]+url[3779]+url[3780]+url[3781]+url[3782]+url[3783]+url[3784]+url[3785]+url[3786]+url[3787]+url[3788]+url[3789]+url[3790]+url[3791]+url[3792]+url[3793]+url[3794]+url[3795]+url[3796]+url[3797]+url[3798]+url[3799]+url[3800]+url[3801]+url[3802]+url[3803]+url[3804]+url[3805]+url[3806]+url[3807]+url[3808]+url[3809]+url[3810]+url[3811]+url[3812]+url[3813]+url[3814]+url[3815]+url[3816]+url[3817]+url[3818]+url[3819]+url[3820]+url[3821]+url[3822]+url[3823]+url[3824]+url[3825]+url[3826]+url[3827]+url[3828]+url[3829]+url[3830]+url[3831]+url[3832]+url[3833]+url[3834]+url[3835]+url[3836]+url[3837]+url[3838]+url[3839]+url[3840]+url[3841]+url[3842]+url[3843]+url[3844]+url[3845]+url[3846]+url[3847]+url[3848]+url[3849]+url[3850]+url[3851]+url[3852]+url[3853]+url[3854]+url[3855]+\
    url[3856]+url[3857]+url[3858]+url[3859]+url[3860]+url[3861]+url[3862]+url[3863]+url[3864]+url[3865]+url[3866]+url[3867]+url[3868]+url[3869]+url[3870]+url[3871]+url[3872]+url[3873]+url[3874]+url[3875]+url[3876]+url[3877]+url[3878]+url[3879]+url[3880]+url[3881]+url[3882]+url[3883]+url[3884]+url[3885]+url[3886]+url[3887]+url[3888]+url[3889]+url[3890]+url[3891]+url[3892]+url[3893]+url[3894]+url[3895]+url[3896]+url[3897]+url[3898]+url[3899]+url[3900]+url[3901]+url[3902]+url[3903]+url[3904]+url[3905]+url[3906]+url[3907]+url[3908]+url[3909]+url[3910]+url[3911]+url[3912]+url[3913]+url[3914]+url[3915]+url[3916]+url[3917]+url[3918]+url[3919]+url[3920]+url[3921]+url[3922]+url[3923]+url[3924]+url[3925]+url[3926]+url[3927]+url[3928]+url[3929]+url[3930]+url[3931]+url[3932]+url[3933]+url[3934]+url[3935]+url[3936]+url[3937]+url[3938]+url[3939]+url[3940]+url[3941]+url[3942]+url[3943]+url[3944]+url[3945]+url[3946]+url[3947]+url[3948]+url[3949]+url[3950]+url[3951]+url[3952]+url[3953]+url[3954]+url[3955]+url[3956]+\
    url[3957]+url[3958]+url[3959]+url[3960]+url[3961]+url[3962]+url[3963]+url[3964]+url[3965]+url[3966]+url[3967]+url[3968]+url[3969]+url[3970]+url[3971]+url[3972]+url[3973]+url[3974]+url[3975]+url[3976]+url[3977]+url[3978]+url[3979]+url[3980]+url[3981]+url[3982]+url[3983]+url[3984]+url[3985]+url[3986]+url[3987]+url[3988]+url[3989]+url[3990]+url[3991]+url[3992]+url[3993]+url[3994]+url[3995]+url[3996]+url[3997]+url[3998]+url[3999]+url[4000]+url[4001]+url[4002]+url[4003]+url[4004]+url[4005]+url[4006]+url[4007]+url[4008]+url[4009]+url[4010]+url[4011]+url[4012]+url[4013]+url[4014]+url[4015]+url[4016]+url[4017]+url[4018]+url[4019]+url[4020]+url[4021]+url[4022]+url[4023]+url[4024]+url[4025]+url[4026]+url[4027]+url[4028]+url[4029]+url[4030]+url[4031]+url[4032]+url[4033]+url[4034]+url[4035]+url[4036]+url[4037]+url[4038]+url[4039]+url[4040]+url[4041]+url[4042]+url[4043]+url[4044]+url[4045]+url[4046]+url[4047]+url[4048]+url[4049]+url[4050]+url[4051]+url[4052]+url[4053]+url[4054]+url[4055]+url[4056]+url[4057]+\
    url[4058]+url[4059]+url[4060]+url[4061]+url[4062]+url[4063]+url[4064]+url[4065]+url[4066]+url[4067]+url[4068]+url[4069]+url[4070]+url[4071]+url[4072]+url[4073]+url[4074]+url[4075]+url[4076]+url[4077]+url[4078]+url[4079]+url[4080]+url[4081]+url[4082]+url[4083]+url[4084]+url[4085]+url[4086]+url[4087]+url[4088]+url[4089]+url[4090]+url[4091]+url[4092]+url[4093]+url[4094]+url[4095]+url[4096]+url[4097]+url[4098]+url[4099]+url[4100]+url[4101]+url[4102]+url[4103]+url[4104]+url[4105]+url[4106]+url[4107]+url[4108]+url[4109]+url[4110]+url[4111]+url[4112]+url[4113]+url[4114]+url[4115]+url[4116]+url[4117]+url[4118]+url[4119]+url[4120]+url[4121]+url[4122]+url[4123]+url[4124]+url[4125]+url[4126]+url[4127]+url[4128]+url[4129]+url[4130]+url[4131]+url[4132]+url[4133]+url[4134]+url[4135]+url[4136]+url[4137]+url[4138]+url[4139]+url[4140]+url[4141]+url[4142]+url[4143]+url[4144]+url[4145]+url[4146]+url[4147]+url[4148]+url[4149]+url[4150]+url[4151]+url[4152]+url[4153]+url[4154]+url[4155]+url[4156]+url[4157]+url[4158]+\
    url[4159]+url[4160]+url[4161]+url[4162]+url[4163]+url[4164]+url[4165]+url[4166]+url[4167]+url[4168]+url[4169]+url[4170]+url[4171]+url[4172]+url[4173]+url[4174]+url[4175]+url[4176]+url[4177]+url[4178]+url[4179]+url[4180]+url[4181]+url[4182]+url[4183]+url[4184]+url[4185]+url[4186]+url[4187]+url[4188]+url[4189]+url[4190]+url[4191]+url[4192]+url[4193]+url[4194]+url[4195]+url[4196]+url[4197]+url[4198]+url[4199]+url[4200]+url[4201]+url[4202]+url[4203]+url[4204]+url[4205]+url[4206]+url[4207]+url[4208]+url[4209]+url[4210]+url[4211]+url[4212]+url[4213]+url[4214]+url[4215]+url[4216]+url[4217]+url[4218]+url[4219]+url[4220]+url[4221]+url[4222]+url[4223]+url[4224]+url[4225]+url[4226]+url[4227]+url[4228]+url[4229]+url[4230]+url[4231]+url[4232]+url[4233]+url[4234]+url[4235]+url[4236]+url[4237]+url[4238]+url[4239]+url[4240]+url[4241]+url[4242]+url[4243]+url[4244]+url[4245]+url[4246]+url[4247]+url[4248]+url[4249]+url[4250]+url[4251]+url[4252]+url[4253]+url[4254]+url[4255]+url[4256]+url[4257]+url[4258]+url[4259]+\
    url[4260]+url[4261]+url[4262]+url[4263]+url[4264]+url[4265]+url[4266]+url[4267]+url[4268]+url[4269]+url[4270]+url[4271]+url[4272]+url[4273]+url[4274]+url[4275]+url[4276]+url[4277]+url[4278]+url[4279]+url[4280]+url[4281]+url[4282]+url[4283]+url[4284]+url[4285]+url[4286]+url[4287]+url[4288]+url[4289]+url[4290]+url[4291]+url[4292]+url[4293]+url[4294]+url[4295]+url[4296]+url[4297]+url[4298]+url[4299]+url[4300]+url[4301]+url[4302]+url[4303]+url[4304]+url[4305]+url[4306]+url[4307]+url[4308]+url[4309]+url[4310]+url[4311]+url[4312]+url[4313]+url[4314]+url[4315]+url[4316]+url[4317]+url[4318]+url[4319]+url[4320]+url[4321]+url[4322]+url[4323]+url[4324]+url[4325]+url[4326]+url[4327]+url[4328]+url[4329]+url[4330]+url[4331]+url[4332]+url[4333]+url[4334]+url[4335]+url[4336]+url[4337]+url[4338]+url[4339]+url[4340]+url[4341]+url[4342]+url[4343]+url[4344]+url[4345]+url[4346]+url[4347]+url[4348]+url[4349]+url[4350]+url[4351]+url[4352]+url[4353]+url[4354]+url[4355]+url[4356]+url[4357]+url[4358]+url[4359]+url[4360]+\
    url[4361]+url[4362]+url[4363]+url[4364]+url[4365]+url[4366]+url[4367]+url[4368]+url[4369]+url[4370]+url[4371]+url[4372]+url[4373]+url[4374]+url[4375]+url[4376]+url[4377]+url[4378]+url[4379]+url[4380]+url[4381]+url[4382]+url[4383]+url[4384]+url[4385]+url[4386]+url[4387]+url[4388]+url[4389]+url[4390]+url[4391]+url[4392]+url[4393]+url[4394]+url[4395]+url[4396]+url[4397]+url[4398]+url[4399]+url[4400]+url[4401]+url[4402]+url[4403]+url[4404]+url[4405]+url[4406]+url[4407]+url[4408]+url[4409]+url[4410]+url[4411]+url[4412]+url[4413]+url[4414]+url[4415]+url[4416]+url[4417]+url[4418]+url[4419]+url[4420]+url[4421]+url[4422]+url[4423]+url[4424]+url[4425]+url[4426]+url[4427]+url[4428]+url[4429]+url[4430]+url[4431]+url[4432]+url[4433]+url[4434]+url[4435]+url[4436]+url[4437]+url[4438]+url[4439]+url[4440]+url[4441]+url[4442]+url[4443]+url[4444]+url[4445]+url[4446]+url[4447]+url[4448]+url[4449]+url[4450]+url[4451]+url[4452]+url[4453]+url[4454]+url[4455]+url[4456]+url[4457]+url[4458]+url[4459]+url[4460]+url[4461]+\
    url[4462]+url[4463]+url[4464]+url[4465]+url[4466]+url[4467]+url[4468]+url[4469]+url[4470]+url[4471]+url[4472]+url[4473]+url[4474]+url[4475]+url[4476]+url[4477]+url[4478]+url[4479]+url[4480]+url[4481]+url[4482]+url[4483]+url[4484]+url[4485]+url[4486]+url[4487]+url[4488]+url[4489]+url[4490]+url[4491]+url[4492]+url[4493]+url[4494]+url[4495]+url[4496]+url[4497]+url[4498]+url[4499]+url[4500]+url[4501]+url[4502]+url[4503]+url[4504]+url[4505]+url[4506]+url[4507]+url[4508]+url[4509]+url[4510]+url[4511]+url[4512]+url[4513]+url[4514]+url[4515]+url[4516]+url[4517]+url[4518]+url[4519]+url[4520]+url[4521]+url[4522]+url[4523]+url[4524]+url[4525]+url[4526]+url[4527]+url[4528]+url[4529]+url[4530]+url[4531]+url[4532]+url[4533]+url[4534]+url[4535]+url[4536]+url[4537]+url[4538]+url[4539]+url[4540]+url[4541]+url[4542]+url[4543]+url[4544]+url[4545]+url[4546]+url[4547]+url[4548]+url[4549]+url[4550]+url[4551]+url[4552]+url[4553]+url[4554]+url[4555]+url[4556]+url[4557]+url[4558]+url[4559]+url[4560]+url[4561]+url[4562]+\
    url[4563]+url[4564]+url[4565]+url[4566]+url[4567]+url[4568]+url[4569]+url[4570]+url[4571]+url[4572]+url[4573]+url[4574]+url[4575]+url[4576]+url[4577]+url[4578]+url[4579]+url[4580]+url[4581]+url[4582]+url[4583]+url[4584]+url[4585]+url[4586]+url[4587]+url[4588]+url[4589]+url[4590]+url[4591]+url[4592]+url[4593]+url[4594]+url[4595]+url[4596]+url[4597]+url[4598]+url[4599]+url[4600]+url[4601]+url[4602]+url[4603]+url[4604]+url[4605]+url[4606]+url[4607]+url[4608]+url[4609]+url[4610]+url[4611]+url[4612]+url[4613]+url[4614]+url[4615]+url[4616]+url[4617]+url[4618]+url[4619]+url[4620]+url[4621]+url[4622]+url[4623]+url[4624]+url[4625]+url[4626]+url[4627]+url[4628]+url[4629]+url[4630]+url[4631]+url[4632]+url[4633]+url[4634]+url[4635]+url[4636]+url[4637]+url[4638]+url[4639]+url[4640]+url[4641]+url[4642]+url[4643]+url[4644]+url[4645]+url[4646]+url[4647]+url[4648]+url[4649]+url[4650]+url[4651]+url[4652]+url[4653]+url[4654]+url[4655]+url[4656]+url[4657]+url[4658]+url[4659]+url[4660]+url[4661]+url[4662]+url[4663]+\
    url[4664]+url[4665]+url[4666]+url[4667]+url[4668]+url[4669]+url[4670]+url[4671]+url[4672]+url[4673]+url[4674]+url[4675]+url[4676]+url[4677]+url[4678]+url[4679]+url[4680]+url[4681]+url[4682]+url[4683]+url[4684]+url[4685]+url[4686]+url[4687]+url[4688]+url[4689]+url[4690]+url[4691]+url[4692]+url[4693]+url[4694]+url[4695]+url[4696]+url[4697]+url[4698]+url[4699]+url[4700]+url[4701]+url[4702]+url[4703]+url[4704]+url[4705]+url[4706]+url[4707]+url[4708]+url[4709]+url[4710]+url[4711]+url[4712]+url[4713]+url[4714]+url[4715]+url[4716]+url[4717]+url[4718]+url[4719]+url[4720]+url[4721]+url[4722]+url[4723]+url[4724]+url[4725]+url[4726]+url[4727]+url[4728]+url[4729]+url[4730]+url[4731]+url[4732]+url[4733]+url[4734]+url[4735]+url[4736]+url[4737]+url[4738]+url[4739]+url[4740]+url[4741]+url[4742]+url[4743]+url[4744]+url[4745]+url[4746]+url[4747]+url[4748]+url[4749]+url[4750]+url[4751]+url[4752]+url[4753]+url[4754]+url[4755]+url[4756]+url[4757]+url[4758]+url[4759]+url[4760]+url[4761]+url[4762]+url[4763]+url[4764]+\
    url[4765]+url[4766]+url[4767]+url[4768]+url[4769]+url[4770]+url[4771]+url[4772]+url[4773]+url[4774]+url[4775]+url[4776]+url[4777]+url[4778]+url[4779]+url[4780]+url[4781]+url[4782]+url[4783]+url[4784]+url[4785]+url[4786]+url[4787]+url[4788]+url[4789]+url[4790]+url[4791]+url[4792]+url[4793]+url[4794]+url[4795]+url[4796]+url[4797]+url[4798]+url[4799]+url[4800]+url[4801]+url[4802]+url[4803]+url[4804]+url[4805]+url[4806]+url[4807]+url[4808]+url[4809]+url[4810]+url[4811]+url[4812]+url[4813]+url[4814]+url[4815]+url[4816]+url[4817]+url[4818]+url[4819]+url[4820]+url[4821]+url[4822]+url[4823]+url[4824]+url[4825]+url[4826]+url[4827]+url[4828]+url[4829]+url[4830]+url[4831]+url[4832]+url[4833]+url[4834]+url[4835]+url[4836]+url[4837]+url[4838]+url[4839]+url[4840]+url[4841]+url[4842]+url[4843]+url[4844]+url[4845]+url[4846]+url[4847]+url[4848]+url[4849]+url[4850]+url[4851]+url[4852]+url[4853]+url[4854]+url[4855]+url[4856]+url[4857]+url[4858]+url[4859]+url[4860]+url[4861]+url[4862]+url[4863]+url[4864]+url[4865]+\
    url[4866]+url[4867]+url[4868]+url[4869]+url[4870]+url[4871]+url[4872]+url[4873]+url[4874]+url[4875]+url[4876]+url[4877]+url[4878]+url[4879]+url[4880]+url[4881]+url[4882]+url[4883]+url[4884]+url[4885]+url[4886]+url[4887]+url[4888]+url[4889]+url[4890]+url[4891]+url[4892]+url[4893]+url[4894]+url[4895]+url[4896]+url[4897]+url[4898]+url[4899]+url[4900]+url[4901]+url[4902]+url[4903]+url[4904]+url[4905]+url[4906]+url[4907]+url[4908]+url[4909]+url[4910]+url[4911]+url[4912]+url[4913]+url[4914]+url[4915]+url[4916]+url[4917]+url[4918]+url[4919]+url[4920]+url[4921]+url[4922]+url[4923]+url[4924]+url[4925]+url[4926]+url[4927]+url[4928]+url[4929]+url[4930]+url[4931]+url[4932]+url[4933]+url[4934]+url[4935]+url[4936]+url[4937]+url[4938]+url[4939]+url[4940]+url[4941]+url[4942]+url[4943]+url[4944]+url[4945]+url[4946]+url[4947]+url[4948]+url[4949]+url[4950]+url[4951]+url[4952]+url[4953]+url[4954]+url[4955]+url[4956]+url[4957]+url[4958]+url[4959]+url[4960]+url[4961]+url[4962]+url[4963]+url[4964]+url[4965]+url[4966]+\
    url[4967]+url[4968]+url[4969]+url[4970]+url[4971]+url[4972]+url[4973]+url[4974]+url[4975]+url[4976]+url[4977]+url[4978]+url[4979]+url[4980]+url[4981]+url[4982]+url[4983]+url[4984]+url[4985]+url[4986]+url[4987]+url[4988]+url[4989]+url[4990]+url[4991]+url[4992]+url[4993]+url[4994]+url[4995]+url[4996]+url[4997]+url[4998]+url[4999]+url[5000]+url[5001]+url[5002]+url[5003]+url[5004]+url[5005]+url[5006]+url[5007]+url[5008]+url[5009]+url[5010]+url[5011]+url[5012]+url[5013]+url[5014]+url[5015]+url[5016]+url[5017]+url[5018]+url[5019]+url[5020]+url[5021]+url[5022]+url[5023]+url[5024]+url[5025]+url[5026]+url[5027]+url[5028]+url[5029]+url[5030]+url[5031]+url[5032]+url[5033]+url[5034]+url[5035]+url[5036]+url[5037]+url[5038]+url[5039]+url[5040]+url[5041]+url[5042]+url[5043]+url[5044]+url[5045]+url[5046]+url[5047]+url[5048]+url[5049]+url[5050]+url[5051]+url[5052]+url[5053]+url[5054]+url[5055]+url[5056]+url[5057]+url[5058]+url[5059]+url[5060]+url[5061]+url[5062]+url[5063]+url[5064]+url[5065]+url[5066]+url[5067]+\
    url[5068]+url[5069]+url[5070]+url[5071]+url[5072]+url[5073]+url[5074]+url[5075]+url[5076]+url[5077]+url[5078]+url[5079]+url[5080]+url[5081]+url[5082]+url[5083]+url[5084]+url[5085]+url[5086]+url[5087]+url[5088]+url[5089]+url[5090]+url[5091]+url[5092]+url[5093]+url[5094]+url[5095]+url[5096]+url[5097]+url[5098]+url[5099]+url[5100]+url[5101]+url[5102]+url[5103]+url[5104]+url[5105]+url[5106]+url[5107]+url[5108]+url[5109]+url[5110]+url[5111]+url[5112]+url[5113]+url[5114]+url[5115]+url[5116]+url[5117]+url[5118]+url[5119]+url[5120]+url[5121]+url[5122]+url[5123]+url[5124]+url[5125]+url[5126]+url[5127]+url[5128]+url[5129]+url[5130]+url[5131]+url[5132]+url[5133]+url[5134]+url[5135]+url[5136]+url[5137]+url[5138]+url[5139]+url[5140]+url[5141]+url[5142]+url[5143]+url[5144]+url[5145]+url[5146]+url[5147]+url[5148]+url[5149]+url[5150]+url[5151]+url[5152]+url[5153]+url[5154]+url[5155]+url[5156]+url[5157]+url[5158]+url[5159]+url[5160]+url[5161]+url[5162]+url[5163]+url[5164]+url[5165]+url[5166]+url[5167]+url[5168]+\
    url[5169]+url[5170]+url[5171]+url[5172]+url[5173]+url[5174]+url[5175]+url[5176]+url[5177]+url[5178]+url[5179]+url[5180]+url[5181]+url[5182]+url[5183]+url[5184]+url[5185]+url[5186]+url[5187]+url[5188]+url[5189]+url[5190]+url[5191]+url[5192]+url[5193]+url[5194]+url[5195]+url[5196]+url[5197]+url[5198]+url[5199]+url[5200]+url[5201]+url[5202]+url[5203]+url[5204]+url[5205]+url[5206]+url[5207]+url[5208]+url[5209]+url[5210]+url[5211]+url[5212]+url[5213]+url[5214]+url[5215]+url[5216]+url[5217]+url[5218]+url[5219]+url[5220]+url[5221]+url[5222]+url[5223]+url[5224]+url[5225]+url[5226]+url[5227]+url[5228]+url[5229]+url[5230]+url[5231]+url[5232]+url[5233]+url[5234]+url[5235]+url[5236]+url[5237]+url[5238]+url[5239]+url[5240]+url[5241]+url[5242]+url[5243]+url[5244]+url[5245]+url[5246]+url[5247]+url[5248]+url[5249]+url[5250]+url[5251]+url[5252]+url[5253]+url[5254]+url[5255]+url[5256]+url[5257]+url[5258]+url[5259]+url[5260]+url[5261]+url[5262]+url[5263]+url[5264]+url[5265]+url[5266]+url[5267]+url[5268]+url[5269]+\
    url[5270]+url[5271]+url[5272]+url[5273]+url[5274]+url[5275]+url[5276]+url[5277]+url[5278]+url[5279]+url[5280]+url[5281]+url[5282]+url[5283]+url[5284]+url[5285]+url[5286]+url[5287]+url[5288]+url[5289]+url[5290]+url[5291]+url[5292]+url[5293]+url[5294]+url[5295]+url[5296]+url[5297]+url[5298]+url[5299]+url[5300]+url[5301]+url[5302]+url[5303]+url[5304]+url[5305]+url[5306]+url[5307]+url[5308]+url[5309]+url[5310]+url[5311]+url[5312]+url[5313]+url[5314]+url[5315]+url[5316]+url[5317]+url[5318]+url[5319]+url[5320]+url[5321]+url[5322]+url[5323]+url[5324]+url[5325]+url[5326]+url[5327]+url[5328]+url[5329]+url[5330]+url[5331]+url[5332]+url[5333]+url[5334]+url[5335]+url[5336]+url[5337]+url[5338]+url[5339]+url[5340]+url[5341]+url[5342]+url[5343]+url[5344]+url[5345]+url[5346]+url[5347]+url[5348]+url[5349]+url[5350]+url[5351]+url[5352]+url[5353]+url[5354]+url[5355]+url[5356]+url[5357]+url[5358]+url[5359]+url[5360]+url[5361]+url[5362]+url[5363]+url[5364]+url[5365]+url[5366]+url[5367]+url[5368]+url[5369]+url[5370]+\
    url[5371]+url[5372]+url[5373]+url[5374]+url[5375]+url[5376]+url[5377]+url[5378]+url[5379]+url[5380]+url[5381]+url[5382]+url[5383]+url[5384]+url[5385]+url[5386]+url[5387]+url[5388]+url[5389]+url[5390]+url[5391]+url[5392]+url[5393]+url[5394]+url[5395]+url[5396]+url[5397]+url[5398]+url[5399]+url[5400]+url[5401]+url[5402]+url[5403]+url[5404]+url[5405]+url[5406]+url[5407]+url[5408]+url[5409]+url[5410]+url[5411]+url[5412]+url[5413]+url[5414]+url[5415]+url[5416]+url[5417]+url[5418]+url[5419]+url[5420]+url[5421]+url[5422]+url[5423]+url[5424]+url[5425]+url[5426]+url[5427]+url[5428]+url[5429]+url[5430]+url[5431]+url[5432]+url[5433]+url[5434]+url[5435]+url[5436]+url[5437]+url[5438]+url[5439]+url[5440]+url[5441]+url[5442]+url[5443]+url[5444]+url[5445]+url[5446]+url[5447]+url[5448]+url[5449]+url[5450]+url[5451]+url[5452]+url[5453]+url[5454]+url[5455]+url[5456]+url[5457]+url[5458]+url[5459]+url[5460]+url[5461]+url[5462]+url[5463]+url[5464]+url[5465]+url[5466]+url[5467]+url[5468]+url[5469]+url[5470]+url[5471]+\
    url[5472]+url[5473]+url[5474]+url[5475]+url[5476]+url[5477]+url[5478]+url[5479]+url[5480]+url[5481]+url[5482]+url[5483]+url[5484]+url[5485]+url[5486]+url[5487]+url[5488]+url[5489]+url[5490]+url[5491]+url[5492]+url[5493]+url[5494]+url[5495]+url[5496]+url[5497]+url[5498]+url[5499]+url[5500]+url[5501]+url[5502]+url[5503]+url[5504]+url[5505]+url[5506]+url[5507]+url[5508]+url[5509]+url[5510]+url[5511]+url[5512]+url[5513]+url[5514]+url[5515]+url[5516]+url[5517]+url[5518]+url[5519]+url[5520]+url[5521]+url[5522]+url[5523]+url[5524]+url[5525]+url[5526]+url[5527]+url[5528]+url[5529]+url[5530]+url[5531]+url[5532]+url[5533]+url[5534]+url[5535]+url[5536]+url[5537]+url[5538]+url[5539]+url[5540]+url[5541]+url[5542]+url[5543]+url[5544]+url[5545]+url[5546]+url[5547]+url[5548]+url[5549]+url[5550]+url[5551]+url[5552]+url[5553]+url[5554]+url[5555]+url[5556]+url[5557]+url[5558]+url[5559]+url[5560]+url[5561]+url[5562]+url[5563]+url[5564]+url[5565]+url[5566]+url[5567]+url[5568]+url[5569]+url[5570]+url[5571]+url[5572]+\
    url[5573]+url[5574]+url[5575]+url[5576]+url[5577]+url[5578]+url[5579]+url[5580]+url[5581]+url[5582]+url[5583]+url[5584]+url[5585]+url[5586]+url[5587]+url[5588]+url[5589]+url[5590]+url[5591]+url[5592]+url[5593]+url[5594]+url[5595]+url[5596]+url[5597]+url[5598]+url[5599]+url[5600]+url[5601]+url[5602]+url[5603]+url[5604]+url[5605]+url[5606]+url[5607]+url[5608]+url[5609]+url[5610]+url[5611]+url[5612]+url[5613]+url[5614]+url[5615]+url[5616]+url[5617]+url[5618]+url[5619]+url[5620]+url[5621]+url[5622]+url[5623]+url[5624]+url[5625]+url[5626]+url[5627]+url[5628]+url[5629]+url[5630]+url[5631]+url[5632]+url[5633]+url[5634]+url[5635]+url[5636]+url[5637]+url[5638]+url[5639]+url[5640]+url[5641]+url[5642]+url[5643]+url[5644]+url[5645]+url[5646]+url[5647]+url[5648]+url[5649]+url[5650]+url[5651]+url[5652]+url[5653]+url[5654]+url[5655]+url[5656]+url[5657]+url[5658]+url[5659]+url[5660]+url[5661]+url[5662]+url[5663]+url[5664]+url[5665]+url[5666]+url[5667]+url[5668]+url[5669]+url[5670]+url[5671]+url[5672]+url[5673]+\
    url[5674]+url[5675]+url[5676]+url[5677]+url[5678]+url[5679]+url[5680]+url[5681]+url[5682]+url[5683]+url[5684]+url[5685]+url[5686]+url[5687]+url[5688]+url[5689]+url[5690]+url[5691]+url[5692]+url[5693]+url[5694]+url[5695]+url[5696]+url[5697]+url[5698]+url[5699]+url[5700]+url[5701]+url[5702]+url[5703]+url[5704]+url[5705]+url[5706]+url[5707]+url[5708]+url[5709]+url[5710]+url[5711]+url[5712]+url[5713]+url[5714]+url[5715]+url[5716]+url[5717]+url[5718]+url[5719]+url[5720]+url[5721]+url[5722]+url[5723]+url[5724]+url[5725]+url[5726]+url[5727]+url[5728]+url[5729]+url[5730]+url[5731]+url[5732]+url[5733]+url[5734]+url[5735]+url[5736]+url[5737]+url[5738]+url[5739]+url[5740]+url[5741]+url[5742]+url[5743]+url[5744]+url[5745]+url[5746]+url[5747]+url[5748]+url[5749]+url[5750]+url[5751]+url[5752]+url[5753]+url[5754]+url[5755]+url[5756]+url[5757]+url[5758]+url[5759]+url[5760]+url[5761]+url[5762]+url[5763]+url[5764]+url[5765]+url[5766]+url[5767]+url[5768]+url[5769]+url[5770]+url[5771]+url[5772]+url[5773]+url[5774]+\
    url[5775]+url[5776]+url[5777]+url[5778]+url[5779]+url[5780]+url[5781]+url[5782]+url[5783]+url[5784]+url[5785]+url[5786]+url[5787]+url[5788]+url[5789]+url[5790]+url[5791]+url[5792]+url[5793]+url[5794]+url[5795]+url[5796]+url[5797]+url[5798]+url[5799]+url[5800]+url[5801]+url[5802]+url[5803]+url[5804]+url[5805]+url[5806]+url[5807]+url[5808]+url[5809]+url[5810]+url[5811]+url[5812]+url[5813]+url[5814]+url[5815]+url[5816]+url[5817]+url[5818]+url[5819]+url[5820]+url[5821]+url[5822]+url[5823]+url[5824]+url[5825]+url[5826]+url[5827]+url[5828]+url[5829]+url[5830]+url[5831]+url[5832]+url[5833]+url[5834]+url[5835]+url[5836]+url[5837]+url[5838]+url[5839]+url[5840]+url[5841]+url[5842]+url[5843]+url[5844]+url[5845]+url[5846]+url[5847]+url[5848]+url[5849]+url[5850]+url[5851]+url[5852]+url[5853]+url[5854]+url[5855]+url[5856]+url[5857]+url[5858]+url[5859]+url[5860]+url[5861]+url[5862]+url[5863]+url[5864]+url[5865]+url[5866]+url[5867]+url[5868]+url[5869]+url[5870]+url[5871]+url[5872]+url[5873]+url[5874]+url[5875]+\
    url[5876]+url[5877]+url[5878]+url[5879]+url[5880]+url[5881]+url[5882]+url[5883]+url[5884]+url[5885]+url[5886]+url[5887]+url[5888]+url[5889]+url[5890]+url[5891]+url[5892]+url[5893]+url[5894]+url[5895]+url[5896]+url[5897]+url[5898]+url[5899]+url[5900]+url[5901]+url[5902]+url[5903]+url[5904]+url[5905]+url[5906]+url[5907]+url[5908]+url[5909]+url[5910]+url[5911]+url[5912]+url[5913]+url[5914]+url[5915]+url[5916]+url[5917]+url[5918]+url[5919]+url[5920]+url[5921]+url[5922]+url[5923]+url[5924]+url[5925]+url[5926]+url[5927]+url[5928]+url[5929]+url[5930]+url[5931]+url[5932]+url[5933]+url[5934]+url[5935]+url[5936]+url[5937]+url[5938]+url[5939]+url[5940]+url[5941]+url[5942]+url[5943]+url[5944]+url[5945]+url[5946]+url[5947]+url[5948]+url[5949]+url[5950]+url[5951]+url[5952]+url[5953]+url[5954]+url[5955]+url[5956]+url[5957]+url[5958]+url[5959]+url[5960]+url[5961]+url[5962]+url[5963]+url[5964]+url[5965]+url[5966]+url[5967]+url[5968]+url[5969]+url[5970]+url[5971]+url[5972]+url[5973]+url[5974]+url[5975]+url[5976]+\
    url[5977]+url[5978]+url[5979]+url[5980]+url[5981]+url[5982]+url[5983]+url[5984]+url[5985]+url[5986]+url[5987]+url[5988]+url[5989]+url[5990]+url[5991]+url[5992]+url[5993]+url[5994]+url[5995]+url[5996]+url[5997]+url[5998]+url[5999]+url[6000]+url[6001]+url[6002]+url[6003]+url[6004]+url[6005]+url[6006]+url[6007]+url[6008]+url[6009]+url[6010]+url[6011]+url[6012]+url[6013]+url[6014]+url[6015]+url[6016]+url[6017]+url[6018]+url[6019]+url[6020]+url[6021]+url[6022]+url[6023]+url[6024]+url[6025]+url[6026]+url[6027]+url[6028]+url[6029]+url[6030]+url[6031]+url[6032]+url[6033]+url[6034]+url[6035]+url[6036]+url[6037]+url[6038]+url[6039]+url[6040]+url[6041]+url[6042]+url[6043]+url[6044]+url[6045]+url[6046]+url[6047]+url[6048]+url[6049]+url[6050]+url[6051]+url[6052]+url[6053]+url[6054]+url[6055]+url[6056]+url[6057]+url[6058]+url[6059]+url[6060]+url[6061]+url[6062]+url[6063]+url[6064]+url[6065]+url[6066]+url[6067]+url[6068]+url[6069]+url[6070]+url[6071]+url[6072]+url[6073]+url[6074]+url[6075]+url[6076]+url[6077]+\
    url[6078]+url[6079]+url[6080]+url[6081]+url[6082]+url[6083]+url[6084]+url[6085]+url[6086]+url[6087]+url[6088]+url[6089]+url[6090]+url[6091]+url[6092]+url[6093]+url[6094]+url[6095]+url[6096]+url[6097]+url[6098]+url[6099]+url[6100]+url[6101]+url[6102]+url[6103]+url[6104]+url[6105]+url[6106]+url[6107]+url[6108]+url[6109]+url[6110]+url[6111]+url[6112]+url[6113]+url[6114]+url[6115]+url[6116]+url[6117]+url[6118]+url[6119]+url[6120]+url[6121]+url[6122]+url[6123]+url[6124]+url[6125]+url[6126]+url[6127]+url[6128]+url[6129]+url[6130]+url[6131]+url[6132]+url[6133]+url[6134]+url[6135]+url[6136]+url[6137]+url[6138]+url[6139]+url[6140]+url[6141]+url[6142]+url[6143]+url[6144]+url[6145]+url[6146]+url[6147]+url[6148]+url[6149]+url[6150]+url[6151]+url[6152]+url[6153]+url[6154]+url[6155]+url[6156]+url[6157]+url[6158]+url[6159]+url[6160]+url[6161]+url[6162]+url[6163]+url[6164]+url[6165]+url[6166]+url[6167]+url[6168]+url[6169]+url[6170]+url[6171]+url[6172]+url[6173]+url[6174]+url[6175]+url[6176]+url[6177]+url[6178]+\
    url[6179]+url[6180]+url[6181]+url[6182]+url[6183]+url[6184]+url[6185]+url[6186]+url[6187]+url[6188]+url[6189]+url[6190]+url[6191]+url[6192]+url[6193]+url[6194]+url[6195]+url[6196]+url[6197]+url[6198]+url[6199]+url[6200]+url[6201]+url[6202]+url[6203]+url[6204]+url[6205]+url[6206]+url[6207]+url[6208]+url[6209]+url[6210]+url[6211]+url[6212]+url[6213]+url[6214]+url[6215]+url[6216]+url[6217]+url[6218]+url[6219]+url[6220]+url[6221]+url[6222]+url[6223]+url[6224]+url[6225]+url[6226]+url[6227]+url[6228]+url[6229]+url[6230]+url[6231]+url[6232]+url[6233]+url[6234]+url[6235]+url[6236]+url[6237]+url[6238]+url[6239]+url[6240]+url[6241]+url[6242]+url[6243]+url[6244]+url[6245]+url[6246]+url[6247]+url[6248]+url[6249]+url[6250]+url[6251]+url[6252]+url[6253]+url[6254]+url[6255]+url[6256]+url[6257]+url[6258]+url[6259]+url[6260]+url[6261]+url[6262]+url[6263]+url[6264]+url[6265]+url[6266]+url[6267]+url[6268]+url[6269]+url[6270]+url[6271]+url[6272]+url[6273]+url[6274]+url[6275]+url[6276]+url[6277]+url[6278]+url[6279]+\
    url[6280]+url[6281]+url[6282]+url[6283]+url[6284]+url[6285]+url[6286]+url[6287]+url[6288]+url[6289]+url[6290]+url[6291]+url[6292]+url[6293]+url[6294]+url[6295]+url[6296]+url[6297]+url[6298]+url[6299]+url[6300]+url[6301]+url[6302]+url[6303]+url[6304]+url[6305]+url[6306]+url[6307]+url[6308]+url[6309]+url[6310]+url[6311]+url[6312]+url[6313]+url[6314]+url[6315]+url[6316]+url[6317]+url[6318]+url[6319]+url[6320]+url[6321]+url[6322]+url[6323]+url[6324]+url[6325]+url[6326]+url[6327]+url[6328]+url[6329]+url[6330]+url[6331]+url[6332]+url[6333]+url[6334]+url[6335]+url[6336]+url[6337]+url[6338]+url[6339]+url[6340]+url[6341]+url[6342]+url[6343]+url[6344]+url[6345]+url[6346]+url[6347]+url[6348]+url[6349]+url[6350]+url[6351]+url[6352]+url[6353]+url[6354]+url[6355]+url[6356]+url[6357]+url[6358]+url[6359]+url[6360]+url[6361]+url[6362]+url[6363]+url[6364]+url[6365]+url[6366]+url[6367]+url[6368]+url[6369]+url[6370]+url[6371]+url[6372]+url[6373]+url[6374]+url[6375]+url[6376]+url[6377]+url[6378]+url[6379]+url[6380]+\
    url[6381]+url[6382]+url[6383]+url[6384]+url[6385]+url[6386]+url[6387]+url[6388]+url[6389]+url[6390]+url[6391]+url[6392]+url[6393]+url[6394]+url[6395]+url[6396]+url[6397]+url[6398]+url[6399]+url[6400]+url[6401]+url[6402]+url[6403]+url[6404]+url[6405]+url[6406]+url[6407]+url[6408]+url[6409]+url[6410]+url[6411]+url[6412]+url[6413]+url[6414]+url[6415]+url[6416]+url[6417]+url[6418]+url[6419]+url[6420]+url[6421]+url[6422]+url[6423]+url[6424]+url[6425]+url[6426]+url[6427]+url[6428]+url[6429]+url[6430]+url[6431]+url[6432]+url[6433]+url[6434]+url[6435]+url[6436]+url[6437]+url[6438]+url[6439]+url[6440]+url[6441]+url[6442]+url[6443]+url[6444]+url[6445]+url[6446]+url[6447]+url[6448]+url[6449]+url[6450]+url[6451]+url[6452]+url[6453]+url[6454]+url[6455]+url[6456]+url[6457]+url[6458]+url[6459]+url[6460]+url[6461]+url[6462]+url[6463]+url[6464]+url[6465]+url[6466]+url[6467]+url[6468]+url[6469]+url[6470]+url[6471]+url[6472]+url[6473]+url[6474]+url[6475]+url[6476]+url[6477]+url[6478]+url[6479]+url[6480]+url[6481]+\
    url[6482]+url[6483]+url[6484]+url[6485]+url[6486]+url[6487]+url[6488]+url[6489]+url[6490]+url[6491]+url[6492]+url[6493]+url[6494]+url[6495]+url[6496]+url[6497]+url[6498]+url[6499]+url[6500]+url[6501]+url[6502]+url[6503]+url[6504]+url[6505]+url[6506]+url[6507]+url[6508]+url[6509]+url[6510]+url[6511]+url[6512]+url[6513]+url[6514]+url[6515]+url[6516]+url[6517]+url[6518]+url[6519]+url[6520]+url[6521]+url[6522]+url[6523]+url[6524]+url[6525]+url[6526]+url[6527]+url[6528]+url[6529]+url[6530]+url[6531]+url[6532]+url[6533]+url[6534]+url[6535]+url[6536]+url[6537]+url[6538]+url[6539]+url[6540]+url[6541]+url[6542]+url[6543]+url[6544]+url[6545]+url[6546]+url[6547]+url[6548]+url[6549]+url[6550]+url[6551]+url[6552]+url[6553]+url[6554]+url[6555]+url[6556]+url[6557]+url[6558]+url[6559]+url[6560]+url[6561]+url[6562]+url[6563]+url[6564]+url[6565]+url[6566]+url[6567]+url[6568]+url[6569]+url[6570]+url[6571]+url[6572]+url[6573]+url[6574]+url[6575]+url[6576]+url[6577]+url[6578]+url[6579]+url[6580]+url[6581]+url[6582]+\
    url[6583]+url[6584]+url[6585]+url[6586]+url[6587]+url[6588]+url[6589]+url[6590]+url[6591]+url[6592]+url[6593]+url[6594]+url[6595]+url[6596]+url[6597]+url[6598]+url[6599]+url[6600]+url[6601]+url[6602]+url[6603]+url[6604]+url[6605]+url[6606]+url[6607]+url[6608]+url[6609]+url[6610]+url[6611]+url[6612]+url[6613]+url[6614]+url[6615]+url[6616]+url[6617]+url[6618]+url[6619]+url[6620]+url[6621]+url[6622]+url[6623]+url[6624]+url[6625]+url[6626]+url[6627]+url[6628]+url[6629]+url[6630]+url[6631]+url[6632]+url[6633]+url[6634]+url[6635]+url[6636]+url[6637]+url[6638]+url[6639]+url[6640]+url[6641]+url[6642]+url[6643]+url[6644]+url[6645]+url[6646]+url[6647]+url[6648]+url[6649]+url[6650]+url[6651]+url[6652]+url[6653]+url[6654]+url[6655]+url[6656]+url[6657]+url[6658]+url[6659]+url[6660]+url[6661]+url[6662]+url[6663]+url[6664]+url[6665]+url[6666]+url[6667]+url[6668]+url[6669]+url[6670]+url[6671]+url[6672]+url[6673]+url[6674]+url[6675]+url[6676]+url[6677]+url[6678]+url[6679]+url[6680]+url[6681]+url[6682]+url[6683]+\
    url[6684]+url[6685]+url[6686]+url[6687]+url[6688]+url[6689]+url[6690]+url[6691]+url[6692]+url[6693]+url[6694]+url[6695]+url[6696]+url[6697]+url[6698]+url[6699]+url[6700]+url[6701]+url[6702]+url[6703]+url[6704]+url[6705]+url[6706]+url[6707]+url[6708]+url[6709]+url[6710]+url[6711]+url[6712]+url[6713]+url[6714]+url[6715]+url[6716]+url[6717]+url[6718]+url[6719]+url[6720]+url[6721]+url[6722]+url[6723]+url[6724]+url[6725]+url[6726]+url[6727]+url[6728]+url[6729]+url[6730]+url[6731]+url[6732]+url[6733]+url[6734]+url[6735]+url[6736]+url[6737]+url[6738]+url[6739]+url[6740]+url[6741]+url[6742]+url[6743]+url[6744]+url[6745]+url[6746]+url[6747]+url[6748]+url[6749]+url[6750]+url[6751]+url[6752]+url[6753]+url[6754]+url[6755]+url[6756]+url[6757]+url[6758]+url[6759]+url[6760]+url[6761]+url[6762]+url[6763]+url[6764]+url[6765]+url[6766]+url[6767]+url[6768]+url[6769]+url[6770]+url[6771]+url[6772]+url[6773]+url[6774]+url[6775]+url[6776]+url[6777]+url[6778]+url[6779]+url[6780]+url[6781]+url[6782]+url[6783]+url[6784]+\
    url[6785]+url[6786]+url[6787]+url[6788]+url[6789]+url[6790]+url[6791]+url[6792]+url[6793]+url[6794]+url[6795]+url[6796]+url[6797]+url[6798]+url[6799]+url[6800]+url[6801]+url[6802]+url[6803]+url[6804]+url[6805]+url[6806]+url[6807]+url[6808]+url[6809]+url[6810]+url[6811]+url[6812]+url[6813]+url[6814]+url[6815]+url[6816]+url[6817]+url[6818]+url[6819]+url[6820]+url[6821]+url[6822]+url[6823]+url[6824]+url[6825]+url[6826]+url[6827]+url[6828]+url[6829]+url[6830]+url[6831]+url[6832]+url[6833]+url[6834]+url[6835]+url[6836]+url[6837]+url[6838]+url[6839]+url[6840]+url[6841]+url[6842]+url[6843]+url[6844]+url[6845]+url[6846]+url[6847]+url[6848]+url[6849]+url[6850]+url[6851]+url[6852]+url[6853]+url[6854]+url[6855]+url[6856]+url[6857]+url[6858]+url[6859]+url[6860]+url[6861]+url[6862]+url[6863]+url[6864]+url[6865]+url[6866]+url[6867]+url[6868]+url[6869]+url[6870]+url[6871]+url[6872]+url[6873]+url[6874]+url[6875]+url[6876]+url[6877]+url[6878]+url[6879]+url[6880]+url[6881]+url[6882]+url[6883]+url[6884]+url[6885]+\
    url[6886]+url[6887]+url[6888]+url[6889]+url[6890]+url[6891]+url[6892]+url[6893]+url[6894]+url[6895]+url[6896]+url[6897]+url[6898]+url[6899]+url[6900]+url[6901]+url[6902]+url[6903]+url[6904]+url[6905]+url[6906]+url[6907]+url[6908]+url[6909]+url[6910]+url[6911]+url[6912]+url[6913]+url[6914]+url[6915]+url[6916]+url[6917]+url[6918]+url[6919]+url[6920]+url[6921]+url[6922]+url[6923]+url[6924]+url[6925]+url[6926]+url[6927]+url[6928]+url[6929]+url[6930]+url[6931]+url[6932]+url[6933]+url[6934]+url[6935]+url[6936]+url[6937]+url[6938]+url[6939]+url[6940]+url[6941]+url[6942]+url[6943]+url[6944]+url[6945]+url[6946]+url[6947]+url[6948]+url[6949]+url[6950]+url[6951]+url[6952]+url[6953]+url[6954]+url[6955]+url[6956]+url[6957]+url[6958]+url[6959]+url[6960]+url[6961]+url[6962]+url[6963]+url[6964]+url[6965]+url[6966]+url[6967]+url[6968]+url[6969]+url[6970]+url[6971]+url[6972]+url[6973]+url[6974]+url[6975]+url[6976]+url[6977]+url[6978]+url[6979]+url[6980]+url[6981]+url[6982]+url[6983]+url[6984]+url[6985]+url[6986]+\
    url[6987]+url[6988]+url[6989]+url[6990]+url[6991]+url[6992]+url[6993]+url[6994]+url[6995]+url[6996]+url[6997]+url[6998]+url[6999]+url[7000]+url[7001]+url[7002]+url[7003]+url[7004]+url[7005]+url[7006]+url[7007]+url[7008]+url[7009]+url[7010]+url[7011]+url[7012]+url[7013]+url[7014]+url[7015]+url[7016]+url[7017]+url[7018]+url[7019]+url[7020]+url[7021]+url[7022]+url[7023]+url[7024]+url[7025]+url[7026]+url[7027]+url[7028]+url[7029]+url[7030]+url[7031]+url[7032]+url[7033]+url[7034]+url[7035]+url[7036]+url[7037]+url[7038]+url[7039]+url[7040]+url[7041]+url[7042]+url[7043]+url[7044]+url[7045]+url[7046]+url[7047]+url[7048]+url[7049]+url[7050]+url[7051]+url[7052]+url[7053]+url[7054]+url[7055]+url[7056]+url[7057]+url[7058]+url[7059]+url[7060]+url[7061]+url[7062]+url[7063]+url[7064]+url[7065]+url[7066]+url[7067]+url[7068]+url[7069]+url[7070]+url[7071]+url[7072]+url[7073]+url[7074]+url[7075]+url[7076]+url[7077]+url[7078]+url[7079]+url[7080]+url[7081]+url[7082]+url[7083]+url[7084]+url[7085]+url[7086]+url[7087]+\
    url[7088]+url[7089]+url[7090]+url[7091]+url[7092]+url[7093]+url[7094]+url[7095]+url[7096]+url[7097]+url[7098]+url[7099]+url[7100]+url[7101]+url[7102]+url[7103]+url[7104]+url[7105]+url[7106]+url[7107]+url[7108]+url[7109]+url[7110]+url[7111]+url[7112]+url[7113]+url[7114]+url[7115]+url[7116]+url[7117]+url[7118]+url[7119]+url[7120]+url[7121]+url[7122]+url[7123]+url[7124]+url[7125]+url[7126]+url[7127]+url[7128]+url[7129]+url[7130]+url[7131]+url[7132]+url[7133]+url[7134]+url[7135]+url[7136]+url[7137]+url[7138]+url[7139]+url[7140]+url[7141]+url[7142]+url[7143]+url[7144]+url[7145]+url[7146]+url[7147]+url[7148]+url[7149]+url[7150]+url[7151]+url[7152]+url[7153]+url[7154]+url[7155]+url[7156]+url[7157]+url[7158]+url[7159]+url[7160]+url[7161]+url[7162]+url[7163]+url[7164]+url[7165]+url[7166]+url[7167]+url[7168]+url[7169]+url[7170]+url[7171]+url[7172]+url[7173]+url[7174]+url[7175]+url[7176]+url[7177]+url[7178]+url[7179]+url[7180]+url[7181]+url[7182]+url[7183]+url[7184]+url[7185]+url[7186]+url[7187]+url[7188]+\
    url[7189]+url[7190]+url[7191]+url[7192]+url[7193]+url[7194]+url[7195]+url[7196]+url[7197]+url[7198]+url[7199]+url[7200]+url[7201]+url[7202]+url[7203]+url[7204]+url[7205]+url[7206]+url[7207]+url[7208]+url[7209]+url[7210]+url[7211]+url[7212]+url[7213]+url[7214]+url[7215]+url[7216]+url[7217]+url[7218]+url[7219]+url[7220]+url[7221]+url[7222]+url[7223]+url[7224]+url[7225]+url[7226]+url[7227]+url[7228]+url[7229]+url[7230]+url[7231]+url[7232]+url[7233]+url[7234]+url[7235]+url[7236]+url[7237]+url[7238]+url[7239]+url[7240]+url[7241]+url[7242]+url[7243]+url[7244]+url[7245]+url[7246]+url[7247]+url[7248]+url[7249]+url[7250]+url[7251]+url[7252]+url[7253]+url[7254]+url[7255]+url[7256]+url[7257]+url[7258]+url[7259]+url[7260]+url[7261]+url[7262]+url[7263]+url[7264]+url[7265]+url[7266]+url[7267]+url[7268]+url[7269]+url[7270]+url[7271]+url[7272]+url[7273]+url[7274]+url[7275]+url[7276]+url[7277]+url[7278]+url[7279]+url[7280]+url[7281]+url[7282]+url[7283]+url[7284]+url[7285]+url[7286]+url[7287]+url[7288]+url[7289]+\
    url[7290]+url[7291]+url[7292]+url[7293]+url[7294]+url[7295]+url[7296]+url[7297]+url[7298]+url[7299]+url[7300]+url[7301]+url[7302]+url[7303]+url[7304]+url[7305]+url[7306]+url[7307]+url[7308]+url[7309]+url[7310]+url[7311]+url[7312]+url[7313]+url[7314]+url[7315]+url[7316]+url[7317]+url[7318]+url[7319]+url[7320]+url[7321]+url[7322]+url[7323]+url[7324]+url[7325]+url[7326]+url[7327]+url[7328]+url[7329]+url[7330]+url[7331]+url[7332]+url[7333]+url[7334]+url[7335]+url[7336]+url[7337]+url[7338]+url[7339]+url[7340]+url[7341]+url[7342]+url[7343]+url[7344]+url[7345]+url[7346]+url[7347]+url[7348]+url[7349]+url[7350]+url[7351]+url[7352]+url[7353]+url[7354]+url[7355]+url[7356]+url[7357]+url[7358]+url[7359]+url[7360]+url[7361]+url[7362]+url[7363]+url[7364]+url[7365]+url[7366]+url[7367]+url[7368]+url[7369]+url[7370]+url[7371]+url[7372]+url[7373]+url[7374]+url[7375]+url[7376]+url[7377]+url[7378]+url[7379]+url[7380]+url[7381]+url[7382]+url[7383]+url[7384]+url[7385]+url[7386]+url[7387]+url[7388]+url[7389]+url[7390]+\
    url[7391]+url[7392]+url[7393]+url[7394]+url[7395]+url[7396]+url[7397]+url[7398]+url[7399]+url[7400]+url[7401]+url[7402]+url[7403]+url[7404]+url[7405]+url[7406]+url[7407]+url[7408]+url[7409]+url[7410]+url[7411]+url[7412]+url[7413]+url[7414]+url[7415]+url[7416]+url[7417]+url[7418]+url[7419]+url[7420]+url[7421]+url[7422]+url[7423]+url[7424]+url[7425]+url[7426]+url[7427]+url[7428]+url[7429]+url[7430]+url[7431]+url[7432]+url[7433]+url[7434]+url[7435]+url[7436]+url[7437]+url[7438]+url[7439]+url[7440]+url[7441]+url[7442]+url[7443]+url[7444]+url[7445]+url[7446]+url[7447]+url[7448]+url[7449]+url[7450]+url[7451]+url[7452]+url[7453]+url[7454]+url[7455]+url[7456]+url[7457]+url[7458]+url[7459]+url[7460]+url[7461]+url[7462]+url[7463]+url[7464]+url[7465]+url[7466]+url[7467]+url[7468]+url[7469]+url[7470]+url[7471]+url[7472]+url[7473]+url[7474]+url[7475]+url[7476]+url[7477]+url[7478]+url[7479]+url[7480]+url[7481]+url[7482]+url[7483]+url[7484]+url[7485]+url[7486]+url[7487]+url[7488]+url[7489]+url[7490]+url[7491]+\
    url[7492]+url[7493]+url[7494]+url[7495]+url[7496]+url[7497]+url[7498]+url[7499]+url[7500]+url[7501]+url[7502]+url[7503]+url[7504]+url[7505]+url[7506]+url[7507]+url[7508]+url[7509]+url[7510]+url[7511]+url[7512]+url[7513]+url[7514]+url[7515]+url[7516]+url[7517]+url[7518]+url[7519]+url[7520]+url[7521]+url[7522]+url[7523]+url[7524]+url[7525]+url[7526]+url[7527]+url[7528]+url[7529]+url[7530]+url[7531]+url[7532]+url[7533]+url[7534]+url[7535]+url[7536]+url[7537]+url[7538]+url[7539]+url[7540]+url[7541]+url[7542]+url[7543]+url[7544]+url[7545]+url[7546]+url[7547]+url[7548]+url[7549]+url[7550]+url[7551]+url[7552]+url[7553]+url[7554]+url[7555]+url[7556]+url[7557]+url[7558]+url[7559]+url[7560]+url[7561]+url[7562]+url[7563]+url[7564]+url[7565]+url[7566]+url[7567]+url[7568]+url[7569]+url[7570]+url[7571]+url[7572]+url[7573]+url[7574]+url[7575]+url[7576]+url[7577]+url[7578]+url[7579]+url[7580]+url[7581]+url[7582]+url[7583]+url[7584]+url[7585]+url[7586]+url[7587]+url[7588]+url[7589]+url[7590]+url[7591]+url[7592]+\
    url[7593]+url[7594]+url[7595]+url[7596]+url[7597]+url[7598]+url[7599]+url[7600]+url[7601]+url[7602]+url[7603]+url[7604]+url[7605]+url[7606]+url[7607]+url[7608]+url[7609]+url[7610]+url[7611]+url[7612]+url[7613]+url[7614]+url[7615]+url[7616]+url[7617]+url[7618]+url[7619]+url[7620]+url[7621]+url[7622]+url[7623]+url[7624]+url[7625]+url[7626]+url[7627]+url[7628]+url[7629]+url[7630]+url[7631]+url[7632]+url[7633]+url[7634]+url[7635]+url[7636]+url[7637]+url[7638]+url[7639]+url[7640]+url[7641]+url[7642]+url[7643]+url[7644]+url[7645]+url[7646]+url[7647]+url[7648]+url[7649]+url[7650]+url[7651]+url[7652]+url[7653]+url[7654]+url[7655]+url[7656]+url[7657]+url[7658]+url[7659]+url[7660]+url[7661]+url[7662]+url[7663]+url[7664]+url[7665]+url[7666]+url[7667]+url[7668]+url[7669]+url[7670]+url[7671]+url[7672]+url[7673]+url[7674]+url[7675]+url[7676]+url[7677]+url[7678]+url[7679]+url[7680]+url[7681]+url[7682]+url[7683]+url[7684]+url[7685]+url[7686]+url[7687]+url[7688]+url[7689]+url[7690]+url[7691]+url[7692]+url[7693]+\
    url[7694]+url[7695]+url[7696]+url[7697]+url[7698]+url[7699]+url[7700]+url[7701]+url[7702]+url[7703]+url[7704]+url[7705]+url[7706]+url[7707]+url[7708]+url[7709]+url[7710]+url[7711]+url[7712]+url[7713]+url[7714]+url[7715]+url[7716]+url[7717]+url[7718]+url[7719]+url[7720]+url[7721]+url[7722]+url[7723]+url[7724]+url[7725]+url[7726]+url[7727]+url[7728]+url[7729]+url[7730]+url[7731]+url[7732]+url[7733]+url[7734]+url[7735]+url[7736]+url[7737]+url[7738]+url[7739]+url[7740]+url[7741]+url[7742]+url[7743]+url[7744]+url[7745]+url[7746]+url[7747]+url[7748]+url[7749]+url[7750]+url[7751]+url[7752]+url[7753]+url[7754]+url[7755]+url[7756]+url[7757]+url[7758]+url[7759]+url[7760]+url[7761]+url[7762]+url[7763]+url[7764]+url[7765]+url[7766]+url[7767]+url[7768]+url[7769]+url[7770]+url[7771]+url[7772]+url[7773]+url[7774]+url[7775]+url[7776]+url[7777]+url[7778]+url[7779]+url[7780]+url[7781]+url[7782]+url[7783]+url[7784]+url[7785]+url[7786]+url[7787]+url[7788]+url[7789]+url[7790]+url[7791]+url[7792]+url[7793]+url[7794]+\
    url[7795]+url[7796]+url[7797]+url[7798]+url[7799]+url[7800]+url[7801]+url[7802]+url[7803]+url[7804]+url[7805]+url[7806]+url[7807]+url[7808]+url[7809]+url[7810]+url[7811]+url[7812]+url[7813]+url[7814]+url[7815]+url[7816]+url[7817]+url[7818]+url[7819]+url[7820]+url[7821]+url[7822]+url[7823]+url[7824]+url[7825]+url[7826]+url[7827]+url[7828]+url[7829]+url[7830]+url[7831]+url[7832]+url[7833]+url[7834]+url[7835]+url[7836]+url[7837]+url[7838]+url[7839]+url[7840]+url[7841]+url[7842]+url[7843]+url[7844]+url[7845]+url[7846]+url[7847]+url[7848]+url[7849]+url[7850]+url[7851]+url[7852]+url[7853]+url[7854]+url[7855]+url[7856]+url[7857]+url[7858]+url[7859]+url[7860]+url[7861]+url[7862]+url[7863]+url[7864]+url[7865]+url[7866]+url[7867]+url[7868]+url[7869]+url[7870]+url[7871]+url[7872]+url[7873]+url[7874]+url[7875]+url[7876]+url[7877]+url[7878]+url[7879]+url[7880]+url[7881]+url[7882]+url[7883]+url[7884]+url[7885]+url[7886]+url[7887]+url[7888]+url[7889]+url[7890]+url[7891]+url[7892]+url[7893]+url[7894]+url[7895]+\
    url[7896]+url[7897]+url[7898]+url[7899]+url[7900]+url[7901]+url[7902]+url[7903]+url[7904]+url[7905]+url[7906]+url[7907]+url[7908]+url[7909]+url[7910]+url[7911]+url[7912]+url[7913]+url[7914]+url[7915]+url[7916]+url[7917]+url[7918]+url[7919]+url[7920]+url[7921]+url[7922]+url[7923]+url[7924]+url[7925]+url[7926]+url[7927]+url[7928]+url[7929]+url[7930]+url[7931]+url[7932]+url[7933]+url[7934]+url[7935]+url[7936]+url[7937]+url[7938]+url[7939]+url[7940]+url[7941]+url[7942]+url[7943]+url[7944]+url[7945]+url[7946]+url[7947]+url[7948]+url[7949]+url[7950]+url[7951]+url[7952]+url[7953]+url[7954]+url[7955]+url[7956]+url[7957]+url[7958]+url[7959]+url[7960]+url[7961]+url[7962]+url[7963]+url[7964]+url[7965]+url[7966]+url[7967]+url[7968]+url[7969]+url[7970]+url[7971]+url[7972]+url[7973]+url[7974]+url[7975]+url[7976]+url[7977]+url[7978]+url[7979]+url[7980]+url[7981]+url[7982]+url[7983]+url[7984]+url[7985]+url[7986]+url[7987]+url[7988]+url[7989]+url[7990]+url[7991]+url[7992]+url[7993]+url[7994]+url[7995]+url[7996]+\
    url[7997]+url[7998]+url[7999]+url[8000]+url[8001]+url[8002]+url[8003]+url[8004]+url[8005]+url[8006]+url[8007]+url[8008]+url[8009]+url[8010]+url[8011]+url[8012]+url[8013]+url[8014]+url[8015]+url[8016]+url[8017]+url[8018]+url[8019]+url[8020]+url[8021]+url[8022]+url[8023]+url[8024]+url[8025]+url[8026]+url[8027]+url[8028]+url[8029]+url[8030]+url[8031]+url[8032]+url[8033]+url[8034]+url[8035]+url[8036]+url[8037]+url[8038]+url[8039]+url[8040]+url[8041]+url[8042]+url[8043]+url[8044]+url[8045]+url[8046]+url[8047]+url[8048]+url[8049]+url[8050]+url[8051]+url[8052]+url[8053]+url[8054]+url[8055]+url[8056]+url[8057]+url[8058]+url[8059]+url[8060]+url[8061]+url[8062]+url[8063]+url[8064]+url[8065]+url[8066]+url[8067]+url[8068]+url[8069]+url[8070]+url[8071]+url[8072]+url[8073]+url[8074]+url[8075]+url[8076]+url[8077]+url[8078]+url[8079]+url[8080]+url[8081]+url[8082]+url[8083]+url[8084]+url[8085]+url[8086]+url[8087]+url[8088]+url[8089]+url[8090]+url[8091]+url[8092]+url[8093]+url[8094]+url[8095]+url[8096]+url[8097]+\
    url[8098]+url[8099]+url[8100]+url[8101]+url[8102]+url[8103]+url[8104]+url[8105]+url[8106]+url[8107]+url[8108]+url[8109]+url[8110]+url[8111]+url[8112]+url[8113]+url[8114]+url[8115]+url[8116]+url[8117]+url[8118]+url[8119]+url[8120]+url[8121]+url[8122]+url[8123]+url[8124]+url[8125]+url[8126]+url[8127]+url[8128]+url[8129]+url[8130]+url[8131]+url[8132]+url[8133]+url[8134]+url[8135]+url[8136]+url[8137]+url[8138]+url[8139]+url[8140]+url[8141]+url[8142]+url[8143]+url[8144]+url[8145]+url[8146]+url[8147]+url[8148]+url[8149]+url[8150]+url[8151]+url[8152]+url[8153]+url[8154]+url[8155]+url[8156]+url[8157]+url[8158]+url[8159]+url[8160]+url[8161]+url[8162]+url[8163]+url[8164]+url[8165]+url[8166]+url[8167]+url[8168]+url[8169]+url[8170]+url[8171]+url[8172]+url[8173]+url[8174]+url[8175]+url[8176]+url[8177]+url[8178]+url[8179]+url[8180]+url[8181]+url[8182]+url[8183]+url[8184]+url[8185]+url[8186]+url[8187]+url[8188]+url[8189]+url[8190]+url[8191]+url[8192]+url[8193]+url[8194]+url[8195]+url[8196]+url[8197]+url[8198]+\
    url[8199]+url[8200]+url[8201]+url[8202]+url[8203]+url[8204]+url[8205]+url[8206]+url[8207]+url[8208]+url[8209]+url[8210]+url[8211]+url[8212]+url[8213]+url[8214]+url[8215]+url[8216]+url[8217]+url[8218]+url[8219]+url[8220]+url[8221]+url[8222]+url[8223]+url[8224]+url[8225]+url[8226]+url[8227]+url[8228]+url[8229]+url[8230]+url[8231]+url[8232]+url[8233]+url[8234]+url[8235]+url[8236]+url[8237]+url[8238]+url[8239]+url[8240]+url[8241]+url[8242]+url[8243]+url[8244]+url[8245]+url[8246]+url[8247]+url[8248]+url[8249]+url[8250]+url[8251]+url[8252]+url[8253]+url[8254]+url[8255]+url[8256]+url[8257]+url[8258]+url[8259]+url[8260]+url[8261]+url[8262]+url[8263]+url[8264]+url[8265]+url[8266]+url[8267]+url[8268]+url[8269]+url[8270]+url[8271]+url[8272]+url[8273]+url[8274]+url[8275]+url[8276]+url[8277]+url[8278]+url[8279]+url[8280]+url[8281]+url[8282]+url[8283]+url[8284]+url[8285]+url[8286]+url[8287]+url[8288]+url[8289]+url[8290]+url[8291]+url[8292]+url[8293]+url[8294]+url[8295]+url[8296]+url[8297]+url[8298]+url[8299]+\
    url[8300]+url[8301]+url[8302]+url[8303]+url[8304]+url[8305]+url[8306]+url[8307]+url[8308]+url[8309]+url[8310]+url[8311]+url[8312]+url[8313]+url[8314]+url[8315]+url[8316]+url[8317]+url[8318]+url[8319]+url[8320]+url[8321]+url[8322]+url[8323]+url[8324]+url[8325]+url[8326]+url[8327]+url[8328]+url[8329]+url[8330]+url[8331]+url[8332]+url[8333]+url[8334]+url[8335]+url[8336]+url[8337]+url[8338]+url[8339]+url[8340]+url[8341]+url[8342]+url[8343]+url[8344]+url[8345]+url[8346]+url[8347]+url[8348]+url[8349]+url[8350]+url[8351]+url[8352]+url[8353]+url[8354]+url[8355]+url[8356]+url[8357]+url[8358]+url[8359]+url[8360]+url[8361]+url[8362]+url[8363]+url[8364]+url[8365]+url[8366]+url[8367]+url[8368]+url[8369]+url[8370]+url[8371]+url[8372]+url[8373]+url[8374]+url[8375]+url[8376]+url[8377]+url[8378]+url[8379]+url[8380]+url[8381]+url[8382]+url[8383]+url[8384]+url[8385]+url[8386]+url[8387]+url[8388]+url[8389]+url[8390]+url[8391]+url[8392]+url[8393]+url[8394]+url[8395]+url[8396]+url[8397]+url[8398]+url[8399]+url[8400]+\
    url[8401]+url[8402]+url[8403]+url[8404]+url[8405]+url[8406]+url[8407]+url[8408]+url[8409]+url[8410]+url[8411]+url[8412]+url[8413]+url[8414]+url[8415]+url[8416]+url[8417]+url[8418]+url[8419]+url[8420]+url[8421]+url[8422]+url[8423]+url[8424]+url[8425]+url[8426]+url[8427]+url[8428]+url[8429]+url[8430]+url[8431]+url[8432]+url[8433]+url[8434]+url[8435]+url[8436]+url[8437]+url[8438]+url[8439]+url[8440]+url[8441]+url[8442]+url[8443]+url[8444]+url[8445]+url[8446]+url[8447]+url[8448]+url[8449]+url[8450]+url[8451]+url[8452]+url[8453]+url[8454]+url[8455]+url[8456]+url[8457]+url[8458]+url[8459]+url[8460]+url[8461]+url[8462]+url[8463]+url[8464]+url[8465]+url[8466]+url[8467]+url[8468]+url[8469]+url[8470]+url[8471]+url[8472]+url[8473]+url[8474]+url[8475]+url[8476]+url[8477]+url[8478]+url[8479]+url[8480]+url[8481]+url[8482]+url[8483]+url[8484]+url[8485]+url[8486]+url[8487]+url[8488]+url[8489]+url[8490]+url[8491]+url[8492]+url[8493]+url[8494]+url[8495]+url[8496]+url[8497]+url[8498]+url[8499]+url[8500]+url[8501]+\
    url[8502]+url[8503]+url[8504]+url[8505]+url[8506]+url[8507]+url[8508]+url[8509]+url[8510]+url[8511]+url[8512]+url[8513]+url[8514]+url[8515]+url[8516]+url[8517]+url[8518]+url[8519]+url[8520]+url[8521]+url[8522]+url[8523]+url[8524]+url[8525]+url[8526]+url[8527]+url[8528]+url[8529]+url[8530]+url[8531]+url[8532]+url[8533]+url[8534]+url[8535]+url[8536]+url[8537]+url[8538]+url[8539]+url[8540]+url[8541]+url[8542]+url[8543]+url[8544]+url[8545]+url[8546]+url[8547]+url[8548]+url[8549]+url[8550]+url[8551]+url[8552]+url[8553]+url[8554]+url[8555]+url[8556]+url[8557]+url[8558]+url[8559]+url[8560]+url[8561]+url[8562]+url[8563]+url[8564]+url[8565]+url[8566]+url[8567]+url[8568]+url[8569]+url[8570]+url[8571]+url[8572]+url[8573]+url[8574]+url[8575]+url[8576]+url[8577]+url[8578]+url[8579]+url[8580]+url[8581]+url[8582]+url[8583]+url[8584]+url[8585]+url[8586]+url[8587]+url[8588]+url[8589]+url[8590]+url[8591]+url[8592]+url[8593]+url[8594]+url[8595]+url[8596]+url[8597]+url[8598]+url[8599]+url[8600]+url[8601]+url[8602]+\
    url[8603]+url[8604]+url[8605]+url[8606]+url[8607]+url[8608]+url[8609]+url[8610]+url[8611]+url[8612]+url[8613]+url[8614]+url[8615]+url[8616]+url[8617]+url[8618]+url[8619]+url[8620]+url[8621]+url[8622]+url[8623]+url[8624]+url[8625]+url[8626]+url[8627]+url[8628]+url[8629]+url[8630]+url[8631]+url[8632]+url[8633]+url[8634]+url[8635]+url[8636]+url[8637]+url[8638]+url[8639]+url[8640]+url[8641]+url[8642]+url[8643]+url[8644]+url[8645]+url[8646]+url[8647]+url[8648]+url[8649]+url[8650]+url[8651]+url[8652]+url[8653]+url[8654]+url[8655]+url[8656]+url[8657]+url[8658]+url[8659]+url[8660]+url[8661]+url[8662]+url[8663]+url[8664]+url[8665]+url[8666]+url[8667]+url[8668]+url[8669]+url[8670]+url[8671]+url[8672]+url[8673]+url[8674]+url[8675]+url[8676]+url[8677]+url[8678]+url[8679]+url[8680]+url[8681]+url[8682]+url[8683]+url[8684]+url[8685]+url[8686]+url[8687]+url[8688]+url[8689]+url[8690]+url[8691]+url[8692]+url[8693]+url[8694]+url[8695]+url[8696]+url[8697]+url[8698]+url[8699]+url[8700]+url[8701]+url[8702]+url[8703]+\
    url[8704]+url[8705]+url[8706]+url[8707]+url[8708]+url[8709]+url[8710]+url[8711]+url[8712]+url[8713]+url[8714]+url[8715]+url[8716]+url[8717]+url[8718]+url[8719]+url[8720]+url[8721]+url[8722]+url[8723]+url[8724]+url[8725]+url[8726]+url[8727]+url[8728]+url[8729]+url[8730]+url[8731]+url[8732]+url[8733]+url[8734]+url[8735]+url[8736]+url[8737]+url[8738]+url[8739]+url[8740]+url[8741]+url[8742]+url[8743]+url[8744]+url[8745]+url[8746]+url[8747]+url[8748]+url[8749]+url[8750]+url[8751]+url[8752]+url[8753]+url[8754]+url[8755]+url[8756]+url[8757]+url[8758]+url[8759]+url[8760]+url[8761]+url[8762]+url[8763]+url[8764]+url[8765]+url[8766]+url[8767]+url[8768]+url[8769]+url[8770]+url[8771]+url[8772]+url[8773]+url[8774]+url[8775]+url[8776]+url[8777]+url[8778]+url[8779]+url[8780]+url[8781]+url[8782]+url[8783]+url[8784]+url[8785]+url[8786]+url[8787]+url[8788]+url[8789]+url[8790]+url[8791]+url[8792]+url[8793]+url[8794]+url[8795]+url[8796]+url[8797]+url[8798]+url[8799]+url[8800]+url[8801]+url[8802]+url[8803]+url[8804]+\
    url[8805]+url[8806]+url[8807]+url[8808]+url[8809]+url[8810]+url[8811]+url[8812]+url[8813]+url[8814]+url[8815]+url[8816]+url[8817]+url[8818]+url[8819]+url[8820]+url[8821]+url[8822]+url[8823]+url[8824]+url[8825]+url[8826]+url[8827]+url[8828]+url[8829]+url[8830]+url[8831]+url[8832]+url[8833]+url[8834]+url[8835]+url[8836]+url[8837]+url[8838]+url[8839]+url[8840]+url[8841]+url[8842]+url[8843]+url[8844]+url[8845]+url[8846]+url[8847]+url[8848]+url[8849]+url[8850]+url[8851]+url[8852]+url[8853]+url[8854]+url[8855]+url[8856]+url[8857]+url[8858]+url[8859]+url[8860]+url[8861]+url[8862]+url[8863]+url[8864]+url[8865]+url[8866]+url[8867]+url[8868]+url[8869]+url[8870]+url[8871]+url[8872]+url[8873]+url[8874]+url[8875]+url[8876]+url[8877]+url[8878]+url[8879]+url[8880]+url[8881]+url[8882]+url[8883]+url[8884]+url[8885]+url[8886]+url[8887]+url[8888]+url[8889]+url[8890]+url[8891]+url[8892]+url[8893]+url[8894]+url[8895]+url[8896]+url[8897]+url[8898]+url[8899]+url[8900]+url[8901]+url[8902]+url[8903]+url[8904]+url[8905]+\
    url[8906]+url[8907]+url[8908]+url[8909]+url[8910]+url[8911]+url[8912]+url[8913]+url[8914]+url[8915]+url[8916]+url[8917]+url[8918]+url[8919]+url[8920]+url[8921]+url[8922]+url[8923]+url[8924]+url[8925]+url[8926]+url[8927]+url[8928]+url[8929]+url[8930]+url[8931]+url[8932]+url[8933]+url[8934]+url[8935]+url[8936]+url[8937]+url[8938]+url[8939]+url[8940]+url[8941]+url[8942]+url[8943]+url[8944]+url[8945]+url[8946]+url[8947]+url[8948]+url[8949]+url[8950]+url[8951]+url[8952]+url[8953]+url[8954]+url[8955]+url[8956]+url[8957]+url[8958]+url[8959]+url[8960]+url[8961]+url[8962]+url[8963]+url[8964]+url[8965]+url[8966]+url[8967]+url[8968]+url[8969]+url[8970]+url[8971]+url[8972]+url[8973]+url[8974]+url[8975]+url[8976]+url[8977]+url[8978]+url[8979]+url[8980]+url[8981]+url[8982]+url[8983]+url[8984]+url[8985]+url[8986]+url[8987]+url[8988]+url[8989]+url[8990]+url[8991]+url[8992]+url[8993]+url[8994]+url[8995]+url[8996]+url[8997]+url[8998]+url[8999]+url[9000]+url[9001]+url[9002]+url[9003]+url[9004]+url[9005]+url[9006]+\
    url[9007]+url[9008]+url[9009]+url[9010]+url[9011]+url[9012]+url[9013]+url[9014]+url[9015]+url[9016]+url[9017]+url[9018]+url[9019]+url[9020]+url[9021]+url[9022]+url[9023]+url[9024]+url[9025]+url[9026]+url[9027]+url[9028]+url[9029]+url[9030]+url[9031]+url[9032]+url[9033]+url[9034]+url[9035]+url[9036]+url[9037]+url[9038]+url[9039]+url[9040]+url[9041]+url[9042]+url[9043]+url[9044]+url[9045]+url[9046]+url[9047]+url[9048]+url[9049]+url[9050]+url[9051]+url[9052]+url[9053]+url[9054]+url[9055]+url[9056]+url[9057]+url[9058]+url[9059]+url[9060]+url[9061]+url[9062]+url[9063]+url[9064]+url[9065]+url[9066]+url[9067]+url[9068]+url[9069]+url[9070]+url[9071]+url[9072]+url[9073]+url[9074]+url[9075]+url[9076]+url[9077]+url[9078]+url[9079]+url[9080]+url[9081]+url[9082]+url[9083]+url[9084]+url[9085]+url[9086]+url[9087]+url[9088]+url[9089]+url[9090]+url[9091]+url[9092]+url[9093]+url[9094]+url[9095]+url[9096]+url[9097]+url[9098]+url[9099]+url[9100]+url[9101]+url[9102]+url[9103]+url[9104]+url[9105]+url[9106]+url[9107]+\
    url[9108]+url[9109]+url[9110]+url[9111]+url[9112]+url[9113]+url[9114]+url[9115]+url[9116]+url[9117]+url[9118]+url[9119]+url[9120]+url[9121]+url[9122]+url[9123]+url[9124]+url[9125]+url[9126]+url[9127]+url[9128]+url[9129]+url[9130]+url[9131]+url[9132]+url[9133]+url[9134]+url[9135]+url[9136]+url[9137]+url[9138]+url[9139]+url[9140]+url[9141]+url[9142]+url[9143]+url[9144]+url[9145]+url[9146]+url[9147]+url[9148]+url[9149]+url[9150]+url[9151]+url[9152]+url[9153]+url[9154]+url[9155]+url[9156]+url[9157]+url[9158]+url[9159]+url[9160]+url[9161]+url[9162]+url[9163]+url[9164]+url[9165]+url[9166]+url[9167]+url[9168]+url[9169]+url[9170]+url[9171]+url[9172]+url[9173]+url[9174]+url[9175]+url[9176]+url[9177]+url[9178]+url[9179]+url[9180]+url[9181]+url[9182]+url[9183]+url[9184]+url[9185]+url[9186]+url[9187]+url[9188]+url[9189]+url[9190]+url[9191]+url[9192]+url[9193]+url[9194]+url[9195]+url[9196]+url[9197]+url[9198]+url[9199]+url[9200]+url[9201]+url[9202]+url[9203]+url[9204]+url[9205]+url[9206]+url[9207]+url[9208]+\
    url[9209]+url[9210]+url[9211]+url[9212]+url[9213]+url[9214]+url[9215]+url[9216]+url[9217]+url[9218]+url[9219]+url[9220]+url[9221]+url[9222]+url[9223]+url[9224]+url[9225]+url[9226]+url[9227]+url[9228]+url[9229]+url[9230]+url[9231]+url[9232]+url[9233]+url[9234]+url[9235]+url[9236]+url[9237]+url[9238]+url[9239]+url[9240]+url[9241]+url[9242]+url[9243]+url[9244]+url[9245]+url[9246]+url[9247]+url[9248]+url[9249]+url[9250]+url[9251]+url[9252]+url[9253]+url[9254]+url[9255]+url[9256]+url[9257]+url[9258]+url[9259]+url[9260]+url[9261]+url[9262]+url[9263]+url[9264]+url[9265]+url[9266]+url[9267]+url[9268]+url[9269]+url[9270]+url[9271]+url[9272]+url[9273]+url[9274]+url[9275]+url[9276]+url[9277]+url[9278]+url[9279]+url[9280]+url[9281]+url[9282]+url[9283]+url[9284]+url[9285]+url[9286]+url[9287]+url[9288]+url[9289]+url[9290]+url[9291]+url[9292]+url[9293]+url[9294]+url[9295]+url[9296]+url[9297]+url[9298]+url[9299]+url[9300]+url[9301]+url[9302]+url[9303]+url[9304]+url[9305]+url[9306]+url[9307]+url[9308]+url[9309]+\
    url[9310]+url[9311]+url[9312]+url[9313]+url[9314]+url[9315]+url[9316]+url[9317]+url[9318]+url[9319]+url[9320]+url[9321]+url[9322]+url[9323]+url[9324]+url[9325]+url[9326]+url[9327]+url[9328]+url[9329]+url[9330]+url[9331]+url[9332]+url[9333]+url[9334]+url[9335]+url[9336]+url[9337]+url[9338]+url[9339]+url[9340]+url[9341]+url[9342]+url[9343]+url[9344]+url[9345]+url[9346]+url[9347]+url[9348]+url[9349]+url[9350]+url[9351]+url[9352]+url[9353]+url[9354]+url[9355]+url[9356]+url[9357]+url[9358]+url[9359]+url[9360]+url[9361]+url[9362]+url[9363]+url[9364]+url[9365]+url[9366]+url[9367]+url[9368]+url[9369]+url[9370]+url[9371]+url[9372]+url[9373]+url[9374]+url[9375]+url[9376]+url[9377]+url[9378]+url[9379]+url[9380]+url[9381]+url[9382]+url[9383]+url[9384]+url[9385]+url[9386]+url[9387]+url[9388]+url[9389]+url[9390]+url[9391]+url[9392]+url[9393]+url[9394]+url[9395]+url[9396]+url[9397]+url[9398]+url[9399]+url[9400]+url[9401]+url[9402]+url[9403]+url[9404]+url[9405]+url[9406]+url[9407]+url[9408]+url[9409]+url[9410]+\
    url[9411]+url[9412]+url[9413]+url[9414]+url[9415]+url[9416]+url[9417]+url[9418]+url[9419]+url[9420]+url[9421]+url[9422]+url[9423]+url[9424]+url[9425]+url[9426]+url[9427]+url[9428]+url[9429]+url[9430]+url[9431]+url[9432]+url[9433]+url[9434]+url[9435]+url[9436]+url[9437]+url[9438]+url[9439]+url[9440]+url[9441]+url[9442]+url[9443]+url[9444]+url[9445]+url[9446]+url[9447]+url[9448]+url[9449]+url[9450]+url[9451]+url[9452]+url[9453]+url[9454]+url[9455]+url[9456]+url[9457]+url[9458]+url[9459]+url[9460]+url[9461]+url[9462]+url[9463]+url[9464]+url[9465]+url[9466]+url[9467]+url[9468]+url[9469]+url[9470]+url[9471]+url[9472]+url[9473]+url[9474]+url[9475]+url[9476]+url[9477]+url[9478]+url[9479]+url[9480]+url[9481]+url[9482]+url[9483]+url[9484]+url[9485]+url[9486]+url[9487]+url[9488]+url[9489]+url[9490]+url[9491]+url[9492]+url[9493]+url[9494]+url[9495]+url[9496]+url[9497]+url[9498]+url[9499]+url[9500]+url[9501]+url[9502]+url[9503]+url[9504]+url[9505]+url[9506]+url[9507]+url[9508]+url[9509]+url[9510]+url[9511]+\
    url[9512]+url[9513]+url[9514]+url[9515]+url[9516]+url[9517]+url[9518]+url[9519]+url[9520]+url[9521]+url[9522]+url[9523]+url[9524]+url[9525]+url[9526]+url[9527]+url[9528]+url[9529]+url[9530]+url[9531]+url[9532]+url[9533]+url[9534]+url[9535]+url[9536]+url[9537]+url[9538]+url[9539]+url[9540]+url[9541]+url[9542]+url[9543]+url[9544]+url[9545]+url[9546]+url[9547]+url[9548]+url[9549]+url[9550]+url[9551]+url[9552]+url[9553]+url[9554]+url[9555]+url[9556]+url[9557]+url[9558]+url[9559]+url[9560]+url[9561]+url[9562]+url[9563]+url[9564]+url[9565]+url[9566]+url[9567]+url[9568]+url[9569]+url[9570]+url[9571]+url[9572]+url[9573]+url[9574]+url[9575]+url[9576]+url[9577]+url[9578]+url[9579]+url[9580]+url[9581]+url[9582]+url[9583]+url[9584]+url[9585]+url[9586]+url[9587]+url[9588]+url[9589]+url[9590]+url[9591]+url[9592]+url[9593]+url[9594]+url[9595]+url[9596]+url[9597]+url[9598]+url[9599]+url[9600]+url[9601]+url[9602]+url[9603]+url[9604]+url[9605]+url[9606]+url[9607]+url[9608]+url[9609]+url[9610]+url[9611]+url[9612]+\
    url[9613]+url[9614]+url[9615]+url[9616]+url[9617]+url[9618]+url[9619]+url[9620]+url[9621]+url[9622]+url[9623]+url[9624]+url[9625]+url[9626]+url[9627]+url[9628]+url[9629]+url[9630]+url[9631]+url[9632]+url[9633]+url[9634]+url[9635]+url[9636]+url[9637]+url[9638]+url[9639]+url[9640]+url[9641]+url[9642]+url[9643]+url[9644]+url[9645]+url[9646]+url[9647]+url[9648]+url[9649]+url[9650]+url[9651]+url[9652]+url[9653]+url[9654]+url[9655]+url[9656]+url[9657]+url[9658]+url[9659]+url[9660]+url[9661]+url[9662]+url[9663]+url[9664]+url[9665]+url[9666]+url[9667]+url[9668]+url[9669]+url[9670]+url[9671]+url[9672]+url[9673]+url[9674]+url[9675]+url[9676]+url[9677]+url[9678]+url[9679]+url[9680]+url[9681]+url[9682]+url[9683]+url[9684]+url[9685]+url[9686]+url[9687]+url[9688]+url[9689]+url[9690]+url[9691]+url[9692]+url[9693]+url[9694]+url[9695]+url[9696]+url[9697]+url[9698]+url[9699]+url[9700]+url[9701]+url[9702]+url[9703]+url[9704]+url[9705]+url[9706]+url[9707]+url[9708]+url[9709]+url[9710]+url[9711]+url[9712]+url[9713]+\
    url[9714]+url[9715]+url[9716]+url[9717]+url[9718]+url[9719]+url[9720]+url[9721]+url[9722]+url[9723]+url[9724]+url[9725]+url[9726]+url[9727]+url[9728]+url[9729]+url[9730]+url[9731]+url[9732]+url[9733]+url[9734]+url[9735]+url[9736]+url[9737]+url[9738]+url[9739]+url[9740]+url[9741]+url[9742]+url[9743]+url[9744]+url[9745]+url[9746]+url[9747]+url[9748]+url[9749]+url[9750]+url[9751]+url[9752]+url[9753]+url[9754]+url[9755]+url[9756]+url[9757]+url[9758]+url[9759]+url[9760]+url[9761]+url[9762]+url[9763]+url[9764]+url[9765]+url[9766]+url[9767]+url[9768]+url[9769]+url[9770]+url[9771]+url[9772]+url[9773]+url[9774]+url[9775]+url[9776]+url[9777]+url[9778]+url[9779]+url[9780]+url[9781]+url[9782]+url[9783]+url[9784]+url[9785]+url[9786]+url[9787]+url[9788]+url[9789]+url[9790]+url[9791]+url[9792]+url[9793]+url[9794]+url[9795]+url[9796]+url[9797]+url[9798]+url[9799]+url[9800]+url[9801]+url[9802]+url[9803]+url[9804]+url[9805]+url[9806]+url[9807]+url[9808]+url[9809]+url[9810]+url[9811]+url[9812]+url[9813]+url[9814]+\
    url[9815]+url[9816]+url[9817]+url[9818]+url[9819]+url[9820]+url[9821]+url[9822]+url[9823]+url[9824]+url[9825]+url[9826]+url[9827]+url[9828]+url[9829]+url[9830]+url[9831]+url[9832]+url[9833]+url[9834]+url[9835]+url[9836]+url[9837]+url[9838]+url[9839]+url[9840]+url[9841]+url[9842]+url[9843]+url[9844]+url[9845]+url[9846]+url[9847]+url[9848]+url[9849]+url[9850]+url[9851]+url[9852]+url[9853]+url[9854]+url[9855]+url[9856]+url[9857]+url[9858]+url[9859]+url[9860]+url[9861]+url[9862]+url[9863]+url[9864]+url[9865]+url[9866]+url[9867]+url[9868]+url[9869]+url[9870]+url[9871]+url[9872]+url[9873]+url[9874]+url[9875]+url[9876]+url[9877]+url[9878]+url[9879]+url[9880]+url[9881]+url[9882]+url[9883]+url[9884]+url[9885]+url[9886]+url[9887]+url[9888]+url[9889]+url[9890]+url[9891]+url[9892]+url[9893]+url[9894]+url[9895]+url[9896]+url[9897]+url[9898]+url[9899]+url[9900]+url[9901]+url[9902]+url[9903]+url[9904]+url[9905]+url[9906]+url[9907]+url[9908]+url[9909]+url[9910]+url[9911]+url[9912]+url[9913]+url[9914]+url[9915],
    return Url

    
  
   



def OTVdecode(text, k=16):
    nl = len(text)
    val = int(binascii.hexlify(text[-1]), 16)
    if val > k:
        raise ValueError('Input is not padded or padding is corrupt')

    l = nl - val
    return text[:l]


def OTVencode(text, k=16):
    l = len(text)
    output = StringIO.StringIO()
    val = k - (l % k)
    for _ in xrange(val):
        output.write('%02x' % val)
    return text + binascii.unhexlify(output.getvalue())  
class OTVPLAYER:    

    def playLink(self,name,url,iconimage):
        
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        xbmcPlayer = xbmc.Player()
        while True:
          if self.onPlayBackEnded or time.time() - self._start_time > 300:
                if self.totalTime == 999999:
                    raise PlaybackFailed(
                        'XBMC silently failed to start playback')
                break

          xbmc.sleep(500)
        
    def totalTime(self):
        self.totalTime = self.getTotalTime()

    def __getPlayList(self):
        return xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

    def addItemToPlaylist(self, oGuiElement):
        oGui = cGui()
        oListItem =  oGui.createListItem(oGuiElement)
        self.__addItemToPlaylist(oGuiElement, oListItem)
	
    def __addItemToPlaylist(self, oGuiElement, oListItem):    
        oPlaylist = self.__getPlayList()	
        oPlaylist.add(oGuiElement.getMediaUrl(), oListItem )
    
    
    def addToPlaylist(self):
        oGui = cGui()

        oInputParameterHandler = cInputParameterHandler()

        sHosterIdentifier = oInputParameterHandler.getValue('sHosterIdentifier')
        sMediaUrl = oInputParameterHandler.getValue('sMediaUrl')
        bGetRedirectUrl = oInputParameterHandler.getValue('bGetRedirectUrl')
        sFileName = oInputParameterHandler.getValue('sFileName')

        if (bGetRedirectUrl == 'True'):
            sMediaUrl = self.__getRedirectUrl(sMediaUrl)

        VSlog("Hoster - playlist " + sMediaUrl)
        oHoster = self.getHoster(sHosterIdentifier)
        oHoster.setFileName(sFileName)

        oHoster.setUrl(sMediaUrl)
        aLink = oHoster.getMediaLink()

        if (aLink[0] == True):
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(self.SITE_NAME)
            oGuiElement.setMediaUrl(aLink[1])
            oGuiElement.setTitle(oHoster.getFileName())

            oPlayer = cPlayer()
            oPlayer.addItemToPlaylist(oGuiElement)
            self.DIALOG.VSinfo(str(oHoster.getFileName()), 'Playlist')
            return

        oGui.setEndOfDirectory()

    def __getRedirectUrl(self, sUrl):
        oRequest = cRequestHandler(sUrl)
        oRequest.request()
        return oRequest.getRealUrl()
    def libForPlayback(self):
        try:
            if self.DBID == None: raise Exception()

            if self.content == 'movie':
                rpc = '{"jsonrpc": "2.0", "method": "VideoLibrary.SetMovieDetails", "params": {"movieid" : %s, "playcount" : 1 }, "id": 1 }' % str(self.DBID)
            elif self.content == 'episode':
                rpc = '{"jsonrpc": "2.0", "method": "VideoLibrary.SetEpisodeDetails", "params": {"episodeid" : %s, "playcount" : 1 }, "id": 1 }' % str(self.DBID)

            control.jsonrpc(rpc) ; control.refresh()
        except:
            pass


    def idleForPlayback(self):
        for i in range(0, 200):
            if control.condVisibility('Window.IsActive(busydialog)') == 1: control.idle()
            else: break
            control.sleep(100)

    # Kodi 17 relevant, broken in Kodi 18
    # TODO: Remove when Kodi 18 is in stable
    def onPlayBackStarted(self):
        control.execute('Dialog.Close(all,true)')
        if not self.offset == '0': self.seekTime(float(self.offset))
        subtitles().get(self.name, self.imdb, self.season, self.episode)
        self.idleForPlayback()

    # Exposed by kodi core in v18 when a video starts playing 
    # https://forum.kodi.tv/showthread.php?tid=334929
    def onAVStarted(self):
        xbmc.sleep(1000)
        control.execute('Dialog.Close(all,true)')
        if not self.offset == '0': self.seekTime(float(self.offset))
        subtitles().get(self.name, self.imdb, self.season, self.episode)
        self.idleForPlayback()

    def onPlayBackStopped(self):
        bookmarks().reset(self.currentTime, self.totalTime, self.name, self.year)
        if control.setting('crefresh') == 'true':
            xbmc.executebuiltin('Container.Refresh')

        try:
            if (self.currentTime / self.totalTime) >= .90:
                self.libForPlayback()
        except: pass

    def onPlayBackEnded(self):
        self.libForPlayback()
        self.onPlayBackStopped()
        if control.setting('crefresh') == 'true':
            xbmc.executebuiltin('Container.Refresh')

       
   
                