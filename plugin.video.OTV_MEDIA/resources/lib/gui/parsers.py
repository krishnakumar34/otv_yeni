# -*- coding: utf-8 -*-
from resources.lib.logger import logger 
import re
import json

from resources.lib.config import GestionCookie

from resources.lib.comaddon import dialog, VSlog, isMatrix
from resources.lib.handler.premiumHandler import cPremiumHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.util import Unquote


import base64, sys, os, json, time, string, random, datetime, hashlib
import codecs, re, xbmcplugin, xbmcgui, xbmcaddon, xbmc, xbmcvfs
isPy3 = False
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
    from urllib.request import URLError as URLError
    isPy3 = True; unicode = str; unichr = chr; long = int; xrange = range

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
    from urllib2 import URLError as URLError

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
__addonuserdata__    = xbmc.translatePath(settings.getAddonInfo('profile') )
UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 OPR/73.0.3856.344'
videolist = []
qualitylist = []
linkler = []
kaynaklar = []
root = settings.getSetting("root")
tokens = root.split('/')
root2 = '/'.join(tokens[:-2])
temp = xbmc.translatePath("special://temp")

def to_utf8(dct):
    if isinstance(dct, dict):
        return dict((to_utf8(key), to_utf8(value)) for key, value in dct.items())
    elif isinstance(dct, list):
        return [to_utf8(element) for element in dct]
    elif isinstance(dct, unicode):
        dct = dct.encode("utf8")
        if isPy3: dct = dct.decode("utf8")
        return dct
    elif isPy3 and isinstance(dct, bytes):
        try:
            return dct.decode('utf-8')
        except:
            return dct.decode('ISO-8859-1')
    else:
        return dct

def fetch(url, data = None, head = None):
    try:
        cookie_handler = HTTPCookieProcessor(cookielib.LWPCookieJar())
        opener = build_opener(cookie_handler, HTTPBasicAuthHandler(), HTTPHandler())
        opener = install_opener(opener)
        headers = {'User-Agent': UA}
        if url.startswith('//www.'):
            url = 'http:' + url
        elif url.startswith('www.'):
            url = 'http://' + url
        elif url.startswith('//'):
            url = 'http:' + url
        key = settings.getSetting("key")
        answer = settings.getSetting("answer")
        if data is not None and 'hdtvler.tv' not in url and 'fembed' not in url and 'feurl' not in url and 'fplay' not in url:
            data = Urlencode(data)
        if head is not None:
            headers = headers.copy()
            headers.update(head)
        try:
            req = Request(url, data.encode('utf-8'), headers)
        except:
            req = Request(url, data, headers)
        res = None
        try:
            res = urlopen(req, timeout = 5)
        except:
            try:
                time.sleep(3)
                res = urlopen(req, timeout = 5)
            except:
                m3u_url = "-1"
                if 'http' in settings.getSetting('m3u'):
                    m3u_url = settings.getSetting('m3u')
                if 'cachekey.php' not in url and m3u_url not in url and 'updateMail.php?username=' not in url and 'hasMail.php?username=' not in url and 'user.php?type=add&email=' not in url and 'tvyayinakisi.com' not in url and 'mesaj.php' not in url:
                    showMessage('[COLOR orange][B]Veri Alınamıyor...[/B][/COLOR]','[COLOR red]Hata tekrar ederse lütfen internet bağlantınızı kontrol ediniz.[/COLOR]')
        if res is not None:
            if 'mail.ru' in url:
                cont = res.read() + 'kuki :' + str(res.headers.get('Set-Cookie'))
            else:
                cont = res.read()
            res.close()
            return to_utf8(cont)
        else:
            return ""
    except URLError as e:
        if  'ssl.c:510: error' in str(e.reason):
            showMessage("[COLOR orange][B]OTV_MEDIA[/B][/COLOR]","[COLOR red][B]Kodi Sürümünüz bu linki desteklemiyor![/B][/COLOR]",2000)
            
def cache(url):
    try:
        cont = codecs.open(xbmc.translatePath(os.path.join(temp,'86519', hashlib.md5(url.encode('UTF-8')).hexdigest())), "r", "utf-8-sig").read()
    except:
        cont = fetch(url)
        if cont != None and  cont != '' and 'save.php' not in url and 'episodes.php' not in url and 'faviptv.php' not in url and 'cachekey.php' not in url and 'vipbilgi.php' not in url and 'show.php?type=user' not in url and 'show.php?type=history' not in url and 'search.php' not in url:
            with codecs.open(xbmc.translatePath(os.path.join(temp,'86519', hashlib.md5(url.encode('UTF-8')).hexdigest())), "w+", "utf-8-sig") as out:
                out.write(to_utf8(cont))
    return to_utf8(cont)

def cache_clear():
    try:
        path = os.path.join(temp,'86519')
        files = xbmcvfs.listdir(path)
        for fil in files[1]:
            xbmcvfs.delete(os.path.join(path, fil))
    except:
        pass
            
def showMessage(heading='OTV_MEDIA',message='',times=2000,pics=''):
    try:
        xbmc.executebuiltin('Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
    except:
        pass
                        
def select(kaynaklar, linkler, tip = 2):
    name = 'Kalite'
    if tip == 1:
        name = 'Kaynak'
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Lütfen ' + name + ' Seçiniz...',kaynaklar)
    if ret > -1:
        return linkler[ret]
    else:
        return 'selection cancelled'
    
def error(url):
    showMessage("[COLOR orange][B]OTV_MEDIA[/B][/COLOR]","[COLOR orange][B]Medya Bulunamadı!!![/B][/COLOR]")
    fetch(root + 'linkerrorskodi.php?link=' + url)

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    if isPy3:    
        data = base64.b64decode(data)
        return data.decode('UTF-8')
    else:    
        return base64.decodestring(data)
    
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
        
        if base == 0 :
            base = 36
        
        if 2 <= base <= 36:
            self.unbase = lambda string: int(string, base)
        else:
            if base < 62:
                self.ALPHABET[base] = self.ALPHABET[62][0:base]
            elif 62 < base < 95:
                self.ALPHABET[base] = self.ALPHABET[95][0:base]
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
    
def parse(url):
    options = {"fullhdfilmizlesene": fullhdfilmizlesene,"dizidimi": dizidimi,"ok.ru/videoembed": okru, "odnoklassniki.ru": okru,"vidmoly": vidmoly,"flmplayer": vidmoly,"closeload": closeload,
               "filmakinesi": filmakinesi,"canlitvlive": canlitvlive,"uptostream": uptostream,"youtube": youtube,"filmmodu": filmmodu,"mail.ru": mailru,
               "fembed": fembed, "feurl": fembed,"fplay": fembed,"imdb": imdb,"s1cdn": s1cdn,"showtv.com": show, "showturk.com.tr": show, "showmax.com.tr": show,
               "yjco.xyz": yjco,"foxplay.com": foxplay, "fox": foxplay,"startv.com": startv,"ahaber.com.tr": ahaber, "apara": ahaber, "anews.com.tr": ahaber,
               "aspor.com.tr": ahaber, "a2tv": ahaber,"atv.com.tr": atv, "atv.json": atv,"dailymotion": dailymotion,"fileru": fileru,"supervideo.tv": supervideo,
               "kanald.com": kanald, "kanald.json": kanald,"dizibox": dizibox,"dizilab.pw": dizilab,"chefkoch24.eu": chefkoch24,"haberturk.com": haberturk,
               "bloomberght.com": haberturk,"dha.com": dha,"tv8.json": kanald,"tlctv.com": tlc, "dmax.com": tlc,"milyontv.com": milyontv,"ntv.com.tr": ntv,
               "womantv": ntv,"videobin.co": videobin,"gounlimited.to": gounlimited,"saruch.co": saruch,"yabancidizi": yabancidizi,
               "streamtheworld.com": streamtheworld,"chaturbate.com": chaturbate,"hdtvler.tv": hdtvler,"cnnturk.com": cnnteve2,
               "teve2.com.tr/canli-yayin": cnnteve2,"teve2.com.tr/diziler": teve2,"kanal7.com/dizi": kanal7dizi,"kanal7.com/ozel-haber": kanal7dizi,"kanal7.com/canli-izle": kanal7,
               "halktv.com.tr": halktv, "tv100.com": halktv,"kralmuzik.com.tr": kralmuzik,"numberone.com.tr": numberone,
               "tv360.com.tr": tv360, "m.star.com.tr/video/canli.asp": tv360,"ucankus.com": ucankus,"dreamturk.com.tr": dreamturk,"beyaztv.com.tr": beyaztv,
               "tvem.com.tr": tvem,"ulusal.com.tr": ulusal,"kanalb.com.tr": kanalb,"ekoturk.com": ekoturk,
               "womantv.com.tr": womantv,"tjk.org": tjk,"yabantv.com": yaban, "koytv.tv": yaban,"canliradyolar.org": canliradyolar,"ashemaletube.com": ashemale,
               "pornhub.com": pornhub,"clipwatching.com": clipwatching,"xvideos.com": xvideos,"sabantv.com": sabantv,"puhutv.com": puh,".plus": diziplus,
               "radyohome.com": radyohome,"onlineradiobox.com": onlineradiobox,"tv8.com.tr": tv8,"streamtape.com": streamtape,"7dak": dak7,"xnxx.com": dak7,
               "unlockxh1.com": xhamster, "xhamster.com": xhamster,"dizilla": dizilla, "dizipub": dizilla,"dizigom": dizigom,
               "koreanturk": koreanturk,"unutulmazfilmler": unutulmazfilmler,"filese.me": filese,"contentx.me": contentx,
               "ugurfilm": ugurfilm,"hdfilmcehennemi": hdfilmcehennemi,"webteizle": webteizle,"yilmaztv.com": yilmaztv,"k2s.cc": k2s,"vcdn.io": vcdn,
               "720pizle": a720pizle,"cloudvideo": cloudvideo,"mixdrop": mixdrop,"jetfilmizle": jetfilmizle,"plus4.asp": plus4,"sezonlukdizi": sezonlukdizi,
               "upstream.to": upstream,"streamsb": upstream,"videoseyred": videoseyred,"tele1": tele1,"ulketv": ulketv,"uptostream": uptostream,"filmegel": filmegel,"tvnet": tvnet}
    if  url is not None:
        if 'selection cancelled' not in url:
            for key in options.keys():
                if key in url:                                                                                    
                    try:
                        url = options[key](url)                                                                             
                    except:                                                                                    
                        url = None
                    if url is not None:
                        if 'selection cancelled' not in url:
                            if ('videoseyred' in url and 'Referer' not in url)  or 'fplay' in url or 'flmplayer' in url or 'plus4' in url or 'filese.me/iframe' in url or 'videobin.co/embed' in url or 'vcdn.io' in url or 'mixdrop' in url or 'cloudvideo' in url  or 'contentx.me/iframe' in url or 'dailymotion.com/embed' in url or 'youtube.com/embed' in url or 'youtube.com/watch' in url or ('gounlimited' in url and 'v.mp4' not in url) or ('upstream.to' in url and 'Referer' not in url) or ("vidmoly" in url and 'Referer' not in url) or ("closeload" in url and 'Referer' not in url) or ("odnoklassniki.ru" in url and 'Referer' not in url) or ("ok.ru" in url and 'Referer' not in url) or ("streamsb" in url and 'Referer' not in url) or ("mail.ru" in url and 'Referer' not in url) or ("fembed" in url and 'Referer' not in url):
                                 url = parse(url)
                    break
    return url
            
    
def youtube(url):
    url = url.replace('https://www.youtube.com/embed/','https://www.youtube.com/watch?v=')
    html = fetch(url)
    html = html.replace('\\','')
    if 'm3u8' in html:
        link = re.findall('"(http[^"]+m3u8)"', html, re.IGNORECASE)[0]
        page = fetch(link)
        url_main = '/'.join(link.split('/')[:-1]) + '/'
        page1 = fetch(url_main)
        qualitylist = re.findall(',RESOLUTION=.*?x([0-9]+)', page1)
        videolist= re.findall('(https.*?m3u8)', page1)
        return videolist[-1:][0]
    else:
        try: 
            v_id = re.findall('v=(.*?)$',url)[0]
        except:
            v_id = re.findall('embed\/(.*?)$',url)[0]
        embeds_url = 'https://www.y2mate.com/mates/en64/analyze/ajax'
        values = {'url' : url,
                  'q_auto' : 0,
                  'ajax' : 1 }
        the_page = fetch(embeds_url, data = values).replace('\\','')
        k__id = re.findall('k__id\s*=\s*"(.*?)"',the_page)[0]
        qualitylist = re.findall('a href="#" rel="nofollow">\s*(.*?)\s*\(\.mp4\)',the_page)
        res = select(qualitylist,qualitylist)
        if res is not None and res != 'selection cancelled':
            res = res.replace('p','')
            embeds_url = 'https://www.y2mate.com/mates/en64/convert'
            values = {'type' : 'youtube',
                      'token' : "",
                      'ftype' : "mp4",
                      'fquality' : res,
                      '_id' : k__id,
                      'v_id' : v_id }
            the_page = fetch(embeds_url, data = values).replace('\\','')
            return re.findall('a\s*href\s*=\s*"(.*?)"\s*rel', the_page)[0]
        else:
            return res
 
def uptostream(url):
    html = fetch(url)
    base = re.findall("window\.sources = JSON\.parse\(atob\('(.*?)'",html)
    acik_base = decode_base64(base[0])
    try:
        for i in re.finditer('"src":"([^"]+)","type":"[^"]+","label":"([^"]+)"', acik_base):
            qualitylist.append(i.group(2))
            videolist.append(i.group(1).replace('\\', ''))
    except:
        for i in re.finditer('source src=[\'|"](.*?)[\'|"].*?data-res=[\'|"](.*?)[\'|"]', acik_base):
            qualitylist.append(i.group(2))
            videolist.append('http:' + i.group(1))
    if not qualitylist:
        error(url)
    else:
        return select(qualitylist,videolist)
    
def canlitvlive(url):
    html = fetch(url)
    link = re.findall("player.src\('(.*?)'", html) 
    header = '#Referer='+url+'&User-Agent=' + UA
    return link[0] + header
    
def closeload(url):
    html = fetch(url, head={'Referer': url, 'Origin': url})
    Header = '#Referer='+url+'&User-Agent=' + UA +'&Origin=' + url
    link = re.findall('"contentUrl": "([^"]+)"', html)
    subtitles = re.findall('track src="(/vtt.*?)"',html)
    son = link[0] + Header
    if len(subtitles)>0:
        altyazilar = []
        for subtitle in subtitles:
            altyazilar.append('https://closeload.com' + subtitle)
        return [son, altyazilar]
    else:
        return son
    
def vidmoly(url):
    videolist1 = []
    if "flmplayer" in url:
       req = Request(url, headers={ 'User-agent': UA})
       html = urlopen(req)
       html1 = html.read()
       content = html1
       url = html.geturl()
    else:
       url =  url.replace("http:","")
       url =  url.replace("https:","")
       url= 'https:' + url
       content = fetch(url)
    try:
        window = re.findall("window.location\s*=\s*'(.*?)'",content)[0]
        url = url.replace('embed-',window)
        try:
            content = fetch(url)
        except:
            url = url.replace('.me','.to')
            content = fetch(url,head={'Referer': url})
    except:
        pass
    m3u8link = re.findall('([^"]+\.m3u8)',content)
    videolist = re.findall('([^"]+\.mp4)',content)
    qualitylist = re.findall(',label:"(.*?)"',content)
    subtitle = re.findall('file\s*:\s*"(/srt.*?)"',content)
   
    if qualitylist :
       for i in videolist:
           videolist1.append(i)
    else:
       videolist1.append(videolist[0])
       qualitylist.append('mp4')
    try:
       videolist1.append(m3u8link[0])
       qualitylist.append('m3u8')
    except:
       pass
    if len(subtitle)>0:
        res = select(qualitylist,videolist1)
        if res is not None:
            return [res, ['http://vidmoly.to' + subtitle[0]]]
    else:
        return select(qualitylist,videolist1)

def okru(url):
    url =  url.replace("http:","")
    url =  url.replace("https:","")
    url= 'https:' + url
    id1 = re.findall('https?://(?:www.)?(?:odnoklassniki|ok).ru/(?:videoembed/|dk\\?cmd=videoPlayerMetadata&mid=)(\\d+)', url)[0]
    nurl = 'https://ok.ru/videoembed/' + id1
    html = fetch(nurl)
    data = re.findall('''data-options=['"]([^'^"]+?)['"]''', html)[0]
    data = data.replace('\\', '').replace('&quot;', '').replace('u0026', '&')
    hata = re.findall('error":"([^"]+)', data)
    if hata:
        error(url)
    else:
        qualitylist = re.findall('{name:(\\w+),url:.*?}', data)
        videolist = re.findall('{name:\\w+,url:(.*?),seekSchema', data)
        res = select(qualitylist,videolist)
        if res is not None:
            return res + '#Referer=https://odnoklassniki.ru/'
    
def filmmodu(url):
    html = fetch(url)
    videolist = re.findall('"src":"(.*?)"',html)
    qualitylist = re.findall('"label":"(.*?)"',html)
    try:
        subtitle = re.findall('"subtitle":"(.*?)"',html)[0]
        subtitle1 = 'https://www.filmmodu.org' + subtitle
    except:
        subtitle1 = ''
    res = select(qualitylist,videolist)
    if res is not None:
        return [res,[subtitle1]]
    
def mailru(url):
    code = fetch(url)
    meta = re.findall('(?:metadataUrl|metaUrl)":.*?(//my[^"]+)', code)
    if meta:
        url2 = 'https:%s?ver=0.2.123' % meta[0]
        page = fetch(url2)
        key = re.findall('video_key[^;]+', page)
        if key:
            for match in re.finditer('url":"(//cdn[^"]+).+?(\\d+p)', page):
                videolist.append('http:' + match.group(1) + '#Referer=' + url+ '&User-Agent=' + UA + '&Cookie=' + key[0])
                qualitylist.append(match.group(2))
        if len(qualitylist) > 1:
            return select(qualitylist,videolist)
        else:
            return videolist[0]
    
def fembed(url):
    try:
        if 'vcdn' in url:
            url= url.replace('vcdn.io','feurl.com')
    except:
        pass
    url = url.replace('/v/','/api/source/')
    dt = re.findall('(?:www.fembed.net|fembed.net|feurl.com|fembed.com|www.fplay.cf|fplay.cf)', url, re.IGNORECASE)[0]
    dat = "r=&d=" + dt
    html = fetch(url, data=dat, head={'Referer': url})
    html = html.replace('\\','')
    for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
        qualitylist.append(match.group(2))
        videolist.append(match.group(1))
    if len(qualitylist) > 1:
        return select(qualitylist,videolist)
    else:
        return videolist[0]

def imdb(url):
    a= fetch(url)
    re1 = re.findall('"embedUrl":.*?"(.*?)"',a)[0]
    url2 = 'https://www.imdb.com' + re1.replace('video/imdb', 'videoembed')
    b = fetch(url2)
    for match in re.finditer('"videoUrl":"(.*?)"},{"definition":"(.*?)"', b):
        qualitylist.append(match.group(2))
        videolist.append(match.group(1).replace('\\u002F','/'))
    return select(qualitylist,videolist)
    
def s1cdn(url):
    page = fetch(url)
    base = re.findall('"#2(.*?)"',page)
    return decode_base64(re.sub('(//.*?=)','',base[0]))

def show(url):
    if not 'canli-yayin' in url and not 'canliyayin' in url:
        page = fetch(url)
        a = re.findall("data-ht='(.*?)'",page)[0].replace("'",'"')
        aa = re.findall('"name":"(.*?)","file":"(.*?)"',a)[:4]
        for i in aa:
            videolist.append(i[1].replace('\\', "") + '#Referer=https://www.showtv.com.tr')
            qualitylist.append(i[0])
        if len(qualitylist) > 1:
            return select(qualitylist,videolist)
        elif len(qualitylist) == 1:
            return videolist[0]
    else:
        page =fetch(url)
        return re.findall('ht_stream_m3u8":"(.*?)"', page)[0].replace('\/','/')
    
def yjco(url):
    page = fetch(url)
    a = re.findall('"file".*?:.*?"(.*?)".*?,.*?"label".*?:.*?"(.*?)"',page)
    for i in a:
        qualitylist.append(i[1])
        videolist.append(i[0])
    return select(qualitylist,videolist)
    
def foxplay(url):
    if not 'canli-yayin' in url:
        a = fetch(url)
        b = re.findall("videoSrc.*?:.*?'(.*?)'", a)
        return b[0]
    else:
        page =fetch(url)
        return re.findall("videoSrc\s*:.*?'(.*?)'\s*:", page)[0]
    
def startv(url):
    if 'canli-yayin' in url:
        page = fetch(url)
        link = re.findall('src: "(.*?)"',page)
        return "https:" + link[0]
    else:
        a = fetch(url)
        c = re.findall('"videoUrl".*?:.*?"(.*?)"',a)
        d = fetch(c[0])
        b = json.loads(d)
        return b["data"]["flavors"]["hls"]
        return b[0]
    
def atv(url):
    if 'atv.json' in url:
        page = fetch(url)
        link = re.findall('"hlsmanifest"\s*:\s*"(.*?)"',page)
        page1 = fetch(link[0])
        labels_links = re.findall('RESOLUTION=(.*?)x.*?\n(http.*?)\n',page1,re.DOTALL)
        return labels_links[1][1]
    else:
        headers = {'Referer':'http://www.atv.com.tr/'}
        data44 = fetch(url, None, headers)
        website_id = re.findall('data-videoid="(.*?)".*?data-websiteid="(.*?)"',data44)
        url44 = 'https://videojs.tmgrup.com.tr/getvideo/' + website_id[0][1] + '/' + website_id[0][0]
        data = fetch(url44, None, headers)
        url2, url1 = re.findall('"VideoUrl":"([^"]+)".*?"VideoSmilUrl":"([^"]+)"', data, re.IGNORECASE)[0]
        host = 'https://securevideotoken.tmgrup.com.tr/webtv/secure?url=' + url1 + '&url2=' + url2
        data2= fetch(host, None, headers)
        qualitylist =["m3u8","mp4"]
        videolist = re.findall('.*?Url":"(.*?)"', data2, re.IGNORECASE)
        if 'a2tv/canli-yayin' in url:
            return videolist[qualitylist.index("m3u8")]
        return select(qualitylist,videolist)
    
def dailymotion(url):
    if not 'embed' in url:
        url = url.replace('video','embed/video')
    page = fetch(url)
    link = re.findall('mpegURL","url":"(.*?)"',page)
    ff = fetch (link[0].replace('\\/','/'))
    try:
        d = re.findall('EXT.*?NAME="720"\\n(.*?)\\n',ff)[0]
    except:
        try:
            d = re.findall('EXT.*?NAME="480"\\n(.*?)\\n',ff)[0]
        except:
            url = re.findall('mpegURL","url":"(.*?)"', page)[0].replace('\/','/')
            page = fetch(url)
            try:
                d = re.findall('NAME="720",PROGRESSIVE-URI="(.*?)#', page)[0]
            except:
                d = re.findall('NAME="480",PROGRESSIVE-URI="(.*?)#', page)[0]
    return d

def fileru(url): 
    header={'Referer': 'https://dizilla.com'}
    url = url.replace('https:', '').replace('http:', '')
    url = 'http:' + url
    html = fetch(url, head=header)
    source_json = re.findall("getJSON\('(.*?)'", html)[0]
    source_link = 'http://fileru.net/' + source_json
    json_page = ufetch(source_link, head=header)
    json_now = json.loads(json_page)
    for source in json_now["sources"]:
        qualitylist.append(source["label"])
        videolist.append(source["file"])
    return select(qualitylist,videolist)
    
def supervideo(url):
    content = fetch(url)
    content = re.findall('<script type=\'text/javascript\'>eval(.*?)</script>', content, re.DOTALL)
    content = content[0].split('|')
    content = content[1:-2]
    file_index = content.index("file")
    main_url = "https://" + content[file_index + 3] + "." + content[file_index + 2] + "." + content[file_index + 1] + "/"
    hls_index = content.index("hls")
    urlset_index = content.index("urlset")
    ready_index = content.index("ready")
    diff = hls_index - urlset_index
    hls = ""
    for x in range(1, diff):
        hls = hls + content[hls_index-x]+ ","
    if diff == 1:
        hls = ',' + content[ready_index-2] + ','
    hls = 'hls/' + hls + '.' + content[urlset_index] + '/master.m3u8'
    return main_url + hls
     
def kanald(url):
    if 'kanald.json' in url or 'tv8.json' in url:
        page = fetch(url)
        link = re.findall('"hlsmanifest"\s*:\s*"(.*?)"',page)
        page1 = fetch(link[0])
        labels_links = re.findall('RESOLUTION=(.*?)x.*?\n(http.*?)\n',page1,re.DOTALL)
        return labels_links[1][1]
    else:
        html = fetch(url)
        embed_url = re.findall('"embedUrl":"(.*?)"',html)[0]
        page = fetch(embed_url)
        return re.findall('"contentUrl":"(.*?)"',page)[0] + '#User-Agent=' + UA

def dizibox(url):
    link = None
    providers = []
    links = []
    page = fetch(url)
    partial = re.findall('woca-linkpages-dd selectBox(.*?)span-eight', page, re.DOTALL)
    alternates = re.findall("(?:value='|href=')(.*?)'.*?>(.*?)<", partial[0])
    if len(alternates) > 1:
        for alternate in alternates:
            providers.append(alternate[1])
            links.append(alternate[0])
        referer = '/'.join(url.split('/')[:-2]) + '/'
        res = select(providers,links,1)
        if res is not None and res != 'selection cancelled':
            apage = fetch(res, head={'Referer': referer})
        elif res == 'selection cancelled':
            return res
    else:
        apage = page
        res = 1
    try:
        if res is not None:
            url = re.findall('<iframe\s*src="(.*?)"', apage, re.IGNORECASE)[0]
            ref = re.findall('(^.*?/)player',url)[0]
            html = fetch(url, head={'Referer': ref, 'Cookie':'dbxu='})
        else:
            return None
    except:
        error(url)
    if 'mecnun.php' in url:
        link = re.findall('file:"(.*?)"', html)[0]
    elif 'moly.php' in url:
        page = Unquote(html)
        page_atob = re.findall('atob\(unescape\("(.*?)"',page)[0]
        page = decode_base64(page_atob)
        link = re.findall('iframe src="(.*?)"',page)[0]
    elif 'indi.php' in url:
        link = re.findall('file:"(.*?)"',html)[0]
    elif 'haydi.php' in url:
        link = re.findall('frame src="(.*?)"',html)[0]
    elif 'king.php' in url:
        link1 = re.findall('frame src="(.*?)"',html)[0]
        link = link1 + '/sheila#User-Agent=' + UA + '&Referer=' + link1
        page = fetch(link, head={'Referer': link})
        name = 'cont' + ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        r = fetch(root2 + "/kodi/contentx/online.php", data ={"url": page, "name": name}, head={'X-Requested-With': 'XMLHttpRequest'})
        link = root2 + '/kodi/contentx/play.php?name=' + name
        link = link + '#Referer=https://dbx.molystream.net&User-Agent=' + UA
    return link

def chefkoch24(url):
    page = fetch(url)
    a = re.findall('source\s*src="(.*?)"\s*type=\'.*?\'\s*label\s*=\'(.*?)\'',page)
    for i in a:
        qualitylist.append(i[1])
        videolist.append(i[0].replace('https://','http://'))
    return select(qualitylist,videolist)
    
def haberturk(url):
    page = fetch(url)
    return re.findall('ht_stream_m3u8":"(.*?)"',page)[0].replace('\/','/')
    
def dha(url):
    page = fetch(url)
    return re.findall("video.src\s*=\s*'(.*?)'",page)[0].replace('\/','/')
    
def tv8(url):
    page = fetch(url)
    return re.findall('file"\s*:\s*"(.*?)"',page)[0]
    
def cnnteve2(url):
    page = fetch(url)
    link = re.findall('"contentUrl"\s*:\s*"(.*?)"',page)[0]
    if 'cnn' in url:
        ref_use = '#Referer=https://www.cnnturk.com/&User-Agent=' + UA
    elif 'teve2' in url:
        ref_use = '#Referer=https://www.teve2.com.tr/canli-yayin&User-Agent=' + UA
    return link + ref_use
    

def tlc(url):
    page = fetch(url)
    link = re.findall('liveUrl\s*=\s*"(.*?)"',page)[0]
    page = fetch(link)
    link1 = re.findall(',RESOLUTION=1280x720\n(.*?m3u8)', page)[0]
    if 'dmax'in url:
        link = 'https://jviqfbc2.rocketcdn.com/dmax.smil/' + link1
    return link
    
def ntv(url):
    page = fetch(url)
    return re.findall('srcLive\s*=\s*"(.*?)"',page)[0]
    
def kanal7(url):
    page = fetch(url)
    return re.findall("video-source'\s*,\s*'(.*?)'",page)[0] + '#Referer=https://www.kanal7.com/canli-izle&User-Agent=' + UA
        
def kanal7dizi(url):
    page = fetch(url)
    url = re.findall('<iframe src="(.*?)"', page)[0]
    page = fetch(url)
    kod = re.findall('play_video\s*=\s*"(.*?)"', page)[0]
    return 'https://www.dailymotion.com/embed/video/' + kod
        
def halktv(url):
    page = fetch(url)
    return re.findall('<iframe.*?src="(.*?)"',page)[0].replace('/embed/','/watch?v=')
    
def kralmuzik(url):
    page = fetch(url)
    return 'https://www.youtube.com/watch?v=' + re.findall("youtube.init\('(.*?)'",page)[0]
    
def numberone(url):
    page = fetch(url)
    return 'https:' + re.findall('<iframe.*?src="(.*?)"',page)[0]
    
def ahaber(url):
    a = 'https://securevideotoken.tmgrup.com.tr/webtv/secure?851521&url='
    if 'apara' in url:
        aa = 'http%3A%2F%2Ftrkvz-live.ercdn.net%2Faparahd%2Faparahd.m3u8'
    elif 'ahaber' in url:
        aa = 'https%3A%2F%2Ftrkvz-live.ercdn.net%2Fahaberhd%2Fahaberhd.m3u8'
    elif 'anews' in url:
        aa = 'http%3A%2F%2Ftrkvz-live.ercdn.net%2Fanewshd%2Fanewshd.m3u8'
    elif 'aspor' in url:
        aa = 'https%3A%2F%2Ftrkvz-live.ercdn.net%2Fasporhd%2Fasporhd.m3u8'
    elif 'a2tv' in url:
        aa = 'https%3A%2F%2Ftrkvz-live.ercdn.net%2Fa2tv%2Fa2tv.m3u8'
    referer = url
    url = a + aa
    content = fetch(url,head={'Referer': referer})
    return re.findall('"Url":"(.*?)"', content)[0]

def tv360(url):
    content = fetch(url)
    return re.findall('source src="(.*?)"', content)[0]

def ucankus(url):
    content = fetch(url)
    return re.findall('<source\s*src="(.*?)"', content)[0]
 
def dreamturk(url):
    content = fetch(url)
    vid_id = re.findall("var\s*_itemId\s*=\s*'(.*?)'", content)[0]
    url2 = 'https://www.dreamturk.com.tr/actions/content/media/' + vid_id
    content = fetch(url2)
    linkos = json.loads(content)
    return linkos["Media"]["Link"]["ServiceUrl"] + linkos["Media"]["Link"]["SecurePath"]
 
def beyaztv(url):
    content = fetch(url)
    return re.findall('"embedUrl"\s*:\s*"(.*?)"', content)[0]
 
def tvem(url):
    content = fetch(url)
    url2 = re.findall('<div class="live-area">\s*\n.*?<script src="(.*?)"></script>', content)[0]
    url2 = 'http:' + url2
    content = fetch(url2)
    url3 = re.findall('yayincomtr4="(.*?)"', content)[0]
    content = fetch('http:' + url3)
    link = re.findall('#EXT-X-STREAM-INF.*?RESOLUTION=720x486\n(.*?)$', content)[0]
    return 'http://cdn-TVEM.yayin.com.tr/TVEM/TVEM/' + link

def ulusal(url):
    content = fetch(url)
    content = Unquote(content)
    return re.findall('<iframe.*?src="(.*?)"',content)[0].replace('https://www.youtube.com/embed/','https://www.youtube.com/watch?v=')

def kanalb(url):
    content = fetch(url)
    return re.findall('file\s*:\s*"(.*?)"',content)[0]

def ekoturk(url):
    content = fetch(url)
    return re.findall('<iframe.*?src="(.*?)\?',content)[0].replace('/embed/','/watch?v=')

def womantv(url):
    url = 'https://appie.vidpanel.com/wmtv/video/live'
    content = fetch(url)
    content = json.loads(content)
    return content["video"]

def tjk(url):
    url = 'https://www.tjk.org/TR/YarisSever/Static/Canli'
    content = fetch(url)
    return re.findall("hls\s*:\s*'(.*?)'", content)[0]

def yaban(url):
    content = fetch(url)
    url2 =re.findall('<iframe.*?src="(.*?)"', content)[0]
    if not 'http' in url2:
        url2 = 'http:' + url2
    content = fetch(url2)
    return re.findall('file\s*:\s*"(.*?)"', content)[0]
        
def videobin(url):
    page = fetch(url)
    links = re.findall('sources:\s*\["(.*?)","(.*?)"', page)
    for link in links[0]:
        if 'm3u8' in link:
            qualitylist.append('m3u8')
            videolist.append(link)
        if 'mp4' in link:
            qualitylist.append('mp4')
            videolist.append(link)
    return select(qualitylist,videolist)
    
def gounlimited(url):
    page = fetch(url)
    link_code = re.findall("type\|(.*?)'.split", page)[0]
    link = link_code.split("|")
    return "https://" + link[1]+ ".gounlimited.to/" + link[0] + "/v.mp4#Referer=" + url
    
def saruch(url):
    vid_id = url.split('/')
    url = 'https://api.saruch.co/videos/' + vid_id[4] + '/stream?referrer=' +Quote(url)
    page = fetch(url)
    link = re.findall('"file":"(.*?)"', page)[0].replace('\/','/')
    de, en = re.findall('"de":"(.*?)","en":"(.*?)"', page)[0]
    link = link + '?de=' + de + '&en=' + en + '&.m3u8'
    showMessage("[COLOR orange][B]OTV_MEDIA[/B][/COLOR]","[COLOR red][B]Kodi bu linki desteklemiyor![/B][/COLOR]",4000)
    link = None
    return link
     
def streamtheworld(url):
    page = fetch(url)
    ip = re.findall('<ip>(.*?)</ip>',page)[0]
    radyo = re.findall('<mount>(.*?)</mount>', page)[0]
    return 'https://' + ip + '/' + radyo +'.mp3'
        
def chaturbate(url):
    content = fetch(url)
    content = re.findall('hls_source\\\\u0022:\s*\\\\u0022(.*?)\\\\u0022', content)[0].replace('\u002D','-')
    content1 = content.rsplit('/',1)[:-1][0]
    page = fetch(content)
    try:
        link = re.findall('RESOLUTION=1280x720\n(.*?)$', page)[0]
    except:
        link = re.findall('RESOLUTION=1280x720\n(.*?m3u8)', page)[0]
    link = content1 + '/' + link
    return link
        
def hdtvler(url): 
    page = fetch(url)
    values = re.findall('const data = (.*?);',page, re.DOTALL)[0].replace(' ','').replace('\n','').replace("'",'"').replace(':','":').replace('{', '{"').replace(',', ',"').replace('\r','')
    headers = {'Referer':url, 'X-Requested-With': 'XMLHttpRequest','Content-Type': 'application/json'}
    url="https://www.hdtvler.tv/Tv/TVShow"
    the_page = fetch(url, head=headers ,data=json.dumps(json.loads(values)))
    js = json.loads(the_page)
    try:
        return re.findall("file:'(.*?)'", js["result"]["playerBodyEnd"])[0]
    except:
        return re.findall('contentURL"\s*:\s*(.*?)"', js["result"]["playerBodyEnd"])[0]
        
def canliradyolar(url):
    content = fetch(url)
    url = re.findall('iframe\s*src="(.*?)"\s*name=', content)[0]
    content = fetch(url)
    return re.findall('"m4a"\s*:\s*"(.*?);',content)[0]
        
def ashemale(url):
    page = fetch(url)
    links_labels = re.findall('"src":"(.*?)","desc":"(.*?)",', page)
    for link in links_labels:
        qualitylist.append(link[1])
        videolist.append(link[0].replace("\\/","/"))
    return select(qualitylist,videolist)
    
def pornhub(url):
    html = fetch(url)
    sources = []
    fvars = re.search(r"qualityItems[^\[]+([^;]+)", html)
    if fvars:
        try:
            sources = json.loads(fvars.group(1))
            sources = [(src.get('text'), src.get('url')) for src in sources if src.get('url')]
        except:
            pass
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
            if 'hls' not in link:
                r = re.findall(r'(\d+p)', link, re.I)
                qual = r[0] if r else 'auto'
                sources.append((qual, link))
    for source in sources:
        videolist.append(source[1])
        qualitylist.append(source[0])
    return select(qualitylist,videolist)

def clipwatching(url):
    page = fetch(url)
    return re.findall('{src: "(.*?)"',page)[0] + '#Referer=http://streamingporn.xyz'
    
def xvideos(url):
    page = fetch(url)
    links = re.findall(r'''setVideo(?:Url)?(?P<label>(?:HLS|High|Low))\(['"](?P<url>[^"']+)''',page)
    for link in links:
        qualitylist.append(link[0])
        videolist.append(link[1])
    return select(qualitylist,videolist)

def sabantv(url):
    page = fetch(url)
    player_key = re.findall('playerKey\s*=\s*"(.*?)"', page)[0]
    url2 = 'https://saban.tiviplayer.com/player/data.json/' + player_key
    m3u8_page = json.loads(fetch(url2))
    return m3u8_page["playerSourceM3U"] + '#Referer=https://sabantv.com'

def puh(url):
    a = fetch(url)
    b = re.findall("'(PUHU_.*?)'", a)[0]
    c ='https://dygvideo.dygdigital.com/api/video_info?akamai=true&PublisherId=29&ReferenceId=' + b + '&SecretKey=NtvApiSecret2014'
    d = fetch(c)
    e = json.loads(d)
    try:
        return e["data"]["flavors"]["0"]["file_url_1"]
    except:
        return e["data"]["flavors"]["0"]["hls"]

def teve2(url):
    a = fetch(url)
    b = re.findall('itemprop="embedURL" href="(.*?)"', a)[0]
    b = b.replace('video','action/media')
    d = fetch(b)
    c = re.findall('"ServiceUrl"\s*:\s*"(.*?)"',d)[0]
    return c + '/' + re.findall('"SecurePath"\s*:\s*"(.*?)"',d)[0] + '#User-Agent=' + UA 

def milyontv(url):
    page = fetch(url)
    return re.findall("source\s*:\s*'(.*?)'", page)[0]

def dizilab(url):
    flag = True
    page = fetch(url)
    if 'fa fa-angle-down' in page:
        partial_page = re.findall('fa fa-angle-down(.*?)Sonra',page, re.DOTALL)[0]
        alts = re.findall('<a href="(.*?)">.*?\n.*?\n(.*?)\s*</a>',partial_page)
        for alt in alts:
            linkler.append(alt[0])
            kaynaklar.append(alt[1])
        res = select(kaynaklar,linkler,1)
        if res is not None and res != 'selection cancelled':
            page = fetch(res)
        else:
            flag = False
    if flag:        
        video_id = re.findall("loadVideo\('(.*?)'\)", page ,re.IGNORECASE)[0]
        url = 'https://dizilab.pw/request/php/'
        values = {'vid' : video_id,'tip' : '0','type' : 'loadVideo' }
        headers = {'Referer': 'dizilab.pw', 'X-Requested-With': 'XMLHttpRequest'}
        embed_page = fetch(url, data=values, head=headers)
        try:
            url2= re.findall('src=\\\\"(.*?)"', embed_page)[0].replace('\\','')
            page2 = fetch(url2)
            return re.findall('file:"(.*?)"', page2)[0]
        except:
            try:
                linkler = []
                kaliteler = []
                json_page =json.loads(embed_page)
                for link in json_page["sources"]:
                    linkler.append(link["file"])
                    kaliteler.append(link["label"])
                res = select(kaliteler,linkler)
                if res is not None:
                    return res + '#Referer=https://dizilab.pw&User-Agent=' + UA
                else:
                    return None
            except:
                if 'u kaynak attaya' in embed_page:
                    showMessage("[COLOR orange][B]OTV_MEDIA[/B][/COLOR]","[COLOR orange][B]Medya kaynak sitede silinmiş!!![/B][/COLOR]")
    else:
        return res
    
def diziplus(url):
    url1 = url.split("#")
    page = fetch(url1[0], head={'Referer': url1[0]})
    embed_link = re.findall('data-hhs="(.*?)"', page)[0]
    if '.plus' in embed_link:
        temp_page = fetch(embed_link, head={'Referer': embed_link})
        embed_link = re.findall('iframe src="(.*?)"',temp_page)[0]
    if 'flowcdn' in embed_link:
        second_page = fetch(embed_link, head={'Referer': "https://dizi.plus"})
        try:
            content = re.findall('<script type=\'text/javascript\'>(.*?)</script>', second_page, re.DOTALL)
            d = cPacker().unpack(content[0])
            stream_url = re.findall('file:"(.*?)"', d)[0]
        except:
            stream_url = re.findall('file:"(.*?m3u8)"', second_page)[0]
        
        if '#l=0' in url:
            try:
                try:
                    sub_link = re.findall('tracks.*?file:"(.*?)",label:"Turkce"', d)[0]
                except:
                    sub_link = re.findall('tracks.*?file:"(.*?)",label:"Turkce"', second_page)[0]
            except:
                try:
                    try:
                        sub_link = re.findall('tracks.*?file:"(.*?)"', d)[0]
                    except:
                        sub_link = re.findall('tracks.*?file:"(.*?)"', second_page)[0]
                except:
                    sub_link = ''
        else:
            sub_link = ''
        m3u = fetch(stream_url, head={'Referer': embed_link})
        pattern = re.findall("#EXT-X-MEDIA:.*?LANGUAGE=\"(.*?)\".*?AUTOSELECT=(.*?),.*?URI=\"(.*?)\"", m3u)
        last_part_m3u = re.findall('EXT-X-STREAM.*?RESOLUTION=1920x.*?\n(.*?)\n',m3u)[0] ##
##        last_part_m3u = "index-v1-a1.m3u8"
        if '#l=1' in url:
            for pat in pattern:
                if pat[0] == "tr":
                    part = re.findall('index-(.*?)\.m3u8',pat[2])
                    last_part_m3u = "index-v1-"+ part[0] +".m3u8"          
        else:
            for pat in pattern:
                if pat[0] != "tr":
                    part = re.findall('index-(.*?)\.m3u8',pat[2])
                    last_part_m3u = "index-v1-"+ part[0] +".m3u8"       
        m3u_link = stream_url.rsplit('/', 1)[0] + '/' + last_part_m3u
        if '#l=1' in url:
            return m3u_link + '#Referer=' + m3u_link
        else:
            try:
                ff = fetch(sub_link)
            except:
                ff = ''
            ff = re.sub('(\d+:\d+\.\d*) --> (\d+:\d+\.\d*)',r'00:\1 --> 00:\2',ff) 
            vvv = open(xbmc.translatePath(os.path.join(__addonuserdata__,"okey.vtt")), "w+")
            vvv.write(ff)
            vvv.close()
            return[m3u_link + '#Referer=' + m3u_link, [os.path.join(__addonuserdata__,"okey.vtt")]]
    else:
        page = fetch(embed_link, head={'Referer': embed_link})
        return re.findall('source: "(.*?)"',page)[1]
    
def radyohome(url):
    page = fetch(url)
    return re.findall('"hls","url":"(.*?)"',page)[0].replace('\/','/')

def streamtape(url):
    headers = {'Referer': 'https://streamtape.com/',
               'User-Agent': UA}
    page = fetch(url, head=headers)
    src = re.search(r'''ById\('vi.+?=\s*["']([^"']+)['"].+?["']([^"']+)''', page)
    link = 'https:'  + src.group(1) + src.group(2) + '&stream=1#Referer=https://streamtape.com/&User-Agent=' + UA
    return link
                      
def onlineradiobox(url):
    page = fetch(url)
    return re.findall('stream="(.*?)"',page)[0]

def dak7(url):
    page = fetch(url)
    if '7dak.com' in url:
        links = re.findall('source\s*src="(.*?)".*?title="(.*?)"', page)
        if links:
            for d in links:
                videolist.append(d[0])
                qualitylist.append(d[1])
        links = re.findall('source\s*src="(.*?)"', page)
        for d in links:
            videolist.append(d)
            qual = re.findall('quality=(.*?)$',d)[0]
            qualitylist.append(qual)
    elif 'xnxx.com' in url:
        links = re.findall("setVideoUrl(Low|High)\('(.*?)'", page)
        if links:
            for d in links:
                videolist.append(d[1])
                qualitylist.append(d[0])
    return select(qualitylist,videolist)
    
def dizigom(url):
    p = fetch(url)
    second = re.findall('"contentUrl"\s*:\s*"(.*?)"',p)[0]
    referer = '/'.join(url.split('/')[:-2]) + '/'
    pp = fetch(second, head={'Referer': referer})
    try:
        data_uri = re.findall('data-uri="(.*?)"',pp)
        sources = re.findall('data-short="(.*?)"',pp)
        test = sources[0]
        for source in sources:
            kaynaklar.append(source)
        data_u = select(kaynaklar,data_uri,1)
        if data_u is not None and data_u != 'selection cancelled':
            if data_u == 'refresh':
                evall = re.findall('\{(eval.*?\)\);)\}',pp)[0]
                d = cPacker().unpack(evall)
                try:
                    link = re.findall('"file"\s*:\s*"(.*?)"', d)[0].replace('\\\\/','/')
                except:
                    error(url)
            else:
                uri = data_u
                hashe = re.findall('video\/(.*?)$',uri)
                embeds_url = uri + '?do=getVideo'
                values = {'r' : referer,'s' : "",'hash' : hashe }
                d = fetch(embeds_url, data=values)
                link = re.findall('"file"\s*:\s*"(.*?)"', d)[0].replace('\/','/')
            return link
        else:
            return data_u
    except:
        evall = re.findall('\{(eval.*?\)\);)\}',pp)[0]
        d = cPacker().unpack(evall)
        try:
            link = re.findall('"file"\s*:\s*"(.*?)"', d)[0].replace('\\\\/','/')
            return link
        except:
            error(url)

def unutulmazfilmler(url):
    c = fetch(url, head={'Referer': url})
    ilk_embed = re.findall('<iframe.*?src="(.*?)"', c)[0]
    if not 'http' in ilk_embed:
        ilk_embed = 'https:' + ilk_embed
    provider = re.findall('(?:\/\/www|\/\/)(.*?)\.',ilk_embed)[0].capitalize()
    fi = 1
    co = 1        
    if 'Filese' in provider or 'Contentx' in provider:
        if 'Filese' in provider :
            provider = provider + str(fi)
            fi = fi + 1
        if 'Contentx' in provider:
            provider = provider + str(co)
            co = co + 1
        kaynaklar.append(provider)
        linkler.append(ilk_embed)
    embedz  = re.findall('<li class="part">.*?\n.*?<a href="(.*?)"',c)
    if len(embedz) > 0:
        for em in embedz:
            d = fetch(em, head={'Referer': em})
            embed = re.findall('<iframe.*?src="(.*?)"', d)[0]
            if not 'http' in embed:
                embed = 'https:' + embed
            provider = re.findall('(?:\/\/www|\/\/)(.*?)\.',embed)[0].capitalize()
            if 'Filese' in provider or 'Contentx' in provider:
                if 'Filese' in provider:
                    provider = provider + str(fi)
                    fi = fi + 1
                if 'Contentx' in provider:
                    provider = provider + str(co)
                    co = co + 1
                kaynaklar.append(provider)
                linkler.append(embed)
    if len(linkler) > 1:
        res = select(kaynaklar,linkler,1)
        return res
    elif len(linkler) == 1:
        return linkler[0]
    elif len(linkler) < 1:
        showMessage("[COLOR orange][B]OTV_MEDIA[/B][/COLOR]","[COLOR red][B]Kodinin oynatabileceği link yok![/B][/COLOR]",5000)
        return None

def dizilla(url):
    c = fetch(url, head={'Referer': url})
    try:
        partial = re.findall('Kaynak(.*?)dropdown inline',c,re.DOTALL)[0]
        kaynak_link = re.findall('<li class=".*?lightEscape">\s*\n\s*<a href="(.*?)".*?>\s*\n\s*(.*?)\s*<',partial)
    except:
        partial = re.findall('Kaynak Se(.*?)END ALTERNATIVE PLAYER',c,re.DOTALL)[0]
        kaynak_link = re.findall('<(?:span class=|a href=)"(.*?)".*?\n\s*(.*?)\s*<',partial)
    second = False
    for kl in kaynak_link:
        link = kl[0].replace('button-hole-link selected',url)
        page = fetch(link, head={'Referer': link})
        first = re.findall('<iframe.*?src="(.*?)".*?</iframe>', page)[0]
        if not 'https' in first:
            first = 'https:' + first
        if 'dizilla.org/vmplayer' in first: ##
            kod = first.split('?vid=')[1]##
            first = 'https://vidmoly.to/embed-' + kod + '.html'##
        linkler.append(first)
        prov = re.findall('//(?:www.|)(.*?)\.',first)[0]
        kk = kl[1].title()
        kaynaklar.append(kk)
    if len(kaynaklar) >1: 
        return select(kaynaklar,linkler,1)
    else:
        return linkler[0]
    
def filese(url): 
    page = fetch(url, head={'Referer': url})
    regex = re.findall("getJSON\('(.*?)'",page)
    x = regex[0]
    url = "https://filese.me" + x.replace("'", "")
    page = fetch(url, head={'User-Agent': 'Mozilla/5.0 OTV_MEDIA__KODI', 'Referer': url});
    qualitylist = re.findall('"label":"(.*?)"',page)
    videolist = re.findall('"file":"(.*?)"',page)
    res = select(qualitylist,videolist)
    if res is not None and res != 'selection cancelled':
        return res.replace('\\/','/') + '#Referer=https://filese.me&User-Agent=' + UA
    elif res == 'selection cancelled':
        return res
    
def contentx(url):
    page = fetch(url, head={'Referer': 'https://contentx.me/'})
    regex = re.findall('window.openPlayer\((.*?)\)',page)
    x = regex[0].split(',')[0].replace("'", "")
    url = "https://contentx.me/source.php?v=" + x
    page = fetch(url ,head={'Referer': 'https://contentx.me/'})
    link = re.findall('"file":"(.*?)"',page)[0].replace('\/','/')
    page = fetch(link ,head={'User-Agent': 'Mozilla/5.0 OTV_MEDIA__KODI','Referer': 'https://contentx.me/'})
    labels_links = re.findall('RESOLUTION=.*?x(.*?)\n(http.*?)\n',page,re.DOTALL)
    for a in labels_links:
        qualitylist.append(a[0])
        videolist.append(a[1])
    name = 'cont' + ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    link = select(qualitylist,videolist)
    if link is not None and link != 'selection cancelled':
        page = fetch(link, head={'Referer': 'https://contentx.me/'})
        r = fetch(root2 + "/kodi/contentx/online.php", data ={"url": page, "name": name}, head={'X-Requested-With': 'XMLHttpRequest'})
        link = root2 + '/kodi/contentx/play.php?name=' + name
        return link + '#Referer=https://contentx.me&User-Agent=' + UA
    elif link == 'selection cancelled':
        return link
    
def yabancidizi(url):
    page = fetch(url)
    alternatif_link_kodlari_partial = re.findall('series-tabs(.*?)mofycon',page,re.DOTALL)[0]
    alternatif_link_kodlari = re.findall('data-eid="(.*?)"\s*data-type="(.*?)"', alternatif_link_kodlari_partial)
    for b in alternatif_link_kodlari:
        lang = re.findall('\?l=(\d)$',url)[0]
        if str(lang) == str(b[1]):
            episode1  = b[0]
    links = []
    sources = []
    values = {'lang' : lang,
              'episode' : episode1,
              'type' : 'langTab'}
    page = fetch('https://yabancidizi.pw/ajax/service', data=values)
    bolum_embedleri = re.findall('data-hash=\\\\"(.*?)\\\\"\s*data-link=\\\\"(.*?)\\\\"', page)
    for bolum_embed in bolum_embedleri:
        values = {'hash' : bolum_embed[0].replace('\\','') ,
                  'link' : bolum_embed[1].replace('\\','') ,
                  'querytype' : 'alternate',
                  'type' : 'videoGet'}
        page1 = fetch('https://yabancidizi.pw/ajax/service', data=values)
        link = re.findall('"api_iframe":\s*"(.*?)"', page1)[0].replace('\\','')
        provider = re.findall('/api/(.*?)/',link)[0].capitalize()
        links.append(link)
        sources.append(provider)
    url = select(sources,links,1)
    if url is not None and url != 'selection cancelled': 
        referer = 'https://yabancidizi.pw/dizi'
        page= fetch(url, head={'Referer': referer})
        if 'api/cf' in url or 'api/indi' in url:
            link = re.findall('file:"(.*?)"', page)[0]
        elif 'api/moly' in url or 'api/ruplay' in url or 'api/saru' in url or 'api/goo' in url or 'api/superv' in url or 'api/drive' in url:
            link = re.findall('iframe src="(.*?)"', page)[0]
            if 'api/drive' in url:
                link = link.replace("ydx", "dbx") + "/sheila"
                name = 'cont' + ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                page = fetch(link, head={'Referer': 'https://yabancidizi.pw/'})
                r = fetch(root2 + "/kodi/contentx/online.php", data ={"url": page, "name": name}, head={'X-Requested-With': 'XMLHttpRequest'})
                link = root2 + '/kodi/contentx/play.php?name=' + name
                link = link + '#Referer=https://dbx.molystream.net&User-Agent=' + UA                
        return link
    if url == 'selection cancelled':
        return url
    
def fullhdfilmizlesene(url):
    url1 = url.split('?')[0]
    url_onek = '/'.join(url1.split('/')[:-3])
    sec = re.findall('\?l=(\d)',url)[0]
    try:
        page = fetch(url1, head={'Referer': url1})
    except:
        pass
    flag = False
    try:
        code = re.findall('"vidid":"(.*?)","name":"(.*?)","nameTxt":"(.*?)".*?"types":"(.*?)"',page)
        if 'tr,en' in code[0][3]:
            flag = True
    except:
        code = re.findall('"vidid":"(.*?)","name":"(.*?)","nameTxt":"(.*?)"',page)
    sources = []
    for cod in code:
        if 'atom' in cod[2].lower() or 'turbo' in cod[2].lower() or 'vmol' in cod[2].lower() or 'voltran' in cod[2].lower():
            sources.append(cod)
    if len(sources) > 1:
        for source in sources:
            kaynaklar.append(source[1])
        code = select(kaynaklar,sources,1)
        if code is None:
            return None
        elif code ==  'selection cancelled':
            return code
    elif len(sources) == 1:
        code = sources[0]
    elif len(sources) < 1:
        return None
    if not flag:
        url2 = url_onek + '/player/api.php?type=t&get=video&name='+ code[1] + '&id=' + code[0]
    else:
        if sec == "0":
            url2 = url_onek + '/player/api.php?type=t&get=video&name='+ code[1] + '&id=' + code[0] + '&pno=tr' 
        if sec == "1":
            url2 = url_onek + '/player/api.php?type=t&get=video&name='+ code[1] + '&id=' + code[0] + '&pno=en'
    page = fetch(url2, head={'Referer': url2})
    try:
        url3 = re.findall('src="(.*?)"', page)[0]
    except:
        url3 = re.findall('src=\"(.*?)\""', page)[0]
    if 'vidmoly' in url3:
        return url3.replace('\/','/')
    else:                  
        page = fetch(url3, head={'Referer': url3})
        try:
            m3u8_raw = re.findall('"file"\s*:\s*"(.*?)"',page)[0].replace("\\x", "")
            if isPy3 == False:
                m3u8 = m3u8_raw.decode('hex')
            else:
                m3u8 = bytes.fromhex(m3u8_raw).decode('utf-8')
            cc_json = re.findall('jwSetup\.tracks\s*=\s*(\[.*?\])',page)[0]
            json_data = json.loads(cc_json)
            subtitles = []
            try:
                ccs = json_data[0]["file"]
                if 'http' in ccs:
                    subtitles.append(ccs)
            except:
                ccs = json_data[1]["file"]
                if 'http' in ccs:
                    subtitles.append(ccs)
            if sec == '1':
                return [m3u8,subtitles]
            elif sec == '0':
                return m3u8
        except:
            return 'https:' + re.findall('"hls"\s*:\s*"(.*?)"',page)[0].replace("\\/", "/")

def koreanturk(url):
    page= fetch(url, head={'Referer': url})
    part = re.findall('tab-content icerikler(.*?)text/css', page, re.DOTALL)[0]
    embeds = re.findall('id="(.*?)".*?(?:iframe.*?src|a.*?href)="(.*?)"', part)
    linklist = []
    providerlist = []
    for embed in embeds:
        if "ok.ru" in embed[1] or "vidmoly.me" in embed[1] or "fembed.com" in embed[1] or "videobin.co" in embed[1] or "gounlimited.to" in embed[1] or "vidmoly.me" in embed[1] or "dailymotion" in embed[1] :
            embedus = embed[1]
            if 'dailymotion' in embed[1]:
                embedus = 'https:' + re.findall('^(.*?)\?', embed[1])[0]
            if 'vidmoly' in embed[1]:
                embedus = 'https:' + embed[1]
            linklist.append(embedus)
            providerlist.append(embed[0])
    return select(providerlist,linklist,1)

def filmakinesi(url):
    lang = re.findall('\?l=(\d)$',url)[0]
    url = url.split('?')[0]
    page = fetch(url, head={'Referer': url})
    try:
        alts = re.findall("<div class=\"film_part hidden-mobile\">(.*?)<i class=\"fa fa-comment\"", page)[0]
    except:
        pass
    alt = re.findall("<span>(.*?)</span>",alts)
    alt_link = re.findall("<a href=(.*?) class",alts)
    alt_link.insert(0, url)
    for al in alt:
        if 'Altyaz' in al:
            flag = True
            break
        else:
            flag = False
    x = 0
    for al in alt:
        if lang == '0' and flag:
            if 'Altyaz' in al and 'Fragman' not in al and 'up' not in al.lower():
                kaynaklar.append((al.lower().replace('tek ','').replace('altyazılı ','')).capitalize() )
                linkler.append(alt_link[x])
        elif not flag:
            if 'Fragman' not in al and 'up' not in al.lower():
                kaynaklar.append((al.lower().replace('tek ','').replace('altyazılı ','')).capitalize() )
                linkler.append(alt_link[x])
        elif lang == '1' and flag:
            if 'Altyaz' not in al and 'Fragman' not in al and 'up' not in al.lower():
                kaynaklar.append((al.lower().replace('tek ','').replace('altyazılı ','')).capitalize() )
                linkler.append(alt_link[x])
        x = x + 1
    if len(kaynaklar) == 1:
        son_link = linkler[0]
    if len(kaynaklar) > 1:
        son_link = select(kaynaklar,linkler,1)
    if son_link is not None and son_link != 'selection cancelled':
        page = fetch(son_link, head={'Referer': son_link})
        return re.findall("<p><iframe.*?data-src=(.*?) \s*.*?></iframe></p>", page)[0]
    else:
        return son_link

def ugurfilm(url):
    c = fetch(url)
    player = re.findall('<iframe.*?src="(.*?)"', c)[0]
    if 'ugurfilm.com/player/play.php' in player :
        vid_id = player.split("=")[-1:][0]
        d = fetch(player, head={'Referer': player})
        embedsz = re.findall('class="c-dropdown__item"\s*data-dropdown-value="(.*?)" data-order-value="(\d+)"',d)
        for embed in embedsz:
            embeds_url = "https://ugurfilm.com/player/ajax_sources.php"
            values = {"vid" : vid_id,"alternative" : embed[0],"ord" : embed[1] }
            headers = {"Referer": "https://ugurfilm.com", "X-Requested-With": "XMLHttpRequest"}
            the_page = fetch(embeds_url, data=values, head=headers)
            embed_link = re.findall('"iframe":"(.*?)"',the_page)[0].replace('\/','/')
            if not 'http' in embed_link:
                embed_link = 'https:' + embed_link
            provider = re.findall('(?:\/\/www|\/\/)(.*?)\.',embed_link)[0].capitalize()
            if 'mail' in embed_link:
                kaynaklar.append('Mailru')
                linkler.append(embed_link)
            elif 'fembed' in embed_link:
                kaynaklar.append('Fembed')
                linkler.append(embed_link)
            elif 'ok.ru' in embed_link:
                linkler.append(embed_link)
                kaynaklar.append('Odk')
            elif 'odnoklassniki' in embed_link:
                kaynaklar.append('Odk')
                linkler.append(embed_link)
            elif 'youtube' in embed_link:
                kaynaklar.append('Youtube')
                linkler.append(embed_link)
    else:
        try:
            partial = re.findall('parttab tab-aktif(.*?)</iframe>',c, re.DOTALL)
            embedler = re.findall('href="(.*?)"',partial[0])
            for e in embedler:
                h = fetch(e)
                embed_link = re.findall("iframe.*?src=(?:'|\")(.*?)(?:'|\")",h)[0]
                if not 'http' in embed_link:
                    embed_link = 'https:' + embed_link
                
                provider = re.findall('(?:\/\/www|\/\/)(.*?)\.',embed_link)[0].capitalize()
                if 'mail' in embed_link:
                    kaynaklar.append('Mailru')
                    linkler.append(embed_link)
                elif 'fembed' in embed_link:
                    kaynaklar.append('Fembed')
                    linkler.append(embed_link)
                elif 'ok.ru' in embed_link:
                    kaynaklar.append('Odk')
                    linkler.append(embed_link)
                elif 'odnoklassniki' in embed_link:
                    kaynaklar.append('Odk')
                    linkler.append(embed_link)
                elif 'youtube' in embed_link:
                    kaynaklar.append('Youtube')
                    linkler.append(embed_link)
        except:
            embed_link = re.findall('iframe.*?src="(.*?)"',c)[0]
            if 'youtube' in embed_link:
                kaynaklar.append('Youtube')
                linkler.append(embed_link)
        
    return select(kaynaklar,linkler,1)

def get_embed_url_hdfilmcehennemi(url):
    page = fetch(url, head={'Referer': url})
    try:
        embed = ''
        embed_64 = re.findall("<script>var.*?'(.*?)'",page)[0]
        embed_decoded = decode_base64(embed_64).lower()
        embed_hdfilm = re.findall('iframe.*?src\s*=\s*(?:"|\')(.*?)(?:"|\')',embed_decoded)[0]
        if 'moly' in embed_hdfilm:
            if 'watch.php' in embed_hdfilm:
                embed = 'https://vidmoly.to/embed-' + embed_hdfilm.replace('https://www.hdfilmcehennemi2.pw/watch.php?v=v/','') + '.html'
            else:
                embed = 'https:' + embed_hdfilm
        elif 'odnok' in embed_hdfilm or 'ok.ru' in embed_hdfilm:
            if 'watch.php' in embed_hdfilm:
                embed = 'https://odnoklassniki.ru/videoembed/' + embed_hdfilm.replace('https://www.hdfilmcehennemi2.pw/watch.php?v=ok/','')
            else:
                embed = 'https:' + embed_hdfilm
        elif 'up' in embed_hdfilm:
            if 'watch.php' in embed_hdfilm:
                embed = 'https://uptostream.com/iframe/' + embed_hdfilm.replace('https://www.hdfilmcehennemi2.pw/watch.php?v=up/','')
            else:
                embed = 'https:' + embed_hdfilm
        elif 'fembed' in embed_hdfilm:
            if 'watch.php' in embed_hdfilm:
                embed = 'https://www.fembed.net/v/' + embed_hdfilm.replace('https://www.hdfilmcehennemi2.pw/watch.php?v=fembed/','')
            else:
                embed = 'https:' + embed_hdfilm        
    except:
        embed = re.findall('iframe.*?src\s*=\s*(?:"|\')(.*?)(?:"|\')',page)[0]
        if 'fembed' in embed:
            embed = 'https:' + embed
    return embed

def hdfilmcehennemi(url):
    lang = re.findall('\?l=(\d)$',url)[0]
    url = url.split('?')[0]
    page = fetch(url, head={'Referer': url})
    partial = re.findall('keremiya_part">(.*?)class="vrkust', page, re.DOTALL)[0]
    first = re.findall('<span>(.*?)</span>',partial)[0]
    first_alt = (url,first)
    alternatives = re.findall('href="(.*?)" class="post-page-numbers"><span>(.*?)<', partial)
    alternatives.append(first_alt)
    for alt in alternatives:
        embed_link = get_embed_url_hdfilmcehennemi(alt[0])
        try:
            provider = re.findall('(?:\/\/www.|\/\/)(.*?)\.',embed_link)[0].capitalize()
        except:
            provider = 'boncuk'
        if 'Odnoklassniki' in provider:
            provider = 'ODK'
        if 'My' in provider:
            provider = 'Mailru'
        if 'Uptostream' in provider:
            provider = 'Upto'
        if 'outube' not in provider and 'oncuk' not in provider and 'pto' not in provider:
            if lang == "0" and 'ALTYZ' in alt[1]:
                linkler.append(embed_link)
                kaynaklar.append(provider)
            elif lang == "1" and 'TR' in alt[1]:
                linkler.append(embed_link)
                kaynaklar.append(provider)
            elif 'ALTYZ' not in alt[1] and 'TR' not in alt[1]:
                linkler.append(embed_link)
                kaynaklar.append(provider)                    
    return select(kaynaklar,linkler)
    
def webteizle(url):
    page = fetch(url)
    wip  = re.findall("data-id=\"(.*?)\"", page)[0]
    if 'dublaj' in url:
        dub = 0
    elif 'altyazi' in url:
        dub = 1
    if 'sezon' not in url and 'bolum' not in url: ##
        values = {'filmid' : wip, 'dil' : dub}
    else:##
        sez_bol = re.findall('(\d*)-sezon-(\d*)-', url)##
        values = {'filmid' : wip, 'dil' : dub, 's': sez_bol[0][0], 'b': sez_bol[0][1]}##
    page = fetch("https://webteizle.vip/ajax/dataAlternatif.asp", data=values, head = {"Referer": url})
    dub_json = json.loads(page)
    links = []
    embeds = []
    for embed in dub_json["data"]:
        values = {'id': embed["id"]}
        emb_content = fetch("https://webteizle.vip/ajax/dataEmbed.asp", data=values, head = {"Referer": url})
        if 'bir yerde bulamad' in emb_content:##
            showMessage("[COLOR orange][B]OTV_MEDIA[/B][/COLOR]","[COLOR red][B]Bu link kaynak sitede silinmiş![/B][/COLOR]")##
            return##
        try:
            prov = re.findall("<script>(.*?)\('.*?',.*?\);</script>", emb_content, re.DOTALL)[0]
            emb_lin = re.findall("<script>.*?\('(.*?)',.*?\);</script>", emb_content, re.DOTALL)[0]            
        except:
            continue
        if prov == "sper":
            embeds.append("Super")
            links.append("https://supervideo.tv/e/"+emb_lin)
        elif prov == "fembed":
            embeds.append("fembed")
            links.append("https://www.fembed.net/v/"+emb_lin)
        elif prov == "vidmoly":
            embeds.append("VidMoly")
            links.append("https://vidmoly.to/embed-"+emb_lin+".html")
        elif prov == "mailru":
            embeds.append("mailru")
            var = emb_lin.split("/")
            links.append("https://my.mail.ru/"+var[0]+"/"+var[1]+"/video/embed/"+var[2]+"/"+var[3])
        elif prov == "okru":
            embeds.append("ODK")
            links.append("https://ok.ru/videoembed/"+emb_lin)
    if len(links)>1:
        return select(embeds,links,1)
    if len(links) == 1:
        return links[0]

def yilmaztv(url):
    return url + '#Referer=https://www.yilmaztv.com&User-Agent=' + UA

def xhamster(url):
    page = fetch(url)
    return 'https://unlockxh1.com' + re.findall('"hls":\{"url":"(.*?)"',page)[0].replace('\/','/')
        
def k2s(url):
    api_base = 'https://api.k2s.cc/v1'
    headers = {'Referer': url,
               'Origin': 'https://k2s.cc'}
    data = {"grant_type": "client_credentials",
            "client_id": "k2s_web_app",
            "client_secret": "pjc8pyZv7vhscexepFNzmu4P"}
    code = url.split('/')[4]
    page = fetch(api_base + '/auth/token', data=data, head=headers)
    access_token = json.loads(page).get('access_token')
    headers = {'Referer': url,
               'Origin': 'https://k2s.cc',
               'Authorization': 'Bearer '+access_token}
    page = fetch(api_base + '/files/' + code  + '?embed=permanentAbuse',head=headers)
    link = json.loads(page).get('videoPreview').get('video')
    headers.pop('Authorization')
    return link

def vcdn(url):
    code = url.split('/')[4]
    url = 'https://femax20.com/api/source/' + code
    values = {"d": "femax20.com",
              "r":""}
    page = fetch(url, data=values, head= {"Referer": url})
    values = re.findall('"file":"(.*?)","label":"(.*?)"',page.replace('\\',''))
    for value in values:
        qualitylist.append(value[1])
        videolist.append(value[0])
    return  select(qualitylist,videolist)

def a720pizle(url):
    page = fetch(url)
    partial = re.findall('menu oval alternatif(.*?)download',page,re.DOTALL)
    alts = re.findall('a href="(.*?)".*?\n\s*(.*?)\s',partial[0])
    for alt in alts:
        kaynaklar.append(alt[1].title())
        linkler.append(alt[0])
    url = select(kaynaklar,linkler,1)
    if url is not None and url != 'selection cancelled':
        page = fetch(url)
        try:
            return re.findall('<iframe src="(.*?)"',page)[0]
        except:
            kod = re.findall("<script>mailru\('(.*?)'",page)[0]
            return ' https://my.mail.ru/' + kod.replace('_myvideo','video/embed/_myvideo')
    else:
        return url

                       

               #Cookie: aff=3528986

def uptostream(url):
        cookies = GestionCookie().Readcookie("uptobox")
        import requests, re
        url=url.replace('https://uptostream.com','https://uptobox.com').replace('iframe/','')
        page = fetch(url,head= {'Cookie': 'aff=3528986','Referer': 'https://uptobox.com/'})
        logger.info("alt_links : %s" % page)
        tok = re.search('<a href="(https://www44.uptobox.com/dl.+?)"', page).group(1) +'#Cookie=_ga=GA1.2.313382106.1621875296; _gid=GA1.2.727117019.1621875296; _gat=1' + UA 
       
        return  tok

                 
def filmegel(url):
        page = fetch(url,head= {"Referer": url})
        eval = re.findall('(eval\(function.*?)\n',page)
        page = cPacker().unpack(eval[0])
        return re.findall('file:"(.*?)"',page)[0]
    
def cloudvideo(url):
        page = fetch(url)
        eval = re.findall('ipt">(eval.*?)\n',page)
        page = cPacker().unpack(eval[0])
        return re.findall('src:"(.*?)"',page)[0]
    
def mixdrop(url):
    page = fetch(url)
    eval = re.findall('(eval\(function.*?)\n',page)
    page = cPacker().unpack(eval[0])
    link = re.findall('MDCore.wurl="(.*?)"',page)[0]
    if link.startswith('//'):
        link = 'https:' + link
    return link


def jetfilmizle(url):
    page = fetch(url)
    partial = re.findall('<div class="col-md-19">(.*?)<center>',page)[0]
#    alt_names = re.findall('<span>(.*?)</span>',partial)
    remo = re.findall('href="(.*?)".*?<span>(.*?)</span>',partial)
    
#    remo = ["Zeus","JetPlay","Denver","Oslo","Tokyo","Vip","BinPlay","JPlay","Plat-1","Mail","FETube","Aparat","Vidmoly","CPlay","MixPlay"]
    for alt_links,alt_names in remo:
        if not 'http' in alt_links:
          alt_links='https://jetfilmizle.live'+ alt_links
        #logger.info("alt_links : %s" % alt_links)
        try:
            #index = alt_names.index(rem)
            kaynaklar.append(alt_names)
            linkler.append(alt_links)
        except:
            pass
    if len(kaynaklar)>0:
        url = select(kaynaklar, linkler, 1)
    else:
        showMessage("[COLOR orange][B]OTV_MEDIA[/B][/COLOR]","Oynatılabilecek kaynak bulunamadı!")
        return None
    if url is not None and url != 'selection cancelled':
        page = fetch(url)
        url = re.findall("iframe src='(.*?)'",page)[0]
       # logger.info("url : %s" % url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
                                'Accept': 'application/json, text/javascript, */*; q=0.01',
                                'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                                'Connection': 'keep-alive',
                                'Referer': 'https://jetfilmizle.live/',
                                'X-Requested-With': 'XMLHttpRequest'}

        if 'https://jetv.xyz/' in url:
            data = ""     
            page = fetch(url, data=data , head=headers)
            page = page.replace(" server + ","") 
            url2 = re.findall('secure: true,url:"(.*?)"', page, re.IGNORECASE)[0]
            link = fetch(url2,  head=headers)
            son_url= re.findall('sources:.*?file:"(.*?)"', link, re.IGNORECASE)[0]
            return son_url
        if 'mixdrop' in url or 'videobin' in url:
            if url.startswith('//'):
                url = 'https:' + url
            return url
        if 'aparat.cam' in url:
            page = fetch(url, head=headers)
            link = re.findall('src: "(.*?)"',page)
            return link[0]
        if 'gp.jetcdn' in url  or 'yjco.xyz' in url or "jetfilmvid" in url:
            page = fetch(url, head=headers)
            page = page.replace("\\","")    
            if "iframe src=" in page:
                url = re.findall('iframe src=["\'](.*?)["\']', page, re.IGNORECASE)[0]
                return url
            if '"label":"' in page:
                for match in re.finditer('"label":"([^"]+)","type":"[^"]+","file":"([^"]+)"', page):
                    qualitylist.append(match.group(1))
                    videolist.append(match.group(2))
                return select(qualitylist,videolist)
            if 'm3u8' in page:
                son_url = re.findall('"?file"? ?: ?"([^"]+)"', page, re.IGNORECASE)[0]
                return son_url
            else:
                for match in re.finditer('"?file"? ?: ?"([^"]+)", ?"(?:type|label)": ?"([^"]+)"', page):
                    qualitylist.append(match.group(2))
                    videolist.append(match.group(1))
                if len(qualitylist) > 1:
                    return select(qualitylist,videolist)
                elif len(qualitylist) == 1:
                    return videolist[0]
                else:
                    error(url)
        if 'hls.jetcdn' in url:
            data = ""
            key = re.findall('(?:key|id)=(.*?)$', url, re.IGNORECASE)[0]
            url2 = 'https://hls.jetcdn.co/getHost/' + key
            link = fetch(url2, data=data , head=headers)
            son_url = decode_base64(link)
            return son_url
        
        if 'api.ocdn' in url:
            if '/fe/' in url:
                url = url.replace('https://api.ocdn.top/fe/embed-', 'https://vcdn.io/v/').replace('.html','')
                return url
            if '/clo/' in url:
                key = re.findall('embed-(.*?).html', url, re.IGNORECASE)[0]
                data = {"vars": key}                       
                link = fetch('https://api.ocdn.top/clo/api.php',data=data,head=headers)
                link2 = re.findall(r'src="(\S+)[\s|\.]', link)[0] + '.html'
                return link2
            if '/o1/' in url:
                link = fetch(url, head=headers)
                link2 = re.findall(r'src="(\S+)[\s|\.]', link)[0] + '.html'
                return link2
            if '/vi/' in url:
                url = url.replace('https://api.ocdn.top/vi/', 'https://vidmoly.to/')
                return url
        if 'jetcdn.co/api/' in url:
            if url.startswith('//'):
                url = 'https:' + url
            page = fetch(url)
            link = re.findall('src="(.*?)"', page)[0]
            return link
    else:
        return 'selection cancelled'
    
def epg(settings, tumu = 0):
    descs = []
    channels = []
    if tumu == 0:
        old = settings.getSetting("epg_now")
        now = datetime.datetime.today().strftime('%H')
        if old != now:
            try:
                settings.setSetting("epg_now", now)
                url = 'https://www.api.tvyayinakisi.com/new/index.php?lang=tr&show=tv_simdi&_=1612815105729'
                page = fetch(url,head={'Referer': 'https://www.tvyayinakisi.com/'})
                with codecs.open(xbmc.translatePath(os.path.join(__addonuserdata__,"now")),"w","utf-8-sig") as outfile:
                    outfile.write(page)
            except:
                pass
        page = codecs.open(xbmc.translatePath(os.path.join(__addonuserdata__,"now")),'r',"utf-8-sig").read()        
    else:
        old = settings.getSetting("epg_day")
        now = datetime.datetime.today().strftime('%Y%m%d')
        if old != now:
            try:
                settings.setSetting("epg_day", now)
                url ='https://www.api.tvyayinakisi.com/new/index.php?lang=tr&show=tv_bugun&_=1612945622865'
                page = fetch(url,head={'Referer': 'https://www.tvyayinakisi.com/'})
                
                with codecs.open(xbmc.translatePath(os.path.join(__addonuserdata__,"day")),"w","utf-8-sig") as outfile:
                    outfile.write(page)
            except:
                pass
        page = codecs.open(xbmc.translatePath(os.path.join(__addonuserdata__,"day")),'r',"utf-8-sig").read()
        return page
    js = json.loads(page)
    for i, j in enumerate(js):
        channel =  j["0"]["channel"].lower().replace(' hd','').replace(' tv','')
        name = j["0"]["name"]
        start = j["0"]["start"]
        finish = j["0"]["finish"]
        type = j["0"]["type"]
        try:
            name1 = j["1"]["name"]
            start1 = j["1"]["start"]
            finish1 = j["1"]["finish"]
            type1 = j["1"]["type"]
        except:
            name1 = ""
            start1 = ""
            finish1 = ""
            type1 = ""
        if type == '':
            type = to_utf8('Diğer')
        descs.append('[COLOR orange]' + start + '-' + finish + '[/COLOR] ' + name + '(' + type + ')\n\n' + '[COLOR orange]' + start1 + '-' + finish1 + '[/COLOR]  ' + name1 + '(' + type1 + ')')
        channels.append(channel.lower().replace(' ',''))
    return [channels, descs]

def dizidimi(url):
    url = url.split('?')[0]
    page = fetch(url)
    return re.findall('class=video-container><p><iframe.*?src=(.*?)\s',page)[0]

def plus4(url):
    if url.startswith('/player/'):
        url = 'https://sezonlukdizi.vip' + url
    page = fetch(url, head={"Referer":url})
    videolist = re.findall('"file":"(.*?)"', page)
    qualitylist = re.findall('"label":"(.*?)"', page)
    res = select(qualitylist, videolist)
    if res is not None and res != 'selection cancelled':
        return res + "#Referer=https://sezonlukdizi.vip"
    elif res == 'selection cancelled':
        return res
    
def upstream(url):
    page = fetch(url)
    evall = re.findall("text/javascript'>(.*?)\n", page)[0]
    d = cPacker().unpack(evall)
    try:
        link = re.findall('file:"(.*?mp4)"', d)[0]
    except:
        link = re.findall('file:"(.*?)"', d)[0]
    return link + "#Referer=" + url + "&User-Agent=" + UA

def videoseyred(url):
    page = fetch(url)
    part = re.findall("playlistUrl='(.*?)'", page)[0]
    json_link = 'https://videoseyred.in' + part
    page = fetch(json_link, head = {"Referer": url})
    jpage = json.loads(page)
    link = jpage[0]["sources"][0]["file"]
    sub = ''
    for j in jpage[0]["tracks"]:
        if "label" in j:
            if 'T' in j["label"]:
                sub = j["file"]
    sonek = '#Referer=' + url + '&User-Agent=' + UA
    if sub == "":
        return link + sonek
    else:
        return [link + sonek, [sub]]

def sezonlukdizi(url):
    alt_names = []
    alt_ids = []
    url_lang = url.split('?l=')
    url = url_lang[0]
    lang = url_lang[1]
    if lang == "0":
        dil = "1"
    else:
        dil ="0"
    page = fetch(url)
    bid = re.findall('<div\s*bid="(\d*)"\s*did=', page)[0]
    ajax_page = fetch('https://sezonlukdizi.vip/ajax/dataAlternatif.asp', data = {"bid": bid, "dil": dil})
    if 'eklenmedi' not in ajax_page:
        if not isPy3:
            jso = json.loads(ajax_page.decode('UTF-8','ignore'))
        else:
            jso = json.loads(ajax_page.replace('Ý','İ'))
        for js in jso["data"]:
            if not isPy3:
                alt_names.append(js["baslik"].replace('ngilizce', 'İngilizce'))
            else:
                 alt_names.append(js["baslik"].title())
            alt_ids.append(js["id"])  
        remo = ["Netu","Multi","Uptobox"]
        for rem in remo:
            try:
                alt_names.pop(alt_names.index(rem))
                alt_ids.pop(alt_names.index(rem))
            except:
                pass
        res = select(alt_names, alt_ids, 1)
        if res is not None and res != 'selection cancelled':
            page = fetch('https://sezonlukdizi.vip/ajax/dataEmbed.asp', data={"id": res})
            link = re.findall('(?:SRC|src)="(.*?)"', page)[0]
            if link.startswith('//'):
                link = 'https:' + link
            if '/player/fembed.asp' in link:
                code = link.split('?v=')[1]
                link = 'https://www.fplay.cf/api/source/' + code
            return link
        else:
            return res
    else:
        error(url)

def tele1(url):
    page = fetch(url)
    return re.findall('iframe.*?src="(.*?)"',page)[0]

def ulketv(url):
    page = fetch(url)
    return re.findall('xt/html"\s*src="(.*?)\?', page)[0]

def tvnet(url):
    page = fetch(url)
    return re.findall('live-image"\s*href="(.*?)"', page)[0]
