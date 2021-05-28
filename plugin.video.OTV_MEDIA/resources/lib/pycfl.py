# -*- coding: utf-8 -*-
import re, sys, urllib, urllib2
from time import sleep
from urlparse import urlparse

from bs4 import BeautifulSoup as bs
import requests
import cloudscraper
import time
from resources.lib.comaddon import VSlog#, dialog
from resources.lib.otvhelper import  gegetUrl,getUrl ,alfabekodla

import re
import requests
import time
from resources.lib.config import cConfig
import urllib2, urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
from resources.lib.comaddon import VSlog#, dialog
from resources.lib.handler.requestHandler3 import cRequestHandler
import logging
import re
import sys
import ssl
import requests

try:
    import copyreg
except ImportError:
    import copy_reg as copyreg

try:
    from HTMLParser import HTMLParser
except ImportError:
    if sys.version_info >= (3, 4):
        import html
    else:
        from html.parser import HTMLParser

from copy import deepcopy
from time import sleep
from collections import OrderedDict

from requests.sessions import Session
from requests.adapters import HTTPAdapter


from resources.lib.cloudscraper.interpreters.encapsulated import templatt


import re, os, time, json, random, ssl, requests
import xbmcvfs
from requests.adapters import HTTPAdapter
from collections import OrderedDict
from requests.sessions import Session
from jsunfuck import JSUnfuck
from resources.lib import common

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

#old version
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

class GestionCookie():
    PathCache = common.profilePath

    def DeleteCookie(self,Domain):
        Name = "/".join([self.PathCache, "cookie_%s.txt"]) % (Domain)
        xbmcvfs.delete(Name)

    def SaveCookie(self,Domain,data):
        Name = "/".join([self.PathCache, "cookie_%s.txt"]) % (Domain)
        f = xbmcvfs.File(Name, 'w')
        f.write(data)
        f.close()

    def Readcookie(self,Domain):
        Name = "/".join([self.PathCache, "cookie_%s.txt"]) % (Domain)
        try:
            f = xbmcvfs.File(Name)
            data = f.read()
            f.close()
        except:
            return ''
        return data

class CipherSuiteAdapter(HTTPAdapter):
    def __init__(self, cipherSuite=None, **kwargs):
        self.cipherSuite = cipherSuite

        if hasattr(ssl, 'PROTOCOL_TLS'):
            self.ssl_context = create_urllib3_context(
                ssl_version=getattr(ssl, 'PROTOCOL_TLSv1_3', ssl.PROTOCOL_TLSv1_2),
                ciphers=self.cipherSuite
            )
        else:
            self.ssl_context = create_urllib3_context(ssl_version=ssl.PROTOCOL_TLSv1)
        super(CipherSuiteAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs['ssl_context'] = self.ssl_context
        return super(CipherSuiteAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        kwargs['ssl_context'] = self.ssl_context
        return super(CipherSuiteAdapter, self).proxy_manager_for(*args, **kwargs)

Mode_Debug = True

if (False):
    Mode_Debug = True
    import logging
    # These two lines enable debugging at httplib level (requests->urllib3->http.client)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger('requests.packages.urllib3')
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def GetHeadercookie(url):
        #urllib.parse.quote_plus()
        Domain = re.sub(r'https*:\/\/([^/]+)(\/*.*)', '\\1', url)
        cook = GestionCookie().Readcookie(Domain.replace('.', '_'))
        if cook == '':
            return ''

        return  cook

def ParseCookies( data):
        list = {}

        sPattern = '(?:^|[,;]) *([^;,]+?)=([^;,\/]+)'
        aResult = re.findall(sPattern, data)
        ##VSlog(str(aResult))
        if (aResult):
            for cook in aResult:
                if 'deleted' in cook[1]:
                    continue
                list[cook[0]] = cook[1]
                #cookies = cookies + cook[0] + '=' + cook[1]+ ';'

        ##VSlog(str(list))

        return list


def unescape(html_text):
        if sys.version_info >= (3, 0):
            if sys.version_info >= (3, 4):
                return html.unescape(html_text)

            return HTMLParser().unescape(html_text)

        return HTMLParser().unescape(html_text)
   
def simpleException( exception, msg):
        _solveDepthCnt = 0
        sys.tracebacklimit = 0
        raise exception(msg)
import collections
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path')).decode('utf-8')
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
data_file = os.path.join(RESOURCES_DIR, 'data.txt')
r = requests.Session()
__sResponseHeader = ''
Memorised_Headers = None

def SetHeader():
        head = OrderedDict()
        #Need to use correct order
        h = ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection', 'Upgrade-Insecure-Requests']
        v = [UA, 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'en-US,en;q=0.5', 'gzip, deflate', 'close', '1']
        for i in enumerate(h):
            k = checklowerkey(i[1],Memorised_Headers)
            if k:
                head[i[1]] = Memorised_Headers[k]
            else:
                head[i[1]] = v[i[0]]

        #optional headers
        if 'Referer' in Memorised_Headers:
            head['Referer'] = Memorised_Headers['Referer']

        if (False):
            #Normalisation because they are not case sensitive:
            Headers = ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Cache-Control', 'Dnt', 'Pragma', 'Connexion']
            Headers_l = [x.lower() for x in Headers]
            head2 = dict(head)
            for key in head2:
                if not key in Headers and key.lower() in Headers_l:
                    p  = Headers_l.index(key.lower())
                    head[Headers[p]] = head[key]
                    del head[key]

        return head


def GetCookies():
        
        
        if not __sResponseHeader:
            return ''
        if 'Set-Cookie' in __sResponseHeader:
            import re

            #cookie_string = self.__sResponseHeader.getheaders('set-cookie')
            #c = ''
            #for i in cookie_string:
            #    c = c + i + ', '
            c = __sResponseHeader.get('set-cookie')

            c2 = re.findall('(?:^|,) *([^;,]+?)=([^;,\/]+?);', c)
            if c2:
                cookies = ''
                for cook in c2:
                    cookies = cookies + cook[0] + '=' + cook[1] + ';'
                cookies = cookies[:-1]
                return cookies
        return ''
def pycfl(url):
      import chrome.cmd
      

def pycf2(url, htmlcontent = '', cookies = '', postdata = None, Gived_headers = ''):
            
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36', 'Upgrade-Insecure-Requests':'1', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Cookie': '__cfduid=d44cbf60c2d1aa34dccb03639ec3afd9b1588489679'}
        body = requests.get(url, headers = header).text
        formPayload = re.search(
                r'<form (?P<form>.*?="challenge-form" '
                r'action="(?P<challengeUUID>.*?'
                r'__cf_chl_jschl_tk__=\S+)"(.*?)</form>)',
                body,
                re.M | re.DOTALL
            ).groupdict()
            

        Memorised_Headers = Gived_headers

        #Memorise postdata
        Memorised_PostData = postdata

        #Memorise cookie
        Memorised_Cookies = cookies
        #VSlog(cookies)

        #cookies in headers?
        if Gived_headers != '':
            if Gived_headers.get('Cookie',None):
                if cookies:
                    Memorised_Cookies = cookies + '; ' + Gived_headers.get('Cookie')
                else:
                    Memorised_Cookies = Gived_headers['Cookie']

        #For debug
        if (Mode_Debug):
            VSlog('Headers present ' + str(Gived_headers))
            VSlog('url ' + url)
            if (htmlcontent):
                VSlog('code html ok')
            VSlog('cookies passés : ' + Memorised_Cookies)
            VSlog('post data :' + str(postdata))

        hostComplet = re.sub(r'(https*:\/\/[^/]+)(\/*.*)', '\\1', url)
        host = re.sub(r'https*:\/\/', '', hostComplet)
        url = url

        cookieMem = GestionCookie().Readcookie(host.replace('.', '_'))
        if not (cookieMem == ''):
            if (Mode_Debug):
                VSlog('cookies present sur disque :' + cookieMem )
            if not (Memorised_Cookies):
                cookies = cookieMem
            else:
                cookies = Memorised_Cookies + '; ' + cookieMem
        else:
            if (Mode_Debug):
                VSlog('Pas de cookies présent sur disque' )

        data = {}
        if postdata:
            method = 'POST'
            #Need to convert data to dictionnary
            d = postdata.split('&')
            for dd in d:
                ddd = dd.split('=')
                data[ddd[0]] = ddd[1]
        else:
            method = 'GET'
        
       
 
        Parsed =url+unescape(formPayload['challengeUUID']) 
        for rc in formPayload:
                 jschl_r = re.search('name="r" value="(.+?)"', body).group(1)
                 jschl_vc = re.search('type="hidden" value="(.+?)"', body).group(1)
                 jschl_pass = re.search('name="pass" value="(.+?)"', body).group(1)
                 params= {'r': jschl_r,'jschl_vc': jschl_vc,
                 'pass': jschl_pass,
                 'jschl_answer': templatt( body, url)}

                 hostParsed = urlparse(url)
                 
        
                 
                 time.sleep(5) 
                 rc = r.get(url+unescape(formPayload['challengeUUID']), params=params).text
                                    
                 
                 VSlog('payload-' + rc )

                 
           
            
