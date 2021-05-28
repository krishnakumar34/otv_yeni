import sys
import urllib2, urllib,cookielib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64


import sys
import urllib
import json
import os
import urlparse
import re, uuid
from time import time
from datetime import datetime
import math
import urllib2
import hashlib
from xml.dom import minidom

key = None;
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()));
sn = None;
device_id = None;
device_id2 = None;
signature = None;
AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path')
pwdir = os.path.join(addonDir, "password")
cdir = os.path.join(xbmc.translatePath("special://temp"),"files")
DFolder = os.path.join(addonDir, 'download', '')
addon = xbmcaddon.Addon()
#xbmcgui.Dialog().ok(addonname, 'aaa')
#base_url ='http://5.254.113.208:80'
number =''
serial = addon.getSetting('serial_number_' + number);
import requests
    

def encode_log(message=""):
    # Unicode to utf8
    if type(message) == unicode:
        message = message.encode("utf8")

    # All encodings to utf8
    elif type(message) == str:
        message = unicode(message, "utf8", errors="replace").encode("utf8")

    # Objects to string
    else:
        message = str(message)

    return message


def get_caller(message=None):
    module = inspect.getmodule(inspect.currentframe().f_back.f_back)

    # En boxee en ocasiones no detecta el modulo, de este modo lo hacemos manual
    if module is None:
        module = ".".join(os.path.splitext(inspect.currentframe().f_back.f_back.f_code.co_filename.split("streamondemand")[1])[0].split(os.path.sep))[1:]
    else:
        module = module.__name__

    function = inspect.currentframe().f_back.f_back.f_code.co_name

    if module == "__main__":
        module = "OTV_MEDIA"
    else:
        module = "OTV_MEDIA." + module
    if message:
        if module not in message:
            if function == "<module>":
                return module + " " + message
            else:
                return module + " [" + function + "] " + message
        else:
            return message
    else:
        if function == "<module>":
            return module
        else:
            return module + "." + function

def info(texto=""):
    if loggeractive:
        xbmc.log(get_caller(encode_log(texto)), xbmc.LOGNOTICE)

if not os.path.exists(addonDir):
    os.makedirs(addonDir)
if not os.path.exists(pwdir):
    os.makedirs(pwdir)	
if not os.path.exists(cdir):
    os.makedirs(cdir)
if not os.path.exists(DFolder):
    os.makedirs(DFolder)

cache_version = '3'

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True

def setMac(nmac):
	global mac;
	
	if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", nmac.lower()):
		mac = nmac;

def getMac():
	global mac;
	return mac;
	
	
def setSerialNumber(serial):
	global sn, device_id, device_id2, signature;
	
	if serial == None:
		return;
	
	elif serial['custom'] == False:
		sn = hashlib.md5(mac).hexdigest().upper()[13:];
		device_id = hashlib.sha256(sn).hexdigest().upper();
		device_id2 = hashlib.sha256(mac).hexdigest().upper();
		signature = hashlib.sha256(sn + mac).hexdigest().upper();
	
	elif serial['custom'] == True:
		sn = serial['sn'];
		device_id = serial['device_id'];
		device_id2 = serial['device_id2'];
		signature = serial['signature'];
   
def handshake(url,mac, ti =''):
	global key;
	
	if key != None:
		return;
	
	info = retrieveData(url, mac,key,values = {
		'type' : 'stb', 
		'action' : 'handshake',
		'token' : '',
                'mac' : mac })
		
	key = info['js']['token']
#	info("STB_EMU test5: %s" %key )
	getProfile(url,mac,key);
	

def getProfile(url,mac,key):
	global sn, device_id, device_id2, signature;
	
	values = {
		'type' : 'stb', 
		'action' : 'get_profile',
		'hd' : '1',
		'ver' : 'ImageDescription:%200.2.18-r11-pub-254;%20ImageDate:%20Wed%20Mar%2018%2018:09:40%20EET%202015;%20PORTAL%20version:%204.9.14;%20API%20Version:%20JS%20API%20version:%20331;%20STB%20API%20version:%20141;%20Player%20Engine%20version:%200x572',
		'num_banks' : '1',
		'stb_type' : 'MAG254',
		'image_version' : '218',
		'auth_second_step' : '0',
		'hw_version' : '2.6-IB-00',
		'not_valid_token' : '0',
		'JsHttpRequest' : '1-xml'}

	if sn != None:
		values['sn'] = sn;
		values['device_id'] = device_id;
		values['device_id2'] = device_id2;
		values['signature'] = signature;


	info = retrieveData(url,mac,key ,values);

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
from resources.lib.handler.requestHandler import cRequestHandler
def eveData(url,mac,key , values ):

	mac =mac.replace(":","%3A")	
#	url += '/stalker_portal'
	load = 'server/load.php'
	refer = '/c/'
	timezone = 'Europe%2FParis;'
                           #Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3
	user_agent 	= 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3';
	
	if key != None:
		headers 	= { 
			'User-Agent' : user_agent, 
			'Cookie' : 'mac=' + mac + '; stb_lang=en; timezone=' + timezone,
			'Referer' : url + refer,
			'Accept' : 'text/html, */*',
			'Content-Type' : 'text/html',
			'X-User-Agent' : 'Model: MAG254; Link: Ethernet',
			'Authorization' : 'Bearer ' + key };
	
	else:
		headers 	= { 
			'User-Agent' : user_agent, 
			'Cookie' : 'mac=' + mac+ '; stb_lang=en; timezone=' + timezone,
			'Referer' : url + refer,
			'Accept' : '*/*',
			'Connection' : 'Keep-Alive',
			'X-User-Agent' : 'Model: MAG254; Link: Ethernet' };

	
	data = urllib.urlencode(values);
	
#        req = cRequestHandler(url + load, data, headers).request()
	req = urllib2.Request(key, data, headers);
	resp = urllib2.urlopen(req).read().encode("utf8").decode('iso-8859-1')

	
	if not is_json(resp):
		req = urllib2.Request(url + load + '?' + data, headers=headers);
		resp = urllib2.urlopen(req).read().encode("utf8").decode('iso-8859-1')



	if not is_json(resp):
		raise Exception(resp)

	info = json.loads(resp)

	return info;

def retrieveData(url,mac,key ,  values ):

		
#	url += '/stalker_portal'
	load = '/server/load.php'
	refer = '/c/'
	timezone = 'America%2FChicago';

	user_agent 	= 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3';
	
	if key != None:
		headers 	= { 
			'User-Agent' : user_agent, 
			'Cookie' : 'mac=' + mac + '; stb_lang=en; timezone=' + timezone,
			'Referer' : url + refer,
			'Accept' : '*/*',
			'Connection' : 'Keep-Alive',
			'X-User-Agent' : 'Model: MAG254; Link: Ethernet',
			'Authorization' : 'Bearer ' + key };
	
	else:
		headers 	= { 
			'User-Agent' : user_agent, 
			'Cookie' : 'mac=' + mac+ '; stb_lang=en; timezone=' + timezone,
			'Referer' : url+ refer ,
			'Accept' : '*/*',
			'Connection' : 'Keep-Alive',
			'X-User-Agent' : 'Model: MAG254; Link: Ethernet' };

	
	data = urllib.urlencode(values);
	

	req = urllib2.Request(url + load, data, headers);
	resp = urllib2.urlopen(req).read().decode("utf-8");
	
	if not is_json(resp):
		req = urllib2.Request(url + load + '?' + data, headers=headers);
		resp = urllib2.urlopen(req).read().decode("utf-8");

	if not is_json(resp):
		raise Exception(resp)

	info = json.loads(resp)

	return info;

def getPLAYER(mac, url, cmd, path):	
	global  cache_version;
	
	now = time();
	portalurl = "_".join(re.findall("[a-zA-Z0-9]+", url));
	portalurl = path + '/' + portalurl + '-genres';
	
##	setMac(portal_mac);
#	setSerialNumber(serial);
	
	if not os.path.exists(path): 
		os.makedirs(path);
	
	if os.path.exists(portalurl):
		#check last time
		with open(portalurl) as data_file: data = json.load(data_file);
		
		if 'version' not in data or data['version'] != cache_version:
			clearCache(url, path);
			
		else:
			time_init = float(data['time']);
			# update 12h
			if ((now - time_init) / 3600) < 12:
				return data;
	
	handshake(url,mac);
        key= url+'/portal.php?type=itv&action=create_link&cmd='+cmd+'&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'

        info = eveData(url,mac,key, values = {
		'type' : 'itv', 
		'create_link' : '',
                'cmd' : cmd,
		'series' : '',
		'forced_storage' : '0',
		'disable_ad' : '0',
		'download' : '0',
		'force_ch_link_check' : '0',
                'JsHttpRequest' : '1-xml'})		
	
        return   info

def getGenres(mac, url, serial, path):	
	global key, cache_version;
	
	now = time();
	portalurl = "_".join(re.findall("[a-zA-Z0-9]+", url));
	portalurl = path + '/' + portalurl + '-genres';
	
##	setMac(portal_mac);
#	setSerialNumber(serial);
	
	if not os.path.exists(path): 
		os.makedirs(path);
	
	if os.path.exists(portalurl):
		#check last time
		with open(portalurl) as data_file: data = json.load(data_file);
		
		if 'version' not in data or data['version'] != cache_version:
			clearCache(url, path);
			
		else:
			time_init = float(data['time']);
			# update 12h
			if ((now - time_init) / 3600) < 12:
				return data;
	
	handshake(url,mac);
	
        info = retrieveData(url,mac,key, values = {
		'type' : 'itv', 
		'action' : 'get_genres',
		'JsHttpRequest' : '1-xml'})
		
	
        return   info
	
	
#	data = data[:-3] + '\n}}'
      
#	with open(portalurl, 'w') as f: f.write(data.encode('utf-8'));
	     
#	return json.loads(data.encode('utf-8'));
	
def getVoD(mac, url, serial, path):	
	now = time();
	portalurl = "_".join(re.findall("[a-zA-Z0-9]+", url));
	portalurl = path + '/' + portalurl + '-vod';
	
	setMac(portal_mac);
	setSerialNumber(serial);
	
	if not os.path.exists(path):
		os.makedirs(path)
	
	if os.path.exists(portalurl):
		#check last time
		with open(portalurl) as data_file: data = json.load(data_file);
	
		if 'version' not in data or data['version'] != cache_version:
			clearCache(url, path);
			
		else:
			time_init = float(data['time']);
			# update 12h
			if ((now - time_init) / 3600) < 12:
				return data;
	
	handshake(url);
	
	data = '{ "version" : "' + cache_version + '", "time" : "' + str(now) + '", "vod" : [  \n'
	
	page = 1;
	pages = 0;
	total_items = 1.0;
	max_page_items = 1.0;
	
	while True:
		info = retrieveData(url,mac,key, values = {
			'type' : 'vod', 
			'action' : 'get_ordered_list',
			'sortby' : 'added',
			'not_ended' : '0',
			'p' : page,
			'fav' : '0',
			'JsHttpRequest' : '1-xml'})
		
		total_items = float(info['js']['total_items']);
		max_page_items = float(info['js']['max_page_items']);
		pages = math.ceil(total_items/max_page_items);
		
		results = info['js']['data']


		for i in results:
			name 	= i["name"]
			cmd 	= i['cmd']
			logo 	= i["screenshot_uri"]
		
			data += '{"name":"'+ name +'", "cmd":"'+ cmd +'", "logo":"'+ logo +'"}, \n'

		page += 1;
		if page > pages or page == 10:
			break;

	data = data[:-3] + '\n]}'

	with open(portalurl, 'w') as f: f.write(data.encode('utf-8'));
	
	return json.loads(data.encode('utf-8'));


def orderChannels(channels):
      	n_data = {};
      	for i in channels:	
      		number 		= i["number"];
      		n_data[int(number)] = i;
      	
      	ordered = sorted(n_data);
      	data = {};
      	for i in ordered:	
      		data[i] = n_data[i];
      		
      	return data.values();


def getAllChannels(mac, url, did, path):

	added = False;
	
	now = time();
	
	handshake(url,mac);
	
	genres = getGenres(mac, url, serial, path);

	


	page = 1;
	pages = 0;
	total_items = 0;
	max_page_items = 0;

	primler = [0,1,2,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19]
        for urg in primler: 
		# retrieve adults
		info = retrieveData(url,mac,key, values = {
			'type' : 'itv', 
			'action' : 'get_ordered_list',
			'genre' : did,
			'force_ch_link_check' : '',
                        'fav' : '0',
                        'sortby' : 'number',
                        'hd' : '0',
                        
                        'p' : urg ,
			'fav' : '0',
			'JsHttpRequest' : '1-xml',
                        'from_ch_id' : '0'})
	
		total_items = float(info['js']['total_items']);
		max_page_items = float(info['js']['max_page_items']);
		pages = math.ceil(total_items/max_page_items);
	
		

	

		page += 1;
		if page > pages:
			break;
	



	

	
		return info

def getEPG(portal_mac, url, serial, path):	
	global key, cache_version;
	
	now = time();
	portalurl = "_".join(re.findall("[a-zA-Z0-9]+", url));
	portalurl = path + '/' + portalurl + '-epg';
	
	setMac(portal_mac);
	setSerialNumber(serial);
	
	if not os.path.exists(path): 
		os.makedirs(path);
	
	if os.path.exists(portalurl):
		#check last time
		xmldoc = minidom.parse(portalurl);
		
		itemlist = xmldoc.getElementsByTagName('tv');
		
		version = itemlist[0].attributes['cache-version'].value;
		
		if version != cache_version:
			clearCache(url, path);
			
		else:
			time_init = float(itemlist[0].attributes['cache-time'].value);
			# update 2h
			if ((now - time_init) / 3600) < 2:
				return xmldoc.toxml(encoding='utf-8');
	

	channels = getAllChannels(portal_mac, url, serial, path);
	channels = channels['channels'];
	
	handshake(url);
	
	info = retrieveData(url,mac,key, values = {
		'type' : 'itv', 
		'action' : 'get_epg_info',
		'period' : '6',
		'JsHttpRequest' : '1-xml'})


	results = info['js']['data'];
	
	doc = minidom.Document();
	base = doc.createElement('tv');
	base.setAttribute("cache-version", cache_version);
	base.setAttribute("cache-time", str(now));
	base.setAttribute("generator-info-name", "IPTV Plugin");
	base.setAttribute("generator-info-url", "http://www.xmltv.org/");
	doc.appendChild(base)


	for c in results:
		
		if not str(c) in channels:
			continue;
	
		channel = channels[str(c)];
		name = channel['name'];
		
		c_entry = doc.createElement('channel');
		c_entry.setAttribute("id", str(c));
		base.appendChild(c_entry)
		
		
		dn_entry = doc.createElement('display-name');
		dn_entry_content = doc.createTextNode(name);
		dn_entry.appendChild(dn_entry_content);
		c_entry.appendChild(dn_entry);
	

	for k,v in results.iteritems():
	
		channel = None;
		
		if str(k) in channels:
			channel = channels[str(k)];
		
		for epg in v:
		
			start_time 	= datetime.fromtimestamp(float(epg['start_timestamp']));
			stop_time	= datetime.fromtimestamp(float(epg['stop_timestamp']));
			
			pg_entry = doc.createElement('programme');
			pg_entry.setAttribute("start", start_time.strftime('%Y%m%d%H%M%S -0000'));
			pg_entry.setAttribute("stop", stop_time.strftime('%Y%m%d%H%M%S -0000'));
			pg_entry.setAttribute("channel", str(k));
			base.appendChild(pg_entry);
			
			t_entry = doc.createElement('title');
			t_entry.setAttribute("lang", "en");
			t_entry_content = doc.createTextNode(epg['name']);
			t_entry.appendChild(t_entry_content);
			pg_entry.appendChild(t_entry);
			
			d_entry = doc.createElement('desc');
			d_entry.setAttribute("lang", "en");
			d_entry_content = doc.createTextNode(epg['descr']);
			d_entry.appendChild(d_entry_content);
			pg_entry.appendChild(d_entry);
			
			dt_entry = doc.createElement('date');
			dt_entry_content = doc.createTextNode(epg['on_date']);
			dt_entry.appendChild(dt_entry_content);
			pg_entry.appendChild(dt_entry);
			
			c_entry = doc.createElement('category');
			c_entry_content = doc.createTextNode(epg['category']);
			c_entry.appendChild(c_entry_content);
			pg_entry.appendChild(c_entry);
			
		
			if channel != None and channel['logo'] != '':
				i_entry = doc.createElement('icon');
				i_entry.setAttribute("src", url + '/stalker_portal/misc/logos/320/' + channel['logo']);
				i_entry.appendChild(i_entry_content);
				pg_entry.appendChild(i_entry);

	
	with open(portalurl, 'w') as f: f.write(doc.toxml(encoding='utf-8'));
	
	return doc.toxml(encoding='utf-8');
	



def retriveUrl(portal_mac, url, serial, channel, tmp):
	
	setMac(portal_mac);
	setSerialNumber(serial);
		
	if 'matrix' in channel:
		return retrieve_matrixUrl(url, channel);
		
	else:
		return retrive_defaultUrl(url, channel, tmp);
		
	
		
def retrive_defaultUrl(url, channel, tmp):

	if tmp == '0':
		s = channel.split(' ');
		url = s[0];
		if len(s)>1:
			url = s[1];
		return url;


	handshake(url);
	
	cmd = channel;
	

	info = retrieveData(url, values = {
		'type' : 'itv', 
		'action' : 'create_link', 
		'cmd' : channel,
		'forced_storage' : 'undefined',
		'disable_ad' : '0',
		'JsHttpRequest' : '1-xml'});
	cmd = info['js']['cmd'];
		
	s = cmd.split(' ');
			
	url = s[0];
	
	if len(s)>1:
		url = s[1];


	# RETRIEVE THE 1 EXTM3U
	request = urllib2.Request(url)
	request.get_method = lambda : 'HEAD'
	response  = urllib2.urlopen(request);
	data = response.read().decode("utf-8");
	
	
	data = data.splitlines();
	data = data[len(data) - 1];

	# RETRIEVE THE 2 EXTM3U
	url = response.geturl().split('?')[0];
	url_base = url[: -(len(url) - url.rfind('/'))]
	return url_base + '/' + data;

	
	return url;


def retrieve_matrixUrl(url, channel):

	channel = channel.split('/');
	channel = channel[len(channel) -1];
	
	url += '/stalker_portal/server/api/matrix.php?channel=' + channel + '&mac=' + mac;
	
	# RETRIEVE THE 1 EXTM3U
	request = urllib2.Request(url)
	response  = urllib2.urlopen(request);
	data = response.read().decode("utf-8");

	_s1 = data.split(' ');	
	data = _s1[0];
	if len(_s1)>1:
		data = _s1[len(_s1) -1];
	
	return data;



def retriveVoD(portal_mac, url, serial, video):
	
	setMac(portal_mac);
	setSerialNumber(serial);
		
	s = video.split(' ');
	url = s[0];
	if len(s)>1:
		url = s[1];

	
	url = url.replace('TOMTOM:', 'http://');
	

	# RETRIEVE THE 1 EXTM3U
	request = urllib2.Request(url)
	response  = urllib2.urlopen(request);
	url = response.geturl();


	# RETRIEVE THE 1 EXTM3U
	request = urllib2.Request(url)
	#request.get_method = lambda : 'HEAD'
	response  = urllib2.urlopen(request);
	data = response.read().decode("utf-8");
	data = data.splitlines();
	data = data[len(data) - 1];
	
	# RETRIEVE THE 2 EXTM3U
	url = response.geturl().split('?')[0];
	url_base = url[: -(len(url) - url.rfind('/'))]
	return url_base + '/' + data;

def clearCache(url, path):
	
	portalurl = "_".join(re.findall("[a-zA-Z0-9]+", url));
	
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.startswith(portalurl):
				os.remove(root + '/' + file);




