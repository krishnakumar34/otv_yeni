#-*- coding: utf-8 -*-

from resources.sites.LIVETV2 import *  
#from hashlib import md5
AddonID = 'plugin.video.OTV_MEDIA'
#from sqlite3 import dbapi2 as sqlite
import re
import io
s = requests.Session()
import base64 

#from resources.lib.backtothefuture import PY2


import urllib as urllib2
import requests
def fix_auth_date(auth):
    now = datetime.datetime.utcnow()
    _in = list(auth)
    _in.pop(len(_in) + 2 - 3 - int(str(now.year)[:2]))
    _in.pop(len(_in) + 3 - 4 - int(str(now.year)[2:]))
    # java January = 0
    _in.pop(len(_in) + 4 - 5 - (now.month - 1 + 1 + 10))
    _in.pop(len(_in) + 5 - 6 - now.day)
    return "".join(_in)

ddatam_url='http://app.liveplanettv.com/beta/api.php?device_id=354630080742220'   
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('profile'))
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
data_file = os.path.join(RESOURCES_DIR, 'data.txt')
AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
icon = Addon.getAddonInfo('icon')
AddonName = Addon.getAddonInfo("name")
addonDir = Addon.getAddonInfo('path')

SITE_IDENTIFIER = 'adult_eu'
from resources.lib.config import cConfig


import sys


TIK='|User-Agent=Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G950U1 Build/NRD90M)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()

da_url= 'http://glazandroid.com/andr/chas-online-json-1.5.php'
#http://139.59.68.238/stm-v3/api/def2.php?id=723&quality=0&type=0
Host = 'https://raw.githubusercontent.com/PrivateTr/Zone_enigma/master/userbouquet.Remy_IPTV2.tv'
Hostbir = 'https://raw.githubusercontent.com/PrivateTr/Zone_enigma/master/userbouquet.Remy_IPTV1.tv'
              

useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
      



selfAddon = xbmcaddon.Addon()
ulkeLists = 'http://85.132.71.12/channels'
ulkeListem ='http://hyfystreamz.com/dfytv/list.json'



def sEcho(s):
    s=s
    if '/page/1/' in s:
       s=s.replace('/page/1/','/page/2/')
       return s 
    if '/page/2/' in s:
       s=s.replace('/page/2/','/page/3/')
       return s 
    if '/page/3/' in s:	
       s=s.replace('/page/3/','/page/4/')
       return s 


def getyoutubepage( url):
    headers = {'Host': 'www.youtube.com',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
               'Accept': '*/*',
               'DNT': '1',
               'Referer': 'https://www.youtube.com',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.8,de;q=0.6'}

    result = requests.get(url,  headers=headers, allow_redirects=True)
    return result.text

class urlKap(object):
    """
        urlKap(url).result
        urlKap(url, output = 'geturl').result
        urlKap(url, output = 'cookie').result
        urlKap(url, timeout='30').result
        post = {'hash':media_id}
        urlKap(url, post = post).result
        url = 'http://www.diziizleyin.net/index.php?x=isyan'
        postfields = {'pid' : 'p2x29464a434'}
        txheaders = {'X-Requested-With':'XMLHttpRequest'}
        urlKap(url, postfields, headers, loc)
    """

    def __init__(self, url, close = True, proxy = None, post = None, mobile = False, referer = None, cookie = None, output = '', timeout = '10'):
        if not proxy == None:
            proxy_handler = urllib2.ProxyHandler({'http': '%s' % proxy})
            opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or output == 'kukili' or not close == True:
            import cookielib
            cookie_handler = urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar())
            opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
            opener = urllib2.install_opener(opener)
        if not post == None:
            import urllib
            post = urllib.urlencode(post)
            request = urllib2.Request(url, post)
        else:
            request = urllib2.Request(url, None)
        if mobile == True:
            request.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7')
        else:
            request.add_header('User-Agent', UA)
        if not referer == None:
            request.add_header('Referer', referer)
        if not cookie == None:
            request.add_header('cookie', cookie)
        response = urllib2.urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = str(response.headers.get('Set-Cookie'))
        elif output == 'kukili':
            result = response.read() + 'kuki :' + str(response.headers.get('Set-Cookie'))
        elif output == 'geturl':
            result = response.geturl()
        elif output == 'lenght':
            result = str(response.headers.get('Content-Length'))
        else:
            result = response.read()
        if close == True:
            response.close()
        self.result = result

def orhantvalman():
    oGui = cGui()
   

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'AlmanKINO', 'KINO FILME', 'filmkino.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '23')
    oGui.addDir('livenettv', 'list_channels', 'IPTV TV ', 'worldiptv.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '28')
    oGui.addDir(SITE_IDENTIFIER, 'livestreamtv', 'TV SENDER', 'worldiptv.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')

    oGui.addDir('radio_de', 'radiode', 'RADIO', 'bradio.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('adult_eu', 'pincode', 'ADULT', 'sexyfrau.jpg', oOutputParameterHandler)

   
    oGui.setEndOfDirectory()
#<span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.dorftv.at/livestream" rel="noreferrer noopener">https://www.dorftv.at/livestream</a>" <span class="html-attribute-name">target</span>="<span class="html-attribute-value">_blank</span>"&gt;</span>
#<tr><td class="line-number" value="328"></td><td class="line-content"><span class="html-tag">&lt;br /&gt;</span>(.*?)</td></tr>
#<tr><td class="line-number" value="329"></td><td class="line-content"><span class="html-tag">&lt;br /&gt;</span>Channel name: <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://fs1.tv/" rel="noreferrer noopener">https://fs1.tv/</a>" <span class="html-attribute-name">target</span>="<span class="html-attribute-value">_blank</span>"&gt;</span>(.*?)<span class="html-tag">&lt;/a&gt;</span></td></tr>
def livestreamtv():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'https://www.harryshomepage.de/webtv.html'
  
    data=  getHtml(sUrl)
      
     

       
    tarzlistesi = re.findall('Channel name: (.*?)\n<br />URL: (.*?)\n', data , re.S)
    for sTitle,sUrl in tarzlistesi:

            
                                               
            sPicture = 'https://www.harryshomepage.de/hahop_banner2.jpg'
            
            sUrl=sUrl.replace('index_1_av-p.m3u8','master.m3u8')                        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'otvplay__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        
        
         
    oGui.setEndOfDirectory()
   
def AlmanKINO():
    oGui = cGui()
   
    ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
    SITES_DIR = os.path.join(ADDON_DATA_DIR, 'resources','sites')
                         
    oInputParameterHandler = cInputParameterHandler()
    Urrl = 'https://github.com/streamxstream/plugin.video.xstream/tree/nightly/sites'
    sHtmlContent = getHtml(Urrl)       
    
    sPattern = '<a class="js-navigation-open Link--primary" title="(.*?).py" data-pjax="#repo-content-pjax-container" href="/streamxstream/plugin.video.xstream/blob/nightly/sites/(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
      total = len(aResult[1])
      for aEntry in aResult[1]:                               
        sourcestr = ''
        url = 'https://raw.githubusercontent.com/streamxstream/plugin.video.xstream/nightly/sites/' +  aEntry[1]
        modsource = getHtml(url) 
        obj = compile(modsource, sourcestr, 'exec')
        from resources.lib import comon
        import imp
        module = imp.new_module(aEntry[0])
        exec(obj, module.__dict__)
        data = os.path.join(SITES_DIR,aEntry[1].replace('-','')) 
        list = modsource
        comon.SaveList2(data,list)
        
        sTitle =module.SITE_NAME
        png = module.SITE_ICON
        module=module.SITE_IDENTIFIER
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(module, 'load', sTitle, png, oOutputParameterHandler)
    oGui.setEndOfDirectory()  


def SearchAra():
        params = ParameterHandler()
        searchterm = False
        if params.exist('searchterm'):
            searchterm = params.getValue('searchterm')
        searchGlobal(searchterm)
      
def msearchGlobal(sSearchText=False):
    import threading
    oGui = cGui()
    oGui.globalSearch = True
    oGui._collectMode = True
    if not sSearchText:
        sSearchText = oGui.showKeyBoard()
    if not sSearchText: return True
    aPlugins = []
    aPlugins = cPluginHandler().getAvailablePlugins()
    dialog = xbmcgui.DialogProgress()
    dialog.create('xStream', 'Searching...')
    numPlugins = len(aPlugins)
    threads = []
    for count, pluginEntry in enumerate(aPlugins):
        dialog.update((count + 1) * 50 // numPlugins, 'Searching: ' + str(pluginEntry['name']) + '...')
        if dialog.iscanceled(): return
        if sys.version_info[0] == 2:
            logger.info('Searching for %s at %s' % (sSearchText, pluginEntry['id']))
        else:
            logger.info('Searching for %s at %s' % (sSearchText, pluginEntry['id']))

        t = threading.Thread(target=_pluginSearch, args=(pluginEntry, sSearchText, oGui), name=name)
        threads += [t]
        t.start()
    for count, t in enumerate(threads):
        if dialog.iscanceled(): return
        t.join()
        dialog.update((count + 1) * 50 // numPlugins + 50, t.getName() + ' returned')
    dialog.close()
    # deactivate collectMode attribute because now we want the elements really added
    oGui._collectMode = False
    total = len(oGui.searchResults)
    dialog = xbmcgui.DialogProgress()
    dialog.create('xStream', 'Gathering info...')
    for count, result in enumerate(sorted(oGui.searchResults, key=lambda k: k['guiElement'].getSiteName()), 1):
        if dialog.iscanceled(): return
        oGui.addFolder(result['guiElement'], result['params'], bIsFolder=result['isFolder'], iTotal=total)
        dialog.update(count * 100 // total, str(count) + ' of ' + str(total) + ': ' + result['guiElement'].getTitle())
    dialog.close()
    oGui.setView()
    oGui.setEndOfDirectory()
    return True

      
def searchGlobal(sSearchText=False):
      import threading
      oGui = cGui()
      oGui.globalSearch = True
      oGui._collectMode = True
      if not sSearchText:
        sSearchText = oGui.showKeyBoard()
      if not sSearchText: return True
      aPlugins = []
     
      dialog = xbmcgui.DialogProgress()
      dialog.create('OTV_MEDIA', 'Searching...')
      count= 0
      threads = []
      url = 'https://dl.dropboxusercontent.com/s/kiqm16dtd6tsfcm/almanfilms.txt'
      content = getHtml(url)
      aPlugins=re.findall("ASITE_IDENTIFIER = '(.*?)'SITE_NAME = '(.*?)'",content, re.S)      
      for  pluginEntry,name in aPlugins:
        name = (str(name)).replace('.py','')
        numPlugins = len(pluginEntry)
        VSlog('globalsearch-'+pluginEntry)
        dialog.update((count + 1) * 50 // numPlugins, 'Searching: ' + str(name) + '...')
        VSlog('Searching for %s at %s' % (sSearchText, pluginEntry))
        t = threading.Thread(target=_pluginSearch, args=(pluginEntry, sSearchText, oGui), name=name)
        threads += [t]
        t.start()
      for count, t in enumerate(threads):
        t.join()
        dialog.update((count + 1) * 50 / numPlugins + 50, t.getName() + ' returned')
      dialog.close()
    # deactivate collectMode attribute because now we want the elements really added
      oGui._collectMode = False
      total = len(oGui.searchResults)
      
      dialog = xbmcgui.DialogProgress()
      dialog.create('OTV_MEDIA', 'Gathering info...')
      for count, result in enumerate(sorted(oGui.searchResults, key=lambda k: k['guiElement'].getSiteName()), 1):
        oGui.addFolder(result['guiElement'], result['params'], bIsFolder=result['isFolder'], iTotal=total)
        dialog.update(count * 200 // total, str(count) + ' of ' + str(total) + ': ' + result['guiElement'].getTitle())
      dialog.close()
       
      oGui.setView()
      oGui.setEndOfDirectory()
      return True


def _pluginSearch(pluginEntry, sSearchText, oGui):
      try:
        plugin = __import__(pluginEntry, globals(), locals())
        function = getattr(plugin, '_search')
        function(oGui, sSearchText)
      except:
        #VSlog(pluginEntry+['name'] + ': search failed')
        import traceback
        VSlog('_search'+traceback.format_exc())
      


      



class getUrl(object):
    def __init__(self, url,output, close=True, proxy=None, post=None, headers=None, mobile=False, referer=None, cookie=None,  timeout='10'):
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
 

class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data

 


def get_media_url(url, result_blacklist=None, patterns=None, generic_patterns=True):
    if patterns is None: patterns = []
    scheme = urlparse(url).scheme
    if result_blacklist is None:
        result_blacklist = []
    elif isinstance(result_blacklist, str):
        result_blacklist = [result_blacklist]

    result_blacklist = list(set(result_blacklist + ['.smil']))  # smil(not playable) contains potential sources, only blacklist when called from here
    net = common.Net()
    headers = {'User-Agent': common.RAND_UA}

    response = getHtml(url, headers=headers)
    response_headers = response.get_headers(as_dict=True)
    headers.update({'Referer': url})
    cookie = response_headers.get('Set-Cookie', None)
    if cookie:
        headers.update({'Cookie': cookie})
    html = response.content

    source_list = scrape_sources(html, result_blacklist, scheme, patterns, generic_patterns)
    source = pick_source(source_list)
    return source + append_headers(headers)




def load():
    linktv = cConfig().getSetting('pvr-view')
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Pour Modifier ou  Ajouter des chaînes à FramaPad https://annuel.framapad.org/p/vstream [/COLOR]', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_FREE)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'FramaPad (Bêta)', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_SFR)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Sfr TV', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_ORANGE)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Orange TV', 'tv.png', oOutputParameterHandler)
    
    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_BG)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Bouygues TV', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_WEB)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Tv du web', 'tv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Tu veux voir ta chaîne sur Libretv.me alors partage ta chaîne![/COLOR]', 'libretv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_LIBRETV)
    oGui.addDir(SITE_IDENTIFIER, 'showLibreMenu', 'Libretv.me', 'libretv.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()
settingpin =addon.getSetting( "adultPIN" )

def pincode():
    oGui = cGui()
    pincode = oGui.pinKeyBoard()
    if settingpin in pincode:  
            showGenre()


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  

def showGenre():
    oGui = cGui()         
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://live.redtraffic.xyz/all.m3u')
    oGui.addDir('adult', 'main','PORN SITES', 'genres.png', oOutputParameterHandler)
    

     
    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', "http://oklivetv.com/genre/adult-18/page/1/")
    oGui.addDir(SITE_IDENTIFIER, 'OKliveTV2', 'OKliveTV.com adult tv channels. Watch online free live Internet TV', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', "https://www.oklivecams.com/tag/mistress/f/")
    oGui.addDir(SITE_IDENTIFIER, 'oklivecams','OK Live Cams', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl','http://topplay.do.am/AdultsTopPlay.m3u')
    oGui.addDir(SITE_IDENTIFIER, 'liveGenre', 'VIDEOS', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', "http://hdporn.net/channels/")
    oGui.addDir(SITE_IDENTIFIER, 'hdpornGenre', 'HDPorn', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl',"http://ero-tv.org/uppod/pl/playlist_video69-897.txt")
    oGui.addDir(SITE_IDENTIFIER, 'GetPlayList', 'VIDEO PLAYLIST', 'genres.png', oOutputParameterHandler)

#    oOutputParameterHandler = cOutputParameterHandler()
#    oOutputParameterHandler.addParameter('siteUrl',"http://www.pornhd.com/category")
#    oGui.addDir(SITE_IDENTIFIER, 'pornhdGenre','PornHD', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', "https://www.pornhub.com/categories")
    oGui.addDir(SITE_IDENTIFIER, 'pornhubGenre','PornHub', 'genres.png', oOutputParameterHandler)
           
                    
    oGui.setEndOfDirectory()
def oklivecams(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
   
      
    sHtmlContent= getHtml(Url)
    sPattern = '<div id="hashtag_ticker">(.+?)<div id="hashtag_ticker">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)" data-floatingnav>#(.*?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        
        for aEntry in aResult[1]:
            sPicture = 'https://ssl-ccstatic.highwebmedia.com/favicons/favicon-96x96.png'
            sTitle = aEntry[1]
            Link = 'https://www.oklivecams.com'+ aEntry[0]
            
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'oklivecams2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory() 

def oklivecams2(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    oRequest = cRequestHandler(Url)
      
    sHtmlContent= oRequest.request()
    

    sPattern = '<img src="(.*?)" width="180" height=".*?" alt="(.*?)" class=".*?<a href="/.*?/" data-room="(.*?)"> '
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        
        for aEntry in aResult[1]:
            sPicture = aEntry[0]
            sTitle = aEntry[1]
            Link = aEntry[2]
           
            URL ='https://www.oklivecams.com/embed/'+Link+'/?join_overlay=1&campaign=W52kq&embed_video_only=1&disable_sound=0&tour=sEAI&mobileRedirect=never'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', URL)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'oklivecamplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory() 

def oklivecamplayer():
          oGui = cGui()
          oInputParameterHandler = cInputParameterHandler()
          liste = oInputParameterHandler.getValue('siteUrl')
          name = oInputParameterHandler.getValue('sMovieTitle')
          auth =getHtml(liste)    
          auth =malfabekodla(auth)                              
          logger.info('oklive>%s' % auth)                
          url =re.search('"hls_source": "(.*?)"', auth).group(1)
         
                                    
         
           
          addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')



               
def OKliveTV2(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urll = "http://oklivetv.com/" 
#    cookie = urlKap(Urll , output='cookie').result 
    sHtmlContent = getHtml(Url)
    sPattern = '<div class="nag cf">(.+?)<script'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a class="clip-link" data-id=".*?" title="(.*?)" href="(.*?)">.*?<img src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        
        for aEntry in aResult[1]:
            sPicture = str(aEntry[2])
            sTitle = aEntry[0]
            Link = aEntry[1]
           
            sTitle =malfabekodla(sTitle) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('refsiteUrl', Link)
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'madulto', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        sNextPage =sEcho(str(Url))
        if (sNextPage != False):
             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteUrl', sNextPage)
             oGui.addDir(SITE_IDENTIFIER, 'OKliveTV2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory() 

try:
    from urllib.parse import quote as orig_quote
except ImportError:
    from urllib import quote as orig_quote

def quote(s, safe = ''):
    return orig_quote(s.encode('utf-8'), safe.encode('utf-8'))
def oklidecode2( data):   
     for m in data:	                
       return(m)[1:]
def oklidecode( data):   
	                
     data = (str(data)).replace('0a','a')
     data = (str(data)).replace('0b','b')
     data = (str(data)).replace('0c',"c")
     data = (str(data)).replace('0d',"d")
     data = (str(data)).replace('0e',"e")
     data = (str(data)).replace('0f',"f")
     data = (str(data)).replace('01','1')
     data = (str(data)).replace('02','2')
     data = (str(data)).replace('03','3')
     data = (str(data)).replace('04','4')
     data = (str(data)).replace('05','5')
     data = (str(data)).replace('06','6')
     data = (str(data)).replace('07','7')
     data = (str(data)).replace('08','8')
     data = (str(data)).replace('09','9')
     
     return  data
from resources.lib.comaddon import VSlog#, dialog
import binascii
   


def okliDecode(txt):
    import codecs
    txt =codecs.decode(txt, 'hex').decode('ascii')
    return txt

def mmadulto():

      
       oInputParameterHandler = cInputParameterHandler()
       Url = oInputParameterHandler.getValue('siteUrl')
       refUrl = oInputParameterHandler.getValue('refsiteUrl')
       name = oInputParameterHandler.getValue('sMovieTitle')
       hosters = []
       Urll = "http://oklivetv.com/" 
#       cookie = getUrl(Url, output='cookie').result 
#       headers = 'User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
       data3 = requests.session().get(Url,headers={"Cookie": "","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","Host": "oklivetv.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text

       Url2 ='http:'+re.search("""<iframe.+?src=["'](.+?)["']""",  data3).group(1)
                    
       
       oRequest = cRequestHandler(Url2)

                        
       oRequest.addHeaderEntry('Host', 'oklivetv.com')
       oRequest.addHeaderEntry('Connection', 'keep-alive')
       oRequest.addHeaderEntry('Upgrade-Insecure-Requests', '1')
       oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')
       oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
#       oRequest.addHeaderEntry('Sec-Fetch-Site', 'cross-site')
#       oRequest.addHeaderEntry('Sec-Fetch-Mode', 'navigate')
#       oRequest.addHeaderEntry('Sec-Fetch-Dest', 'iframe')
       oRequest.addHeaderEntry('Referer', Url )
       oRequest.addHeaderEntry('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7')
#       oRequest.addHeaderEntry('Cookie', cookie)
       oRequest.addHeaderEntry('Accept-Encoding', 'gzip, deflate')
      
       
       
       data1= oRequest.request()
          
     
       #aut = re.compile('(custom.function.+?)</script>').findall(data1)
       logger.info("player_auth: %s" % data1 ) 
       #auth =unpack(aut)
       #data1 =data1.replace('|',"Host")
#       autti =re.search("p2pchannelid='(.+?)'", auth).group(1)
       auti =re.findall('0680740740(.+?)33075038', data1)
       auti =re.search("0680740740(.+?)33075038", data1).group(1)
       auti = '0680740740'+auti+'33075038 ' 
       url =oklidecode(auti).decode('hex')
       info('Good cookie :' + url)
       TIK='|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36&Referer='+Url
          
       addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url+TIK , '')
def potwmplay():
    oInputParameterHandler = cInputParameterHandler()
    name = oInputParameterHandler.getValue('sMovieTitle')[2:]                            
    Url = oInputParameterHandler.getValue('siteUrl')                                     
    TIK='|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

    url=  potwm()
    logger.info("player_auth: %s" %url ) 

qualitylist = []
videolist = []
def potwm():
    urla= 'http://pt.potwm.com/'
    
    url= "http://pt.potwm.com/live-feed/fk/?c=object_container&site=wl3&cobrandId=241040&psid=oklivetv&pstool=319_1&psprogram=cbrnd&campaign_id=94891&vp%5BshowChat%5D=false&vp%5BchatAutoHide%5D=false&vp%5BshowCallToAction%5D=false&vp%5BshowPerformerName%5D=false&vp%5BshowPerformerStatus%5D=false&subAffId=%7BSUBAFFID%7D&categoryName=girl&embedTool=1&origin="
    referer=[('Referer',urla)]                
    page=gegetUrl(url,headers=referer).replace("\t",'').replace("\n",'')
    logger.info('oklive>%s' % page)
    values = re.findall('gaLabel: "(.*?)".*?url: "(.*?)"', page)
    for name,urll in values:
        urll= 'http:'+ urll
        import streamer
        streamer.sstreamer(name,urll)
  
        return  
       
  
                      



def madulto():
       oInputParameterHandler = cInputParameterHandler()
       Url = oInputParameterHandler.getValue('siteUrl')
       refUrl = oInputParameterHandler.getValue('refsiteUrl')
       name = oInputParameterHandler.getValue('sMovieTitle')
       data3= getHtml(Url)
       Url2 ='http:'+re.search("""<iframe.+?src=["'](.+?)["']""",  data3).group(1)
       cookie =SetCookie(Url2 )
       data1 = requests.session().get(Url2, headers={"Cookie": cookie,"Referer": Url ,"Content-Type": "application/x-www-form-urlencoded","User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',"sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',"x-requested-with": "XMLHttpRequest"}).text        
       data1=to_utf8( data1)
       data=oklidecode(data1)
       auti =re.search('(687474703a.+?6d337538)', data).group(1)
       logger.info('oklive>%s' % auti) 
       auti =okliDecode(auti)
       logger.info('oklive>%s' % auti)
       TIK='|Referer='+Url2 +'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' 
       baddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, auti+TIK, '')
        
     
def baddLink(name, url, iconimage):
    ok = True                                  
                                          
   # url = str(url).replace('.m3u8','.m3u8|Cookie=__cfduid=daf238e349b76e7174a4eeb73854a7b651617059685; _ga=GA1.2.19173863.1617059687; _gid=GA1.2.1342217077.1617059687; _awl=2.1617063081.0.4-d202cd53-f5a07719162167cc6c34809c7770960b-6763652d6575726f70652d7765737431-60626ca9-0; euconsent-v2=CPD17oIPD17oIAKAXAENBTCsAP_AAH_AAAwIHqtf_X__b39j-_59__t0eY1f9_7_v-0zjhfdt-8N2f_X_L8X42M7vF36pq4KuR4Eu3LBIQFlHOHUTUmw6okVrTPsak2Mr7NKJ7LEinMbe2dYGHtfn91TuZKYr_78_9fz__-__v__79f_r-3_3_vp9X---_e_V399xLv9f-B6oBJhqXwAWYljgyTRpVCiBCFcSHQCgAooRhaJrCBlcFOyuAj1BAwAQGoCMCIEGIKMWAQAAAQBIREBIAeCARAEQCAAEAKkBCAAiYBBYAWBgEAAoBoWIEUAQgSEGRwVHKYEBEi0UE8lYAlF3saYQhlFgBQKP6KjARKkECwMgAAA.YAAAAAAAAAAA; cwv3_cookie__cat_268=true; JuicyPop0=1; __viCookieActive=true; _gat_gtag_UA_57647313_3=1; _gat=1Accept-Encoding: gzip, deflate Content-Length: 51').replace("b'",'')
 
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 



def liveGenre():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    url= requests.get(sUrl, headers = headers).text
    url=url.replace('#extinf',"#EXTINF")
#    name = 'flashx.tv'
#    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
#def lsmhowWeb():
#    oGui = cGui()
#    if data:
#        channels = re.findall('#EXTINF:-1 tvg-id="" tvg-name="(.*?)" tvg-logo="" group-title=".*?\n(.*?)\n', data, re.S)           
#    else:
    channels = re.findall('#EXTINF:(.*?)\n(.*?)\n', url, re.S)          
    for title, path in channels:                            
                                  
              sTitle =malfabekodla(title)[2:] 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', path)
              oOutputParameterHandler.addParameter('sMovieTitle',title)
              oGui.addDir(SITE_IDENTIFIER, 'liveplaylive', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()

   
                                                                                                         	
                       
						
							              
  
def liveplaylive():
    oInputParameterHandler = cInputParameterHandler()
    name = oInputParameterHandler.getValue('sMovieTitle')[2:]                            
    Url = oInputParameterHandler.getValue('siteUrl')                                     
    TIK='|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

    url=  Url+TIK 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')
                                                                                        
	
def ultHosters():
        names = []
        urls = []
        names.append("Tivu Stream XXX")
        urls.append("https://patbuweb.com/iptv/e2liste/userbouquet.tivustream_adultxxx.tv") 
        i = 0
        for name in names:
                url = urls[i]
                pic = " "
                i = i+1
                addDirectoryItem(name, {"name":name, "url":url, "mode":"1"}, pic)
        xbmcplugin.endOfDirectory(hos)


def showContentB1(): 
                oGui = cGui()  
                Host="https://patbuweb.com/iptv/e2liste/userbouquet.tivustream_adultxxx.tv"
                content =cRequestHandler(Host).request() 
                        
                pass#print "content A =", content
                regexcat = '#DESCRIPTION ---(.*?)---'
                match = re.compile(regexcat,re.DOTALL).findall(content)
                pass#print "match A=", match
                i = 0
                for sTitle in match:
                        
                        if i < 3:
                              i = i+1
                              continue
                        i = i+1 
                        # if (not "ADULTI" in name) and (not "VINTAGE ITALIANO Film Completi" in name):
                              # continue     
                        url1 = Host
                        sPicture= " "
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl',  url1)
                        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
                        oGui.addMovie(SITE_IDENTIFIER, 'showContentB2',sTitle, sPicture, sPicture, '', oOutputParameterHandler)

                oGui.setEndOfDirectory()



                
def playVideo(name, url):
                 
                 pass#print "In playVideo url =", url
                 player = xbmc.Player()
                 player.play(url)
                 

std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}  

def addDirectoryItem(name, parameters={},pic=""):
    li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)





def adulttvlive():
    oGui = cGui()
   
  
        #oInputParameterHandler = cInputParameterHandler()
        #sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl ='http://www.adulttvlive.net/channels/'
    url =cRequestHandler(sUrl).request() 
    url = url.replace('&nbsp;','')
 
       
    sPattern = '<tr><td valign="top"></td><td><a href="(.*?php)">(.*?).php</a> '
     
               
                                                                                
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(url, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        
       
        for aEntry in aResult[1]:
           
            sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
                          
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
               sUrl ='http://www.adulttvlive.net/channels/'+ sUrl
            
            sTitle = str(aEntry[1])         
            sTitle =buyuktext(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'play__adulttvlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()
def play__adulttvlive():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                              
  
      
    TIK='|Referer='+referer+'&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','Host': 'www.adulttvlive.net','Referer': referer  }
    data= requests.get(Url, headers = headers).text
    if  'Clappr.Player' in data:        
        sHosterUrl = re.findall('source:"(.*?)"', data)[0]+TIK
    else:
        sHosterUrl = re.findall('file:"(.*?)"', data)[0]+TIK
        sHosterUrl =sHosterUrl.replace('playlist.m3u8','chunks.m3u8')             
        sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
        
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()      
         
def LiveTV():
    oGui = cGui()
   

        #oInputParameterHandler = cInputParameterHandler()
        #sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl ='http://oklivetv.com/genre/adult-18/?orderby=likes'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'http://miplayer.net/embed.php?id=ligtv1&width=650&height=480&autoplay=true', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    url = getHtml(sUrl)
#    url = unicode(url, 'latin-1')#converti en unicode

 
       
    sPattern = '<div class="thumb">.*?<a class="clip-link" data-id=".*?" title="(.*?)" href="(.*?)">.*?<img src="(.*?)"'
     
   
                                                                                
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(url, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        
       
        for aEntry in aResult[1]:
          
           
            sPicture = str(aEntry[2])
                            
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
               sUrl ='http:'+ sUrl
            sTitle = str(aEntry[0])        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'fatplaylive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
def fatplaylive():
    oInputParameterHandler = cInputParameterHandler()
    token =  "http://www.adulttvlive.net/channels/leotv.php"                             
                                         
#    url= cRequestHandler(token).request() 
    headers = {'Referer': 'http://www.adulttvlive.net/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    sJson = requests.get(token, headers = headers).text    
    urll = re.findall('file:"(.*?)"',sJson , re.S)[0] +"|Referer="+token+"&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    name =  "https://goo.gl/wqsVrs"  
    url=  "http://live.redtraffic.xyz/teen.m3u8" 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')
                                                                                        
   
def play__LiveTV2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    referer ='http://oklivetv.com/genre/adult-18/?orderby=likes'
    dat= cRequestHandler(sUrl).request()                                                                                                   	
    url = re.findall("<iframe style='width:100%;height:100%;background-color: #1A1A1A;' scrolling='no' frameborder='0' src='(.*?)'",dat, re.S)[0]
    if not 'http' in url:
         url ='http:'+ url                      
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Referer': referer  }
    data= requests.get(url, headers = headers).text   
    data=data.replace('" class="current">','">')
    sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
    tarzlistesi = re.findall('id="tab.*?" href="(.*?)">(.*?)</a>', data , re.S)
    for sUrl,sTitle in tarzlistesi:
        Url ='http://oklivetv.com/xplay/'+ sUrl
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'play__LiveTV3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()   
       
    
def play__LiveTV3():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                               
 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Referer': referer  }
    data= requests.get(url, headers = headers).text
    data=data.replace('\r',"").replace('\s',"").replace('\n',"")
    if re.search('<div id="object_container"', data):    
               rUrl = re.findall('<script src="(.*?)"', data)[0]
               if not 'http' in rUrl:
                  rUrl = 'http:' + rUrl
               ptaweHosters(rUrl)
               
    if  'id="wrd"' in data:
          rUrl = re.findall('src="(.*?)"', data)[0]
          rUrl =rUrl.replace(' ', '%20')
          if not 'http' in rUrl:
                rUrl = 'http:' + rUrl
         
          
          
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Referer': referer  }
          ata= requests.get(rUrl, headers = headers).text
          ata =ata.replace("\/",'/').replace("\\",'')  
        
            
          sHosterUrl =  ata
          #sHosterUrl='https://fash1043.cloudycdn.services/slive/_definst_/ftv_midnite_secrets_adaptive.smil/playlist.m3u8|Referer=http://oklivetv.com/xplay/4d6a5131.html&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'
   
    sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
  
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()      
  
def ptaweHosters(rUrl):
    oGui = cGui()


   
  
    referer ='http://oklivetv.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Referer': referer  }
    ata= requests.get(rUrl, headers = headers).text
    prUrl =re.findall("'(//pt.protoawe.com.*?)',", ata)[0]
          
    if not 'http' in prUrl:
         prUrl = 'http:' + prUrl 
    
    resp = getHtml(prUrl)
    data = resp.content                                                                                                        	
    data = data.replace('\/','/')
      
                               
    tarzlistesi = re.findall('gaLabel: "(.*?)".*?url: "(.*?)",', data , re.S)
    # 1 seul resultat et sur leur propre hebergeur
    for sTitle,sUrl in tarzlistesi:
        
       
            
    
    
        Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
      
        if not 'http' in sUrl:
           sUrl = 'http:' + sUrl  
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
     
  

def GetPlayList():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    pos = oInputParameterHandler.getValue('sMovieTitle')
    img = oInputParameterHandler.getValue('sThumbnail')
    data = getHtml(url)
    
 
    s_url = ''
    s_num = 0
    for rec in re.compile('{(.+?)}', re.MULTILINE|re.DOTALL).findall(data.replace('{"playlist":[', '')):
        for par in rec.replace('"','').split(','):
            if par.split(':')[0]== 'comment':
                sTitle =' Video_'+  str(s_num+1) #par.split(':')[1]+' '
            if par.split(':')[0]== 'file':
                if 'http' in par.split(':')[1]:
                    s_url = par.split(':')[1]+':'+par.split(':')[2]
               
        s_num += 1

        if s_num >= pos :
                    sPicture='http://ero-tv.org/wp-content/uploads/2014/08/brazzers.gif'
                    
                    liste = []
                    liste.append( [sTitle,s_url] )
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', str(s_url))
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                    oOutputParameterHandler.addParameter('liste', str(liste))
                    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
                    oGui.addMovie(SITE_IDENTIFIER, 'otvplay__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
        
  
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

def dizizleABC():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    name =  malfabekodla(sTitle)       
        
  
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            



def otvplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle =  malfabekodla(sTitle)
    sHosterUrl = sUrl+ '|User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    

      
    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 

def pornhdGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    
    data = getHtml(url)                                                                                                        	
                          
    if re.match('.*?<li class="category"', data, re.S):    
      data = data.replace("\n",'')
      tarzlistesi = re.findall('<li class="category"><a href="(.*?)".*?data-original="(.*?)".*?</span>(.*?)</a>', data , re.S)
      for sUrl,sPicture,sTitle in tarzlistesi:
        Url ='https://www.pornhd.com'+ sUrl
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'pornhdliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  
def wpornhdliste():
   

    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    name=  malfabekodla(sTitle)
    urla  = "https://www.pornhd.com/"
                     
    referer=[('Referer',urla)]
    url=gegetUrl(urll,headers=referer)  
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')

def pornhdliste():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
       
    urla  = "https://www.pornhd.com/"
                     
    referer=[('Referer',urla)]
    sHtmlContent=getHtml(url)
 
    tarzlistesi = re.findall('data-mp4=".*?" data-webm=".*?" data-id=".*?" data-video=".*?" ><a class=".*?" href="(.*?)"><img alt="(.*?)"  src="(.*?)"', sHtmlContent , re.S)
    for sUrl,sTitle,sPicture in tarzlistesi:
        Url ='https://www.pornhd.com'+ sUrl
        sTitle = malfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'pornhdHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    
  
def pornhdNextPage(sHtmlContent,sUrl):
    oGui = cGui()
    

                                 
      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '<li class="next ">.*?<span class="icon jsFilter js-link" data-query-key="page" data-query-value="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sUrl)+'?page='+ aResult[1][0]
    return False


def hdpornGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    
    data = getHtml(url)                                                                                                        	
    
    if re.match('.*?<div id="main">', data, re.S):    
      data = data.replace("\n",'')
      tarzlistesi = re.findall('<div class="content">.*?<a href="(.*?)" title="(.*?)".*?src="(.*?)"', data , re.S)
      for sUrl,sTitle,sPicture in tarzlistesi:
        Url ='http://hdporn.net'+ sUrl
        sTitle = malfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'hdpornliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  



def hdpornliste():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
       
                                                                                                                                       
    sHtmlContent =  getHtml(url)
    tarzlistesi = re.findall('<div class="content col-xs-12 col-sm-4 col-md-3">.*?<a  href=".*?" title="(.*?)" target="_self">.*?src="(.*?)".*?this.src="(.*?.mp4)/.*?.mp4-.*?.jpg"', sHtmlContent , re.S)
    for sTitle,sPicture,sUrl in tarzlistesi:
        Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
       
        Url = sUrl.replace('thumbs','videos')+ '|' + Header 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) 
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  

def hdpornNextPage(sHtmlContent,url):
    oGui = cGui()
    

    
      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '<div id="pagination">.*?<span>.*?</span><a href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sUrl)+ aResult[1][0]
    return False


def redtubeGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
                                                                                  
                        
    sHtmlContent = cRequestHandler(url).request()
    sHtmlContent = sHtmlContent.replace("\n",'').replace("//cdne",'http://cdne')
    tarzlistesi = re.findall('<button class="dropdown_option js_drpd_item" type="button" data-value="(.*?)">(.*?)</button>', sHtmlContent , re.S)
    for sUrl,sTitle  in tarzlistesi:
        Url ='http://www.redtube.com/redtube/'+ sUrl
        
        sPicture='https://ei.rdtcdn.com/www-static/cdn_files/redtube/images/pc/category/'+ sUrl+'_001.jpg'
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'redtubeliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    
     
def redtubeliste(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    
    data = cRequestHandler(url).request()                                                                                                       	
    data = data.replace("\n",'')
      
     
         
         
         
                          
    tarzlistesi = re.findall('<img id="img_browse_(.*?)".*?src="(.*?)".*?alt="(.*?)"', data , re.S)
    for sUrl,sPicture,sTitle in tarzlistesi:
        Url ='https://www.redtube.com/'+ sUrl
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        
        oGui.addMovie(SITE_IDENTIFIER, 'redtubeHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  
def redtubeNextPage(sHtmlContent,sUrl):
    oGui = cGui()
    
    
    
    kUrl ='http://www.redtube.com'  
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = 'id="currentPageNum"><b>.*?</b></a>.*?<a href="(.*?)" title=".*?" onclick="trackByCookie.*?'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(kUrl)+ aResult[1][0]
    return False



def pornhubGenre():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
   
    data = getHtml(url)                                                                                                       	

						                                                                                                                                                        
							                 
    tarzlistesi = re.findall('<a class="js-mixpanel" data-mixpanel-listing="" href="(.*?)" onclick="ga.*?;" alt="(.*?)">.*?<img class="js-menuSwap" data-image="(.*?)"', data , re.S)
    for sUrl,sTitle,sPicture in tarzlistesi:
        Url ='https://de.pornhub.com'+ sUrl
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'pornhubliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
def pornhubliste(sSearch = ''):
   
    oGui = cGui()
       
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.fox.com.tr/bolum-izle'
        request = urllib2.Request(url,data,headers)
          
  
      #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="preloadLine">.*?<a href="(.*?)" title="(.*?)".*?data-related-url="(.*?)".*?data-mediumthumb="(.*?)"'                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl= oInputParameterHandler.getValue('siteUrl')
       
        sHtmlContent = getHtml(sUrl)  
        
   

                                            
			                                                                                                     	
                                            
                               
        sPattern = '<div class="preloadLine">.*?<a href="(.*?)" title="(.*?)".*?data-related-url="(.*?)".*?data-thumb_url = "(.*?)"'                    

                                         
    sHtmlContent = sHtmlContent
   
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        
       
        for aEntry in aResult[1]:
            sTitle = aEntry[1] 
           
            
                
            Url ='https://de.pornhub.com'+ aEntry[0]
            sPicture =aEntry[3]+getHeaders(Url)
            logger.info('sPicture>%s' %sPicture) 
           # sPicture  = unicode(sPicture , errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
#            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'redtubeHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        
           
        if not sSearch:
          
            sNextPage = pornhubNextPage(sHtmlContent,sUrl)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pornhubliste', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                              #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def pornhubNextPage(sHtmlContent,sUrl):
    oGui = cGui()
                 
   
    sHtmlContent =sHtmlContent.replace('amp;','')
    kUrl ='http://www.pornhub.com'                                      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = ' <li class="page_current"><span class="greyButton">.*?<li class="page_number"><a class="greyButton" href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(kUrl)+ aResult[1][0]
    return False                 
def __checkForNextPage(sHtmlContent):
    oGui = cGui()
    

    
      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '<li class=\'active\'><a href=".*?">.*?</a></li>.*?<li ><a href="(.*?)">.*?</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_MAIN)+ aResult[1][0]
    return False


def mpornhdHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    
    
    sHtmlContent =  cRequestHandler(url).request()
    sHtmlContent = sHtmlContent.replace('\/','/')
    sTitle = cUtil().DecoTitle(sTitle)       
    sPattern = '"720p":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
          
    if (aResult[0] == True):
        
        
            
        sUrl= '' + aResult[1][0]
           
        

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sUrl)
        oGuiElement.setThumbnail(sThumbnail)

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
        return
        
    oGui.setEndOfDirectory()    
def play__():
   

    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    name= sTitle
      
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def playVideo(isAutoplay = False):
        oInputParameterHandler = cInputParameterHandler()
        urlll = oInputParameterHandler.getValue('siteUrl')
        title = oInputParameterHandler.getValue('sMovieTitle')
        if title:
            listitem.setInfo('video', {'title': title})

        if not isAutoplay:
            xbmcplugin.setResolvedUrl(self.handle, True, listitem)
        else:
            url = urllib.unquote_plus(urlll)
            xbmc.Player().play(url, listitem)                                                                                            

def play2():
    
                     
    oInputParameterHandler = cInputParameterHandler()
    rest = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    sHosterUrl= rest + '|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36' + Header    

    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
NO_DEFAULT=""

_search_regex=''
def extract_js_vars(webpage, pattern, default=NO_DEFAULT):
            assignments = _search_regex(
                pattern, webpage)
            if not assignments:
                return {}

            assignments = assignments.split(';')

            js_vars = {}

            def parse_js_value(inp):
                inp = re.sub(r'/\*(?:(?!\*/).)*?\*/', '', inp)
                if '+' in inp:
                    inps = inp.split('+')
                    return functools.reduce(
                        operator.concat, map(parse_js_value, inps))
                inp = inp.strip()
                if inp in js_vars:
                    return js_vars[inp]
                return remove_quotes(inp)

            for assn in assignments:
                assn = assn.strip()
                if not assn:
                    continue
                assn = re.sub(r'var\s+', '', assn)
                vname, value = assn.split('=', 1)
                js_vars[vname] = parse_js_value(value)
            return js_vars

def redtubeHosters():
   oGui = cGui()
                        
   oInputParameterHandler = cInputParameterHandler()
   Url2 = oInputParameterHandler.getValue('siteUrl')
                          
   
   oRequest = cRequestHandler(Url2)

                        
   oRequest.addHeaderEntry('Referer', 'https://de.pornhub.com/categories/')
   oRequest.addHeaderEntry('Connection', 'keep-alive')
   oRequest.addHeaderEntry('Upgrade-Insecure-Requests', '1')
   oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
   oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
   oRequest.addHeaderEntry('Cookie', 'ua=1a2dc04bb795f060fbb9a0d4921dd3e5')
#       oRequest.addHeaderEntry('Sec-Fetch-Mode', 'navigate')
#       oRequest.addHeaderEntry('Sec-Fetch-Dest', 'iframe')
#       oRequest.addHeaderEntry('Referer', Url )
   oRequest.addHeaderEntry('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7')
#       oRequest.addHeaderEntry('Cookie', cookie)
   oRequest.addHeaderEntry('Accept-Encoding', 'gzip, deflate')
      
       
   FIX = ('media', 'quality', 'qualityItems')

   html= oRequest.request()
   html=to_utf8(html)
   sections = re.findall(r'(var\sra[a-z0-9]+=.+?);flash', html)
   for section in sections:
    
          

      pvars = re.findall(r'var\s(ra[a-z0-9]+)=([^;]+)', section)
      link = re.findall(r'var\smedia_\d+=([^;]+)', section)[0]
      link = re.sub(r"/\*.+?\*/", '', link)
      for key, value in pvars:
                    link = re.sub(key, value, link)
      link = link.replace('"', '').split('+')
      link = [i.strip() for i in link]
      link = ''.join(link)
      bink =link.replace('/1080P', '_1080P').replace('/240P', '_240P').replace('/720P', '_720P').replace('/480P', '_480P').replace('/,1080P', '_1080P')           
      sTitl = re.findall('https://.+?_([0-9]+)P_.+?', bink, re.IGNORECASE)
      for sTitle in sTitl:    
        
                        
        oOutputParameterHandler = cOutputParameterHandler()                           
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', link)
        oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)


   oGui.setEndOfDirectory() 
    
def mredtubeHosters():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url2 = oInputParameterHandler.getValue('siteUrl')
        
   
        oRequest = cRequestHandler(Url2)

                        
        oRequest.addHeaderEntry('Referer', 'https://de.pornhub.com/categories/')
        oRequest.addHeaderEntry('Connection', 'keep-alive')
        oRequest.addHeaderEntry('Upgrade-Insecure-Requests', '1')
        oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
        oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
        oRequest.addHeaderEntry('Cookie', 'ua=1a2dc04bb795f060fbb9a0d4921dd3e5')
#       oRequest.addHeaderEntry('Sec-Fetch-Mode', 'navigate')
#       oRequest.addHeaderEntry('Sec-Fetch-Dest', 'iframe')
#       oRequest.addHeaderEntry('Referer', Url )
        oRequest.addHeaderEntry('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7')
#       oRequest.addHeaderEntry('Cookie', cookie)
        oRequest.addHeaderEntry('Accept-Encoding', 'gzip, deflate')
      
       
        html= oRequest.request()
   
        sources = []

        qvars = re.search(r'qualityItems_[^\[]+(.+?)";', html)
        if qvars:
            sources = qvars.group(1).replace('\\', '')
            sources = [(src.get('text'), src.get('url')) for src in sources if src.get('url')]

        if not sources:
            fvars = re.search(r'flashvars_\d+\s*=\s*(.+?);\s', html)
            if fvars:
                sources = json.loads(fvars.group(1)).get('mediaDefinitions')
                sources = [(src.get('quality'), src.get('videoUrl')) for src in sources if
                           type(src.get('quality')) is not list and src.get('videoUrl')]

        if not sources:
            sections = re.findall(r'(var\sra[a-z0-9]+=.+?);flash', html)
            for section in sections:
                pvars = re.findall(r'var\s(ra[a-z0-9]+)=([^;]+)', section)
                link = re.findall(r'var\smedia_\d+=([^;]+)', section)[0]
                link = re.sub(r"/\*.+?\*/", '', link)
                for key, value in pvars:
                    link = re.sub(key, value, link)
                link = link.replace('"', '').split('+')
                link = [i.strip() for i in link]
                link = ''.join(link)
                if 'urlset' not in link:
                    r = re.findall(r'(\d+p)', link, re.I)
                    if r:
                        info('red- ' + sources)
                        sPicture  = "http://cdne-st.redtubefiles.com/images/logos/logo_RT_premium.png?v=5d9a2e0cf0b93d9f391d915e19214fe37f64c3501481841392"
                        sTitle =  sources
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                        oOutputParameterHandler.addParameter('siteUrl', link)
                        oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        oGui.setEndOfDirectory() 
def mmmredtubeHosters():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
   
  
    url = oInputParameterHandler.getValue('siteUrl')
    resp = getHtml(url)
    data = resp.content                                                                                                        	
    data = data.replace('\/','/')
      
                               
    tarzlistesi = re.findall('sources: ."480":"(.*?)".*?videoTitle: "(.*?)"', data , re.S)
    # 1 seul resultat et sur leur propre hebergeur
    for sUrl,sTitle in tarzlistesi:
        
       
            
    
    
        Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
        sTitle =  sTitle
        sHosterUrl = sHosterUrl + '|' + Header  
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
     
 
def pornhdHosters():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle= oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
   
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('Host', 'www.pornhd.com')
    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; rv:67.0) Gecko/20100101 Firefox/67.0')
    oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    oRequest.addHeaderEntry('Accept-Language', 'en-US,en;q=0.5')
    oRequest.addHeaderEntry('Accept-Encoding', 'gzip, deflate, br')
    oRequest.addHeaderEntry('Referer', sUrl)
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    oRequest.addHeaderEntry('Cookie', '_ga=GA1.2.143518839.1559884905; _gid=GA1.2.955783398.1559884905; webpSupported=1; phd-ses=7rgpj80t3trht0ebh7tp6r87aa; _csrf-frontend=85e2c4571974ef97b3683f46331e0e01184f88c725aea9a192104bcbd7541cffa%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22a3QNbitrgKW6DvfUKFY9csabdXhhk8qM%22%3B%7D; g36FastPopSessionRequestNumber=1')
    oRequest.addHeaderEntry('Upgrade-Insecure-Requests', '1')
    oRequest.addHeaderEntry('Cache-Control', 'max-age=0')
    sHtmlContent = oRequest.request()
    sHtmlContent = sHtmlContent.replace('\/','/')
    oParser = cParser()
    
  
    sPattern =  '"720p":"(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
     
    # 1 seul resultat et sur leur propre hebergeur
    if (aResult[0] == True):
        
        
       
         
       
#        url =requests.get(new_url, allow_redirects=False)
    
#        encoded='eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpc3MiOiJodHRwczpcL1wvd3d3LnBvcm5oZC5jb20iLCJhdWQiOiJodHRwczpcL1wvd3d3LnBvcm5oZC5jb20iLCJqdGkiOiI0MjIwNCIsImlhdCI6MTU1OTkxMTU1MSwiZXhwIjoxNTU5OTEzMzUxLCJ1cmwiOiJwOUVRWFBjYVNEZlE3UXZtQXJuQ0V3T29qZ2FOalludFdseFE2Ykl3c2JXVmVkN0Z0eHJndzJDK1wvd3hpN0dwNllvSlhsUjB5TFhrN0E0VmFub3EzSitzVVozbmxcL1wvRXRTZVhTWGVCVUhXWE5UV1paWkxvWFlUck9lNUJBbnozMCIsInZpZGVvSWQiOjQyMjA0fQ.","480p":"\/gvf\/eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpc3MiOiJodHRwczpcL1wvd3d3LnBvcm5oZC5jb20iLCJhdWQiOiJodHRwczpcL1wvd3d3LnBvcm5oZC5jb20iLCJqdGkiOiI0MjIwNCIsImlhdCI6MTU1OTkxMTU1MSwiZXhwIjoxNTU5OTEzMzUxLCJ1cmwiOiJwOUVRWFBjYVNEZlE3UXZtQXJuQ0V3T29qZ2FOalludFdseFE2Ykl3c2JYRjBuU1VoS1wvRE90YjVxMmozS1ozcGRvZHViVnF2U2g4ank2aTdsTWxBOGVWOEMzTFJtREc2UW9cLzVjN1BDczRlR1VxeExIdDBvb3c0RFhLYW9HUGhmIiwidmlkZW9JZCI6NDIyMDR9'
#        jwt.decode(encoded, 'secret', algorithms=['HS256'])
              
        
        res = urllib2.urlopen(sUrl, timeout=12)
        cookie = res.info()['Set-Cookie']
        TIK='|Cookie='+ cookie

          
        link ='https://www.pornhd.com'+aResult[1][0] #+TIK
#        encoded =  b64decode(he) 
#        Url =jwt.decode(encoded, 'secret', algorithms=['HS256'])
        
  
#        Url =urla  = "https://www.pornhd.com/"                            Range: bytes=0-
        
      
     
        
      
        Url = link +TIK
       
        name =  "https://goo.gl/wqsVrs"  
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, Url, '')
     
             
  
    
def GetRealUrl(url):
    oParser = cParser()
    sPattern = '\[REGEX\](.+?)\[URL\](.+$)'
    aResult = oParser.parse(url, sPattern)
    
    if (aResult):
        reg = aResult[1][0][0]
        url2 = aResult[1][0][1]
        oRequestHandler = cRequestHandler(url2)
        sHtmlContent = oRequestHandler.request()
        
        aResult = oParser.parse(sHtmlContent, reg)
        if (aResult):
            url = aResult[1][0]
            
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()
        
    return url
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
    

def epornhubGenre():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    data = requests.get(Url).content
                                                                                                         	

						
							              
    tarzlistesi = re.findall('<div class="categoriesbox" id=".*?"> <div class="ctbinner"> <a href="(.*?)" title=".*?"> <img src="(.*?)" alt="(.*?)">', data , re.S)
    for sUrl,sPicture,sTitle in tarzlistesi:
        Url ='http://www.eporner.com'+ sUrl
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'epornhubliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
