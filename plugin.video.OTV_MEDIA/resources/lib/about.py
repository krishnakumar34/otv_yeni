#-*- coding: utf-8 -*-
import urllib
import os
import json

import xbmc,xbmcaddon
from resources.lib.common import addonPath, profilePath
from resources.lib.download import cDownload
import sys
## Android K18 ZIP Fix.
if sys.version_info[0] == 2:
    from xbmc import translatePath, LOGNOTICE, LOGERROR, log, executebuiltin, getCondVisibility, getInfoLabel
else:
    from xbmc import LOGINFO as LOGNOTICE, LOGERROR, log, executebuiltin, getCondVisibility, getInfoLabel
    from xbmcvfs import translatePath
# Android K18 ZIP Fix.
if getCondVisibility('system.platform.android') and int(getInfoLabel('System.BuildVersion')[:2]) == 18:
    import fixetzipfile as zipfile
else:
    import zipfile


import requests
from resources.lib.comaddon import addon, progress, dialog, xbmcgui, window, VSlog, xbmc
from resources.lib.handler.requestHandler import cRequestHandler

import urllib
import xbmcvfs
import datetime, time
from resources.lib.config import cConfig
try:
    import json
except:
    import simplejson as json
from resources.lib import ziptools
SITE_IDENTIFIER = 'about'
SITE_NAME = 'About'

AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
localizedString = Addon.getLocalizedString
AddonName = Addon.getAddonInfo("name")
icon = Addon.getAddonInfo('icon')
addon_version = Addon.getAddonInfo('version')
addonDir = Addon.getAddonInfo('path')
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
#from resources.lib.handler.pluginHandler import cPluginHandler

ROOT_DIR = addonPath
ADDON_DIR = os.path.abspath(os.path.join(ROOT_DIR, '..'))
XSTREAM_DIRNAME = os.path.basename(ROOT_DIR)
AddonID = 'plugin.video.OTV_MEDIA'
addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ), AddonID)
def DownloaderClass(url,dest):
    
    dp = xbmcgui.DialogProgress()
    dp.create("OTV_MEDIA ZIP DOWNLOADER","Downloading File",url)
    urllib.request.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except: 
        percent = 100
        dp.update(percent)
        time.sleep(20)
        dp.close()
    if dp.iscanceled(): 
        dp.close()

dinamic_url = "https://netcologne.dl.sourceforge.net/project/e2-orhantv1/plugin.video.OTV_MEDIA.zip"

0
## Filename of the update File.
LOCAL_NIGHTLY_VERSION = os.path.join(profilePath, "orhantv_sha")

LOCAL_FILE_NAME_XSTREAM = 'update_orhantv.zip'


def OPEN_URL(url):
	
	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	link = requests.session().get(url, headers=headers, verify=False).text
	link = link.encode('ascii', 'ignore')
	return link
class cAbout:

		
      
    def getUpdate(self):
		
        sUrl = 'https://dl.dropboxusercontent.com/s/gzgt0smbzhioant/version'
#        data = urllib2.urlopen(sUrl).read()
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        tag_publicada = re.findall('"tag_name": "(.*?)"', sHtmlContent)[0]
        version_yen = re.findall('"tag_name": "(.*?)"', sHtmlContent)[0]
        version_local =cConfig().getAddonVersion()
        
        if (version_yen > version_local):

            extpath = os.path.join(xbmc.translatePath("special://home/addons/")) 
            dest = addon_data_dir + '/lastupdate.zip'                
            UPDATE_URL = 'https://netcologne.dl.sourceforge.net/project/e2-orhantv1/plugin.video.OTV_MEDIA-' + version_yen + '.zip'
            xbmc.log('START DOWNLOAD UPDATE:' + UPDATE_URL)
                
            DownloaderClass(UPDATE_URL,dest)  
                  
            
            unzipper = ziptools.ziptools()
            unzipper.extract(dest,extpath)
                
            line7 = 'New version installed .....'
            line8 = 'Version: ' + tag_publicada 
            xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)
                
            if os.remove( dest ):
                xbmc.log('TEMPORARY ZIP REMOVED')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.sleep(1500)


        if (version_yen > version_local):

            extpath = os.path.join(xbmc.translatePath("special://home/addons/")) 
            dest = addon_data_dir + '/temp.zip'  
                    
            urllib.urlretrieve(dinamic_url,dest)
            xbmc.log('START DOWNLOAD PARTIAL UPDATE:' + dinamic_url) 
                    
            
            unzipper = ziptools.ziptools()
            unzipper.extract(dest,extpath)
                    
            line7 = 'Plugin data updated .....'
            line8 = 'Description: ' + tag_publicada
            xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)
                    
            if os.remove( dest ): 
                xbmc.log('TEMPORARY ZIP REMOVED')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            u = False
        else:
            xbmc.log('No partial updates are available' )
            u = True
                        
