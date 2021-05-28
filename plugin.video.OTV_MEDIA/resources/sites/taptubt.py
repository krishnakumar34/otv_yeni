#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'taptubt'
import sys
from xbmcgui import ListItem
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from routing import Plugin

import os
import time
from requests.exceptions import RequestException
#from resources.lib.uktvnow import UKTVNow
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
plugin = Plugin()
plugin.name = addon.getAddonInfo("name")
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo("profile"))
data_time = int(addon.getSetting("data_time") or "0")
cache_time = int(addon.getSetting("cache_time") or "0")
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

def load():
        params = ParameterHandler()
        searchterm = False
        if params.exist('searchterm'):
            searchterm = params.getValue('searchterm')
        searchGlobal(searchterm)
      
      
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
        numPlugins = len(pluginEntry)
        VSlog('globalsearch-'+pluginEntry)
        dialog.update((count + 1) * 50 / numPlugins, 'Searching: ' +str(name) + '...')
        VSlog('Searching for %s at %s' % (sSearchText.decode('utf-8'), pluginEntry))
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
        dialog.update(count * 100 / total, str(count) + ' of ' + str(total) + ': ' +name)
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
      

