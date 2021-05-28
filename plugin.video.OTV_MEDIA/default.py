#-*- coding: utf-8 -*-
def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

PY3 = False

try:
    from urllib.parse import urlencode as Urlencode
    from urllib.parse import unquote_plus as Unquote_plus
    from urllib.parse import unquote as Unquote
    from urllib.request import HTTPHandler
    from urllib.request import build_opener
    from urllib.request import install_opener
    from urllib.error import HTTPError
    from urllib.request import Request
    from urllib.request import urlopen
    from html.entities import name2codepoint as n2cp
    PY3 = True; unicode = str; unichr = chr; long = int
except:
    from urllib import urlencode as Urlencode
    from urllib import unquote_plus as Unquote_plus
    from urllib import unquote as Unquote
    from urllib2 import HTTPHandler
    from urllib2 import build_opener
    from urllib2 import install_opener
    from urllib2 import HTTPError
    from urllib2 import Request
    from urllib2 import urlopen
    from htmlentitydefs import name2codepoint as n2cp


from resources.lib.util import urlEncode, Unquote
from resources.lib.util import UnquotePlus, Unquote
from resources.lib.util import QuotePlus
from resources.lib.gui.hoster import cHosterGui
from resources.lib.home import cHome
from resources.lib.gui.gui import cGui
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.comaddon import progress, VSlog, addon, window, xbmc
from resources.lib.util import Quote
# http://kodi.wiki/view/InfoLabels
# http://kodi.wiki/view/List_of_boolean_conditions
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.lib.config import cConfig
#import j2py
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.cconfig import ccConfig
import   sys, os
from resources.lib import common
from resources.lib.comaddon import addon
from os.path import join
from sys import path
from resources.lib.logger import logger 
addons= addon()
__settings__ = common.addon
__cwd__ = common.addonPath
 
path.append(join(__cwd__, "resources", "lib"))
path.append(join(__cwd__, "resources", "lib", "gui"))
path.append(join(__cwd__, "resources", "lib", "handler"))
path.append(join(__cwd__, "resources", "sites"))
#path.append(join(__cwd__, "sites"))
addons = addon()
class main:
 def __init__(self,argv=None):
    if sys.argv:
        argv = sys.argv
    self.parseUrl()
   
    
 

 
 def parseUrl(self):
        
            
       
        Params = cInputParameterHandler()
        oInputParameterHandler = cInputParameterHandler()
        if (oInputParameterHandler.exist('function')):
            #print 'Debug 3'
            sFunction = oInputParameterHandler.getValue('function')
        else:
            #print 'Debug 4'
            cConfig().log('call load methode')
            sFunction = "load"

        #print 'Debug 5'   
        if (sFunction=='DoNothing'):
            return

        if (oInputParameterHandler.exist('site')):
            sSiteName = oInputParameterHandler.getValue('site')
            sSiteName=sSiteName.replace('-','')


            
            if Params.exist('playMode'):
               from resources.lib.gui.ahoster import HosterGui
               url = False
               playMode = Params.getValue('playMode')
               isHoster = Params.getValue('isHoster')
               url = Params.getValue('url')
               manual = Params.exist('manual')
               if ccConfig().getSetting(
                       'hosterSelect') == 'Auto' and playMode != 'jd' and playMode != 'jd2' and playMode != 'pyload' and not manual:
                   HosterGui().streamAuto(playMode, sSiteName, sFunction)
               else:
                   HosterGui().stream(playMode, sSiteName, sFunction, url)
               return             
            
            if isHosterGui(sSiteName, sFunction):
                return

            if isGui(sSiteName, sFunction):
                return

            if isFav(sSiteName, sFunction):
                return

            if isLibrary(sSiteName, sFunction):
                return

            if isDl(sSiteName, sFunction):
                return

            if isHome(sSiteName, sFunction):
                return

            if isTrakt(sSiteName, sFunction):
                return

            if sSiteName == 'globalSearch':
                searchGlobal()
                return

            if sSiteName == 'globalRun':
                __import__('resources.lib.runscript', fromlist = ['runscript'])
                # function = getattr(plugins, sFunction)
                # function()
                return

            if sSiteName == 'globalSources':
                oGui = cGui()
                oPluginHandler = cPluginHandler()
                aPlugins = oPluginHandler.getAvailablePlugins(True)

                if len(aPlugins) == 0:
                    addons = addon()
                    addons.openSettings()
                    xbmc.executebuiltin('Container.Refresh')
                else:
                    for aPlugin in aPlugins:
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
                        icon = 'sites/%s.png' % (aPlugin[1])
                        # icon = 'https://imgplaceholder.com/512x512/transparent/fff?text=%s&font-family=Roboto_Bold' % aPlugin[1]
                        oGui.addDir(aPlugin[1], 'load', aPlugin[0], icon, oOutputParameterHandler)

                oGui.setEndOfDirectory()
                return

            if sSiteName == 'globalParametre':
                addons = addon()
                addons.openSettings()
                return
            # if isAboutGui(sSiteName, sFunction) == True:
                # return

            #if (isAboutGui(sSiteName, sFunction) == True):            
                #return

       
#            exec "plugin://" + plugin
#            exec "plugin."+ sFunction +"()"
            exec("from resources.sites import " + sSiteName + " as plugin")
            exec("plugin."+ sFunction +"()")
           
            #    cConfig().log('could not load site: ' + sSiteName )
        else:
        
            plugins = __import__('resources.lib.home', fromlist=['home']).cHome()
            function = getattr(plugins, 'load')
            function()
            return

#            plugins = __import__('resources.sayfalar.orhantv', fromlist=['orhantv']).orhantv()
#            function = getattr(plugins, 'load')
#            function()
#            return
            
                     
           
            if sSiteName == 'orhantv':

                oGui = cGui()
                oPluginHandler = cPluginHandler()
                aPlugins = oPluginHandler.getAvailablePlugins(True)
                if (len(aPlugins) == 0):
                    addons = addon()
                    addons.openSettings()
                    xbmc.executebuiltin("Container.Refresh")
                else:
                    for aPlugin in aPlugins:

                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', 'http://orhan')
                        icon = 'sites/%s.png' % (aPlugin[1])
                        #icon = 'https://imgplaceholder.com/512x512/transparent/fff?text=%s&font-family=Roboto_Bold' % aPlugin[1]
                        oGui.addDir(aPlugin[1], 'load', aPlugin[0], icon, oOutputParameterHandler)

            oGui.setEndOfDirectory()            
               

 
            

       
        
def isHosterGui(sSiteName, sFunction):
    if (sSiteName == 'cHosterGui'):
        oHosterGui = cHosterGui()
        exec("oHosterGui."+ sFunction +"()")
        return True
    return False
    
def isGui(sSiteName, sFunction):
    if (sSiteName == 'cGui'):
        oGui = cGui()
        exec("oGui."+ sFunction +"()")
        return True
    return False
    
def isFav(sSiteName, sFunction):
    if (sSiteName == 'cFav'):
        from resources.lib.favourite import cFav
        oFav = cFav()
        exec("oFav."+ sFunction +"()")
        return True
    return False
    
def isLibrary(sSiteName, sFunction):
    if (sSiteName == 'cLibrary'):
        from resources.lib.library import cLibrary
        oLibrary = cLibrary()
        exec("oLibrary."+ sFunction +"()")
        return True
    return False

def isDl(sSiteName, sFunction):
    if (sSiteName == 'cDownload'):
        from resources.lib.download import cDownload
        oDownload = cDownload()
        exec("oDownload."+ sFunction +"()")
        return True
    return False

def isHome(sSiteName, sFunction):
    if (sSiteName == 'cHome'):
        oHome = cHome()
        exec("oHome."+ sFunction +"()")
        return True
    return False
def isTrakt(sSiteName, sFunction):
    if sSiteName == 'cTrakt':
        from resources.lib.trakt import cTrakt
        oTrakt = cTrakt()
        exec ("oTrakt." + sFunction + "()")
        return True
    return False

def searchGlobal():
    oGui = cGui()
    addons = addon()

    oInputParameterHandler = cInputParameterHandler()
    sSearchText = oInputParameterHandler.getValue('searchtext')
    sCat = oInputParameterHandler.getValue('sCat')

    oHandler = cRechercheHandler()
    oHandler.setText(sSearchText)
    oHandler.setCat(sCat)
    aPlugins = oHandler.getAvailablePlugins()
    if not aPlugins:
        return True

    total = len(aPlugins)
    progress_ = progress().VScreate()

    # kodi 17 vire la fenetre busy qui se pose au dessus de la barre de Progress
    try:
        xbmc.executebuiltin('Dialog.Close(busydialog)')
    except:
        pass

    oGui.addText('globalSearch', addons.VSlang(30081) % sSearchText, 'none.png')
    sSearchText = Quote(sSearchText)

    count = 0
    for plugin in aPlugins:
 
        progress_.VSupdate(progress_, total, plugin['name'], True)
        if progress_.iscanceled():
            progress_.close()
            break
 
        oGui.searchResults[:] = []  # vider le tableau de résultats pour les récupérer par source
        _pluginSearch(plugin, sSearchText)

        if len(oGui.searchResults) > 0: # Au moins un résultat
            count += 1

            # nom du site
            oGui.addText(plugin['identifier'], '%s. [COLOR olive]%s[/COLOR]' % (count, plugin['name']), 'sites/%s.png' % (plugin['identifier']))
            for result in oGui.searchResults:
                oGui.addFolder(result['guiElement'], result['params'])
 
    if not count:   # aucune source ne retourne de résultats
        oGui.addText('globalSearch') # "Aucune information"

    progress_.VSclose(progress_)

    oGui.setEndOfDirectory()
    return True


def _pluginSearch(plugin, sSearchText):

    # Appeler la source en mode Recherche globale
    window(10101).setProperty('search', 'true')
    
    try:
        plugins = __import__('resources.sites.%s' % plugin['identifier'], fromlist = [plugin['identifier']])
        function = getattr(plugins, plugin['search'][1])
        sUrl = plugin['search'][0] + str(sSearchText)
        
        function(sUrl)
        
        VSlog('Load Search: ' + str(plugin['identifier']))
    except:
        VSlog(plugin['identifier'] + ': search failed')

    window(10101).setProperty('search', 'false')


def encode_log(message=""):
    # Unicode to utf8
    if type(message) == str:
        message = message.encode("utf8")

    # All encodings to utf8
    elif type(message) == str:
        message = str(message, "utf8", errors="replace").encode("utf8")

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




params= get_params()

url = None
name = None
mode = None
iconimage = None

try:
	url = Unquote_plus(params["url"])
        
except:
	pass
try:
	name = Unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = Unquote_plus(params["iconimage"])
except:
	pass
try:
    fanart = unquote_plus(params["fanart"])
except:
    pass
try:
    description = unquote_plus(params["description"])
except:
    pass
try:
    query = unquote_plus(params["query"])
except:
    pass
VSlog("Mode: " + str(mode))

VSlog( "Name: " + str(name))
VSlog("iconimage: " + str(iconimage))
    

if mode == None or url == None or len(url) < 1:
     sys.exit(main())
elif mode == 1:
     from resources.sites.adult import search
     search()

elif mode == 2:
     xbmc.log("mode==2, starturl=%s" % url, xbmc.LOGERROR)
     from resources.sites.adult import *
     start(url)

elif mode == 3:
     from resources.sites.adult import media_list
     media_list(url)
elif mode == 4:
     from resources.sites.adult import *
     resolve_url(url)
elif mode == 8:
     from resources.sites.adult import redtube_sorting
     redtube_sorting(url)
elif mode == 9:
     from resources.sites.adult import redtube_categories
     redtube_categories(url)
elif mode == 12:
     from resources.sites.adult import lubtetube_pornstars
     lubtetube_pornstars(url)
elif mode == 13:
     from resources.sites.adult import flv_channels_list
     flv_channels_list(url)
elif mode == 16:
     from resources.sites.adult import vikiporn_categories
     vikiporn_categories(url)
elif mode == 17:
     from resources.sites.adult import xhamster_categories
     xhamster_categories(url)
elif mode == 18:
     from resources.sites.adult import fantasti_categories
     fantasti_categories(url)
elif mode == 23:
     from resources.sites.adult import zbporn_categories
     zbporn_categories(url)
elif mode == 24:
     from resources.sites.adult import xhamster_content
     xhamster_content(url)
elif mode == 27:
     from resources.sites.adult import xvideos_categories
     xvideos_categories(url)
elif mode == 28:
     from resources.sites.adult import youjizz_categories
     youjizz_categories(url)
elif mode == 29:
     from resources.sites.adult import hentaigasm_categories
     hentaigasm_categories(url)
elif mode == 30:
     from resources.sites.adult import ashemaletube_categories
     ashemaletube_categories(url)
elif mode == 32:
     from resources.sites.adult import xvideos_pornstars
     xvideos_pornstars(url)
elif mode == 33:
     from resources.sites.adult import heavyr_categories
     heavyr_categories(url)
elif mode == 39:
     from resources.sites.adult import pornxs_categories
     pornxs_categories(url)
elif mode == 41:
     from resources.sites.adult import gotporn_content
     gotporn_content(url)
elif mode == 42:
     from resources.sites.adult import xhamster_rankigs
     xhamster_rankigs(url)
elif mode == 44:
     from resources.sites.adult import motherless_sorting
     motherless_sorting(url)
elif mode == 45:
     from resources.sites.adult import emplix_categories
     emplix_categories(url)
elif mode == 46:
     from resources.sites.adult import emplix_sorting
     emplix_sorting(url)
elif mode == 48:
     from resources.sites.adult import fantasti_collections
     fantasti_collections(url)
elif mode == 49:
     from resources.sites.adult import fatasti_sorting
     fatasti_sorting(url)
elif mode == 52:
     from resources.sites.adult import yespornplease_categories
     yespornplease_categories(url)
elif mode == 54:
     from resources.sites.adult import uflash_categories
     uflash_categories(url)
elif mode == 55:
     from resources.sites.adult import ashemaletube_pornstars
     ashemaletube_pornstars(url)
elif mode == 60:
     from resources.sites.adult import motherless_galeries_ca
     motherless_galeries_cat(url)
elif mode == 61:
     from resources.sites.adult import motherless_being_watched_now
     motherless_being_watched_now(url)
elif mode == 62:
     from resources.sites.adult import motherless_groups_cat
     motherless_groups_cat(url)
elif mode == 64:
     from resources.sites.adult import javbangers_categories
     javbangers_categories(url)
elif mode == 68:
     from resources.sites.adult import luxuretv_categories
     luxuretv_categories(url)
elif mode == 71:
      from resources.sites.adult import xvideos_sorting
      xvideos_sorting(url)
                       
elif mode == 114:
     from resources.sites.stb_emula import *
     m3uCategory(url,False )
elif mode == 120:
     from resources.sites.stb_emula import *
     AddNewList()
elif mode == 121 or mode == 154 or mode == 160 or mode == 164:
    
     from resources.sites.stb_emula import *
     PMFolder( url )	
elif mode == 122:
    from resources.sites.stb_emula import *
    RemoveFromLists(url)
elif mode == 123:
    from resources.sites.stb_emula import *
    ChangeName(name,playlistsFile2,"name",10004)
elif mode == 124:
    from resources.sites.stb_emula import *
    ChangeUrl(url,playlistsFile2,"url",10005)
elif mode == 161:
    from resources.sites.stb_emula import *
    ChangeName(name,playlistsFile4,"name",10004)        
elif mode == 169:
    from resources.sites.stb_emula import *
    ChangeName(name,favoritesFile,"name",10004)
elif mode == 125:
    from resources.sites.stb_emula import importList
    importList()
elif mode == 126:
    from resources.sites.stb_emula import *
    if os.path.isfile( playlistsFile3 ) :
        if os.path.isfile( playlistsFile2 ) : os.remove( playlistsFile2 )
        shutil.copyfile( playlistsFile3, playlistsFile2 )
        xbmc.sleep ( 200 )
        os.remove( playlistsFile3 )
        xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}')".format(AddonID))
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName,addons.VSlang(10125).encode('utf-8'), 3600, icon)) 
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName,addons.VSlang(10126).encode('utf-8'), 3600, icon))


elif mode == 191:
     from resources.sites.stb_emula import PM_index
     PM_index()
elif mode == 192:
     from resources.sites.stb_emula import unzip_PM_data
     unzip_PM_data()

elif mode == 115:
    from resources.sites.stb_emula import *
    if url.find("urhd.tv")>0:
        try:
            url = common.urhd(url)
        except:
            pass
    if url.startswith("opus"):
        url = Opus(url)    
        
    Play_f4mProxy(url, name, iconimage)

elif mode == 180:
     from resources.sites.stb_emula import PM_index
     PM_index()
elif mode == 116 or mode == 117:
    from resources.sites.stb_emula import *
    DF = xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path')
    
    if not DF=='':  
        dpath = DF
    else:    
        dpath = DFolder
    
    ext = url.split('.')[-1]
    
    fileS = dpath + name + "." + ext + ".stopped"
    if not os.path.isfile(fileS):
        
        title = addons.VSlang(10203).encode('utf-8')
        string = GetKeyboardText(title, name)
        if len(string) >0:    
            common.StartDowloader(url,string,mode,DFolder)
    else:
        common.StartDowloader(url,name,mode,DFolder)

elif mode == 157 or mode == 172:
     from resources.sites.stb_emula import comon
     comon.StopDowloader(url,name,mode,DFolder)
elif mode == 158 or mode == 171:
    from resources.sites.stb_emula import comon
    comon.DeletePartialDowload(url,name,mode,DFolder)       
       
elif mode == 165 or mode == 181:
    from resources.sites.stb_emula import *
    title = addons.VSlang(10250).encode('utf-8')
    string = GetKeyboardText(title, "")
    if len(string) >0:
        string = string.lower()
        if url == "search":
            sch_global(string)
        elif mode == 81:
            findm3u(url, string)
        else:
            sch_folder(url,string)
elif mode == 113:
    from resources.sites.xiptvozel  import  STB_EMU
    STB_EMU(url,name)
        
elif mode == 116 or mode == 117:
    from resources.sites.stb_emula import comon
    DF = xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path')
    
    if not DF=='':  
        dpath = DF
    else:    
        dpath = DFolder
    
    ext = url.split('.')[-1]
    
    fileS = dpath + name + "." + ext + ".stopped"
    if not os.path.isfile(fileS):
        
        title = addons.VSlang(10203).encode('utf-8')
        string = GetKeyboardText(title, name)
        if len(string) >0:    
            comon.StartDowloader(url,string,mode,DFolder)
    else:
        comon.StartDowloader(url,name,mode,DFolder)
        
elif mode == 159:
    from resources.sites.stb_emula import comon
    comon.StartDowloader(url,name,mode,DFolder)                 
elif mode == 157 or mode == 172:
    from resources.sites.stb_emula import *
    common.StopDowloader(url,name,mode,DFolder)
elif mode == 158 or mode == 171:
    from resources.sites.stb_emula import *
    common.DeletePartialDowload(url,name,mode,DFolder)
elif mode == 110:
    # deleted
    sys.exit()
elif mode == 120:
    from resources.sites.stb_emula import AddNewList
    AddNewList()
elif mode == 121 or mode == 54 or mode == 60 or mode == 64:
    from resources.sites.stb_emula import PMFolder
    PMFolder( url )
elif mode == 122:
    RemoveFromLists(url)
elif mode == 123:
    from resources.sites.stb_emula import ChangeName
    ChangeName(name,playlistsFile2,"name",10004)
elif mode == 124:
    from resources.sites.stb_emula import ChangeUrl
    ChangeUrl(url,playlistsFile2,"url",10005)
elif mode == 161:
    from resources.sites.stb_emula import ChangeName
    ChangeName(name,playlistsFile4,"name",10004)        
elif mode == 169:
    ChangeName(name,favoritesFile,"name",10004)
elif mode == 125:
    from resources.sites.stb_emula import importList
    importList()
elif mode == 126:
    from resources.sites.stb_emula import *
    if os.path.isfile( playlistsFile3 ) :
        if os.path.isfile( playlistsFile2 ) : os.remove( playlistsFile2 )
        shutil.copyfile( playlistsFile3, playlistsFile2 )
        xbmc.sleep ( 200 )
        os.remove( playlistsFile3 )
        xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}')".format(AddonID))
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName,addons.VSlang(10125).encode('utf-8'), 3600, icon)) 
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName,addons.VSlang(10126).encode('utf-8'), 3600, icon))
elif mode == 130:
    from resources.sites.stb_emula import ListFavorites
    ListFavorites()
elif mode == 131: 
    from resources.sites.stb_emula import AddFavorites
    AddFavorites(url, iconimage, name)
elif mode == 155:
    from resources.sites.stb_emula import RemoveDirFromLists
    RemoveDirFromLists(url,name)
elif mode == 156:
    from resources.sites.stb_emula import *
    os.remove( os.path.join(pwdir, base64.standard_b64encode(url))) 
    xbmc.executebuiltin("XBMC.Container.Refresh()")
elif mode == 133:
    from resources.sites.stb_emula import RemoveFavorties
    RemoveFavorties(url)       
elif mode == 112:
    from resources.sites.stb_emula import m3uCategory 
    m3uCategory(url)
elif mode == 139:
    from resources.sites.stb_emula import PM_index
    PM_index()
#elif mode == 70:   
	#Header = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        #url = url+ '|' + Header 
#    item = xbmcgui.ListItem(name, path = url)
#    item.setMimeType('video/mp4')
#    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
xbmcplugin.endOfDirectory(int(sys.argv[1]))