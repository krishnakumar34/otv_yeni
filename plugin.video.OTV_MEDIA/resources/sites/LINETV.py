#-*- coding: utf-8 -*-
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
import re
from resources.lib.gui.guiElement import cGuiElement
SITE_IDENTIFIER = 'LINETV'
SITE_NAME = 'LIVE NET TV'
SPORT_SPORTS = (True, 'root')    

player_user_agent = 'ExoPlayerDemo/2.0 (Linux;Android 5.0.1) ExoPlayerLib/2.7.3/19.0 (Linux;Android 6.0.1) ExoPlayerLib/2.7.2'
from binascii import b2a_hex
import binascii
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem
from routing import Plugin


import requests
import urllib
import time
import json
import io
import os
import re
import string
import random
import datetime
import uuid
from hashlib import md5
from base64 import b64encode, b64decode
from itertools import chain

import json
import time

user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTS Build/LVY48F)"
HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
import http.cookiejar
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
from datetime import timedelta

try:
    from http.cookiejar import LWPCookieJar
except ImportError:
    from cookielib import LWPCookieJar
def _get(request, post = None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request, post).read()


s = requests.Session()
plugin = Plugin()
#import nginx
try:
    from urllib.parse import quote as orig_quote
except ImportError:
    from urllib import quote as orig_quote
dat_url = 'https://www.swiftstreamz.cc/SwiftStreamzv2.1/datav2.php'
#dat_url = 'https://dl.dropboxusercontent.com/s/lzjea5w2b0fmpbg/katogeri.raw'
datam_url = 'http://128.199.114.52/stm-v3/api/data37.json'
ddatam_url = 'http://128.199.114.52/stm-v3/api/data37.json'
data_url = 'http://hyfystreamz.com/swift/api.php'
addonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(id=addonID)
player_agent = 'ExoPlayerDemo/2.0 (Linux;Android 5.0.1) ExoPlayerLib/2.7.3/19.0 (Linux;Android 6.0.1) ExoPlayerLib/2.7.2'
User_agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
def quote(s, safe = ''):
    return orig_quote(s.encode('utf-8'), safe.encode('utf-8'))

def get_post_data():
    _key = 'cLt3Gp39O3yvW7Gw'
    _iv = 'bRRhl2H2j7yXmuk4'
                
#1561570680     
    cipher = AES.new(_key, AES.MODE_CBC, iv=_iv)
    _time = str(int(time.time()))
#    h2=md5("66726563636D30746E70716D6F6C6468".format().encode("utf-8")).hexdigest() 
    _plain = "1561570680&fc2f07372982634c95b93371e44ef76c".format().ljust(48).encode("utf-8")
    cry = cipher.encrypt(_plain)
    return b2a_hex(cry).decode("utf-8")

def fetcher48():
    wms_url = "http://212.83.158.140:6060/aves.nettv/"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Referer':'http://xyz,com','Authorization': 'Basic QDA3NzEyMSM6QDA3NzEyMSM=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text

def fetcher38():
    wms_url = "http://212.83.158.140:6060/temporary/def.php"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Referer':'http://xyz,com','Authorization': 'Basic eWFyYXBuYWthYW1rYXJvOnR1bmduYWtpYWthcm8=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text



def fetcher44():
    wms_url = "http://212.83.182.86:8080/chick.nettv/"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Authorization': 'Basic QDA3NzEyMSM6QDA3NzEyMSM=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text


def fetcher33():
    wms_url = "http://78.129.139.44:3030/duck.nettv/"
    req = requests.Request('GET', wms_url, headers={'Modified': '10514263348556648368','Authorization': 'Basic QDA3NzEyMSM6QDA3NzEyMSM=','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)'})
    prq = req.prepare()
    r = s.send(prq)
    return r.text
def rbtv():
               )
       Url='http://51.15.209.90:8800/3rd.rbtv'
       req = urllib.request.Request(Url
#       req.add_header('Modified','10514263348556648368')
       req.add_header('Host','51.15.209.90:8800') 
       req.add_header('Authorization','Basic eWFyYXBuYWthYW1rYXJvOnR1bmduYWtpYWthcm8=')
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1; P6 PRO Build/LMY47D)')
       son=  _get(req)       
       return son

def fetcher22():
     
       Url='http://212.47.231.14:8090/data/(~)/auth.nettv/'
       req = urllib.request.Request(Url
       req.add_header('Modified','10514263348556648368')
       req.add_header('Host','linenettv.net:8090') 
       req.add_header('Authorization','Basic QFN3aWZ0MTQjOkBTd2lmdDE0Iw==')
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)')
       son=  _get(req)       
       return son
        
def mget_post_data():
       #token 6 http://134.209.153.85/stm-v3/api/def2.php?id=1198&quality=0&type=0
       #token 13 http://134.209.153.85/stm-v3/api/def2.php?id=470&quality=0&type=0
       oInputParameterHandler = cInputParameterHandler()
       Url='http://139.59.68.238/stm-v3/api/def39.php?id=340&quality=0&type=0'
       data=requests.session().get(Url,headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)","Host": "139.59.68.238","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
#       data = data.replace('\/','/')   
#       post_data = {"type":  "swt","link":  "","token":  ""}
#       r = s.post(Url, headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)","Host": "139.59.68.238","Connection": "Keep-Alive","Accept-Encoding": "gzip"}, data=post_data, timeout=10)
#       auth = r.text    
       name =  "https://goo.gl/wqsVrs"  
       addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, data, '')
      
def fetcher54():
    Url= "http://212.83.183.94:8085/ksio/drng/"
    req = urllib.request.Request(Url
#    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3')
#    req.add_header('X-Powered-By','PHP/5.5.9-1ubuntu4.2') 
#    req.add_header('Upgrade-Insecure-Requests','1')
    req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5A MIUI/V10.1.1.0.NCKMIFI)')
    son=  _get(req) 
#    token = re.findall('<script>(.*?)</script>"', son, re.S) 
   
    ur= str(time.strftime('%d'))
                    
    text = re.findall('t'+ur+'=(.*?)\n', son, re.S)[0]
    text =text.replace('maGFzaF92YWx1Z1','maGFzaF92YWx1ZT1').replace('n0PTmdmFsaLWRta51dGVzPTI=','RPT0mdmFsaWRtaW51dGVzPTI=')
    return text          

def mmget_post_data():
    Url = 'http://39.59.68.238/stm-v3/api/def39.php?id=470&quality=0&type=0'
    data=requests.session().get(Url,headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)","Host": "134.209.153.85","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
    liste = re.findall('"token": "(.*?)"',data, re.S)[0]    
    liste = b64decode(liste[2:]) 
    listem = re.findall('"swt","aYW10=","1","(.*?)"',liste, re.S)[0]  

    datama = b64decode(listem[2:]) 
    data= re.findall('"data":"(.*?)"',datama, re.S)[0]
    return data


def rootat():
    oGui = cGui()              
    liste = []
    liste.append( ['WORLD TV1','http://film.bestaway.club//api/get_category?api_key=c3sbB6K0yVc2GFH/GJ3tjiVu/40=','http://www.nekadarizlendi.com/wp-content/uploads/2017/02/Ekran-Resmi-2017-02-19-11.50.16.png'])
    liste.append( ['WORLD TV','http://139.59.68.238/stm-v3/api/data.json','https://pbs.twimg.com/profile_images/543610023973097472/lEtD1thL.png'] ) 
    liste.append( ['RADIO','Radio','https://pbs.twimg.com/profile_images/543610023973097472/lEtD1thL.png'] ) 
#    liste.append( ['ADULT','Radio','https://pbs.twimg.com/profile_images/543610023973097472/lEtD1thL.png'] ) 
                     
    for sTitle,url,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', url)
        if sTitle == 'WORLD TV1':
             oGui.addMovie(SITE_IDENTIFIER, 'indiaroot',sTitle, 'sPicture', 'sPicture', '<fanart>http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif</fanart>', oOutputParameterHandler)
        elif sTitle == 'WORLD TV':
             oGui.addMovie(SITE_IDENTIFIER, 'worldroot',sTitle, 'sPicture', 'sPicture', '', oOutputParameterHandler)
        elif sTitle == 'RADIO':
             oGui.addMovie(SITE_IDENTIFIER, 'AdLIVETV', sTitle, 'radio.jpg', 'radio.jpg', '', oOutputParameterHandler)
        elif sTitle == 'ADULT':
             oGui.addMovie(SITE_IDENTIFIER, 'AdultLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
             oGui.addMovie(SITE_IDENTIFIER, 'Taraftar2', sTitle, 'http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif', 'http://bestaway.club/resim/uploads/5bed7f35e4cf6_468x60tipobit.gif', '', oOutputParameterHandler)      
#             oGui.addDir(SITE_IDENTIFIER, 'Taraftar2',  sTitle, '<fanart>5bed7f35e4cf6_468x60tipobit.gif</fanart>', oOutputParameterHandler)       
    oGui.setEndOfDirectory()                    

def worldroot():
    oGui = cGui()
    sJson = cRequestHandler(datam_url).request()    
    aJson = json.loads(sJson)
    
    for cat in aJson["data"]["country"]:
            catid =cat['id']
            sTitle =cat['title']
            sPic=cat['logo']
#            sTitle = alfabekodla(sTitle)
            sPicture='http://139.59.68.238/stm-v3/api/'+ sPic 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',catid )
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'worldLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory() 
def AdLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_title = oInputParameterHandler.getValue('siteUrl')
#    cat_title = oInputParameterHandler.getValue('sMovieTitle')
    sJson = cRequestHandler(ddatam_url).request()    
    aJson = json.loads(sJson)
    liste =aJson["data"]["channels"]
    for cat in liste:
      if cat["cat_title"] == cat_title:
            stream = cat.get("id")
            sTitle =cat['title']
            sPic=cat['logo']
          
                     
            #sTitle = alfabekodla(sTitle)      
          
            sPicture='http://139.59.68.238/stm-v3/api/'+ sPic 
            #stream_url =cat['ulink']
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',stream )
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'atplaylive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()  

def AdultLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    cat_title = 'Adult'
    sJson = cRequestHandler(ddatam_url).request()    
    aJson = json.loads(sJson)
    liste =aJson["data"]["channels"]
    for cat in liste:
      if cat["cat_title"] == cat_title:
            stream = cat.get("id")
            sTitle =cat['title']
            sPic=cat['logo']
          
                     
            sTitle = alfabekodla(sTitle)      
          
            sPicture='http://139.59.68.238/stm-v3/api/'+ sPic 
            #stream_url =cat['ulink']
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',stream )
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'adultplaylive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()  
  
def adultplaylive():
    oInputParameterHandler = cInputParameterHandler()
    Urla = oInputParameterHandler.getValue('siteUrl')
    Url = 'http://139.59.5.164/stm-v3/api/def39.php?id=%s&quality=0&type=0'%Urla
    name = oInputParameterHandler.getValue('sMovieTitle')
    data=requests.session().get(Url,headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/NRD90M)","Host": "139.59.5.164","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
    data = data.replace('\/','/')
    #token = re.findall('"link": "(.*?)"',data, re.S)[0] 
    #headers = {'Referer': 'http://www.adulttvlive.net/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    #sJson = requests.get(token, headers = headers).text    
    #url = re.findall('file:"(.*?)"',sJson , re.S)[0] +"|Referer="+token+"&User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, data, '')


def worldLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    cat_title = oInputParameterHandler.getValue('sMovieTitle')
    sJson = cRequestHandler(ddatam_url).request()    
    aJson = json.loads(sJson)
    liste =aJson["data"]["channels"]
    for cat in liste:
      if cat["cou_title"] == cat_title:
            stream = cat.get("id")
            sTitle =cat['title']
            sPic=cat['logo']
          
                    
            #sTitle = alfabekodla(sTitle)      
          
            sPicture='http://139.59.68.238/stm-v3/api/'+ sPic
            #stream_url =cat['ulink']
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',stream )
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'atplaylive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()  
    



def indiaroot():
    oGui = cGui()
    sJson = cRequestHandler(datam_url).request()    
    aJson = json.loads(sJson)
    
    for cat in aJson["data"]["categories"]:
            catid =cat['id']
            sTitle =cat['title']
            sPic=cat['logo']
            #sTitle = alfabekodla(sTitle)
            sPicture='http://139.59.68.238/stm-v3/api/'+ sPic 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',catid)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'atLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory() 


def atLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    sJson = cRequestHandler(datam_url).request()    
    aJson = json.loads(sJson)
    liste =aJson["data"]["channels"]
    for cat in liste:
      if cat["cat_id"] == cat_id:
            stream = cat.get("id")
            sTitle =cat['title']
            sPic=cat['logo']
          
                     
            #sTitle = alfabekodla(sTitle)      
          
            sPicture='http://139.59.68.238/stm-v3/api/'+ sPic 
            #stream_url =cat['ulink']
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',stream )
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'atplaylive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()  
    



from LIVETV import get_auth_token_48, get_auth_token_21 ,get_auth_token_38   

def atplaylive():
    
    oInputParameterHandler = cInputParameterHandler()
    Urla = oInputParameterHandler.getValue('siteUrl')
    Url = 'http://128.199.114.52/stm-v3/api/def39.php?id=%s&quality=0&type=0'%Urla
    name = oInputParameterHandler.getValue('sMovieTitle')
    data=requests.session().get(Url,headers={"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020)","Host": "128.199.114.52","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
    data = data.replace('\/','/')
    url = re.findall('"link": "(.*?)"',data, re.S)[0] 
    liste = re.findall('"token": "(.*?)"',data, re.S)[0]    
    liste = b64decode(liste[2:]) 
    if   "swt" in liste:
         listem = re.findall('"swt","aYW10=","1","(.*?)"',liste, re.S)[0]  
         datama = b64decode(listem[2:]) 
         dadat= re.findall('"data":"(.*?)"',datama, re.S)[0]
    if   "rb" in liste:
         
         dat = b64decode(re.findall('"link": "(.*?)"',data, re.S)[0][2:])    
         liste = re.findall('(http://.*?.rbtv/),(.*?),(http://.*?.m3u8)',dat, re.S)  
         m,token, media_url = liste[0]
         if token== "48":
             url =  media_url+ get_auth_token_48()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
         elif  token== "21":
             url =  media_url+ get_auth_token_21()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
         elif  token== "38":
             url = media_url+ get_auth_token_38()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
   
    if not 'http' in url:     
       dat = b64decode(re.findall('"link": "(.*?)"',data, re.S)[0][2:])    
       liste = re.findall('(http://.*?.php),(http://.*?.m3u8)',dat, re.S)  
       if liste : 
          token, File = liste[0] 
          post_data = {"data":  dadat}
          req = urllib2.Request(token)
                            
          req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
#       req.add_header('"WWW-Authenticate','IVYBOWQn+1rgFXNAWMDB06XjA=')
          req.add_header('Host','swiftstreamz.com')
          post = urllib.urlencode(post_data)
          autho=_get(req,post)  
       #post = {"type":"swt","source":"http://swiftstreamz.com/newapptoken13.php,http://212.8.253.141:7071/wildsci2019/animalplanet/playlist.m3u8", "data":"?wmsAuthSign=c2VydmVyX3RpbWU9Ni8yNy8yMDE5IDY6MTE6MjEgUE0maGFzaF92YWx1ZT1xcVlDc25lM1JnMmNvUDU2bThIeTh3PT0mdmFsaWRtaW51dGVzPTI=", "":""}
          post = {"type":"swt","source":"%s,%s"%(token,File),"data":autho, }
                          
          Urlu='http://128.199.114.52/stm-v3/api/get.php'                                       
          req = urllib2.Request(Urlu)
                            
          req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
          req.add_header('"WWW-Authenticate','IVYBOWQn+1rgFXNAWMDB06XjA=')
          req.add_header('Host','139.59.12.146')
          post = urllib.urlencode(post)
          auth=_get(req,post).replace('\/',"/")
       
          data= re.findall('link": "(.*?)"',auth, re.S)[0]
          url =data+ "|User-Agent="+player_user_agent 
 
#          url = "{0}{1}|User-Agent={2}".format(File, auth_token, quote(player_user_agent))

#    url = b64decode(url[2:])+"|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def matplaylive():
    
    oInputParameterHandler = cInputParameterHandler()
    Urla = oInputParameterHandler.getValue('siteUrl')
    Url = 'http://128.199.114.52/stm-v3/api/def39.php?id=%s&quality=0&type=0'%Urla
    name = oInputParameterHandler.getValue('sMovieTitle')
    data=requests.session().get(Url,headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)","Host": "139.59.5.164","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
    data = data.replace('\/','/')
    url = re.findall('"link": "(.*?)"',data, re.S)[0] 
    liste = re.findall('"token": "(.*?)"',data, re.S)[0]    
    token_link = b64decode(liste[2:]) 
    if   "swt" in liste:
       listem = re.findall('"swt","aYW10=","1","(.*?)"',liste, re.S)[0]  
       datama = b64decode(listem[2:]) 
       dadat= re.findall('"data":"(.*?)"',datama, re.S)[0]
       post_data  = {"data":dadat, }
       
       req = urllib2.Request(token)
                            
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
#       req.add_header('"WWW-Authenticate','IVYBOWQn+1rgFXNAWMDB06XjA=')
       req.add_header('Host','swiftstreamz.com')
       post = urllib.urlencode(post_data)
       autho=_get(req,post)  
       #post = {"type":"swt","source":"http://swiftstreamz.com/newapptoken13.php,http://212.8.253.141:7071/wildsci2019/animalplanet/playlist.m3u8", "data":"?wmsAuthSign=c2VydmVyX3RpbWU9Ni8yNy8yMDE5IDY6MTE6MjEgUE0maGFzaF92YWx1ZT1xcVlDc25lM1JnMmNvUDU2bThIeTh3PT0mdmFsaWRtaW51dGVzPTI=", "":""}
       post = {"type":"swt","source":"%s,%s"%(token_link,stream_url),"data":autho, }
                          
       Urlu='http://128.199.114.52/stm-v3/api/get.php'                                       
       req = urllib2.Request(Urlu)
                            
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
       req.add_header('"WWW-Authenticate','IVYBOWQn+1rgFXNAWMDB06XjA=')
       req.add_header('Host','139.59.12.146')
       post = urllib.urlencode(post)
       auth=_get(req,post).replace('\/',"/")
       
       data= re.findall('link": "(.*?)"',auth, re.S)[0]
       url =data+ "|User-Agent="+player_user_agent 

    
    if   "rb" in liste:
         
         dat = b64decode(re.findall('"link": "(.*?)"',data, re.S)[0][2:])    
         liste = re.findall('(http://.*?.rbtv/),(.*?),(http://.*?.m3u8)',dat, re.S)  
         m,token, media_url = liste[0]
         if token== "48":
             url =  media_url+ get_auth_token_48()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
         elif  token== "21":
             url =  media_url+ get_auth_token_21()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
         elif  token== "38":
             url = media_url+ get_auth_token_38()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
    if not 'http' in url:     
       dat = b64decode(re.findall('"link": "(.*?)"',data, re.S)[0][2:])    
       liste = re.findall('(http://.*?.php),(http://.*?.m3u8)',dat, re.S)  
       if liste : 
          token, File = liste[0] 
         
          r = s.post(token, headers={"Content-Length": "101","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}, data=post_data, timeout=10)
          auth_token= r.text                                                                                                   
          #token= 'http://hyfytv.xyz/decrypt1.php?token='+ auth 
          #auth_token = cRequestHandler(token).request()     
          url = "{0}{1}|User-Agent={2}".format(File, auth_token, quote(player_user_agent))

#    url = b64decode(url[2:])+"|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def matplaylive():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    stream_url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    if   '/mercury/' in stream_url:
        url =stream_url+ get_auth_token_48()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
    if   '/swiftp2p/' in stream_url:
        url = stream_url+ get_auth_token_21()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
    if   '/venus/' in stream_url:
        url =stream_url+ get_auth_token_48()+"|User-Agent=stagefright/1.2 (Linux;Android 5.2.3)"
       
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')

     



                                               
def root():
    oGui = cGui()
    oGui = cGui()
    r = requests.get(data_url, headers = {'Content-Length': '0','Host': 'swiftstreamz.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip'}, timeout=10)
    res = r.json(strict=False)
    
   
    for cat in res['LIVETV1']:
          sTitle =cat['category_name']
          sPicture=cat['category_image']
          sUrl =cat['cid']

             
                       
          #sTitle = alfabekodla(sTitle)
         
           
          oOutputParameterHandler = cOutputParameterHandler()
          oOutputParameterHandler.addParameter('siteUrl', sUrl)
          oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
          oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
          if  'INDIAN MOVIES 2019' in sTitle:
             oGui.addMovie(SITE_IDENTIFIER, 'vodLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          elif sTitle == 'PUBNJABI MOVIES':
             oGui.addMovie(SITE_IDENTIFIER, 'vodLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          elif sTitle == 'PAKISTANI MOVIES':
            oGui.addMovie(SITE_IDENTIFIER, 'vodLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          elif sTitle == 'ATV YEDEK':
             oGui.addMovie(SITE_IDENTIFIER, 'LIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          else:
			oGui.addMovie(SITE_IDENTIFIER, 'LIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory() 

def MLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    r = requests.get(llist_url.format(cat_id), headers = {'User-Agent': user_agent}, timeout=10)
    res = r.json(strict=False)
    for ch in res['LIVETV']:
            sPicture=ch['channel_thumbnail']
            sTitle =ch['channel_title']
            stream_id = ch['cat_id'] 
            stream_url = ch['stream_url']             
            token = ch['token']           
            #sTitle = alfabekodla(sTitle)
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', stream_url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oOutputParameterHandler.addParameter('token', token)
            oOutputParameterHandler.addParameter('stream_id', stream_id)
            oGui.addMovie(SITE_IDENTIFIER, 'playlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()  
      

def vodLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    liste = 'http://swiftstreamz.com/SwiftPanel/apiv1.php?get_videos_by_cat_id=' + cat_id
    sHtmlContent = requests.session().get(liste,headers = {"Content-Length": "0","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)"}).text
    oParser = cParser()
    sPattern = '"video_title": "(.*?)".*?"vod_stream_id": "(.*?)".*?"stream_url": "(.*?)".*?"token": "(.*?)".*?"video_thumbnail_s": "(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            token = aEntry[3]
            stream_id = aEntry[1]
            sUrl = aEntry[2]
            sPicture = aEntry[4]
           
            sTitle = aEntry[0]
            #sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('stream_id', stream_id)
            oOutputParameterHandler.addParameter('token', token)
#            oOutputParameterHandler.addParameter('liste', liste)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'playLINETV2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def vgetauthtoken(token, id):
    wms_url = 'http://swiftstreamz.com/newapptoken%s.php' % token
    auth = 'Basic QFN3aWZ0MTIjOkBTd2lmdDEyIw=='
    mod_value = int(id)
    modified = lambda value: ''.join(chain(*zip(str(int(time.time()) ^ value), '0123456789')))
    req = requests.Request('GET', wms_url, headers={'User-Agent': user_agent,
     'Accept-Encoding': 'gzip',
     'Modified': modified(mod_value)})
    prq = req.prepare()
    r = s.send(prq)
    return r.text



def playlive():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    stream_url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    token = oInputParameterHandler.getValue('token')
    strea= oInputParameterHandler.getValue('liste')
#    html= requests.session().get(data_url,headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)"}).text
    html =cRequestHandler(data_url).request()
#    sJson =requests.session().get(t_url,headers = {"Content-Length": "0","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)"}).text


#    html =cRequestHandler(data_url).request()
    r = re.search(r'apiUrl": "([^"]+)"', html, re.DOTALL)
    tokene = r.group(1)
    r = re.search(r'data": "([^"]+)"', html, re.DOTALL)
    datam = r.group(1)        
    post_data = {"data": datam}
    r = s.post(t_url, headers = {"Content-Length": "0","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)"}, data=post_data, timeout=10)
    data = r.json(strict=False)
    token_list = data["LIVETV"]["token_list"]
    for _token in token_list:
        if _token["t_id"] == token:
          token_link = _token["token_link"]
          post_data = {"data": datam}
          r = s.post(token_link, headers={"Content-Length": "101","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}, data=post_data, timeout=10)
          auth = r.text                                                                                                   
#    sJson =requests.session().get(t_url,headers = {"Content-Length": "0","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)"}).text

          #r = s.post(token_link, headers={"Content-Length": "101","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}, data=post_data, timeout=10)
#          addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,auth, '')


          token= 'http://hyfytv.xyz/decrypt1.php?token='+ auth 
          auth_token = cRequestHandler(token).request()  
          url = "{0}{1}|User-Agent={2}".format(stream_url,auth_token, quote(player_user_agent))  +gget_post_data() 
#          iconimage= oInputParameterHandler.getValue('sMovieTitle')
          name =  alfabekodla(sTitle)
          addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')

    oGui.setEndOfDirectory()



def LINETV2():
    oGui = cGui()
    r = requests.get(data_url, headers = {'Content-Length': '0','Host': 'swiftstreamz.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip'}, timeout=10)
    res = r.json(strict=False)
    
   
    for cat in res['LIVETV1']:
          sTitle =cat['category_name']
          sPicture=cat['category_image']
          sUrl =cat['cid']

             
                       
         # sTitle = alfabekodla(sTitle)
         #
           
          oOutputParameterHandler = cOutputParameterHandler()
          oOutputParameterHandler.addParameter('siteUrl', sUrl)
          oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
          oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
          if  'INDIAN MOVIES 2019' in sTitle:
             oGui.addMovie(SITE_IDENTIFIER, 'vodLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          elif sTitle == 'PUBNJABI MOVIES':
             oGui.addMovie(SITE_IDENTIFIER, 'vodLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          elif sTitle == 'PAKISTANI MOVIES':
            oGui.addMovie(SITE_IDENTIFIER, 'vodLIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          elif sTitle == 'ATV YEDEK':
             oGui.addMovie(SITE_IDENTIFIER, 'LIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
          else:
			oGui.addMovie(SITE_IDENTIFIER, 'LIVETV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory() 
def LIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    liste = 'http://swiftstreamz.com/SwiftPanel/apiv1.php?get_channels_by_cat_id='+ cat_id
#    url = requests.get(liste, headers = {'Content-Length': 'user_agent','Host': 'swiftstreamz.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip'}, timeout=10)
    sJson =requests.session().get(liste,headers = {"Content-Length": "0","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)"}).text
    res = json.loads(sJson)
    for ch in res['LIVETV']:
       for cch in ch['stream_list']:
            sPicture=ch['channel_thumbnail']
            sTitle =ch['channel_title']
            stream_id = ch['cat_id'] 
            stream_url = cch['stream_url']             
            token = cch['token']           
            #sTitle = alfabekodla(sTitle)
                      
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', stream_url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oOutputParameterHandler.addParameter('token', token)
            oOutputParameterHandler.addParameter('stream_id', stream_id)
            oGui.addMovie(SITE_IDENTIFIER, 'playLINETV2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()  

#    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + cat_id, url, '')
def mLIVETV():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    liste = 'http://swiftstreamz.com/SwiftPanel/apiv1.php?get_channels_by_cat_id' + cat_id
    sHtmlContent = requests.get(liste, headers = {'Content-Length': '0','Host': 'swiftstreamz.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip'}, timeout=10)
    oParser = cParser()
    sPattern = '"channel_title": "(.*?)".*?"stream_id": "(.*?)".*?"stream_url": "(.*?)".*?"token": "(.*?)".*?"channel_thumbnail": "(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            token = aEntry[3]
            stream_id = aEntry[1]
            sUrl = aEntry[2]
            sPicture = aEntry[4]
           
            sTitle = aEntry[0]
            #sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('stream_id', stream_id)
            oOutputParameterHandler.addParameter('token', token)
#            oOutputParameterHandler.addParameter('liste', liste)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'playLINETV2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def LINETV2list():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    cat_id = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = cRequestHandler(data_url).request()
    oParser = cParser()
    sPattern = '"cat_id": "'+cat_id+'".*?"channel_title": "(.*?)".*?"stream_id": "(.*?)".*?"stream_url": "(.*?)".*?"token": "(.*?)".*?"channel_thumbnail": "(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            token = aEntry[3]
            stream_id = aEntry[1]
            sUrl = aEntry[2]
            sPicture = aEntry[4]
           
            sTitle = aEntry[0]
            #sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('stream_id', stream_id)
            oOutputParameterHandler.addParameter('token', token)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'playLINETV2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def mplayLINETV2():
    oInputParameterHandler = cInputParameterHandler()
    stream_url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    token = oInputParameterHandler.getValue('token')
    strea= oInputParameterHandler.getValue('liste')
    Url = 'http://139.59.5.164/stm-v3/api/def39.php?id=1283&quality=0&type=0'
    url=requests.session().get(Url,headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/NRD90M)","Host": "139.59.5.164","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text

    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')
     
def playLINETV2():
    oInputParameterHandler = cInputParameterHandler()
    stream_url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    token = oInputParameterHandler.getValue('token')
    strea= oInputParameterHandler.getValue('liste')
    #html =cRequestHandler(data_url).request()
    #r = re.search(r'apiUrl": "([^"]+)"', html, re.DOTALL)
    #tokene = r.group(1)
    #r = re.search(r'data": "([^"]+)"', html, re.DOTALL)
    #datam = r.group(1)        
    post_data = {"data":"6e2189574541eddefc8506d6cb364cb9f95d3ce0e6be28a40c8b4596bbe8b19c2fdaf576bbe1ec7262ee1e215889133c"}
    r = s.post(t_url, headers = {"Content-Length": "0","Host": "swiftstreamz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)"}, data=post_data, timeout=10)

    data = r.json(strict=False)
    token_list = data["LIVETV"]["token_list"]
    for _token in token_list:
     if _token["t_id"] == token:
       token_link = _token["token_link"]       
    
       Url = 'http://128.199.114.52/stm-v3/api/def39.php?id=1283&quality=0&type=0'
       data=requests.session().get(Url,headers={"WWW-Authenticate": "IVYBOWQn+1rgFXNAWMDB06XjA=","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/NRD90M)","Host": "139.59.5.164","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
       liste = re.findall('"token": "(.*?)"',data, re.S)[0]    
       liste = b64decode(liste[2:]) 
       listem = re.findall('"swt","aYW10=","1","(.*?)"',liste, re.S)[0]  

       datama = b64decode(listem[2:]) 
       data= re.findall('"data":"(.*?)"',datama, re.S)[0]

       post = {"data":data, }
       
       req = urllib2.Request(token_link)
                            
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
#       req.add_header('"WWW-Authenticate','IVYBOWQn+1rgFXNAWMDB06XjA=')
       req.add_header('Host','swiftstreamz.com')
       post = urllib.urlencode(post)
       autho=_get(req,post)  
       #post = {"type":"swt","source":"http://swiftstreamz.com/newapptoken13.php,http://212.8.253.141:7071/wildsci2019/animalplanet/playlist.m3u8", "data":"?wmsAuthSign=c2VydmVyX3RpbWU9Ni8yNy8yMDE5IDY6MTE6MjEgUE0maGFzaF92YWx1ZT1xcVlDc25lM1JnMmNvUDU2bThIeTh3PT0mdmFsaWRtaW51dGVzPTI=", "":""}
       post = {"type":"swt","source":"%s,%s"%(token_link,stream_url),"data":autho, }
                          
       Urlu='http://128.199.114.52/stm-v3/api/get.php'                                       
       req = urllib2.Request(Urlu)
                            
       req.add_header('User-Agent','Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)')
       req.add_header('"WWW-Authenticate','IVYBOWQn+1rgFXNAWMDB06XjA=')
       req.add_header('Host','139.59.12.146')
       post = urllib.urlencode(post)
       auth=_get(req,post).replace('\/',"/")
       
       data= re.findall('link": "(.*?)"',auth, re.S)[0]
       url =data+ "|User-Agent="+player_user_agent 
      
       addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')
                              


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
