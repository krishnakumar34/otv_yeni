# -*- coding: UTF-8 -*-
import gettext
import locale
import os
import xbmc, xbmcaddon, xbmcplugin
import xbmcgui

try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)

USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('profile'))
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
resolveFilename = os.path.join(ADDON_DATA_DIR, 'resources')


SCOPE_LANGUAGE = 7
class Language:
	def __init__(self):
		gettext.install(addon, resolveFilename,  codeset="utf-8", names=None)
		gettext.bindtextdomain(addon, resolveFilename)
		gettext.textdomain(addon)
		self.activeLanguage = 0
		self.catalog = None
		self.lang = {}
		self.langlist = []
		# FIXME make list dynamically
		# name, iso-639 language, iso-3166 country. Please don't mix language&country!
		self.addLanguage("Arabic",	"ar", "AE", "ISO-8859-15")
		self.addLanguage("?????????",	"bg", "BG", "ISO-8859-15")
		self.addLanguage("Catala",	"ca", "AD", "ISO-8859-15")
		self.addLanguage("Cesky",	"cs", "CZ", "ISO-8859-15")
		self.addLanguage("Dansk",	"da", "DK", "ISO-8859-15")
		self.addLanguage("Deutsch",	"de", "DE", "ISO-8859-15")
		self.addLanguage("????????",	"el", "GR", "ISO-8859-7")
		self.addLanguage("English",	"en", "EN", "ISO-8859-15")
		self.addLanguage("Espanol",	"es", "ES", "ISO-8859-15")
		self.addLanguage("Eesti",	"et", "EE", "ISO-8859-15")
		self.addLanguage("?????",	"fa", "IR", "UTF-8")
		self.addLanguage("Suomi",	"fi", "FI", "ISO-8859-15")
		self.addLanguage("Francais",	"fr", "FR", "ISO-8859-15")
		self.addLanguage("Frysk",	"fy", "NL", "ISO-8859-15")
		self.addLanguage("Galician",	"gl", "ES", "ISO-8859-15")
		self.addLanguage("Hebrew",	"he", "IL", "ISO-8859-15")
		self.addLanguage("Hrvatski",	"hr", "HR", "ISO-8859-15")
		self.addLanguage("Magyar",	"hu", "HU", "ISO-8859-15")
		self.addLanguage("Indonesian",	"id", "ID", "ISO-8859-15")
		self.addLanguage("Islenska",	"is", "IS", "ISO-8859-15")
		self.addLanguage("Italiano",	"it", "IT", "ISO-8859-15")
		self.addLanguage("Kurdish",	"ku", "KU", "ISO-8859-15")
		self.addLanguage("Lietuviu",	"lt", "LT", "ISO-8859-15")
		self.addLanguage("Latviesu",	"lv", "LV", "ISO-8859-15")
		self.addLanguage("??????????",	"mk", "MK", "ISO-8859-5")
		self.addLanguage("Nederlands",	"nl", "NL", "ISO-8859-15")
		self.addLanguage("Norsk Bokmel","nb", "NO", "ISO-8859-15")
		self.addLanguage("Norsk Nynorsk", "nn", "NO", "ISO-8859-15")
		self.addLanguage("Polski",	"pl", "PL", "ISO-8859-15")
		self.addLanguage("Portugues",	"pt", "PT", "ISO-8859-15")
		self.addLanguage("Portugues do Brasil","pt", "BR", "ISO-8859-15")
		self.addLanguage("Romanian",	"ro", "RO", "ISO-8859-15")
		self.addLanguage("???????",	"ru", "RU", "ISO-8859-15")
		self.addLanguage("Slovensky",	"sk", "SK", "ISO-8859-15")
		self.addLanguage("Slovenscina",	"sl", "SI", "ISO-8859-15")
		self.addLanguage("Srpski",	"sr", "YU", "ISO-8859-15")
		self.addLanguage("Svenska",	"sv", "SE", "ISO-8859-15")
		self.addLanguage("???????",	"th", "TH", "ISO-8859-15")
		self.addLanguage("Turkce",	"tr", "TR", "ISO-8859-15")
		self.addLanguage("??????????",	"uk", "UA", "ISO-8859-15")
		self.addLanguage("Ti?ng Vi?t",	"vi", "VN", "UTF-8")
		self.addLanguage("SChinese",	"zh", "CN", "UTF-8")
		self.addLanguage("TChinese",	"zh", "HK", "UTF-8")

		self.callbacks = []

	def addLanguage(self, name, lang, country, encoding):
		try:
			self.lang[str(lang + "_" + country)] = ((name, lang, country, encoding))
			self.langlist.append(str(lang + "_" + country))
		except:
			print ("Language " + str(name) + " not found" )

	def activateLanguage(self, index):
		try:
			if index not in self.lang:
				print( "Selected language %s does not exist, fallback to en_EN!" % index )
				index = "en_EN"
			lang = self.lang[index]
			print( "Activating language " + lang[0])
			os.environ["LANGUAGE"] = lang[1] # set languange in order gettext to work properly on external plugins
			self.catalog = gettext.translation('enigma2', resolveFilename(SCOPE_LANGUAGE, ""), languages=[index])
			self.catalog.install(names=("ngettext", "pgettext"))
			self.activeLanguage = index
			for x in self.callbacks:
				x()
		except:
			print( "Error in activating language!" )
		# NOTE: we do not use LC_ALL, because LC_ALL will not set any of the categories, when one of the categories fails.
		# We'd rather try to set all available categories, and ignore the others
		for category in [locale.LC_CTYPE, locale.LC_COLLATE, locale.LC_TIME, locale.LC_MONETARY, locale.LC_MESSAGES, locale.LC_NUMERIC]:
			try:
				locale.setlocale(category, (self.getLanguage(), 'UTF-8'))
			except:
				pass
		# HACK: sometimes python 2.7 reverts to the LC_TIME environment value, so make sure it has the correct value
		os.environ["LC_TIME"] = self.getLanguage() + '.UTF-8'
		os.environ["GST_SUBTITLE_ENCODING"] = self.getGStreamerSubtitleEncoding()

	def activateLanguageIndex(self, index):
		if index < len(self.langlist):
			self.activateLanguage(self.langlist[index])

	def getLanguageList(self):
		return [ (x, self.lang[x]) for x in self.langlist ]

	def getActiveLanguage(self):
		return self.activeLanguage

	def getActiveCatalog(self):
		return self.catalog

	def getActiveLanguageIndex(self):
		idx = 0
		for x in self.langlist:
			if x == self.activeLanguage:
				return idx
			idx += 1
		return None

	def getLanguage(self):
		try:
			return str(self.lang[self.activeLanguage][1]) + "_" + str(self.lang[self.activeLanguage][2])
		except:
			return ''

	def getGStreamerSubtitleEncoding(self):
		try:
			return str(self.lang[self.activeLanguage][3])
		except:
			return 'ISO-8859-15'

	def addCallback(self, callback):
		self.callbacks.append(callback)

language = Language()