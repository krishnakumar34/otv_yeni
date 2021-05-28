import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os


ADDON = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
DATA_PATH = os.path.join(xbmc.translatePath('special://profile/data/plugin.video.OTV_MEDIA'), '')

def addon():
    return ADDON

def setView():
    if ADDON.getSetting('auto-view') == 'true':
        return True
    else:
        return False

        
        
