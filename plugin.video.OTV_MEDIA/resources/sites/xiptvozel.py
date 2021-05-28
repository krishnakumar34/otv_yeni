#-*- coding: utf-8 -*-
#python -c "import lxml"
from resources.sites.LIVETV2 import *
try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range





class NoRedirection(urllib2.HTTPErrorProcessor):
  def http_response(self, request, response):
    return response


addon = xbmcaddon.Addon()
class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data
# https://didri.com/raw/Jr1HUK4FCW
#https://paste.rs/PO7
try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)"
USER_DATA_DIR = translatePath(addon.getAddonInfo("profile"))
ADDON_DATA_DIR = translatePath(addon.getAddonInfo("path"))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, "resources")
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

cert_file = os.path.join(RESOURCES_DIR, "com.android.browser-key.cer")
cert_key_file = os.path.join(RESOURCES_DIR, "com.android.browser.cer")

#s.cert = (cert_file, cert_key_file)
ddatam_url = 'http://app.liveplanettv.com/beta/api.php?device_id=354630080742220'
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('profile'))
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
data_file = os.path.join(RESOURCES_DIR, 'data.html')
app_config = os.path.join(RESOURCES_DIR, 'data.html')
AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
icon = Addon.getAddonInfo('icon')
AddonName = Addon.getAddonInfo('name')
addonDir = Addon.getAddonInfo('path')
f4mProxy = os.path.join(addonDir, 'f4mProxy')
SITE_IDENTIFIER = 'xiptvozel'
from resources.lib.config import cConfig
number =''
serial_number = addon.getSetting('serial_number_' + number);

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')

TIK = '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
streamtype = "HLS"
def _get(request, post = None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request, post).read()

yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvMjJ0NGJxbXJtdG55Zng3L290dmlwdHYubTN1P2RsPTA="
URL_WEB=base64.b64decode(yen)
da_url = 'http://glazandroid.com/andr/chas-online-json-1.5.php'
Host = 'https://raw.githubusercontent.com/PrivateTr/Zone_enigma/master/userbouquet.Remy_IPTV2.tv'
Hostbir = 'https://raw.githubusercontent.com/PrivateTr/Zone_enigma/master/userbouquet.Remy_IPTV1.tv'
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'

def okuoku(cba):
    oku = ''
    i = len(cba) - 1
    while i >= 0:
        oku += cba[i]
        i -= 1

    return oku


UA = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36'

headers = {'User-Agent': UA, 'Accept': '*/*', 'Connection': 'keep-alive'}

icon = 'tv.png'
# /home/lordvenom/.kodi/
# sRootArt = cConfig().getRootArt()
sRootArt = 'special://home/addons/plugin.video.vstream/resources/art/tv'


from requests.sessions import Session




selfAddon = xbmcaddon.Addon()
ulkeLists = 'http://85.132.71.12/channels'
ulkeListem = 'http://hyfystreamz.com/dfytv/list.json'

SITE_NAME = 'IPTV OZEL'
MOVIE_VIEWS = (True, 'user_info')
icon = 'tv.png'

def getyoutubepage(url):
    headers = {'Host': 'www.youtube.com',
     'Connection': 'keep-alive',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
     'Accept': '*/*',
     'DNT': '1',
     'Referer': 'https://www.youtube.com',
     'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'en-US,en;q=0.8,de;q=0.6'}
    result = requests.get(url, headers=headers, allow_redirects=True)
    return result.text
def IPTVdep( gobble ) :
        gobble= gobble.replace('get.php',"panel_api.php")
        return gobble










def iptvuser_info():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir('redbox', 'root', 'REDBOX', 'redbox-tv-logo.jpg', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir('Swift', 'root', 'SwiftStream', 'SWIFTlogo.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir('LIVETV', 'roootom', 'LIVE NET', 'turkey-free-iptv.png', oOutputParameterHandler)
    
      
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir('livenettv', 'root', 'Live NetTV v4.8.2', 'LIVENETLogo.png', oOutputParameterHandler)
    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir(SITE_IDENTIFIER, 'STB_link3','IPTV PANEL GÜNCEL-IPTV PANEL UPDATED', 'turkey-free-iptv.png', oOutputParameterHandler)
     
    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir(SITE_IDENTIFIER, 'OKliveTV', 'OKliveTV World ', 'turkey-free-iptv.png', oOutputParameterHandler)
    
    

    oGui.setEndOfDirectory()


#import py_compile        

#py_compile.compile('plugin.pyc')
#py_compile.main(['plugin.pyc', 'plugin.py']) 
#import compileall
#compileall.compile_dir('.')
#compileall.compile_file('plugin.pyc')

primler = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
for urgg in primler: 
    userr = urgg 
    userr = ''

def get_keyboard(heading, default='', hidden=False):
    keyboard = xbmc.Keyboard()
    if hidden:
        keyboard.setHiddenInput(True)
    keyboard.setHeading(heading)
    if default:
        keyboard.setDefault(default)
    keyboard.doModal()
    if keyboard.isConfirmed():
        return keyboard.getText()
    else:
        return None

def prompt_for_link(old_link='', old_name=''):
    if old_link.endswith('\n'): old_link = old_link[:-1]
    if old_name.endswith('\n'): old_name = old_name[:-1]
    new_link = get_keyboard('Edit Link', old_link)
    if new_link is None:
        return

    new_name = get_keyboard('Enter mac', old_name)
    if new_name is None:
        return

    if new_name:
        STB_EMUM(new_link, new_name)
    else:
        return (new_link, )



def spor():
    oGui = cGui()
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir('ssport365', 'Main_menu', 'sporthd Live event, Sport Streams', 'sports.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://freestreams-live1.com/turkey-channels/')
    oGui.addDir(SITE_IDENTIFIER, 'iptvturkem', 'WORLD SPORT LIVE EVENT', 'sports.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '1')
    oGui.addDir('livenettv', 'list_live', 'LIVE EVENT', 'sports.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir(SITE_IDENTIFIER, 'turkom2','GOL VAR LIVE EVENT', 'sports.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '1')
    oGui.addDir('livenettv', 'list_channels', 'SPORT Channels', 'sports.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '1')
    oGui.addDir('redbox', 'list_channels', 'SPORT Channels2', 'sports.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '1')
    oGui.addDir('LIVETV', 'list_channels', 'SPORT Channels3', 'sports.png', oOutputParameterHandler)
   
                                            
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '1')
    oGui.addDir(SITE_IDENTIFIER, 'Open_settings', '[COLOR lime][B]Open Setting- Saat ayari-Time setting [/B][/COLOR]', 'sports.png', oOutputParameterHandler)
    
        


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir(SITE_IDENTIFIER, 'peerstv','root test', 'canliio.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()

def Open_settings():
  
      cConfig().showSettingsWindow()

                               
                             
def sporturke(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://sportbar.biz/beinsport1tur.html')
    oOutputParameterHandler.addParameter('sMovieTitle', 'TR-BEIN SPOR 1 HD')
    oGui.addDir(SITE_IDENTIFIER, 'freestreams3', 'TR-BEIN SPOR 1 HD', 'beinsports1.jpg', oOutputParameterHandler)
  
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '62')
    oOutputParameterHandler.addParameter('sMovieTitle', 'TR-BEIN SPOR 1 HD')
    oGui.addDir(SITE_IDENTIFIER, 'freestreams2', 'TR-BEIN SPOR 1 HD', 'beinsports1.jpg', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.futbolcafe120.xyz/futbolcafe/izle/bein1.html')
    oOutputParameterHandler.addParameter('sMovieTitle', 'TR-BEIN SPOR 1 HD')
    oGui.addDir(SITE_IDENTIFIER, 'freestreams3', 'TR-BEIN SPOR 1 HD', 'beinsports1.jpg', oOutputParameterHandler)
   
    oOutputParameterHandler.addParameter('siteUrl', '63')
    oOutputParameterHandler.addParameter('sMovieTitle', 'TR-BEIN SPOR 2 HD')
    oGui.addDir(SITE_IDENTIFIER, 'freestreams2', 'TR-BEIN SPOR 2 HD', 'beinspor2.png', oOutputParameterHandler)
                            #videoLink = '(.*?)'
    oOutputParameterHandler.addParameter('siteUrl', 'https://sportbar.biz/turbein2sport.html')
    oOutputParameterHandler.addParameter('sMovieTitle', 'TR-BEIN SPOR 2 HD')
    oGui.addDir(SITE_IDENTIFIER, 'freestreams3', 'TR-BEIN SPOR 2 HD', 'beinspor2.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', '64')
    oOutputParameterHandler.addParameter('sMovieTitle', 'TR-BEIN SPOR 3 HD')
    oGui.addDir(SITE_IDENTIFIER, 'freestreams2', 'TR-BEIN SPOR 3 HD', 'beinsports3.jpg', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', '67')
    oOutputParameterHandler.addParameter('sMovieTitle', 'TR-BEIN SPOR 4 HD')
    oGui.addDir(SITE_IDENTIFIER, 'freestreams2', 'TR-BEIN SPOR 4 HD', 'beinspor4.png', oOutputParameterHandler)


    oGui.setEndOfDirectory() 

def SSSTB_EMUM_info():
  oGui = cGui()
  s_num = 0
  primler = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
  for urge in primler:   
       s_num += 1
   
      # break
       oOutputParameterHandler = cOutputParameterHandler()
       oOutputParameterHandler.addParameter('urg', urge)
       oGui.addDir(SITE_IDENTIFIER, 'turkom2','GOL VAR Link-'+str(s_num+0), 'canliio.png', oOutputParameterHandler)
    
  oGui.setEndOfDirectory()
import math  
import string
import random
from datetime import date

today = str(int(time.time() * 60))

def id_generator(size=8, chars=today):
   return ''.join(random.choice(chars) for _ in range(size))
def deCFEmail(fp):
        try:
            r = int(fp[:2],16)
            email = ''.join([chr(int(fp[i:i+2], 16) ^ r) for i in range(2, len(fp), 2)])
            return email
        except (ValueError):
            pass





from collections import OrderedDict

s = requests.Session()
from resources.lib.comaddon import VSlog
from resources.lib.config import GestionCookie
from requests.adapters import HTTPAdapter
from collections import OrderedDict
import re, ssl, requests  #, os, time, json, random
from requests.sessions import Session
from resources.lib.util import urlEncode

try:  # Python 2
    from urlparse import urlparse
except ImportError:  # Python 3
    from urllib.parse import urlparse

# old version
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
def CleanTitle(title):
    title = cUtil().unescape(title)
    title = cUtil().removeHtmlTags(title)
    try:
        #title = unicode(title, 'utf-8')
        title = unicode(title, 'iso-8859-1')
    except:
        pass
    title = unicodedata.normalize('NFD', title).encode('ascii', 'ignore')
    
    return to_utf8(title)
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
user_file = os.path.join(ADDON_DATA_DIR, 'plugin.pyc' )
input_code =CleanTitle(user_file)
try:
    with io.open(input_code, 'rb') as f:
        input_cod = f.read()
except IOError:
    input_cod = ''


try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin
interpreter=""
#UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'


import sys
import re
def getTimer():
    datenow = datetime.utcnow().replace(second=0, microsecond=0)
    datenow = datenow + timedelta(days=1)
    epoch = datetime(1970, 1, 1)

    return (datenow - epoch).total_seconds() // 1


AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
vnnput_code = os.path.join(RESOURCES_DIR, 'livenettv.db')

def canlitv(url):
    headers = {'Host': 'izle.canlitvlive.io',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
     'Accept': '*/*',
     'Accept-Language': 'de-DE,tr-TR;q=0.8,tr;q=0.6,en-US;q=0.4,en;q=0.2',
     'Accept-Encoding': 'gzip, deflate, br',
     'Connection': 'keep-alive',
     'Referer': 'https://izle.canlitvlive.io/kanal-d-canli-izle-210506',
     'Cookie': '_ga=GA1.2.745982601.1617351284; __gads=ID=ec8243411b51eb5d-2282ab757aa70044:T=1617978259:S=ALNI_MbHRfr5m09vkV7vQZLXMXQW10gI4w; __cfduid=de1a3b6fdef3863330690394c3d52039a1620114779; _gid=GA1.2.1945820051.1620327937; termsCookies=true; PHPSESSID=247c4dd66baa765ca5551b15f614ba29; _GPSLSC=',
     'TE': 'Trailers'}
    result = requests.get(url, headers=headers, allow_redirects=True)
    return result.headers
#UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0'


def deCFEmail(fp):
        try:
            r = int(fp[:2],16)
            email = ''.join([chr(int(fp[i:i+2], 16) ^ r) for i in range(2, len(fp), 2)])
            return email
        except (ValueError):
            pass
try:
    from sqlite3 import dbapi2 as sqlite
except:
    from pysqlite2 import dbapi2 as sqlite
DB = 'special://home/addons/plugin.video.OTV_MEDIA/resources/livenettv.db'

try:
    REALDB = VSPath(DB).decode('utf-8')
except AttributeError:
    REALDB = VSPath(DB)
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    from contextlib import closing

    with closing(sqlite3.connect(db_file)) as connection:
      with closing(connection.cursor()) as cursor:
        rows = cursor.fetchall()
        print(rows)
        return  rows

 


# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
import imp
def makemodule(sourcestr = ''):
    oInputParameterHandler = cInputParameterHandler()
    modname = oInputParameterHandler.getValue('sMovieTitle')
    url = 'https://raw.githubusercontent.com/streamxstream/plugin.video.xstream/nightly/sites/' +  modname
    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {"User-Agent": UA}
    modsource = urllib.request.urlopen(urllib.request.Request(url, data=None, headers=headers)).read()
    obj = compile(modsource, sourcestr, 'exec')
    module = imp.new_module(modname)
    exec(obj, module.__dict__)
    logger.info("plugin: %s" %module )
    return module




def peerstv(): #affiche les genres
    oGui = cGui()
       
    ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
    SITES_DIR = os.path.join(ADDON_DATA_DIR, 'resources','sites')
                         
    oInputParameterHandler = cInputParameterHandler()
    Urrl = 'https://github.com/streamxstream/plugin.video.xstream/tree/nightly/sites'
    #logger.info("STB_EMU STB_EMU_Urll: %s" % Urrl )
#    cookie = getUrl(Url, output='cookie').result
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
        module = imp.new_module(aEntry[0])
        exec(obj, module.__dict__)
        modul = str(module).replace("<module '", "'>")
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













UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'   
def captoken():
    site_key = "6LeII50UAAAAAA5jiKIwKnJ_iDc9uVuc7qzYi8-_"
    co = "aHR0cHM6Ly93d3cuMjRkZXR2LmRlOjQ0Mw.."
    sa = ''
    cb = 's5kxgdpbca0j'
    headers1 = {'user-agent':UA,
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
               'Referer':'https://www.24detv.de/'
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
      #  import ffmpeg_streaming
def vyeniplay():
        oInputParameterHandler = cInputParameterHandler()
        name = oInputParameterHandler.getValue('sMovieTitle')
        v_id = oInputParameterHandler.getValue('siteUrl')
                               
        logger.info("sUrl : %s" % url)
        s = requests.Session()
        cookie_string = "; ".join([str(x) + "=" + str(y) for x, y in s.cookies.items()])
        token = 'https://redirectdetective.com/ld.px'
        post_data = {'w':v_id,'f':'false'}
        s = requests.Session()
        r = s.post(token, headers={'Cookie': '__utma=132634637.1201225376.1617003196.1617003196.1617003196.1; __utmc=132634637; __utmz=132634637.1617003196.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=132634637.3.10.1617003196',
             'Referer': 'https://redirectdetective.com/',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
             'Origin': 'https://redirectdetective.com',
             #'Connection': 'Keep-Alive',
             'Accept-Encoding': 'gzip'}, data=post_data, timeout=10)
        urll = r.text#.replace("\\", '')
        logger.info("sUrl : %s" % urll)
        url = re.search('.+?title="(.+?)">https://.+?....</a></button>', urll).group(1)
        
        addLink('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url,'')
                
                                     

def mpeerstv():
#    oGui = cGui()
            cfmail='4120252c282f01382023202f222825283b286f2e3326'
            decodemail=deCFEmail(cfmail)
            logger.info("decodemail: %s" %decodemail )
            url = "https://yabancidizi.org/film-izle"
            r = requests.get(url)                              
            r.headers
            cookie_arg=r.headers['Set-Cookie']
            logger.info("res : %s" %r.headers ) 
            headerss = {   'Host': 'yabancidizi.org',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                   'Content-Type': 'application/x-www-form-urlencoded',
#                   'Accept-Language': 'de-DE,tr-TR;q=0.8,tr;q=0.6,en-US;q=0.4,en;q=0.2',
                   'Connection': 'keep-alive',
                  # 'Referer': 'https://www.yabancidizi.pw/',
                   'Cookie': cookie_arg}                     
#                   'Accept-Encoding': 'gzip, deflate'} 
#    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
            payload = {'email' : decodemail ,'data' : 'abcacfc6c2c5ebd2cac9cac5c8c2cfc2d1c285c4d9cc'}
            s = requests.Session()
            r = s.post(url ,  headers=headerss,data=payload , allow_redirects=False)
            #urrl=r.headers['Location']            
            
            #bod =to_utf8(r.text)
           # time.sleep(5)
            #logger.info("cf : %s" %r.headers)
            #logger.info("cf : %s" %r.text) 
            #cookie =SetCookie(urll)
            urrl=r.headers['Location']
            r = requests.get(urrl)                              
            r.headers
            cookie=r.headers['Set-Cookie']
           
            urr='https://cdn-cgi/challenge-platform/h/b/orchestrate/jsch/v1?ray=64ce1cd49e0505ed'
            body= requests.get(urr,  headers={'Cookie':cookie,'Referer': 'https://yabancidizi.pw/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'Host': 'yabancidizi.pw',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'}).text
            bod =to_utf8(body)
            logger.info("cfkkk : %s" %bod) 
           # jschl_answer = JavaScriptInterpreter.dynamicImport(interpreter ).solveChallenge(body, hostParsed.netloc)
                                      
            jschl_answer = re.search('hh: "(.+?)"', bod).group(1)
            tok = re.search('id="challenge-form" action="(.+?)"', bod).group(1)
            rep = re.search('type="hidden" name="r" value="(.*?)"', bod).group(1)
            jschl_vc= re.search('type="hidden" value="(\w+)"', bod).group(1)
            pas= re.search('type="hidden" name="pass" value="(.*?)"', bod).group(1)
                          
            
            token = "https://www.yabancidizi.pw" + tok
            #token  = token+"&ul=de-de&de=UTF-8&dt=yabancidizi.org%20|%20yabanc%C4%B1%20dizi%20izle,%20yabanc%C4%B1%20film%20izle&sd=24-bit&sr=1536x864&vp=1163x750&je=0&ec=general&ea=HeartBeat&_u=CACAAUABAAAAAC~&jid=1778031460&gjid=1363167938&cid=484785676.1614953100&tid=UA-187930534-1&_gid=1363860594.1616864270&_r=1&gtm=2ou3h0&z=1324323876" 
            s = requests.Session()                                                       
            r = requests.get(token)                              
            r.headers
            logger.info("token : %s" %r.headers)          
             
            post_data = {'r': rep,'jschl_vc':jschl_vc,'pass':pas,'jschl_answer':jschl_answer,'cf_ch_verify':'plat'}
            logger.info("ost_data : %s" %post_data ) 
            r = s.post(token, headers={'Cookie':cookie_arg,
             'Content-Type': 'application/x-www-form-urlencoded',
             'Referer': 'https://yabancidizi.pw/',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
             'Accept-Encoding': 'gzip'}, data=post_data)
            auth = to_utf8(r.text)                         
            time.sleep(5)
            logger.info("auth: %s" %auth  )                  
                        
def peerstvplay():
        oInputParameterHandler = cInputParameterHandler()
        sUrl= oInputParameterHandler.getValue('siteUrl')+'|Referer=https://golvar2.com/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        name = oInputParameterHandler.getValue('sMovieTitle')
        sUrl= sUrl+'|Referer=https://peers.tv/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, sUrl, '')         
       


def get_videos_decodedlink(url,pattern,titlen,urln, imgn=None, mmgn=None):
            oParser = cParser()
            
            sHtmlContent = cRequestHandler(url).request()
            
            oParser = cParser()
            aResult = oParser.parse(sHtmlContent, pattern)
            if (aResult[0] == True):
               total = len(aResult[1])
               for aEntry in aResult[1]:

               
                  
                    title =aEntry[titlen] 
                    logger.info("==text_pattern: %s" %   title)
                    url = aEntry[urln]
                    logger.info("==text_pattern: %s" %   url)
                    img = aEntry[imgn]
                    logger.info("==text_pattern: %s" %   img)
                    mmg = aEntry[mmgn]
                    logger.info("==text_pattern: %s" %   mmg)
def get_films( url, pattern_1, pattern_2,titlen,urln, imgn,imdbn, sonraki=None):
            page = cRequestHandler(url).request()
            logger.info("TURKVODPARSER test: %s" %page)
            video_list_temp = []
            chan_counter = 0
            if pattern_2=='' or re.search(pattern_1, page):    
                pattern = pattern_1
            else:
                pattern = pattern_2
            
            aResult = oParser.parse(page,pattern) # finditer
            if (aResult[0] == True):
              for aEntry in aResult[1]:
             
                title =  aEntry[titlen]#.replace('/',' ').replace('izle','').replace('dizi','')
                logger.info("TURKVODPARSER  title : %s" % title )
               
                imdb = aEntry[imdbn]
                logger.info("TURKVODPARSER  imdb: %s" % imdb)
                url = aEntry[urln]
                logger.info("TURKVODPARSER  url: %s" % url)
               
                  
                img = aEntry[imgn]
def __createDisplayStart(iPage):
    return (1 * int(iPage)) + 1
         
def kom():
     iPage =1
     oInputParameterHandler = cInputParameterHandler()
     iPage = oInputParameterHandler.getValue('siteUrl')
     Page =__createDisplayStart(iPage)
     return Page
def mturkomkom():
    
     oGui = cGui()
     iPage =1
     
     sTitle ='test-'+kom()
     logger.info("time_auth: %s" % sTitle)  
     oOutputParameterHandler = cOutputParameterHandler()
     oOutputParameterHandler.addParameter('siteUrl',iPage)
     oGui.addDir(SITE_IDENTIFIER, 'kom', sTitle, 'genres.png', oOutputParameterHandler)
     oGui.setEndOfDirectory()  



          
#from resources.lib.regexer import Regexer    
def turkomkom():
#   Url2='https://jetfilmizle.live/film-turu/aksiyon-filmleri'
    Urrl="https://yabancidizi.pw/"
#    Url='http://destek.korax.com.tr/UYDUSIS/CLOUD.txt'
    cookie =  gegetHtml(Urrl)
    logger.info("aEntry _cookie: %s" %cookie)
#    from resources.lib.handler.requestHandler import cRequestHandler                         
#    data = 'cf-request-id=08e171613c00004e867c288000000001' #+ test
#    oRequest = cRequestHandler(url)
#    oRequest.addHeaderEntry('cf-ray', '6314dc8608442c22-FRA')
#    oRequest.addHeaderEntry('Referer', 'https://yabancidizi.pw/')
#    oRequest.addHeaderEntry('content-type', 'text/html; charset=UTF-8')
#    oRequest.addHeaderEntry('CF-Challenge', 'c64cfc77ea94956')
#    oRequest.addHeaderEntry('nel', '{"max_age":604800,"report_to":"cf-nel"}')
#    oRequest.addHeaderEntry('report-to', '{"group":"cf-nel","endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report?s=R2QSCkqjGAFKOQzm0Gsz70GtD72yK%2BuPU1KnV16LiRaVE5u%2Flg6YqV2VoScXyXaoE3WABvY7M4C9YgjrOY7bQRwpDWPQy6zKohY9KVMS3d6%2B41USofri0mNiIw%3D%3D"}],"max_age":604800}')
#    oRequest.addHeaderEntry('server', 'cloudflare')
#    oRequest.addHeaderEntry('vary', 'Accept-Encoding')
#    oRequest.addHeaderEntry('Host', 'yabancidizi.pw')
#    oRequest.addHeaderEntry('Cookie', cookie)
#    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
#    oRequest.addParametersLine(data)
#    Json = oRequest.request()
    #logger.info("aEntry _auth: %s" %Json )  
   ##url = v_id["url"]
            #title = v_id.group('title')
            #img = v_id.group('img')
  # logger.info("aEntry _auth: %s" % url  )  
            #logger.info("aEntry _auth: %s" %title  )    
            #logger.info("aEntry _auth: %s" %img  )        
import parsers
def mturkomkom():
                 # fetch(url)
            name='showtv'      
            urll='https://www.showtv.com.tr/dizi/tum_bolumler/alev-alev-sezon-1-bolum-18-izle/94160'
            url = parsers.parse(urll)
            subs = []
            is_array = lambda var: isinstance(var, (list))
            if is_array(url):
                subs =url[1]
                url = url[0]
                isArray = True
            url = url.replace("#", "|")
            url = url.strip()  # 
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')    
            logger.info("aEntry _auth: %s" % url  )  
           
           # sPicture = str(aEntry[2])
            
            #Link = aEntry[0]
            #sTitle=  aEntry[1]                                                                     
            
#            sTitle = sTitle.replace('\n',"").replace('u015a',"S").replace('u0105',"a").replace('u0119',"e").replace('u017c',"z")
                                        
            #oOutputParameterHandler = cOutputParameterHandler()
            #oOutputParameterHandler.addParameter('siteUrl', Link)
            #oGui.addTV(SITE_IDENTIFIER, 'play__weebtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        
                      
        
    


#            sTitle = sTitle.replace('\n',"").replace('u015a',"S").replace('u0105',"a").replace('u0119',"e").replace('u017c',"z")
                                        

  
def _prepare_time_and_rpc():
    millis = int(round(time.time() * 1000))
   
    rand = random.randint(1, 99999999)
    a = '0.%s' % str(rand * 2147483647)
    rpc = int(100000000 * float(a))
    #xbmc.log('Rpc-token: %s' % rpc)
    return (millis, rpc)



  
import os.path

def generate_sections_of_url(url):
    path = urlparse(url).path
    sections = []; temp = "";
    while path != '/':
        temp = os.path.split(path)
        path = temp[0]
        sections.append(temp[1])
    return sections
def turkom2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    urg= oInputParameterHandler.getValue('urg')
    url="https://mode.cfnode.cloud/cdn/events.json?time=26998259"        
    logger.info("Json url: %s" % url)                                                
    oRequest = cRequestHandler(url)
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    oRequest.addHeaderEntry('Host', 'mode.cfnode.cloud')
    oRequest.addHeaderEntry('Origin', 'https://www.golvar54.co')
    oRequest.addHeaderEntry('Referer', 'https://www.golvar54.co/')
    oRequest.addHeaderEntry('Sec-Fetch-Dest', 'empty')
    oRequest.addHeaderEntry('Sec-Fetch-Mode', 'cors')
    oRequest.addHeaderEntry('Sec-Fetch-Site', 'cross-site')
    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
    Json = oRequest.request()
    Json =to_utf8(Json)
    logger.info("Json url: %s" % Json) 
    aJson = json.loads(Json)
    for cat in aJson:
      bes = cat['live']
      cid = cat['id']
      Title = cat['eventhome']
      bir = cat['eventaway']
      iki = cat['start']
      uc = cat['sport']
      dort = cat['country']
      Urrl='https://golvar1.com/player.html?id=190&title=SSPOR%20TV'
      r = requests.get(Urrl)                              
      r.headers
      res=r.headers['Set-Cookie']
      res = to_utf8(res)
      domain = re.search('domain=.(.+?);', res).group(1)      
      Urrll='https://'+domain+'/player.html?id=190&title=SSPOR%20TV'
      data = getHtml(Urrll)
      iki= '[COLOR blue][B]%s[/B][/COLOR]'%(iki) 
      sTitle =iki+'-'+Title+'-'+bir+'-'+dort
      sTitle  = malfabekodla(sTitle)  
      data = data.replace('"+cid+"',"%s")     
      tion = re.search('poster:"",source:"(https://.+?)"', data).group(1)
      oOutputParameterHandler = cOutputParameterHandler()
      oOutputParameterHandler.addParameter('siteUrl',tion)
      oOutputParameterHandler.addParameter('siteUrlref',Urrll)
      oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
      oGui.addDir(SITE_IDENTIFIER, 'sshowtv', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()  

def sshowtv():
        oInputParameterHandler = cInputParameterHandler()
        sUrl= oInputParameterHandler.getValue('siteUrl')
        sUrlref= oInputParameterHandler.getValue('siteUrlref')
        name = oInputParameterHandler.getValue('sMovieTitle')
        sUrl= sUrl+'|Referer='+sUrlref+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, sUrl, '')         
       

                  #Host=mode.cfnode.cloud&


    
    
    
    
		
     
from datetime import datetime       
def m3uliste():
    url = cRequestHandler('http://iptvhit.com/freeiptv').request()  
    url = url.split('name="content1"', 1)[-1]
    url = url.split('name="content3"', 1)[0]
    e = re.findall('href="([^"]*)', url)
    e = [i for i in e if 'username=' in i]
    
    return e[:8]

def STB_link3():
    oGui = cGui()
    import parsers
    oInputParameterHandler = cInputParameterHandler()
#  Urrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
          
    Urrl ='http://iptvhit.com/freeiptv'                         
    sHtmlContent = getHtml(Urrl) 
    oOutputParameterHandler = cOutputParameterHandler()
    time  = datetime.now().strftime('%d/%m/%Y')
    Lin  = 'http://iptvhit.com/freeiptv'
    oOutputParameterHandler.addParameter('siteUrl', Lin)
    oGui.addDir(SITE_IDENTIFIER,'find_lpanel2', time,  'turkey-free-iptv.png', oOutputParameterHandler)
   
    sPattern = "<a href='(.*?)/(.*?)/(.*?)'"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            
            
            logger.info("STB_EMU STB_EMU_Urll: %s" % time )
            Link  = 'http://iptvhit.com/freeiptv'+  aEntry[0]+'/'+aEntry[1]+'/'+ aEntry[2]
            sTitle = aEntry[0]+'/'+aEntry[1]+'/'+ aEntry[2]
            #Link = aEntry[0]
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addDir(SITE_IDENTIFIER, 'find_lpanel2', sTitle, 'turkey-free-iptv.png', oOutputParameterHandler)
  
    oGui.setEndOfDirectory()          
def find_lpanel2():
    oGui = cGui()
    import parsers                           
    oInputParameterHandler = cInputParameterHandler()
    Urrl = oInputParameterHandler.getValue('siteUrl')
    logger.info("STB_EMU STB_EMU_Urll: %s" % Urrl )
#    cookie = getUrl(Url, output='cookie').result
    data3 = getHtml(Urrl)       
    data3=data3.replace('|','"')
    logger.info("STB_EMU STB_EMU_Urll: %s" % data3 )
    regex = re.compile('color:white">(.*?)</a> " (.*?) " (.*?) "', re.MULTILINE | re.DOTALL).findall(data3)
    for Url,sTitle,itle in regex:
                                   
        sTitle =sTitle+'|'+ itle
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'find_lpanel', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()  


def find_lpanel():#affiche les genres
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl=sUrl.replace('get.php','panel_api.php')
    logger.info("==text_pattern: %s" %  sUrl)
    sHtmlContent=getHtml(sUrl) 
    logger.info("==text_pattern: %s" %  sHtmlContent)
    aJson = json.loads(sHtmlContent)
    for cat in aJson['categories']:
        if 'live' in  cat:    
           sTitle = 'LIVE CHANNEL'
           Url = 'live'
           stream = 'ts'
        if 'series' in  cat:
           sTitle ='SERIES'
           Url ='series' 
           stream = 'm3u8'
        if 'movie' in  cat:
            sTitle ='MOVIE'
            Url ='movie'
            stream = 'm3u8'
        if 'radio' in  cat:
            sTitle ='RADIO'
            Url ='radio'
            stream = 'ts'
          #Link= cat['username']
                                    
          #sTitle = cat['password']                      
        #find_elpanel(sHtmlContent,Url)
        logger.info("==live_lpanel: %s" %  sTitle) 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sitem', sUrl)
        oOutputParameterHandler.addParameter('stream', stream)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'find_elpanel', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()


def find_elpanel():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    cid = oInputParameterHandler.getValue('siteUrl')
    ssUrl = oInputParameterHandler.getValue('sitem')
    stream = oInputParameterHandler.getValue('stream')
   

#    ssUrl=ssUrl.replace('get.php','panel_api.php')
    
  
    sHtmlContent=getHtml(ssUrl) 
    aJson = json.loads(sHtmlContent)
    for cat in aJson['categories'][''+cid]:
          Link= cat['category_id']
     
          sTitle = cat['category_name']
          #sTitle = malfabekodla(sTitle)
          #live_nlpanel(sHtmlContent,Link)
          oOutputParameterHandler = cOutputParameterHandler()
          oOutputParameterHandler.addParameter('siteUrl', Link)
          oOutputParameterHandler.addParameter('sitem', ssUrl)
          oOutputParameterHandler.addParameter('stream', stream)
          oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
          oGui.addDir(SITE_IDENTIFIER, 'live_nlpanel', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory() 


         
def live_nlpanel():
    oGui = cGui()         
   
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    cid = oInputParameterHandler.getValue('siteUrl')
    ssUrl = oInputParameterHandler.getValue('sitem')
    stream = oInputParameterHandler.getValue('stream')
    sHtmlContent=getHtml(ssUrl) 
    sHtmlContent =sHtmlContent.replace('"container_extension":""','"container_extension":null,')
    Json =sHtmlContent                   
    aJson = json.loads(Json)
    panel =aJson['user_info']                                      
    pan =aJson['server_info']
    username= panel['username']
    password= panel['password']
    url= pan['url']
    port= pan['port']                
    https_port= pan['https_port']
    logger.info("sTitle: %s" % sTitle)                              
    Jsonn= aJson['available_channels']
    Jsonn =str(Jsonn)[1:].strip("'<>() ").replace('\'', '\"').replace('\0', '')
    
    sPattern  = '\{(.*?)\}'                    
    oParser = cParser()
    aResult = oParser.parse(Jsonn, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
          if  '"category_id": "%s"' %(cid) in aEntry:
         
          #Pars1 = json.dumps(Pars)
         # Pars2 = json.loads(Pars1)
             logger.info("_aEntry: %s" % aEntry)
             title = re.findall('"name": "(.*?)".*?"stream_id": "(.*?)"', aEntry, re.S)
             for sTitle, stream_id in title:
                
                
                Urll = 'http://%s:%s/live/%s/%s/%s.%s' % (url,port,username,password,stream_id,stream)
                  
            
                sTitle =  malfabekodla(sTitle)
          
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', Urll)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oGui.addDir(SITE_IDENTIFIER, 'showtv', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()                 
         


def showtv():
        oInputParameterHandler = cInputParameterHandler()

        sUrl= oInputParameterHandler.getValue('siteUrl')


        name = oInputParameterHandler.getValue('sMovieTitle')
  
    
        sUrl= sUrl+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
 
        Play_f4mProxy('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, sUrl, '')         
def Play_f4mProxy(name,url, iconimage):
    
    import streamer
    streamer.sstreamer(name,url)
                
def STB_link2():
  oGui = cGui()
  oInputParameterHandler = cInputParameterHandler()
  Urrl = oInputParameterHandler.getValue('siteUrl')
  sTitle = oInputParameterHandler.getValue('sMovieTitle')
  Title =''                           
  sHtmlContent = cRequestHandler(Urrl).request()  
  sHtmlContent =sHtmlContent.replace('00:1a:79:','00:1A:79:')#.replace('</a>','//</a>')
  s_num = 0   
  regex  = re.findall("aria-label='link to url'>(http://.+?)</a>(.*?)</div><div class=",sHtmlContent, re.S)
  for Url, biro in regex :
     rege = re.compile("00:1A:79:(\w\w):(\w\w):(\w\w)", re.MULTILINE | re.DOTALL).findall(biro)
     for  bir,iki,uc in rege:
        if not 'username' in Url:
            name ='STB_EMU_'+  Url
            sTitle ="[COLOR cyan][B]{0}[/B][/COLOR]".format(name)
            ref = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',Url)
            Urll='http://' +ref
            logger.info("STB_EMU STB_EMU_Urll: %s" % sTitle ) 
        else:
            Urlk=Url
            Title ='IPTV-m3u_'+  Urlk
            sTitle ="[COLOR ff74ff4a][B]{0}[/B][/COLOR]".format(Title).encode('utf-8')
            logger.info("PTV-m3u_: %s" %sTitle )
        mac ='00:1A:79:%s:%s:%s'%(bir,iki,uc )
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Urll)
        oOutputParameterHandler.addParameter('mac', mac)
        oGui.addDir(SITE_IDENTIFIER, 'find_lpanel', sTitle, 'genres.png', oOutputParameterHandler)
  oGui.setEndOfDirectory()
data_time = int(addon.getSetting("data_time") or "0")
cache_time = int(addon.getSetting("cache_time") or "0")

USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('profile'))
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
channel_list_file = os.path.join(RESOURCES_DIR, 'iptvchannels.json')
#with io.open('data.json', 'w', encoding='utf8') as outfile:str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ': '), ensure_ascii=False)
#outfile.write(to_unicode(str_))




def mshowtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl= oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                             
    
     
#    sHosterUrl =  alfabekodla(sHosterUrl)
#    sHosterUrl =str(sHosterUrl)
    Header = 'User-Agent=VLC/3.0.6 LibVLC/3.0.6'
    sUrl= sUrl + '|' + Header 
    sTitle=  alfabekodla(sTitle) 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + sTitle, sUrl, '')         

def STB_EMUu():
        oGui = cGui()                
        oInputParameterHandler = cInputParameterHandler()  

        mac = oInputParameterHandler.getValue('mac')
 
 

        
        urlm = oInputParameterHandler.getValue('siteUrl')
        logger.info("STB_EMU testSTB_EMUu: %s" %urlm+mac)
        urlm =urlm.replace('/c/',"")
        urlmm =urlm.replace('http://',"").replace('https://',"")
        Url = urlm+'/server/load.php?action=handshake&type=stb&token=&mac='+ mac 
        logger.info("STB_EMU test5: %s" %Url)
        data = requests.session().get(Url, headers={'Content-Type': 'text/html',
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
        'Host': urlmm,
        'Accept': 'text/html, */*'}).text

        Authorization = re.search('"token":"(.+?)"', data).group(1)
        logger.info("STB_EMU test5: %s" %data)
        cookie = 'mac='+mac+'; stb_lang=en; timezone=Europe%2FParis;'
        cookie =cookie.replace(":","%3A")
        logger.info("STB_EMU cookie: %s" %cookie) 
        
        
         
        data = "type=account_info&action=get_main_info&mac="+ mac  
        oRequestHandler = cRequestHandler('%s/server/load.php'%urlm)
        oRequestHandler.setRequestType(1)
        oRequestHandler.addHeaderEntry('Referer', urlm+'/c/')
        oRequestHandler.addHeaderEntry('Accept', 'text/html, */*')
        oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3')
        oRequestHandler.addHeaderEntry('Content-Length', len(data))
        oRequestHandler.addHeaderEntry('Authorization', 'Bearer '+Authorization+'')
        oRequestHandler.addHeaderEntry('X-User-Agent', 'Model: MAG250; Link:')
        oRequestHandler.addHeaderEntry('Cookie', cookie)
        oRequestHandler.addParametersLine(data)
        datum = oRequestHandler.request()
        if 'phone' in datum:
           DATUM =re.search('"phone":"(.+?)"', datum).group(1) 
           logger.info("STB_EMU test5: %s" %DATUM)
          
        else: 
        
           urll = urlm+'/server/load.php?type=stb&action=get_profile'
           get_profile =STB_EMUm(urll,cookie,Authorization,urlmm)
           logger.info("STB_EMU get_profile: %s" %get_profile)
           data = "type=itv&action=get_genres&JsHttpRequest=1-xml" 
           oRequestHandler = cRequestHandler('%s/server/load.php'%urlm)
           oRequestHandler.setRequestType(1)
           oRequestHandler.addHeaderEntry('Referer', urlm+'/c/')
           oRequestHandler.addHeaderEntry('Accept', 'text/html, */*')
           oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3')
           oRequestHandler.addHeaderEntry('Content-Length', len(data))
           oRequestHandler.addHeaderEntry('Authorization', 'Bearer '+Authorization+'')
           oRequestHandler.addHeaderEntry('X-User-Agent', 'Model: MAG250; Link:')
           oRequestHandler.addHeaderEntry('Cookie', cookie)
           oRequestHandler.addParametersLine(data)
           Json = oRequestHandler.request()
        #urlamm = urlm+'/server/load.php?type=series&action=get_categories&JsHttpRequest=1-xml&mac='+ mac 
        #urlakk =STB_EMUm(urll,cookie,Authorization,urlmm)
           logger.info("STB_EMU IPTV LIVE-: %s" %Json)            
           if 'alias' in Json:
#           sJson= xload_channels.getGenres(mac, urlm, serial_number, addonDir)
              aJson = json.loads(Json)
              for cat in aJson['js']:
                 tid = cat['id']
                 sTitle = cat['title']
                 oOutputParameterHandler = cOutputParameterHandler()
                 oOutputParameterHandler.addParameter('siteUrl', tid)
                 oOutputParameterHandler.addParameter('cookie', cookie)
                 oOutputParameterHandler.addParameter('Authorization', Authorization)
                 oOutputParameterHandler.addParameter('urlmm', urlmm)
                 oOutputParameterHandler.addParameter('urlm', urlm)
                 oOutputParameterHandler.addParameter('mac', mac)
                 oGui.addLink(SITE_IDENTIFIER, 'STBEMU_bchannel', sTitle, 'STBEMU.png','', oOutputParameterHandler)
        oGui.setEndOfDirectory()

def STBEMU_bchannel():
  oGui = cGui()
  oInputParameterHandler = cInputParameterHandler()
#  sDesc = oInputParameterHandler.getValue('sDesc')
  tid = oInputParameterHandler.getValue('siteUrl')
  cookie = oInputParameterHandler.getValue('cookie')
  cookie =cookie.replace(":","%3A")
  Authorization = oInputParameterHandler.getValue('Authorization')
  urlmm = oInputParameterHandler.getValue('urlmm')
  urlm = oInputParameterHandler.getValue('urlm')
#  Urlp = 'http://scarface.network:8880/portal.php?type=itv&action=get_ordered_list&genre=%s&force_ch_link_check=&fav=0&sortby=number&hd=0&p=0&JsHttpRequest=1-xml&from_ch_id=0'%(tid)
  
      
        
  mac = oInputParameterHandler.getValue('mac')
  Urlp =xload_channels.handshake(urlm,mac)
  logger.info("STB_EMU IPTV LIVE-: %s" %Urlp)
  primler = [0,1,2,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19]
  for urg in primler: 
    data = "type=itv&action=get_ordered_list&genre=%s&force_ch_link_check=&fav=0&sortby=number&hd=0&p=0&JsHttpRequest=1-xml&from_ch_id=0"%(tid)

    oRequestHandler = cRequestHandler('%s/server/load.php'%urlm)
    oRequestHandler.setRequestType(1)
    oRequestHandler.addHeaderEntry('Referer', urlm+'/c/')
    oRequestHandler.addHeaderEntry('Accept', 'text/html, */*')
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3')
    oRequestHandler.addHeaderEntry('Content-Length', len(data))
    oRequestHandler.addHeaderEntry('Authorization', 'Bearer '+Authorization+'')
    oRequestHandler.addHeaderEntry('X-User-Agent', 'Model: MAG250; Link:')
    oRequestHandler.addHeaderEntry('Cookie', cookie)
    oRequestHandler.addParametersLine(data)
    Json = oRequestHandler.request()
    logger.info("STB_EMU IPTV LIVE-: %s" %Json)   
    if 'data' in Json:
    
      aJson = json.loads(Json)
      for cat in aJson['js']['data']:
        catid = cat['id']
        sTitle = cat['name']
        sPicture = cat['logo']+'|User-Agent=Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6'
        cmd = cat['cmd']
        cat= urlm+'/portal.php?type=itv&action=create_link&cmd='+cmd+'&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', cat)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('cookie', cookie)
        oOutputParameterHandler.addParameter('Authorization', Authorization)
        oOutputParameterHandler.addParameter('urlmm', urlmm)
        oOutputParameterHandler.addParameter('urlm', urlm)
        oOutputParameterHandler.addParameter('mac', mac)
        oGui.addMovie(SITE_IDENTIFIER, 'STBEMU_play', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

  oGui.setEndOfDirectory()

        
                    
        

def pasSTB_EMU():
  oGui = cGui()
  oInputParameterHandler = cInputParameterHandler()  
  urlm = oInputParameterHandler.getValue('siteUrl')
  ma = oInputParameterHandler.getValue('mac')
   
  macContent = cRequestHandler(ma).request()  
  rege = re.compile('00:1A:79:(\w\w):(\w\w):(\w\w)', re.MULTILINE | re.DOTALL).findall(macContent)
  for  bir,iki,uc in rege:
        
    
    mac = '00:1A:79:%s:%s:%s'%(bir,iki,uc )
    logger.info("STB_EMU STB_link2: %s" %mac)
    data=xload_channels.getGenres(mac, urlm, serial_number, addonDir)
    logger.info("STB_EMU testdata: %s" %urlm)
    for cat in data['js']:
        tid = cat['id']
        sTitle = cat['title']

        

    


	#logger.info("STB_EMU test1: %s" %id)        
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',urlm )
        oOutputParameterHandler.addParameter('sit', tid)
        oOutputParameterHandler.addParameter('mac', mac )
 
        oGui.addDir(SITE_IDENTIFIER, 'pasSTBEMU_channel', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
                    
def pasSTBEMU_channel():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    mac = oInputParameterHandler.getValue('mac')
    did = oInputParameterHandler.getValue('sit')
    urlm = oInputParameterHandler.getValue('siteUrl')
    aJson =xload_channels.getAllChannels(mac, urlm,did , addonDir)
    logger.info("STB_EMU test1_channe: %s" %aJson)  
    for cat in aJson['js']['data']:
     
        sTitle = cat['name']
        sPicture = cat['logo']+'|User-Agent=Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6'
        cmdm = cat['id']
        cmd= 'ffmpeg%20http://localhost/ch/'+ cmdm+'_' 
#              ffmpeg http : \/\/localhost\/ch\/70109_
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', urlm)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('cmd', cmd  )
        oOutputParameterHandler.addParameter('mac', mac )
        oGui.addMovie(SITE_IDENTIFIER, 'SSTBEMU_play', sTitle, sPicture, sPicture,'', oOutputParameterHandler)

 
    oGui.setEndOfDirectory()
def SSTBEMU_play():
    oInputParameterHandler = cInputParameterHandler()
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url= oInputParameterHandler.getValue('siteUrl')
    cmd = oInputParameterHandler.getValue('cmd')
    mac = oInputParameterHandler.getValue('mac')
    name = oInputParameterHandler.getValue('sMovieTitle')
    aJson= xload_channels.getPLAYER(mac, Url,cmd , addonDir)
    cat =aJson['js']
        
#    stre = cat['id']
    streams = cat['cmd'] 
    
    
    logger.info("STB_EMU test1_channe: %s" %aJson)         
#    stre = cat['id']
    
    streams = streams.replace('ffmpeg ht',"ht")+'|User-Agent=Lavf/57.73.100'
 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, streams, '')         
        
def pasSTBEMU_cmen():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    user = oInputParameterHandler.getValue('user')
    pas= oInputParameterHandler.getValue('pass')
    mac = oInputParameterHandler.getValue('mac')
    cookie = oInputParameterHandler.getValue('cookie')
    cookie =cookie.replace(":","%3A")
    Authorization = oInputParameterHandler.getValue('Authorization')
    urlmm = oInputParameterHandler.getValue('urlmm')
    urlm = oInputParameterHandler.getValue('urlm')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sJson = requests.session().get(Url, headers={'Content-Type': 'text/html',
            'Authorization': 'Bearer '+Authorization+'',
            'Cookie': cookie,
            'Host': urlmm,
            'X-User-Agent': 'Model: MAG250; Link: WiFi',
            'Accept': 'text/html, */*',
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'}).text
    aJson = json.loads(sJson)
    for cat in aJson['js']:
           tid = cat['id']
           sTitle = cat['title']
           oOutputParameterHandler = cOutputParameterHandler()
           oOutputParameterHandler.addParameter('siteUrl', tid)
           oOutputParameterHandler.addParameter('cookie', cookie)
           oOutputParameterHandler.addParameter('Authorization', Authorization)
           oOutputParameterHandler.addParameter('urlmm', urlmm)
           oOutputParameterHandler.addParameter('urlm', urlm)
           oOutputParameterHandler.addParameter('sDesc', sDesc )
           oOutputParameterHandler.addParameter('mac', mac)
           oOutputParameterHandler.addParameter('user', user)
           oOutputParameterHandler.addParameter('pass ', pas )
           oGui.addLink(SITE_IDENTIFIER, 'pasSTBEMU_channel', sTitle, 'STBEMU.png', sDesc, oOutputParameterHandler)
    oGui.setEndOfDirectory()







               
def OPEN_URL(url):
	headers = {}
	headers['User-Agent'] = 'TheWizardIsHere'
	link = requests.session().get(url, headers=headers, verify=False).text
	link = link.encode('ascii', 'ignore')
	return link




def mpasSTBEMU_channel():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    user = oInputParameterHandler.getValue('user')
    pas= oInputParameterHandler.getValue('pass')
    mac = oInputParameterHandler.getValue('mac')
    sDesc = oInputParameterHandler.getValue('sDesc')
    tid = oInputParameterHandler.getValue('siteUrl')
    cookie = oInputParameterHandler.getValue('cookie')
    cookie =cookie.replace(":","%3A")
    Authorization = oInputParameterHandler.getValue('Authorization')
    urlmm = oInputParameterHandler.getValue('urlmm')
    urlm = oInputParameterHandler.getValue('urlm')
    portal = oInputParameterHandler.getValue('urlm')
    urlam = urlm+'/portal.php?type=account_info&action=get_main_info&mac='+ mac 
    oOutputParameterHandler = cOutputParameterHandler()
    
    urlak =xload_channels.getAllChannels(mac, urlm, serial_number, addonDir)
    logger.info("STB_EMU test1: %s" %urlak)
    
    Url =STB_EMUm(sUrl,cookie,Authorization,urlmm)
    logger.info("STB_EMU testyeni: %s" %Url) 
    oGui.setEndOfDirectory()


def STB_EMUm(url,cookie,Authorization,urlmm):
#        cookie =str(cookie).replace(':',"%3A")
        data2 = requests.session().get(url, headers={'Content-Type': 'text/html',
            'Authorization': 'Bearer '+Authorization+'',
            'Cookie': cookie,
            'Host': urlmm,
            'X-User-Agent': 'Model: MAG250; Link: WiFi',
            'Accept': 'text/html, */*',
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'}).text
        
        
        return  data2

def STB_EMUM(urlm,mac):
        oGui = cGui()
        
        mac=tr_buyuk(mac)
        urlm =urlm.replace('/c/',"")
        urlmm =urlm.replace('http://',"").replace('https://',"")
       
        Url = urlm+'/portal.php?action=handshake&type=stb&token=&mac='+ mac 
        
        logger.info("STB_EMU test5: %s" %Url)
       
        data = requests.session().get(Url, headers={'Content-Type': 'text/html',
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
        'Host': urlmm,
        'Accept': 'text/html, */*'}).text
        if not 'token' in data:
            line7 = 'STB EMU link not working .....Calismiyor'
            line8 = 'Yours truly-Saygilarimla'
            xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)

        Authorization = re.search('"token":"(.+?)"', data).group(1)
         
#           oRequest = cRequestHandler(sUrl)
#        oRequest.setRequestType(1)
#    oRequest.addHeaderEntry('Accept', 'text/html, */*')
#    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3')
#    oRequest.addHeaderEntry('Authorization', 'Bearer AF7EA92BBF25534B97CFB69E6F78605E')
    
#    oRequest.addHeaderEntry('Cookie', 'mac=00%3A1a%3A79%3AB4%3AF1%3A7E; stb_lang=en; timezone=Europe%2FParis;')
#    oRequest.addHeaderEntry('Host', 'client-urostream.club:8080')
    
   
#    oRequest.addHeaderEntry('X-User-Agent', 'Model: MAG250; Link:')
#    oRequest.addHeaderEntry('Content-Type', 'text/html')         
                                
 #   tent = oRequest.request()
#    logger.info("STB_EMU test5: %s" %tent)    

        cookie = 'mac='+urlcuk+'; stb_lang=en; timezone=Europe%2FParis;'
        
        logger.info("STB_EMU cookie: %s" %cookie) 
 
        urll = urlm+'/portal.php?type=stb&action=get_profile'
        urlakk =STB_EMUm(urll,cookie,Authorization,urlmm)
       
        urlaa = urlm+'/portal.php?type=itv&action=get_genres&JsHttpRequest=1-xml' 
        
        
        urlamm = urlm+'/portal.php?type=vod&action=get_categories&JsHttpRequest=1-xml&mac='+ mac 
        
        
        urlamm = urlm+'/portal.php?type=series&action=get_categories&JsHttpRequest=1-xml&mac='+ mac 
        
        
        logger.info("STB_EMU urlakk: %s" %urlakk)            
                       
        urlam = urlm+'/portal.php?type=account_info&action=get_main_info&mac='+ mac 
        urlak =STB_EMUm(urlam,cookie,Authorization,urlmm)
        if not 'phone' in urlak:
            line7 = 'STB EMU LINK Out of Date .Calismiyor Tarihi gecmis'
            line8 = 'Yours truly-Saygilarimla'
            xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)

        sYear = 'Account Expriy Date :                           :'+re.search('"phone":"(.+?)"', urlak).group(1)
        

#        info("STB_EMU urlaka: %s" %urlaka)
       
#        info("STB_EMU urlakak: %s" %urlakak)
        
#        info("STB_EMU urlakaka: %s" %urlakaka)
                                    
        sDesc = ('[COLOR teal]%s[/COLOR]') % ( sYear)
        liste = []
        liste.append( ['IPTV LIVE',urlaa] ) 
        liste.append( ['IPTV VOD',urlamm] ) 

        liste.append( ['IPTV series',urlamm] )
        for sTitle,sUrl2 in liste:
           oOutputParameterHandler = cOutputParameterHandler()
           oOutputParameterHandler.addParameter('siteUrl', sUrl2)
           oOutputParameterHandler.addParameter('cookie', cookie)
           oOutputParameterHandler.addParameter('Authorization', Authorization)
           oOutputParameterHandler.addParameter('urlmm', urlmm)
           oOutputParameterHandler.addParameter('urlm', urlm)
           oOutputParameterHandler.addParameter('sDesc', sDesc )
           oGui.addLink(SITE_IDENTIFIER, 'STBEMU_cmen', sTitle, 'STBEMU.png', sDesc, oOutputParameterHandler)
        
                    
        oGui.setEndOfDirectory()



def STB_EMU():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()  
        urlm = oInputParameterHandler.getValue('siteUrl')
        mac = oInputParameterHandler.getValue('mac')
        
        urlm =urlm.replace('/c/',"")
        urlmm =urlm.replace('http://',"").replace('https://',"")
        Url = urlm+'/portal.php?action=handshake&type=stb&token=&mac='+ mac 
        logger.info("STB_EMU test5: %s" %Url)
        data = requests.session().get(Url, headers={'Content-Type': 'text/html',
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
        'Host': urlmm,
        'Accept': 'text/html, */*'}).text
        if not 'token' in data:
            line7 = 'STB EMU LINK Out of Date .Calismiyor Tarihi gecmis'
            line8 = 'Yours truly-Saygilarimla'
            xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)
        Authorization = re.search('"token":"(.+?)"', data).group(1)
        
        cookie = 'mac='+mac+'; stb_lang=en; timezone=Europe%2FParis;'
        cookie =cookie.replace(":","%3A")
        logger.info("STB_EMU cookie: %s" %cookie) 
        urll = urlm+'/portal.php?type=stb&action=get_profile'
        urlaa = urlm+'/portal.php?type=itv&action=get_genres&JsHttpRequest=1-xml' 
        urlamm = urlm+'/portal.php?type=series&action=get_categories&JsHttpRequest=1-xml&mac='+ mac 
        urlakk =STB_EMUm(urll,cookie,Authorization,urlmm)
        logger.info("STB_EMU urlakk: %s" %urlakk)            
        liste = []
        liste.append( ['IPTV LIVE',urlaa] ) 
        liste.append( ['IPTV VOD',urlamm] ) 

        liste.append( ['IPTV series',urlamm] )
        for sTitle,sUrl2 in liste:
           urlam = urlm+'/portal.php?type=account_info&action=get_main_info&mac='+ mac 
           urlak =STB_EMUm(urlam,cookie,Authorization,urlmm)
           if not 'phone' in urlak:
              line7 = 'STB EMU LINK Out of Date .Calismiyor Tarihi gecmis'
              line8 = 'Yours truly-Saygilarimla'
              xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)

           sYear = 'Account Expriy Date :                           :'+re.search('"phone":"(.+?)"', urlak).group(1)
           logger.info("STB_EMU test1: %s" %urlak)
           sDesc = ('[COLOR teal]%s[/COLOR]') % ( sYear) 
           oOutputParameterHandler = cOutputParameterHandler()
           oOutputParameterHandler.addParameter('siteUrl', sUrl2)
           oOutputParameterHandler.addParameter('cookie', cookie)
           oOutputParameterHandler.addParameter('Authorization', Authorization)
           oOutputParameterHandler.addParameter('urlmm', urlmm)
           oOutputParameterHandler.addParameter('urlm', urlm)
           oOutputParameterHandler.addParameter('sDesc', sDesc )
           oGui.addLink(SITE_IDENTIFIER, 'STBEMU_cmen', sTitle, 'STBEMU.png', sDesc, oOutputParameterHandler)
        
                    
        oGui.setEndOfDirectory()
def STBEMU_cmen():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    cookie = oInputParameterHandler.getValue('cookie')
    cookie =cookie.replace(":","%3A")
    Authorization = oInputParameterHandler.getValue('Authorization')
    urlmm = oInputParameterHandler.getValue('urlmm')
    urlm = oInputParameterHandler.getValue('urlm')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sJson = requests.session().get(Url, headers={'Content-Type': 'text/html',
            'Authorization': 'Bearer '+Authorization+'',
            'Cookie': cookie,
            'Host': urlmm,
            'X-User-Agent': 'Model: MAG250; Link: WiFi',
            'Accept': 'text/html, */*',
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'}).text
    aJson = json.loads(sJson)
    for cat in aJson['js']:
           tid = cat['id']
           sTitle = cat['title']
           oOutputParameterHandler = cOutputParameterHandler()
           oOutputParameterHandler.addParameter('siteUrl', tid)
           oOutputParameterHandler.addParameter('cookie', cookie)
           oOutputParameterHandler.addParameter('Authorization', Authorization)
           oOutputParameterHandler.addParameter('urlmm', urlmm)
           oOutputParameterHandler.addParameter('urlm', urlm)
           oOutputParameterHandler.addParameter('sDesc', sDesc )
           oGui.addLink(SITE_IDENTIFIER, 'STBEMU_channel', sTitle, 'STBEMU.png', sDesc, oOutputParameterHandler)
    oGui.setEndOfDirectory()









def STBEMU_channel():
  oGui = cGui()
  oInputParameterHandler = cInputParameterHandler()
  sDesc = oInputParameterHandler.getValue('sDesc')
  tid = oInputParameterHandler.getValue('siteUrl')
  cookie = oInputParameterHandler.getValue('cookie')
  cookie =cookie.replace(":","%3A")
  Authorization = oInputParameterHandler.getValue('Authorization')
  urlmm = oInputParameterHandler.getValue('urlmm')
  urlm = oInputParameterHandler.getValue('urlm')
  Urlp = 'http://scarface.network:8880/portal.php?type=itv&action=get_ordered_list&genre=%s&force_ch_link_check=&fav=0&sortby=number&hd=0&p=0&JsHttpRequest=1-xml&from_ch_id=0'%(tid)
  urlavl =STB_EMUm(Urlp,cookie,Authorization,urlmm)
        
        
  
  logger.info("STB_EMU urlavl: %s" %urlavl)  
  primler = [0,1,2,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19]
  for urg in primler: 
    Url = 'http://scarface.network:8880/portal.php?type=itv&action=get_ordered_list&genre=%s&force_ch_link_check=&fav=0&sortby=number&hd=0&p=%s&JsHttpRequest=1-xml&from_ch_id=0'%(tid,urg)
    sJson = requests.session().get(Url, headers={'Content-Type': 'text/html',
            'Authorization': 'Bearer '+Authorization+'',
            'Cookie': cookie,
            'Host': urlmm,
            'X-User-Agent': 'Model: MAG250; Link:',
            'Accept': 'text/html, */*',
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'}).text
    if not 'total_items' in sJson:
          line7 = re.search('<title>(.+?)</title>', sJson).group(1)
          line8 = 'Yours truly-Saygilarimla'
          xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)

    aJson = json.loads(sJson)
    for cat in aJson['js']['data']:
        catid = cat['id']
        sTitle = cat['name']
        sPicture = cat['logo']+'|User-Agent=Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6'
        cmd = cat['cmd']
        cat= urlm+'/portal.php?type=itv&action=create_link&cmd='+cmd+'&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', cat)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('cookie', cookie)
        oOutputParameterHandler.addParameter('Authorization', Authorization)
        oOutputParameterHandler.addParameter('urlmm', urlmm)
        oOutputParameterHandler.addParameter('urlm', urlm)
        oGui.addMovie(SITE_IDENTIFIER, 'STBEMU_play', sTitle, sPicture, sPicture, sDesc, oOutputParameterHandler)

  oGui.setEndOfDirectory()


def STBEMU_play():
    oInputParameterHandler = cInputParameterHandler()
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url= oInputParameterHandler.getValue('siteUrl')
    cookie = oInputParameterHandler.getValue('cookie')
    cookie =cookie.replace(":","%3A")
    Authorization = oInputParameterHandler.getValue('Authorization')
    urlmm = oInputParameterHandler.getValue('urlmm')
    urlm = oInputParameterHandler.getValue('urlm')
    mac = oInputParameterHandler.getValue('mac')
    Urlp =xload_channels.handshake(urlm,mac)
    logger.info("STB_EMU IPTV LIVE-: %s" %Urlp)
    sJson = requests.session().get(Url, headers={'Cookie': cookie,
           'Content-Type': 'text/html',
           'Authorization': 'Bearer '+Authorization+'',
           'Cookie': cookie,
           'X-User-Agent': 'Model: MAG250; Link:',
           'Host': urlmm,
           'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'}).text
    aJson = json.loads(sJson)
    cat =aJson['js']
        
    stre = cat['id']
    streams = cat['cmd'] 
    streams = streams.replace('ffmpeg ht',"ht")+'|User-Agent=Lavf/57.73.100'
 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, streams, '')         
def MSTBEMU_play():
    oInputParameterHandler = cInputParameterHandler()
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url= oInputParameterHandler.getValue('sThumbnail')
    cookie = oInputParameterHandler.getValue('cookie')
    iconimage=oInputParameterHandler.getValue('cookie')
    Authorization = oInputParameterHandler.getValue('Authorization')
    urlmm = oInputParameterHandler.getValue('urlmm')
    urlm = oInputParameterHandler.getValue('urlm')
    sJson = requests.session().get(Url, headers={'Cookie': cookie,
           'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
           'Host': urlmm,
           'Authorization': 'Bearer '+Authorization+''}).text
    streams = re.search('"cmd":"ffmpeg (.+?)"', sJson).group(1)

    url = streams.replace('\/', '/')+'|User-Agent=Lavf/57.73.100'
 
    maxbitrate = Addon.getSetting('BitRateMax')
    if Addon.getSetting('use_simple') == "true":
        simpledownloader = True
    else:
        simpledownloader = False
    sys.path.insert(0, f4mProxy)
    from F4mProxy import f4mProxyHelper
    player=f4mProxyHelper()
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
    
    if streamtype == "HLS":
        maxbitrate = 9000000
    start_proxy(url, name, None, True, maxbitrate, simpledownloader, None, streamtype, False, None, None, None, iconimage)    
    sys.exit()
    return ok 
                
                      
def iptvturkeme(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl=oInputParameterHandler.getValue('siteUrl')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    
    sHtmlContent =sHtmlContent.replace('\n',"").replace('#','"').replace('&','"')
    
    sPattern = '<ul class="list-group list-group-flush display-3">(.+?)</div>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    
    sPattern = '<a href=".+?stream=([A-z0-9]+)".*?<i class="fas fa-futbol"></i></span>(.*?)<b>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        
        for aEntry in aResult[1]:
            
            Link = aEntry[0]
             
            sTitle=  aEntry[1]                                                                     
           
#            sTitle = sTitle.replace('\n',"").replace('u015a',"S").replace('u0105',"a").replace('u0119',"e").replace('u017c',"z")
                                        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'selcuksport', sTitle, 'genres.png', oOutputParameterHandler)
        

    oGui.setEndOfDirectory() 

def selcuksport():
    oInputParameterHandler = cInputParameterHandler()
    name = oInputParameterHandler.getValue('sMovieTitle')
    Link = oInputParameterHandler.getValue('siteUrl')
    
 #   if  'index.php' in   Link:
         
#         id = re.search('.+?id=(.+?)|#|&', Link).group(1)
         
#         streams = 'https://v.xx.strmrdrcdn.net/lvideo-ist1-prn/_nc_cat-601/'+id+'/manifest.m3u8'   
    
    #      streams = 'https://srvbbbb.beyazrenk.xyz/kaynakstreamradarco/selcukbein1/naxi/caxi.m3u8'
#    streams = 'https://srvbbbb.beyazrenk.xyz/kaynakstreamradarco/'+Link+'/naxi/caxi.m3u8'
#    streams = 'https://srvb.yazgeldigidelim.xyz/kaynakstreamradarco/'+Link+'/strmrdr.m3u8'
    streams = 'http://stream99.astalavistababy.xyz/selcuksportssinema/'+Link+'/playlist.m3u8'   

    streams = streams+'|User-Agent=Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6&Referer=https://s7.slcksprtsbot.com/selcuk1.html?sdf3dsssfdsfdg2345236as'
 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, streams, '')
  
             
            
              
             
                             
def iptvturkem(): #affiche les genres
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl='https://www.unacanita.com'
    sHtmlContent=getHtml(sUrl)
    sHtmlContent = sHtmlContent.replace(' target','target')                                                     
    sPattern = '<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td><a href=/canal/(.*?)target="_blank"> <span>(.*?)</span></a></td>.*?</tr>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            tarih=  aEntry[0] 
            saat = aEntry[1]
            turu= aEntry[2]
            ulke=  aEntry[3]                                                                     
            canal=  aEntry[5]
            Link=  aEntry[4]
            canal= '[COLOR lightblue][B]%s[/B][/COLOR]'%(canal) 
            saat= '[COLOR red][B]%s[/B][/COLOR]'%(saat) 
            sTitle =tarih+' '+saat+' '+turu+'-'+ulke+'(%s)'%canal                                     
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'freestreams2', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
      
def GetRealUrl(sUrl): 
    chain  =getHtml(sUrl)
    r = re.search('<video.+?src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('items=Array."(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search("=.+?'(http.+?.m3u8)'", chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('=.+?"(http.+?.m3u8)"', chain)
    if (r):
        url = r.group(1)
        return url
 
                
def freestreams3():
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    if 'futbolcafe' in Url:
          streams=GetRealUrl(Url)
          streams = streams+'|User-Agent=Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6&Referer=http://www.futbolcafe118.xyz/'
          addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, streams, '')  
    if 'sportbar' in Url:
        data6=getHtml(Url)
        streams = re.search("videoLink = '(.*?)'", data6).group(1)
        streams = streams+'|User-Agent=Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6&Referer=http://www.futbolcafe118.xyz/'
        logger.info("futbolcafe: %s" %data6)
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, streams, '')  
def freestreams4():
            oInputParameterHandler = cInputParameterHandler()
            Url = oInputParameterHandler.getValue('siteUrl')
            logger.info("cookie data4: %s" %Url)
            name = oInputParameterHandler.getValue('sMovieTitle')

            Url2 ='https://poscitech.club/tv/ch%s.php' %(Url)
            sHtmlContent=getHtml(Url)
            Url4 = re.search('<iframe src="(.+?)"', sHtmlContent).group(1)
            referer=[('Referer',Url2)]
            sHtmlContent=gegetUrl(Url4,headers=referer) 
            #logger.info("cookie data2: %s" % Content)
            oParser = cParser()
            sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
            aResult = oParser.parse(sHtmlContent, sPattern)

            if (aResult[0] == True):
                  data1= cPacker().unpack(aResult[1][0])                    
                 
                  
                     # data1=data1.replace('\n',"").replace('\t',"")
                  logger.info("cookie data1: %s" %data1)
                  U = re.search('source:"(.+?)"', data1).group(1)
                     # logger.info("U: %s" %U)
                      #tent=getHtml(data2)
                  
                     # logger.info("Url: %s" %tent)
                  addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')

   

                                                     
def freestreams2():
            oInputParameterHandler = cInputParameterHandler()
            Url = oInputParameterHandler.getValue('siteUrl')
            name = oInputParameterHandler.getValue('sMovieTitle')
            Url3 ='https://poscitech.club/'
            Url2 ='https://poscitech.club/tv/ch%s.php' %(Url)
            ssHtmlContent=getHtml(Url2)
            Url4 = re.search('<iframe src="(.+?)"', ssHtmlContent).group(1)
            referer=[('Referer',Url3)]
            sHtmlContent=gegetUrl(Url4,headers=referer) 
            logger.info("sHtmlConten: %s" % sHtmlContent)
            if 'source' in   sHtmlContent:
               U = re.search('source     : "(.+?)"', sHtmlContent).group(1)
               U = U+'|Referer=https://wigistream.to/'
               addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
            #
            else:
               oParser = cParser()
               sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
               aResult = oParser.parse(sHtmlContent, sPattern)

               if (aResult[0] == True):
                  data1= cPacker().unpack(aResult[1][0])                    
                 
                  
                     # data1=data1.replace('\n',"").replace('\t',"")
                  logger.info("cookie data1: %s" %data1)
                  U = re.search('source:"(.+?)"', data1).group(1)
                     # logger.info("U: %s" %U)
                      #tent=getHtml(data2)
                  
                     # logger.info("Url: %s" %tent)
                  U = U+'|Referer=https://wigistream.to/'
                  addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')



def dailymotion(sUrl):                                  
        api_call = False
        url=[]
        qua=[]
        if not 'http' in sUrl:
           sUrl='http:'+ sUrl.replace('@60', '')
        
        
        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0')
        oRequest.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
        oRequest.addHeaderEntry('Cookie', "ff=off")
        sHtmlContent = oRequest.request()


        oParser = cParser()

        sPattern =  '{"type":"application.+?mpegURL","url":"([^"]+)"}'
        aResult = oParser.parse(sHtmlContent, sPattern)

        if (aResult[0] == True):
            oRequest = cRequestHandler(aResult[1][0])
            oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0')
            oRequest.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
            sHtmlContent = oRequest.request()

            sPattern = 'NAME="([^"]+)"(,PROGRESSIVE-URI="([^"]+)"|http(.+?)\#)'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if (aResult[0] == True):
                for aEntry in reversed(aResult[1]):
                    quality = aEntry[0].replace('@60', '')
                    if quality not in qua:
                        qua.append(quality)
                        link = aEntry[2] if aEntry[2]  else 'http' + aEntry[3]
                        url.append(link)

            name_call = dialog().VSselectqual(url,qua)
            api_call = dialog().VSselectqual(qua, url)
            logger.info("api_call: %s" %name_call)
            item = 'sMovieTitle'
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name_call,api_call, '')


       



def bmmoklivecams():
    oRequest = cRequestHandler(Url4)
    oRequest.addHeaderEntry('Cookie', 'cvn1=CwaAAAAAAhQBCgACZh0GAQM%3D;')
    oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
#    oRequest.addHeaderEntry('Accept-Encoding', 'gzip, deflate, br')
    oRequest.addHeaderEntry('Referer', 'https://wigistream.to/')
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    oRequest.addHeaderEntry('Sec-Fetch-Dest', 'iframe')
    oRequest.addHeaderEntry('Sec-Fetch-Mode', 'navigate')
    oRequest.addHeaderEntry('Sec-Fetch-Site', 'cross-site')
    oRequest.addHeaderEntry('Upgrade-Insecure-Requests', '1')
    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')
    sHtmlContent = oRequest.request()    
#    sHtmlContent = oRequest.request()
    oParser = cParser()
    sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        data1= cPacker().unpack(aResult[1][0])                    
        #info("cookie data2: %s" %cookie)
#        info("cookie data3: %s" %the_page_html)
        logger.info("cookie data4: %s" %data1)
#    data1 = data1.replace('|', 'Host')
#    auti = re.search('Host(0680740740.+?)Host', data1).group(1)
#    url = oklidecode(auti).decode('hex')
#    VSlog('Good cookie :' + url)
#    TIK = '|Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9&Host=ls2.livex.to&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    
    
#    


def bmmoklivecams():
      
#      streams = 'https://srvbbbb.beyazrenk.xyz/kaynakstreamradarco/selcukbein1/naxi/caxi.m3u8'
      streams = 'https://srvb.yazgeldigidelim.xyz/kaynakstreamradarco/19/naxi/caxi.m3u8'
      #x ='КиноСезон' 
    
    
      
      streams = streams+'|User-Agent=Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6&Referer=https://s7.slcksprtsbot.com/selcuk1.html?sdf3dsssfdsfdg2345236as'
    
      item = 'Sh'
      addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + item, streams , '')

def tv8canli():

    url ='plugin://script.module.realtv'
    if not url.startswith("plugin://plugin") or not any(x in url for x in g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
        setres=True
        if '$$LSDirect$$' in url:
            url=url.replace('$$LSDirect$$','')
            setres=False
        item = xbmcgui.ListItem(path=url)
        if not setres:
            xbmc.Player().play(url)
        else: 
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
#        print 'Not setting setResolvedUrl'
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')



def miptvturke():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    referer=[('Referer',sUrl)]
    date = gegetUrl(sUrl,headers=referer)
    channels = re.findall("aria-label='link to url'>(https://m3u-editor.com/serve/.*?)</a>",date, re.S)
    for Link in channels:         
       
                                
#       for sTitle in channel:                           
              #sTitle = re.findall('https://m3u-editor.com/serve/(.*?)',Link, re.S)                 
              sTitle =malfabekodla(Link.replace('https://m3u-editor.com/serve/','').replace('telegrampaylasmakguzeldir-','')) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'turkom3', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()
def iptvturke(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl='https://telemetr.io/en/channels/1301958959-paylasmakguzeldirdepo/posts'
    referer=[('Referer',sUrl)]
    sHtmlContent = gegetUrl(sUrl,headers=referer)
   
    sPattern = "aria-label='link to url'>(http://provid.kolpax.de.*?)</a>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        
        for aEntry in aResult[1]:
            sPicture = str(aEntry[2])
            
            Link = aEntry[0]
            sTitle=  aEntry[0]                                                                     
           
#            sTitle = sTitle.replace('\n',"").replace('u015a',"S").replace('u0105',"a").replace('u0119',"e").replace('u017c',"z")
                                        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'play__weebtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory() 
def turkom3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    import re

    referer=[('Referer',url)]
    open = gegetUrl(url,headers=referer)
    logger.info("==text_pattern: %s" %   open)
    regex = re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n', re.MULTILINE | re.DOTALL).findall(open)
    for sTitle, Url in regex:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'ssourcetvm3u', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def turkom2m():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    import re

    referer=[('Referer',url)]
    open = gegetUrl(url,headers=referer)
    regex = re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n', re.MULTILINE | re.DOTALL).findall(open)
    for sTitle, Url in regex:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'iptvturke2', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def iptvturke2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Urll=oInputParameterHandler.getValue('siteUrl')
    name=oInputParameterHandler.getValue('sMovieTitle')
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,Urll, '')

 
#    VSlog(Urll)
#    name = 'hOynat'
#    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,Urll, '')


def TSpanel():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    MAIN = oInputParameterHandler.getValue('siteUrl')                  
    liste = []                
    
    liste.append( ['FULL YERLI LINK',URL_WEB] )
    liste.append( ['IPTV ',MAIN] )
    

               
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
      
        if sTitle == 'Panele Gir':
             oGui.addDir(SITE_IDENTIFIER, 'user_info',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'FULL YERLI LINK':
             oGui.addDir(SITE_IDENTIFIER, 'iptvturke',  sTitle, 'genres.png', oOutputParameterHandler)
       
        else:
             oGui.addDir(SITE_IDENTIFIER, 'ssourcetvm3u',  sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def ssourcetvm3u():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    import re

    referer=[('Referer',url)]
    open = gegetUrl(url,headers=referer) 
    regex = re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n', re.MULTILINE | re.DOTALL).findall(open)
    for sTitle, Url in regex:
        #Url= Url+'?token=HRoLBEZYRwhEVlMFCwQHAgQCVABXVA9RUwVXAQ5QBlJTAAFQUVIAC1MWHhRBQBNVAFg8DQIVAlQEBRgWTUdUETlRB0cPElcCUQEKFB4WFVkMUEFeVwEJUAYPDAAOBR1BFlEHRw8SVgNSBAIUHhYESBVQEQoHW2cGUkFdV10WCw0TVA9JF18LbQJRX1dcUEMKQwRBSEReSxIVDVpBVFgdQQRRFxdURAAQXBYAAQICQxxDVgwRCENKGxUNFnB9Fh1BA0AXAFtDDF0IFggURkdDHENcEDsUUksWRVJVWV1GE1lECEFJF10ESjlXXVhcUQJECFoNF0QNGlMVGxZZV1pYFwlKPBVcVEcIRAUEBwACQ00='
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'iptvturke2', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def user_info(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    ssUrl= IPTVdep(sUrl)
    
  
    referer=[('Referer',ssUrl)]
    sHtmlContent = gegetUrl(ssUrl,headers=referer) 
               
    sPattern = '{"category_id":"(.*?)","category_name":"(.*?)","parent_id":.*?}'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        
        for aEntry in aResult[1]:
            
            
            Link = aEntry[0]
            sTitle =  alfabekodla(sTitle)
            sTitle = aEntry[1].decode("latin-1").encode("utf-8")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('ssUrl', ssUrl)
            oOutputParameterHandler.addParameter('siteUrl', Link)
           
            oGui.addDir(SITE_IDENTIFIER, 'user_info3', sTitle, 'genres.png', oOutputParameterHandler)
                   

            
            
           
        

    oGui.setEndOfDirectory() 
def muser_info3(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    ssUrl = oInputParameterHandler.getValue('ssUrl')
    
    referer=[('Referer',ssUrl)]
    data=gegetUrl(ssUrl,headers=referer) 
    sHosterUrl = re.findall('"username":"(.*?)","password":"(.*?)".*?"server_info":{"url":"(.*?)","port":"(.*?)"', data, re.S)
    (username,password,url,port) =sHosterUrl[0]

   
    

    referer=[('Referer',ssUrl)]
    sHtmlContent = gegetUrl(ssUrl,headers=referer) 
    sPattern = '"category_id":"%s"'%sUrl+',"series_no".*?"tv_archive_duration":0},"(.*?)":{"num":.*?,"name":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        
        for aEntry in aResult[1]:
            sTitle = str(aEntry[1])
            
            
              
            Urll = 'http://%s:%s/live/%s/%s/%s.ts' % (url,port,username,password,aEntry[0])
            if Urll == None:
              callback(Urll)
            
            
            sTitle =  alfabekodla(sTitle)
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Urll)
            oGui.addDir(SITE_IDENTIFIER, 'playrab', sTitle, 'genres.png', oOutputParameterHandler)
                   

            
            
           
        

    oGui.setEndOfDirectory() 



def Arapplaylive():
  
    dat = 'http://yacinelive.com/thefrh/newfrh.php?cat_id=12'
    req = urllib.request.Request(dat)
    req.add_header('token', '14c4b06b824ec593239362517f538b27')
    req.add_header('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/NRD90M)')
    req.add_header('Host', 'yacinelive.com')

    req.add_header('Cookie', 'PHPSESSID=e710uns09pqr86oe1o8r6m3ib4')
    req.add_header('Accept-Encoding', 'gzip, deflate')
    data = _get(req)
#    Auth = re.search('(.+?)', data).group(1)
    name = 'https://goo.gl/wqsVrs'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,data, '')


#onclick="Player.online(.+?, \'(.+?)\', '16/9', event, this)">
                                                 

def limehd():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
   
           
    Urrl = 'https://limehd.tv/camera-online'
    oRequestHandler = cRequestHandler(Urrl)
    sHtmlContent = oRequestHandler.request()
    #sHtmlContent =sHtmlContent.replace('&#39;',"'")
    sPattern = 'onclick="Player.online.+?, \'(.+?)\',.+?">.*?<img alt="(.+?)" class="channel-icon" src="(.+?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            sTitle =aEntry[1]
             
            sPic = aEntry[2]
            sPicture = 'https://cdn.limehd.tv/images' + sPic
            sUrl = str(aEntry[0])
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'playrab', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        
    oGui.setEndOfDirectory()
#from datetime import datetime, timedelta
#import calendar
 
                     
def playrab():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
  

    name = alfabekodla(sTitle)  
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, sUrl, '')

                               
def addLink(name, url, iconimage):
    ok = True
    
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 



#from resources.lib.download import cDownload
#import wgetter

def testPPlanetlive():
    Url = 'https://limehd.tv/camera-online'
    item = 'sMovieTitle'
    oRequest = cRequestHandler(Url)
    wmsAuth = oRequest.request()
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + item, wmsAuth, '')


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def __check_auth(url):
    try:
        js_result = json.loads(cRequestHandler(url).request())
    except ValueError:
        raise ResolverError('Unusable Authorization Response')

    if js_result.get('statusCode') == 0:
        if js_result.get('data') == 'wait-pin-validation':
            return False
        else:
            return js_result


def PPlanetlive():
    oGui = cGui()
    sJson = cRequestHandler(ddatam_url).request()
    aJson = json.loads(sJson)
    for cat in aJson['LIVETV']['category']:
        catid = cat['cid']
        sTitle = cat['category_name']
        sPic = cat['category_image']
        sPicture = 'https://app.liveplanettv.com/beta/images/' + sPic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', catid)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'Planetlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def Planetlive():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cid = oInputParameterHandler.getValue('siteUrl')
    Url = 'https://app.liveplanettv.com/beta/api.php?cat_id=' + cid + '&wmsAuthSign=' + LIVETVtoken() + '&device_id=354630080742220'
    sJson = cRequestHandler(Url).request()
    aJson = json.loads(sJson)
    for cat in aJson['LIVETV']['category_detail']:
        catid = cat['channel_url']
        sTitle = cat['channel_title']
        sPic = cat['channel_thumbnail']
        sPicture = 'https://app.liveplanettv.com/beta/images/' + sPic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', catid)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'play__rabictv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


#from diziizle_net import vodstreams

def play__rabictv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    if re.search('youtube', sUrl):
        vodstreams(sTitle, sUrl)
    sUrl = sUrl + Authtoken() + '|User-Agent=stagefright/1.2 (Linux;Android 5.1.1)'
    name = alfabekodla(sTitle)
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, sUrl, '')


def moklivecams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    item = 'sMovieTitle'
    oRequest = cRequestHandler(Url)
    wmsAuth = oRequest.request()
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + item, wmsAuth, '')

def addLink(name, url, iconimage):
    ok = True
    
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 



def oklivecams2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    oRequest = cRequestHandler(Url)
    sHtmlContent = oRequest.request()
    sPattern = '<a href="/.*?/" data-room="(.*?)">.*?<img src="(.*?)" width="180" height=".*?" alt="(.*?)" class=".*?" '
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            sPicture = aEntry[1]
            sTitle = aEntry[2]
            Link = aEntry[0]
            
            URL = 'https://www.oklivecams.com/embed/' + Link + '/?join_overlay=1&campaign=W52kq&embed_video_only=1&disable_sound=0&tour=sEAI&mobileRedirect=never'
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
    auth = cRequestHandler(liste).request()
    url = re.search("<source src='(.*?)' type='application/x-mpegURL'", auth).group(1)
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def OKliveTV():
    oGui = cGui()
    liste = []
    liste.append(['Cartoons', 'http://oklivetv.com/genre/cartoons/'])
    liste.append(['Documentary', 'http://oklivetv.com/genre/documentary/'])
    liste.append(['Entertainment', 'http://oklivetv.com/genre/entertainment/'])
    liste.append(['Movies', 'http://oklivetv.com/genre/movies/'])
    liste.append(['Music', 'http://oklivetv.com/genre/music/'])
    liste.append(['News', 'http://oklivetv.com/genre/news/'])
    liste.append(['Regional', 'http://oklivetv.com/genre/regional/'])
    liste.append(['Religious', 'http://oklivetv.com/genre/religious/'])
    liste.append(['Shows', 'http://oklivetv.com/genre/shows/'])
    liste.append(['Sports', 'http://oklivetv.com/genre/sports/'])
    for sTitle, sUrl2 in liste:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'PROGRAMLAR':
            oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLAS\xc4\xb0K D\xc4\xb0Z\xc4\xb0LER':
            oGui.addDir(SITE_IDENTIFIER, 'ArshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YEN\xc4\xb0 D\xc4\xb0Z\xc4\xb0LER':
            oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLAS\xc4\xb0K D\xc4\xb0Z\xc4\xb0LER ABC':
            oGui.addDir(SITE_IDENTIFIER, 'klasikdizizleABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ATV YEDEK':
            oGui.addDir(SITE_IDENTIFIER, 'canlitvzoneBox', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'OKliveTV2', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()



def OKliveTV2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urll = 'http://oklivetv.com/'
    cookie = getUrl(Urll, output='cookie').result
    oRequest = cRequestHandler(Url)
    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')
    oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    sHtmlContent = oRequest.request()
    sPattern = '<div class="nag cf">(.+?)<script'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a class="clip-link" data-id=".*?" title="(.*?)" href="(.*?)">.*?<img src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            sPicture = str(aEntry[2])
            sTitle = aEntry[0]
            Link = aEntry[1]
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('refsiteUrl', Url)
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'madulto', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        
        sNextPage = msEcho(str(Url + 'page/1/'))
        if sNextPage != False:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'OKliveTV2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
def msEcho(s):
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


def madulto():
       oInputParameterHandler = cInputParameterHandler()
       Url = oInputParameterHandler.getValue('siteUrl')
       refUrl = oInputParameterHandler.getValue('refsiteUrl')
       name = oInputParameterHandler.getValue('sMovieTitle')
       data3= getHtml(Url)
       Url2 ='http:'+re.search("""<iframe.+?src=["'](.+?)["']""",  data3).group(1)
       
       
       
      # Url3 ='http://oklivetv.com/'+re.search('id="tabOKLiveTV1" href="(.+?)" ', data2).group(1)
       cookie =SetCookie(Url2 )
       logger.info("cookie:" +cookie) 
                                                                                              # , timeout=10
       data1 = requests.session().get(Url2, headers={"Cookie": cookie,"Referer": Url ,"Content-Type": "application/x-www-form-urlencoded","User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',"sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',"x-requested-with": "XMLHttpRequest"}).text        
       data1=to_utf8( data1)
 
       
       data1=oklidecode(data1)
                 
       
       auti =re.search('(687474703a.+?6d337538)', data1).group(1)
       auti =okliDecode(auti)
       logger.info('oklive>%s' % auti)
       TIK='|Cookie='+cookie+'&Referer='+Url2+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' 
       baddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, auti+TIK,Url2 , '')
           
     
def baddLink(name, url,Url2 , iconimage):
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




try:
    from urllib.parse import quote as orig_quote
except ImportError:
    from urllib import quote as orig_quote

def quote(s, safe = ''):
    return orig_quote(s.encode('utf-8'), safe.encode('utf-8'))

def okliDecode(txt):
    return ''.join([chr(int(''.join(c), 16)) for c in zip(txt[0::2],txt[1::2])])

def oklidecode(data):
    data = str(data).replace('0a', 'a')
    data = str(data).replace('0b', 'b')
    data = str(data).replace('0c', 'c')
    data = str(data).replace('0d', 'd')
    data = str(data).replace('0e', 'e')
    data = str(data).replace('0f', 'f')
    data = str(data).replace('01', '1')
    data = str(data).replace('02', '2')
    data = str(data).replace('03', '3')
    data = str(data).replace('04', '4')
    data = str(data).replace('05', '5')
    data = str(data).replace('06', '6')
    data = str(data).replace('07', '7')
    data = str(data).replace('08', '8')
    data = str(data).replace('09', '9')
    return data


from resources.lib.comaddon import VSlog



def mmadulto():
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    refUrl = oInputParameterHandler.getValue('refsiteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    hosters = []
    Urll = 'http://oklivetv.com/'
    cookie = getUrl(Url, output='cookie').result
    data3 = requests.session().get(Url, headers={'Cookie': cookie,
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
     'Host': 'oklivetv.com',
     'Connection': 'Keep-Alive',
     'Accept-Encoding': 'gzip'}).text
    Url2 = 'http:' + re.search('<iframe.+?src=["\'](.+?)["\']', data3).group(1)
    oRequest = cRequestHandler(Url2)
    oRequest.addHeaderEntry('Host', 'oklivetv.com')
    oRequest.addHeaderEntry('Connection', 'keep-alive')
    oRequest.addHeaderEntry('Upgrade-Insecure-Requests', '1')
    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')
    oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    oRequest.addHeaderEntry('Referer', Url)
    oRequest.addHeaderEntry('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7')
    oRequest.addHeaderEntry('Cookie', cookie)
    oRequest.addHeaderEntry('Accept-Encoding', 'gzip, deflate')
    data1 = oRequest.request()
    data1 = data1.replace('|', 'Host')
    auti = re.search('Host(0680740740.+?)Host', data1).group(1)
    url = oklidecode(auti).decode('hex')
    VSlog('Good cookie :' + url)
    TIK = '|Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9&Host=ls2.livex.to&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url + TIK, '')


def aaddLink(title, url, iconimage):
    list_item = xbmcgui.ListItem(path=str(url))
    info = {'Title': title}
    if data['thumb']:
        list_item.setThumbnailImage(data['thumb'])
    if data['showTitle']:
        info['Episode'] = data['episode']
        info['Season'] = data['season']
        info['TVShowTitle'] = data['showTitle']
    if 'foxx' in data['link']:
        list_item.setContentLookup(False)
        list_item.setMimeType('video/mp4')
    list_item.setInfo(type='Video', infoLabels=info)
    list_item.setProperty('IsPlayable', 'true')
    url = str(url)
    xbmcplugin.setResolvedUrl(cGui().pluginHandle, True, list_item)
    xbmc.Player().play(url, list_item)
    xbmcPlayer = xbmc.Player()
    return pPlayer().startPlayer()


def getHosterUrl(sUrl = False):
    sUrl = sUrl + '|verifypeer=false&Origin=https%3A%2F%2Fhdfilme.cx%2F&Referer=https%3A%2F%2Fhdfilme.cx%2F'
    return [{'streamUrl': sUrl,
      'resolved': True}]






def unescape(html_text):
    if sys.version_info >= (3, 0):
        if sys.version_info >= (3, 4):
            return html.unescape(html_text)
        return HTMLParser().unescape(html_text)
    return HTMLParser().unescape(html_text)


def _prepare_time_and_rpc():
    millis = int(round(time.time() * 1000))
    xbmc.log('Time: %s' % millis)
    rand = random.randint(1, 99999999)
    a = '0.%s' % str(rand * 2147483647)
    rpc = int(100000000 * float(a))
    xbmc.log('Rpc-token: %s' % rpc)
    return (millis, rpc)









def adulto():
    oGui = cGui()
    url = 'https://dl.dropboxusercontent.com/s/kjadh847z4iyk0h/dizi.json'
    req = urllib.request.Request(url, None, {'User-agent': 'Mozilla/5.0 seyirTURK__KODI',
     key44: answer44,
     'Connection': 'Close'})
    r = urllib2.urlopen(req).read()
    res = json.loads(r)
    for rs in res['movies']:
        idx = str(rs['ID'])
        sTitle = rs['Name']
        sPicture = rs['Image']
        urls = rs['Link']
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', urls)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addMovie(SITE_IDENTIFIER, 'diziler', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    return


def mdiziler():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    req = urllib.request.Request(url, None, {'User-agent': 'Mozilla/5.0 seyirTURK__KODI',
     key44: answer44,
     'Connection': 'Close'})
    r = urllib2.urlopen(req).read()
    aJson = json.loads(r)
    for rs in aJson['movies']:
        idx = str(rs['ID'])
        sTitle = rs['Name']
        sPicture = rs['Image']
        Language = rs['Language']
        Summary = rs['Summary']
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', idx)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'diziler2', sTitle, Summary, sPicture, Summary, oOutputParameterHandler)

    oGui.setEndOfDirectory()
    return


def diziler2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    urls = 'http://satura.tk/sey/back/episodes.php?id=' + url + '&u_id='
    req = urllib.request.Request(urls, None, {'User-agent': 'Mozilla/5.0 seyirTURK__KODI',
     key44: answer44,
     'Connection': 'Close'})
    r = urllib2.urlopen(req).read()
    aJson = json.loads(r)
    for rs in aJson['episodes']:
        idx = str(rs['ID'])
        sPicture = rs['Image']
        e_id = rs['E_ID']
        season = rs['Season']
        episode = rs['Episode']
        sTitle = rs['Name'] + '-S' + str(season) + 'B' + str(episode)
        urls = 'http://satura.tk/sey/back/streams.php?id=' + idx + '&isTv=' + season + '&e=' + episode + '&s=1&e_id=' + e_id + '&u_id='
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', urls)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'diziler3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    return

def playWithCustomPlayer(url, videoInfo={'magnetUrl':""},seed_after=False):
    url += '|verifypeer=false'
    play_item = xbmcgui.ListItem(path=url)

         
import re
import requests
import time

def cf_sample_domain_function(func_expression, domain):
    parameter_start_index = func_expression.find('}(') + 2
    sample_index = cf_parse_expression(func_expression[parameter_start_index:func_expression.rfind(')))')])
    return ord(domain[int(sample_index)])


def cf_arithmetic_op(op, a, b):
    if op == '+':
        return a + b
    if op == '/':
        return a / float(b)
    if op == '*':
        return a * float(b)
    if op == '-':
        return a - b
    raise Exception('Unknown operation')


def cf_parse_expression(expression, domain = None):

    def _get_jsfuck_number(section):
        digit_expressions = section.replace('!+[]', '1').replace('+!![]', '1').replace('+[]', '0').split('+')
        return int(''.join((str(sum((int(digit_char) for digit_char in digit_expression[1:-1]))) for digit_expression in digit_expressions)))

    if '/' in expression:
        dividend, divisor = expression.split('/')
        dividend = dividend[2:-1]
        if domain:
            divisor_a, divisor_b = divisor.split('))+(')
            divisor_a = _get_jsfuck_number(divisor_a[5:])
            divisor_b = cf_sample_domain_function(divisor_b, domain)
            return _get_jsfuck_number(dividend) / float(divisor_a + divisor_b)
        else:
            divisor = divisor[2:-1]
            return _get_jsfuck_number(dividend) / float(_get_jsfuck_number(divisor))
    else:
        return _get_jsfuck_number(expression[2:-1])


def _extract_js(body, domain):
    form_index = body.find('id="challenge-form"')
    sub_body = body[form_index:]
    if body.find('id="cf-dn-', form_index) != -1:
        extra_div_expression = re.search('id="cf-dn-.*?>(.+?)<', sub_body).group(1)
    if 's,t,o,p, b,r,e,a,k,i,n,g,f,' in body:
        js_answer = cf_parse_expression(re.search(',([^=]+)=({[^\\}]+\\})', body, re.DOTALL).group(1))
    builder = re.search("challenge-form'\\);\\s*;(.*);a.value", body, re.DOTALL).group(1)
    lines = builder.replace(' return +(p)}();', '', 1).split(';')
    for line in lines:
        if len(line) and '=' in line:
            heading, expression = line.split('=', 1)
            if 'eval(eval(' in expression:
                expression_value = cf_parse_expression(extra_div_expression)
            elif 'function(p' in expression:
                expression_value = cf_parse_expression(expression, domain)
            else:
                expression_value = cf_parse_expression(expression)
            js_answer = cf_arithmetic_op(heading[-1], js_answer, expression_value)

    if '+ t.length' in body:
        js_answer += len(domain)
    ret = format(js_answer, '.10f')
    return str(ret)


r = requests.Session()

def get_stream_32(stream):
    user_agent = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)'
    wms_url = 'https://echo-4.livenettv.io/fd.nettv/'
    auth = 'BYjEbsEwrVUHwCvB66Cn+Okwn139hvqTh5J3LzMYhMg='
    mod_value = int('1563634273')
    modified = lambda value: ''.join(chain(*zip(str(int(time.time()) ^ value), '0123456789')))
    api_url = 'http://212.83.158.140:6060/all.nettv/'
    response_body_api_url = 'http://212.83.158.140:6060/all.nettv/'
    response_body_auth = 'BYjEbsEwrVUHwCvB66Cn+Okwn139hvqTh5J3LzMYhMg='
    req = requests.Request('GET', response_body_api_url, headers={'User-Agent': user_agent,
     'pin': response_body_auth})
    prq = req.prepare()
    r = s.send(prq)
    response_body = r.text
    data = {'data': json.dumps({'token': 32,
              'response_body': response_body,
              'stream_url': stream})}
    req = requests.Request('GET', api_url, headers={'User-Agent': user_agent,
     'Accept-Encoding': 'gzip',
     'Modified': modified(mod_value),
     'pin': auth}, data=data)
    prq = req.prepare()
    r = s.send(prq)
    return r


def get_auth_token_44():
    wms_url = 'https://echo-4.livenettv.io/xerau/uarex/'
    auth = 'BYjEbsEwrVUHwCvB66Cn+Okwn139hvqTh5J3LzMYhMg='
    mod_value = int('1563634273')
    modified = lambda value: ''.join(chain(*zip(str(int(time.time()) ^ value), '0123456789')))
    data = {'data': json.dumps({'token': 54,
              'response_body': response_body,
              'stream_url': stream})}
    req = requests.Request('GET', wms_url, headers={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)',
     'Accept-Encoding': 'gzip',
     'Modified': modified(mod_value),
     'pin': auth})
    prq = req.prepare()
    r = s.send(prq)
    return r.text


user = 'b0ca81082dcc06351ba35edce6fcbbd5'
config = ''
host = 'echo-d.livenettv.io/data/1/'
package_name = 'com.int.androidnettv'
sha1 = '39:A0:97:F6:A5:98:2E:2E:BE:15:4D:A4:36:8F:94:7A:97:EE:F9:FC'


#def id_generator(size = 8, chars = string.ascii_lowercase + string.digits):
#    return ''.join((random.choice(chars) for _ in range(size)))


def lmget_channel_list():
    login_url = 'https://echo-i.livenettv.io/index'
    time_stamp = str(int(time.time() * 1000))
    allow = b64encode('{time_md5}${package_name}${apk_cert_sha1}${time_stamp}${user_id}${provider}'.format(time_md5=md5(time_stamp.encode()).hexdigest(), package_name=package_name, apk_cert_sha1=sha1, time_stamp=time_stamp, user_id=user, provider='2').encode())
    data = {'ALLOW': allow}
    r = s.post(login_url, data=data)
    _key = r.json().get('funguo')
    _meta = r.headers['etag'].split(':')[0]
    _enc = r.headers['etag'].split(':')[1]
    _hash, _host = b64decode(_enc + '=' * (-len(_enc) % 4)).split('|')
    if _host.startswith('http'):
        host = _host + 'data.nettv/'
    name = 'test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, host, '')


def mmget_channel_list():
    login_url = 'https://echo-i.livenettv.io/index'
    time_stamp = str(int(time.time() * 1000))
    allow = b64encode('{time_md5}${package_name}${apk_cert_sha1}${time_stamp}${user_id}${provider}'.format(time_md5=md5(time_stamp.encode()).hexdigest(), package_name=package_name, apk_cert_sha1=sha1, time_stamp=time_stamp, user_id=user, provider='2').encode())
    data = {'ALLOW': allow}
    r = s.post(login_url, data=data)
    _key = r.json().get('funguo')
    _meta = r.headers['etag'].split(':')[0]
    _enc = r.headers['etag'].split(':')[1]
    _hash, _host = b64decode(_enc + '=' * (-len(_enc) % 4)).split('|')
    if _host.startswith('http'):
        host = _host + 'data.nettv/'
    check = '1'
    headers = {'Referer': 'https://echo-i.livenettv.io/index',
     'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)'}
    data = {'': ''}
    hos = json.dumps(mylist, separators=(',', ':'))
    name = 'test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, hos, '')


def mmget_channel_list():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = 'https://dl.dropboxusercontent.com/s/1cq9anwx0lfv27g/sh.xml'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    data = data.replace('[COLOR blue]D[/COLOR]ONATION [COLOR blue]RS[/COLOR]IPTV', '')
    datadata = re.findall('<string name="s6023767_seccs">(.*?)</string>', data, re.S)
    datadata = str(datadata).replace('>', ',').replace('<', ',')
    title = re.findall('(\\d+)', datadata, re.S)
    for dat in title:
        sTitle = re.findall('<string name="s' + dat + '_tit">(.*?)</string>', data, re.S)[0]
       
        sUrl = 's' + dat
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, 'channellist', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def channellist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    url = 'https://dl.dropboxusercontent.com/s/1cq9anwx0lfv27g/sh.xml'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    data = data.replace('[COLOR blue]D[/COLOR]ONATION [COLOR blue]RS[/COLOR]IPTV', '')
    datadata = re.findall('<string name="' + cat_id + '_seccs">(.*?)</string>', data, re.S)
    datadata = str(datadata).replace('>', ',').replace('<', ',')
    title = re.findall('(\\d+)', datadata, re.S)
    for dat in title:
        sTitle = re.findall('<string name="s' + dat + '_tit">(.*?)</string>', data, re.S)[0]
        sTitle = sTitle.replace('[COLOR blue]A[/COLOR]UTO', '')
        sUrl = re.findall('<string name="s' + dat + '_url">(.*?)</string>', data, re.S)[0]
        if 'yadi.sk' in sUrl:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
            datak = requests.get(sUrl, headers=headers).text
            sUrl = re.findall('"dimension":"adaptive","size":.*?,"url":"(.*?)"', datak, re.S)[0]
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, 'pplay__rabictv', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def ASCIIDecode(string):
    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c = string[i]
        if string[i:i + 2] == '\\x':
            c = chr(int(string[i + 2:i + 4], 16))
            i += 3
        if string[i:i + 2] == '\\u':
            cc = int(string[i + 2:i + 6], 16)
            if cc > 256:
                return ''
            c = chr(cc)
            i += 5
        ret = ret + c
        i = i + 1

    return ret


def decodeUN(a):
    s3 = a.decode('unicode-escape')


def mget_channel_list():
    oGui = cGui()
    ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
    path = os.path.abspath(os.path.join(ADDON_DATA_DIR, 'sites'))
    for foldername in os.listdir(path):
        if foldername.startswith('.') or foldername.endswith('py') or foldername.endswith('pyc'):
            continue
        zeile = foldername.strip().split('.')
        urls = zeile[0].replace('__init__', '')
        item = 'siteUrl'
        patho = os.path.abspath(os.path.join(path, '%s.py' % urls))
        d = open(patho)
        content = d.read()
        d.close
        wmsAuth = re.findall("SITE_NAME = '(.*?)'", content, re.S)[0]
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + item, wmsAuth, '')


def mget_channel_list():
    oGui = cGui()
    ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
    path = os.path.abspath(os.path.join(ADDON_DATA_DIR, 'sites'))
    for foldername in os.listdir(path):
        if foldername.startswith('.') or foldername.endswith('py') or foldername.endswith('pyc'):
            continue
        zeile = foldername.strip().split('.')
        urls = zeile[0]
        patho = os.path.abspath(os.path.join(path, '' + urls + '.py'))
        d = open(patho)
        content = d.read()
        d.close
        cont = re.findall("SITE_NAME = '(.*?)'.*?SITE_ICON = '(.*?)'", content, re.S)
        for NAME, sPicture in cont:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', urls)
            oOutputParameterHandler.addParameter('sMovieTitle', urls)
            oGui.addDir(SITE_IDENTIFIER, 'testzest', NAME, sPicture, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def testzest():
    oInputParameterHandler = cInputParameterHandler()
    sSiteName = oInputParameterHandler.getValue('siteUrl')
    plugins = __import__('sites.%s' % sSiteName, fromlist=[sSiteName])
    function = getattr(plugins, 'load')
    function()


def eLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    liste = 'http://swiftstreamz.com/SwiftPanel/apiv1.php?get_channels_by_cat_id=28'
    sJson = cRequestHandler(liste).request()
    sPattern = '"stream_url": "(.*?)".*?"token": "(.*?)"'
    jsonOb = re.compile(sPattern, re.DOTALL).findall(sJson)
    for urll, token in jsonOb:
        for i in len(-1):
            stop = step = None
            start = 25
            string = ''
            name = 'TOKEN TYPE'
            url = start[i:0]
            sPicture = 'http://swiftstreamz.com/SwiftPanel/apiv1.php?get_channels_by_token_link=28'
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')

    return





def addOfflineMediaFile(urla, name):
    if 'plugin' in urla:
        liz = xbmcgui.ListItem('', thumbnailImage='https://superrepo.org/static/images/icons/original/xplugin.video.xtream-codes.png.pagespeed.ic.7uLaZTpLY3.png', iconImage='DefaultFolder.png')
        uurl = '' + urla
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), listitem=liz, url=uurl, isFolder=True)


def Russia():
    oGui = cGui()
    sJson = cRequestHandler(da_url).request()
    aJson = json.loads(sJson)
    for cat in aJson['channels']:
        catid = cat['id']
        sTitle = cat['name']
        sPic = cat['logo']
        cat = cat['stream']
        sPicture = '' + sPic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', cat)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'pplay__rabictv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showContentB3():
    oGui = cGui()
    content = getUrl(Hostbir)
    regexcat = '#SERVICE 1:64:.*?:0:0:0:0:0:0:0::([\\S\\s]+?)#'
    match = re.compile(regexcat, re.DOTALL).findall(content)
    i = 0
    for sTitle in match:
        if i < 3:
            i = i + 1
            continue
        i = i + 1
        url1 = Hostbir
        sPicture = ' '
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url1)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'showContentB2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showContentB1():
    oGui = cGui()
    content = cRequestHandler(Host).request()
    regexcat = '\xe2\x98\x85\xe2\x98\x85(.+?)\xe2\x98\x85\xe2\x98\x85'
    match = re.compile(regexcat, re.DOTALL).findall(content)
    i = 0
    for sTitle in match:
        if i < 3:
            i = i + 1
            continue
        i = i + 1
        url1 = Host
        sPicture = ' '
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url1)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'showContentB2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showContentB2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    content = cRequestHandler(url).request()
    name = name.replace('+', ' ')
    name = name.replace('%20', ' ')
    n1 = content.find(name, 0)
    n2 = content.find('---', n1 + 100)
    if n2 > -1:
        content2 = content[n1:n2]
    else:
        content2 = content[n1:]
    regexvideo = '#SERVICE 4097\\:.*?\\:.*?\\:.*?\\:.*?\\:.*?\\:.*?\\:.*?\\:.*?\\:.*?\\:(.*?)\\:(.*?)#'
    match = re.compile(regexvideo, re.DOTALL).findall(content2)
    for url, name in match:
        pic = ' '
        name = name[:-1]
        name = name.replace('"', '')
        name = name.replace('\n', '')
        url = url.replace('%3a', ':')
        Title = name
        url1 = url
        sPicture = ' '
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url1)
        oOutputParameterHandler.addParameter('sMovieTitle', str(Title))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'pplay__rabictv', Title, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def wmsAuth():
    son = cRequestHandler(ddatam_url).request()
    wmsAuth = re.findall('"wmsAuthSign": "(.*?)"', son, re.S)[0]
    return wmsAuth


def Auth():
    dat = 'https://app.liveplanettv.com/beta/api.php?device_id=355757080729185'
    req = urllib.request.Request(dat)
    req.add_header('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/NRD90M)')
    req.add_header('Host', 'app.liveplanettv.com')
    req.add_header('Connection', 'Keep-Alive')
    req.add_header('Accept-Encoding', 'gzip')
    sJson = _get(req)
    AuthSign = re.search('"wmsAuthSign": "(.+?)"', sJson).group(1)
    device_id = re.search('"device_id": "(.+?)"', sJson).group(1)
    list_url = 'https://app.liveplanettv.com/beta/token.php?wmsAuthSign=' + AuthSign + '&device_id=' + device_id
    req = urllib.request.Request(list_url)
    req.add_header('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/NRD90M)')
    req.add_header('Host', 'app.liveplanettv.com')
    req.add_header('Connection', 'Keep-Alive')
    req.add_header('Accept-Encoding', 'gzip')
    sHtml = _get(req)
    time.sleep(5)
    AuthSign = re.search('"videoToken": "(.+?)"', sHtml).group(1)
    return AuthSign


def mAuth():
    son = cRequestHandler(ddatam_url).request()
    wmsAuth = re.findall('"wmsAuthSign": "(.*?)"', son, re.S)[0]
    ddatam = 'http://app.liveplanettv.com/beta/token.php?wmsAuthSign=' + wmsAuth + '&device_id=354630080742220'
    sJson = cRequestHandler(ddatam).request()
    wmsAuthSign = re.findall('"wmsAuthSign": "(.*?)"', sJson, re.S)[0]
    return wmsAuthSign


def nnwmsAuth():
    sJson = cRequestHandler(ddatam_url).request()
    aJson = json.loads(sJson)
    for _token in aJson['LIVETV']['token']:
        Pic = _token
        wmsAuth = Pic.get['wmsAuthSign']
        return wmsAuth




def rrootata():
    oGui = cGui()
    ddat = 'https://dl.dropboxusercontent.com/s/k1lovh8v9ry9cqn/ana.api.json'
    sJson = cRequestHandler(ddat).request()
    Json = json.loads(sJson)
    for cat in Json['LIVETV']['category']:
        catid = cat['cid']
        sTitle = cat['category_name']
        sPic = cat['category_image'].replace('Turkey (1).jpg', 'Turkey.jpg').replace('SOUTHINDIAN (1).jpg', 'SOUTHINDIAN.jpg')
        
        sPicture = 'http://app.liveplanettv.com/beta/images/' + sPic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sTitle)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'tatLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def tatLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    catid = oInputParameterHandler.getValue('siteUrl')
    dat = 'https://dl.dropboxusercontent.com/s/ccwiajaoj9gezpe/al.api.json'
    son = cRequestHandler(dat).request()
    channels = re.findall('"category" : "' + catid + '".*?"icon" : "(.*?)".*?"link" : "(.*?)".*?"name" : "(.*?)"', son, re.S)
    for sPicture, url, sTitle in channels:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'tatplayLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()




def tatplayLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Url = str(sUrl) + Auth()
    name = alfabekodla(sTitle)
    Url = Url + '|User-Agent=stagefright/1.2 (Linux;Android 5.1.1)'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, Url, '')


def aaddLink(name, url, iconimage):
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.setResolvedUrl(cGui().pluginHandle, True, liz)
    xbmc.Player().play(url, liz)
    xbmcPlayer = xbmc.Player()
    return pPlayer().startPlayer()


def atplaylive():
    oInputParameterHandler = cInputParameterHandler()
    Urla = oInputParameterHandler.getValue('siteUrl')
    Url = 'http://139.59.68.238/stm-v3/api/def2.php?id=%s&quality=0&type=0' % Urla
    name = oInputParameterHandler.getValue('sMovieTitle')
    data = requests.session().get(Url, headers={'WWW-Authenticate': 'IVYBOWQn+1rgFXNAWMDB06XjA=',
     'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)',
     'Host': '139.59.68.238',
     'Connection': 'Keep-Alive',
     'Accept-Encoding': 'gzip'}).text
    data = data.replace('\\/', '/')
    url = re.findall('"link": "(.*?)"', data, re.S)[0] + '|User-Agent=User-Agent=stagefright/1.2 (Linux;Android 5.1.1)'
    if 'http' not in url:
        dat = b64decode(re.findall('"link": "(.*?)"', data, re.S)[0][2:])
        liste = re.findall('(http://.*?.php),(http://.*?.m3u8)', dat, re.S)
        if liste:
            token, File = liste[0]
            post_data = {'data': posta_data()}
            r = s.post(token, headers={'Content-Length': '101',
             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'Host': 'swiftstreamz.com',
             'Connection': 'Keep-Alive',
             'Accept-Encoding': 'gzip'}, data=post_data, timeout=10)
            auth = r.text
            token = 'http://hyfytv.today/decrypt1.php?token=' + auth
            auth_token = cRequestHandler(token).request()
            url = '{0}{1}|User-Agent={2}'.format(File, auth_token, quote(player_user_agent))
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def sourcetvm3u():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    import re
#    open = OPEN_URL(url)
#    url = regex_from_to(open, '<p><a href="', '"')
    open = OPEN_URL(url)
    regex = re.compile('#EXTINF:.+?\\,(.+?)\n(.+?)\n', re.MULTILINE | re.DOTALL).findall(open)
    for sTitle, Url in regex:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'iptvplay_info', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def rmootatam():
    oGui = cGui()
    sJson = cRequestHandler(ulkeLists).request()
    aJson = json.loads(sJson)
    for cat in aJson:
        catid = cat['stream']
        sTitle = cat['name']
        sPic = cat['logo_file_name']
        
        sPicture = 'http://apim.livetv.az/images/medium/' + sPic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', catid)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'showtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def worldrootata():
    oGui = cGui()
    ulk = 'http://hyfystreamz.com/dfytv/list.json'
    sJson = cRequestHandler(ulk).request()
    aJson = json.loads(sJson)
    for cat in aJson['CATLIST']:
        sTitle = cat['category']
        sPicture = cat['cat_img']
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sTitle)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'worldroota', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def worldroota():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_title = oInputParameterHandler.getValue('siteUrl')
    ulk = 'http://hyfystreamz.com/dfytv/list.json'
    sJson = cRequestHandler(ulk).request()
    aJson = json.loads(sJson)
    for cat in aJson['TVLINK']:
        if cat['country'] == cat_title:
            sTitle = cat['name']
            url = cat['link']
            sPicture = cat['icon']
            
            surl = b64decode(url[1:])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'showtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def fatplaylive():
    Url = 'http://139.59.68.238/stm-v3/api/def2.php?id=470&quality=0&type=0'
    data = requests.session().get(Url, headers={'WWW-Authenticate': 'IVYBOWQn+1rgFXNAWMDB06XjA=',
     'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)',
     'Host': '134.209.153.85',
     'Connection': 'Keep-Alive',
     'Accept-Encoding': 'gzip'}).text
    liste = re.findall('"token": "(.*?)"', data, re.S)[0]
    liste = b64decode(liste[2:])
    listem = re.findall('"swt","aYW10=","1","(.*?)"', liste, re.S)[0]
    datama = b64decode(listem[2:])
    data = re.findall('"data":"(.*?)"', datama, re.S)[0]
    Urlum = 'http://swiftstreamz.com/newapptoken13.php'
    post = {'data': data}
    req = urllib.request.Request(Urlum)
    req.add_header('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
    req.add_header('Host', 'swiftstreamz.com')
    post = urllib.urlencode(post)
    autho = _get(req, post)
    post = {'data': data}
    Urlu = 'http://swiftstreamz.com/newapptoken13.php'
    req = urllib.request.Request(Urlu)
    req.add_header('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
    req.add_header('"WWW-Authenticate', 'IVYBOWQn+1rgFXNAWMDB06XjA=')
    req.add_header('Host', '139.59.68.238')
    post = urllib.urlencode(post)
    auth = _get(req, post).replace('\\/', '/')
    data = 'http://212.8.253.141:7071/wildsci2019/animalplanet/playlist.m3u8' + auth
    name = 'https://goo.gl/wqsVrs'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, data, '')


def miptv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = 'https://goo.gl/wqsVrs'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    data = data.replace('[COLOR blue]D[/COLOR]ONATION [COLOR blue]RS[/COLOR]IPTV', '')
    title = re.findall('<title>(.*?)</title>.*?<externallink>(.*?)</externallink>', data, re.S)
    for sTitle, sUrl in title:
     
        sUrl = sUrl.replace('$$TSDOWNLOADER$$', '')
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, 'motvshowGenre', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def parseM3U(sUrl=None, infile=None):  # Traite les m3u local
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    if infile is None:
        if 'iptv4sat' in sUrl or '.zip' in sUrl:
            sHtmlContent = getHtml(sUrl)
            zip_files = ZipFile(io.BytesIO(sHtmlContent))
            files = zip_files.namelist()

            for Title in files:
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('sMovieTitle', Title)
                oOutputParameterHandler.addParameter('siteUrl', sUrl)

                oGui.addDir(SITE_IDENTIFIER, 'unZip', Title, 'tv.png', oOutputParameterHandler)

            oGui.setEndOfDirectory()
            return

        elif '#EXTM3U' not in sUrl:
            headers = {'User-Agent': UA}

            oRequestHandler = cRequestHandler(sUrl)
            oRequestHandler.addHeaderEntry('User-Agent', UA)
            inf = oRequestHandler.request()

            if 'drive.google' in inf:
                inf = unGoogleDrive(inf)

            inf = inf.split('\n')
        else:
            inf = infile

    else:
        inf = infile

    try:
        line = inf.readline()
    except:
        pass

    playlist = []
    song = track(None, None, None, None)
    ValidEntry = False

    for line in inf:
        if xbmc.getInfoLabel('system.buildversion')[0:2] >= '19':
            try:
                line = line
            except AttributeError:
                pass

        line = line.strip()
        if line.startswith('#EXTINF:'):
            length, title = line.split('#EXTINF:')[1].split(',', 1)
            try:
                licon = line.split('#EXTINF:')[1].partition('tvg-logo=')[2]
                icon = licon.split('"')[1]
            except:
                icon = 'tv.png'
            ValidEntry = True
            song = track(length, title, None, icon)

        elif (len(line) != 0):
            if (ValidEntry) and (not (line.startswith('!') or line.startswith('#'))):
                ValidEntry = False
                song.path = line
                playlist.append(song)
                song = track(None, None, None, None)

    try:
        inf.close()
    except:
        pass

    return playlist


def showWeb(infile=None):  # Code qui s'occupe de liens TV du Web
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()

    if infile is None:
        sUrl = oInputParameterHandler.getValue('siteUrl')

        playlist = parseM3U(sUrl=sUrl)
    else:
        playlist = parseM3U(infile=infile)

    if oInputParameterHandler.exist('AZ'):
        sAZ = oInputParameterHandler.getValue('AZ')
        string = filter(lambda t: t.title.strip().capitalize().startswith(sAZ), playlist)
        playlist = sorted(string, key=lambda t: t.title.strip().capitalize())
    else:
        playlist = sorted(playlist, key=lambda t: t.title.strip().capitalize())

    if not playlist:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addText(SITE_IDENTIFIER, '[COLOR red]Problème de lecture avec la playlist[/COLOR]')

    else:
        total = len(playlist)
        progress_ = progress().VScreate(SITE_NAME)
        for track in playlist:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            sThumb = track.icon
            if not sThumb:
                sThumb = 'tv.png'

            # les + ne peuvent pas passer
            url2 = track.path.replace('+', 'P_L_U_S')
            if not xbmc.getInfoLabel('system.buildversion')[0:2] >= '19':
                if not '[' in url2 and not ']' in url2 and not '.m3u8' in url2 and not 'dailymotion' in url2:
                    url2 = 'plugin://plugin.video.f4mTester/?url=' + QuotePlus(url2) + '&amp;streamtype=TSDOWNLOADER&name=' + Quote(track.title)

            thumb = '/'.join([sRootArt, sThumb])

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', url2)
            oOutputParameterHandler.addParameter('sMovieTitle', track.title)
            oOutputParameterHandler.addParameter('sThumbnail', thumb)

            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setFunction('play__')
            oGuiElement.setTitle(track.title)
            oGuiElement.setFileName(track.title)
            oGuiElement.setIcon('tv.png')
            oGuiElement.setMeta(0)
            oGuiElement.setThumbnail(thumb)
            oGuiElement.setDirectTvFanart()
            oGuiElement.setCat(6)

            oGui.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, SITE_IDENTIFIER, SITE_IDENTIFIER, 'direct_epg', 'Guide tv Direct')
            oGui.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, SITE_IDENTIFIER, SITE_IDENTIFIER, 'soir_epg', 'Guide tv Soir')
            oGui.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, SITE_IDENTIFIER, SITE_IDENTIFIER, 'enregistrement', 'Enregistrement')
            oGui.createContexMenuBookmark(oGuiElement, oOutputParameterHandler)
            oGui.addFolder(oGuiElement, oOutputParameterHandler)

        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()


def direct_epg():  # Code qui gerent l'epg
    # oGuiElement = cGuiElement()
    oInputParameterHandler = cInputParameterHandler()
    # aParams = oInputParameterHandler.getAllParameter()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    cePg().view_epg(sTitle, 'direct')


def soir_epg():  # Code qui gerent l'epg
    # oGuiElement = cGuiElement()
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    cePg().view_epg(sTitle, 'soir')


def enregistrement():  # Code qui gerent l'epg
    # oGuiElement = cGuiElement()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl').replace('P_L_U_S', '+')

    enregistrementIsActif = ADDON.getSetting('enregistrement_activer')
    if enregistrementIsActif == 'false':
        dialog().VSok('Merci d\'activer l\'enregistrement dans les options')
        return

    if '[' in sUrl and ']' in sUrl:
        sUrl = GetRealUrl(sUrl)

    if 'plugin' in sUrl:
        url = re.findall('url=(.+?)&amp', ''.join(sUrl))
        sUrl = Unquote(url[0])
    cEnregistremement().programmation_enregistrement(sUrl)


def showAZ():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    for i in string.digits:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('AZ', i)
        oGui.addDir(SITE_IDENTIFIER, 'showTV', i, 'az.png', oOutputParameterHandler)

    for i in string.ascii_uppercase:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('AZ', i)
        oGui.addDir(SITE_IDENTIFIER, 'showTV', i, 'az.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showAZRadio():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    for i in string.digits:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('AZ', i)
        oGui.addDir(SITE_IDENTIFIER, 'showWeb', i, 'az.png', oOutputParameterHandler)

    for i in string.ascii_uppercase:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('AZ', i)
        oGui.addDir(SITE_IDENTIFIER, 'showWeb', i, 'az.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showTV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
    sPattern = '<title>(.+?)</title><link>(.+?)</link>'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0] is True:
        progress_ = progress().VScreate(SITE_NAME)

        # affiche par
        if oInputParameterHandler.exist('AZ'):
            sAZ = oInputParameterHandler.getValue('AZ')
            string = filter(lambda t: t[0].strip().capitalize().startswith(sAZ), aResult[1])
            string = sorted(string, key=lambda t: t[0].strip().capitalize())
        else:
            string = sorted(aResult[1], key=lambda t: t[0].strip().capitalize())

        total = len(string)
        for aEntry in string:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', aEntry[1])
            oOutputParameterHandler.addParameter('sMovieTitle', aEntry[0])
            oOutputParameterHandler.addParameter('sThumbnail', 'tv.png')

            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setFunction('play__')
            oGuiElement.setTitle(aEntry[0])
            oGuiElement.setFileName(aEntry[0])
            oGuiElement.setIcon('tv.png')
            oGuiElement.setMeta(0)
            # oGuiElement.setThumbnail('tv.png')
            oGuiElement.setDirectTvFanart()
            oGuiElement.setCat(6)

            oGui.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, SITE_IDENTIFIER, SITE_IDENTIFIER, 'direct_epg', 'Guide tv Direct')
            oGui.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, SITE_IDENTIFIER, SITE_IDENTIFIER, 'soir_epg', 'Guide tv Soir')
            oGui.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, SITE_IDENTIFIER, SITE_IDENTIFIER, 'enregistrement', 'Enregistrement')
            oGui.createContexMenuBookmark(oGuiElement, oOutputParameterHandler)
            oGui.addFolder(oGuiElement, oOutputParameterHandler)

        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()


def play__():  # Lancer les liens

    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl').replace('P_L_U_S', '+')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sDesc = oInputParameterHandler.getValue('sDesc')
    import streamer
    streamer.sstreamer(name,url)
                

    if 'dailymotion' in sUrl:
        showDailymotionStream(sUrl, sTitle, sThumbnail)
        return

    if 'f4mTester' in sUrl:
        xbmc.executebuiltin('XBMC.RunPlugin(' + sUrl + ')')
        return

    else:
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        sUrl = sUrl.replace(' ', '%20')
        oGuiElement.setMediaUrl(sUrl)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setDescription(sDesc)

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
