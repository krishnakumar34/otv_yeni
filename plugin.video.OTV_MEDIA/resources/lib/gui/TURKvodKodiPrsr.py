# -*- coding: utf-8 -*-

from resources.sites.LIVETV2 import *
oParser = cParser()
import re
import os
import base64
import sys
import time
import os.path                
try:
    import ssl
    import socket
    timeout = 30
    socket.setdefaulttimeout(timeout)
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
except ImportError:
    pass
try:
    import json
    import math
    import httplib
except:
    pass
kodi = False

PY3 = False

try:
    import http.cookiejar as cookielib
    from urllib.parse import urlencode as Urlencode
    from urllib.parse import quote_plus as Quote_plus
    from urllib.parse import unquote as Unquote
    from urllib.parse import quote as Quote
    from urllib.parse import urlparse as Urlparse
    from urllib.parse import urljoin as Urljoin
    from urllib.parse import parse_qsl as Parse_qsl
    from urllib.parse import parse_qs as Parse_qs
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.request import HTTPCookieProcessor
    from urllib.request import build_opener
    from urllib.request import HTTPBasicAuthHandler
    from urllib.request import HTTPHandler
    from urllib.request import install_opener
    PY3 = True; unicode = str; unichr = chr; long = int; xrange = range
except:
    import cookielib
    from urllib import urlencode as Urlencode
    from urllib import quote_plus as Quote_plus
    from urllib import unquote as Unquote
    from urllib import quote as Quote
    from urlparse import urlparse as Urlparse
    from urlparse import urljoin as Urljoin
    from urlparse import parse_qsl as Parse_qsl
    from urlparse import parse_qs as Parse_qs
    from urllib2 import Request
    from urllib2 import urlopen
    from urllib2 import HTTPCookieProcessor
    from urllib2 import build_opener
    from urllib2 import HTTPBasicAuthHandler
    from urllib2 import HTTPHandler
    from urllib2 import install_opener

try:
    from Components.config import config
    scrty = config.plugins.TURKVOD.security_key.value
except:
    pass

scr="=0Te0J3Yz9Dco+BnLytGb0N3Ll5+Was52buQ+2b2tmc1R3LvoDc0RHa"   
sys.path.append('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod')


VER = '12.28'
UA = 'Mozilla/5.0 TURKvod-10'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
HEADERS = {"User-Agent":FF_USER_AGENT}

def to_utf8(dct):
    if isinstance(dct, dict):
        return dict((to_utf8(key), to_utf8(value)) for key, value in dct.items())
    elif isinstance(dct, list):
        return [to_utf8(element) for element in dct]
    elif isinstance(dct, unicode):
        dct = dct.encode("utf8")
        if PY3: dct = dct.decode("utf8")
        return dct
    elif PY3 and isinstance(dct, bytes):
        return dct.decode('utf-8')
    else:
        return dct
        
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
        
    
def decoder(data, fn):
    if PY3: 
        data = (to_utf8(base64.b64decode(data)))
    else:
        data = base64.b64decode(data)
    secretKey = {}
    url = ''
    temp = ''
    if not PY3:
        tempData = ''
        for i in xrange(len(data)):
            tempData += ("%" + format(ord(data[i]), '02x'))
        data =  Unquote(tempData)
    x = 0
    while x < 256:
        secretKey[x] = x
        x += 1
    y = 0
    x = 0
    while x < 256:
        y = (y + secretKey[x] + ord(fn[x % len(fn)])) % 256
        temp = secretKey[x]
        secretKey[x] = secretKey[y]
        secretKey[y] = temp
        x += 1
    x = 0
    y = 0
    i = 0
    if PY3: 
        while i < len(data):
            x = (x + 1) % 256
            y = (y + secretKey[x]) % 256
            temp = secretKey[x]
            secretKey[x] = secretKey[y]
            secretKey[y] = temp
            url += (chr(ord(data[i]) ^ secretKey[(secretKey[x] + secretKey[y]) % 256]))
            i += 1
        return url
    else: 
        while i < len(data.decode('utf-8')):
            x = (x + 1) % 256
            y = (y + secretKey[x]) % 256
            temp = secretKey[x]
            secretKey[x] = secretKey[y]
            secretKey[y] = temp
            url += (chr(ord(data.decode('utf-8')[i]) ^ secretKey[(secretKey[x] + secretKey[y]) % 256]))
            i += 1
        return url
    
def decodeur1(Html):
    from ast import literal_eval
    vl = re.search('var *(_\w+) *= *(\[[^;]+\]);', Html, re.DOTALL)
    if vl:
        var_name = vl.group(1)
        list_b64 = vl.group(2)
        start = Html.find(list_b64)
        Html = Html[start:]
        list_b64 = literal_eval(list_b64)
        nrvr = re.search(var_name + ',(0x\w+)\)*; *var *([^=]+) *=', Html, re.DOTALL)
        if nrvr:
            number_ref = int(nrvr.group(1),16)
            var_ref = nrvr.group(2)

            i = 0
            while i < number_ref:
                list_b64.append(list_b64.pop(0))
                i += 1
            test2 = re.findall("(?:;|;}\(\)\);)sources(.+?)};", Html, re.DOTALL)
            if test2:
                url = ''
                movieID = ''
                qua_list = []
                for page in test2:
                    tableau = {}
                    data = page.find("={")
                    if data != -1:
                        Html = page[data:]
                        if Html:
                            i = 0
                            vname = ''
                            for i in xrange(len(Html)):
                                fisrt_r = re.match("([^']+)':", Html, re.DOTALL)
                                if fisrt_r:
                                    vname = fisrt_r.group(1)
                                    tableau[vname] = 'null'
                                    index = len(fisrt_r.group()[:-1])
                                    Html = Html[index:]
                                whats = re.match("[:+]'([^']+)'", Html, re.DOTALL)
                                if whats:
                                    if vname:
                                        ln = tableau[vname]
                                        if not ln == 'null':
                                            tableau[vname] = tableau[vname] + whats.group(1)
                                        else:
                                            tableau[vname] = whats.group(1)
                                    index = len(whats.group(0))
                                    Html = Html[index:]
                                else:
                                    whats = re.match("\+*" + var_ref + "\(\'([^']+)\' *, *\'([^']+)\'\)", Html, re.DOTALL)
                                    if whats:
                                        if vname:
                                            ln = tableau[vname]
                                            if not ln == 'null':
                                                tableau[vname] = tableau[vname] + decoder(list_b64[int(whats.group(1), 16)], whats.group(2))
                                            else:
                                                tableau[vname] = decoder(list_b64[int(whats.group(1), 16)], whats.group(2))
                                        index = len(whats.group(0))
                                        Html = Html[index:]
                                if not whats:
                                    Html = Html[1:]
                                    
                        if tableau:
                            langFre = True
                            qual = ''
                            for i, j in tableau.items():
                                if j.startswith('http') and j.endswith('com'):
                                    url = tableau[i] if not tableau[i] in url else url
                                    continue
                                if len(i) == 5 and len(j) >= 10 and j.isalnum() and not 'video' in j:
                                    movieID = j if not j in movieID else movieID
                                    continue
                                if len(test2) > 1:
                                    if j == 'eng':
                                        langFre = False
                                if j == '360' or j == '480' or j == '720' or j == '1080':
                                    qual = j
                            if langFre and qual and qual not in qua_list:
                                qua_list.append(qual)
                qua_list.sort()
                url_list = []
                for qual in qua_list:
                    url_list.append("{}/{}/{}/0/video.mp4".format(url, movieID, qual))
                return qua_list, url_list
        
class cPacker():
    def detect(self, source):
        """Detects whether `source` is P.A.C.K.E.R. coded."""
        return source.replace(' ', '').startswith('eval(function(p,a,c,k,e,')

    def unpack(self, source):
        """Unpacks P.A.C.K.E.R. packed js code."""
        payload, symtab, radix, count = self._filterargs(source)

        if count != len(symtab):
            raise UnpackingError('Malformed p.a.c.k.e.r. symtab.')
        
        try:
            unbase = Unbaser(radix)
        except TypeError:
            raise UnpackingError('Unknown p.a.c.k.e.r. encoding.')

        def lookup(match):
            """Look up symbols in the synthetic symtab."""
            word  = match.group(0)
            if PY3:
                if "ğ" in word or "ü" in word or "ş" in word or "ı" in word or "ö" in word or "ç" in word or "Ğ" in word or "Ü" in word or "Ş" in word or "İ" in word or "Ö" in word or "Ç" in word:
                    pass
                else:    
                    return symtab[unbase(word)] or word
            else:
                return symtab[unbase(word)] or word
                
        source = re.sub(r'\b\w+\b', lookup, payload)
        return self._replacestrings(source)

    def _cleanstr(self, str):
        str = str.strip()
        if str.find("function") == 0:
            pattern = (r"=\"([^\"]+).*}\s*\((\d+)\)")
            args = re.search(pattern, str, re.DOTALL)
            if args:
                a = args.groups()
                def openload_re(match):
                    c = match.group(0)
                    b = ord(c) + int(a[1])
                    return chr(b if (90 if c <= "Z" else 122) >= b else b - 26)

                str = re.sub(r"[a-zA-Z]", openload_re, a[0]);
                str = Unquote(str)

        elif str.find("decodeURIComponent") == 0:
            str = re.sub(r"(^decodeURIComponent\s*\(\s*('|\"))|(('|\")\s*\)$)", "", str);
            str = Unquote(str)
        elif str.find("\"") == 0:
            str = re.sub(r"(^\")|(\"$)|(\".*?\")", "", str);
        elif str.find("'") == 0:
            str = re.sub(r"(^')|('$)|('.*?')", "", str);

        return str

    def _filterargs(self, source):
        """Juice from a source file the four args needed by decoder."""
        
        source = source.replace(',[],',',0,')

        juicer = (r"}\s*\(\s*(.*?)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*\((.*?)\).split\((.*?)\)")
        args = re.search(juicer, source, re.DOTALL)
        if args:
            a = args.groups()
            try:
                return self._cleanstr(a[0]), self._cleanstr(a[3]).split(self._cleanstr(a[4])), int(a[1]), int(a[2])
            except ValueError:
                raise UnpackingError('Corrupted p.a.c.k.e.r. data.')

        juicer = (r"}\('(.*)', *(\d+), *(\d+), *'(.*)'\.split\('(.*?)'\)")
        args = re.search(juicer, source, re.DOTALL)
        if args:
            a = args.groups()
            try:
                return a[0], a[3].split(a[4]), int(a[1]), int(a[2])
            except ValueError:
                raise UnpackingError('Corrupted p.a.c.k.e.r. data.')

        # could not find a satisfying regex
        raise UnpackingError('Could not make sense of p.a.c.k.e.r data (unexpected code structure)')



    def _replacestrings(self, source):
        """Strip string lookup table (list) and replace values in source."""
        match = re.search(r'var *(_\w+)\=\["(.*?)"\];', source, re.DOTALL)

        if match:
            varname, strings = match.groups()
            startpoint = len(match.group(0))
            lookup = strings.split('","')
            variable = '%s[%%d]' % varname
            for index, value in enumerate(lookup):
                source = source.replace(variable % index, '"%s"' % value)
            return source[startpoint:]
        return source
        
def UnpackingError(Exception):
    #Badly packed source or general error.#
    #xbmc.log(str(Exception))
    print (Exception)
    pass

class Unbaser(object):
    """Functor for a given base. Will efficiently convert
    strings to natural numbers."""
    ALPHABET = {
        62: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        95: (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             '[\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
    }

    def __init__(self, base):
        self.base = base
        
        #Error not possible, use 36 by defaut
        if base == 0 :
            base = 36
        
        # If base can be handled by int() builtin, let it do it for us
        if 2 <= base <= 36:
            self.unbase = lambda string: int(string, base)
        else:
            if base < 62:
                self.ALPHABET[base] = self.ALPHABET[62][0:base]
            elif 62 < base < 95:
                self.ALPHABET[base] = self.ALPHABET[95][0:base]
            # Build conversion dictionary cache
            try:
                self.dictionary = dict((cipher, index) for index, cipher in enumerate(self.ALPHABET[base]))
            except KeyError:
                raise TypeError('Unsupported base encoding.')

            self.unbase = self._dictunbaser

    def __call__(self, string):
        return self.unbase(string)

    def _dictunbaser(self, string):
        """Decodes a  value to an integer."""
        ret = 0
        
        for index, cipher in enumerate(string[::-1]):
            ret += (self.base ** index) * self.dictionary[cipher]
        return ret

def mtr_buyuk(metin):
    metin = metin.replace('%09','').replace('ç','C').replace('i','I').replace('ı','I').replace('ğ','G').replace('ö','O').replace('ş','S').replace('ü','U').replace('İ','I')
    metin = metin.replace('u00e7','C').replace('u0131','I').replace('u011f','G').replace('u00f6','O').replace('u015f','S').replace('u00fc','U').replace('u0130','I').replace('u00c7','C').replace('u011e','G').replace('u00d6','O').replace('u015e','S').replace('u00dc','U')
    metin = metin.replace('&#8217;',"'").replace('&#8220;',"(").replace('&#8221;',")").replace('&#8230;',"...").replace('&#8211;',"-").replace('&#038;',"&")
    metin = metin.upper()
    return metin
    
def tr_clear(metin):
    metin = metin.replace('&#8217;',"'").replace('&#8220;',"(").replace('&#8221;',")").replace('&#8230;',"...").replace('&#8211;',"-").replace('&#038;',"&")
    return metin
             
       
def buyuk_clear(url):              
    logger.info("Json: %s" % url)
    cookie = getUrl(url, output='cookie').result
    oRequest = cRequestHandler(url)
    oRequest.addHeaderEntry('Cookie', cookie)
#    oRequest.addHeaderEntry('Accept', '*/*')
#    oRequest.addHeaderEntry('Accept-Encoding', 'gzip, deflate, br')
#    oRequest.addHeaderEntry('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7')
#    oRequest.addHeaderEntry('Connection', 'keep-alive')

    oRequest.addHeaderEntry('Origin', 'https://yabancidizi.pw')
    oRequest.addHeaderEntry('Referer', 'https://yabancidizi.pw')
    oRequest.addHeaderEntry('Sec-Fetch-Dest', 'document')
    oRequest.addHeaderEntry('Sec-Fetch-Mode', 'navigate')
    oRequest.addHeaderEntry('Sec-Fetch-Site', 'same-origin')
    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
    url = oRequest.request()
    ggetpage(object)
    logger.info("Json: %s" % url)
    return Json 



class getpage(object):
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
    def __init__(self, url, close = True, post = None, mobile = False, referer = None, cookie = None, output = '', timeout = '10'):
    
        if output == 'cookie' or output == 'kukili' or not close == True:
            cookie_handler = HTTPCookieProcessor(cookielib.LWPCookieJar())
            opener = build_opener(cookie_handler, HTTPBasicAuthHandler(), HTTPHandler())
            opener = install_opener(opener)
        if not post == None:
            post = Urlencode(post)
            request = Request(url, post)
        else:
            request = Request(url, None)
        if '720pizle' in url or 'bolumd' in url:
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
            request.add_header('Accept', '*/*')
            request.add_header('Accept-Language', 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3')
            request.add_header('Connection', 'keep-alive')
            request.add_header('X-Requested-With', 'XMLHttpRequest')
        else:
            request.add_header('User-Agent', UA)
        if not referer == None:
            request.add_header('Referer', referer)
        if not cookie == None:
            request.add_header('cookie', cookie)
        response = urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = str(response.headers.get('Set-Cookie'))
        elif output == 'kukili':
            if PY3:
                result = to_utf8(response.read()) + 'kuki :' + str(response.headers.get('Set-Cookie'))
            else:
                result = response.read() + 'kuki :' + str(response.headers.get('Set-Cookie'))
        elif output == 'geturl':
            result = response.geturl()
        elif output == 'lenght':
            result = str(response.headers.get('Content-Length'))
        else:
            result = response.read()
        if PY3:
            result = to_utf8(result)
        if close == True:
            response.close()
        self.result = result
     




def getstlkr(url, mac, token):
    try:
        ref = re.findall('(https?://[^/]+/)', url, re.IGNORECASE)[0]
    except:
        ref = url
    headers = { "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG250 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
        "Referer": ref,
        "Accept-Language": "en-US,*",
        "Accept-Charset": "UTF-8,*;q=0.8",
        "X-User-Agent": "Model: MAG250; Link: Ethernet",
        "Authorization": "Bearer "+token,
        "Cookie": "mac="+Quote(mac)+"; stb_lang=en; timezone=Europe%2FParis",
        "Connection": "Keep-Alive"}
    req = Request(url, None, headers)
    response = urlopen(req)
    page = response.read()
    response.close()
    return page    

            

	
class modules():

    def __init__(self):
        self.video_liste = [] 
        self.next_page_url = ''
        self.next_page_text = ''
        self.prev_page_url = ''
        self.prev_page_text = ''
        self.search_text = ''
        self.video_liste 
        self.error = ''
#	self.playlistname= '' 
                  			
    def reset_buttons(self):
        self.next_page_url = None
        self.next_page_text = ''
        self.prev_page_url = None
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = None
    def get_categories3(self, url, pattern,titlen,urln,imgn=False, sonraki=None):
        o = Urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        img = None
        try:                 
            page = getHtml(url)#.replace("\t",'').replace("\n",'')
            logger.info("get_categories3: %s" %page)
            video_list_temp = []
            chan_counter = 1
#            new = (chan_counter,  None, None, None, 'TRModules@' + domain + '@category@** EN SON EKLENENLER **', None, None, None, None, None)
#            video_list_temp.append(new)
            aResult= oParser.parse( page,pattern)
            for aEntry in aResult[1]:
                title = aEntry[titlen] 
                url = aEntry[urln]
                if url.startswith("/") or not url.startswith("http"):
                   url = domain + url
                img = aEntry[imgn]
                if img.startswith("/"):
                   img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url, 'TRModules@' + url + '@category3@' + title, None, img, None, None, None)
                video_list_temp.append(chan_tulpe)
            self.prev_page_url = ''
            self.prev_page_text = ''
            try:
                s_sayfa = re.findall(sonraki, page)
                next = s_sayfa[0]
                if next.startswith("/"):
                    next = domain + next
                if len(next):
                    self.next_page_url = 'TRModules@' + next + '@start@'
                    self.next_page_text = 'SONRAKI'
                    chan_counter += 1
                    chan_tulpe = (chan_counter, '>> Sonraki sayfa >>', None, None, url, 'TRModules@' + next + '@start@' + title, None, img, None, None, None)
                    video_list_temp.append(chan_tulpe)
            except:
                self.next_page_url = ''
                self.next_page_text = ''
            if len(video_list_temp) < 1:
                print ('ERROR CAT LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_categories')
		


    def get_categories2(self, url, pattern,titlen,urln,imgn=False, sonraki=None):
        o = Urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        img = None
        try:                 
            page = getHtml(url)#.replace("\t",'').replace("\n",'')
            logger.info("get_categories2: %s" %page)
            video_list_temp = []
            chan_counter = 1
#            new = (chan_counter,  None, None, None, 'TRModules@' + domain + '@category@** EN SON EKLENENLER **', None, None, None, None, None)
#            video_list_temp.append(new)
            aResult= oParser.parse( page,pattern)
            for aEntry in aResult[1]:
                title = aEntry[titlen] 
                url = aEntry[urln]
                if url.startswith("/") or not url.startswith("http"):
                   url = domain + url
                img = aEntry[imgn]
                if img.startswith("/"):
                   img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url, 'TRModules@' + url + '@category2@' + title, None, img, None, None, None)
                video_list_temp.append(chan_tulpe)
            self.prev_page_url = ''
            self.prev_page_text = ''
            try:
                s_sayfa = re.findall(sonraki, page)
                next = s_sayfa[0]
                if next.startswith("/"):
                    next = domain + next
                if len(next):
                    self.next_page_url = 'TRModules@' + next + '@start@'
                    self.next_page_text = 'SONRAKI'
                    chan_counter += 1
                    chan_tulpe = (chan_counter, '>> Sonraki sayfa >>', None, None, url, 'TRModules@' + next + '@start@' + title, None, img, None, None, None)
                    video_list_temp.append(chan_tulpe)
            except:
                self.next_page_url = ''
                self.next_page_text = ''
            if len(video_list_temp) < 1:
                print ('ERROR CAT LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_categories')
		
    def get_categories(self, url, pattern,titlen,urln,imgn=False, sonraki=None):
        o = Urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        img = None
        try:                 
            page = getHtml(url)#.replace("\t",'').replace("\n",'')
            logger.info("get_categories: %s" %page)
            video_list_temp = []
            chan_counter = 1
#            new = (chan_counter,  None, None, None, 'TRModules@' + domain + '@category@** EN SON EKLENENLER **', None, None, None, None, None)
#            video_list_temp.append(new)
            aResult= oParser.parse( page,pattern)
            for aEntry in aResult[1]:
                title = aEntry[titlen] 
                url = aEntry[urln]
                if url.startswith("/") or not url.startswith("http"):
                   url = domain + url
                img = aEntry[imgn]
                if img.startswith("/"):
                   img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url, 'TRModules@' + url + '@category@' + title, None, img, None, None, None)
                video_list_temp.append(chan_tulpe)
            self.prev_page_url = ''
            self.prev_page_text = ''
            try:
                s_sayfa = re.findall(sonraki, page)
                next = s_sayfa[0]
                if next.startswith("/"):
                    next = domain + next
                if len(next):
                    self.next_page_url = 'TRModules@' + next + '@start@'
                    self.next_page_text = 'SONRAKI'
                    chan_counter += 1
                    chan_tulpe = (chan_counter, '>> Sonraki sayfa >>', None, None, url, 'TRModules@' + next + '@start@' + title, None, img, None, None, None)
                    video_list_temp.append(chan_tulpe)
            except:
                self.next_page_url = ''
                self.next_page_text = ''
            if len(video_list_temp) < 1:
                print ('ERROR CAT LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_categories')
    def get_films(self,url, pattern_1, pattern_2,titlen,urln, imgn, sonraki=None):
        o = Urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        logger.info("TURKVODPARSER  url: %s" % url)
        try:        
            img = None
            subj = ""
            imdb = ""
            secton = "film"
            if "fullhdfilmizlesene" in url or "koreanturk" in url or "dizigold" in url or "dizimag" in url  or "filmmakinesi" in url or "dizilab" in url:
                secton = "parts"
            if url =="https://dizimag.biz/":
                page = ""
                for a in range(1, 5):
                    data = Urlencode({"page": a, "type":"yabanci"})
                    if PY3:
                        data = data.encode('ascii')
                    host = "https://dizimag.biz/ajax/more_series"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "*/*",
                        "Referer": url,
                        "Content-Type": "application/x-www-form-Urlencoded",
                        "X-Requested-With": "XMLHttpRequest"}
                    req = Request(host, data , headers)
                    response = urlopen(req)
                    html = response.read()
                    html = html.replace('\\','')
                    if PY3:
                        html = to_utf8(html)
                    page = page+html
            else:
                page = getHtml(url)
                
            video_list_temp = []
            chan_counter = 0
            if pattern_2=='' or re.search(pattern_1, page):    
                pattern = pattern_1
            else:
                pattern = pattern_2
            
            aResult = oParser.parse(page,pattern) # finditer
            for aEntry in aResult[1]:
 
                title =  aEntry[titlen]
              
               # subj = aEntry[subjn]
                 
                #imdb = aEntry[imdbn]
                 
                url = aEntry[urln]
                if url.startswith("/") or not url.startswith("http"):
                   url = domain + url
                
                img = aEntry[imgn]
                if img.startswith("/") or not img.startswith("http") :
                   img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, imdb+' - '+subj, None, None, 'TRModules@' + url + '@'+secton+'@' + title, None,  img, '',  None,  None)
                video_list_temp.append(chan_tulpe)
            try:        
                s_sayfa = re.findall(sonraki, page)
                next = s_sayfa[0]
                if next.startswith("/"):
                    next = domain + next
                if len(next):
                    self.next_page_url = 'TRModules@' + next + '@category@' + self.playlist_cat_name
                    self.next_page_text = 'SONRAKI'
                    chan_counter += 1
                    chan_tulpe = (chan_counter, '>> Sonraki sayfa >>', None, None, url, 'TRModules@' + next + '@category@' + title, None, img, None, None, None)
                    video_list_temp.append(chan_tulpe)
            except:
                pass
            self.prev_page_url = 'TRModules@' + domain + '@start@KATEGORILER'
            self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_films')
		

    def bget_films(self, url, pattern_1, pattern_2,titlen,urln, imgn,imdbn, sonraki=None):
            logger.info("TURKVODPARSER url: %s" %url)
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
                logger.info("TURKVODPARSER  img : %s" % img)
            
            
    def get_sezon(self, url, pattern):
        o = Urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        try:        
            img = None
            subj = ""
            imdb = ""
            page = getHtml(url).replace("\t",'').replace("\n",'')
            video_list_temp = []
            chan_counter = 0
            films_regex = re.finditer(pattern, page) # finditer
            for text in films_regex:
                if "(?P<title>" in pattern :  
                    title = text.group('title')
                if "(?P<subj>" in pattern :  
                    subj = tr_clear(text.group('subj'))
                if "(?P<imdb>" in pattern :  
                    imdb = 'IMDB: ' + text.group('imdb')
                if "(?P<url>" in pattern :  
                    url = text.group('url')
                    if url.startswith("/"):
                        url = domain + url
                if "(?P<img>" in pattern :  
                    img = text.group('img')
                    if img.startswith("/"):
                        img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, imdb+' - '+subj, None, None, 'TRModules@' + url + '@category@' + title, None,  img, '',  None,  None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_sezon')
            
    def get_stlkr(self, url):
        try:        
            portal_url, mac = re.findall('stlkr::url=(.*?)::mac=(.*?)$', url, re.IGNORECASE)[0]
            stlkr='==QPjFWbmYHdp1TZwlHdmsmbpx2XlRXYlJ3Y942bpR3Yh9DcoBnLkF2bs9iclZnclN3L'
            headers = {"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                "X-User-Agent": "Model: MAG250; Link: WiFi",
                "Authorization": "Bearer ",
                "Cookie": "PHPSESSID=null; sn=""; mac="+mac+"; stb_lang=en; timezone=Europe/Vilnius"}
            url2 = portal_url + base64.b64decode(stlkr[::-1]) + mac
            req = Request(url2,None,headers)
            response = urlopen(req)
            html = response.read()
            response.close()
            html = html.replace('\\','')
            if PY3:
                html = to_utf8(html)
            tkn = re.findall (r'(https?://.*?/)(.*?)/(.*?)/', html, re.IGNORECASE)[0]
            url = tkn[0] + 'get.php?username='+tkn[1]+'&password='+tkn[2]+'&type=m3u'
            title = self.playlistname
            video_list_temp = [('1', 'LISTEYI AL : E2', None, None, None, 'TURKvodModul@'+ url +'@m3u@TURKvod', None, None, None, None, None), ('2', 'LISTEYI AL : KODI', None, None, None, url, None, None, None, None, None)]
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
            
    def get_stl_kr(self, portal_url, mac):
        try:
            url = portal_url + "/portal.php?type=stb&action=handshake&token=&JsHttpRequest=1-xml%20HTTP/1.1"
            page = getstlkr(url, mac, token="")
            if PY3:
                page = to_utf8(page)
            page = page.replace('\\','')
            token = re.findall('"token":"([^"]+)"', page)[0]
            url = portal_url + "/portal.php?type=stb&action=get_profile&hd=1&num_banks=2&not_valid_token=0&auth_second_step=0&video_out=hdmi&client_type=STB&hw_version_2=3b7bd02430f7662d653d0788ac44981ad04e5126&metrics=%7B%22mac%22%3A%22"+Quote(mac)+"%22%2C%22sn%22%3A%227A9DF81D76388%22%2C%22type%22%3A%22stb%22%2C%22model%22%3A%22MAG250%22%2C%22uid%22%3A%2212746ec5a8c99fd74a29882cc5bf408c9389f1bd451ed2c05b32d4d06a22d026%22%7D&JsHttpRequest=1-xml%20HTTP/1.1";
            page = getstlkr(url, mac, token)
            if PY3:
                page = to_utf8(page)
            page = page.replace('\\','')
            login = ""
            password = ""
            login, password = re.findall('\"login\":\"(|[^\"]+)\",(?:|\\s+)\"password\":\"(|[^\"]+)\"', page, re.IGNORECASE)[0]
            if not login:
                login = ""
            if not password:
                password = ""
            video_list_temp = []
            chan_counter = 0
            url = portal_url + "/portal.php?type=itv&action=get_genres&login="+login+"&password="+password+"JsHttpRequest=1-xml";
            page = getstlkr(url, mac, token)
            if PY3:
                page = to_utf8(page)
            page = page.replace('\\','')
            url = portal_url + "/portal.php?type=vod&action=get_categories&login="+login+"&password="+password+"JsHttpRequest=1-xml";
            page2 = getstlkr(url, mac, token)
            if PY3:
                page2 = to_utf8(page2)
            page2 = page2.replace('\\','')
            cat_regex = re.findall('"id":"(\d+)","title":"([^"]+)"', page)
            for text in cat_regex:
                title = text[1]
                url = "stlkr::itv::portal_url="+portal_url+"::mac="+mac+"::token="+token+"::login="+login+"::password="+password+"::cat="+text[0]+"::pg=1"
                chan_counter += 1
                if 'ADULT' in title or 'XXX' in title:
                    chan_tulpe = (chan_counter, 'TV : '+title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None,  'protected', None)
                else:
                    chan_tulpe = (chan_counter, 'TV : '+title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            cat_regex = re.findall('"id":"(\d+)","title":"([^"]+)"', page2)
            for text in cat_regex:
                title = text[1]
                url = "stlkr::vod::portal_url="+portal_url+"::mac="+mac+"::token="+token+"::login="+login+"::password="+password+"::cat="+text[0]+"::pg=1"
                chan_counter += 1
                if 'ADULT' in title or 'XXX' in title:
                    chan_tulpe = (chan_counter, 'VOD : '+title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None, 'protected', None)
                else:
                    chan_tulpe = (chan_counter, 'VOD : '+title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            self.next_page_url = ''
            self.next_page_text = ''
            self.prev_page_url = ''
            self.prev_page_text = ''
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
            
    def get_stl_kr_link(self, url):
        try:
            login = ""
            password = ""
            portal_url, mac, token, login, password, cat, pg = re.findall('portal_url=(.*?)::mac=(.*?)::token=(.*?)::login=(|[^:]+)::password=(|[^:]+)::cat=(.*?)::pg=(.*?)$', url)[0]
            if not login:
                login = ""
            if not password:
                password = ""
            if '::itv::' in url:
                page=""
                for a in range(1, 100):
                    pg = str(a)
                    url2 = portal_url + "/portal.php?type=itv&action=get_ordered_list&genre=" + cat + "&force_ch_link_check=&fav=0&sortby=number&hd=0&p=" + pg + "&from_ch_id=0&login=" + login + "&password=" + password + "&JsHttpRequest=1-xml";
                    sayfa = getstlkr(url2, mac, token)
                    if PY3:
                        sayfa = to_utf8(sayfa)
                    page = page+sayfa
                    if '"id"' not in sayfa:
                        break
            if '::vod::' in url:
                url2 = portal_url + "/portal.php?type=vod&action=get_ordered_list&category=" + cat + "&force_ch_link_check=&fav=0&sortby=number&hd=0&p="+pg+"&from_ch_id=0&login=" + login + "&password=" + password + "&JsHttpRequest=1-xml";
                page = getstlkr(url2, mac, token)
            if PY3:
                page = to_utf8(page)
            page = page.replace('\\','')
            video_list_temp = []
            chan_counter = 0
            if '::itv::' in url:
                tur = "itv"
                cat_regex = re.findall('"name":"([^"]+)".*?"url":".*?(//[^"]+)"', page)
            if '::vod::' in url:
                tur = "vod"
                cat_regex = re.findall('"name":"([^"]+)".*?"cmd":"([^"]+)"', page)
            for text in cat_regex:
                title = text[0]
                cmd = text[1]
                url3 = "stlkr::portal_url="+portal_url+"::mac="+mac+"::token="+token+"::login="+login+"::password="+password+"::name="+text[0]+"::cmd="+cmd+"::tur="+tur
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url3, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if '::vod::' in url:
                pg = int(pg)
                pg += 1
                pg = str(pg)
                url4 = "stlkr::vod::portal_url="+portal_url+"::mac="+mac+"::token="+token+"::login="+login+"::password="+password+"::cat="+cat+"::pg="+pg
                chan_counter += 1
                chan_tulpe = (chan_counter, "Sonraki sayfa  >>", None, None, None,'TRModules@' + url4 + '@parts@' + "Sonraki", None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
            
    def get_parts(self, url, ilk_pattern, parts_pattern):
        o = Urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        try:
            page = getHtml(url)
            video_list_temp = []
            chan_counter = 1	
            if ilk_pattern !='':
                ilk_parca = re.findall(ilk_pattern, page)
                title = ilk_parca[0].replace("DBX PRO","DIZIBOX PRO")
                ilk = (chan_counter, title, None,  None, None,  'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(ilk)
            parts_regex = re.finditer(parts_pattern, page)
            for text in parts_regex:
                if "(?P<title>" in parts_pattern :  
                    title = text.group('title').upper()
                if "(?P<url>" in parts_pattern :  
                    url = text.group('url')
                    if url.startswith("/"):
                        url = domain + url
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_parts')
				
    def get_videos(self, url, pattern):
        try:
            page = getHtml(url)
            video_list_temp = []
            chan_counter = 0
            vid_link = re.finditer(pattern, page)
            for text in vid_link:
                title = self.playlistname
                if "(?P<title>" in pattern :  
                    title = text.group('title').upper()
                if "(?P<url>" in pattern :  
                    url = text.group('url')
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
    def get_videos_base_u(self, url, pattern_1):
        try:
            page = getHtml(url)
            video_list_temp = []
            chan_counter = 0
            video_link = re.findall(pattern_1, page)
            link = decode_base64(video_link[0])
            if 'youtube' in link:
                url = re.findall('["\'](https://www.youtube.com/embed/.*?)["\']', link, re.IGNORECASE)[0]
                title = 'YOUTUBE FRAGMAN'
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif 'rapidrame' in link:
                link = re.findall('(https://rapidrame.com/embed.*?)["\']', link, re.IGNORECASE)[0]
                link = link.replace('.html','').replace('embed?','embed-')+".html"
                title = 'RAPIDRAME'
                url = link+'::ref::'+url
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif '/player/embed' in link:
                link = re.findall('(https://[^/]+/player/embed.*?)["\']', link, re.IGNORECASE)[0]
                title = 'RAPIDRAME'
                url = link+'::ref::'+url
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif 'fireplayer' in link:
                link = re.findall('(https://[^/]+/fireplayer.*?)["\']', link, re.IGNORECASE)[0]
                title = 'FAST PLAYER'
                url = link+'::ref::'+url
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif '/player/' in link:
                link = re.findall('(https://[^/]+/player.*?)["\']', link, re.IGNORECASE)[0]
                title = 'STREAM+'
                url = 'hdfcdn::'+link+'::ref::'+url
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif 'p4p.php' in link:
                url = 'cdnstreamcdn::' + re.findall('src=["\'](.*?)["\']', link, re.IGNORECASE)[0]
                title = 'HDF PLAYER'
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif 'vidmoly' in link:
                url = re.findall('src=["\'](.*?)["\']', link, re.IGNORECASE)[0]
                title = 'VIDMOLY PLAYER'
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            else:
                uri, key = re.findall('(https://.*?/).*?(?:key|id)=(.*?)"', link, re.IGNORECASE)[0]
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                            'Connection': 'keep-alive',
                            'Referer': url,
                            'X-Requested-With': 'XMLHttpRequest'}
                data = ""
                if PY3:
                    data = data.encode('ascii')                
                url2 = uri + 'initPlayer/' + key
                req = Request(url2, data , headers)
                response = urlopen(req)
                html = response.read()
                if PY3:
                    html = to_utf8(html)
                availablePlayers = re.findall('"availablePlayers":\[(.*?)\]', html, re.IGNORECASE)[0]
                vid_link = re.findall('"(.*?)"', availablePlayers)
                for text in vid_link:
                    chan_counter += 1			
                    url = 'VanLongStream::'+uri + 'getDataPlayer/'+text+'/'+key
                    title = text.upper()
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
		
    def get_videos_parse_fullhdfilmizlesene(self, url):
        try:
            page = getHtml(url)
            video_list_temp = []
            chan_counter = 0
            vid_link = re.findall('"vidid":"([^"]+)","name":"([^"]+)","nameTxt":"([^"]+)".*?"tx":(\d),', page)
            for text in vid_link:
                vidid = text[0]
                name = text[1]
                nameTxt = text[2].upper()
                if text[3]=='2':
                    chan_counter += 1			
                    chan_tulpe = (chan_counter, nameTxt+' - TR', None, None, 'fullhdfilmizlesene_parse:https://www.fullhdfilmizlesene.com/player/api.php?id='+vidid+'&type=t&name='+name+'&get=video&pno=tr&format=json&ssl=true', None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
                    chan_counter += 1			
                    chan_tulpe = (chan_counter, nameTxt+' - ENG', None, None, 'fullhdfilmizlesene_parse:https://www.fullhdfilmizlesene.com/player/api.php?id='+vidid+'&type=t&name='+name+'&get=video&pno=en&format=json&ssl=true', None, None, None, None, None, None)					
                    video_list_temp.append(chan_tulpe)
                else:
                    chan_counter += 1			
                    chan_tulpe = (chan_counter, nameTxt, None, None, 'fullhdfilmizlesene_parse:https://www.fullhdfilmizlesene.com/player/api.php?id='+vidid+'&type=t&name='+name+'&get=video&format=json&ssl=true', None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
        
    def get_videos_decodedlink(self, url, ilk_pattern, parts_pattern,titlen,urln):
        o = Urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        try:
            page = getHtml(url)
            video_list_temp = []
            chan_counter = 1	
            if ilk_pattern !='':
                ilk_parca = re.findall(ilk_pattern, page)
                title = ilk_parca[0]
                url = 'decodedlink:' + url
                ilk = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(ilk)
            aResult = oParser.parse(page, parts_pattern) # finditer
            for aEntry in aResult[1]:
                title =  aEntry[titlen]
                url = aEntry[urln]
                if url.startswith("/"):
                        url = domain + url
                url = 'decodedlink:' + url
                chan_counter += 1
                if "FRAGMAN" in title:
                    url = re.findall('(https://www.youtube.com/embed/.*?)["\'\?\s]', page, re.IGNORECASE)[0]
                chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_parts')

    def get_videos_posted(self, url, pattern):
        ref = url
        try:
            page = getHtml(url)
            video_list_temp = []
            chan_counter = 0
            if re.search('youtube.com/embed', page):
                url = re.findall('["\'](https://www.youtube.com/embed/.*?)["\'\?]', page, re.IGNORECASE)[0]
                title = 'YOUTUBE FRAGMAN'
                you = ('1', title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(you)
            if re.search('\?player=', page):
                vid_link = re.findall(pattern, page)
                for text in vid_link:
                    chan_counter += 1			
                    host = text[0]
                    url = 'posted720plink:host:'+host+':ref:'+ref
                    title = text[1].upper()
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
            
    def get_parts_dizigold(self, url):
        ref = url
        try:
            page = getHtml(url)            
            video_list_temp = []
            chan_counter = 0
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
            host, id, dil, sezon_id = re.findall('var url = "([^"]+)";\s+var view_id="([^"]+)";\s+var dil="([^"]+)"[\s\S]*?var sezon_id="([^"]+)"', page, re.IGNORECASE)[0]
            data = Urlencode({"id": id, "dil": dil, "sezon_id": sezon_id, "tip": "view"})
            if PY3:
                data = data.encode('ascii')            
            req = Request(host, data, headers)
            response = urlopen(req)
            html = response.read() 
            response.close()
            if PY3:
                html = to_utf8(html)            
            html = html.replace('\\','').replace('u0130','I')
            video_list_temp = []
            chan_counter = 0
            vid_link = re.findall('{"trigger":(\d+),"lang":"([^"]+)".*?ame":"([^"]+)"}', html)
            for text in vid_link:
                chan_counter += 1			
                url = "https://player.dizigold1.net/?id="+id+"&s="+text[0]+"&dil="+text[1]+"&ref="+text[2].lower().replace(" ","-")
                title = text[2]
                chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
            
    def get_dizibox_videos(self, url):
        try:
            page = getHtml(url)
            if re.search('(https://\S+stream/embed/[^"]+)"', page):
                url = re.findall('(https://\S+stream/embed/[^"]+)"', page)[0]
                html = getHtml(url)
                url = re.findall('(http\S+m3u8)', html)[0]
            if re.search('https://www.dizibox.vip/player/', page):
                host = re.findall('(https://www.dizibox.vip/player/[^"]+)"', page)
                link = host[0]
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
                    "Referer": url,
                    "Cookie": "__cfduid=d5fac8fa030aaff09b894708499adcbb11603354312; dbxu=1603371662338; _ga=GA1.2.1787408769.1603354316; _gid=GA1.2.520492925.1603354316; __cf_bm=e1e0ec4734bfbea0383332bfcefcc809918b1c09-1603370992-1800-AYq8dWK1tmW/VbQ3AvPFXC/oC36nHYRsKKbhfFvfl1IxPfOhkN/KKwrsAI1VWgr6ogKW68ylmtzm+EVN5BwQg0qimJCWEVcJTH8QN0Dsnkjmfff6OUbFusG4d5MlBm9zf8YEplIZ0tI0ADrE/IPSBlw=; isTrustedUser=true; _gat=1",
                    }
                req = Request(link, None, headers)
                response = urlopen(req)
                html = response.read() 
                response.close()
                if PY3:
                    html = to_utf8(html)            
                if re.search('atob\(unescape\("([^"]+)"', html):
                    txx = re.findall('atob\(unescape\("([^"]+)"', html)
                    hexx = decode_base64(Unquote(txx[0]))
                    if PY3:
                        hexx = to_utf8(hexx)                    
                    moly = re.findall('(https://vidmoly\S+/embed[^"]+)"', hexx)
                    url = moly[0]
                if re.search('<iframe src="([^"]+)"', html):
                    txx = re.findall('<iframe src="([^"]+)"', html)
                    url = txx[0]
                if re.search('file"?: ?"[^"]+"', html):
                    txx = re.findall('file"?: ?"([^"]+)"', html)
                    url = txx[0]
                    if 'indifiles' in url:
                        url = txx[0] + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0&Referer=' + link
            title = self.playlistname
            video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')

    def get_dizimag_videos(self, url):
        try:
            page = getHtml(url)
            link = re.findall('(https://dizimag.biz/videoapi/[^"]+)', page)[0]
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "Referer": url}
            req = Request(link, None, headers)
            response = urlopen(req)
            html = response.read() 
            response.close()
            if PY3:
                html = to_utf8(html)
            id_links = re.findall('"part_id":"(\d+)"', html)
            video_list_temp = []
            chan_counter = 0
            for id in id_links:
                chan_counter += 1			
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "*/*",
                    "Referer": link,
                    "Content-Type": "application/x-www-form-Urlencoded",
                    "X-Requested-With": "XMLHttpRequest"}
                host = 'https://dizimag.biz/videoapipost'
                data = Urlencode({"id": id})
                if PY3:
                    data = data.encode('ascii')                
                req = Request(host, data, headers)
                response = urlopen(req)
                html2 = response.read() 
                response.close()
                if PY3:
                    html2 = to_utf8(html2)
                html2 = html2.replace('\\','')
                if re.search('"iframe":"(http[^"]+)"', html2):
                    link2 = re.findall('"iframe":"(http[^"]+)"', html2)[0]
                    url = link2
                    title = "LINK " + str(chan_counter)
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')

    def get_dizilab_videos(self, url):
        try:
            page = getHtml(url)
            id_links = re.findall("loadVideo\('([^']+)'", page)
            video_list_temp = []
            chan_counter = 0
            for vid in id_links:
                chan_counter += 1			
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
                    "Referer": 'dizilab.pw',
                    "X-Requested-With": "XMLHttpRequest"}
                host = 'https://dizilab.pw/request/php/'
                data = Urlencode({"vid": vid, "tip": "0", "type": "loadVideo"})
                if PY3:
                    data = data.encode('ascii')                
                req = Request(host, data, headers)
                response = urlopen(req)
                html2 = response.read()
                response.close()
                if PY3:
                    html2 = to_utf8(html2)
                html2 = html2.replace('\\','')
                url2 = re.findall('src="(.*?)"', html2)[0]
                html3 = page = getpage(url2).result
                if re.search('sources', html3):
                    link2, kalite = re.findall('file"?:"([^"]+)","?label"?:"([^"]+)"', html3, re.IGNORECASE)[0]
                    url = link2 + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0&Referer='+url2
                    title = kalite
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
                      
    def get_filmmodu_videos(self, url):
        try:
            page = getHtml(url)
            url1 = re.findall("videoId = '(.*?)'", page)[0]
            url2 = re.findall("videoType = '(.*?)'", page)[0]
            urli ='https://www.filmmodu.org/get-source?movie_id='+url1+'&type='+url2
            pag = getpage(urli).result
            id_links = re.findall('"src":"(.*?)","withCredentials":true,"label":"(.*?)"', pag)
            video_list_temp = []
            chan_counter = 0
            for url ,title in id_links:
                chan_counter += 1			
                chan_tulpe = (chan_counter, title, None,  None, None,  'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')
    def get_yabancidizi_parts(self, url):
        try:
            page = getHtml(url)
            ref = url
            id_links = re.findall('data-eid="([^"]+)" data-type="([^"]+)".*?</i>(?P<title>[^<]+)</a>', page)
            video_list_temp = []
            chan_counter = 0
            for vid in id_links:
                chan_counter += 1			
                url = ref+"::"+vid[1]+"::"+vid[0]
                title = vid[2]
                chan_tulpe = (chan_counter, title, None,  None, None,  'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')


    def get_yabancidizi_videos(self, url):
        try:
            ref, lang, episode = re.findall('(http.*?)::(.*?)::(.*?)$', url, re.IGNORECASE)[0]
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': '*/*',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': ref}
            host = 'https://yabancidizi.pw/ajax/service'
            data = Urlencode({"lang": lang, "episode": episode, "type": "langTab"})
            if PY3:
                data = data.encode('ascii')                
            req = Request(host, data, headers)
            response = urlopen(req)
            page = response.read()
            response.close()
            if PY3:
                page = to_utf8(page)
            page = page.replace('\\','')
            id_links = re.findall('data-hash="([^"]+)" data-link="([^"]+)" data-eid="[^"]+" data-querytype="alternate">([^<]+)<', page)
            video_list_temp = []
            chan_counter = 0
            for vid in id_links:
                chan_counter += 1			
                url = "yabancidizi::"+ref+"::"+vid[1]+"::"+vid[0]
                title = vid[2]
                chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')

            
    def mget_bolumd_videos(self, url):
        try:
            url = url.replace("//izle","/izle")
            host, id = re.findall('(https?://[^/]+)/izle/(\d+)/', url, re.IGNORECASE)[0]
            url = "http://www.bolumd.info/embed/"+id
            headers = {'User-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G935F Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36', 'Connection': 'Close', 'Referer': url}
            req = Request(url, None , headers)
            response = urlopen(req)
            html = response.read()
            if PY3:
                html = to_utf8(html)
            if re.search('source src="', html):
                url = re.findall('source src="([^"]+)"', html, re.IGNORECASE)[0]
            else:
                headers = {'User-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G935F Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36', 
                    'Referer': url,
                    'Accept': '*/*',
                    'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection': 'keep-alive',
                    'X-Requested-With': 'com.bolumd.app2'}
                req = Request(id_links, None , headers)
                response = urlopen(req)
                html = response.read()
                if PY3:
                    html = to_utf8(html)
                url = re.findall('source src="([^"]+)"', html, re.IGNORECASE)[0]
            title = self.playlistname
            video_list_temp = [('1', "PLAY", None, None, url, None, None, None, None, None, None)]
            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')




    def get_bolumd_videos(self, url):
        
            page = getHtml(url)
            
            html = re.findall('<iframe id="video_embed_code" src="([^"]+)"', page, re.IGNORECASE)[0]            
            logger.info("get_bolumd_videos -html: %s" %html)
            pag =getHtml(html) 
            pag=pag.replace("\t",'').replace("\n",'')
 
            oParser = cParser()                                                         
            sPattern1 = '<source src="(.*?)"'
            aResult = oParser.parse(pag, sPattern1)
            if (aResult[0] == True):
               #url = aResult[1][0]
               logger.info("get_bolumd_videos -1: %s" %aResult[1][0])
               title = self.playlistname
               name='[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + title
               from resources.sites import LIVETV2 
               LIVETV2.addLink(name,  aResult[1][0], '')
               



#            video_list_temp = [('1', "PLAY", None, None, url, None, None, None, None, None, None)]
#            if len(video_list_temp) < 1:
#               logger.info('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            
    def get_list(self, url):
        self.reset_buttons()
        video_list_temp = []
        parts = url.split('@')
        url = parts[0]
        section = parts[1]
        name = parts[2]
		
        if url.find("720pizle") > -1:
            if section == 'start':
                self.playlistname = name
                titlen =1 
                urln =0
               
                pattern = '<li class="oval">.*?<a href="(.*?)" title=".*?".*?</span>(.*?)</a>'
                self.video_liste = self.get_categories(url, pattern,titlen,urln)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<div class="film-kategori-resim">.*?<a href="(.*?)" title="(.*?)">.*?<img src="(.*?)"'
                pattern_2 = ''
                sonraki = 'href="(?P<next>[^"]+)"(?: title="|>)Sonraki'
                titlen =1 
                urln =0
                imgn=2
                self.video_liste = self.get_films(url, pattern_1, pattern_2,titlen,urln,imgn, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = 'https://www.(youtube).com/embed/'
                parts_pattern = '<a href="(?P<url>(https://720pizle[^/]+)?/izle/(?P<title>[^/]+)/[^"]+)"'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)				
            if section == 'parts':
                self.playlistname = name
                #host = 'https://720p-izle.com/api/dataEmbed3.asp'
                #pattern = 'data-id="([^"]+)">([^<]+)<b class="alternatifrip"'
                pattern = '<a href="(https://720pizle[^/]+/izle[^"]+)" class="text-small">\s+(\S+)\s+<'
                self.video_liste = self.get_videos_posted(url, pattern)
            return self.video_liste

        if url.find("dizibox") > -1:
            if section == 'start':
                self.playlistname = name
                titlen =1 
                urln =1
                pattern = '<a href="(?P<url>.*?)" class="alphabetical-category-link" title="(?P<title>[^<]+)">'
                self.video_liste = self.get_categories2(url, pattern,titlen,urln)
            if section == 'category2':
#                <a title="A Christmas Carol izle" href="https://www.dizibox.vip/diziler/a-christmas-carol/"><i class="icon icon-angle-right"></i>        
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                logger.info("category2-name: %s" % name)
                logger.info("category2-url: %s" % url)
                 
                pattern = '<a title="(%s.*?)" href="(.*?)"><i class="icon icon-angle-right"></i>.*?</a></li>'% (name)
                titlen =0                  
                urln =1                         
                ern = 'https://www.dizibox.vip'
                self.video_liste = self.get_categories3(ern, pattern,titlen,urln)
            if section == 'category3':
#                <a title="A Christmas Carol izle" href="https://www.dizibox.vip/diziler/a-christmas-carol/"><i class="icon icon-angle-right"></i>        
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                logger.info("category2-name: %s" % name)
                logger.info("category2-url: %s" % url)
                           
                pattern = "<a href='(.*?)' class='btn btn-s btn-default-ligh.*?'>(.*?Sez.*?)</a>"
                titlen =1                  
                urln =0                                                                                                                   
                ern = 'https://www.dizibox.vip'
                self.video_liste = self.get_categories(url, pattern,titlen,urln)
                
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<div class="post-title">.*?<a href="(.*?)" class="season-episode link-unstyled full-width">(.*?)</a>'
                pattern_2 = ''
                sonraki = "href=[\"'](?P<next>[^\"']+)[\"'] class=[\"']next[\"']>"
                titlen =1 
                urln =0
                imgn=0
                self.video_liste = self.get_films(url, pattern_1, pattern_2,titlen,urln,imgn, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = "selected='selected'>([^<]+)<"
                parts_pattern = "<option value='(?P<url>[^<']*)'>(?P<title>[^<]+)</option>"
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_dizibox_videos(url)
            return self.video_liste

        if url.find("dizilab") > -1:
            if section == 'start':
                if url == "https://dizilab.pw/":
                    url = "https://dizilab.pw/arsiv?tur=&orderby=ad&yil=&ulke=&order=ASC"
                self.playlistname = name
                sonraki = 'class="active"><a href="[^"]+">\d+</a></li><li class=""><a href="([^"]+)"'
                pattern = 'class="tv-series-single">\s+<a href="(?P<url>[^"]+)" class="film-image">\s+<img src="[^"]+" alt="(?P<title>[^"]+)"'
                self.video_liste = self.get_categories(url, pattern, sonraki)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<li id="\d+" class="[^"]+">\s+(<span[^>]+></span>\s+)?<a href="(?P<url>https://dizilab.pw/(?P<title>[^"]+))">\s+<img width="\d+" height="\d+" src="(?P<img>[^"]+)"'
                pattern_2 = '(?:<a class="episode" |<div class="tv-series-single">\s+)href="(?P<url>https://dizilab.pw/(?P<title>[^"]+))"'
                self.video_liste = self.get_films(url, pattern_1, pattern_2)
            if section == 'film':
                self.playlistname = name
                page = getHtml(url)
                if 'class="active">' not in page:
                    self.playlistname = name
                    self.video_liste = self.get_dizilab_videos(url)
                else:
                    ilk_pattern = 'class="active">\s+<a href="[^"]+">\s+<span class="[^"]+"></span>\s+([^<]+)</a>'
                    parts_pattern = 'class="">\s+<a href="(?P<url>[^"]+)">\s+<span class="[^"]+"></span>\s+(?P<title>[^<]+)</a>'
                    self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_dizilab_videos(url)
            return self.video_liste

        if url.find("dizimag") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = '<a href="(?P<url>.*?)" title="(?P<title>.*?)" class="'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<a href="?(?P<url>https?://dizimag[^/]+/(?P<title>[^"\s]+))(?:\s|").*?(?P<img>https://dizimag[^/]+/dizi/img[^"\s]+)'
                pattern_2 = 'href="(?P<url>[^"]+)" style="[^"]+">(?P<title>[^<]+)<span class="gizle">'
                self.video_liste = self.get_films(url, pattern_1, pattern_2)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_dizimag_videos(url)
            return self.video_liste
                     
        if url.find("filmmodu") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = '<li><a title="(?P<title>[^"]+)" href="(?P<url>[^>"]+)">[^"]+</a></li>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = 'col-xs-6 movie">[\s\S]*?<a href="(?P<url>[^>"]+)">(?P<title>[^<]+)</a>[\s\S]*?<img class="img-responsive" src="(?P<img>[^"]+)"'
                pattern_2 = ''
                sonraki = 'href="([^"]+)">Sonraki'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = ''
                parts_pattern ='<a href="(?P<url>[^>"]+)" type="button" class=".*?dropdown-toggle">\s+(?P<title>[^<]+)</a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_filmmodu_videos(url)
            return self.video_liste
            
        if url.find("filmmakinesi") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.*?"><a href=(.*?) data-wpel-link=internal>(.*?)</a>'
                titlen =1 
                urln =0
                self.video_liste = self.get_categories(url, pattern,titlen,urln)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                         #  
                pattern_1 = '<article class="post-.*?".*?<a href=(.*?) rel=bookmark title="(.*?)" data-wpel-link=internal>.*?data-src=(.*?) class=lazyload[\s\S]*?' 	
                pattern_2 = ''  
                sonraki ='href=(?P<next>\S+)(?:" | )rel="?next'
                titlen =1 
                urln =0
                imgn=2
                imdbn=3
                logger.info("category: %s" %url)
                self.video_liste = self.get_films(url, pattern_1, pattern_2,titlen,urln,imgn, sonraki)
            if section == 'parts':
                self.playlistname = name
                ilk_pattern = '<span>(.*?)</span> <a href='
                parts_pattern = '<a href=(https://filmmakinesi.pw/.*?) class=post-page-numbers data-wpel-link=internal><span>(.*?)</span></a>'
#<a href=https://filmmakinesi.pw/seytanin-gunlugu-izle-2015.html/2 class=post-page-numbers data-wpel-link=internal><span>Tek VidMoly</span></a> 
#<a href=https://filmmakinesi.pw/seytanin-gunlugu-izle-2015.html/3 class=post-page-numbers data-wpel-link=internal><span>Fragman</span></a>
                titlen =1 
                urln =0
                self.video_liste = self.get_videos_decodedlink(url, ilk_pattern, parts_pattern,titlen,urln)
            return self.video_liste
                               #<a href=https://filmmakinesi.pw/seytanin-gunlugu-izle-2015.html/2 class=post-page-numbers data-wpel-link=internal><span>Tek VidMoly</span>
        if url.find("fullhdfilmizlesene") > -1:
            if section == 'start':
                self.playlistname = name
                
                pattern = '<li><a href="(?P<url>https://www.fullhdfilmizlesene.com/(?:filmizle|yil)[^"]+)"[^>]+>(?P<title>[^<]+)</a></li>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<li>(?:|\s+)<img (?:|src="[^"]+" data-)src="(?P<img>[^"]+)" alt="(?P<title>[^"]+)" width="[^"]+" height="[^"]+" class="afis[\s\S]*?<a href="(?P<url>[^"]+)"[\s\S]*?<span>IMDB(?P<imdb>[^<]+)</span>'
                pattern_2 = ''
                sonraki = "class='ileri'><a href='(?P<next>[^']+)'"
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_videos_parse_fullhdfilmizlesene(url)
            return self.video_liste
        
        if url.find("hdfilmcehennemi") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = '<a class="nav-link.*?href="?(?P<url>(?:|https?://[^/]+)/(?:dil|tur|yil)/[^"\s>]+)(?:|[^>]+)>(?P<title>[^<]+)</a>'
                titlen =1 
                urln =0
                self.video_liste = self.get_categories(url, pattern,titlen,urln)
            if section == 'category':                                                                                       
                self.playlist_cat_name = name                                                          
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<div class="col-6 col-sm-3 poster-container px-2 px-sm-1 mb-3 mb-sm-2">.*?<a href="(.*?)".*?<img.*?data-src="(.*?)" alt="(.*?)"'
                pattern_2 = ''
                sonraki = '<a class="page-link" href="#">.*?</a></li><li class="page-item"><a href="?(?P<next>[^">\s]+)"?'
                titlen =2  
                urln =0
                imgn=1
                imdbn=4
                subjn=1
                self.video_liste = self.get_films(url, pattern_1, pattern_2,titlen,urln,imgn, sonraki)
            if section == 'film':
                self.playlistname = name                
   
                  
 
                ilk_pattern = '<a class="nav-link.*?href="?(?P<url>[^">]+)">(?:|\s+)<svg xmlns=".*?"/></svg>\s+(?P<title>[^<]+)\s+</a>'
                parts_pattern = '<a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#videoModal" data-trailer="?(?P<url>[^">]+)"><svg xmlns=".*?"/></svg>(?P<title>[^<]+)</a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':         
                self.playlistname = name
                logger.info("parts: %s" %url)
                video_pattern_1 = "<script>var[^=]+=(?:|\s+)'([^']+)';</script>"
                self.video_liste = self.get_videos_base_u(url, video_pattern_1)
            return self.video_liste            
        if url.find("stlkr::") > -1:
            if section == 'start':
                b64_string = (scr.replace("+",""))[::-1]
                b64_string += "=" * ((4 - len(b64_string) % 4) % 4)
                b64_str = base64.b64decode(b64_string)
                if PY3:
                    b64_str = to_utf8(b64_str)                    
                portal_url, mac = re.findall('stlkr::url=(.*?)::mac=(.*?)$', url, re.IGNORECASE)[0]
                req = Request(b64_str+scrty, None, { 'User-Agent':'Mozilla/5.0 TURKvod-10', 'Referer': portal_url })
                response = urlopen(req)
                portl_url = response.read()
                response.close()
                if PY3:
                    portl_url = to_utf8(portl_url)
                portal_url = portal_url+portl_url
                self.video_liste = self.get_stl_kr(portal_url, mac)
            if section == 'parts':
                if "::token=" in url:
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_stl_kr_link(url)
                else:
                    portal_url, mac, cat, pg = re.findall('portal_url=(.*?)::mac=(.*?)::cat=(.*?)::pg=(\d+)', url, re.IGNORECASE)[0]
                    url = portal_url + "/portal.php?type=stb&action=handshake&token=&JsHttpRequest=1-xml%20HTTP/1.1"
                    page = getstlkr(url, mac, token="")
                    if PY3:
                        page = to_utf8(page)
                    page = page.replace('\\','')
                    token = re.findall('"token":"([^"]+)"', page)[0]
                    url = portal_url + "/portal.php?type=stb&action=get_profile&hd=1&num_banks=2&not_valid_token=0&auth_second_step=0&video_out=hdmi&client_type=STB&hw_version_2=3b7bd02430f7662d653d0788ac44981ad04e5126&metrics=%7B%22mac%22%3A%22"+Quote(mac)+"%22%2C%22sn%22%3A%227A9DF81D76388%22%2C%22type%22%3A%22stb%22%2C%22model%22%3A%22MAG250%22%2C%22uid%22%3A%2212746ec5a8c99fd74a29882cc5bf408c9389f1bd451ed2c05b32d4d06a22d026%22%7D&JsHttpRequest=1-xml%20HTTP/1.1";
                    page = getstlkr(url, mac, token)
                    if PY3:
                        page = to_utf8(page)
                    page = page.replace('\\','')
                    login = ""
                    password = ""
                    login, password = re.findall('\"login\":\"(|[^\"]+)\",(?:|\\s+)\"password\":\"(|[^\"]+)\"', page, re.IGNORECASE)[0]
                    if not login:
                        login = ""
                    if not password:
                        password = ""
                    url = "stlkr::itv::portal_url="+portal_url+"::mac="+mac+"::token="+token+"::login="+login+"::password="+password+"::cat="+cat+"::pg="+pg
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_stl_kr_link(url)
            return self.video_liste
			        
        if url.find("filmizlesene") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'class="cat-item cat-item-\d+"><a href="(?P<url>[^"]+)"(?:|[^>]+)>(?P<title>[^<]+)</a>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<div class="ykutu2">\s+<a href="(?P<url>[^"]+)" title="(?P<title>[^"]+)">[\s\S]*?"(?P<img>http.*?jpg)"'
                pattern_2 = 'class="mkutu2">\s+<a href="(?P<url>[^"]+)" title="(?P<title>[^"]+)">[\s\S]*?<img src="(?P<img>[^"]+)"'
                sonraki = "rel=[\"']next[\"'] href=[\"']([^\"']+)[\"']"
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = ''
                parts_pattern = '<a href="(?P<url>[^"]+)"(?:| class="lactive")>(?P<title>(?:Moly|MRu|FHD|OkR)[^<]+)</a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)			
            if section == 'parts':
                self.playlistname = name
                pattern = "(?P<url>(?:https://vidmoly|https://my.mail.ru|https://video.filmizlesene.pw/hdplayer/vid)[^'\"]+)['\"]"
                self.video_liste = self.get_videos(url, pattern)
            return self.video_liste
                    
        if url.find("jetfilmizle") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'menu-item-\d+"><a title="[^"]+" href="(?P<url>[^"]+)">(?P<title>[^<]+)</a></li>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = 'class="movie[^>]+>\s+<a href="(?P<url>[^"]+)" rel="bookmark" title="(?P<title>[^"]+)">\s+<img.*?src="(?P<img>[^"]+jpg)"'
                pattern_2 = ''
                sonraki = 'rel="next" href="(?P<next>[^"]+)"'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = 'class="film_part">\s+<span>(?P<title>[^<]+)</span>'
                parts_pattern = '<a href="(?P<url>[^<]+)" class="post-page-numbers"><span>(?P<title>[^<]+)</span></a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)				
            if section == 'parts':
                self.playlistname = name
                pattern = "<iframe\s+src=[\"'](?P<url>[^\"']+)[\"']"
                self.video_liste = self.get_videos(url, pattern)
            return self.video_liste

        if url.find("koreanturk") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'class="cat-item cat-item-\d+"><a href="(?P<url>https?://www.koreanturk.com/[^"]+)"[^>]+>(?P<title>[^<]+)</a>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = 'href="(?P<url>https?://www.koreanturk.com/[^"]+)">\s*<div class="resimcik">\s*<img.*?src="(?P<img>[^"]+)".*?alt="(?P<title>[^"]+)"'
                pattern_2 = ''
                sonraki = 'next"><a href="(?P<next>[^"]+)"'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'parts':
                self.playlistname = name
                pattern = 'id="(?P<title>[^"]+)"><(?:iframe.*?src|a href)="(?P<url>[^"]+)"'
                self.video_liste = self.get_videos(url, pattern)
            return self.video_liste
            
        if url.find("yabancidizi") > -1:
            if section == 'start':
                if url == "https://yabancidizi.pw/":
                    url = "https://yabancidizi.pw/dizi-izle"
                self.playlistname = name
                pattern = '<a href="(?P<url>[^"]+)" title="(?P<title>[^"]+)" data-navigo>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<div class="poster poster-xs">\s+<a href="(?P<url>dizi/(?P<title>[^"]+))" data-navigo>[\s\S]*?data-src="/(?P<img>[^"]+)"'
                pattern_2 = '<div class="ordilabel">\s+<a href="(?P<url>dizi/[^/]+/(?P<title>[^"]+))" data-navigo>'
                self.video_liste = self.get_films(url, pattern_1, pattern_2)
            if section == 'film':
                self.playlistname = name
                self.video_liste = self.get_yabancidizi_parts(url)				
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_yabancidizi_videos(url)
            return self.video_liste
            
        if url.find("bolumd") > -1:
            if section == 'start':                   
                self.playlistname = name
                titlen =1 
                urln =0                            
                pattern = '<a href="(.*?)" class="list-group-it.*?">(.*?)</a>'
                self.video_liste = self.get_categories(url, pattern,titlen,urln)
            if section == 'category':
                self.playlist_cat_name = name                        
                self.playlistname = self.playlist_cat_name                           
 
                
                                
                pattern_1 = 'col-xl-2dot4">.*?<a href="/(.*?)".*?<img src="(.*?)" title="(.*?)"'
                pattern_2 = ''
                sonraki = '<li class="page-item d-none d-md-inline"><a class="page-link" href="(?P<next>[^"]+)">'
                titlen =2 
                urln =0
                imgn=1
                imdbn=3
                logger.info("category: %s" %url)
                self.video_liste = self.get_films(url, pattern_1, pattern_2,titlen,urln,imgn, sonraki)

            if section == 'film':
                if not 'http' in url:
                      url='http://www.bolumd.pw' +url
                age = getHtml(url)
                if   '<iframe id="video_embed_code" src="' in age:    
                    from resources.sites import LIVETV2 
                    url =url
                    self.playlistname = name
                    LIVETV2.bolumdvideos(url,name)
                else:   
                     self.playlistname = name
                     ilk_pattern  = ''
                     parts_pattern = 'col-xl-2dot4">[\s\S]*?<a href="(?P<url>[^"]+)"[\s\S]*?<img src="(?P<img>[^"]+)".*?title="(?P<title>.*?)"'
                     self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)				
            if section == 'parts':
                
                if not 'http' in url:
                     url="http://www.bolumd.pw" +url
                url=url.replace('pw//izle','pw/izle')
                from resources.sites import LIVETV2 
                LIVETV2.bolumdvideos(url,name)
            return self.video_liste
              
           
    def aaddLink(self,name, url, iconimage):
           ok = True
           liz = xbmcgui.ListItem(name)
           liz.setInfo(type='video', infoLabels={'Title': name})
           liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
          # liz.setProperty('Fanart_Image', iconimage)
           xbmc.Player().play(url,liz)
           sys.exit()
          
    
          
        
class turkvod_parsers:

    def __init__(self):
        self.quality = ''
        
    def get_parsed_link(self, url):
        if url.startswith('//www.'):
            url = 'http:' + url
        elif url.startswith('www.'):
            url = 'http://' + url
        elif url.startswith('//'):
            url = 'http:' + url
        son_url = ''
        film_quality = []
        video_tulpe = []
        error = None
        try:
        
            if 'https://video.filmizlesene.pw/hdplayer' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "Referer": "https://www.filmizlesene.pw/"}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    page = response.read() 
                    response.close()
                    if PY3:
                        page = to_utf8(page)            
                    if re.search('https://odnoklassniki.ru/', page):
                        url = re.findall('(https://odnoklassniki.ru.*?)["\']', page, re.IGNORECASE)[0]
                        son_url = self.get_parsed_link(url)
                    else:
                        url = url.replace("/vid/","/drive/")
                        req = Request(url, None, headers)
                        response = urlopen(req)
                        page = response.read() 
                        response.close()
                        if PY3:
                            page = to_utf8(page)
                        url = re.findall('(https://drive.google.com.*?)["\']', page, re.IGNORECASE)[0]
                        son_url = self.get_parsed_link(url)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'redirector.googlevideo.com' in url:
                try:
                    opened = urlopen(url)
                    son_url = opened.geturl()
                    return son_url
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'online/embed' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    page = response.read() 
                    response.close()
                    if PY3:
                        page = to_utf8(page)                    
                    if re.search('file:"\[\d+p\]', page):
                        for match in re.finditer('\[(\d+p)\](http[^",]+)', page):
                            film_quality.append(match.group(1))
                            video_tulpe.append(match.group(2))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'lenembed' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    page = response.read() 
                    response.close()
                    if PY3:
                        page = to_utf8(page)
                    for match in re.finditer("video\S+url: '([^']+)',\s.*?(?:|\s+)video_\S+_text: '(\d+p)'", page):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'fireplayer' in url:
                try:
                    url, hash, ref = re.findall('(.*?video/(.*?))::ref::(.*?)$', url, re.IGNORECASE)[0]
                    host = url + "?do=getVideo"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": ref}
                    data = Urlencode({"hash": hash, "r": ref, "s": ""})
                    if PY3:
                        data = data.encode('ascii')
                    req = Request(host, data ,headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    html = html.replace("\\","")
                    for match in re.finditer('file":"([^"]+)","label":"([^"]+)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1))
                except Exception as ex:
                    print (ex)
                    
            if 'sandup.co' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    page = response.read() 
                    response.close()
                    if PY3:
                        page = to_utf8(page)
                    if re.search('mp4', page):
                        for match in re.finditer('"label":"([^"]+)","type":"video/mp4","file":"([^"]+)"', page):
                            film_quality.append(match.group(1))
                            video_tulpe.append(match.group(2)+ "#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0&Referer=" + url)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                   
            if 'u-play' in url:
                try:
                    hash, id = re.findall('/start/(.*?)/(.*?)$', url)[0]
                    link = "https://ustore.bz/getContentJson.php?hash="+hash+"&id="+id
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = Request(link, None, headers)
                    response = urlopen(req)
                    page = response.read() 
                    response.close()
                    if PY3:
                        page = to_utf8(page)
                    if re.search('mp4', page):
                        for match in re.finditer('"(http[^"]+mp4)"', page):
                            if "480-" in match.group(1) : 
                                kalite = "480p"
                            elif "720-" in match.group(1) : 
                                kalite = "720p"
                            elif "1080-" in match.group(1) : 
                                kalite = "1080p"
                            else:
                                kalite = "360p"
                            film_quality.append(kalite)
                            video_tulpe.append(match.group(1)+ "#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0&Referer=" + url)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'ownerity' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    page = response.read() 
                    response.close()
                    if PY3:
                        page = to_utf8(page)
                    if re.search("vidmoly", page):
                        vidlink = re.findall('(https://vidmoly[^"]+)"', page, re.IGNORECASE)[0]
                        son_url = self.get_parsed_link(vidlink)
                    if re.search('"file":"([^"]+)", ?"label":"([^"]+)"', page):
                        for match in re.finditer('"file":"([^"]+)", ?"label":"([^"]+)"', page):
                            link = match.group(1)
                            if '\\x' in link:
                                link = link.decode('unicode-escape').encode('ASCII')
                            film_quality.append(match.group(2))
                            video_tulpe.append(link)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'stlkr::portal_url' in url:
                try:
                    portal_url, mac, token, login, password, name, cmd, tur = re.findall('portal_url=(.*?)::mac=(.*?)::token=(.*?)::login=(|.*?)::password=(|.*?)::name=(.*?)::cmd=(.*?)::tur=(.*?)$', url)[0]
                    if tur == "vod":
                        cmd = cmd.replace("localhost","lclhst")
                    if tur == "itv":
                        cmd = "ffmpeg http:"+cmd;
                    url = portal_url + "/portal.php?type="+tur+"&action=create_link&cmd="+cmd+"&login=" + login + "&password=" + password + "&JsHttpRequest=1-xml";
                    url = url.replace(" ","%20")
                    page = getstlkr(url, mac, token)
                    if PY3:
                        page = to_utf8(page)
                    page = page.replace('\\','')
                    s_url = re.findall('(http[^"]+)"', page)[0]
                    son_url = s_url.replace("ok2.se","46.166.148.101").replace("mytv.fun","78.142.29.68").replace("portal.geniptv.com","62.210.28.131") + '#User-Agent=Lavf53.32.100'
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'dizigold' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    page = response.read() 
                    response.close()
                    if PY3:
                        page = to_utf8(page)
                    if re.search("<iframe.*?src=", page):
                        vidlink = re.findall('<iframe.*?src="(?://|https?://)([^"]+)"', page, re.IGNORECASE)[0]
                        if 'api.dizigold' in vidlink:
                            vidlink = "http://" + vidlink.replace('/play/gd/','/streaming/file/')
                            son_url = vidlink + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                        else:    
                            vidlink = "http://" + vidlink
                            son_url = self.get_parsed_link(vidlink)
                    if re.search('"file":"([^"]+)", ?"label":"([^"]+)"', page):
                        for match in re.finditer('"file":"([^"]+)", "label":"([^"]+)"', page):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'jetcdn.co' in url or 'api.ocdn' in url and 'postedlink' not in url or 'jetv.xyz' in url or 'yjco.xyz' in url or "jetfilmvid" in url:
                if url.startswith("//"):
                    url = "http:" + url
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': 'https://jetfilmizle.live/',
                        'X-Requested-With': 'XMLHttpRequest'}
                    if 'gp.jetcdn' in url or 'jetv.xyz' in url or 'yjco.xyz' in url or "jetfilmvid" in url:
                        req = Request(url, None , headers)
                        response = urlopen(req)
                        page = response.read()
                        response.close()
                        if PY3:
                            page = to_utf8(page)
                        page = page.replace("\\","")    
                        if "iframe src=" in page:
                            url = re.findall('iframe src=["\'](.*?)["\']', page, re.IGNORECASE)[0]
                            return self.get_parsed_link(url)
                        if '"label":"' in page:
                            for match in re.finditer('"label":"([^"]+)","type":"[^"]+","file":"([^"]+)"', page):
                                film_quality.append(match.group(1))
                                video_tulpe.append(match.group(2))
                        if 'm3u8' in page:
                            son_url = re.findall('"?file"? ?: ?"([^"]+)"', page, re.IGNORECASE)[0]
                            return son_url
                        else:
                            for match in re.finditer('"?file"? ?: ?"([^"]+)", ?"(?:type|label)": ?"([^"]+)"', page):
                                film_quality.append(match.group(2))
                                video_tulpe.append(match.group(1))
                    if 'hls.jetcdn' in url:
                        data = ""
                        if PY3:
                            data = data.encode('ascii')                        
                        key = re.findall('(?:key|id)=(.*?)$', url, re.IGNORECASE)[0]
                        url2 = 'https://hls.jetcdn.co/getHost/' + key
                        req = Request(url2, data , headers)
                        response = urlopen(req)
                        link = response.read()
                        response.close()
                        if PY3:
                            link = to_utf8(link)
                        son_url = decode_base64(link)
                    if 'api.ocdn' in url:
                        if '/fe/' in url:
                            url = url.replace('https://api.ocdn.top/fe/embed-', 'https://fembed.net/api/source/').replace('.html','')
                            son_url = self.get_parsed_link(url)
                        if '/clo/' in url:
                            key = re.findall('embed-(.*?).html', url, re.IGNORECASE)[0]
                            data = "vars="+ key
                            if PY3:
                                data = data.encode('ascii')                        
                            req = Request('https://api.ocdn.top/clo/api.php', data , headers)
                            response = urlopen(req)
                            link = response.read()
                            response.close()
                            if PY3:
                                link = to_utf8(link)
                            link2 = re.findall(r'src="(\S+)[\s|\.]', link)[0] + '.html'
                            son_url = self.get_parsed_link(link2)
                        if '/o1/' in url:
                            req = Request(url, None , headers)
                            response = urlopen(req)
                            link = response.read()
                            response.close()
                            if PY3:
                                link = to_utf8(link)
                            link2 = re.findall(r'src="(\S+)[\s|\.]', link)[0] + '.html'
                            son_url = self.get_parsed_link(link2)
                        if '/vi/' in url:
                            url = url.replace('https://api.ocdn.top/vi/', 'https://vidmoly.to/')
                            return self.get_parsed_link(url)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'vipporns' in url or 'mangovideo' in url:
                def decodevip(video_url, license_code, _size=16):
                    d = video_url.split("/")[1:]
                    h = d[6][:2 * _size]
                    v = evip(license_code, _size)
                    if v and h:
                        t = h
                        u = len(h)-1
                        for u in range(u, -1, -1):
                            ind = u
                            k = u
                            for k in range(k, len(v)):
                               ind += int(v[k])
                            while ind >= len(h):
                               ind -= len(h)
                            a = ""
                            for i in range(len(h)):
                                if i == u:
                                   a += h[ind]
                                elif i == ind:
                                   a += h[u]
                                else:
                                   a += h[i]
                            h = a
                        d[6] = d[6].replace(t, h);
                        d.pop(0);
                        video_url = "/".join(d);
                    return video_url
                def evip(license_code, _size):
                    p = license_code
                    d = p
                    s = ""
                    for i in range(1,len(d)):
                        if d[i]:
                            s += str(d[i])
                        else:
                            s += str(1)
                    p = int(len(s)/2)
                    n = int(s[:p + 1])
                    m = int(s[p:])
                    i = m - n;
                    if i < 0:
                        i = -i
                    s = i
                    i = m - n
                    if i < 0:
                        i = -i;
                    s += i;
                    s *= 2;
                    s = str(s);
                    rate = _size / 2 + 2
                    res = ""
                    for i in range(p+1):
                        for x in range(1,5):
                            num = int(d[i+x]) + int(s[i])
                            if num >= rate:
                                num -= rate
                            res += str(num)
                    return res
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    license_code = re.findall("license_code: ?'([^']+)'", html, re.IGNORECASE)[0]
                    video_url = re.findall("video_url: ?'([^']+)'", html, re.IGNORECASE)[0]
                    son_url =  decodevip(video_url, license_code)+'#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'playvidto' in url:
                try:
                    html = getHtml(url)
                    packed = re.findall(">(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                    html4 = cPacker().unpack(packed)
                    if re.search('src:"[^"]+".*?label:"\d+"', html4):
                        for match in re.finditer('src:"([^"]+)".*?label:"(\d+)"', html4):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1)+'p')
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'woof.tube' in url:
                try:
                    req = Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    vidlink = re.findall('id="videolink">(.*?)</p>', html, re.IGNORECASE)[0]
                    son_url = 'https://woof.tube/gettoken/' + vidlink + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
        
            if 'onlystream' in url or 'uqload' in url or 'videobin' in url or 'fastplay.to' in url:
                try:
                    req = Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    if re.search('"([^"]+(mp4|m3u8))"', html):
                        if re.search('"([^"]+(?:mp4|m3u8))".*?label: ?"([^"]+)"', html):
                            for match in re.finditer('"([^"]+(?:mp4|m3u8))".*?label: ?"([^"]+)"', html):
                                film_quality.append(match.group(2))
                                video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=' + url)
                        else:
                            for match in re.finditer('"([^"]+(mp4|m3u8))"', html):
                                 film_quality.append(match.group(2))
                                 video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=' + url)
                    else:
                        packed = re.findall('(eval\(function\(p,a,c,k,e,d.*?\)\)\))', html, re.IGNORECASE)[0]
                        html = cPacker().unpack(packed)
                        for match in re.finditer('file: ?"([^"]+(mp4|m3u8))"', html):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=' + url)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		
            if 'puhhhhhutv' in url:
                try:
                    host = re.findall('(.*?/hls/)', url, re.IGNORECASE)[0]			
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    html = response.read()
                    if PY3:
                        html = to_utf8(html)                    
                    for match in re.finditer('((\d+p)\S+)', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(host + match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=https://puhutv.com/')
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		  
            if 'fembed.net' in url or 'fembed.com' in url or 'feurl.com' in url or 'femax20.com' in url and 'postedlink' not in url:
                try:
                    url = url.replace('/v/','/api/source/').replace('www.','').replace('fembed.com','femax20.com').replace('fembed.net','femax20.com').replace('feurl.com', 'femax20.com')
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = "r=&d=femax20.com"
                    if PY3:
                        data = data.encode('ascii')                    
                    req = Request(url, data , headers)
                    response = urlopen(req)
                    html = response.read()
                    if PY3:
                        html = to_utf8(html)                    
                    html = html.replace('\\','')
                    for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		  
            if 'vidmo.cc' in url:
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = ""
                    if PY3:
                        data = data.encode('ascii')                    
                    req = Request(url, data , headers)
                    response = urlopen(req)
                    html = response.read()
                    if PY3:
                        html = to_utf8(html)                    
                    if re.search("getJSON\('/source.php\?h=", html):
                        key = re.findall("getJSON\('/source.php\?h=(.*?)[\"']", html, re.IGNORECASE)[0]
                        url2 = 'https://vidmo.cc/source.php?h=' + key
                        req = Request(url2, data , headers)
                        response = urlopen(req)
                        html = response.read()
                        if PY3:
                            html = to_utf8(html)                        
                        html = html.replace('\\','')
                        for match in re.finditer('"label":"([^"]+)","file":"([^"]+)"', html):
                            film_quality.append(match.group(1))
                            video_tulpe.append(match.group(2).replace('https','http'))
                    if re.search("file: '/source.php\?h=", html):
                        key = re.findall("file: '/source.php\?h=(.*?)[\"']", html, re.IGNORECASE)[0]
                        finalID = 'https://vidmo.m3u8/source.php?h=' + key
                        son_url = self.get_parsed_link(finalID)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		  
            if 'dizillalink::' in url and 'filerus' not in url:
                try:
                    host, url, ref = re.findall('dizillalink::(https?://[^/]+/)(.*?)::(.*?)$', url, re.IGNORECASE)[0]
                    headers = {'User-agent': 'Mozilla/5.0 TURKvod-10', 'Connection': 'Close', 'Referer': ref}
                    req = Request(host+url, None , headers)
                    response = urlopen(req)
                    html = response.read()
                    if PY3:
                        html = to_utf8(html)
                    if re.search("getJSON\('/source.php\?h=", html):
                        url2 = re.findall("getJSON\('(.*?)'", html)[0]
                        headers = {'User-agent': 'Mozilla/5.0 TURKvod-10', 'Referer': host+url}
                        req = Request(host+url2, None , headers)
                        response = urlopen(req)
                        html2 = response.read()
                        if PY3:
                            html2 = to_utf8(html2)                    
                        for match in re.finditer('"label":"([^"]+)","file":"([^"]+)"', html2):
                            film_quality.append(match.group(1).replace('\\',''))
                            video_tulpe.append(match.group(2).replace('\\',''))
                    if re.search("openPlayer\('", html):
                        url2 = re.findall("openPlayer\('(.*?)'", html)[0]
                        headers = {'User-agent': 'Mozilla/5.0 TURKvod-10', 'Referer': host+url}
                        req = Request(host+"source.php?v="+url2, None , headers)
                        response = urlopen(req)
                        html2 = response.read()
                        if PY3:
                            html2 = to_utf8(html2)
                        html2 = html2.replace('\\','')
                        url3 = re.findall('file":"([^"]+)"', html2)[0]
                        req = Request(url3, None , headers)
                        response = urlopen(req)
                        page = response.read()
                        if PY3:
                            page = to_utf8(page)                    
                        film_quality = re.findall('RESOLUTION=\d+x(\d+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=\d+x\d+\\s(.*)', page)
                            if len(video_tulpe_tmp) > 0:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe+'#Referer=https://contentx.me/')
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'VanLongStream' in url:
                url = url.replace('VanLongStream::','')
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = ""
                    if re.search('fembed', url):
                        req = Request(url, data , headers)
                        response = urlopen(req)
                        html = response.read()
                        if PY3:
                            html = to_utf8(html)                        
                        fembed = re.findall('"data":"([^"]+)"', html, re.IGNORECASE)[0]
                        req = Request(fembed, None , headers)
                        response = urlopen(req)
                        html2 = response.read()
                        if PY3:
                            html2 = to_utf8(html2)                        
                        fembed = re.findall('https://www.fembed.net/v/([^"\']+)', html2, re.IGNORECASE)[0]
                        link = "https://www.fembed.net/api/source/"+fembed
                        son_url = self.get_parsed_link(link)
                    if re.search('gphoto', url):
                        req = Request(url, data , headers)
                        response = urlopen(req)
                        html2 = response.read()
                        if PY3:
                            html2 = to_utf8(html2)                        
                        serverID2 = re.findall('"data":"https://filmizle.hdfilmcehennemi.com/embedplay/(.*?)"', html2, re.IGNORECASE)[0]
                        serverID2 = "https://filmizle.hdfilmcehennemi.com/getLinkStreamMd5/"+serverID2
                        req = Request(serverID2, None , headers)
                        response = urlopen(req)
                        gphoto = response.read()
                        if PY3:
                            gphoto = to_utf8(gphoto)                        
                        for match in re.finditer('"?file"?:"([^"]+)","?label"?:"([^"]+)"', gphoto):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1) + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('vidmoly', url):
                        req = Request(url, data , headers)
                        response = urlopen(req)
                        html3 = response.read()
                        if PY3:
                            html3 = to_utf8(html3)                        
                        serverID3 = re.findall('"data":"(.*?)"', html3, re.IGNORECASE)[0]
                        req = Request(serverID3, None , headers)
                        response = urlopen(req)
                        html33 = response.read()
                        if PY3:
                            html33 = to_utf8(html33)                        
                        finalID = re.findall('(https://vidmoly\S+/embed.*?)["\']', html33, re.IGNORECASE)[0]
                        son_url = self.get_parsed_link(finalID)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'cdnstreamcdn' in url:
                url = re.findall('(?:embed/|\?v=)(.*?)$', url, re.IGNORECASE)[0]
                url = 'https://panel.streamcdn.xyz/embed/'+url
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    req = Request(url, None , headers)
                    response = urlopen(req)
                    html3 = response.read()
                    if PY3:
                        html3 = to_utf8(html3)                        
                    serverID3 = re.findall('file(?:\s+|"|):(?:\s+|)[\"\'](.*?)[\"\']', html3, re.IGNORECASE)[0]
                    if serverID3.startswith("/"):
                        serverID3 = "http:" + serverID3
                    video_tulpe_tmp = []
                    req = Request(serverID3, None , headers)
                    response = urlopen(req)
                    page = response.read()
                    if PY3:
                        page = to_utf8(page)                        
                    if re.search('RESOLUTION=\d+x(\d+)', page):
                        film_quality = re.findall('RESOLUTION=\d+x(\d+).*?AUDIO="audio"', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=.*AUDIO="audio"\\s(.*)', page)
                            if len(video_tulpe_tmp) > 0:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        req = Request(tulpe, None , headers)
                                        response = urlopen(req)
                                        page = response.read()
                                        if PY3:
                                            page = to_utf8(page)                        
                                        keto = re.findall('(http.*?)["\s]', page, re.IGNORECASE)[0]
                                        tulpe = keto + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                                        video_tulpe.append(tulpe.replace('\r', ''))
                        else:
                            son_url = serverID3 + '#Content-type=application/x-mpegURL&Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    else :
                        film_quality = re.findall('height="(\d+)"', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall(' height="\d+">\s+<BaseURL>(.*)</BaseURL>', page)
                            if len(video_tulpe_tmp) > 0:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        keto = tulpe + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                                        video_tulpe.append(keto.replace('\r', ''))
                        else:
                            son_url = serverID3 + '#Content-type=application/x-mpegURL&Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'molystream' in url:
                url = url.replace('ydx', 'dbx') + '/sheila'
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    req = Request(url, None , headers)
                    response = urlopen(req)
                    page = response.read()
                    if PY3:
                        page = to_utf8(page)                    
                    film_quality = re.findall('RESOLUTION=\d+x(\d+)', page)
                    if film_quality:
                        video_tulpe_tmp = re.findall('RESOLUTION=\d+x\d+\\s(.*)', page)
                        if len(video_tulpe_tmp) > 0:
                            if video_tulpe_tmp[0].find('http') > -1:
                                for tulpe in video_tulpe_tmp:
                                    tulpe = tulpe + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                                    video_tulpe.append(tulpe.replace('\r', ''))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'hdfcdn' in url:
                try:
                    url, ref = re.findall('hdfcdn::(.*?)::ref::(.*?)$', url, re.IGNORECASE)[0]
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': ref,
                        'X-Requested-With': 'XMLHttpRequest'}
                    req = Request(url, None , headers)
                    response = urlopen(req)
                    page = response.read()
                    if PY3:
                        page = to_utf8(page)
                    page = page.replace("\\","")
                    if 'EXTM3U' in page:
                        film_quality = re.findall('RESOLUTION=\d+x(\d+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=\d+x\d+\\s(.*)', page)
                            if len(video_tulpe_tmp) > 0:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        tulpe = tulpe + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                                        video_tulpe.append(tulpe.replace('\r', ''))
                    else:                    
                        host, hls, videoServer = re.findall('player_base_url = "(http.*?)/player[\s\S]*?videoUrl":"(.*?)","videoServer":"(\d+)",', page, re.IGNORECASE)[0]
                        link = host + hls + "?s="+videoServer+"&d="
                        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
                            "Accept": "*/*",
                            "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
                            "Connection": "keep-alive",
                            "Referer": url}
                        req = Request(link, None , headers)
                        response = urlopen(req)
                        page2 = response.read()
                        if "error" in page2:
                            videoServer = re.findall('hostList":\{"\d+":\["(.*?)"', page, re.IGNORECASE)[0]
                            link = host + hls + "?s="+base64.b64encode(videoServer)
                            req = Request(link, None , headers)
                            response = urlopen(req)
                            page2 = response.read()
                        if PY3:
                            page2 = to_utf8(page2)
                        page2 = page2.replace("\\","")
                        film_quality = re.findall('RESOLUTION=\d+x(\d+)', page2)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=\d+x\d+\\s(.*)', page2)
                            if len(video_tulpe_tmp) > 0:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        tulpe = tulpe + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                                        video_tulpe.append(tulpe.replace('\r', ''))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'foreverstream' in url:
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = ""
                    if 'hdfilmcehennemi' in url:
                        key = re.findall('\?id=(.*?)$', url, re.IGNORECASE)[0]
                        url2 = 'https://forever.hdfilmcehennemi.com/get/' + key
                    else:
                        key = re.findall('/embed/(.*?)$', url, re.IGNORECASE)[0]
                        url2 = 'https://cdn.foreverstream.host/get/' + key
                    req = Request(url2, None, headers)
                    response = urlopen(req)
                    page = response.read()
                    if PY3:
                        page = to_utf8(page)                    
                    video_tulpe_tmp = []
                    url_main = ''
                    url_main = '/'.join(url2.split('/')[:-2]) + '/'
                    if re.search('RESOLUTION=\d+x(\d+)', page):
                        film_quality = re.findall('RESOLUTION=\d+x(\d+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=.*\\s(.*)', page)
                            if len(video_tulpe_tmp) > 1:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe.replace('\r', ''))
                                else:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(url_main + tulpe.replace('\r', '').replace('/get', 'get')+ '#Referer=' + url)
                            else:
                                film_quality = []
                                son_url = url
                        else:
                            son_url = url
                        
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'iframetoajax' in url:
                try:
                    link, host, ref = re.findall('((https?://.*?)/.*?):iframetoajax:(.*?)$', url, re.IGNORECASE)[0]
                    link = link.replace('iframe','ajax')
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': '*/*',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': ref}
                    js = host+"/video.js?"+str(int(time.time() * 1000))
                    req = Request(js, None, headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    serverID, myip = re.findall("\(window,'(.*?)','(.*?)'", html, re.IGNORECASE)[0]
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': '*/*',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        serverID: myip}
                    req = Request(link, None, headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    file, hash = re.findall('"file":"(.*?)","hash":"(.*?)"', html, re.IGNORECASE)[0]
                    son_url = file.replace('\\','') +"?"+hash
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'yabancidizi::' in url:
                try:
                    ref, link, dhash = re.findall('(http.*?)::(.*?)::(.*?)$', url, re.IGNORECASE)[0]
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
                        "Referer": ref,
                        "Cookie": "__cfduid=da96876df9dcc621c3d0d0010eaadfadb1603374839; __cf_bm=8b74ebd432402a69beb13b9381810f0089e0eb9a-1603374841-1800-AblaTgtnegq0pqRkRfGUiyG8ws0JUOmXxc0Snu5uoAeBpuJbHXEowOSnkudIHAVKS7hjwZCDjjZmvzoeLdfz0n3TEGeIUkzxU/HlE6liLlNarfvMgiyvB4d0N4WkXM5P2lcM9Kuv0UIeTBfmay7h8nU=; udys=1603374840933; ydt=1603375256; _ga=GA1.2.251984768.1603374842; _gid=GA1.2.1359833398.1603374842; _gat_gtag_UA_176085999_1=1; ci_session=4d0caln9618nvs2vqhd9gvohkaneh1od; level=1; watched_38993=1"
                        }
                    host = 'https://yabancidizi.pw/ajax/service'
                    data = Urlencode({"link": link, "hash": dhash, "querytype": "alternate", "type": "videoGet",})
                    if PY3:
                        data = data.encode('ascii')                    
                    req = Request(host, data, headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    html = html.replace("\\","")
                    link = re.findall('iframe":"(.*?)"', html)[0]
                    req = Request(link, None, headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    html = html.replace("\\","")
                    if 'indifiles' in html:
                        for match in re.finditer('"?file"?:"([^"]+)", ?"?label"?: ?"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1) + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    else:
                        vidlink = re.findall('iframe src="(.*?)"', html)[0]
                        son_url = self.get_parsed_link(vidlink)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
		
            if 'fullhdfilmizlesene_parse' in url:
                url = re.findall('fullhdfilmizlesene_parse:(.*?)$', url, re.IGNORECASE)[0]
                headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': 'https://www.fullhdfilmizlesene.com/'}
                req = Request(url, None, headers)
                response = urlopen(req)
                data = response.read()
                response.close()
                if PY3:
                    data = to_utf8(data)
                data = data.replace('\\','')
                if 'name=fast' in url:
                    try:
                        link = re.findall('src=["\'](.*?)["\']', data)[0]
                        req = Request(link, None, headers)
                        response = urlopen(req)
                        data2 = response.read()
                        response.close()
                        if PY3:
                            data2 = to_utf8(data2)
                        link2 = re.findall('skin:[\s\S]*?(eval[\s\S]*?}\)\));', data2)[0]
                        gg =  cPacker().unpack(link2)
                        gg = gg.replace("\\'","'").replace('\\\\\\\\','\\\\\\')
                        ff =  cPacker().unpack(gg)
                        cc = ff.replace("\\","").replace("x","")
                        if PY3:
                            cc = to_utf8(cc)
                        if re.search('"file":".*?","label":.*?"file":".*?","label"', cc):
                            for match in re.finditer('"file":"(.*?)","label":"(.*?)"', cc):
                                film_quality.append(match.group(2))
                                link = match.group(1)
                                if PY3:
                                    import codecs
                                    link = str(codecs.decode(link, 'hex'))[2:-1]
                                else:
                                    link = link.decode('hex')
                                if link.startswith("//"):
                                    link = "https:" + link
                                video_tulpe.append(link)
                        else:
                            link3 = re.findall('"file":"(.*?)"', cc)[0]
                            if PY3:
                                import codecs
                                son_url = str(codecs.decode(link3, 'hex'))[2:-1]
                                return son_url
                            else:    
                                son_url = link3.decode('hex')
                                return son_url
                    except Exception as e:
                        print ('link alinamadi : ' + str(e))
                        error = True
                if 'name=atom' in url:
                    try:
                        link = re.findall('src=["\'](.*?)["\']', data)[0]
                        req = Request(link, None, headers)
                        response = urlopen(req)
                        data2 = response.read()
                        response.close()
                        if PY3:
                            data2 = to_utf8(data2)
                        link2 = re.findall('"file": ?"([^"]+)"', data2)[0]
                        link2 = (link2.replace("\\","").replace("x",""))
                        if PY3:
                            import codecs
                            s_url = str(codecs.decode(link2, 'hex'))[2:-1]
                            son_url = s_url + '#Referer=' + link + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                            return son_url
                        else:
                            s_url = link2.decode('hex')
                            son_url = s_url + '#Referer=' + link + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                            return son_url
                    except Exception as e:
                        print ('link alinamadi : ' + str(e))
                        error = True
                else:
                    try:
                        if re.search('src=', data):
                            link = re.findall('src=["\'](.*?)["\']', data)[0]
                            if re.search('php\?id=.*?&', link):
                                link1 = re.findall('php\?id=(.*?)&', link)[0]
                                son_url = self.get_parsed_link('https://ok.ru/videoembed/'+link1)
                            if re.search('(?:oload|openload)', link):
                                link1 = link
                                son_url = self.get_parsed_link(link1)
                            if re.search('mail.ru/video', link):
                                link1 = link
                                son_url = self.get_parsed_link(link1)
                            if re.search('rx/plx.php', link):
                                link1 = re.findall('src=["\'](.*?)["\']', data)[0]
                                req = Request(link1, None, headers)
                                response = urlopen(req)
                                data2 = response.read()
                                response.close()
                                if PY3:
                                    data2 = to_utf8(data2)
                                link2 = re.findall('(https://www.rapidvideo.com/e/.*?)["\']', data2)[0]
                                son_url = self.get_parsed_link(link2)
                            if re.search('/embed-', link):
                                link1 = re.findall('/embed-(.*?)["\']', data)[0]
                                link1 = 'https://vidmoly.me/embed-' + link1
                                son_url = self.get_parsed_link(link1)
                                return son_url
                            else:    
                                link1 = re.findall('src=["\'](.*?)["\']', data)[0]
                                req = Request(link1, None, headers)
                                response = urlopen(req)
                                data2 = response.read()
                                response.close()
                                if PY3:
                                    data2 = to_utf8(data2)
                                if re.search('"file":"', data2):
                                    for match in re.finditer('"file":"(.*?)","ql":"(.*?)"', data2):
                                        film_quality.append(match.group(2))
                                        link = match.group(1)
                                        if link.startswith("//"):
                                            link = "https:" + link
                                        video_tulpe.append(link)
                                if re.search('"hls":"', data2):
                                    videolink = re.findall('"hls":"([^"]+)"', data2.replace('\\',''))[0]
                                    if videolink.startswith("//"):
                                        videolink = "https:" + videolink
                                    son_url = videolink
                    except Exception as e:
                        print ('link alinamadi : ' + str(e))
                        error = True
		
            if 'decodedlink' in url:
                try:
                    url = re.findall('decodedlink:(.*?)$', url, re.IGNORECASE)[0]
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    data = response.read()
                    response.close()
                    if PY3:
                        data = to_utf8(data)                    
                    if 'vidplayer' in data:
                        link = re.findall('vidplayer\/embed-(.*?)["\'\s]', data)[0]
                        url1 = 'https://vidmoly.to/embed-' + link
                        son_url = self.get_parsed_link(url1)
                    else:
                        link = re.findall('((?:vidmoly.|closeload.com/video|ok.ru|odnoklassniki.ru|uptostream.com).*?)["\'\s]', data)[0]
                        url1 = 'https://' + link
                        son_url = self.get_parsed_link(url1)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'postedlink' in url:
                try:
                    host, data, ref = re.findall('host:(.*?):params:(.*?):ref:(.*?)$', url, re.IGNORECASE)[0]
                    if PY3:
                        data = data.encode('ascii')                    
                    req = Request(host, data, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    if re.search('"file":"([^"]+)","label":"([^"]+)"', html):
                        for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link.replace("\\",""))
                    if re.search("<script>.*?\('[^']+'", html):
                        server, link = re.findall("<script>(.*?)\('([^']+)'", html)[0]
                        if server == "fembed":
                            link = "https://www.fembed.net/api/source/"+link
                        if server == "uptobox":
                            link = "http://uptostream.com/iframe/"+link
                        if server == "rapid":
                            link = "https://www.rapidvideo.com/e/"+link
                        if server == "mailru":
                            link = "https://videoapi.my.mail.ru/videos/embed/"+link+".html"
                        if server == "openload":
                            link = "https://oload.tv/embed/"+link
                        if server == "okru":
                            link = "http://odnoklassniki.ru/videoembed/"+link
                        if server == "vshare":
                            link = "https://vshare.io/v/"+link+"/width-835/height-425/"
                        son_url = self.get_parsed_link(link)
                    if re.search('vidmo.cc/iframe', html):
                        link = re.findall("(vidmo.cc/iframe.*?)[\"']", html)[0]
                        son_url = self.get_parsed_link('https://'+link)
                    if re.search('iframe.php\?v=', html):
                        link = re.findall("(//[^/]+/iframe.php.*?)[\"']", html)[0]
                        link1 = 'https:'+link
                        son_url = self.get_parsed_link(link1+"::"+ref)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'posted720plink' in url:
                try:
                    url1, host, ref = re.findall('host:((http[^\?]+).*?):ref:(.*?)$', url, re.IGNORECASE)[0]
                    html = getpage(url1).result
                    if re.search('iframe.php\?\S+=', html):
                        link = re.findall("(//[^/]+/iframe.php.*?)[\"']", html)[0]
                        link1 = 'https:'+link
                        son_url = self.get_parsed_link("dizillalink::"+link1+"::"+ref)
                    elif re.search('"file":"([^"]+)","label":"([^"]+)"', html):
                        for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            link = link.replace("\\","")
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link)
                    elif re.search("</div><script>.*?\('", html):
                        server, link = re.findall("</div><script>(.*?)\('([^']+)'", html)[0]
                        if server == "fembed":
                            link = "https://www.fembed.net/api/source/"+link
                        if server == "uptobox":
                            link = "http://uptostream.com/iframe/"+link
                        if server == "rapid":
                            link = "https://www.rapidvideo.com/e/"+link
                        if server == "mailru":
                            link = "https://videoapi.my.mail.ru/videos/embed/"+link+".html"
                        if server == "openload":
                            link = "https://oload.tv/embed/"+link
                        if server == "okru":
                            link = "http://odnoklassniki.ru/videoembed/"+link
                        if server == "vshare":
                            link = "https://vshare.io/v/"+link+"/width-835/height-425/"
                        son_url = self.get_parsed_link(link)
                    elif re.search('vidmo.cc/iframe', html):
                        link = re.findall("(vidmo.cc/iframe.*?)[\"']", html)[0]
                        son_url = self.get_parsed_link('https://'+link)
                    elif re.search('vcdn.io', html):
                        link = re.findall("(vcdn.io.*?)[\"']", html)[0]
                        params = ":params:r="+host+"&d=vcdn.io"
                        ref = ":ref:"+host
                        host = "host:https://"+link.replace('vcdn.io/v/', 'vcdn.io/api/source/');
                        video_url= "postedlink:"+host+params+ref
                        son_url = self.get_parsed_link(video_url)
                    else :
                        try:
                            link = re.findall("<iframe src=[\"'](.*?)[\"']", html)[0]
                            son_url = self.get_parsed_link(link)
                        except Exception as e:
                            print ('link alinamadi : ' + str(e))
                            error = True
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if 'withreflink' in url:
                try:
                    url, ref = re.findall('(.*?)withreflink(.*?)$', url, re.IGNORECASE)[0]
                    req = Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    if re.search('videoUrl.*?master.txt', html):
                        video_url = "hdfcdn::"+url+"::ref::"+ref                        
                        son_url = self.get_parsed_link(video_url)
                        return son_url
                    if re.search('iframe[^=]+src=["\']([^"\']+)["\']', html):
                        link = re.findall('iframe[^=]+src=["\']([^"\']+)["\']', html)[0]
                        req = Request(link, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': url })
                        response = urlopen(req)
                        page = response.read()
                        response.close()
                        if PY3:
                            page = to_utf8(page)
                        try: 
                            link2 = re.findall("= ?[\"']//(.*?\?id=.*?)[\"'<]", page)[0]
                            son_url = 'https://'+link2.replace(" ","").replace("'","").replace('"',"").replace('+',"")
                        except:
                            pass
                    if re.search('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                        for match in re.finditer('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('source src="([^"]+)" type="application/x-mpegurl">', html):
                        videolink = re.findall('source src="([^"]+)" type="application/x-mpegurl">', html)[0]
                        son_url = videolink + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search('file:"[^"]+",label:"[^"]+"', html):
                        for match in re.finditer('file:"([^"]+)",label:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search("file[\"'\s+]?[\"'\s+]?[\"'\s+]?:(?:|\s+)[\"'].*?[\"']", html):
                        videolink = re.findall("file[\"'\s+]?[\"'\s+]?[\"'\s+]?:(?:|\s+)[\"'](.*?)[\"']", html)[0]
                        son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("(https?://[^/]+/lba/.*?)[\"']", html):
                        videolink = re.findall("(https?://[^/]+/lba/\S+m3u8\S+)[\"']", html)[0]
                        son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search('file:.*?(?:|\()"[^"]+"(?:|\)),\s+width:', html):
                        try:
                            videolink = re.findall('file: "([^"]+)"', html)[0]
                            son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                        except:
                            link1 = re.findall('file:[\s\S]*?\("([^"]+)"', html)[0]
                            link1 = link1 [::-1]
                            son_url1 = decode_base64(link1)
                            son_url = son_url1 + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("eval\\(function\(p,a,c,k,e,d", html):
                        try:
                            packed = re.findall('(eval\\(function\(p,a,c,k,e,d.*?)\\n', html, re.IGNORECASE)[0]
                            html = html+cPacker().unpack(packed)
                        except:
                            pass
                    if "getPlayer.php" in ref:
                        videolink = re.findall("file:[\"'](.*?(?:m3u8|mp4))[\"']", html)[0]
                        son_url = videolink + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                        return son_url 
                    if re.search('play.php\?vid=', html):
                        videolink, host, vid = re.findall('((https://\S+)play.php\?vid=([^"]+))"', html)[0]
                        ref = url
                        req = Request(videolink, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                        response = urlopen(req)
                        html = response.read()
                        response.close()
                        if PY3:
                            html = to_utf8(html)                        
                        alternative, ord = re.findall('id="alternative" value="([^"]+)"[\S\s]*?id="order" value="([^"]+)"', html)[0]
                        data = Urlencode({"vid": vid, "alternative": alternative, "ord": ord,})
                        if PY3:
                            data = data.encode('ascii')                        
                        req = Request(host+'ajax_sources.php', data, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                        response = urlopen(req)
                        html = response.read()
                        response.close()
                        if PY3:
                            html = to_utf8(html)                        
                    if re.search('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                        for match in re.finditer('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('file"?:"[^"]+",(?:|\s+)"?label"?:"[^"]+"', html):
                        for match in re.finditer('file"?:"([^"]+)",(?:|\s+)"?label"?:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1).replace('\\','')
                            if link.startswith("//"):
                                link = "https:" + link
                            if 'dizigom' in url :                               
                                video_tulpe.append(link)
                            else:
                                video_tulpe.append(link + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search("(?:file|source_url)[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html):
                        videolink = re.findall("(?:file|source_url)[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html)[0]
                        son_url = videolink #+ '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("(https?://[^/]+/lba/.*?)[\"']", html):
                        videolink = re.findall("(https?://[^/]+/lba/\S+m3u8\S+)[\"']", html)[0]
                        son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search('play.php\?vid=', url):
                        videolink, host, vid = re.findall('((https://\S+)play.php\?vid=(.*?))$', url, re.IGNORECASE)[0]
                        req = Request(videolink, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': url })
                        response = urlopen(req)
                        html = response.read()
                        response.close()
                        if PY3:
                            html = to_utf8(html)                        
                        alternative = re.findall('id="alternative" value="([^"]+)"', html)[0]
                        data = Urlencode({"vid": vid, "alternative": alternative})
                        if PY3:
                            data = data.encode('ascii')                        
                        req = Request(host+'ajax_sources.php', data, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                        response = urlopen(req)
                        html = response.read().replace("\\","")
                        response.close()
                        if PY3:
                            html = to_utf8(html)                        
                        for match in re.finditer('file"?:"([^"]+)",(?:|\s+)"?label"?:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1).replace('\\','')
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		
            if '/rbtv/' in url:
                try:
                    url = url.replace('/rbtv/','/') + 'playlist.m3u8'
                    link_id = url
                    data_url = 'http://163.172.181.152:8030/rbtv/token21.php'
                    headers = {'User-agent' : 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G935F Build/LMY48Z)'}
                    url = data_url
                    username  ='@yarapnakaamkaro#';
                    password = '@tungnakiakaro#';
                    request = Request(url,None,headers)
                    if PY3:
                        base64string = ('%s:%s' % (username, password))
                    else:
                        base64string = base64.b64encode('%s:%s' % (username, password))
                    request.add_header("Authorization", "Basic %s" % base64string)   
                    response = urlopen(request)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                        
                    agent = 'User-Agent=stagefright/1.2 (Linux;Android 5.1.1)'
                    if PY3:
                        son_url = link_id + html + '#' + agent
                    else:
                        son_url = link_id + html + '#' + agent.encode('utf-8')
                except Exception as ex:
                    print (ex)

            if 'SwiftLive' in url:
                try:
                    media, token, data = re.findall('(.*?)::SwiftLive::(.*?)::(.*?)$', url, re.IGNORECASE)[0]			
                    media = media + 'playlist.m3u8'
                    headers = {'Content-Type': 'application/x-www-form-Urlencoded; charset=UTF-8', 'Connection': 'Keep-Alive'}
                    url = 'http://62.210.172.84/'+token+'.php'
                    data = Urlencode({"data": data})
                    if PY3:
                        data = data.encode('ascii')                    
                    req = Request(url, data ,headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    auth_token = html.partition('=')[2]
                    auth_token = ''.join([auth_token[:-59], auth_token[-58:-47], auth_token[-46:-35], auth_token[-34:-23], auth_token[-22:-11], auth_token[-10:]])
                    agent = 'User-Agent=Lavf/56.15.102'
                    if PY3:
                        media_url = media+'?wmsAuthSign='+auth_token+'#' + agent
                    else:
                        media_url = media+'?wmsAuthSign='+auth_token+'#' + agent.encode('utf-8')
                    son_url = media_url
                except Exception as ex:
                    print (ex)
							
            if 'rapidrame' in url or "hdfilmcehennemi.net/player" in url:
                try:
                    url, ref = re.findall('(.*?)::ref::(.*?)$', url, re.IGNORECASE)[0]
                    req = Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    if re.search("eval\\(function", html):
                        packed = re.findall('(eval\\(function.*?)\\n', html, re.IGNORECASE)[0]
                        html2 = cPacker().unpack(packed)
                        if PY3:
                            html2 = to_utf8(html2)
                        html = html + html2
                    if re.search('sources:(?:|\s+)\[{(?:|\s+)file:(?:|\s+)"[^"]+"(?:|\s+)}\]', html):
                        linko = re.findall('sources:(?:|\s+)\[{(?:|\s+)file:(?:|\s+)"([^"]+)"(?:|\s+)}\]', html)[0]
                        if linko.startswith("//"):
                            linko = "http:" + linko
                        son_url = linko +'#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    elif re.search('file:"[^"]+",label:"[^"]+', html):
                        for match in re.finditer('file:"([^"]+)",label:"([^"]+)"', html):
                            linko = match.group(1)
                            if linko.startswith("//"):
                                linko = "http:" + linko
                            film_quality.append("mp4 : " + match.group(2))
                            video_tulpe.append(linko +'#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    elif re.search('file ?: ?["\']([^"\']+)["\']', html):
                        linko = re.findall('file ?: ?["\']([^"\']+)["\']', html)[0]
                        if linko.startswith("//"):
                            linko = "http:" + linko
                        son_url = linko +'#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    else:
                        for match in re.finditer('"([^"]+(m3u8))"', html):
                            linko = match.group(1)
                            if linko.startswith("//"):
                                linko = "http:" + linko
                            film_quality.append("m3u8 : ")
                            video_tulpe.append(linko +'#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		
            if 'fastplayer' in url:
                try:
                    url1, ref = re.findall("(http.*?):refurl=(.*?)$", url, re.IGNORECASE)[0]
                    req = Request(url1, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    packed = re.findall('(eval\(function.*?}\)\))', html, re.IGNORECASE)[0]
                    html = cPacker().unpack(packed)
                    videolink = re.findall('"sources":\[{"file":"([^"]+)"', html, re.IGNORECASE)[0]
                    if videolink.startswith("//"):
                        videolink = "https:" + videolink
                    son_url = videolink + '#Referer=' + url1 + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		
            if 'idtbox' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    for match in re.finditer('src="([^"]+)" type=".*?label="([^"]+)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0' + '&Referer=' + url)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
		
            if 'canlitvplayer' in url:
                try:
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    req = Request(url,None,headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    if re.search('file:["\'].*?m3u8.*?["\']', html):
                        videolink = re.findall('file:["\'](.*?m3u8.*?)["\']', html, re.IGNORECASE)[0]
                        son_url = videolink
                    if re.search('/tv/embed.php', html):
                        embedlink = re.findall('(/tv/embed.php[^"]+)"', html, re.IGNORECASE)[0]
                        embedlink = 'https://www.canlitvplayer.com'+embedlink.replace('&#038;','&')
                        headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                                'Referer': url }
                        req = Request(embedlink,None,headers)
                        response = urlopen(req)
                        html1 = response.read()
                        response.close()
                        if PY3:
                            html1 = to_utf8(html1)                        
                        try:
                            videolink = re.findall('source src="([^"]+)"', html1, re.IGNORECASE)[0]
                            son_url = videolink
                        except:
                            videolink = re.findall("file: ?'([^']+)'", html1, re.IGNORECASE)[0]
                            son_url = videolink
                except Exception as ex:
                    print (ex)

            if 'vshare' in url and 'ivshare' not in url:
                try:
                    headers = {'Referer': url}
                    html = getpage(url, headers).result
                    packed = re.findall("(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                    js = cPacker().unpack(packed).split(';')
                    charcodes = [int(val) for val in js[1].split('=')[-1].replace('[', '').replace(']', '').split(',')]
                    sub = int(''.join(char for char in js[2].split('-')[1] if char.isdigit()))
                    charcodes = [val-sub for val in charcodes]
                    srcs = ''.join(map(unichr, charcodes))
                    for match in re.finditer(u'src="([^"]+)".*?label="([^"]+)"', srcs):
                        film_quality.append(match.group(2).encode('utf-8'))
                        video_tulpe.append(match.group(1).encode('utf-8'))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'quark/content' in url:
                try:
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
                    req = Request(url,None,headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    html = html.replace('\\','')
                    for match in re.finditer('"PlayUrl":"/diziler/yerli/[^/]+/([^/]+sezon)/.*?(\d+[^"]+)"[\s\S]*?"Source":"([^"]+)","Url":"([^"]+)"', html):
                        film_quality.append((match.group(1)).replace('-',' ') + ' '+(match.group(2)).replace('-izle','').replace('-',' '))
                        video_tulpe.append((match.group(3)).replace('master.m3u8','media-3/stream.m3u8') + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0&Referer=' +(match.group(4)))
                except Exception as ex:
                    print (ex)

            if 'youdbox' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    embed = re.findall('\[(".*?")\]', html, re.IGNORECASE)[0]
                    link = embed.replace(",","").replace('"','')
                    link = link.decode('unicode-escape').encode('ASCII')
                    link = link[::-1]
                    son_url = re.findall('src="([^"]+)"', link, re.IGNORECASE)[0]
                except Exception as ex:
                    print (ex)
                    error = True

            if 'vidlox' in url:
                try:
                    headers = {'User-Agent': FF_USER_AGENT, 'Referer': url}
                    url = url.replace('https', 'http')
                    html = getpage(url, headers).result
                    for match in re.finditer('"(http[^"]+(m3u8|mp4))"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
					
            if 'strdef' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer': url }
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    data = response.read()
                    if PY3:
                        data = to_utf8(data)                    
                    link = re.findall('document.write\(dhYas638H\(dhYas638H\("([^"]+)"', data)[0]
                    dd = (decode_base64(link))
                    cc = (decode_base64(dd))
                    link2 = re.findall('document.write\(dhYas638H\(dhYas638H\("([^"]+)"', cc)[0]
                    ee = (decode_base64(link2))
                    ff = (decode_base64(ee))
                    url = re.search(r'iframe src="([^"]+)"', ff, re.IGNORECASE).group(1)
                    son_url = self.get_parsed_link(url)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'izletv' in url or 'ozeltv' in url:
                try:
                    url = url.replace('/izletv/','').replace('/ozeltv/','')
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    req = Request(url,None,headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    hash, id = re.findall('(?:watch|live|play)\("([^"]+)","([^"]+)"', html, re.IGNORECASE)[0]
                    data = Urlencode({'hash': hash, 'id': id, 'e': '03BSTMTRKLR'})
                    if PY3:
                        data = data.encode('ascii')                    
                    req = Request(url, data, headers) 
                    response = urlopen(req)
                    link = response.read()
                    response.close()
                    link1 = link [::-1]
                    #link1 = link1.replace('_','=') + '=='
                    #first64, second64 = re.findall('(.*?=)(.*?==)', link1, re.IGNORECASE)[0]
                    #son_url1 = base64.b64decode(first64)+'?'+base64.b64decode(second64)
                    son_url1 = decode_base64(link1)
                    Header = '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    son_url = son_url1 + Header
                except Exception as ex:
                    print (ex)

            if '24video' in url:
                try:
                    media_id = re.findall('embedPlayer/([A-Za-z0-9]+)', url, re.IGNORECASE)[0]
                    weburl = 'http://24video.ws/video/xml/' + media_id + '?mode=play'
                    req = Request(weburl, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    son_url = re.findall('video url=[\'|"](.*?)[\'|"]', html)[0]
                    url = 'http://24video.ws/embedPlayer' + media_id
                    son_url = son_url.replace('&amp;', '&') + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as ex:
                    print (ex)
					
            if 'bitporno' in url:
                try:
                    #url = url.replace('https', 'http')
                    html = getHtml(url)
                    for match in re.finditer('"(http[^"]+)" type="[^"]+" data-res="([^"]+)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1).replace('\\', ''))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'canlitv.com' in url:
                try:
                    request = Request(url, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                     'Connection': 'Close'})
                    response = urlopen(request).read()
                    if PY3:
                        response = to_utf8(response)                    
                    link = re.findall('file: "(.*?)"', response)
                    son_url1 = link[0]
                    if son_url1.startswith("//"):
                        son_url1 = "https:" + son_url1
                    son_url = son_url1

                except Exception as ex:
                    print (ex)

            if 'canlitvlive' in url or 'livetv' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    Header = '#Referer='+url+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
                    try:
                        stlink = re.findall('((?:web|www|tv).canlitvlive.(?:io|site)/tvizle.php\?t=[^"]+)"', html, re.IGNORECASE)[0]
                        stlink = 'http://' + stlink
                        request = Request(stlink, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Connection': 'Close'})
                        response = urlopen(request).read()
                        if PY3:
                            response = to_utf8(response)                    
                        link = re.findall('file(?: |):(?: |)"(.*?)"', response)
                        son_url1 = link[0]
                        if son_url1.startswith("//"):
                            son_url1 = "http:" + son_url1
                            son_url = son_url1 + Header
                    except:
                        link = re.findall('file: ?"(.*?)"', html)
                        son_url1 = link[0]
                        if son_url1.startswith("//"):
                            son_url1 = "http:" + son_url1
                            son_url = son_url1 + Header
                        else:
                            son_url = link[0] + Header
                except Exception as ex:
                    print (ex)
                    
            if 'ecanlitvizle' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', 'Referer': url})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    Header = '#Referer='+url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
                    try:
                        link = re.findall("(?:\"mediaUrl\":|file: )[\"|'](http.*?m3u8.*?)[\"|']", html)
                        son_url1 = link[0]
                        if son_url1.startswith("//"):
                            son_url1 = "http:" + son_url1
                            son_url = son_url1 + Header
                        else:
                            son_url = link[0] + Header
                    except:
                        pass
                except Exception as ex:
                    print (ex)                  
					
            if 'closeload' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', 'Referer': url})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    #packed = re.findall('(eval\\(function.*?)\\n', html, re.IGNORECASE)[0]
                    #html = cPacker().unpack(packed)
                    Header = '#Referer='+url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
                    link = re.findall('"contentUrl": "([^"]+)"', html)
                    sbttl = ""
                    try:
                        subtitle = re.findall('track src="(/vtt.*?)"',html)
                        if kodi: 
                            if len(subtitle)>0:
                                sbttl = '::https://closeload.com' + subtitle[0]
                    except:
                        pass
                    son_url = link[0] + Header + sbttl
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
					
            if 'daclips.in' in url:
                try:
                    request = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    response = urlopen(request).read()
                    if PY3:
                        response = to_utf8(response)                    
                    link = re.findall("(?:file|src): ['|\"](.*?)['|\"],", response)
                    son_url = link[0]
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
					
            if 'dailymotion.com' in url:
                url = url.replace('dailymotion.com/video/', 'dailymotion.com/embed/video/')
                try:
                    HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Referer': url}
                    page = getpage(url, HTTP_HEADER).result
                    page = page.replace('\\', '')
                    if re.search('"auto":\[\{"type"', page):
                        link = re.findall('"auto":\[\{"type"\s*:.+?"url"\s*:\s*"([^"]+)', page)
                        son_url = self.get_parsed_link(link[0])
                    else:
                        v_tulpe = re.findall('"((?:48|72|108|144|216)\d+)"\s*:\s*\[\{"type".+?"url"\s*:\s*"([^"]+)', page)
                        if v_tulpe:
                            for q, v in v_tulpe:
                                page2 = getpage(v, HTTP_HEADER).result
                                if re.search('BANDWIDTH=(\d+)', page2):
                                    vq = re.findall('BANDWIDTH=.*\\s(.*)', page2)
                                    vq = vq[0]
                                else:
                                    vq = v
                                video_tulpe.append(vq)
                                film_quality.append(q + 'p m3u8')
                except Exception as ex:
                    print (ex)
                    error = True
                    
            if 'datoporn' in url or 'dato.porn' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    packed = re.findall(">(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                    html = cPacker().unpack(packed)
                    for match in re.finditer('file:"([^"]+(mp4|m3u8))"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'canlimacref' in url:
                url = url.replace('canlimacref::','')
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    data = response.read()
                    if PY3:
                        data = to_utf8(data)                    
                    link, host, id = re.findall('((https?://[^/]+)/index.php\?id=(\d+))', data)[0]
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
                            'Referer': url }
                    req = Request(link, None, headers)
                    response = urlopen(req)
                    data = response.read()
                    if PY3:
                        data = to_utf8(data)                    
                    fwd1 = re.findall('atob\("([^"]+)"', data)[0]
                    vid_link = base64.b64decode(fwd1)
                    if PY3:
                        vid_link = to_utf8(vid_link)                    
                    vid_link = vid_link.replace('[','').replace(']','').replace('"','').replace('\\','').replace("'","")
                    Header = '#Referer='+link+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
                    if "m3u8" in vid_link and "_dmzyy_" not in vid_link:
                        if "," in vid_link:
                            vid_link = re.findall('(http[^,]+),', vid_link)[0]
                        sonurl = vid_link+ Header
                    else:
                        req = Request(host+'/dmzjsn.json', None, headers)
                        response = urlopen(req)
                        dmzdata = response.read()
                        if PY3:
                            dmzdata = to_utf8(dmzdata)                    
                        fwd1 = re.findall('"d": "([^"]+)"', dmzdata)[0]
                        fwd2 = re.findall('"fdcub": "(.*?)%id%', dmzdata)[0]
                        cocugu = host + re.findall('src=[\'"](\S+cocugu.*?js)', data)[0]
                        req = Request(cocugu, None, headers)
                        response = urlopen(req)
                        cocugudata = response.read()
                        if PY3:
                            cocugudata = to_utf8(cocugudata)                    
                        http, harf, play = re.findall('config.main.source(?:|\s+)=(?:|\s+)"(.*?)".*?"(.*?)"\+window.mainSource\+"(.*?)"', cocugudata)[0]
                        if "m3u8" in vid_link and "_dmzyy_" in vid_link:
                            sonurl = vid_link.replace( "_dmzyy_", "x."+fwd1) + Header
                        else:
                            sonurl = http+fwd1+harf+id+play+Header
                    son_url = sonurl.replace('[','').replace(']','').replace('"','').replace('\\','').replace("'","")
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
                    
            if '/channel/' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer': url }
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    data = response.read()
                    if PY3:
                        data = to_utf8(data)                    
                    Header = 'Referer='+url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
                    try: 
                        link = re.findall("file: '(.*?m3u8[^']+)'", data)[0]
                        son_url = link + '#' + Header
                    except:
                        link = re.findall('atob\("([^"]+)"', data)[0]
                        dd = (base64.b64decode(link))
                        if PY3:
                            dd = to_utf8(dd)
                        Header = 'Referer='+url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
                        son_url = re.findall('source ?(?:\:|=) ?[\'"](http[^"\']+)[\'"]', dd)[0] + '#' + Header
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'matchservice' in url:
                url = url.replace('matchservice::','')            
                try:
                    html = getHtml(url)
                    if re.search('https?://matchservice', html):
                        link = re.findall('(https?://matchservice[^"\']+)', html, re.IGNORECASE)[0]
                    if re.search('https?://watch', html):
                        link = re.findall('(https?://watch[^"\']+)', html, re.IGNORECASE)[0]
                    else:
                        link = re.findall('<iframe(?:\s+|[\s\S]*?)src=["\'](http[^"\']+)', html, re.IGNORECASE)[0]
                    req = Request(link, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0', 'Referer': url})
                    response = urlopen(req)
                    data = response.read()
                    Headers = response.headers
                    response.close()
                    if PY3:
                        data = to_utf8(data)                    
                    son_url1 = re.findall('source ?= ?["\'](.*?)["\']', data, re.IGNORECASE)[0]
                    son_url = son_url1 + "#User-Agent=Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/30.0.1599.12 Mobile/11A465 Safari/8536.25 (3B92C18B-D9DE-4CB7-A02A-22FD2AF17C8F)&Referer=" + link
                    if son_url.startswith("#"):
                        son_url = ''
                    else:
                        son_url = son_url
                except Exception as ex:
                    print (ex)

            if 'docs.google.com' in url or 'drive.google.com' in url:
                try:
                    media_id = re.findall(r'https?://(?:(?:docs|drive)\.google\.com/(?:uc\?.*?id=|file/d/)|video\.google\.com/get_player\?.*?docid=)(?P<id>[a-zA-Z0-9_-]{20,40})', url, re.IGNORECASE)[0]
                    url = 'http://drive.google.com/file/d/%s/view' % media_id
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0', 'Referer': url})
                    response = urlopen(req)
                    html = response.read()
                    Headers = response.headers
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    c = Headers['Set-Cookie']
                    c2 = re.findall('(?:^|,) *([^;,]+?)=([^;,\/]+?);',c)
                    if c2:
                        cookies = ''
                        for cook in c2:
                            cookies = cookies + cook[0] + '=' + cook[1] + ';'
                    links_parts = re.findall('"fmt_stream_map","(.*?)"', html.decode('unicode-escape'))[0]
                    links_part = re.findall('\\|(.*?)(?:,|$)', links_parts)
                    film_quality = []
                    for link_part in links_part:
                        if link_part.encode('utf_8').find('itag=18') > -1:
                            video_link = (link_part + "#User-Agent=" + FF_USER_AGENT + "&Referer=https://youtube.googleapis.com/" + "&Cookie=" + cookies).encode('utf_8')
                            video_tulpe.append(video_link)
                            film_quality.append('360p')
                        if link_part.encode('utf_8').find('itag=22') > -1:
                            video_link = (link_part + "#User-Agent=" + FF_USER_AGENT + "&Referer=https://youtube.googleapis.com/" + "&Cookie=" + cookies).encode('utf_8')
                            video_tulpe.append(video_link)
                            film_quality.append('720p')
                        if link_part.encode('utf_8').find('itag=37') > -1:
                            video_link = (link_part + "#User-Agent=" + FF_USER_AGENT + "&Referer=https://youtube.googleapis.com/" + "&Cookie=" + cookies).encode('utf_8')
                            video_tulpe.append(video_link)
                            film_quality.append('1080p')
                except Exception as ex:
                    print (ex)
                    error = True
										
            if 'estream' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    for match in re.finditer('"([^"]+)" type=\'video\/mp4\' label=\'\d+x(.*?)\'', html):
                        film_quality.append(match.group(2)+'p')
                        video_tulpe.append(match.group(1))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'hqq.tv' in url or 'hqq.watch' in url or 'netu.tv' in url or 'waaw.tv' in url:
                try:
			
                    def tb(b_m3u8_2):
                        j = 0
                        s2 = ""
                        while j < len(b_m3u8_2):
                            s2 += "\\u0" + b_m3u8_2[j:(j + 3)]
                            j += 3

                        return s2.decode('unicode-escape').encode('ASCII', 'ignore')

                    ## loop2unobfuscated
                    def jswise(wise):
                        while True:
                            wise = re.search("var\s.+?\('([^']+)','([^']+)','([^']+)','([^']+)'\)", wise, re.DOTALL)
                            if not wise: break
                            ret = wise = js_wise(wise.groups())

                        return ret

                    ## js2python
                    def js_wise(wise):
                        w, i, s, e = wise

                        v0 = 0;
                        v1 = 0;
                        v2 = 0
                        v3 = [];
                        v4 = []

                        while True:
                            if v0 < 5:
                                v4.append(w[v0])
                            elif v0 < len(w):
                                v3.append(w[v0])
                            v0 += 1
                            if v1 < 5:
                                v4.append(i[v1])
                            elif v1 < len(i):
                                v3.append(i[v1])
                            v1 += 1
                            if v2 < 5:
                                v4.append(s[v2])
                            elif v2 < len(s):
                                v3.append(s[v2])
                            v2 += 1
                            if len(w) + len(i) + len(s) + len(e) == len(v3) + len(v4) + len(e): break

                        v5 = "".join(v3);
                        v6 = "".join(v4)
                        v1 = 0
                        v7 = []

                        for v0 in range(0, len(v3), 2):
                            v8 = -1
                            if ord(v6[v1]) % 2: v8 = 1
                            v7.append(chr(int(v5[v0:v0 + 2], 36) - v8))
                            v1 += 1
                            if v1 >= len(v4): v1 = 0

                        return "".join(v7)

                    media_id = re.findall('php\?vid=([0-9a-zA-Z/-]+)', url, re.IGNORECASE)[0]
                    headers = {'User-Agent': FF_USER_AGENT,
                               'Referer': 'https://waaw.tv/watch_video.php?v=%s&post=1' % media_id}
                    html = getpage(url, headers).result
                    wise = re.search('''<script type=["']text/javascript["']>\s*;?(eval.*?)</script>''', html,
                                     re.DOTALL | re.I).groups()[0]
                    data_unwise = jswise(wise).replace("\\", "")
                    try:
                        at = re.search('at=(\w+)', data_unwise, re.I).groups()[0]
                    except:
                        at = ""
                    try:
                        http_referer = re.search('http_referer=(.*?)&', data_unwise, re.I).groups()[0]
                    except:
                        http_referer = ""
                    player_url = "http://hqq.watch/sec/player/embed_player.php?iss=&vid=%s&at=%s&autoplayed=yes&referer=on&http_referer=%s&pass=&embed_from=&need_captcha=0&hash_from=&secured=0" % (
                    media_id, at, http_referer)
                    headers.update({'Referer': url})
                    data_player = getpage(player_url, headers).result
                    data_unescape = re.findall('document.write\(unescape\("([^"]+)"', data_player)
                    data = ""
                    for d in data_unescape:
                        data += Unquote(d)

                    data_unwise_player = ""
                    wise = ""
                    wise = re.search('''<script type=["']text/javascript["']>\s*;?(eval.*?)</script>''', data_player,
                                     re.DOTALL | re.I)
                    if wise:
                        data_unwise_player = jswise(wise.group(1)).replace("\\", "")

                    try:
                        vars_data = re.search('/player/get_md5.php",\s*\{(.*?)\}', data, re.DOTALL | re.I).groups()[0]
                    except:
                        vars_data = ""
                    matches = re.findall('\s*([^:]+):\s*([^,]*)[,"]', vars_data)
                    params = {}
                    for key, value in matches:
                        if key == "adb":
                            params[key] = "0/"
                        elif '"' in value:
                            params[key] = value.replace('"', '')
                        else:
                            try:
                                value_var = re.search('var\s*%s\s*=\s*"([^"]+)"' % value, data, re.I).groups()[0]
                            except:
                                value_var = ""
                            if not value_var and data_unwise_player:
                                try:
                                    value_var = \
                                    re.search('var\s*%s\s*=\s*"([^"]+)"' % value, data_unwise_player, re.I).groups()[0]
                                except:
                                    value_var = ""
                            params[key] = value_var
                    data = Urlencode(params)
                    headers.update({'X-Requested-With': 'XMLHttpRequest', 'Referer': player_url})
                    url = "http://hqq.watch/player/get_md5.php?"
                    req = Request(url, data, headers)
                    response = urlopen(req)
                    link = response.read()
                    response.close()
                    if PY3:
                        link = to_utf8(link)                    
                    url_data = json.loads(link)
                    media_url = "https:" + tb(url_data["obf_link"].replace("#", "")) + ".mp4.m3u8"
                    if media_url:
                        del headers['X-Requested-With']
                        headers.update({'Origin': 'https://hqq.watch'})

                    def append_headers(headers):
                        return '|%s' % '&'.join(['%s=%s' % (key, Quote_plus(headers[key])) for key in headers])
                            
                    son_url = media_url + append_headers(headers)
						
                except:
                    print ('link alinamadi')
                    error = True

            if 'izlesene.com' in url:
                try:
                    request = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    response = urlopen(request).read()
                    if PY3:
                        response = to_utf8(response)                    
                    page = response.replace('\\', '').replace('%3A', ':').replace('%2F', '/').replace('%3F', '?').replace('%3D', '=').replace('%26', '&')
                    for match in re.finditer('value":"([^"]+)","source":"([^"]+)"', page):
                        video_tulpe.append(match.group(2))
                        film_quality.append(match.group(1))
                except Exception as ex:
                    print (ex)
                    error = True
					
            if '.m3u8' in url and 'puhutv' not in url:
                try:
                    error = None
                    video_tulpe_tmp = []
                    url_main = ''
                    page = getHtml(url)
                    url_main = '/'.join(url.split('/')[:-1]) + '/'
                    if re.search('RESOLUTION=\d+x(\d+)', page):
                        film_quality = re.findall('RESOLUTION=\d+x(\d+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=.*\\s(.*)', page)
                            if len(video_tulpe_tmp) > 1:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe.replace('\r', ''))
                                else:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(url_main + tulpe.replace('\r', ''))
                            else:
                                film_quality = []
                                son_url = url
                        else:
                            son_url = url
                                        
                    elif re.search('AVERAGE-BANDWIDTH=(\d+)', page):
                        film_quality = re.findall('AVERAGE-BANDWIDTH=(\d+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('AVERAGE-BANDWIDTH=.*\\s(.*)', page)
                            if len(video_tulpe_tmp) > 1:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe.replace('\r', ''))
                                else:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(url_main + tulpe.replace('\r', ''))
                            else:
                                film_quality = []
                                son_url = url
                        else:
                            son_url = url
                                            
                    else:
                        film_quality = re.findall('BANDWIDTH=([0-9]+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('BANDWIDTH=.*\\s(.*)', page)
                            if len(video_tulpe_tmp) > 1:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe.replace('\r', ''))
                                else:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(url_main + tulpe.replace('\r', ''))
                            else:
                                film_quality = []
                                son_url = url
                        else:
                            son_url = url
                except:
                    son_url = url
					
            if 'mail.ru' in url:
                try:
                    html = getHtml(url)
                    metadataUrl = re.findall('(?:metadataUrl|metaUrl)":.*?(//my[^"]+)', html)
                    if PY3:
                        metadataUrl = to_utf8(metadataUrl)                        
                    if metadataUrl:
                        nurl = 'https:%s?ver=0.2.123' % metadataUrl[0]
                        page = getpage(nurl, output='kukili').result
                        video_key = re.findall('video_key[^;]+', page)
                        if PY3:
                            video_key = to_utf8(video_key)                        
                        if video_key:
                            for match in re.finditer('url":"(//cdn[^"]+).+?(\\d+p)', page):
                                video_tulpe.append('http:' + match.group(1) + '#User-Agent=' + FF_USER_AGENT + '&Cookie=' + video_key[0])
                                film_quality.append(match.group(2))
                    else:
                        error = True
                except Exception as ex:
                    print (ex)
                    error = True
					
            if 'ok.ru/videoembed' in url or 'odnoklassniki.ru' in url:
                try:
                    id1 = re.findall('https?://(?:www.)?(?:odnoklassniki|ok).ru/(?:videoembed/|dk\\?cmd=videoPlayerMetadata&mid=)(\\d+)', url)[0]
                    nurl = 'https://odnoklassniki.ru/videoembed/' + id1
                    html = getpage(nurl).result
                    data = re.findall('''data-options=['"]([^'^"]+?)['"]''', html)[0]
                    data = data.replace('\\', '').replace('&quot;', '').replace('u0026', '&')
                    hata = re.findall('error":"([^"]+)', data)
                    if hata:
                        error = True
                    else:
                        film_quality = re.findall('{name:(\\w+),url:.*?}', data)
                        video_tulpe = re.findall('{name:\\w+,url:(.*?),seekSchema', data)
                except:
                    error = True
                    print ('link alinamadi')
					
            if 'plus.google.com' in url:
                try:
                    request = Request(url, None, HEADERS)
                    response = urlopen(request).read()
                    if PY3:
                        response = to_utf8(response)                    
                    page = response.replace('\\', '')
                    for match in re.finditer(r'\[\d+,(\d+),\d+,"([^"]+)"\]', page):
                        film_quality.append(match.group(1))
                        video_tulpe.append(match.group(2).replace('\\', '').replace('u003d', '='))
                except Exception as ex:
                    print (ex)
                    error = True
					
            if 'radio.de' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    page = response.read()
                    response.close()
                    if PY3:
                        page = to_utf8(page)                    
                    if re.match('.*?"stream"', page, re.S):
                        pattern = re.compile('"stream":"(.*?)"')
                        stationStream = pattern.findall(page, re.S)
                        if stationStream:
                            film_quality = []
                            son_url = stationStream[0]
                except:
                    print ('link alinamadi')
                    error = True
					
            if 'rapidvideo' in url:
                try:
                    media_id = re.findall('rapidvideo.(?:org|com)/(?:\\?v=|e/|embed/)([A-z0-9]+)', url, re.IGNORECASE)[0]
                    web_url = 'https://www.rapidvideo.com/v/%s' % media_id
                    request = Request(web_url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    response = urlopen(request).read()
                    if PY3:
                        response = to_utf8(response)                    
                    if '&q=' in response:
                        for match in re.finditer(r'"(http.*?%s&q=([^"]+))"' % media_id, response):
                            request2 = Request(match.group(1), None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3','Connection': 'Close'})
                            response2 = urlopen(request2).read()
                            if PY3:
                                response2 = to_utf8(response2)                    
                            for match2 in re.finditer(r'source src="([^"]+)" type="video/mp4" title="([^"]+)"', response2):
                                film_quality.append(match2.group(2))
                                video_tulpe.append(match2.group(1).replace('\\', ''))
                    elif 'type="video/mp4" label=' in response:
                        for match3 in re.finditer('src="([^"]+)" type="video/mp4" label="([^"]+)"', response):
                            film_quality.append(match3.group(2))
                            video_tulpe.append(match3.group(1).replace('\\', ''))
                    else:
                        for match4 in re.finditer('src="(http[^"]+)" type="video/mp4"', response):
                            son_url = match4.group(1)
                except Exception as ex:
                    print (ex)
                    error = True
				
            if 'raptu' in url:
                try:
                    url = url.replace("raptu", "bitporno")
                    son_url = self.get_parsed_link(url)
                    #media_id = re.findall('raptu.com/(?:\?v\=|embed/|.+?\u=)?([0-9a-zA-Z]+)', url, re.IGNORECASE)[0]
                    #web_url = 'https://www.raptu.com/?v=%s' % media_id
                    #request = Request(web_url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                    # 'Connection': 'Close'})
                    #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
                    #logger.info = urlopen(request, context=gcontext).read()
                    #response = urlopen(request).read()
                    #response = response.replace('\\', '')
                    #for match in re.finditer(r'"file":"([^"]+)","label":"([^"]+)"', response):
                    #    film_quality.append(match.group(2))
                    #    video_tulpe.append(match.group(1).replace('\\', ''))
						
                except Exception as ex:
                    print (ex)
                    error = True
					
            if 'sportstream365' in url:
                try:
                    id = re.findall('http://sportstream365/(.*?)/', url, re.IGNORECASE)[0]
                    #tk = 'http://sportstream-365.com/LiveFeed/GetGame?id='+id+'&partner=24'####>>>>>>>http://sportstream365.com/js/iframe.js
                    #html = getpage(tk, referer='http://www.sportstream-365.com/').result
                    #file = re.findall('true,"VI":"(.*?)"',html)[0]
                    #file = re.findall('.*?VI[\'"]*[:,]\s*[\'"]([^\'"]+)[\'"].*',html)[0]
                    link = '"http://213.183.42.50/hls-live/xmlive/_definst_/' + id + '/' + id + '.m3u8?whence=1001":"Server 1", "http://93.189.63.194/hls-live/xmlive/_definst_/' + id + '/' + id + '.m3u8?whence=1001":"Server 2"'
                    for match in re.finditer('"(.*?)":"(.*?)"', link):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36')
                    #son_url = 'http://213.183.46.114/hls-live/xmlive/_definst_/' + id + '/' + id + '.m3u8?whence=1001' + '#User-Agent=Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36'
                except Exception as ex:
                    print (ex)

            if 'startv.com' in url:
                try:
                    HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Referer': url}
                    html = getpage(url, HTTP_HEADER).result
                    ol_id = re.search(r'"videoUrl": "([^"]+)"', html, re.IGNORECASE).group(1)
                    html1 = getpage(ol_id, HTTP_HEADER).result
                    video_url = re.search(r'"hls":"([^"]+)"', html1, re.IGNORECASE).group(1)
                    son_url = video_url.replace('\\', '')
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
					
            if 'streamango' in url or 'streamcherry' in url or 'fruithosts' in url:
                try:
                    url = url.replace('http:','https:').replace('streamango','streamcherry')
                    if 'reffo' in url:
                        url, ref = re.findall('(.*?)reffo:(.*?)$', url, re.IGNORECASE)[0]
                    else:
                        ref = url
                    def decode(encoded, code):

                        _0x59b81a = ""
                        k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
                        k = k[::-1]

                        count = 0

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

                                _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
                                _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
                                _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
                                _0x2e4782 = _0x2e4782 ^ code

                                _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

                                if _0x3b6833 != 64:
                                    _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
                                if _0x3b6833 != 64:
                                    _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

                        return _0x59b81a
				
                    HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Referer': ref}
                    html = getHtml(url)
                    video_urls = []

                    matches = re.findall("type:\"video/([^\"]+)\",src:d\('([^']+)',(.*?)\).+?height:(\d+)", html, re.DOTALL | re.MULTILINE)

                    for ext, encoded, code, quality in matches:

                        media_url = decode(encoded, int(code))

                        if not media_url.startswith("http"):
                            media_url = "http:" + media_url
                        video_urls.append(["%sp" % (quality), media_url])

                    video_urls.reverse()
                    for video_url in video_urls:

                        videourl = video_url[1].replace("@", "")
                        headers = HTTP_HEADER
                        req = Request(videourl, None, headers)
                        res = urlopen(req)
                        vid_url = res.geturl()
                        video_tulpe.append(vid_url)
                        film_quality.append(video_url[0])
					
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'streamcloud' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    postdata = {}
                    for i in re.finditer('<input.*?name="(.*?)".*?value="(.*?)">', html):
                        postdata[i.group(1)] = i.group(2).replace("download1", "download2")
                    data = Urlencode(postdata)
                    if PY3:
                        data = data.encode('ascii')                    
                    req = Request(url, data, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    keto = response.read()
                    response.close()
                    if PY3:
                        keto = to_utf8(keto)                    
                    r = re.search('file: "(.+?)",', keto)
                    if r:
                        son_url = r.group(1) + "#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0&Referer=" + url
                except Exception as ex:
                    print (ex)
                    error = True
                    
            if 'uptostream' in url:
                try:
                    id = url.split('/')[-1]
                    sUrl2 = "https://uptostream.com/api/streaming/source/get?token=null&file_code=" + id 
                    req = Request(sUrl2, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': url })
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)
                    qua, url_list = decodeur1(html)
                    i=0
                    if qua and url_list:
                        i=0
                        url = ''
                        for x1 in qua:
                            url = url_list[i]
                            video_tulpe.append(url.replace("\\", ""))
                            film_quality.append(x1)
                            i=i+1
                except:
                    print ('link alinamadi')
                    error = True

            if 'userscloud' in url:
                try:
                    url = url.replace('https', 'http')
                    request = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    try:
                        page = urlopen(request).read()
                    except httplib.IncompleteRead as e:
                        page = e.partial
                    if PY3:
                        page = to_utf8(page)                        
                    video_url = re.findall('"(http[^"]+mp4)"', page)[0]
                    son_url = video_url
                except Exception as ex:
                    print (ex)
					
            if 'cccam' in url:
                try:
                    def get_html(link):
                            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                                'Accept-Encoding': 'none',
                                'Accept-Language': 'en-US,en;q=0.8',
                                'Referer': link}
                            req = Request(link, None, headers)
                            try: 
                                response = urlopen(req, timeout = 10)
                                html = response.read()
                                response.close()
                                if PY3:
                                    html = to_utf8(html)                        
                                return html
                            except:
                                pass
                    list = ('http://bosscccam.co/Test.php', 'http://cccammania.com/free5/get2.php', 'https://premiumcccam.store/freetest.php', 'https://thecccam.com/cccam-free.php', 'https://www.cccambird.com/freecccam.php',
                            'http://cccamnice.com/free5/get2.php', 'https://cccamiptv.co/index.php/free-cccam/', 'http://cccamgoal.com/free5/get2.php', 'https://www.cccamprime.com/cccam48h.php', 'https://cccamsupreme.com/cccamfree/get.php')
                    cccamlast = '\n\n\nALLOW TELNETINFO: yes\nALLOW WEBINFO: yes\nWEBINFO LISTEN PORT : 16001\nSTATIC CW FILE : /usr/keys/constant.cw\nCAID PRIO FILE : /etc/CCcam.prio\nPROVIDERINFO FILE : /etc/CCcam.providers\nCHANNELINFO FILE : /etc/CCcam.channelinfo'
                    cccam_list = []
                    counter = 1
                    for link in list:
                        try:
                            html = get_html(link)
                            try: 
                                server, port, user, pasw = re.findall('(?:\s|>| )(?:c|C):\s+(\S+)\s+(\d+)\s+(\S+)\s+(.*?)(?:\s|<| )', html, re.IGNORECASE)[0]
                            except:
                                try: 
                                    server, port, user, pasw = re.findall('Host(?:\s|):(?:\s|)(\S+)</li>.*?Port(?:\s|):(?:\s|)(\d+).*?User(?:\s|):(?:\s|)(\S+)</li>.*?Password(?:\s|):(?:\s|)(\S+)(?:\s|<| )', html, re.IGNORECASE)[0]
                                except:
                                    server, port, user, pasw = re.findall("Host(?:\s+|)</th><th>(.*?)</th.*?Port(?:\s+|)</th><th>(\d+)</.*?User(?:\s+|)</th><th>(.*?)</th.*?Password(?:\s+|)</th><th>(\S+)(?:\s+|<)", html, re.IGNORECASE)[0]
                            server_list = (str(counter), server, port, user, pasw)
                            cccam_list.append(server_list)
                            counter += 1
                        except:
                            pass
                            
                    if 'path' in url:
                        osname = "oscam"
                        ccname = "CCcam.cfg"
                        if 'ncam' in url:
                            osname = "ncam"
                        if 'gcam' in url:
                            osname = "gcam"
                        if 'mgcam' in url:
                            ccname = "cccamd.list"
                        try:
                            path = re.findall('path::(.*?)$', url, re.IGNORECASE)[0]
                            oscam = open ( path+'/'+osname+'.server', 'w')
                            cccam = open ( path+'/'+ccname, 'w')
                            for satir in cccam_list:
                                oscam_line = '\n\n[reader]\nlabel=TURKvod_server_'+satir[0]+'\nenable=1\nprotocol=cccam\ndevice=' + satir[1] + ',' + satir[2] + '\nuser=' + satir[3] + '\npassword=' + satir[4] +'\ncccversion=2.1.2\ngroup=1\ninactivitytimeout=1\nreconnecttimeout=30\nlb_weight=100\ncccmaxhops=10\nccckeepalive=1\ncccwantemu=0\naudisabled=1\ndisablecrccws_only_for=0500:032830,030B00;1811:003311,003315;1819:00006D;098C:000000;09C4:000000;098D:000000;0500:050F00'
                                oscam.write(oscam_line)
                                cccam_line = 'C: ' + satir[1] + ' ' + satir[2] + ' ' + satir[3] + ' ' + satir[4] + '\n'
                                cccam.write(cccam_line)
                            cccam.write(cccamlast)
                            oscam.close()
                            cccam.close()
                        except:
                            pass
                        try:
                            path = re.findall('path::(.*?)$', url, re.IGNORECASE)[0]
                            SoftCam = open ( path+'/SoftCam.Key', 'w')
                            html = get_html("https://raw.githubusercontent.com/popking159/softcam/master/SoftCam.Key")
                            SoftCam.write(html)
                            SoftCam.close()
                        except:
                            pass
                    else:
                        try:
                            if os.path.isfile('/usr/keys/CCcam.cfg'):
                                contents = open ('/usr/keys/CCcam.cfg', 'r').read()
                                cccamlast = re.findall('(ALLOW[\s\S]*?)$', contents, re.IGNORECASE)[0]
                                cccamlast = "\n\n" + cccamlast
                            cccam = open ('/usr/keys/CCcam.cfg', 'w')
                            oscam = open ('/usr/keys/oscam.server', 'w')
                            for satir in cccam_list:
                                oscam_line = '\n\n[reader]\nlabel=TURKvod_server_'+satir[0]+'\nenable=1\nprotocol=cccam\ndevice=' + satir[1] + ',' + satir[2] + '\nuser=' + satir[3] + '\npassword=' + satir[4] +'\ncccversion=2.1.2\ngroup=1\ninactivitytimeout=1\nreconnecttimeout=30\nlb_weight=100\ncccmaxhops=10\nccckeepalive=1\ncccwantemu=0\naudisabled=1\ndisablecrccws_only_for=0500:032830,030B00;1811:003311,003315;1819:00006D;098C:000000;09C4:000000;098D:000000;0500:050F00'
                                oscam.write(oscam_line)
                                cccam_line = 'C: ' + satir[1] + ' ' + satir[2] + ' ' + satir[3] + ' ' + satir[4] + '\n'
                                cccam.write(cccam_line)
                            cccam.write(cccamlast)
                            oscam.close()
                            cccam.close()
                        except:
                            pass
                        try:
                            if os.path.isfile('/etc/CCcam.cfg'):
                                contents = open ('/etc/CCcam.cfg', 'r').read()
                                cccamlast = re.findall('(ALLOW[\s\S]*?)$', contents, re.IGNORECASE)[0]
                                cccamlast = "\n\n" + cccamlast
                            cccam = open ('/etc/CCcam.cfg', 'w')
                            for satir in cccam_list:
                                cccam_line = 'C: ' + satir[1] + ' ' + satir[2] + ' ' + satir[3] + ' ' + satir[4] + '\n'
                                cccam.write(cccam_line)
                            cccam.write(cccamlast)
                            cccam.close()
                        except:
                            pass
                        try:
                            oscam = open ('/etc/tuxbox/config/oscam/oscam.server', 'w')
                            for satir in cccam_list:
                                oscam_line = '\n\n[reader]\nlabel=TURKvod_server_'+satir[0]+'\nenable=1\nprotocol=cccam\ndevice=' + satir[1] + ',' + satir[2] + '\nuser=' + satir[3] + '\npassword=' + satir[4] +'\ncccversion=2.1.2\ngroup=1\ninactivitytimeout=1\nreconnecttimeout=30\nlb_weight=100\ncccmaxhops=10\nccckeepalive=1\ncccwantemu=0\naudisabled=1\ndisablecrccws_only_for=0500:032830,030B00;1811:003311,003315;1819:00006D;098C:000000;09C4:000000;098D:000000;0500:050F00'
                                oscam.write(oscam_line)
                            oscam.close()
                        except:
                            pass
                        son_url = oscam_line
                except Exception as ex:
                    print (ex)
					
            if 'videojs.tmgrup.com' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer':'http://www.atv.com.tr/'}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    data = response.read()
                    if PY3:
                        data = to_utf8(data)                    
                    url2, url1 = re.findall('"VideoUrl":"([^"]+)".*?"VideoSmilUrl":"([^"]+)"', data, re.IGNORECASE)[0]
                    host = 'https://securevideotoken.tmgrup.com.tr/webtv/secure?url=' + url1 + '&url2=' + url2
                    req = Request(host, None, headers)
                    response = urlopen(req)
                    data2 = response.read()
                    if PY3:
                        data2 = to_utf8(data2)                    
                    url3 = re.findall('true,"Url":"([^"]+)"', data2, re.IGNORECASE)[0]
                    son_url = self.get_parsed_link(url3)
                except:
                    print ('link alinamadi')
                    error = True					
					
            if 'videotoken.tmgrup.com.tr' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer':'http://www.atv.com.tr/webtv/canli-yayin'}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    data = response.read()
                    if PY3:
                        data = to_utf8(data)                    
                    match = re.findall('true,"Url":"(.+?)"', data, re.DOTALL | re.MULTILINE)
                    son_url = '**** '+match[0]
                    if match:
      	              url3 = match[0]
      	              son_url = self.get_parsed_link(url3)
                except:
                    print ('link alinamadi')
                    error = True					
					
            if 'vidmoly' in url or 'supervideo' in url or 'venus/playm' in url or 'akar/playm' in url or 'newsexit' in url or 'viduplayer' in url or 'vidfast' in url or 'mixdrop' in url or 'cloudvideo' in url or 'vidia.tv' in url or 'letsupload' in url or 'prostream' in url or 'upstream' in url:
                try:
                    url = url.replace("vidmoly.me","vidmoly.to")
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
                    req = Request(url, None, headers)
                    response = urlopen(req)
                    html = response.read()
                    if PY3:
                        html = to_utf8(html)                    
                    if re.search("window.location", html):
                        embed = re.findall('window.location = ["\']([^"\']+)["\']', html, re.IGNORECASE)[0]
                        url = url.replace("embed-", embed )
                        req = Request(url, None, headers)
                        response = urlopen(req)
                        html = response.read()
                    if PY3:
                        html = to_utf8(html)                    
                    if re.search("(eval\\(function.*?)\\n", html):
                        packed = re.findall("(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                        html2 = cPacker().unpack(packed)
                        html = html + html2
                    sbttl = ""
                    try:
                        subtitle = re.findall('(/srt.*?)"', html, re.IGNORECASE)[0],
                        if kodi: 
                            if len(subtitle)>0:
                                sbttl = '::http://vidmoly.to' + subtitle[0]
                    except:
                        pass
                    if re.search('"[^"]+mp4",(?:|\s+)label:(?:|\s+)"[^"]+"', html):
                        for match in re.finditer('file:(?:|\s+)"((?:http|//)[^"]+mp4)",(?:|\s+)label:(?:|\s+)"([^"]+)"', html):
                            linko = match.group(1)
                            if linko.startswith("//"):
                                linko = "http:" + linko
                            film_quality.append("Play mp4 : "+match.group(2))
                            video_tulpe.append(linko +'#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0&Referer=' + url + sbttl)
                    if re.search('[\'"]\S+(mp4|m3u8)\S+[\'"]', html):
                        for match in re.finditer('(?:src=|url=|file: ?)[\'"]((?:http|//)\S+(mp4|m3u8)[^\'"]+)[\'"]', html):
                            linko = match.group(1)
                            if linko.startswith("//"):
                                linko = "http:" + linko
                            film_quality.append("Play " + match.group(2))
                            video_tulpe.append(linko +'#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0&Referer=' + url + sbttl)
                    if re.search('"[^"]+(mp4|m3u8)"', html):
                        for match in re.finditer('"((?:http|//)[^"]+(mp4|m3u8))"', html):
                            linko = match.group(1)
                            if linko.startswith("//"):
                                linko = "http:" + linko
                            film_quality.append("Play " + match.group(2))
                            video_tulpe.append(linko +'#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0&Referer=' + url + sbttl)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
            if 'vidoza' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    try:
                        for match in re.finditer('src(?:\:|=) ?["|\'](.*?)["|\'],? type:.*?res:["|\'](.*?)["|\']', html):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1))
                    except :
                        for match in re.finditer('src(?:\:|=) ?["|\'](.*?)["|\'],? type(?:\:|=)["|\'](.*?)["|\']', html):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1))
                        
                except Exception as ex:
                    print (ex)
                    error = True
				
            if 'vidto.me' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    link = response.read()
                    response.close()
                    if PY3:
                        link = to_utf8(link)                    
                    ids = re.compile('<input type="hidden" name="id".*?value="(.*?)">').findall(link)[0]
                    fname = re.compile('<input type="hidden" name="fname".*?value="(.*?)">').findall(link)[0]
                    hash1 = re.compile('<input type="hidden" name="hash".*?value="(.*?)">').findall(link)[0]
                    postdata = {'op': 'download1',
                     'id': ids,
                     'fname': fname,
                     'hash': hash1,
                     'referer': '',
                     'imhuman': 'Proceed to video',
                     'usr_login': ''}
                    sleep_time = int(re.findall('>([0-9])</span> seconds<', link)[0])
                    time.sleep(sleep_time)
                    data = Urlencode(postdata)
                    if PY3:
                        data = data.encode('ascii')                     
                    req = Request(url, data, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    for match in re.finditer('file:"(.*?)",label:"(\d+p)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1))
                except Exception as ex:
                    print (ex)
                    error = True

            if 'vidup' in url and 'viduplayer' not in url:
                try:
                    media_id = re.findall("embed/([A-z0-9]+)", url, re.IGNORECASE)[0]
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    data = Urlencode({})
                    if PY3:
                        data = data.encode('ascii')                     
                    url = 'https://vidup.io/api/serve/video/%s' % media_id
                    req = Request(url, data, headers)
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    for match in re.finditer('"(\d+p)":"([^"]+)"', html):
                        film_quality.append(match.group(1))
                        video_tulpe.append(match.group(2))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'vidzi' in url:
                try:
                    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urlopen(req)
                    html = response.read()
                    response.close()
                    if PY3:
                        html = to_utf8(html)                    
                    if re.search("type='text/javascript'>(eval\\(function.*?)\\n", html):
                        packed = re.findall("type='text/javascript'>(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                        html = cPacker().unpack(packed)
                    for match in re.finditer('file:?"([^"]+(m3u8|mp4))"', html):
                        film_quality.append(match.group(2).replace('v.mp', 'mp4'))
                        video_tulpe.append(match.group(1).replace('?embed=', ''))
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True

            if 'vk.com' in url:
                if "oid" not in url:
                    oid, id = re.findall('vk.com/video(.*?)_(.*?)$', url, re.IGNORECASE)[0]
                    url = "http://vk.com/video_ext.php?oid="+oid+"&id="+id
                query = url.split('?', 1)[-1]
                query = Parse_qs(query)
                x_m = '=smd6IXY6wWY60WY6IXY6smd9MWYt9FevJmJ'
                v_k = '=0DZpZ3PwhGcusmdvIXYsFWbhJXYvATMv82YuQ2b2tmc1R3LvoDc0RHa'
                #api_url = 'http://vk.com/al_video.php?act=show_inline&al=1&video=%s_%s' % (query['oid'][0], query['id'][0])
                #media_id = 'https://vk.com/video%s_%s' % (query['oid'][0], query['id'][0])
                #req = urllib2.Request(api_url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                #response = urllib2.urlopen(req)
                #html = response.read()
                #response.close()
                if PY3:
                    kv = to_utf8(base64.b64decode(v_k[::-1]))
                    kkv = to_utf8(base64.b64decode(x_m[::-1]))
                else:
                    kv = base64.b64decode(v_k[::-1])
                    kkv = base64.b64decode(x_m[::-1])
                req = Request((kv+query['oid'][0]+"_"+query['id'][0]+kkv), None, {'User-agent': 'Mozilla/5.0 TURKvod-10'})
                response = urlopen(req)
                html = response.read()
                Headers = response.headers
                response.close()
                if PY3:
                    html = to_utf8(html)                    
                for match in re.finditer('<mp4_([^>]+)>([^>]+)<', html):
                    film_quality.append(match.group(1).replace('mp4_','')+'P')
                    video_tulpe.append(Unquote(match.group(2)))

            if 'vimeo.com' in url:
                try:
                    ids = re.findall('vimeo.com(?:/video)?/(\\d+)', url)[0]
                    url = 'http://player.vimeo.com/video/' + ids + '/config'
                    headers = {'Referer': 'https://vimeo.com/',
                               'Origin': 'https://vimeo.com'}
                    data = getpage(url,headers).result
                    packed = re.findall('("progressive":\[{.+?}\]})', data, re.IGNORECASE)[0]
                    reg = re.findall(',"url":"(.+?)",.+?"quality":"(.+?)",', packed)
                    for src, quality in reg:
                        video_tulpe.append(src)
                        film_quality.append(quality)
                except:
                    error = True
                    print ('link alinamadi')

            if 'web.tv' in url:
                try:
                    request = Request(url, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                     'Connection': 'Close'})
                    response = urlopen(request).read()
                    if PY3:
                        response = to_utf8(response)                                        
                    link = re.findall('"src":"(.*?)"', response)
                    son_url = link[0]
                    son_url = son_url.replace('\\', '')
                except Exception as ex:
                    print (ex)
				
            if 'yourporn' in url:
                try:
                    request = Request(url, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                     'Connection': 'Close'})
                    response = urlopen(request).read()
                    if PY3:
                        response = to_utf8(response)                    
                    link = re.findall("src='([^']+mp4)'", response)
                    son_url1 = link[0]
                    if son_url1.startswith("//"):
                        son_url1 = "http:" + son_url1
                    son_url = son_url1
                except Exception as ex:
                    print (ex)
                    
            if 'youtube' in url:
                gecerli_url = '^\n                 (\n                     (?:https?://)?                                       # http(s):// (optional)\n                     (?:youtu\\.be/|(?:\\w+\\.)?youtube(?:-nocookie)?\\.com/|\n                        tube\\.majestyc\\.net/)                             # the various hostnames, with wildcard subdomains\n                     (?:.*?\\#/)?                                          # handle anchor (#/) redirect urls\n                     (?!view_play_list|my_playlists|artist|playlist)      # ignore playlist URLs\n                     (?:                                                  # the various things that can precede the ID:\n                         (?:(?:v|embed|e)/)                               # v/ or embed/ or e/\n                         |(?:                                             # or the v= param in all its forms\n                             (?:watch(?:_popup)?(?:\\.php)?)?              # preceding watch(_popup|.php) or nothing (like /?v=xxxx)\n                             (?:\\?|\\#!?)                                  # the params delimiter ? or # or #!\n                             (?:.*?&)?                                    # any other preceding param (like /?s=tuff&v=xxxx)\n                             v=\n                         )\n                     )?                                                   # optional -> youtube.com/xxxx is OK\n                 )?                                                       # all until now is optional -> you can pass the naked ID\n                 ([0-9A-Za-z_-]+)                                         # here is it! the YouTube video ID\n                 (?(1).+)?                                                # if we found the ID, everything can follow\n                 $'
                mobj = re.match(gecerli_url, url, re.VERBOSE)
                video_id = mobj.group(2)
                html = getHtml(url)
                html = html.replace('\\','')
                try:
                    if 'm3u8' in html:
                        link = re.findall('"(http[^"]+m3u8)"', html, re.IGNORECASE)[0]
                        page = getpage(link).result
                        url_main = '/'.join(link.split('/')[:-1]) + '/'
                        film_quality = re.findall('BANDWIDTH=([0-9]+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('BANDWIDTH=.*\\s(.*)', page)
                            if len(video_tulpe_tmp) > 1:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe.replace('\r', ''))
                                else:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(url_main + tulpe.replace('\r', ''))
                            else:
                                film_quality = []
                                son_url = link
                        else:
                            son_url = link
                    else:
                        try:
                            found = False
                            for el in ['&el=embedded',
                             '&el=detailpage',
                             '&el=vevo',
                             '']:
                                info_url = 'https://www.youtube.com/get_video_info?&video_id=%s%s&ps=default&eurl=&gl=US&hl=en' % (video_id, el)
                                try:
                                    infopage = getpage(info_url).result
                                    videoinfo = Parse_qs(infopage)
                                    if ('url_encoded_fmt_stream_map' or 'fmt_url_map') in videoinfo:
                                        found = True
                                        break
                                except Exception as ex:
                                    print (ex, 'YT ERROR 1')
                            if found:
                                fmt_value = {'18': '360p',
                                 '22': '720p',
                                 '37': '1080p',
                                 '84': '720p'}
                                if videoinfo.has_key('url_encoded_fmt_stream_map'):
                                    videos = videoinfo['url_encoded_fmt_stream_map'][0].split(',')
                                    for video in videos:
                                        if Parse_qs(video)['itag'][0] in fmt_value.keys():
                                            film_quality.append(fmt_value[Parse_qs(video)['itag'][0]])
                                            video_tulpe.append(Parse_qs(video)['url'][0])
                            else:
                                videos = videoinfo['player_response'][0]
                                for match in re.finditer('"itag":(18|22),"url":"([^"]+)"', videos):
                                    film_quality.append(match.group(1).replace('18','360p').replace('22','720p'))
                                    video_tulpe.append(match.group(2).replace('\\u0026','&'))
                        except:
                            pass
                except Exception as ex:
                    print (ex)
                    error = True
                    
            if 'youwatch' in url or 'chouhaa' in url:
                try:
                    headers = {'User-Agent': FF_USER_AGENT, 'Referer': url}
                    media_id = re.findall('(?://|\.)(?:youwatch.org|chouhaa.info|voodaith7e.com|youwatch.to)/(?:embed-|)([a-z0-9]+)', url, re.IGNORECASE)[0]
                    page_url = 'http://youwatch.org/embed-%s.html' % media_id
                    html = getpage(page_url, headers).result
                    html1 = re.findall('<iframe\s+src\s*=\s*"([^"]+)', html, re.IGNORECASE)[0]
                    html2 = getpage(html1, headers).result
                    for match in re.finditer('file:"([^"]+)",label:"(\d+)"', html2):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + "#Referer=" + html1)
                except Exception as e:
                    print ('link alinamadi : ' + str(e))
                    error = True
					
            if error:
                return (error, video_tulpe, film_quality)
            elif film_quality:
                return (error, video_tulpe, film_quality)
            else:
                return son_url
        except Exception as ex:
            print (ex)
            print ('html_parser ERROR')