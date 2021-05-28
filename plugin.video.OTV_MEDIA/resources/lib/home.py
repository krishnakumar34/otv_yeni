#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
#Venom.
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
#from resources.lib.handler.pluginHandler import cPluginHandler
#from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.siteHandler import cSiteHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.db import cDb
from resources.lib.about import cAbout
from resources.lib.comaddon import addon, window
import xbmc, urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
from resources.lib.handler.ParameterHandler import ParameterHandler

from resources.lib.comaddon import progress, VSlog
from resources.lib.handler.requestHandler import cRequestHandler
SITE_IDENTIFIER = 'cHome'
SITE_NAME = 'Home'

#temp d'execution
# import time, random

# l = range(100000)

# tps1 = time.clock()
# random.shuffle(l)
# l.sort()
# tps2 = time.clock()
# print(tps2 - tps1)

class cHome:

    ADDON = addon()


    def load(self):

        oGui = cGui()

        if (self.ADDON.getSetting('home_update') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'showUpdate', '%s (%s)' % (self.ADDON.VSlang(30418), self.ADDON.getSetting('service_futur')), 'update.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('fox_com_tr', 'orhatvturk', 'TÜrK_MEDIA', 'turkbayragi.png', oOutputParameterHandler)
        
                                        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('xiptvozel', 'iptvuser_info', 'WORLD IPTV', 'worldiptv.jpg', oOutputParameterHandler)


        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('xiptvozel', 'spor', 'SPORT', 'sports.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('adult_eu', 'orhantvalman', 'GERMANY_MEDIA+18', 'alman.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('iptvbox', 'kurdtv', 'KÜrd Media', 'karwan-tv-1.png', oOutputParameterHandler)
       
        
#        oOutputParameterHandler = cOutputParameterHandler()
#        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
#        oGui.addDir('liveonlinetv247', 'Sport', self.ADDON.VSlang(30113), 'sport.jpg', oOutputParameterHandler)
#        oOutputParameterHandler = cOutputParameterHandler()
#        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
#        oGui.addDir('xiptvozel', 'STB_EMUM_info', 'STB Emulator', 'stbemu.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('youtubecom_tr', 'YouTUBE', 'YouTUBE', 'youtube.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('filmon_com', 'FILMON', 'FILMON' , 'FilmOntv.jpg', oOutputParameterHandler)
        
#        oOutputParameterHandler = cOutputParameterHandler()
#        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
#        oGui.addDir('movies365', 'movies365', 'MOVIES_365', 'mov365.png', oOutputParameterHandler)


#        oOutputParameterHandler = cOutputParameterHandler()
#        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
#        oGui.addDir('orhantv', 'otvtest', self.ADDON.VSlang(30023) , 'radio.jpg', oOutputParameterHandler)

                

        view = False
        if (self.ADDON.getSetting("active-view") == 'true'):
            view = self.ADDON.getSetting('accueil-view')

        oGui.setEndOfDirectory(view)

          
 
    def showUpdate(self):
            from resources.lib.about import cAbout
            cAbout()
       
    def mshowUsers(self):
        


        oGui = cGui()
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'searchGlobal', self.ADDON.VSlang(30076), 'search.png', oOutputParameterHandler)
      

        oGui.setEndOfDirectory()


 

    # def showSources(self):
    #     oGui = cGui()

    #     oPluginHandler = cPluginHandler()
    #     aPlugins = oPluginHandler.getAvailablePlugins()
    #     for aPlugin in aPlugins:
    #         oOutputParameterHandler = cOutputParameterHandler()
    #         oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    #         icon = 'sites/%s.png' % (aPlugin[1])
    #         oGui.addDir(aPlugin[1], 'load', aPlugin[0], icon, oOutputParameterHandler)

    #     oGui.setEndOfDirectory()
        
   

    def showHistory(self):

        oGui = cGui()

        row = cDb().get_history()
        if row:
            oGui.addText(SITE_IDENTIFIER, self.ADDON.VSlang(30416))
        else :
            oGui.addText(SITE_IDENTIFIER)
        for match in row:
            oOutputParameterHandler = cOutputParameterHandler()

            #code to get type with disp
            type = self.ADDON.getSetting('search' + match[2][-1:] + '_type')
            if type:
                oOutputParameterHandler.addParameter('type', type)
                #xbmcgui.Window(10101).setProperty('search_type', type)
                window(10101).setProperty('search_type', type)

            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oOutputParameterHandler.addParameter('searchtext', match[1])
            #oOutputParameterHandler.addParameter('disp', match[2])
            #oOutputParameterHandler.addParameter('readdb', 'False')


            oGuiElement = cGuiElement()
            oGuiElement.setSiteName('globalSearch')
            oGuiElement.setFunction('globalSearch')
            oGuiElement.setTitle("- " + match[1])
            oGuiElement.setFileName(match[1])
            oGuiElement.setCat(match[2])
            oGuiElement.setIcon("search.png")
            oGui.CreateSimpleMenu(oGuiElement,oOutputParameterHandler,SITE_IDENTIFIER,'cHome','delSearch', self.ADDON.VSlang(30412))
            oGui.addFolder(oGuiElement, oOutputParameterHandler)

        if row:

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'delSearch', self.ADDON.VSlang(30413), 'search.png', oOutputParameterHandler)


        oGui.setEndOfDirectory()

    def delSearch(self):
        cDb().del_history()
        return True


    def callpluging(self):
        oGui = cGui()

        oInputParameterHandler = cInputParameterHandler()
        sSiteUrl = oInputParameterHandler.getValue('siteUrl')

        oPluginHandler = cSiteHandler()
        aPlugins = oPluginHandler.getAvailablePlugins(sSiteUrl)
        for aPlugin in aPlugins:
            try:
                #exec "import " + aPlugin[1]
                #exec "sSiteUrl = " + aPlugin[1] + "." + sVar
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', aPlugin[0])
                icon = 'sayfalar/%s.png' % (aPlugin[2])
                oGui.addDir(aPlugin[2], aPlugin[3], aPlugin[1], icon, oOutputParameterHandler)
            except:
                pass

        oGui.setEndOfDirectory()

    # def searchMovie(self):
    #     oGui = cGui()
    #     oInputParameterHandler = cInputParameterHandler()
    #     sSearchText = oInputParameterHandler.getValue('searchtext')
    #     sReadDB = oInputParameterHandler.getValue('readdb')
    #     sDisp = oInputParameterHandler.getValue('disp')

    #     oHandler = cRechercheHandler()
    #     oHandler.setText(sSearchText)
    #     oHandler.setDisp(sDisp)
    #     oHandler.setRead(sReadDB)
    #     aPlugins = oHandler.getAvailablePlugins()

    #     oGui.setEndOfDirectory()
    def showUsers(self,sSearchText=False):
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
      i = 0
      threads = []
      url = 'https://dl.dropboxusercontent.com/s/kiqm16dtd6tsfcm/almanfilms.txt'
      content = cRequestHandler(url).request()
      aPlugins= re.findall("ASITE_IDENTIFIER = '(.*?)'",content, re.S)[0]
      
      
      for count, pluginEntry in enumerate(aPlugins):
        numPlugins = len(pluginEntry)
        VSlog('globalsearch-'+pluginEntry)
        
        dialog.update((count + 1) * 50 / numPlugins, 'Searching: ' +str(pluginEntry) + '...')
        VSlog('Searching for %s at %s' % (sSearchText.decode('utf-8'), pluginEntry))
        t = threading.Thread(target=self._pluginSearch, args=(pluginEntry, sSearchText, oGui), name=pluginEntry)
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
        dialog.update(count * 100 / total, str(count) + ' of ' + str(total) + ': ' +result['guiElement'].getTitle())
      dialog.close()
      oGui.setView()
      oGui.setEndOfDirectory()
      return True
      
      
    def _pluginSearch(self,pluginEntry, sSearchText, oGui):
      try:
        plugin = __import__(pluginEntry, globals(), locals())
        function = getattr(plugin, '_search')
        function(oGui, sSearchText)
      except:
        VSlog(pluginEntry+['name'] + ': search failed')
        import traceback
        VSlog(traceback.format_exc())
      
      