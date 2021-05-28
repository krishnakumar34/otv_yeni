#-*- coding: utf-8 -*-
import urllib2, urllib,cookielib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
from resources.lib.otvhelper import  gegetUrl,getUrl ,alfabekodla
from resources.lib.config import cConfig
import requests
import re,xbmcgui,unicodedata              
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import Parser as cParser
from resources.lib.comaddon import progress, VSlog
from resources.lib.player import cPlayer

from resources.lib.gui.guiElement import cGuiElement

SITE_NAME = 'OTV_MEDIA'
from resources.lib.gui.gui import cGui

import binascii


SITE_IDENTIFIER = 'orhantv'


from json import dumps, loads, JSONEncoder, JSONDecoder

from decimal import Decimal
from base64 import b64encode, b64decode
from json import dumps, loads, JSONEncoder


class PythonObjectEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (list,
         dict,
         str,
         int,
         float,
         bool,
         type(None))):
            return super().default(obj)
        else:
            return {'_python_object': b64encode(pickle.dumps(obj)).decode('utf-8')}
            return


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(b64decode(dct['_python_object'].encode('utf-8')))
    return dct


class mPythonObjectEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (list,
         dict,
         str,
         unicode,
         int,
         float,
         bool,
         type(None))):
            return JSONEncoder.default(self, obj)
        else:
            return {'_python_object': pickle.dumps(obj)}
            return


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct


import urlparse, sys, re, xbmcgui, os
import re, unicodedata
HOST = '?idd=&prev=search&ved=2ahUKEwi'
import md5
from binascii import b2a_hex

from urllib2 import Request, URLError, urlopen as urlopen2
from datetime import timedelta
from base64 import b64decode
addon = xbmcaddon.Addon()
user_agent = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTS Build/LVY48F)'
import sys
import os
import io
import json
import requests
import datetime
from datetime import timedelta
from base64 import b64decode, urlsafe_b64encode
s = requests.Session()
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
s = requests.Session()
user_agent = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)'
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)
implemented = ['0',
 '38',
 '21',
 '48']
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path')).decode('utf-8')
user_file = os.path.join(ADDON_DATA_DIR, 'list.json')
app_config_file = os.path.join(USER_DATA_DIR, 'config.json')
channel_list_file = os.path.join(USER_DATA_DIR, 'channels.json')
from time import gmtime, strftime
ulkeLists = 'http://85.132.71.12/channels'

def SwiftAuthSign(base_url):
    conv = time.strptime(from_date, '%n %j %d %Y')
    time.strftime('%d/%m/%Y', conv)
    key = '@SwiftStreamz#'
    validminutes = 2
    str2hash = (key, today, validminutes)
    md5raw = hashlib.md5(str2hash).hexdigest()
    base64hash = base64_encode(md5raw)
    urlsignature = 'server_time=' + today + '&hash_value=' + base64hash + '&validminutes=$validminutes'
    base64urlsignature = base64_encode(urlsignature)
    return base_url + '?wmsAuthSign=' + base64urlsignature


def okuoku(cba):
    oku = ''
    i = len(cba) - 1
    while i >= 0:
        oku += cba[i]
        i -= 1

    return oku


class GIFError(Exception):
    pass


def get_gif_num_frames(filename):
    frames = 0
    with open(filename, 'rb') as f:
        if f.read(6) not in ('GIF87a', 'GIF89a'):
            raise GIFError('not a valid GIF file')
        f.seek(4, 1)

        def skip_color_table(flags):
            if flags & 128:
                f.seek(3 << (flags & 7) + 1, 1)

        flags = ord(f.read(1))
        f.seek(2, 1)
        skip_color_table(flags)
        while True:
            block = f.read(1)
            if block == ';':
                break
            if block == '!':
                f.seek(1, 1)
            elif block == ',':
                frames += 1
                f.seek(8, 1)
                skip_color_table(ord(f.read(1)))
                f.seek(1, 1)
            else:
                raise GIFError('unknown block type')
            while True:
                l = ord(f.read(1))
                if not l:
                    break
                f.seek(l, 1)

    return frames


def unpad_pkcs5(padded):
    if is_py3:
        return padded[:-padded[-1]]
    else:
        return padded[:-ord(padded[-1])]


url1 = 'PXdXYjQ1Q1praDJMbWxUTTI4V2NrbFdadzRXY25KRE52TTNMdDkyWXVRbmJsUm5idk5tY2xOWGQ0OW1ZdzltY2s1Q2JrOXlMNk1IYzBSSGE='
url2 = base64.b64decode(url1)
url3 = okuoku(url2)
streamurl = base64.b64decode(url3)

def amzddecode(k4):
    k4 = k4.replace('htup>+.akegw|gv7#~q+ixa?bem&k7w8 mi!', 'https://yayin2.betajani.net/hls/lig1.m3u8?st=').replace('htupw>./lej}mqmnl`fjrd}b?"\x7f{)lns0rt{*4t+b.*gg/', 'https://canlimacyayiniajanspor.us/hls/lig1.m3u8?st=').replace('#a>', '&e=').replace('', '').replace('2f626567686565', 'macyayinajanspor.us/hls/lig1.m3u8?st=').replace('0645978320', 'canlimacyayiniajanspor.us/hls/lig1.m3u8?st=').replace('074342858670', '%').replace('093857354460', 'www').replace('07463394760', '/')
    k4 = k4.replace('6a', 'a').replace('0890', 'b').replace('0920', 'c').replace('0970', 'd').replace('0740', 'e').replace('0940', 'f').replace('60', 'g').replace('0140', 'h').replace('6c', 'i')
    k4 = k4.replace('6e', 'j').replace('0130', 'k').replace('0110', 'l').replace('7f', 'm').replace('63', 'n').replace('0460', 'p').replace('0710', 'q').replace('0270', 'r')
    k4 = k4.replace('0340', 's').replace('7e', 't').replace('0860', 'u').replace('77', 'v').replace('0330', 'w').replace('0830', 'x').replace('0350', 'y').replace('01230', 'z')
    k4 = k4.replace('0910', 'A').replace('0160', 'B').replace('0590', 'C').replace('0690', 'D').replace('47', 'E').replace('56', 'F').replace('0720', 'G').replace('0580', 'H').replace('46', 'I')
    k4 = k4.replace('4c', 'J').replace('0730', 'K').replace('0120', 'L').replace('0750', 'M').replace('0210', 'N').replace('5c', 'P').replace('51', 'Q').replace('0780', 'R')
    k4 = k4.replace('0650', 'S').replace('0420', 'T').replace('5d', 'U').replace('098340', 'V').replace('09740', 'W').replace('047450', 'X').replace('08820', 'Y').replace('59', 'Z')
    k4 = k4.replace('6d', 'm').replace('45', 'E').replace('08658476940', '$').replace('09284656560', '/').replace('0856483980', '%').replace('0847337644730', '*')
    k4 = k4.replace('01928595750', '?').replace('087535889970', '\\').replace('05372893470', '^').replace('085337390560', '&').replace('085337777560', '+').replace('033779940', '.')
    k4 = k4.replace('011996430', '#').replace('0774411990', '"').replace('09774320', '(').replace('0777224880', ')').replace('087232220', '{').replace('07772374260', '}').replace('086735754840', "'").replace('0573757534590', ':').replace('05731122590', ';')
    k4 = k4.replace('083475590', '!').replace('0777446310', '|').replace('097544770', '[').replace('07547382590', '\\]').replace('08345867760', '_').replace('0847785894580', '-')
    k4 = k4.replace('0760', '1').replace('0660', '2').replace('09190', '3').replace('07590', '4').replace('3c', '5').replace('0950', '6').replace('07210', '7').replace('36', '8').replace('28', '9').replace('0810', '0').replace('39', '8')
    return k4


def streamangodecode(encoded):
    _0x59b81a = ''
    k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    k = k[::-1]
    count = 0
    D = 'B7'
    for index in range(0, len(encoded) - 1):
        while count <= len(encoded) - 1:
            _0x4a2f3a = k.index(encoded[count])
            count += 1
            _0x29d5bf = k.index(encoded[count])
            count += 1
            _0x3b6833 = k.index(encoded[count])
            count += 1
            _0x426d70 = k.index(encoded[count])
            count += 1
            _0x2e4782 = _0x4a2f3a << 2 | _0x29d5bf >> 4
            _0x2c0540 = (_0x29d5bf & 15) << 4 | _0x3b6833 >> 2
            _0x5a46ef = (_0x3b6833 & 3) << 6 | _0x426d70
            _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)
            if _0x3b6833 != 64:
                _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
            if _0x3b6833 != 64:
                _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

    return _0x59b81a


def clear():
    try:
        cacheFile = os.path.join(control.dataPath, 'regex.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute('DROP TABLE IF EXISTS regex')
        dbcur.execute('VACUUM')
        dbcon.commit()
    except:
        pass


def aes_decdecrypt(result):
    from resources.lib import pyaes
    aes = pyaes.AESModeOfOperationCTR(control.key)
    result = aes.decrypt(result)
    data = binascii.hexlify(result)
    return data


HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

def _get(request, post = None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request, post).read()


def _html(url, rheaders = None):
    """Downloads the resource at the given url and parses via BeautifulSoup"""
    headers = {'User-Agent': HEADER_USER_AGENT}
    if rheaders:
        headers.update(rheaders)
    request = urllib2.Request(url, headers=headers)
    return BeautifulSoup(_get(request), convertEntities=BeautifulSoup.HTML_ENTITIES)


def orhantv():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'orhatvturk', 'T\xc3\xbcrK_MEDIA', 'https://img3.picload.org/image/rappiapc/turk_bayragi_tc_16.png', 'https://img3.picload.org/image/rappiapc/turk_bayragi_tc_16.png', 'https://img3.picload.org/image/rappiapc/turk_bayragi_tc_16.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'TUrKVod', 'T\xc3\x9crK_Vod', 'https://picload.org/thumbnail/rwlgpaci/icon.jpg', 'https://picload.org/thumbnail/rwlgpaci/icon.jpg', '', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'Taraftar', 'Derbi TV HD', 'https://yt3.ggpht.com/a-/AN66SAwmPQiOdH4m74dwb9hQ4J_8su4eqpJFB-8uaA=s900-mo-c-c0xffffffff-rj-k-no', 'https://yt3.ggpht.com/a-/AN66SAwmPQiOdH4m74dwb9hQ4J_8su4eqpJFB-8uaA=s900-mo-c-c0xffffffff-rj-k-no', '', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'iptvuser_info', 'IPTV_int new', 'https://images-eu.ssl-images-amazon.com/images/I/51mG8c3eYWL.png', 'https://images-eu.ssl-images-amazon.com/images/I/51mG8c3eYWL.png', '', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'orhantvalman', 'GERMAN_MEDIA', 'https://node01.flagstat.net/media/catalog/product/detail/12720.png', 'https://node01.flagstat.net/media/catalog/product/detail/12720.png', '', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'Sport', 'SPORT', 'http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg', 'http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg', '', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'YouTUBE', 'YouTUBE', 'http://pngimg.com/uploads/youtube/youtube_PNG23.png', 'http://pngimg.com/uploads/youtube/youtube_PNG23.png', '', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'FILMON', 'FILMON', 'http://talkbusiness360.com/wp-content/uploads/2017/03/FilmOn-TV-img-390x215.png', 'http://talkbusiness360.com/wp-content/uploads/2017/03/FilmOn-TV-img-390x215.png', '', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'kuoku', '[COLOR teal]My PlayList[/COLOR]', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1EJoofnHYe-8L92TT8nWdn6uqBZpQxEE9YhVKII2oAUN-Jk9V', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1EJoofnHYe-8L92TT8nWdn6uqBZpQxEE9YhVKII2oAUN-Jk9V', '', oOutputParameterHandler)
    oGui.setEndOfDirectory()


import base64
import binascii

def rsiptv():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.rsiptv_tv",return)')


import requests
import json


def homeMovies365():
    from movies365 import homeMovies365
    homeMovies365()


def read_html(url):
    web_sock = urllib.urlopen(url)
    html = web_sock.read()
    web_sock.close()
    return html


def otvtest2():
    oGui = cGui()
    datay_ur = 'https://dl.dropboxusercontent.com/s/bnwq7w99jq82mg7/sources.json'
    r = requests.get(datay_ur, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}, timeout=10)
    res = r.json(strict=False)
    for cat in res['CATLIST']:
        sTitle = cat['category']
        sPicture = cat['cat_img']
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sTitle)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'otvtest4', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def motvtest4(index = ''):
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Thum = oInputParameterHandler.getValue('sThumbnail')
    sUrl = 'http://hyfystreamz.com/rflix/list.json'
    r = requests.get(sUrl)
    json_input = r.text
    decoded = jsontools.load_json(json_input)
    url = decoded.index('VODLIST')
    addLink('[COLOR lightblue][B]OTV MEDIA RADIO >>  [/B][/COLOR]' + name, url, Thum)


def otvtest4():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://hyfystreamz.com/rflix/list.json'
    with io.open(user_file, 'r', encoding='utf-8') as f:
        channel_list = json.loads(f.read())
        stream_ = channel_list['CATLIST']
        for cat in stream_:
            if cat['country'] == cat_id:
                sPicture = cat['icon']
                sTitle = cat['name']
                stream_url = cat['link']
                sTitle = alfabekodla(sTitle)
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', stream_url)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'playintmovielive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def playintmovielive():
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Thum = oInputParameterHandler.getValue('sThumbnail')
    url = b64decode(urll[1:])
    url = url + '|User-Agent=LiveTVApp/Silver Build 15 (Linux;Android 5.1.1) ExoPlayerLib/2.7.3'
    addLink('[COLOR lightblue][B]OTV MEDIA RADIO >>  [/B][/COLOR]' + name, url, Thum)


def aes_decdecrypt(result):
    from resources.lib import pyaes
    aes = pyaes.AESModeOfOperationCTR(control.key)
    result = aes.decrypt(result)
    data = binascii.hexlify(result)
    return data


def decrypt_stream_url(encoded_url):
    data = yaz64(encoded_url)
    cipher_text = binascii.unhexlify(data[96:])
    decryptor = AES.new(binascii.unhexlify(data[32:96]), AES.MODE_CBC, binascii.unhexlify(data[:32]))
    return unpad_pkcs5(decryptor.decrypt(cipher_text))


USER = 'SolidStreamz'
PASS = '@!SolidStreamz!@'
data_url = 'http://solidstreamz.com/api/streamzdata.php'

def mmdhamkatv():
    oGui = cGui()
    my_list = requests.get('https://raw.githubusercontent.com/jassa007/eurekatv/master/ss.txt', headers={'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.3.1; WT19M-FI Build/JLS36I)',
     'Authorization': 'Basic YWRtaW46QWxsYWgxQA==',
     'Accept': 'gzip'}).text
    for item in my_list:
        if item.find('ABCDEFGHIJKLMNOPQRSTUVWXYZ') != -1:
            name = 'http://trvod.me/prs/TURKvodPrsr'
            url = 'http://trvod.me/prs/TURKvodPrsr'
            sPicture = 'https://archive.li/r4gOb/3fbda78e0bc2bcf323e23bbcc8d877d3228ec895.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', str(name))
            oOutputParameterHandler.addParameter('siteUrl', url)
            oGui.addMovie(SITE_IDENTIFIER, 'kuoku', item, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def toHex(dec):
    x = dec % 16
    digits = '0123456789ABCDEF'
    rest = dec / 16
    if rest == 0:
        return digits[x]
    return toHex(rest) + digits[x]


args = urlparse.parse_qs(sys.argv[2][1:])
memberID0 = args.get('memberID', '0')
if type(memberID0) is list:
    memberID = memberID0[0]
else:
    memberID = memberID0
secret0 = args.get('secret', '')
if type(secret0) is list:
    secret = secret0[0]
else:
    secret = secret0
connection_id0 = args.get('connection_id', '')
if type(connection_id0) is list:
    connection_id = connection_id0[0]
else:
    connection_id = connection_id0
ACTION_PREVIOUS_MENU = 10
ACTION_NAV_BACK = 92
ACTION_MOUSE_MOVE = 107
ACTION_MOVE_UP = 3
ACTION_MOVE_DOWN = 4

def build_url(query):
    global secret
    global memberID
    global connection_id
    query['memberID'] = memberID
    query['secret'] = secret
    query['connection_id'] = connection_id
    return sys.argv[0] + '?' + urllib.urlencode(query)


def deviceID():
    return 'KODI_' + memberID


def RequestURL():
    timestamp = int(time.time())
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    ktime = str(int(time.time()))
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
     'Accept-Encoding': 'none',
     'Accept-Language': 'en-US,en;q=0.8',
     'Connection': 'keep-alive'}
    urlL = 'http://iptvbase.net/roku_interface/3C2/0/3/BRSSPHUHANIV4KCOVA3BX6CMM2HZLDAQ/KODI_Windows-DESKTOP-IP33OE6-10-10.0.17134-x86-x86_Family_6_Model_55_Stepping_8,_GenuineIntel-' + timestamp + '.32/0/get_id/tv7633/XBMC'
    page = cRequestHandler(urlL).request()
    page = page.replace('2^3^0^0^', '"').replace('^^^0^^^~0^^', '"')
    token = re.findall('"(.*?)"', page)[0]
    url = 'http://iptvbase.net/roku_interface/3C2/0/3/' + token + '/KODI_Windows-DESKTOP-IP33OE6-10-10.0.17134-x86-x86_Family_6_Model_55_Stepping_8,_GenuineIntel-' + timestamp + '.26/0/getContentDetails/44436/relative/' + timestamp
    req = urllib2.Request(url, headers=hdr)
    r = opener.open(req)
    the_page = r.read()
    return the_page


def motvtest():
    url = RequestURL()
    name = 'r'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def encode_complex(obj):
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    raise TypeError(repr(obj) + ' is not JSON serializable')


def otvtest():
    oGui = cGui()
    datay_ur = 'http://hyfystreamz.com/radio/list.json'
    r = requests.get(datay_ur, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}, timeout=10)
    res = r.json(strict=False)
    for cat in res['CATLIST']:
        sTitle = cat['category']
        sPicture = cat['cat_img']
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sTitle)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oGui.addMovie(SITE_IDENTIFIER, 'RADIOLIVE', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def RADIOLIVE():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.radio-browser.info/webservice/json/stations/bycountry/' + cat_id
    r = requests.get(sUrl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}, timeout=10)
    liste = r.json(strict=False)
    for cat in liste:
        if cat['country'] == cat_id:
            sPicture = cat['favicon']
            sTitle = cat['name']
            stream_url = cat['url']
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', stream_url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'playRADIOlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def playRADIOlive():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Thum = oInputParameterHandler.getValue('sThumbnail')
    url = url + '|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&X-Forwarded-For=62.75.128.93'
    addLink('[COLOR lightblue][B]OTV MEDIA RADIO >>  [/B][/COLOR]' + name, url, Thum)


def decodeURL():
    oGui = cGui()
    sUrl = 'https://www.youtube.com/watch?v=Qirbpm7O3E4'
    sMovieTitle = 'Incredible Turkey in 4K (Ultra HD)'
    sHosterUrl = sUrl
    sMovieTitle = alfabekodla(sMovieTitle)
    oHoster = cHosterGui().checkHoster(sHosterUrl)
    sThumbnail = 'http://www.solidstreamz.com/geopocket/streamzdata.php'
    if oHoster != False:
        sMovieTitle = sMovieTitle
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
    oGui.setEndOfDirectory()


def bennms():
    url = 'https://dl.dropboxusercontent.com/s/zve0u4hvid4f10l/mtv_de.xml?dl=0'
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().get(url)




def decodeSourceURL(uhash):
    uhash = uhash.decode('ISO-8859-15').encode('utf-8')
    return decode(uhash)




def xor_strings(xs, ys):
    return ''.join((chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys)))


import base64

def yaz64(s):
    """Add missing padding to string and return the decoded base64 string."""
    log = logging.getLogger()
    s = str(s).strip()
    try:
        return base64.b64decode(s)
    except TypeError:
        padding = len(s) % 4
        if padding == 1:
            log.error('Invalid base64 string: {}'.format(s))
            return ''
        if padding == 2:
            s += '=='
        elif padding == 3:
            s += '='
        return base64.b64decode(s)


def yaz64(e):
    _keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    t = ''
    f = 0
    e = re.sub('[^A-Za-z0-9\\+\\/\\=]', '', e)
    while f < len(e):
        s = _keyStr.find(e[f])
        f += 1
        o = _keyStr.find(e[f]) if f < len(e) else 0
        f += 1
        u = _keyStr.find(e[f]) if f < len(e) else 0
        f += 1
        a = _keyStr.find(e[f]) if f < len(e) else 0
        f += 1
        n = s << 2 | o >> 4
        r = (o & 15) << 4 | u >> 2
        i = (u & 3) << 6 | a
        t = t + chr(n)
        if u != 64:
            t = t + chr(r)
        if a != 64:
            t = t + chr(i)

    return t


try:
    import thread
except ImportError:
    import _thread as thread

import time

def on_message(ws, message):
    print message


def on_error(ws, error):
    print error


def on_close(ws):
    print '### closed ###'


def on_open(ws):
    print 'Open'

    def run(*args):
        for i in range(3):
            time.sleep(1)

        time.sleep(1)
        ws.close()
        print 'thread terminating...'

    thread.start_new_thread(run, ())


def crypt_stream_url(encoded_url):
    data = encoded_url
    cipher_text = binascii.unhexlify(data[96:])
    decryptor = AES.new(binascii.unhexlify(data[32:96]), AES.MODE_CBC, binascii.unhexlify(data[:32]))
    return decryptor.decrypt(cipher_text).decode('utf8')




user = ''
user_id = '210210'



def aes_encrypt(result):
    key = 'sXKiC9t8dVqo15Nc'
    iv = 'cLt3Gp39O3yvW7Gw'
    sult = binascii.a2b_hex(result)
    from resources.lib import pyaes
    counter = pyaes.Counter(initial_value=100)
    aes = pyaes.AESModeOfOperationCTR(key)
    result = aes.decrypt(sult)
    return result


def getm_post_data(crya):
    _key = '7lzjr5ozbkvxglav'
    _iv = 'freccm0tnpqmoldh'
    plain = b2a_hex(crya).decode('utf-8')
    cipher = AES.new(_key, AES.MODE_CBC, iv=_iv)
    cry = cipher.decrypt(plain)
    return cry




def kuoku():
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'https://verystream.com/e/BCFvf5nU71V/'
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('Referer', 'https://filmpalast.to/stream/saphirblau')
    page = oRequest.request()
    token = re.findall('videolink">([^<]+)', page)[0]
    url = 'https://verystream.com/gettoken/' + token + '?mime=true'
    name = 'r'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def addLink(name, url, iconimage):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('Fanart_Image', iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=str(url), listitem=liz)
    xbmc.Player().play(url, liz)
    sys.exit()
    return ok


def okuoku(cba):
    oku = ''
    i = len(cba) - 1
    while i >= 0:
        oku += cba[i]
        i -= 1

    return oku


def geantsat1():
    sUrl = 'http://www.geantsat.com/free-iptv/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69',
     'Referer': 'https://www.tv8.com.tr/canli-yayin',
     'Connection': 'keep-alive',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(sUrl, headers=headers).text
    liste = re.findall('<a style="font-size: 20px;" href="(.*?)"', data, re.S)
    for Url in liste:
        return Url


def TurkishTV(s):
    kem = [ s[HEM:HEM + 3] for HEM in range(0, len(s), 3) ]
    return ''.join((chr(int(val)) for val in kem))


from urlparse import urlparse

def matvcomtr():
    oGui = cGui()
    liste = []
    liste.append(['ATV CANLI', '#EXTINF:0 tvg-name=".*?".*?>(TR:.*?)\n(.*)\n'])
    liste.append(['ATV YEDEK', 'https://canlitv.co/atv.html'])
    liste.append(['A HABER CANLI', 'http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/ahaberhd/ahaberhd.m3u8'])
    liste.append(['A SPOR CANLI', 'http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/asporhd/asporhd.m3u8'])
    liste.append(['minikaGO CANLI', 'http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/minikago/minikago.m3u8'])
    liste.append(['minikaCOCUK CANLI', 'http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/minikagococuk/minikagococuk.m3u8'])
    liste.append(['YEN\xc4\xb0 D\xc4\xb0Z\xc4\xb0LER', 'http://www.atv.com.tr/(S(w3ia53anisrqi0zawpcegfnk))/diziler'])
    liste.append(['KLAS\xc4\xb0K D\xc4\xb0Z\xc4\xb0LER', 'http://www.atv.com.tr/(S(w3ia53anisrqi0zawpcegfnk))/klasik-diziler'])
    for sTitle, sUrl2 in liste:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'PROGRAMLAR':
            oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLAS\xc4\xb0K D\xc4\xb0Z\xc4\xb0LER':
            oGui.addDir(SITE_IDENTIFIER, 'ArshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YEN\xc4\xb0 D\xc4\xb0Z\xc4\xb0LER':
            oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'D\xc4\xb0Z\xc4\xb0LER ABC':
            oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ATV YEDEK':
            oGui.addDir(SITE_IDENTIFIER, 'canlitvzoneBox', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'mplay__weebtv', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def livestreamtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://www.live-stream.tv/online/fernsehen/deutsch/arte.html'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = 'class="list-group sidebarActive">(.+?)<div id="sidenavTwitter"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)" class="list-group-item">.*?<img src="(.*?)" alt="(.*?)"'
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = alfabekodla(aEntry[2])
            sPicture = 'http://www.live-stream.tv' + str(aEntry[1])
            sUrl = str(aEntry[0])
            if 'http' not in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'PLAYlivestreamtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


from resources.lib import unwise

def PLAYlivestreamtv():
    oGui = cGui()
    UA = 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    dat = requests.get(Url).content
    urll = re.findall('<iframe src="(.*?)"', dat, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36',
     'Referer': referer}
    urlm = requests.get(urll, headers=headers).text
    urlm = urlm.replace('\r', '').replace('\\s', '').replace('\n', '').replace(';eval', 'eval').replace(';</script>', '</script>')
    TIK = '|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    urlh = re.findall('<script type="text/javascript">(eval.function.w,i,s,e.*?)</script>', urlm, re.S)[0]
    urlk = unwise.unwise_process(urlh)
    urlk = urlk.replace('//', '').replace('\r', '').replace('\\s', '').replace('\n', '').replace('; eval', 'eval')
    urln = re.findall('(\\s*eval\\s*\\(\\s*function(?:.|\\s)+?{}\\)\\))', urlk, re.S)[0]
    urlw = cPacker().unpack(urln)
    urlw = urlw.replace('\\', '')
    baseUrl = re.findall('baseUrl:"(.*?)"', urlw, re.S)[0]
    TIK = '|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25&Referer=' + referer
    url = re.findall("source:'(.*?)'", urlw, re.S)[0]
    url = url.replace('https:', 'https://').replace('http:', 'http://')
    cookie = getUrl(urll, output='cookie').result
    if url.find('akamaihd') > -1:
        url = url + '|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&X-Forwarded-For=62.75.128.93'
    else:
        url = url + '|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&Referer=' + urll
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def sshowBox3(url, name):
    name = alfabekodla(name)
    from resources.lib.hlsplayer import hlsproxy
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying = threading.Event()
    _bitrate = 0
    f4m_proxy = hlsproxy()
    stopPlaying.clear()
    runningthread = thread.start_new_thread(f4m_proxy.start, (stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype = 'HLS'
    progress.update(20, '', 'Loading local proxy', '')
    url_to_play = f4m_proxy.prepare_url(url, proxy, use_proxy_for_chunks, maxbitrate=maxbitrate, simpleDownloader=simpleDownloader, auth=auth, streamtype=streamtype, swf=swf, callbackpath=callbackpath, callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name, path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return (url_to_play, listitem)
    mplayer = MyPlayer()
    mplayer.stopPlaying = stopPlaying
    progress.close()
    mplayer.play(url_to_play, listitem)
    firstTime = True
    played = False
    while True:
        if stopPlaying.isSet():
            break
        if xbmc.Player().isPlaying():
            played = True
        xbmc.log('Sleeping...')
        xbmc.sleep(200)

    print 'Job done'
    return played


class MyPlayer(xbmc.Player):

    def __init__(self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player().play(url, listitem)

    def onPlayBackEnded(self):
        print 'seting event in onPlayBackEnded '
        self.stopPlaying.set()
        print 'stop Event is SET'

    def onPlayBackStopped(self):
        print 'seting event in onPlayBackStopped '
        self.stopPlaying.set()
        print 'stop Event is SET'


def _m3u8Exit(self):
    import otv_kuresel
    otv_kuresel.yt_tmp_storage_dirty = True


class mmMyPlayer(xbmc.Player):

    def __init__(self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player().play(url, listitem)

    def onPlayBackEnded(self):
        print 'seting event in onPlayBackEnded '
        self.stopPlaying.set()
        print 'stop Event is SET'

    def onPlayBackStopped(self):
        print 'seting event in onPlayBackStopped '
        self.stopPlaying.set()
        print 'stop Event is SET'


def root(url):
    try:
        url = base64.b64decode(url)
        return url
    except:
        pass


enc = ''

def _m3u8Exit(url):
    return url


url1 = 'PXdXYjQ1Q1praDJMbWxUTTI4V2NrbFdadzRXY25KRE52TTNMdDkyWXVRbmJsUm5idk5tY2xOWGQ0OW1ZdzltY2s1Q2JrOXlMNk1IYzBSSGE='
url2 = base64.b64decode(url1)
url3 = okuoku(url2)
streamurl = base64.b64decode(url3)

def weebtv():
    oGui = cGui()
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().root()


def hextranslate(s):
    res = ''
    for i in range(len(s) / 2):
        realIdx = i * 2
        res = res + chr(int(s[realIdx:realIdx + 2], 16))

    return res


def app_login(url, username = '', password = '', app_id = 'dce89f12-ac16-4262-9489-df5e0434b86e'):
    login_data = json.dumps({'username': username,
     'password': password})
    r = s.post(url, data=login_data, headers={'Content-Type': 'application/json'})
    return r


def StartPort(url):
    app_id = 'dce89f12-ac16-4262-9489-df5e0434b86e'
    headers = {'app_id': 'dce89f12-ac16-4262-9489-df5e0434b86e',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:63.0) Gecko/20100101 Firefox/63.0'}
    data = requests.session().get(url, headers=headers).text
    return data


def aes_dec(result):
    try:
        from resources.lib.modules import pyaes
        aes = pyaes.AESModeOfOperationOFB(control.key, iv=control.iv)
        result = aes.decrypt(result.decode('string-escape'))
        return result
    except:
        return result


def Swift15(url):
    link = url.replace('#Swift2', '') + ''
    token_url = 'http://uygulama14.club/token/tivibuadrenalin.php?channel_desc=0_1'
    headers = {'Referer': 'http://uygulama14.club/',
     'User-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:63.0) Gecko/20100101 Firefox/63.0'}
    req = urllib2.Request(token_url, None, headers)
    post = {'id': '247',
     'channel_desc': '0_1'}
    post = urllib.urlencode(post)
    html = _get(req, post)
    agent = 'User-Agent=Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G935F Build/LMY48Z)'
    media_url = link + html + '|' + agent.encode('utf-8')
    return media_url


def kmmdecodeURL():
    urlm = 'http://mike.ruby.pt:4554/mercury/bein1tr/playlist.m3u8'
    url = strftime('n/j/Y g:i:s A', gmtime())
    name = 'test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def maddLink(name, url, iconimage):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=str(url), listitem=liz)
    xbmc.Player().play(url, liz)
    sys.exit()
    return ok

def orhatvturk():
    oGui = cGui()
   

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('kanald_com_tr', 'turkTV', 'T\xc3\xbcrk TV', 'diziler.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '28')
    oGui.addDir('Swift', 'list_channels', 'T\xc3\xbcrk IPTV', 'turkey-free-iptv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.sporizle1.pw')
    oGui.addDir('xiptvozel', 'rakiptv', 'T\xc3\xbcrk IPTV 2', 'turkey-free-iptv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'rmootatam', 'T\xc3\xbcrk VE AZ TV HD', 'turkazeri.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('diziizle_net', 'turkdizi', 'T\xc3\xbcrk Dizi', 'diziler.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://')
    oGui.addDir('turkvod_org', 'TUrKVod', 'TUrKVod-T\xc3\xbcrk Sinema,Dizi', 'turksiemalar.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('canlifm_com', 'Radyo', 'T\xc3\xbcrk Radyo', 'trradyo.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    

def turksinema():
    oGui = cGui()
   

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('turkfilmleri_org', 'turkfilmleri', 'Türk Filmleri', 'turksiemalar.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '28')
    oGui.addDir('bicaps_net', 'bicaps', 'Full HD Film izlesene', 'fulhdfilm.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('fullhd4kfilmizle', 'hd4kfilmizle', 'Indirmeden Film Izle', 'indirmedenfilmizle1.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('hdfilmcehennemi_com', 'hdfilmcehennemi', 'Hdfilmcehennemi', 'hdfilmcehennemi1.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('filmakinesi_org', 'filmakinesi', 'FilMakinesi', 'filmakinesi.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('jetfilmizle_biz', 'jetfilmizle', 'Jetfilmizle', 'jetfilmizle.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('filmifullizle_org', 'filmifullizle', 'FilmiFullizle', 'fulhdfilm.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
                                                                         

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
            sTitle = alfabekodla(sTitle)
            catid = cat['stream']
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('siteUr', catid)
            oGui.addMovie(SITE_IDENTIFIER, 'mplay__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        sTitle = cat['name']
        sTitle ='stream-2-'+ sTitle
        sTitle = alfabekodla(sTitle)
        cati= cat['streams2']
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', cati)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
        oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory()

def mplay__():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url =oInputParameterHandler.getValue('siteUr')
    
    name = oInputParameterHandler.getValue('sMovieTitle')
    
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,Url,'')

def play__():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    
    sUrl = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,sUrl,'')
                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok
def PLAYtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Header = 'User-Agent=VLC/3.0.6 LibVLC/3.0.6'
    sUrl = sUrl + '|' + Header
    sTitle = alfabekodla(sTitle)
    cHosterGui().addLink(sTitle, sUrl, '')


def Taraftar2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    import requests, json
    open = requests.get(sUrl, headers={'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.3.1; WT19M-FI Build/JLS36I)'}).text
    json = json.loads(open)
    js = json['LIVETV']
    for a in js:
        name = a['category_name']
        catid = a['cid']
        icon = a['category_image']
        name = alfabekodla(name)
        if 'tipo' in sUrl:
            url = 'http://tipo.bestaway.club//api/get_latest_channels?api_key=okba75fn00dE5ZqQk1dHWZEf82r2pYyWO2bbjTMbBnvTv'
            sPicture = 'http://tipo.bestaway.club/images/' + icon
        if 'film' in sUrl:
            url = 'http://film.bestaway.club//api/get_latest_channels?api_key=okba75fn00dE5ZqQk1dHWZEf82r2pYyWO2bbjTMbBnvTv/40='
            sPicture = 'http://film.bestaway.club/images/' + icon
        if 'dizi' in sUrl:
            url = 'http://dizi.bestaway.club//api/get_latest_channels?api_key=okba75fn00dE5ZqQk1dHWZEf82r2pYyWO2bbjTMbBnvTv/40='
            sPicture = 'http://dizi.bestaway.club/images/' + icon
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(name))
        oOutputParameterHandler.addParameter('siteUrl', url)
        oOutputParameterHandler.addParameter('catid', catid)
        oGui.addMovie(SITE_IDENTIFIER, 'Taraftar3', name, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def Taraftar3():
    oGui = cGui()
    import json, requests
    import requests, json, urllib
    oInputParameterHandler = cInputParameterHandler()
    caturl = oInputParameterHandler.getValue('siteUrl')
    cat_id = oInputParameterHandler.getValue('catid')
    js = requests.session().get(caturl, headers={'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.3.1; WT19M-FI Build/JLS36I)'}).text
    js = js.replace('\\/', '/')
    liste = re.findall('"id":(.*?),"cat_id":%s,"channel_title":"(.*?)","channel_user":"(.*?)","channel_pass":"(.*?)","token_link":"(.*?)","channel_resim":"(.*?)","channel_url":"(.*?)","channel_thumbnail":".*?","channel_desc":".*?","cid":.*?,".*?","category_image":".*?"' % cat_id, js, re.S)
    for id, name, user, pas, token, icon, url in liste:
        sPicture = icon
        sTitle = alfabekodla(name)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', url)
        oOutputParameterHandler.addParameter('user', user)
        oOutputParameterHandler.addParameter('pass', pas)
        oOutputParameterHandler.addParameter('token', token)
        if 'vk.com' in url:
            oGui.addMovie(SITE_IDENTIFIER, 'uygulama2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'playlist.m3u8' in url:
            oGui.addMovie(SITE_IDENTIFIER, 'Swift', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'vk.com' in url:
            oGui.addMovie(SITE_IDENTIFIER, 'playuygulama', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'vk.com' in url:
            oGui.addMovie(SITE_IDENTIFIER, 'tv8canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'SwiftLive' in url:
            oGui.addMovie(SITE_IDENTIFIER, 'playuygulama', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
            oGui.addMovie(SITE_IDENTIFIER, 'playuygulama', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def Swift():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    agent = 'User-Agent=Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G935F Build/LMY48Z)'
    sUrl = url + lahasha + '|' + agent.encode('utf-8')
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()


def uygulama6():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Url = 'http://uygulama14.club/token/vip/bein3.php' + lahasha
    js = requests.session().get(Url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}).text
    js = js.replace('\\/', '/')
    liste = re.findall('"url":".*?playlist.m3u8(.*?)"', js, re.S)[0]
    sUrl = sUrl + liste + '|User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.15 Safari/537.36'
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()


def uygulama2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = 'http://uygulama14.club/token/vip/bein3.php' + lahasha
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    js = requests.session().get(Url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}).text
    js = js.replace('\\/', '/')
    liste = re.findall('"url":".*?playlist.m3u8(.*?)"', js, re.S)[0]
    sUrl = 'http://s1.turkcast.club:8081/calaninanasinisikeyim/bein1/playlist.m3u8' + liste + '|User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.15 Safari/537.36'
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()


def playuygulama():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl') + lahasha
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    js = requests.session().get(Url, headers={'Acceptt': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}).text
    js = js.replace('\\/', '/')
    liste = re.findall('"url":"(.*?)"', js, re.S)[0]
    sUrl = liste + '|User-Agent=Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F)'
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()




def addinstall():
    oGui = cGui()
    liste = []
    liste.append(['Istall LIVE NET TV1', 'otvlivetv3'])
    liste.append(['Istall Urlresolver 5.0.36', 'urlresolver-5.0.36'])
    for sTitle, url in liste:
        sPicture = 'http://www.stickpng.com/assets/images/586abf73b6fc1117b60b2754.png'
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url)
        if sTitle == 'KINO FILME':
            oGui.addMovie(SITE_IDENTIFIER, 'almanKINO', sTitle, sPicture, sPicture, '<fanart>http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif</fanart>', oOutputParameterHandler)
        elif sTitle == 'TV SENDER':
            oGui.addMovie(SITE_IDENTIFIER, 'Almanlivestream', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'RADIO':
            oGui.addMovie(SITE_IDENTIFIER, 'radiode', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'ADULT':
            oGui.addMovie(SITE_IDENTIFIER, 'pincode', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
            oGui.addMovie(SITE_IDENTIFIER, 'Oinstall', sTitle, 'http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif', 'http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif', '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def Taraftar():
    oGui = cGui()
    liste = []
    liste.append(['Canli TV Izle', 'http://tipo.bestaway.club//api/get_category?api_key=okba75fn00dE5ZqQk1dHWZEf82r2pYyWO2bbjTMbBnvTv', 'https://lh6.ggpht.com/oRC2FbooV1AM_CzYXld6WS0UNmmILRDVmE30zRcNjDsxgFX-Qrz_Z-ks9P3MCteWMg=h1080'])
    liste.append(['Film Izle', 'http://film.bestaway.club//api/get_category?api_key=c3sbB6K0yVc2GFH/GJ3tjiVu/40=', 'http://www.nekadarizlendi.com/wp-content/uploads/2017/02/Ekran-Resmi-2017-02-19-11.50.16.png'])
    liste.append(['Dizi Izle', 'http://dizi.bestaway.club//api/get_category?api_key=c3sbB6K0yVc2GFH/GJ3tjiVu/40=', 'https://pbs.twimg.com/profile_images/543610023973097472/lEtD1thL.png'])
    for sTitle, url, sPicture in liste:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url)
        if sTitle == 'KINO FILME':
            oGui.addMovie(SITE_IDENTIFIER, 'almanKINO', sTitle, sPicture, sPicture, '<fanart>http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif</fanart>', oOutputParameterHandler)
        elif sTitle == 'TV SENDER':
            oGui.addMovie(SITE_IDENTIFIER, 'Almanlivestream', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'RADIO':
            oGui.addMovie(SITE_IDENTIFIER, 'radiode', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'ADULT':
            oGui.addMovie(SITE_IDENTIFIER, 'pincode', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
            oGui.addMovie(SITE_IDENTIFIER, 'Taraftar2', sTitle, 'http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif', 'http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif', '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def xkaraoketr():
    oGui = cGui()
    from youtubecom_tr import KARAOKEturk
    KARAOKEturk()
    oGui.setEndOfDirectory()


def orhantvalman():
    oGui = cGui()
   

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'AlmanKINO', 'KINO FILME', 'filmkino.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', '28')
    oGui.addDir('liveonlinetv247', 'Almanlivestream', 'TV SENDER', 'worldiptv.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')

    oGui.addDir('radio_de', 'radiode', 'RADIO', 'bradio.jpg', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir('adult_eu', 'pincode', 'ADULT', 'sexyfrau.jpg', oOutputParameterHandler)

   
    oGui.setEndOfDirectory()

   
def AlmanKINO():
        oGui = cGui()
        url = 'https://dl.dropboxusercontent.com/s/6narqajjhg46meh/otvmain.txt'
        content = cRequestHandler(url).request()
        cont= re.findall("ASITE_IDENTIFIER = '(.*?)'SITE_NAME = '(.*?)'SITE_ICON = '(.*?)'",content, re.S)
        for urls,NAME,sPicture in cont:

             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
             oGui.addDir(urls, 'load',NAME, sPicture, oOutputParameterHandler)
        oGui.setEndOfDirectory()	


def testzest():        
#   from default import  pparseUrl
   oInputParameterHandler = cInputParameterHandler()
   sSiteName = oInputParameterHandler.getValue('siteUrl')
   plugins = __import__('resources.sayfalar.%s' % sSiteName, fromlist=[sSiteName])
   function = getattr(plugins, 'load')
   function()                                                                                         

def regex_from_to(text, from_string, to_string, excluding = True):
    import re, string
    if excluding:
        try:
            r = re.search('(?i)' + from_string + '([\\S\\s]+?)' + to_string, text).group(1)
        except:
            r = ''

    else:
        try:
            r = re.search('(?i)(' + from_string + '[\\S\\s]+?' + to_string + ')', text).group(1)
        except:
            r = ''

    return r


def regex_get_all(text, start_with, end_with):
    import re, string
    r = re.findall('(?i)(' + start_with + '[\\S\\s]+?' + end_with + ')', text)
    return r


def tv8canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sHosterUrl = sUrl
    sMovieTitle = alfabekodla(sMovieTitle)
    oHoster = cHosterGui().checkHoster(sHosterUrl)
    if oHoster != False:
        sMovieTitle = sMovieTitle
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
    oGui.setEndOfDirectory()


def OPEN_URL(url):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    link = requests.session().get(url, headers=headers, verify=False).text
    link = link.encode('ascii', 'ignore')
    return link


def addDir(name, url, mode, iconimage, fanart, description):
    import xbmcgui, xbmcplugin, urllib, sys
    u = sys.argv[0] + '?url=' + url + '&mode=' + str(mode) + '&name=' + urllib.quote_plus(name) + '&iconimage=' + urllib.quote_plus(iconimage) + '&description=' + urllib.quote_plus(description)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage='DefaultFolder.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name,
     'Plot': description})
    liz.setProperty('fanart_image', fanart)
    if mode == 102 or mode == 9999 or mode == 99999 or mode == 10:
        liz.setProperty('IsPlayable', 'true')
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
    else:
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok