# -*- coding: utf-8 -*-
import re
import string
import unicodedata
from resources.lib.comaddon import addon, xbmc
from resources.lib.comaddon import addon, xbmc, isMatrix, VSlog
from resources.lib.db import cDb
from resources.lib.util import QuoteSafe
import random
from resources.lib.tools import logger, cParser, cUtil
from resources.lib.config import cConfig
from resources.lib.common import addon
from os import path
try:
    from urlparse import parse_qsl, urlsplit
    from urllib import unquote_plus, urlencode
except ImportError:
    from urllib.parse import parse_qsl, urlsplit, unquote_plus, urlencode
from resources.lib.util import urlEncode, Unquote
from resources.lib.util import UnquotePlus, Unquote

class cGuiElement:
    '''
    This class "abstracts" a xbmc listitem.

    Kwargs:
        sTitle    (str): title/label oft the GuiElement/listitem
        sSite     (str): siteidentifier of the siteplugin, which is called if the GuiElement is selected 
        sFunction (str): name of the function, which is called if the GuiElement is selected
    
        These arguments are mandatory. If not given on init, they have to be set by their setter-methods, before the GuiElement is added to the Gui. 
    '''
#    DB = cDb()
    DEFAULT_FOLDER_ICON = 'DefaultFolder.png'
   
    MEDIA_TYPES = ['movie','tvshow','season','episode']
   
    def __init__(self, sTitle = '', sSite = None, sFunction = None):
        self.__sRootArt = 'special://home/addons/plugin.video.OTV_MEDIA/resources/art/'

        self.__sType = 'video'
        self.__sMediaUrl = ''
        self.__sTitle = cUtil.cleanse_text(sTitle)
        self.__sTitleSecond = ''
        self.__sDescription = ''
        self.__sThumbnail = ''
        self.__sIcon = self.DEFAULT_FOLDER_ICON
        self.__aItemValues = {}
        self.__aProperties = {}
        self.__aContextElements = []
        self.__sMeta = 0
        self.__sPlaycount = 0        
        self.__sFanart = "special://home/addons/plugin.video.OTV_MEDIA/fanart.jpg"
        self.__sMediaUrl = ''
        self.__sSiteUrl = ''
        self.__sSiteName = sSite
        self.__sFunctionName = sFunction
        self._sLanguage = ''
        self._sSubLanguage = ''
        self.__TmdbId = ''
        self._sYear = ''
        self.__sPoster = ''
        self._sQuality = ''
        self._mediaType = ''
        self.__sMediaUrl = ''
        self.__sFileName = ''
        self._season = ''
        self._episode = ''
        self.__ImdbId = ''
        self.__aItemValues = {}
        self._imdbID = ''
        self._rating = ''
        self._isMetaSet = False
        self.__sCat = ''
        self.__sTitleWatched = ''
    def setType(self, sType):
        self.__sType = sType

    def getType(self):
        return self.__sType
    def getCleanTitle(self):
        self.__sTitle=self.__sTitle
        return self.__sTitle

    def setMediaUrl(self, sMediaUrl):
        self.__sMediaUrl = sMediaUrl
    def addItemValues(self, sItemKey, mItemValue):
        self.__aItemValues[sItemKey] = mItemValue

    def getMediaUrl(self):
        return self.__sMediaUrl
    def setImdbId(self, data):
        self.__ImdbId = data

    def getImdbId(self):
        return self.__ImdbId

    def setSiteName(self, sSiteName):
        self.__sSiteName = sSiteName
    def getTitleWatched(self):
        return self.__sTitleWatched

    def getSiteName(self):
        return self.__sSiteName
    def setMeta(self, sMeta):
        self.__sMeta = sMeta

    def getMeta(self):
        return self.__sMeta
    def setCat(self, sCat):
        self.__sCat = sCat
    def setFileName(self, sFileName):
        self.__sFileName = sFileName

    def getFileName(self):
        return self.__sFileName

    def getCat(self):
        return self.__sCat
    def setTmdbId(self, data):
        self.__TmdbId = data

    def getTmdbId(self):
        return self.__TmdbId
    def getFileName(self):
        return self.__sFileName

    def setFunction(self, sFunctionName):
        self.__sFunctionName = sFunctionName
    def setSiteUrl(self, sSiteUrl):
        self.__sSiteUrl = sSiteUrl

    def getSiteUrl(self):
        return self.__sSiteUrl
    def getFunction(self):
        return self.__sFunctionName
    def setMediaUrl(self, sMediaUrl):
        self.__sMediaUrl = sMediaUrl

    def getMediaUrl(self):
        return self.__sMediaUrl
    def getInfoLabel(self):
        meta = {
        'title': xbmc.getInfoLabel('ListItem.title'),
        'label': xbmc.getInfoLabel('ListItem.title'),
        'originaltitle': xbmc.getInfoLabel('ListItem.originaltitle'),
        'year': xbmc.getInfoLabel('ListItem.year'),
        'genre': xbmc.getInfoLabel('ListItem.genre'),
        'director': xbmc.getInfoLabel('ListItem.director'),
        'country': xbmc.getInfoLabel('ListItem.country'),
        'rating': xbmc.getInfoLabel('ListItem.rating'),
        'votes': xbmc.getInfoLabel('ListItem.votes'),
        'mpaa': xbmc.getInfoLabel('ListItem.mpaa'),
        'duration': xbmc.getInfoLabel('ListItem.duration'),
        'trailer': xbmc.getInfoLabel('ListItem.trailer'),
        'writer': xbmc.getInfoLabel('ListItem.writer'),
        'studio': xbmc.getInfoLabel('ListItem.studio'),
        'tagline': xbmc.getInfoLabel('ListItem.tagline'),
        'plotoutline': xbmc.getInfoLabel('ListItem.plotoutline'),
        'plot': xbmc.getInfoLabel('ListItem.plot'),
        'cover_url': xbmc.getInfoLabel('ListItem.Art(thumb)'),
        'backdrop_url': xbmc.getInfoLabel('ListItem.Art(fanart)'),
        'imdb_id': xbmc.getInfoLabel('ListItem.IMDBNumber'),
        'season': xbmc.getInfoLabel('ListItem.season'),
        'episode': xbmc.getInfoLabel('ListItem.episode')
        }

        if meta['title']:
            meta['title'] = self.getTitle()

        for key, value in meta.items():
            self.addItemValues(key, value)

        if meta['backdrop_url']:
            self.addItemProperties('fanart_image', meta['backdrop_url'])
            self.__sFanart = meta['backdrop_url']
        if meta['trailer']:
            meta['trailer'] = meta['trailer'].replace(u'\u200e', '').replace(u'\u200f', '')
            self.__sTrailerUrl = meta['trailer']
        if meta['cover_url']:
            self.__sThumbnail = meta['cover_url']
            self.__sPoster = meta['cover_url']

        return

    def setTitle(self, sTitle):
        self.__sTitle = cUtil.cleanse_text(sTitle)

    def getTitle(self):
        return self.__sTitle

    def setMediaType(self, mediaType):
        '''
        Set mediatype for GuiElement

        Args:
            mediaType(str): 'movie'/'tvshow'/'season'/'episode'
        '''
        mediaType = mediaType.lower()
        if mediaType in self.MEDIA_TYPES:
            self._mediaType = mediaType
        else:
            logger.info('Unknown MediaType given for %s' % self.getTitle())

    def setSeason(self, season):
        self._season = season
        self.__aItemValues['season'] = str(season)

    def setEpisode(self, episode):
        self._episode = episode
        self.__aItemValues['episode'] = str(episode)

    def setTVShowTitle(self, tvShowTitle):
        self.__aItemValues['TVShowTitle'] = str(tvShowTitle)

    def setYear(self, year):
        try:
            year = int(year)
        except:
            logger.info('Year given for %s seems not to be a valid number' % self.getTitle())
            return False
        if len(str(year)) != 4:
            logger.info('Year given for %s has %s digits, required 4 digits' % (self.getTitle(), len(str(year))))
            return False
        if year > 0:
            self._sYear = str(year)
            self.__aItemValues['year'] = year
            return True
        else:
            logger.info('Year given for %s must be greater than 0' % self.getTitle())
            return False

    def setTitleSecond(self, sTitleSecond):
        self.__sTitleSecond = cUtil.cleanse_text(str(sTitleSecond))

    def getTitleSecond(self):
        return self.__sTitleSecond

    def setDescription(self, sDescription):
        sDescription = cUtil.cleanse_text(sDescription)
        self.__sDescription = sDescription
        self.__aItemValues['plot'] = sDescription

    def getDescription(self):
        if 'plot' not in self.__aItemValues:
            return self.__sDescription
        else:
            return self.__aItemValues['plot']

    def setThumbnail(self, sThumbnail):
        self.__sThumbnail = sThumbnail

    def getThumbnail(self):
        return self.__sThumbnail

    def setIcon(self, sIcon):
        try:
            self.__sIcon = unicode(sIcon, 'utf-8')
        except:
            self.__sIcon = sIcon
        self.__sIcon = self.__sIcon.encode('utf-8')
        self.__sIcon = QuoteSafe(self.__sIcon)

    def getIcon(self):
        #if 'http' in self.__sIcon:
        #    return ununquote_plus(self.__sIcon)
        folder = "special://home/addons/plugin.video.OTV_MEDIA/resources/art"
        path = "/".join([folder, self.__sIcon]) 
        #return os.path.join(unicode(self.__sRootArt, 'utf-8'), self.__sIcon)
        return path

    
    def setFanart(self, sFanart):
        self.__sFanart = sFanart

    def getFanart(self):
        return self.__sFanart
    def setPoster(self, sPoster):
        self.__sPoster = sPoster

    def getPoster(self):
        return self.__sPoster

    def addItemValue(self, sItemKey, sItemValue):
        self.__aItemValues[sItemKey] = sItemValue
        
    def setItemValues(self, aValueList):
        self.__aItemValues = aValueList

    def getItemValues(self):
        self.__aItemValues['title'] = self.getTitle()
        if self.getDescription():
            self.__aItemValues['plot'] = self.getDescription()
        for sPropertyKey in self.__aProperties.keys():
            self.__aItemValues[sPropertyKey] = self.__aProperties[sPropertyKey]
        return self.__aItemValues
    
    def addItemProperties(self, sPropertyKey, sPropertyValue):
        self.__aProperties[sPropertyKey] = sPropertyValue
  
    def getItemProperties(self):
        for sItemValueKey in self.__aItemValues.keys():
            if not self.__aItemValues[sItemValueKey]=='':
                try:
                    self.__aProperties[sItemValueKey] = str(self.__aItemValues[sItemValueKey])
                except:
                    pass
        return self.__aProperties

    def addContextItem(self, oContextElement):
        self.__aContextElements.append(oContextElement)

    def getContextItems(self):
        return self.__aContextElements

    def setLanguage(self, sLang):
        self._sLanguage = str(sLang)

    def setSubLanguage(self, sLang):
        self._sSubLanguage = str(sLang)

