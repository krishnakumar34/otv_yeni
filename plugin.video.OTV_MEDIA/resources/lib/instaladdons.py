# -*- coding: utf-8 -*-
SITE_IDENTIFIER = 'instaladdons'
SITE_NAME = 'instaladdons'
import re,urllib2
from resources.lib.otvhelper import * 
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os
import time
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler

from resources.lib import downloader
from resources.lib import kodi
from resources.lib import extract
from resources.lib import addon_able
dialog = xbmcgui.Dialog()
class addonsEnabled():
 def __init__(self, addon_id):
        self.addon_id=addon_id
        DISABLE_PATH = os.path.join(xbmc.translatePath('special://profile').decode('utf-8'), 'addon_data', '%s', 'DISABLED')%self.addon_id
        ENABLE_PATH = os.path.join(xbmc.translatePath('special://profile').decode('utf-8'), 'addon_data', '%s', 'ENABLED')%self.addon_id
        

        self.enableAddon()          
 def getXBMCVersion(self):
    import json
    resp = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Application.GetProperties", "params": {"properties": ["version", "name"]}, "id": 1 }')
    data = json.loads(resp)
    if not 'result' in data: return None
    if not 'version' in data['result']: return None
    return data['result']['version']

      

 def addonIsEnabled(self):
    DISABLE_PATH = os.path.join(xbmc.translatePath('special://profile').decode('utf-8'), 'addon_data', '%s', 'DISABLED')%self.addon_id
    if os.path.exists(DISABLE_PATH):
        return False

    if self.isPostInstalled():
        import json
        resp = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "id": 1, "method": "Addons.GetAddonDetails", "params": {"addonid":"%s","properties": ["name","version","enabled"]}}'%self.addon_id)
        data = json.loads(resp)
        if not 'result' in data: return False
        if not 'addon' in data['result']: return False
        if not 'enabled' in data['result']['addon']: return False
        return data['result']['addon']['enabled']
    else:
        return True


 def toggleEnabled(self):
    try:
        if not addonIsEnabled(): raise Exception('Addon Disabled')
        xbmcaddon.Addon('%s')
        xbmc.log('%s: DISABLING')
        xbmc.executebuiltin('XBMC.RunScript(%s,key.SHUTDOWN)')%self.addon_id
    except:
        xbmc.log('%s: ENABLING')
        enableAddon()


 def reset(self):
    if not addonIsEnabled(): return
    disableAddon()
    ct=0
    while addonIsEnabled() and ct < 11:
        xbmc.sleep(500)
        ct+=1
    enableAddon()


 def isPostInstalled(self):
    homePath = xbmc.translatePath('special://home').decode('utf-8')
    postInstalledPath = os.path.join(homePath, 'addons', '%s')%self.addon_id
    return os.path.exists(postInstalledPath)

 def markPreOrPost(self,enable=False, disable=False):
    ENABLE_PATH = os.path.join(xbmc.translatePath('special://profile').decode('utf-8'), 'addon_data', '%s', 'ENABLED')%self.addon_id
    DISABLE_PATH = os.path.join(xbmc.translatePath('special://profile').decode('utf-8'), 'addon_data', '%s', 'DISABLED')%self.addon_id
    if os.path.exists(ENABLE_PATH) or enable:
        with open(ENABLE_PATH, 'w') as f:
            f.write(self.isPostInstalled() and 'POST' or 'PRE')

    if os.path.exists(DISABLE_PATH) or disable:
        with open(DISABLE_PATH, 'w') as f:
            f.write(self.isPostInstalled() and 'POST' or 'PRE')


 def enableAddon(self):
    BASE = '{ "jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": { "addonid": "'+self.addon_id+'","enabled":%s}, "id": 1 }'
    DISABLE_PATH = os.path.join(xbmc.translatePath('special://profile').decode('utf-8'), 'addon_data', '%s', 'DISABLED')%self.addon_id
    if os.path.exists(DISABLE_PATH):
        os.remove(DISABLE_PATH)

    self.markPreOrPost(enable=True)

    if self.isPostInstalled():
        if self.addonIsEnabled():
            xbmc.executebuiltin('RunScript(%s)'%self.addon_id)
        else:
            xbmc.executeJSONRPC(BASE % 'true') #So enable it instead
    else:
        xbmc.executebuiltin('RunScript(%s)'%self.addon_id)

def enableaddons(url):
   
    if not 'video' in url:
        m = re.search('.*?/(script.module.*?.zip)', url)
           
        zipi = m.groups(1)[0]
        m = re.search('.*?/(script.module.*?).zip', url)
           
        addon_id = m.groups(1)[0]
    
    else:    
    
        m = re.search('.*?/(plugin.video.*?.zip)', url)
           
        zipi = m.groups(1)[0]
        m = re.search('.*?/(plugin.video.*?).zip', url)
           
        addon_id = m.groups(1)[0]
    path = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Please Wait", " ", '', 'Installing Official OpenSubtitles Addon')
    lib = os.path.join(path, ''+zipi)
    try:
        os.remove(lib)
    except OSError:
        pass
   
    downloader.download(url, lib, dp, timeout=120)
    addonfolder = xbmc.translatePath(os.path.join('special://', 'home', 'addons'))
    time.sleep(2)
    try:
        extract.all(lib, addonfolder, '')
    except IOError as e:
        kodi.message("Failed to open required files", "Error is: ", str(e))
        return False
        
    xbmc.executebuiltin('CECActivateSource')
    xbmc.executebuiltin("InstallAddon(%s)"%addon_id)
    xbmc.executebuiltin("RunAddon(%s)"%addon_id)
    xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
    addon_able.set_enabled("service.subtitles.opensubtitles_by_opensubtitles")
    xbmc.executebuiltin("RunScript(%s"%addon_id)
    addon = xbmcaddon.Addon()
#    SER_DATA_DIR = os.path.join(xbmc.translatePath('special://profile').decode('utf-8')
    SER_DATA_DIR = xbmc.translatePath(('special://profile').decode("utf-8"))
    if not os.path.exists(os.path.join(SER_DATA_DIR,  "addon_data",""+addon_id)):
        os.mkdir(os.path.join(SER_DATA_DIR, "addon_data", ""+addon_id))

    addonsEnabled(addon_id)
    dialog.ok("Installation Complete!", "    We hope you enjoy your Kodi addon experience!",
              "    Brought To You By  Orhan t")                                               

def Enableaddons():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    if not 'video' in url:
        m = re.search('.*?/(script.module.*?.zip)', url)
           
        zipi = m.groups(1)[0]
        m = re.search('.*?/(script.module.*?).zip', url)
           
        addon_id = m.groups(1)[0]
    
    else:    
    
        m = re.search('.*?/(plugin.video.*?.zip)', url)
           
        zipi = m.groups(1)[0]
        m = re.search('.*?/(plugin.video.*?).zip', url)
           
        addon_id = m.groups(1)[0]
    path = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Please Wait", " ", '', 'Installing Official OpenSubtitles Addon')
    lib = os.path.join(path, ''+zipi)
    try:
        os.remove(lib)
    except OSError:
        pass
   
    downloader.download(url, lib, dp, timeout=120)
    addonfolder = xbmc.translatePath(os.path.join('special://', 'home', 'addons'))
    time.sleep(2)
    downloader.download(url, lib, dp, timeout=120)
    addonfolder = xbmc.translatePath(os.path.join('special://', 'home', 'addons'))

    
    try:
        extract.all(lib, addonfolder, '')
    except IOError as e:
        kodi.message("Failed to open required files", "Error is: ", str(e))
        return False
        
    xbmc.executebuiltin('CECActivateSource')
    xbmc.executebuiltin("InstallAddon(%s)"%addon_id)
    xbmc.executebuiltin("RunAddon(%s)"%addon_id)
    xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
    addon_able.set_enabled("service.subtitles.opensubtitles_by_opensubtitles")
    xbmc.executebuiltin("RunScript(%s"%addon_id)
    addon = xbmcaddon.Addon()
#    SER_DATA_DIR = os.path.join(xbmc.translatePath('special://profile').decode('utf-8')
    SER_DATA_DIR = xbmc.translatePath(('special://profile').decode("utf-8"))
    if not os.path.exists(os.path.join(SER_DATA_DIR,  "addon_data",""+addon_id)):
        os.mkdir(os.path.join(SER_DATA_DIR, "addon_data", ""+addon_id))

    addonsEnabled(addon_id)
    dialog.ok("Installation Complete!", "    We hope you enjoy your Kodi addon experience!",
              "    Brought To You By  Orhan t")