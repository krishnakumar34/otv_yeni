#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
from resources.lib.gui.contextElement import cContextElement
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.cconfig import ccConfig
from resources.lib.util import QuotePlus

from resources.lib.db import cDb
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.parser import  cParser
from resources.lib import util
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.comaddon import listitem, addon, dialog, isKrypton, window, xbmc
import sys
import xbmcplugin
import urllib
import unicodedata, re
from resources.lib.config import cConfig
from os import path
try:
    from urlparse import parse_qsl, urlsplit
    from urllib import unquote_plus, urlencode
except ImportError:
    from urllib.parse import parse_qsl, urlsplit, unquote_plus, urlencode
from resources.lib.util import urlEncode, Unquote
from resources.lib.util import UnquotePlus, Unquote
PY3 = False
try:
    import ssl
    import socket
    timeout = 30
    socket.setdefaulttimeout(timeout)
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
except ImportError:
    pass
try:
    import json
    import math
    import httplib
except:
    pass
try:
    import http.cookiejar as cookielib
    from urllib.parse import urlencode as Urlencode
    from urllib.parse import unquote_plus as Unquote_plus
    from urllib.parse import unquote as Unquote
    from urllib.parse import quote 
    from urllib.parse import urlparse 
    from urllib.parse import urljoin 
    from urllib.parse import parse_qsl 
    from urllib.parse import parse_qs 
    from html.parser import HTMLParser
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.request import HTTPCookieProcessor
    from urllib.request import build_opener
    from urllib.request import HTTPBasicAuthHandler
    from urllib.request import HTTPHandler
    from urllib.request import install_opener
    PY3 = True; unicode = str; unichr = chr; long = int
except:
    import cookielib
    from HTMLParser import HTMLParser
    from urllib import urlencode as Urlencode
    from urllib import unquote_plus as Unquote_plus
    from urllib import unquote as Unquote
    from urllib import quote 
    from urlparse import urlparse 
    from urlparse import urljoin 
    from urlparse import parse_qsl 
    from urlparse import parse_qs 
    from urllib2 import Request    
    from urllib2 import urlopen
    from urllib2 import HTTPCookieProcessor
    from urllib2 import build_opener
    from urllib2 import HTTPBasicAuthHandler
    from urllib2 import HTTPHandler
    from urllib2 import install_opener  
    





class cGui():

    SITE_NAME = 'cGui'
    CONTENT = 'files'
    searchResults = []
    #modif 22/06
    listing = []
    ADDON = addon()

    if isKrypton():
        CONTENT = 'addons'
    def __init__(self):
        try:
            self.pluginHandle = int(sys.argv[1])
        except:
            self.pluginHandle = 0
        try:
            self.pluginPath = sys.argv[0]
        except:
            self.pluginPath = ''
        self.isMetaOn = ccConfig().getSetting('TMDBMETA') == 'true'
        if ccConfig().getSetting('metaOverwrite') == 'true':
            self.metaMode = 'replace'
        else:
            self.metaMode = 'add'
        # for globalSearch or alterSearch
        self.globalSearch = False
        self._collectMode = False
        self._isViewSet = False
        self.searchResults = []
      
 

    def addMovie(self, sId, sFunction, sLabel, sIcon, sThumbnail, sDesc, oOutputParameterHandler = ''):
        cGui.CONTENT = "movies"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setPoster(sThumbnail)
        oGuiElement.setMeta(1)
        oGuiElement.setDescription(sDesc)
        #oGuiElement.setMovieFanart()
        oGuiElement.setCat(1)

        if oOutputParameterHandler.getValue('sMovieTitle'):
            sTitle = oOutputParameterHandler.getValue('sMovieTitle')
            oGuiElement.setFileName(sTitle)

        self.adFolder(oGuiElement, oOutputParameterHandler)


    def addTV(self, sId, sFunction, sLabel, sIcon, sThumbnail, sDesc, oOutputParameterHandler = ''):
        cGui.CONTENT = "tvshows"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setPoster(sThumbnail)
        oGuiElement.setMeta(2)
        oGuiElement.setDescription(sDesc)
        #oGuiElement.setTvFanart()
        oGuiElement.setCat(2)

        # if oOutputParameterHandler.getValue('season'):
            # sSeason = oOutputParameterHandler.getValue('season')
            # oGuiElement.addItemValues('Season', sSeason)

        # if oOutputParameterHandler.getValue('episode'):
            # sSeason = oOutputParameterHandler.getValue('episode')
            # oGuiElement.addItemValues('Episode', sSeason)

        if oOutputParameterHandler.getValue('sMovieTitle'):
            sTitle = oOutputParameterHandler.getValue('sMovieTitle')
            oGuiElement.setFileName(sTitle)


        self.adFolder(oGuiElement, oOutputParameterHandler)

    def addMisc(self, sId, sFunction, sLabel, sIcon, sThumbnail, sDesc, oOutputParameterHandler = ''):
        cGui.CONTENT = "movies"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(sThumbnail)
        #oGuiElement.setPoster(sThumbnail)
        oGuiElement.setMeta(0)
        #oGuiElement.setDirFanart(sIcon)
        oGuiElement.setCat(5)

        oGuiElement.setDescription(sDesc)

        if oOutputParameterHandler.getValue('sMovieTitle'):
            sTitle = oOutputParameterHandler.getValue('sMovieTitle')
            oGuiElement.setFileName(sTitle)

        self.createContexMenuWatch(oGuiElement, oOutputParameterHandler)
        #self.createContexMenuinfo(oGuiElement, oOutputParameterHandler)
        self.createContexMenuFav(oGuiElement, oOutputParameterHandler)

        self.adFolder(oGuiElement, oOutputParameterHandler)

    #non utiliser le 18/04
    #def addFav(self, sId, sFunction, sLabel, sIcon, sThumbnail, fanart, oOutputParameterHandler = ''):
        #cGui.CONTENT = "files"
        #oGuiElement = cGuiElement()
        #oGuiElement.setSiteName(sId)
        #oGuiElement.setFunction(sFunction)
        #oGuiElement.setTitle(sLabel)
        #oGuiElement.setIcon(sIcon)
        #oGuiElement.setMeta(0)
        #oGuiElement.setThumbnail(sThumbnail)
        #oGuiElement.setFanart(fanart)

        #self.createContexMenuDelFav(oGuiElement, oOutputParameterHandler)

        #self.adFolder(oGuiElement, oOutputParameterHandler)


    def addLink(self, sId, sFunction, sLabel, sThumbnail, sDesc, oOutputParameterHandler = ''):
        cGui.CONTENT = "files"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        #oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setPoster(sThumbnail)
        oGuiElement.setDescription(sDesc)
        oGuiElement.setMeta(0)
        #oGuiElement.setDirFanart('')

        oInputParameterHandler = cInputParameterHandler()
        sCat = oInputParameterHandler.getValue('sCat')
        if sCat:
            oGuiElement.setCat(sCat)


        self.adFolder(oGuiElement, oOutputParameterHandler)


    def addDir(self, sId, sFunction, sLabel, sIcon, oOutputParameterHandler = ''):
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(oGuiElement.getIcon())
        oGuiElement.setMeta(0)
        #oGuiElement.setDirFanart(sIcon)

        oOutputParameterHandler.addParameter('sFav', sFunction)

        #context parametre
        if isKrypton():
            self.createContexMenuSettings(oGuiElement, oOutputParameterHandler)

        self.adFolder(oGuiElement, oOutputParameterHandler)

    def addNext(self, sId, sFunction, sLabel, oOutputParameterHandler):
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon('next.png')
        oGuiElement.setThumbnail(oGuiElement.getIcon())
        oGuiElement.setMeta(0)
        #oGuiElement.setDirFanart('next.png')
        oGuiElement.setCat(5)

        self.createContexMenuPageSelect(oGuiElement, oOutputParameterHandler)
        self.createContexMenuFav(oGuiElement, oOutputParameterHandler)

        self.adFolder(oGuiElement, oOutputParameterHandler)

    #utiliser oGui.addText(SITE_IDENTIFIER)
    def addNone(self, sId):
        return self.addText(sId)


    def addText(self, sId, sLabel = '', sIcon = 'none.png'):
        
        # Pas de texte lors des recherches globales
        if window(10101).getProperty('search') == 'true':
            return

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction('DoNothing')
        if not sLabel:
            sLabel = self.ADDON.VSlang(30204)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(oGuiElement.getIcon())
        oGuiElement.setMeta(0)

        oOutputParameterHandler = cOutputParameterHandler()
        self.adFolder(oGuiElement, oOutputParameterHandler)

    #non utiliser depuis le 22/04
    def addMovieDB(self, sId, sFunction, sLabel, sIcon, sThumbnail, sFanart, oOutputParameterHandler = ''):

        cGui.CONTENT = "movies"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setMeta(1)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sFanart)
        oGuiElement.setCat(7)

        if oOutputParameterHandler.getValue('sMovieTitle'):
            sTitle = oOutputParameterHandler.getValue('sMovieTitle')
            oGuiElement.setFileName(sTitle)

        self.adFolder(oGuiElement, oOutputParameterHandler)

    #non utiliser 22/04
    def addTVDB(self, sId, sFunction, sLabel, sIcon, sThumbnail, sFanart, oOutputParameterHandler = ''):

        cGui.CONTENT = "tvshows"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setMeta(2)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sFanart)
        oGuiElement.setCat(7)

        if oOutputParameterHandler.getValue('sMovieTitle'):
            sTitle = oOutputParameterHandler.getValue('sMovieTitle')
            oGuiElement.setFileName(sTitle)

        self.adFolder(oGuiElement, oOutputParameterHandler)

    #afficher les liens non playable
    def addFolder(self, oGuiElement, params='', bIsFolder=True, iTotal=0, isHoster=False):
        # add GuiElement to Gui, adds listitem to a list
        # abort xbmc list creation if user requests abort
        if xbmc.Monitor().abortRequested():
            self.setEndOfDirectory(False)
            raise RuntimeError('UserAborted')
        # store result in list if we searched global for other sources
        if self._collectMode:
            import copy
            self.searchResults.append({'guiElement': oGuiElement, 'params': copy.deepcopy(params), 'isFolder': bIsFolder})
            return
        if not oGuiElement._isMetaSet and self.isMetaOn and oGuiElement._mediaType and iTotal < 100:
            tmdbID = params.getValue('tmdbID')
            if tmdbID:
                oGuiElement.getMeta(oGuiElement._mediaType, tmdbID, mode=self.metaMode)
            else:
                oGuiElement.getMeta(oGuiElement._mediaType, mode=self.metaMode)
        sUrl = self._createItemUrl(oGuiElement, bIsFolder, params)
        listitem = self.createListItem(oGuiElement)
        if not bIsFolder and ccConfig().getSetting('hosterSelect') == 'List':
            bIsFolder = True
        if isHoster:
            bIsFolder = False
        listitem = self._createContextMenu(oGuiElement, listitem, bIsFolder, sUrl)
        if not bIsFolder:
            listitem.setProperty('IsPlayable', 'true')
#        xbmcplugin.addDirectoryItem(self.pluginHandle, sUrl, listitem, bIsFolder, iTotal)

#        oListItem = self.__createContextMenu(oGuiElement, oListItem)

        # sPluginHandle = cPluginHandler().getPluginHandle()
        # xbmcplugin.addDirectoryItem(sPluginHandle, sItemUrl, oListItem, isFolder=_isFolder)
        self.listing.append(( sUrl, listitem, bIsFolder, iTotal))
    
    

    def adFolder(self, oGuiElement, params='', bIsFolder=True, iTotal=0, isHoster=False):
        # add GuiElement to Gui, adds listitem to a list
        # abort xbmc list creation if user requests abort
        if xbmc.Monitor().abortRequested():
            self.setEndOfDirectory(False)
            raise RuntimeError('UserAborted')
          # store result in list if we searched global for other sources
        if self._collectMode:
            import copy
            self.searchResults.append({'guiElement': oGuiElement, 'params': copy.deepcopy(params), 'isFolder': bIsFolder})
            return
        if not oGuiElement._isMetaSet and self.isMetaOn and oGuiElement._mediaType:
            imdbID = params.getValue('imdbID')
            if imdbID:
                oGuiElement.getMeta(oGuiElement._mediaType, imdbID, mode=self.metaMode)
            else:
                oGuiElement.getMeta(oGuiElement._mediaType, mode=self.metaMode)
        sUrl = self._createItemUrl(oGuiElement, bIsFolder, params)
        listitem = self.createListItem(oGuiElement)
        if not bIsFolder and ccConfig().getSetting('hosterSelect') == 'List':
            bIsFolder = True
        if isHoster:
            bIsFolder = False
        sPluginHandle = cPluginHandler().getPluginHandle()
        listitem = self._createContextMenu(oGuiElement, listitem, bIsFolder, sUrl)
        if not bIsFolder:
            listitem.setProperty('IsPlayable', 'true')
        
        
        oListItem = self.createListItem(oGuiElement)
        oListItem.setProperty("IsPlayable", "false")
        oListItem = self.__createContextMenu(oGuiElement, oListItem)
        sItemUrl = self.__createItemUrl(oGuiElement, params)
        sPluginHandle = cPluginHandler().getPluginHandle()
        #modif 22/06
        #xbmcplugin.addDirectoryItem(sPluginHandle, sItemUrl, oListItem, isFolder=_isFolder)
        self.listing.append((sUrl, oListItem, bIsFolder))

    def setView(self, content='movies'):
        '''
        set the listing to a certain content, makes special views available
        sets view to the viewID which is selected in xStream settings

        see http://mirrors.xbmc.org/docs/python-docs/stable/xbmcplugin.html#-setContent
        (seasons is also supported but not listed)
        '''
        content = content.lower()
        supportedViews = ['files', 'songs', 'artists', 'albums', 'movies', 'tvshows', 'seasons', 'episodes', 'musicvideos']

        if content in supportedViews:
            self._isViewSet = True
            xbmcplugin.setContent(self.pluginHandle, content)
        if ccConfig().getSetting('auto-view')=='true' and content:
            viewId = ccConfig().getSetting(content+'-view')
            if viewId:
                xbmc.executebuiltin("Container.SetViewMode(%s)" % viewId)

    def createListItem(self, oGuiElement):

        oListItem = listitem(oGuiElement.getTitle())
        oListItem.setInfo(oGuiElement.getType(), oGuiElement.getItemValues())
        #oListItem.setThumbnailImage(oGuiElement.getThumbnail())
        #oListItem.setIconImage(oGuiElement.getIcon())

        #krypton et sont comportement
        oListItem.setArt({'poster': oGuiElement.getPoster(), 'thumb': oGuiElement.getThumbnail(), 'icon': oGuiElement.getIcon(), 'fanart': oGuiElement.getFanart() })

        aProperties = oGuiElement.getItemProperties()
        for sPropertyKey in aProperties.keys():
            oListItem.setProperty(sPropertyKey, aProperties[sPropertyKey])

        return oListItem
    def addNextPage(self, site, function, oParams='', totalPages = 0):
        '''
        inserts a standard "next page" button into a listing 
        '''
        guiElement = cGuiElement('[COLOR teal]Next >>>[/COLOR]',site,function)
        self.adFolder(guiElement, oParams)

    #affiche les liens playable
    def addHost(self, oGuiElement, oOutputParameterHandler=''):

        if isKrypton():
            cGui.CONTENT = 'movies'

        if oOutputParameterHandler.getValue('siteUrl'):
            sSiteUrl = oOutputParameterHandler.getValue('siteUrl')
            oGuiElement.setSiteUrl(sSiteUrl)

        oListItem = self.createListItem(oGuiElement)
        #oListItem.setProperty("IsPlayable", "true")
        #oListItem.setProperty("Video", "true")

        #oListItem.addStreamInfo('video', {})

        sItemUrl = self.__createItemUrl(oGuiElement, oOutputParameterHandler)

        oListItem = self.__createContextMenu(oGuiElement, oListItem)

        sPluginHandle = cPluginHandler().getPluginHandle()

        #modif 13/09
        #xbmcplugin.addDirectoryItem(sPluginHandle, sItemUrl, oListItem, isFolder=False)
        self.listing.append((sItemUrl, oListItem, False))
    # marque page
    def createContexMenuBookmark(self, oGuiElement, oOutputParameterHandler=''):
        oOutputParameterHandler.addParameter('sCleanTitle', oGuiElement.getCleanTitle())
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oOutputParameterHandler.addParameter('sFav', oGuiElement.getFunction())
        oOutputParameterHandler.addParameter('sCat', oGuiElement.getCat())

        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cFav', 'cFav', 'setBookmark', self.ADDON.VSlang(30210))
    def createContexMenuinfo(self, oGuiElement, oOutputParameterHandler=''):
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sTitle', oGuiElement.getTitle())
        oOutputParameterHandler.addParameter('sFileName', oGuiElement.getFileName())
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oOutputParameterHandler.addParameter('sMeta', oGuiElement.getMeta())
        oOutputParameterHandler.addParameter('sYear', oGuiElement.getYear())

        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cGui', oGuiElement.getSiteName(), 'viewInfo', self.ADDON.VSlang(30208))

    #Marquer vu/Non vu
    def createContexMenuWatch(self, oGuiElement, oOutputParameterHandler= ''):
        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cGui', oGuiElement.getSiteName(), 'setWatched', self.ADDON.VSlang(30206))

    def _createContextMenu(self, oGuiElement, listitem, bIsFolder, sUrl):
        contextmenus = []
        if len(oGuiElement.getContextItems()) > 0:
            for contextitem in oGuiElement.getContextItems():
                params = contextitem.getOutputParameterHandler()
                sParams = params.getParameterAsUri()
                sTest = "%s?site=%s&function=%s&%s" % (self.pluginPath, contextitem.getFile(), contextitem.getFunction(), sParams)
                contextmenus += [(contextitem.getTitle(), "RunPlugin(%s)" % (sTest,),)]
        itemValues = oGuiElement.getItemValues()
        contextitem = cContextElement()

        if oGuiElement._mediaType == 'movie' or oGuiElement._mediaType == 'tvshow':
            contextitem.setTitle("Erweiterte Info (TMDB)")
            searchParams = {'searchTitle': oGuiElement.getTitle(), 'sMeta': oGuiElement._mediaType, 'sYear': oGuiElement._sYear}
            contextmenus += [(contextitem.getTitle(), "RunPlugin(%s?function=viewInfo&%s)" % (self.pluginPath, urlencode(searchParams),),)]
        if oGuiElement._mediaType == 'season' or oGuiElement._mediaType == 'episode':
            contextitem.setTitle("Info")
            contextmenus += [(contextitem.getTitle(), "Action(Info)",)]
        # search for alternative source
        contextitem.setTitle("Weitere Quellen")
        searchParams = {'searchTitle': oGuiElement.getTitle()}
        if 'imdb_id' in itemValues:
            searchParams['searchImdbID'] = itemValues['imdb_id']
        contextmenus += [(contextitem.getTitle(), "Container.Update(%s?function=searchAlter&%s)" % (self.pluginPath, urlencode(searchParams),),)]
        if 'imdb_id' in itemValues and 'title' in itemValues:
            metaParams = {}
            if itemValues['title']:
                metaParams['title'] = oGuiElement.getTitle()
            if 'mediaType' in itemValues and itemValues['mediaType']:
                metaParams['mediaType'] = itemValues['mediaType']
            elif 'TVShowTitle' in itemValues and itemValues['TVShowTitle']:
                metaParams['mediaType'] = 'tvshow'
            else:
                metaParams['mediaType'] = 'movie'
            if 'season' in itemValues and itemValues['season'] and int(itemValues['season']) > 0:
                metaParams['season'] = itemValues['season']
                metaParams['mediaType'] = 'season'
            if 'episode' in itemValues and itemValues['episode'] and int(itemValues['episode']) > 0 and 'season' in itemValues and itemValues['season'] and int(itemValues['season']):
                metaParams['episode'] = itemValues['episode']
                metaParams['mediaType'] = 'episode'

        # context options for movies or episodes
        if not bIsFolder:
            contextitem.setTitle("add to Playlist")
            contextmenus += [(contextitem.getTitle(), "RunPlugin(%s&playMode=enqueue)" % (sUrl,),)]
            contextitem.setTitle("download")
            contextmenus += [(contextitem.getTitle(), "RunPlugin(%s&playMode=download)" % (sUrl,),)]
            if ccConfig().getSetting('jd_enabled') == 'true':
                contextitem.setTitle("send to JDownloader")
                contextmenus += [(contextitem.getTitle(), "RunPlugin(%s&playMode=jd)" % (sUrl,),)]
            if ccConfig().getSetting('jd2_enabled') == 'true':
                contextitem.setTitle("send to JDownloader2")
                contextmenus += [(contextitem.getTitle(), "RunPlugin(%s&playMode=jd2)" % (sUrl,),)]
            if ccConfig().getSetting('pyload_enabled') == 'true':
                contextitem.setTitle("send to PyLoad")
                contextmenus += [(contextitem.getTitle(), "RunPlugin(%s&playMode=pyload)" % (sUrl,),)]
            if ccConfig().getSetting('hosterSelect') == 'Auto':
                contextitem.setTitle("select hoster")
                contextmenus += [(contextitem.getTitle(), "RunPlugin(%s&playMode=play&manual=1)" % (sUrl,),)]
        listitem.addContextMenuItems(contextmenus)
        # listitem.addContextMenuItems(contextmenus, True)
        return listitem
        


    def createContexMenuPageSelect(self, oGuiElement, oOutputParameterHandler):
        #sSiteUrl = oGuiElement.getSiteName()

        oContext = cContextElement()

        oContext.setFile('cGui')
        oContext.setSiteName('cGui')

        oContext.setFunction('selectpage')
        oContext.setTitle('[COLOR azure]Selectionner page[/COLOR]')
        oOutputParameterHandler.addParameter('OldFunction', oGuiElement.getFunction())
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oContext.setOutputParameterHandler(oOutputParameterHandler)
        oGuiElement.addContextItem(oContext)

        oContext = cContextElement()

        oContext.setFile('cGui')
        oContext.setSiteName('cGui')

        oContext.setFunction('viewback')
        oContext.setTitle('[COLOR azure]Retour Site[/COLOR]')
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oContext.setOutputParameterHandler(oOutputParameterHandler)
        oGuiElement.addContextItem(oContext)


    #marque page
    def createContexMenuFav(self, oGuiElement, oOutputParameterHandler= ''):
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oOutputParameterHandler.addParameter('sFav', oGuiElement.getFunction())
        oOutputParameterHandler.addParameter('sCat', oGuiElement.getCat())

        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cFav', 'cFav', 'setFavorite', self.ADDON.VSlang(30207))

    def createContexMenuTrakt(self, oGuiElement, oOutputParameterHandler= ''):

        oOutputParameterHandler.addParameter('sImdbId', oGuiElement.getImdbId())
        oOutputParameterHandler.addParameter('sTmdbId', oGuiElement.getTmdbId())
        oOutputParameterHandler.addParameter('sFileName', oGuiElement.getFileName())

        sType = cGui.CONTENT.replace('tvshows', 'shows')
        oOutputParameterHandler.addParameter('sType', sType)
        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cTrakt', 'cTrakt', 'getAction', self.ADDON.VSlang(30214))

    def createContexMenuTMDB(self, oGuiElement, oOutputParameterHandler= ''):

        oOutputParameterHandler.addParameter('sImdbId', oGuiElement.getImdbId())
        oOutputParameterHandler.addParameter('sTmdbId', oGuiElement.getTmdbId())
        oOutputParameterHandler.addParameter('sFileName', oGuiElement.getFileName())

        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'themoviedb_org', 'themoviedb_org', 'getAction', 'TMDB')

    def createContexMenuDownload(self, oGuiElement, oOutputParameterHandler= '', status = '0'):

        if status == '0':
            self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cDownload', 'cDownload', 'StartDownloadOneFile', self.ADDON.VSlang(30215))

        if status == '0' or status == '2':
            self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cDownload', 'cDownload', 'delDownload', self.ADDON.VSlang(30216))
            self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cDownload', 'cDownload', 'DelFile', self.ADDON.VSlang(30217))

        if status == '1':
            self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cDownload', 'cDownload', 'StopDownloadList', self.ADDON.VSlang(30218))

        if status == '2':
            self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cDownload', 'cDownload', 'ReadDownload', self.ADDON.VSlang(30219))
            self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cDownload', 'cDownload', 'ResetDownload', self.ADDON.VSlang(30220))


    #Information
    def createContexMenuinfo(self, oGuiElement, oOutputParameterHandler= ''):

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sTitle', oGuiElement.getTitle())
        oOutputParameterHandler.addParameter('sFileName', oGuiElement.getFileName())
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oOutputParameterHandler.addParameter('sMeta', oGuiElement.getMeta())

        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cGui', oGuiElement.getSiteName(), 'viewinfo', self.ADDON.VSlang(30208))

    def createContexMenuba(self, oGuiElement, oOutputParameterHandler= ''):

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sTitle', oGuiElement.getTitle())
        oOutputParameterHandler.addParameter('sFileName', oGuiElement.getFileName())

        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cGui', oGuiElement.getSiteName(), 'viewBA', self.ADDON.VSlang(30212))


    def createContexMenuSimil(self, oGuiElement, oOutputParameterHandler= ''):

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sFileName', oGuiElement.getFileName())
        oOutputParameterHandler.addParameter('sTitle', oGuiElement.getTitle())
        oOutputParameterHandler.addParameter('sCat', oGuiElement.getCat())

        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cGui', oGuiElement.getSiteName(), 'viewsimil', self.ADDON.VSlang(30213))

    def CreateSimpleMenu(self,oGuiElement, oOutputParameterHandler, file, name, function, title):
        oContext = cContextElement()
        oContext.setFile(file)
        oContext.setSiteName(name)
        oContext.setFunction(function)
        oContext.setTitle(title)

        oContext.setOutputParameterHandler(oOutputParameterHandler)

        oGuiElement.addContextItem(oContext)

    def createContexMenuDelFav(self, oGuiElement, oOutputParameterHandler= ''):
        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'cFav', 'cFav', 'delFavouritesMenu', self.ADDON.VSlang(30209))

    def createContexMenuSettings(self, oGuiElement, oOutputParameterHandler= ''):
        self.CreateSimpleMenu(oGuiElement, oOutputParameterHandler, 'globalParametre', 'globalParametre', 'opensetting', self.ADDON.VSlang(30023))


    def __createContextMenu(self, oGuiElement, oListItem):
        sPluginPath = cPluginHandler().getPluginPath()
        aContextMenus = []

        #Menus classiques reglés a la base
        if (len(oGuiElement.getContextItems()) > 0):
            for oContextItem in oGuiElement.getContextItems():
                oOutputParameterHandler = oContextItem.getOutputParameterHandler()
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)
                aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.RunPlugin(%s)" % (sTest,),)]

            oListItem.addContextMenuItems(aContextMenus, True)

        return oListItem

    def __ContextMenu(self, oGuiElement, oListItem):
        sPluginPath = cPluginHandler().getPluginPath()
        aContextMenus = []

        if (len(oGuiElement.getContextItems()) > 0):
            for oContextItem in oGuiElement.getContextItems():
                oOutputParameterHandler = oContextItem.getOutputParameterHandler()
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)
                aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.RunPlugin(%s)" % (sTest,),)]

            oListItem.addContextMenuItems(aContextMenus)
            #oListItem.addContextMenuItems(aContextMenus, True)

        return oListItem

    def __ContextMenuPlay(self, oGuiElement, oListItem):
        sPluginPath = cPluginHandler().getPluginPath()
        aContextMenus = []

        if (len(oGuiElement.getContextItems()) > 0):
            for oContextItem in oGuiElement.getContextItems():
                oOutputParameterHandler = oContextItem.getOutputParameterHandler()
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)
                aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.RunPlugin(%s)" % (sTest,),)]

            oListItem.addContextMenuItems(aContextMenus)
            #oListItem.addContextMenuItems(aContextMenus, True)

        return oListItem

    def setEndOfDirectory(self, ForceViewMode = False):

        iHandler = cPluginHandler().getPluginHandle()
        #modif 22/06
        if not self.listing:
            self.addText('cGui')

        xbmcplugin.addDirectoryItems(iHandler, self.listing, len(self.listing))

        xbmcplugin.setPluginCategory(iHandler, "")
        xbmcplugin.setContent(iHandler, cGui.CONTENT)
        xbmcplugin.addSortMethod(iHandler, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(iHandler, succeeded=True, cacheToDisc=True)
        #reglage vue
        #50 = liste / 51 grande liste / 500 icone / 501 gallerie / 508 fanart /
        if (ForceViewMode):
            xbmc.executebuiltin('Container.SetViewMode(' + str(ForceViewMode) + ')')
        else:
            if (self.ADDON.getSetting('active-view') == 'true'):
                if cGui.CONTENT == "movies":
                    #xbmc.executebuiltin('Container.SetViewMode(507)')
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('movie-view'))
                elif cGui.CONTENT == "tvshows":
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('serie-view'))
                elif cGui.CONTENT == "files":
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('default-view'))

        #bug affichage Kodi 18
        del self.listing [:]

    def updateDirectory(self):
        xbmc.executebuiltin("Container.Refresh")

    def viewback(self):
        sPluginPath = cPluginHandler().getPluginPath()
        oInputParameterHandler = cInputParameterHandler()
        sParams = oInputParameterHandler.getAllParameter()

        sId = oInputParameterHandler.getValue('sId')

        sTest = '%s?site=%s' % (sPluginPath, sId)
        xbmc.executebuiltin('XBMC.Container.Update(%s, replace)' % sTest )

    def viewsimil(self):
        sPluginPath = cPluginHandler().getPluginPath()
        oInputParameterHandler = cInputParameterHandler()
        sFileName = oInputParameterHandler.getValue('sFileName')
        sTitle = oInputParameterHandler.getValue('sTitle')
        sCat = oInputParameterHandler.getValue('sCat')

        oOutputParameterHandler = cOutputParameterHandler()
        #oOutputParameterHandler.addParameter('searchtext', sFileName)
        oOutputParameterHandler.addParameter('searchtext', util.cUtil().CleanName(sTitle))
        oOutputParameterHandler.addParameter('sCat', sCat)

        oOutputParameterHandler.addParameter('readdb', 'False')

        sParams = oOutputParameterHandler.getParameterAsUri()
        sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, 'globalSearch', 'globalSearch', sParams)
        xbmc.executebuiltin('XBMC.Container.Update(%s)' % sTest )
        return False


    def selectpage(self):
        sPluginPath = cPluginHandler().getPluginPath()
        oInputParameterHandler = cInputParameterHandler()
        #sParams = oInputParameterHandler.getAllParameter()

        sId = oInputParameterHandler.getValue('sId')
        sFunction = oInputParameterHandler.getValue('OldFunction')
        siteUrl = oInputParameterHandler.getValue('siteUrl')

        oParser = cParser()
        oldNum = oParser.getNumberFromString(siteUrl)
        newNum = 0
        if oldNum:
            newNum = self.showNumBoard()
        if newNum:
            try:
                siteUrl = siteUrl.replace(oldNum, newNum)

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, sId, sFunction, sParams)
                xbmc.executebuiltin('XBMC.Container.Update(%s)' % sTest )
            except:
                return False

        return False


    def selectpage2(self):
        sPluginPath = cPluginHandler().getPluginPath()
        oInputParameterHandler = cInputParameterHandler()

        sParams = oInputParameterHandler.getAllParameter()


        sId = oInputParameterHandler.getValue('sId')
        siteUrl = oInputParameterHandler.getValue('siteUrl')
        sFunction = oInputParameterHandler.getValue('OldFunction')

        selpage = self.showNumBoard()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', siteUrl)
        oOutputParameterHandler.addParameter('Selpage', selpage)

        sParams = oOutputParameterHandler.getParameterAsUri()
        sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, sId, sFunction, sParams)
        xbmc.executebuiltin('XBMC.Container.Update(%s, replace)' % sTest )

    def setWatched(self):

        oInputParameterHandler = cInputParameterHandler()

        aParams = oInputParameterHandler.getAllParameter()
        # import xbmc
        # xbmc.log(str(aParams))

        sSite = oInputParameterHandler.getValue('siteUrl')
        sTitle = xbmc.getInfoLabel('ListItem.label')

        meta = {}
        meta['title'] = sTitle
        meta['site'] = sSite

        row = cDb().get_watched(meta)
        if row:
            cDb().del_watched(meta)
            cDb().del_resume(meta)
        else:
            cDb().insert_watched(meta)

        xbmc.executebuiltin( 'Container.Refresh' )


    def viewBA(self):
        oInputParameterHandler = cInputParameterHandler()
        sFileName = oInputParameterHandler.getValue('sFileName')

        from resources.lib.ba import cShowBA
        cBA = cShowBA()
        cBA.SetSearch(sFileName)
        cBA.SearchBA()


    def viewinfo(self):

        from resources.lib.config import WindowsBoxes

        oGuiElement = cGuiElement()
        oInputParameterHandler = cInputParameterHandler()

        sTitle = oInputParameterHandler.getValue('sTitle')
        sId = oInputParameterHandler.getValue('sId')
        sFileName = oInputParameterHandler.getValue('sFileName')
        sYear = oInputParameterHandler.getValue('sYear')
        sMeta = oInputParameterHandler.getValue('sMeta')

        #sMeta = 1 >> film sMeta = 2 >> serie
        sCleanTitle = util.cUtil().CleanName(sFileName)

        #on vire saison et episode
        if (True):#sMeta == 2:
            sCleanTitle = re.sub('(?i).pisode [0-9]+', '', sCleanTitle)
            sCleanTitle = re.sub('(?i)saison [0-9]+', '', sCleanTitle)
            sCleanTitle = re.sub('(?i)S[0-9]+E[0-9]+', '', sCleanTitle)
            sCleanTitle = re.sub('(?i)[S|E][0-9]+', '', sCleanTitle)

        ui = WindowsBoxes(sTitle, sCleanTitle, sMeta, sYear)

    def __createItemUrl(self, oGuiElement, oOutputParameterHandler=''):
        if (oOutputParameterHandler == ''):
            oOutputParameterHandler = cOutputParameterHandler()

        sParams = oOutputParameterHandler.getParameterAsUri()
        # cree une id unique
        # if oGuiElement.getSiteUrl():
            # print(str(hash(oGuiElement.getSiteUrl())))

        sPluginPath = cPluginHandler().getPluginPath()

        if (len(oGuiElement.getFunction()) == 0):
            sItemUrl = '%s?site=%s&title=%s&%s' % (sPluginPath, oGuiElement.getSiteName(), QuotePlus(oGuiElement.getCleanTitle()), sParams)
        else:
            sItemUrl = '%s?site=%s&function=%s&title=%s&%s' % (sPluginPath, oGuiElement.getSiteName(), oGuiElement.getFunction(), QuotePlus(oGuiElement.getCleanTitle()), sParams)

        return sItemUrl

    def setEndOfDirectory(self, ForceViewMode=False):
        iHandler = cPluginHandler().getPluginHandle()
        # modif 22/06
        if not self.listing:
            self.addText('cGui')

        xbmcplugin.addDirectoryItems(iHandler, self.listing, len(self.listing))
        xbmcplugin.setPluginCategory(iHandler, '')
        xbmcplugin.setContent(iHandler, cGui.CONTENT)
        xbmcplugin.addSortMethod(iHandler, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(iHandler, succeeded=True, cacheToDisc=True)
        # reglage vue
        # 50 = liste / 51 grande liste / 500 icone / 501 gallerie / 508 fanart /
        if ForceViewMode:
            xbmc.executebuiltin('Container.SetViewMode(' + str(ForceViewMode) + ')')
        else:
            if self.ADDON.getSetting('active-view') == 'true':
                if cGui.CONTENT == 'movies':
                    # xbmc.executebuiltin('Container.SetViewMode(507)')
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('movie-view'))
                elif cGui.CONTENT == 'tvshows':
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('serie-view'))
                elif cGui.CONTENT == 'files':
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('default-view'))

        # bug affichage Kodi 18
        del self.listing[:]

    def pinKeyBoard(self):
        keyboard = xbmc.Keyboard( '', "ADULT PIN->setting", False )
        keyboard.doModal()
        if ( keyboard.isConfirmed() ):
            pincode = keyboard.getText()
            if (len(pincode)) > 0:
                return pincode
        return False 
 
    def showKeyBoard(self, sDefaultText=''):
        keyboard = xbmc.Keyboard(sDefaultText)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            sSearchText = keyboard.getText()
            if (len(sSearchText)) > 0:
                return sSearchText

        return False


    def showNumBoard(self, sDefaultNum=''):
        dialogs = dialog()
        numboard = dialogs.numeric(0, 'Entrer la page', sDefaultNum)
        #numboard.doModal()
        if numboard != None:
                return numboard

        return False

    def _createItemUrl(self, oGuiElement, bIsFolder, params=''):
        if params == '':
            params = ParameterHandler()
        itemValues = oGuiElement.getItemValues()
        if 'tmdb_id' in itemValues and itemValues['tmdb_id']:
            params.setParam('tmdbID', itemValues['tmdb_id'])
        if 'TVShowTitle' in itemValues and itemValues['TVShowTitle']:
            params.setParam('TVShowTitle', itemValues['TVShowTitle'])
        if 'season' in itemValues and itemValues['season'] and int(itemValues['season']) > 0:
            params.setParam('season', itemValues['season'])
        if 'episode' in itemValues and itemValues['episode'] and float(itemValues['episode']) > 0:
            params.setParam('episode', itemValues['episode'])
        # TODO change this, it can cause bugs it influencec the params for the following listitems
        if not bIsFolder:
            params.setParam('MovieTitle', oGuiElement.getTitle())
            thumbnail = oGuiElement.getThumbnail()
            if thumbnail:
                params.setParam('thumb', thumbnail)
            if oGuiElement._mediaType:
                params.setParam('mediaType', oGuiElement._mediaType)
            elif 'TVShowTitle' in itemValues and itemValues['TVShowTitle']:
                params.setParam('mediaType', 'tvshow')
            if 'season' in itemValues and itemValues['season'] and int(itemValues['season']) > 0:
                params.setParam('mediaType', 'season')
            if 'episode' in itemValues and itemValues['episode'] and float(itemValues['episode']) > 0:
                params.setParam('mediaType', 'episode')
        sParams = params.getParameterAsUri()
        if len(oGuiElement.getFunction()) == 0:
            sUrl = "%s?site=%s&title=%s&%s" % (self.pluginPath, oGuiElement.getSiteName(),  QuotePlus(oGuiElement.getTitle()), sParams)
        else:
            sUrl = "%s?site=%s&function=%s&title=%s&%s" % (self.pluginPath, oGuiElement.getSiteName(), oGuiElement.getFunction(),  QuotePlus(oGuiElement.getTitle()), sParams)
            if not bIsFolder:
                sUrl += '&playMode=play'
        return sUrl

    def setEndOfDirectory(self, ForceViewMode=False):
        iHandler = cPluginHandler().getPluginHandle()
        # modif 22/06
        if not self.listing:
            self.addText('cGui')

        xbmcplugin.addDirectoryItems(iHandler, self.listing, len(self.listing))
        xbmcplugin.setPluginCategory(iHandler, '')
        xbmcplugin.setContent(iHandler, cGui.CONTENT)
        xbmcplugin.addSortMethod(iHandler, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(iHandler, succeeded=True, cacheToDisc=True)
        # reglage vue
        # 50 = liste / 51 grande liste / 500 icone / 501 gallerie / 508 fanart /
        if ForceViewMode:
            xbmc.executebuiltin('Container.SetViewMode(' + str(ForceViewMode) + ')')
        else:
            if self.ADDON.getSetting('active-view') == 'true':
                if cGui.CONTENT == 'movies':
                    # xbmc.executebuiltin('Container.SetViewMode(507)')
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('movie-view'))
                elif cGui.CONTENT == 'tvshows':
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('serie-view'))
                elif cGui.CONTENT == 'files':
                    xbmc.executebuiltin('Container.SetViewMode(%s)' % self.ADDON.getSetting('default-view'))

        # bug affichage Kodi 18
        del self.listing[:]

    def openSettings(self):
        return False

    def showNofication(self, sTitle, iSeconds=0):
        return False

    def showError(self, sTitle, sDescription, iSeconds=0):
        return False

    def showInfo(self, sTitle, sDescription, iSeconds=0):
        return False
