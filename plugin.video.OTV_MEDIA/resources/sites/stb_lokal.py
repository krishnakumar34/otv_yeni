# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TURKvod/plugin.py
from Components.config import ConfigSelection, ConfigInteger, getConfigListEntry, ConfigText, ConfigClock, ConfigSubsection, ConfigDirectory, ConfigPIN
from enigma import eBackgroundFileEraser, eAVSwitch, addFont, eConsoleAppContainer, eRCInput, eTimer, eDVBVolumecontrol, ePoint, eWidget, eSize, loadPNG, loadJPG, getDesktop, RT_HALIGN_LEFT, RT_HALIGN_CENTER, RT_VALIGN_CENTER, eListboxPythonMultiContent, gFont, ePicLoad, eServiceCenter, iServiceInformation, eServiceReference, iSeekableService, iPlayableService, iPlayableServicePtr, getPrevAsciiCode
from Screens.InfoBarGenerics import InfoBarSeek, InfoBarAudioSelection, InfoBarCueSheetSupport, InfoBarNotifications, InfoBarSubtitleSupport, InfoBarShowHide, NumberZap
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from Components.ActionMap import ActionMap, HelpableActionMap, NumberActionMap
from Components.ServiceEventTracker import ServiceEventTracker, InfoBarBase
from Components.Task import Task, Job, job_manager as JobManager, Condition
from os import listdir as os_listdir, path as os_path, system as os_system
from Screens.ChannelSelection import service_types_radio, service_types_tv
from Components.ServicePosition import ServicePositionGauge
from xml.etree.cElementTree import fromstring, ElementTree
from Tools.NumericalTextInput import NumericalTextInput
from Components.Sources.StaticText import StaticText
from Components.ConfigList import ConfigListScreen
from Components.VolumeControl import VolumeControl
from keymapparser import readKeymap, removeKeymap
from Components.Converter import ServicePosition
from Screens.InfoBarGenerics import InfoBarSeek
from Components.ScrollLabel import ScrollLabel
from Tools.BoundFunction import boundFunction
from Plugins.Plugin import PluginDescriptor
from Screens.Standby import TryQuitMainloop
from GlobalActions import globalActionMap
from ConfigParser import SafeConfigParser
from Components.FileList import FileList
from Screens.MessageBox import MessageBox
from Components.Language import language
from Components.Sources.List import List
from Components.MenuList import MenuList
from Components.AVSwitch import AVSwitch
from Tools.LoadPixmap import LoadPixmap
from xml.dom.minidom import parseString
from Components.Slider import Slider
from Screens.InputBox import InputBox
from Screens.TaskView import JobView
from Components.Pixmap import Pixmap
from Screens.Standby import Standby
from Components.Input import Input
from Components.Label import Label
from Screens.Screen import Screen
from urllib import FancyURLopener
from Tools import ASCIItranslit
from datetime import datetime
from xml.dom import minidom
from skin import parseColor
from urllib import quote
from time import time
from os import popen
import urllib as ul
import urlparse
import hashlib
import os.path
import urllib2
import urllib
import base64
import sys
import re
import imp
import os
try:
    import shutil
    import socket
    from twisted.internet._sslverify import ClientTLSOptions
    from twisted.web.client import getPage, error
    from twisted.internet import ssl, reactor
    from twisted.web import client
    from OpenSSL import SSL
    TWIST = 1
except:
    from twisted.web.client import downloadPage, getPage, error
    try:
        import shutil
        import socket
        import ssl
        import cookielib
    except:
        pass

    TWIST = 0

if TWIST == 1:

    class SNIFactory(ssl.ClientContextFactory):

        def __init__(self, hostname = None):
            self.hostname = hostname

        def getContext(self):
            ctx = self._contextFactory(self.method)
            if self.hostname:
                ClientTLSOptions(self.hostname, ctx)
            return ctx


DESKHEIGHT = getDesktop(0).size().height()

PLUGIN_PATH = '/usr/lib/enigma2/python/Plugins/Extensions/TURKvod'
try:
    from Tools.Directories import fileExists, pathExists, resolveFilename
    from Components.Network import iNetwork
    from Components.config import config, ConfigYesNo, NoSave
except Exception as ex:
    print ex
    print 'IMPORT ERROR'

try:
    from Plugins.Extensions.SubsSupport import SubsSupport
    SUBS = 1
except:
    SUBS = 0

try:
    addFont('%s/TURKvod-Regular.otf' % PLUGIN_PATH, 'RegularTURKvod', 100, 1)
    addFont('%s/turkvod.TTF' % PLUGIN_PATH, 'TURKvodRegular', 100, 1)
except Exception as ex:
    print ex

config.plugins.TURKVOD = ConfigSubsection()
config.plugins.TURKVOD.csifre = ConfigText(default='1234', fixed_size=False)
config.plugins.TURKVOD.use_rtmpw = ConfigText(default='', fixed_size=False)
config.plugins.TURKVOD.start_scale = ConfigSelection(default='3', choices=[('0', '4:3 LetterBox'),
 ('1', '4:3 PanScan'),
 ('2', '16:9'),
 ('3', '16:9 Always'),
 ('4', '16:10 LetterBox'),
 ('5', '16:10 PanScan'),
 ('6', '16:9 Letterbox')])
config.plugins.TURKVOD.end_scale = ConfigSelection(default='3', choices=[('0', '4:3 LetterBox'),
 ('1', '4:3 PanScan'),
 ('2', '16:9'),
 ('3', '16:9 Always'),
 ('4', '16:10 LetterBox'),
 ('5', '16:10 PanScan'),
 ('6', '16:9 Letterbox')])
config.plugins.TURKVOD.use_ts_percent = ConfigSelection(default='15', choices=[('15', '15'),
 ('20', '20'),
 ('30', '30'),
 ('50', '50'),
 ('70', '70'),
 ('90', '90')])
config.plugins.TURKVOD.images_tmp = ConfigText(default='1', fixed_size=False)
config.plugins.TURKVOD.images_tmp_path = ConfigText(default='/tmp', fixed_size=False)
config.plugins.TURKVOD.security_key = ConfigText(default='', fixed_size=False)
config.plugins.TURKVOD.mac_id = ConfigText(default='', fixed_size=False)
config.plugins.TURKVOD.sifreip = ConfigYesNo(default=False)
config.plugins.TURKVOD.httpsposter = ConfigYesNo(default=False)
config.plugins.TURKVOD.dortka = ConfigYesNo(default=False)
config.plugins.TURKVOD.mod = ConfigSelection(default='10', choices=[('10', _('KAPALI')), ('10/cocuk/', _('ACIK'))])
config.plugins.TURKVOD.cachefold = ConfigSelection(default='/media/hdd/', choices=[('/media/hdd/', _('HDD')), ('/media/usb/', _('FLASH DISK')), ('/hdd/movie/', _('HDD MOVIE'))])
config.plugins.TURKVOD.thema = ConfigSelection(default='metrixhd', choices=[('red', _('TURKvod KIRMIZI SKIN')),
 ('black', _('TURKvod SIYAH SKIN')),
 ('seffaf', _('TURKvod SEFFAF SKIN')),
 ('metrixhd', _('MetrixHD SKIN'))])
config.plugins.TURKVOD.fontcolor = ConfigSelection(default='#ffffff', choices=[('#ffffff', _('BEYAZ')),
 ('#d02f2f', _('KIRMIZI')),
 ('#b9b6b6', _('GRI')),
 ('#61ca6b', _('YESIL')),
 ('#bf50bb', _('PEMBE')),
 ('#e7dd44', _('SARI')),
 ('#1c84ef', _('MAVI')),
 ('#929292', _('SIYAH'))])
config.plugins.TURKVOD.menufontcolor = ConfigSelection(default='#e7dd44', choices=[('#e7dd44', _('SARI')),
 ('#d02f2f', _('KIRMIZI')),
 ('#b9b6b6', _('GRI')),
 ('#61ca6b', _('YESIL')),
 ('#bf50bb', _('PEMBE')),
 ('#ffffff', _('BEYAZ')),
 ('#1c84ef', _('MAVI')),
 ('#929292', _('SIYAH'))])
config.plugins.TURKVOD.menualtfontcolor = ConfigSelection(default='#ffffff', choices=[('#ffffff', _('BEYAZ')),
 ('#d02f2f', _('KIRMIZI')),
 ('#b9b6b6', _('GRI')),
 ('#61ca6b', _('YESIL')),
 ('#bf50bb', _('PEMBE')),
 ('#e7dd44', _('SARI')),
 ('#1c84ef', _('MAVI')),
 ('#929292', _('SIYAH'))])
config.plugins.TURKVOD.klevye = ConfigSelection(default='TR', choices=[('TR', _('TR')), ('EN', _('EN')), ('RUS', _('RUS'))])
config.plugins.TURKVOD.server = ConfigSelection(default='co', choices=[('co', _('Server_EU_1')),
 ('site', _('Server_EU_2')),
 ('net', _('Server_EU_3')),
 ('xyz', _('Server_TR'))])
config.plugins.TURKVOD.language = ConfigSelection(default='TR', choices=[('TR', _('TR')),
 ('EN', _('EN')),
 ('DE', _('DE')),
 ('ES', _('ES')),
 ('FR', _('FR'))])
config.plugins.TURKVOD.metrixrenk = ConfigText(default='#18080911', fixed_size=False)
config.plugins.TURKVOD.metrixzemin = ConfigSelection(default='#18080911', choices=[('#40000000', _('SEFFAF-SIYAH')),
 ('#18080911', _('SEFFAF-KOYU SIYAH')),
 ('#40149baf', _('SEFFAF-MAVI')),
 ('#33bab329', _('SEFFAF-SARI')),
 ('#45005050', _('SEFFAF-TURKUAZ')),
 ('#00000000', _('SIYAH')),
 ('#00bf9217', _('SARI')),
 ('#0070ad11', _('YESIL')),
 ('#001f771f', _('KOYU YESIL')),
 ('#00102c54', _('MAVI')),
 ('#00003258', _('KOYU MAVI')),
 ('#00c3461b', _('KIREMIT'))])
serverurl = 'http://turkvod.co/parser/TURKvodPrsr'
TURKvod_headers = {'User-Agent': 'Mozilla/5.0 TURKvod-10'}
def makemodule(url, sourcestr = '', modname = ''):
    modsource = urllib2.urlopen(urllib2.Request(url, data=None, headers=TURKvod_headers)).read()
    obj = compile(modsource, sourcestr, 'exec')
    module = imp.new_module(modname)
    exec obj in module.__dict__
    return module


try:
    TURKvodPrsr = makemodule(url=serverurl, modname='TURKvodPrsr')
except:
    import TURKvodPrsr
TRModules = TURKvodPrsr.modules()
UA = TURKvodPrsr.UA
VER = TURKvodPrsr.VER
themarenk = config.plugins.TURKVOD.thema.value
themarengi = themarenk
if DESKHEIGHT < 1000:
    VERSION = VER
    versiyon = 'hd'
    ver_carpan = 1
    CHANNEL_NUMBER = [5,
     5,
     60,
     30,
     0]
    if themarengi == 'red':
        CHANNEL_NAME = [70,
         5,
         640,
         30,
         1]
    else:
        CHANNEL_NAME = [70,
         5,
         780,
         30,
         1]
    config.plugins.TURKVOD.fontlar = ConfigSelection(default='RegularTURKvod;20', choices=[('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;40', _('40')),
     ('RegularTURKvod;38', _('38')),
     ('RegularTURKvod;36', _('36')),
     ('RegularTURKvod;34', _('34')),
     ('RegularTURKvod;32', _('32')),
     ('RegularTURKvod;30', _('30')),
     ('RegularTURKvod;28', _('28')),
     ('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;24', _('24')),
     ('RegularTURKvod;22', _('22')),
     ('RegularTURKvod;20', _('20'))])
    config.plugins.TURKVOD.fontaciklama = ConfigSelection(default='RegularTURKvod;20', choices=[('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;40', _('40')),
     ('RegularTURKvod;38', _('38')),
     ('RegularTURKvod;36', _('36')),
     ('RegularTURKvod;34', _('34')),
     ('RegularTURKvod;32', _('32')),
     ('RegularTURKvod;30', _('30')),
     ('RegularTURKvod;28', _('28')),
     ('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;24', _('24')),
     ('RegularTURKvod;22', _('22')),
     ('RegularTURKvod;20', _('20'))])
    config.plugins.TURKVOD.fontliste = ConfigSelection(default='22', choices=[('30', _('30')),
     ('40', _('40')),
     ('38', _('38')),
     ('36', _('36')),
     ('34', _('34')),
     ('32', _('32')),
     ('30', _('30')),
     ('28', _('28')),
     ('26', _('26')),
     ('24', _('24')),
     ('22', _('22')),
     ('20', _('20'))])
if DESKHEIGHT > 1000 and DESKHEIGHT < 2000:
    VERSION = VER + ' FHD'
    versiyon = 'fhd'
    ver_carpan = 1.5
    CHANNEL_NUMBER = [16,
     7,
     70,
     50,
     0]
    if themarengi == 'red':
        CHANNEL_NAME = [105,
         7,
         860,
         50,
         1]
    else:
        CHANNEL_NAME = [105,
         7,
         1150,
         50,
         1]
    config.plugins.TURKVOD.fontlar = ConfigSelection(default='RegularTURKvod;32', choices=[('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;40', _('40')),
     ('RegularTURKvod;38', _('38')),
     ('RegularTURKvod;36', _('36')),
     ('RegularTURKvod;34', _('34')),
     ('RegularTURKvod;32', _('32')),
     ('RegularTURKvod;30', _('30')),
     ('RegularTURKvod;28', _('28')),
     ('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;24', _('24')),
     ('RegularTURKvod;22', _('22')),
     ('RegularTURKvod;20', _('20'))])
    config.plugins.TURKVOD.fontaciklama = ConfigSelection(default='RegularTURKvod;28', choices=[('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;40', _('40')),
     ('RegularTURKvod;38', _('38')),
     ('RegularTURKvod;36', _('36')),
     ('RegularTURKvod;34', _('34')),
     ('RegularTURKvod;32', _('32')),
     ('RegularTURKvod;30', _('30')),
     ('RegularTURKvod;28', _('28')),
     ('RegularTURKvod;26', _('26')),
     ('RegularTURKvod;24', _('24')),
     ('RegularTURKvod;22', _('22')),
     ('RegularTURKvod;20', _('20'))])
    config.plugins.TURKVOD.fontliste = ConfigSelection(default='34', choices=[('30', _('30')),
     ('40', _('40')),
     ('38', _('38')),
     ('36', _('36')),
     ('34', _('34')),
     ('32', _('32')),
     ('30', _('30')),
     ('28', _('28')),
     ('26', _('26')),
     ('24', _('24')),
     ('22', _('22')),
     ('20', _('20'))])
if DESKHEIGHT > 2000 or config.plugins.TURKVOD.dortka.value == True:
    VERSION = VER + ' UHD'
    versiyon = 'uhd'
    ver_carpan = 3
    CHANNEL_NUMBER = [30,
     10,
     140,
     70,
     0]
    CHANNEL_NAME = [170,
     10,
     1500,
     70,
     1]
    config.plugins.TURKVOD.fontlar = ConfigSelection(default='RegularTURKvod;52', choices=[('RegularTURKvod;48', _('48')), ('RegularTURKvod;60', _('60')), ('RegularTURKvod;70', _('70'))])
    config.plugins.TURKVOD.fontaciklama = ConfigSelection(default='RegularTURKvod;52', choices=[('RegularTURKvod;48', _('48')), ('RegularTURKvod;60', _('60')), ('RegularTURKvod;70', _('70'))])
    config.plugins.TURKVOD.fontliste = ConfigSelection(default='48', choices=[('48', _('48')),
     ('50', _('50')),
     ('60', _('60')),
     ('70', _('70')),
     ('80', _('80')),
     ('90', _('90')),
     ('20', _('20'))])
par = SafeConfigParser()
par.read('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/language.ini')
Dil = str(config.plugins.TURKVOD.language.value)
if config.plugins.TURKVOD.metrixrenk.value == '#18080911':
    metrixBackground = config.plugins.TURKVOD.metrixzemin.value
else:
    metrixBackground = config.plugins.TURKVOD.metrixrenk.value
BLOCK_H = 40
try:
    pats = os.path.isfile('/media/hdd/TURKvodXML')
    if pats == False:
        os.mkdir('/media/hdd/TURKvodXML')
except Exception as ex:
    print ex
    print 'IMPORT ERROR'

def addstreamboq(bouquetname = None):
    boqfile = '/etc/enigma2/bouquets.tv'
    if not os.path.exists(boqfile):
        pass
    else:
        fp = open(boqfile, 'r')
        lines = fp.readlines()
        fp.close()
        add = True
        for line in lines:
            if 'userbouquet.' + bouquetname + '.tv' in line:
                print '41mahmoud'
                add = False
                break

    if add == True:
        t_v_1 = '#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.%s.tv" ORDER BY bouquet\n'
        fp = open(boqfile, 'a')
        fp.write(t_v_1 % bouquetname)
        fp.close()
        add = True


def addstream(url = None, name = None, bouquetname = None):
    try:
        t_v_2 = '/etc/enigma2/userbouquet.%s.tv'
        t_v_3 = '#SERVICE 4097:0:0:0:0:0:0:0:0:0:%s:%s\r\n'
        error = 'none'
        bouquetname = 'TURKvod'
        fileName = t_v_2 % bouquetname
        out = t_v_3 % (urllib.quote(url), urllib.quote(name))
        addstreamboq(bouquetname)
        if not os.path.exists(fileName):
            fp = open(fileName, 'w')
            fp.write('#NAME %s\n' % bouquetname)
            fp.close()
            fp = open(fileName, 'a')
            fp.write(out)
        else:
            fp = open(fileName, 'r')
            lines = fp.readlines()
            fp.close()
            for line in lines:
                if out in line:
                    error = par.get(Dil, '123')
                    return error

            fp = open(fileName, 'a')
            fp.write(out)
        fp.write('')
        fp.close()
    except:
        error = 'OYNATMA LINKI DEGIL / EKLENEMEDI'

    return error


def debug(obj, text = ''):
    print datetime.fromtimestamp(time()).strftime('[%H:%M:%S]')
    print '%s' % text + ' %s\n' % obj


def mod_request(url, param = None):
    url = 'http://' + url.replace('http://', '').replace('https://', '')
    html = ''
    try:
        debug(url, 'MODUL REQUEST URL')
        req = urllib2.Request(url, param, {'User-agent': UA,
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class iptv_streamse():

    def __init__(self):
        global TRModules
        global TURKVODMODUL
        self.vod = 'http://turkvod.' + config.plugins.TURKVOD.server.value + '/'
        self.iptv_list = []
        self.list_index = 0
        self.iptv_list_tmp = []
        self.list_index_tmp = 0
        self.playlistname_tmp = ''
        self.video_status = False
        self.groups = []
        self.user_mac = ''
        self.playlistname = ''
        self.next_page_url = ''
        self.next_page_text = ''
        self.prev_page_url = ''
        self.prev_page_text = ''
        self.search_text = ''
        self.portal = ''
        self.search_on = ''
        self.url = ''
        self.search_string = ''
        self.startportal = ''
        self.startportalurl = ''
        self.use_rtmpw = False
        self.play_vod = False
        self.play_iptv = False
        self.go_back = False
        self.film_info = []
        self.xml_error = ''
        self.ar_id_start = 0
        self.ar_id_player = int(config.plugins.TURKVOD.start_scale.value)
        self.ar_id_end = 0
        self.iptv_list_history = []
        self.iptv_list_history_list = []
        self.ar_exit = True
        self.ar_start = True
        self.clear_url = ''
        self.my_favorites = []
        self.my_favoritestv = []
        self.kanalliste = []
        self.img_loader = False
        self.moviefolder = config.plugins.TURKVOD.cachefold.value
        self.password = config.plugins.TURKVOD.csifre.value
        self.meldung = ''
        self.banned_text = ''
        self.cont_play = False
        self.cont_pass = False
        self.systems = ''
        self.playhack = ''
        self.url_tmp = ''
        self.security_key = config.plugins.TURKVOD.security_key.value
        self.mac_id = config.plugins.TURKVOD.mac_id.value
        self.delete_images = ''
        self.next_page_url_tmp = ''
        self.next_page_text_tmp = ''
        self.prev_page_url_tmp = ''
        self.prev_page_text_tmp = ''
        self.search_text_tmp = ''
        self.search_on_tmp = ''
        self.pla_url = ''
        self.count = 0
        self.FONT_0 = ('RegularTURKvod', int(config.plugins.TURKVOD.fontliste.value))
        self.FONT_1 = ('RegularTURKvod', int(config.plugins.TURKVOD.fontliste.value))
        self.disable_audioselector = False
        self.history_enable = False
        TURKVODMODUL = modu()
        TRModules = TURKvodPrsr.modules()

    def getValue(self, definitions, default):
        Len = len(definitions)
        return Len > 0 and definitions[Len - 1].text or default

    def read_con(self):
        try:
            url = self.vod
            if not url.startswith('http'):
                url = '%s%s' % ('http://', url)
            p = urlparse.urlparse(url)
            URL_BASE = 'http://' + p.netloc
            PATHS = ['/']
            for path in PATHS:
                self.http = urlparse.urljoin(URL_BASE, path)

        except Exception:
            print 'HATA'

    def read_config(self):
        try:
            xml = ''
            self.read_con()
            startportal = self.http + config.plugins.TURKVOD.mod.value
            if startportal and startportal != '':
                self.startportal = startportal
                self.url = self.startportal
            use_rtmpw = config.plugins.TURKVOD.use_rtmpw.value
            if use_rtmpw and use_rtmpw != '':
                self.use_rtmpw = use_rtmpw
            self.ar_id_start = int(config.plugins.TURKVOD.start_scale.value)
            print 'START SCALE     %s' % self.ar_id_start
            self.ar_id_end = int(config.plugins.TURKVOD.end_scale.value)
            print 'END SCALE       %s' % self.ar_id_end
            self.use_ts_percent = int(config.plugins.TURKVOD.use_ts_percent.value)
            print 'use_ts_percent       %s' % self.use_ts_percent
            self.moviefolder = config.plugins.TURKVOD.cachefold.value
            print 'moviefolder       %s' % self.moviefolder
            print 'startportal     %s' % self.startportal
            print 'use_rtmpw       %s' % self.use_rtmpw
            print 'START SCALE     %s' % self.ar_start
            print 'END SCALE       %s' % self.ar_exit
            print 'Images          %s' % self.img_loader
            print 'Images Fol.     %s' % config.plugins.TURKVOD.images_tmp_path.value
            print 'Moviefolder     %s' % self.moviefolder
            print 'password        %s' % self.password
            print 'delete_images   %s' % self.delete_images
            print 'disable_a.sel  %s' % self.disable_audioselector
            print '-----------CONFIG------------'
        except Exception:
            print '++++++++++ERROR READ CONFIG+++++++++++++'

    def reset_buttons(self):
        self.next_page_url = None
        self.next_page_text = ''
        self.prev_page_url = None
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = None
        return

    def get_list(self, url = None, send_mac = True):
        global PLUGIN_PATH
        self.xml_error = ''
        self.url = url
        self.clear_url = url
        self.list_index = 0
        iptv_list_temp = []
        xml = None
        try:
            if url == 'playlist_history':
                self.iptv_list = self.iptv_list_history_list
                test = self.iptv_list
                self.playlistname = 'GOZATMA GECMISI'
                test.sort(reverse=True)
            elif url == None or url == '':
                tree = ElementTree()
                xml = tree.parse('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/TURKvodLokal.xml')
            elif url == 'favorites':
                tree = ElementTree()
                xml = tree.parse('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/TURKvodFavorites.xml')
            elif url == 'module':
                tree = ElementTree()
                xml = tree.parse('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/TURKvodLokal.xml')
            elif url == 'usb':
                tree = ElementTree()
                xml = tree.parse('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/usb.xml')
            elif url.find('/media/') > -1 and url.find('TURKvodModul@') == -1 and url.find('http') == -1:
                tree = ElementTree()
                xml = tree.parse(url)
            elif url == 'hdd':
                tree = ElementTree()
                xml = tree.parse('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/hdd.xml')
            elif url.find('/media/') > -1 and url.find('TURKvodModul@') == -1 and url.find('http') == -1:
                tree = ElementTree()
                xml = tree.parse(url)
            elif url.find('TURKvodModul') > -1:
                url = url.replace('TURKvodModul@', '')
                print 'START TURKvodModul'
                if self.search_string != '':
                    url = url + '@' + self.search_string
                iptv_list_temp = TURKVODMODUL.get_list(url)
                self.next_page_url = TURKVODMODUL.next_page_url
                self.next_page_text = TURKVODMODUL.next_page_text
                self.prev_page_url = TURKVODMODUL.prev_page_url
                self.prev_page_text = TURKVODMODUL.prev_page_text
                self.search_text = TURKVODMODUL.search_text
                self.search_on = TURKVODMODUL.search_on
                self.playlistname = TURKVODMODUL.playlistname
                self.search_string = ''
                self.xml_error = TURKVODMODUL.error
            elif url.find('TRModules') > -1:
                url = url.replace('TRModules@', '')
                print 'START TRModules'
                if self.search_string != '':
                    url = url + '@' + self.search_string
                iptv_list_temp = TRModules.get_list(url)
                self.next_page_url = TRModules.next_page_url
                self.next_page_text = TRModules.next_page_text
                self.prev_page_url = TRModules.prev_page_url
                self.prev_page_text = TRModules.prev_page_text
                self.search_text = TRModules.search_text
                self.search_on = TRModules.search_on
                self.playlistname = TRModules.playlistname
                self.search_string = ''
                self.xml_error = TRModules.error
            elif url.find('http') > -1:
                xml = self._request(url, send_mac)
            else:
                try:
                    tree = ElementTree()
                    xml = tree.parse(PLUGIN_PATH + '/' + url)
                except Exception:
                    print 'ERROR: XML to LISTE'

            if xml:
                self.next_page_url = ''
                self.next_page_text = ''
                self.prev_page_url = ''
                self.prev_page_text = ''
                self.search_text = ''
                self.protected = ''
                self.playlistname = xml.findtext('playlist_name').encode('utf-8')
                self.next_page_url = xml.findtext('next_page_url')
                next_page_text_element = xml.findall('next_page_url')
                if next_page_text_element:
                    self.next_page_text = next_page_text_element[0].attrib.get('text').encode('utf-8')
                self.prev_page_url = xml.findtext('prev_page_url')
                prev_page_text_element = xml.findall('prev_page_url')
                if prev_page_text_element:
                    self.prev_page_text = prev_page_text_element[0].attrib.get('text').encode('utf-8')
                self.search_on = xml.findtext('search_on')
                search_text_element = xml.findall('search_on')
                if search_text_element:
                    self.search_text = search_text_element[0].attrib.get('text').encode('utf-8')
                chan_counter = 0
                for channel in xml.findall('channel'):
                    chan_counter = chan_counter + 1
                    name = channel.findtext('title').encode('utf-8')
                    piconname = channel.findtext('logo_30x30')
                    description = channel.findtext('description')
                    protected_search = channel.findtext('protected')
                    if protected_search:
                        protected = 'True'
                    else:
                        protected = None
                    img_src = ''
                    if description != None:
                        description = description.encode('utf-8')
                        img_src_list = re.findall('img .*?src="(.*?)"', description)
                        if len(img_src_list) > 0:
                            img_src = img_src_list[0]
                        else:
                            img_src_list = re.findall("img .*?src='(.*?)'", description)
                            if len(img_src_list) > 0:
                                img_src = img_src_list[0]
                        description = description.replace('<br>', '\n')
                        description = description.replace('<br/>', '\n')
                        description = description.replace('</h1>', '</h1>\n')
                        description = description.replace('</h2>', '</h2>\n')
                        description = description.replace('&nbsp;', ' ')
                        description4playlist_html = description
                        text = re.compile('<[\\/\\!]*?[^<>]*?>')
                        description = text.sub('', description)
                    stream_url = channel.findtext('stream_url')
                    if stream_url and self.use_rtmpw:
                        stream_url = stream_url.replace('rtmp', 'http://127.0.0.1:1234/?r=rtmp')
                        if stream_url.find('rtmp') > 0:
                            name = name + ' [RTMPGW on]'
                    playlist_url = channel.findtext('playlist_url')
                    category_id = channel.findtext('category_id')
                    ts_stream = channel.findtext('ts_stream')
                    chan_tulpe = (chan_counter,
                     name,
                     description,
                     piconname,
                     stream_url,
                     playlist_url,
                     category_id,
                     img_src,
                     description4playlist_html,
                     protected,
                     ts_stream)
                    iptv_list_temp.append(chan_tulpe)

        except Exception as ex:
            print ex
            self.xml_error = ex
            print '!!!!!!!!!!!!!!!!!! ERROR: XML to LISTE'

        if len(iptv_list_temp):
            self.history_enable = True
            last_channel = self.url
            if len(self.iptv_list_history) > 1:
                prelast_channel = self.iptv_list_history[len(self.iptv_list_history) - 1]
                if last_channel == prelast_channel:
                    self.history_enable = False
                if self.history_enable == True:
                    for list_enable in self.iptv_list_history:
                        if list_enable == last_channel:
                            self.history_enable = False

            if last_channel != None and last_channel != '' and self.history_enable == True:
                self.iptv_list_history.append(last_channel)
            self.iptv_list = iptv_list_temp
        else:
            print 'ERROR IPTV_LIST_LEN = %s' % len(iptv_list_temp)
        return

    def _request(self, url, mac = None):
        sign = '?'
        url = url.strip(' \t\n\r')
        if url.find('?') > -1:
            sign = '&'
        mac = self.mac_id
        if mac != '':
            url = url + sign + 'box_mac=' + mac + '&key=' + self.security_key
        else:
            mac = self.user_mac
            url = url + sign + 'box_mac=' + mac + '&key=' + self.security_key
        if self.search_string != '':
            url = url + '&' + self.search_on + '=' + ul.quote(self.search_string)
        try:
            if url.find('|') > -1:
                parts = url.split('|')
                url = parts[0]
                cookie = parts[1]
                req = urllib2.Request(url, None, {'User-agent': UA,
                 'Connection': 'Close',
                 'Cookie': cookie})
            else:
                req = urllib2.Request(url, None, {'User-agent': UA,
                 'Connection': 'Close'})
                xmlstream = urllib2.urlopen(req).read()
                res = fromstring(xmlstream)
        except Exception as ex:
            print ex
            print 'REQUEST Exception'
            res = None
            self.xml_error = ex

        self.search_string = ''
        return res

    def write_favorites(self):
        print 'START write_favorites'
        try:
            fileObj = open(PLUGIN_PATH + '/' + TURKvod + 'Favorites.xml', 'w')
            fileObj.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
            fileObj.write('<items>\n')
            fileObj.write('<playlist_name>' + par.get(Dil, '1') + '</playlist_name>\n')
            for channel in self.my_favorites:
                fileObj.write('\t<channel>\n')
                fileObj.write('\t\t\t<title>%s</title>\n' % channel[1].replace(' [RTMPGW on]', ''))
                if channel[3]:
                    fileObj.write('\t\t\t<logo_30x30><![CDATA[%s]]></logo_30x30>\n' % channel[3])
                if channel[4]:
                    fileObj.write('\t\t\t<stream_url><![CDATA[%s]]></stream_url>\n' % channel[4].replace('http://127.0.0.1:1234/?r=rtmp', 'rtmp'))
                if channel[5]:
                    fileObj.write('\t\t\t<playlist_url><![CDATA[%s]]></playlist_url>\n' % channel[5])
                fileObj.write('\t\t\t<description><![CDATA[%s]]></description>\n' % channel[8])
                if channel[9]:
                    fileObj.write('\t\t\t<protected><![CDATA[%s]]></protected>\n' % channel[9])
                if channel[10]:
                    fileObj.write('\t\t\t<ts_stream><![CDATA[%s]]></ts_stream>\n' % channel[10])
                fileObj.write('\t</channel>\n\n\n')

            fileObj.write('</items>\n')
            fileObj.close()
        except Exception as ex:
            print ex
            print 'Exception write_favorites'

        print 'END write_favorites'


HW_INFO = {}
TURKvod = 'TURKvod'
s = '.xml'
_n_ = config.plugins.TURKVOD.server.value
fontcolorfont = config.plugins.TURKVOD.fontcolor.value
menufontcolor = config.plugins.TURKVOD.menufontcolor.value
menuustfontcolor = config.plugins.TURKVOD.menualtfontcolor.value
mfont = config.plugins.TURKVOD.fontlar.value
fontaciklama = config.plugins.TURKVOD.fontaciklama.value
try:
    import commands
except Exception as ex:
    print ex

try:
    import servicewebts
    print 'OK servicewebts TURKvod *******************************************************'
except Exception as ex:
    print ex
    print 'ERROR servicewebts TURKvod *******************************************************'

class IPTVInfoBarShowHide():
    STATE_HIDDEN = 0
    STATE_HIDING = 1
    STATE_SHOWING = 2
    STATE_SHOWN = 3

    def __init__(self):
        self['ShowHideActions'] = ActionMap(['InfobarShowHideActions'], {'toggleShow': self.toggleShow,
         'hide': self.hide}, 1)
        self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evStart: self.serviceStarted})
        self.__state = self.STATE_SHOWN
        self.__locked = 0
        self.hideTimer = eTimer()
        self.hideTimer.callback.append(self.doTimerHide)
        self.hideTimer.start(1000, True)
        self.onShow.append(self.__onShow)
        self.onHide.append(self.__onHide)

    def serviceStarted(self):
        if self.execing:
            if config.usage.show_infobar_on_zap.value:
                self.doShow()

    def __onShow(self):
        self.__state = self.STATE_SHOWN
        self.startHideTimer()

    def startHideTimer(self):
        if self.__state == self.STATE_SHOWN and not self.__locked:
            idx = config.usage.infobar_timeout.index
            if idx:
                self.hideTimer.start(idx * 1000, True)

    def __onHide(self):
        self.__state = self.STATE_HIDDEN

    def doShow(self):
        self.show()
        self.startHideTimer()

    def doTimerHide(self):
        self.hideTimer.stop()
        if self.__state == self.STATE_SHOWN:
            self.hide()

    def toggleShow(self):
        if self.__state == self.STATE_SHOWN:
            self.hide()
            self.hideTimer.stop()
        elif self.__state == self.STATE_HIDDEN:
            self.show()

    def lockShow(self):
        self.__locked = self.__locked + 1
        if self.execing:
            self.show()
            self.hideTimer.stop()

    def unlockShow(self):
        self.__locked = self.__locked - 1
        if self.execing:
            self.startHideTimer()


class downloadJob(Job):

    def __init__(self, toolbox, cmdline, filename, filetitle):
        Job.__init__(self, par.get(Dil, '2') + ' %s' % filetitle)
        self.filename = filename
        self.toolbox = toolbox
        self.retrycount = 0
        downloadTask(self, cmdline, filename)

    def retry(self):
        self.retrycount += 1
        self.restart()

    def cancel(self):
        self.abort()


class downloadTask(Task):
    ERROR_CORRUPT_FILE, ERROR_RTMP_ReadPacket, ERROR_SEGFAULT, ERROR_SERVER, ERROR_UNKNOWN = range(5)

    def __init__(self, job, cmdline, filename):
        Task.__init__(self, job, _(par.get(Dil, '3')))
        self.postconditions.append(downloadTaskPostcondition())
        self.setCmdline(cmdline)
        self.filename = filename
        self.toolbox = job.toolbox
        self.error = None
        self.lasterrormsg = None
        return

    def processOutput(self, data):
        try:
            if data.endswith('%)'):
                startpos = data.rfind('sec (') + 5
                if startpos and startpos != -1:
                    self.progress = int(float(data[startpos:-4]))
            elif data.find('%') != -1:
                tmpvalue = data[:data.find('%')]
                tmpvalue = tmpvalue[tmpvalue.rfind(' '):].strip()
                tmpvalue = tmpvalue[tmpvalue.rfind('(') + 1:].strip()
                self.progress = int(float(tmpvalue))
            else:
                Task.processOutput(self, data)
        except Exception as errormsg:
            print 'Error processOutput: ' + str(errormsg)
            Task.processOutput(self, data)

    def processOutputLine(self, line):
        line = line[:-1]
        self.lasterrormsg = line
        if line.startswith('ERROR:'):
            if line.find('RTMP_ReadPacket') != -1:
                self.error = self.ERROR_RTMP_ReadPacket
            elif line.find('corrupt file!') != -1:
                self.error = self.ERROR_CORRUPT_FILE
                os_system('rm -f %s' % self.filename)
            else:
                self.error = self.ERROR_UNKNOWN
        elif line.startswith('wget:'):
            if line.find('server returned error') != -1:
                self.error = self.ERROR_SERVER
        elif line.find('Segmentation fault') != -1:
            self.error = self.ERROR_SEGFAULT

    def afterRun(self):
        pass


class downloadTaskPostcondition(Condition):
    RECOVERABLE = True

    def check(self, task):
        if task.returncode == 0 or task.error is None:
            return True
        else:
            return False
            return

    def getErrorMessage(self, task):
        return {task.ERROR_CORRUPT_FILE: _(par.get(Dil, '5') + '\n\n' + par.get(Dil, '6') + '\n%s' % task.lasterrormsg),
         task.ERROR_RTMP_ReadPacket: _(par.get(Dil, '5') + '\n\n' + par.get(Dil, '7') + '\n%s' % task.lasterrormsg),
         task.ERROR_SEGFAULT: _(par.get(Dil, '5') + '\n\n' + par.get(Dil, '8') + '\n%s' % task.lasterrormsg),
         task.ERROR_SERVER: _(par.get(Dil, '5') + '\n\n' + par.get(Dil, '9') + '\n%s' % task.lasterrormsg),
         task.ERROR_UNKNOWN: _(par.get(Dil, '5') + '\n\n' + par.get(Dil, '10') + '\n%s' % task.lasterrormsg)}[task.error]


def getInfo():
    try:
        info = {}
        brand = 'Dream Multimedia'
        model = 'unknown'
        chipset = 'unknown'
        mac = ''
        if fileExists('/proc/stb/info/vumodel'):
            brand = 'Vuplus'
            f = open('/proc/stb/info/vumodel', 'r')
            model = f.readline().strip()
            f.close()
        elif fileExists('/proc/stb/info/boxtype'):
            brand = 'Clarke-Xtrend'
            f = open('/proc/stb/info/boxtype', 'r')
            model = f.readline().strip()
            f.close()
        else:
            f = open('/proc/stb/info/model', 'r')
            model = f.readline().strip()
            f.close()
        if fileExists('/proc/stb/info/chipset'):
            f = open('/proc/stb/info/chipset', 'r')
            chipset = f.readline().strip()
            f.close()
        info['brand'] = brand
        info['model'] = model
        info['chipset'] = chipset
        try:
            ifaces = iNetwork.getConfiguredAdapters()
            mac = iNetwork.getAdapterAttribute(ifaces[0], 'mac')
        except Exception as ex:
            print ex
            mac = ''
            print 'ERROR info[mac]'

        info['mac'] = mac
    except Exception as ex:
        print ex
        print 'ERROR GET HW INFO'

    return info


VIDEO_ASPECT_RATIO_MAP = {0: '4:3 Letterbox',
 1: '4:3 PanScan',
 2: '16:9',
 3: '16:9 Always',
 4: '16:10 Letterbox',
 5: '16:10 PanScan',
 6: '16:9 Letterbox'}

def nextAR():
    try:
        TURKVOD.ar_id_player += 1
        if TURKVOD.ar_id_player > 6:
            TURKVOD.ar_id_player = 0
        eAVSwitch.getInstance().setAspectRatio(TURKVOD.ar_id_player)
        print 'TURKVOD.ar_id_player NEXT %s' % VIDEO_ASPECT_RATIO_MAP[TURKVOD.ar_id_player]
        return VIDEO_ASPECT_RATIO_MAP[TURKVOD.ar_id_player]
    except Exception as ex:
        print ex
        return 'nextAR ERROR %s' % ex


def prevAR():
    try:
        TURKVOD.ar_id_player -= 1
        if TURKVOD.ar_id_player == -1:
            TURKVOD.ar_id_player = 6
        eAVSwitch.getInstance().setAspectRatio(TURKVOD.ar_id_player)
        print 'TURKVOD.ar_id_player PREV %s' % VIDEO_ASPECT_RATIO_MAP[TURKVOD.ar_id_player]
        return VIDEO_ASPECT_RATIO_MAP[TURKVOD.ar_id_player]
    except Exception as ex:
        print ex
        return 'prevAR ERROR %s' % ex


def menu(menuid, **kwargs):
    if menuid == 'mainmenu':
        return [('TURKvod',
          Start_iptv_palyer,
          'TURKvod',
          4)]
    return []


def getmac(eth):
    global MAC
    mac = None
    try:
        mac = os.popen("ip link show %s | awk '/ether/ {print $2}'" % eth).read()
        print 'os.popen'
    except Exception as ex:
        print ex
        print 'getmac'
        try:
            ifconfig = commands.getoutput('ifconfig ' + eth)
            print 'ifconfig'
            mac_search = re.search('\\w\\w:\\w\\w:.+\n', ifconfig)
            mac = mac_search.group(0).lower()
        except Exception as ex:
            print ex
            print 'getmac2'

    mac = mac.strip(' \t\n\r')
    if mac is None:
        parsedMac = 'xxxxxxxxxxx'
    else:
        parsedMac = mac
    MAC = parsedMac
    return parsedMac


def web_info(message):
    try:
        message = str(message)
        cmd = "wget 'http://127.0.0.1/web/message?type=2&timeout=10&text=%s' 2>/dev/null &" % message
        debug(cmd, 'CMD -> Console -> WEBIF')
        os.popen(cmd)
    except:
        print 'web_info ERROR'


def Start_iptv_palyer(session, **kwargs):
    global PLUGIN_PATS
    global httpss
    global FIRST_SESSION
    global VERSION
    global TURKVOD
    global HW_INFO
    global TURKVOD_PARSER
    global TURKvod_PATS
    print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
    print '######################################################################'
    print '#######--------------- START TURKvod ver %s ---------------#######' % VERSION
    print '######################################################################'
    HW_INFO = getInfo()
    print 'hw_info: ', HW_INFO
    print HW_INFO['brand']
    print HW_INFO['model']
    print HW_INFO['chipset']
    TURKVOD = iptv_streamse()
    TURKVOD.read_config()
    PLUGIN_PATS = TURKVOD.http
    ifaces = iNetwork.getConfiguredAdapters()
    httpss = iNetwork.getAdapterAttribute(ifaces[0], 'mac')
    TURKvod_PATS = 'http://turkvod.' + _n_ + '/'
    try:
        TURKVOD.user_mac = getmac('eth0')
        print 'MAC from Console'
    except:
        TURKVOD.user_mac = HW_INFO['mac']
        print 'MAC from Enigma2'

    if TURKVOD.ar_start:
        eAVSwitch.getInstance().setAspectRatio(TURKVOD.ar_id_start)
        print 'setAspectRatio(TURKVOD.ar_id_start)'
    try:
        TURKVOD_PARSER = TURKvodPrsr.turkvod_parsers()
    except Exception as ex:
        print ex
        print 'PARSER ERROR'

    if TURKVOD.use_rtmpw:
        try:
            cmd = '/usr/bin/rtmpgw -g 1234 -v 2>/dev/null &'
            os.popen(cmd)
            debug(cmd)
        except Exception as ex:
            print ex
            print 'rtmpgw'

    TURKVOD.get_list('favorites')
    TURKVOD.my_favorites = TURKVOD.iptv_list
    TURKVOD.get_list(TURKVOD.startportal)
    FIRST_SESSION = session.nav.getCurrentlyPlayingServiceReference()
    print 'FIRST_SESSION'
    session.open(TURKvodPlaylist)


class TURKvodPlaylist(Screen):
    fontcolor = fontcolorfont
    menufont = menufontcolor
    menuust = menuustfontcolor
    menufontt = mfont
    aciklamafont = fontaciklama
    if themarengi == 'red':
        if versiyon == 'hd':
            skin = '\n\t\t<screen position="0,0" size="1280,720" backgroundColor="transparent" flags="wfNoBorder" title="Playlist" >\n\t\t\t<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/menu' + themarengi + '.png" zPosition="-5" transparent="0" alphatest="blend" />\n\t\t\t<widget  name="Listbox1" position="626,125" size="634,520" foregroundColorSelected="' + str(menufont) + '" backgroundColor="#21000000" backgroundColorSelected="#42000C" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/x37' + themarengi + '.png" foregroundColor="' + str(menuust) + '" enableWrapAround="0" zPosition="1" scrollbarMode="showOnDemand" transparent="3" />\n\t\t\t<widget  backgroundColor="#26181d20" foregroundColor="#ffffff" position="21,125" size="329,300" halign="right" name="description" font="' + aciklamafont + '" zPosition="4" transparent="1" />\n\t\t\t<widget  name="playlist" position="690,89" zPosition="4" size="550,28" halign="left" font="TURKvodRegular;22" transparent="5" foregroundColor="#ffdfdf" backgroundColor="#21000000"  />\n\t\t\t<widget  name="poster"   position="364,125"  size="250,365" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget  name="version"  position="50,673" zPosition="4" size="70,25" halign="left" font="RegularTURKvod;20" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" text="" />\n\t\t\t<widget  name="chminus"  position="725,37"  zPosition="4" size="250,30" halign="left" font="' + menufontt + '" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"  />\n\t\t\t<widget  name="chplus"   position="1002,37" zPosition="4" size="250,30" halign="left" font="' + menufontt + '" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"  />\n\t\t\t<widget name="menu" font="' + menufontt + '" position="200,37" size="110,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="gecmis" font="' + menufontt + '" position="353,37" size="100,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="favori" font="' + menufontt + '" position="322,673" size="105,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="filme_don" font="' + menufontt + '" position="1125,673" size="130,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="hdd" font="' + menufontt + '" position="782,673" size="125,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cekis" font="' + menufontt + '" position="660,673" size="85,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="lokal" font="' + menufontt + '" position="953,673" size="135,25" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="indirilen" font="' + menufontt + '" position="486,673" size="135,25" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" />\n\t\t\t<widget source="session.VideoPicture" render="Pig" position="30,447" size="310,174" zPosition="7" backgroundColor="transparent" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="130,661" size="120,45" foregroundColor="#ffffff" zPosition="2" font="TURKvodRegular;40" halign="left" transparent="2" >\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t</screen>'
        if versiyon == 'fhd':
            skin = '\n\t\t<screen position="0,0" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder" title="Playlist" >\n\t\t\t<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/menufhd' + themarengi + '.png" zPosition="-5" transparent="0" alphatest="blend" />\n\t\t\t<widget  name="Listbox1" position="939,188" size="951,762" foregroundColorSelected="' + str(menufont) + '" backgroundColor="#21000000" backgroundColorSelected="#21000000" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/x37fhd' + themarengi + '.png" foregroundColor="' + str(menuust) + '" enableWrapAround="0" zPosition="1" scrollbarMode="showOnDemand" transparent="3" />\n\t\t\t<widget  backgroundColor="#26181d20" foregroundColor="#ffffff" position="32,188" size="494,450" halign="right" name="description" font="' + aciklamafont + '" zPosition="4" transparent="1" />\n\t\t\t<widget  name="playlist" position="1006,134" zPosition="4" size="825,40" halign="left" font="TURKvodRegular;36" transparent="5" foregroundColor="#ffdfdf" backgroundColor="#21000000"  />\n\t\t\t<widget  name="poster"   position="546,187"  size="375,548" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget  name="version"  position="45,1010" zPosition="4" size="130,38" halign="left" font="RegularTURKvod;24" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" text="" />\n\t\t\t<widget  name="chminus"  position="1088,56"  zPosition="4" size="375,45" halign="left" font="' + menufontt + '" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"  />\n\t\t\t<widget  name="chplus"   position="1503,56" zPosition="4" size="375,45" halign="left" font="' + menufontt + '" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"  />\n\t\t\t<widget name="menu" font="' + menufontt + '" position="300,56" size="165,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="gecmis" font="' + menufontt + '" position="530,56" size="150,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="favori" font="' + menufontt + '" position="483,1010" size="158,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="filme_don" font="' + menufontt + '" position="1688,1010" size="195,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="hdd" font="' + menufontt + '" position="1173,1010" size="188,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cekis" font="' + menufontt + '" position="990,1010" size="128,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="lokal" font="' + menufontt + '" position="1430,1010" size="203,38" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="indirilen" font="' + menufontt + '" position="729,1010" size="203,38" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" />\n\t\t\t<widget source="session.VideoPicture" render="Pig" position="45,670" size="465,261" zPosition="7" backgroundColor="transparent" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="195,992" size="180,68" foregroundColor="#ffffff" zPosition="2" font="TURKvodRegular;66" halign="left" transparent="2" >\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t</screen>'
    if themarengi == 'black':
        if versiyon == 'hd':
            skin = '\n\t\t<screen position="0,0" size="1280,720" backgroundColor="transparent" flags="wfNoBorder" title="Playlist" >\n\t\t\t<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/menu' + themarengi + '.png" zPosition="-5" transparent="0" alphatest="blend" />\n\t\t\t<widget name="Listbox1" position="490,107" size="784,510" foregroundColorSelected="' + str(menufont) + '" backgroundColor="#21000000" backgroundColorSelected="#21000000" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/x37' + themarengi + '.png" foregroundColor="' + str(menuust) + '" enableWrapAround="0" zPosition="1" scrollbarMode="showOnDemand" transparent="3" />\n\t\t\t<widget backgroundColor="#26181d20" foregroundColor="#9e9e9a" position="47,450" size="376,175" halign="center" name="description" font="' + aciklamafont + '" zPosition="4" transparent="1" />\n\t\t\t<widget name="playlist" position="503,50" zPosition="4" size="770,26" halign="left" font="TURKvodRegular;22" transparent="5" foregroundColor="#b0af81" backgroundColor="#21000000"  />\n\t\t\t<widget name="poster"   position="107,107"  size="250,313" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="version"  position="200,60" zPosition="4" size="90,30" halign="left" font="RegularTURKvod;16" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" text="" />\n\t\t\t<widget name="filme_don" font="' + menufontt + '" position="1118,661" size="167,26"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cekis" font="' + menufontt + '" position="531,661" size="167,26"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="lokal" font="' + menufontt + '" position="897,661" size="167,26" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="hdd" font="' + menufontt + '" position="667,661" size="167,26" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="347,660" size="120,46" foregroundColor="#9e9e9a" zPosition="2" font="TURKvodRegular;40" halign="left" transparent="2" >\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t</screen>'
        if versiyon == 'fhd':
            skin = '\n\t\t<screen position="0,0" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder" title="Playlist" >\n\t\t\t<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/menufhd' + themarengi + '.png" zPosition="-5" transparent="0" alphatest="blend" />\n\t\t\t<widget  name="Listbox1" position="735,160" size="1175,765" foregroundColorSelected="' + str(menufont) + '" backgroundColor="#21000000" backgroundColorSelected="#21000000" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/x37fhd' + themarengi + '.png" foregroundColor="' + str(menuust) + '" enableWrapAround="0" zPosition="1" scrollbarMode="showOnDemand" transparent="3" />\n\t\t\t<widget  backgroundColor="#26181d20" foregroundColor="#9e9e9a" position="70,675" size="565,262" halign="center" name="description" font="' + aciklamafont + '" zPosition="4" transparent="1" />\n\t\t\t<widget  name="playlist" position="754,75" zPosition="4" size="1155,38" halign="left" font="TURKvodRegular;36" transparent="5" foregroundColor="#b0af81" backgroundColor="#21000000"  />\n\t\t\t<widget  name="poster"   position="160,160"  size="375,470" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget  name="version"  position="300,90" zPosition="4" size="130,38" halign="left" font="RegularTURKvod;22" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" text="" />\n\t\t\t<widget name="filme_don" font="' + menufontt + '" position="1677,992" size="250,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cekis" font="' + menufontt + '" position="797,992" size="250,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="lokal" font="' + menufontt + '" position="1346,992" size="250,38" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="hdd" font="' + menufontt + '" position="1000,992" size="250,38" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="520,990" size="180,68" foregroundColor="#9e9e9a" zPosition="2" font="TURKvodRegular;50" halign="left" transparent="2" >\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t</screen>'
    if themarengi == 'seffaf':
        if versiyon == 'hd':
            skin = '\n\t\t<screen position="0,0" size="1280,720" backgroundColor="#44000000" flags="wfNoBorder" title="Playlist" >\n\t\t\t<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/menu' + themarengi + '.png" zPosition="-5" transparent="0" alphatest="blend" />\n\t\t\t<widget name="Listbox1" position="490,107" size="784,510" foregroundColorSelected="' + str(menufont) + '" backgroundColor="#21000000" backgroundColorSelected="#44000000" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/x37' + themarengi + '.png" foregroundColor="' + str(menuust) + '" enableWrapAround="0" zPosition="1" scrollbarMode="showOnDemand" transparent="3" />\n\t\t\t<widget backgroundColor="#26181d20" foregroundColor="#9e9e9a" position="47,450" size="376,175" halign="center" name="description" font="' + aciklamafont + '" zPosition="4" transparent="1" />\n\t\t\t<widget name="playlist" position="503,50" zPosition="4" size="770,26" halign="left" font="TURKvodRegular;22" transparent="5" foregroundColor="#b0af81" backgroundColor="#21000000"  />\n\t\t\t<widget name="poster"   position="107,107"  size="250,313" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="version"  position="200,60" zPosition="4" size="90,30" halign="left" font="RegularTURKvod;16" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" text="" />\n\t\t\t<widget name="filme_don" font="' + menufontt + '" position="1118,661" size="167,26"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cekis" font="' + menufontt + '" position="531,661" size="167,26"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="lokal" font="' + menufontt + '" position="897,661" size="167,26" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="hdd" font="' + menufontt + '" position="667,661" size="167,26" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="347,660" size="120,46" foregroundColor="#9e9e9a" zPosition="2" font="TURKvodRegular;40" halign="left" transparent="2" >\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t</screen>'
        if versiyon == 'fhd':
            skin = '\n\t\t<screen position="0,0" size="1920,1080" backgroundColor="#44000000" flags="wfNoBorder" title="Playlist" >\n\t\t\t<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/menufhd' + themarengi + '.png" zPosition="-5" transparent="0" alphatest="blend" />\n\t\t\t<widget  name="Listbox1" position="735,160" size="1175,765" foregroundColorSelected="' + str(menufont) + '" backgroundColor="#21000000" backgroundColorSelected="#44000000" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/x37fhd' + themarengi + '.png" foregroundColor="' + str(menuust) + '" enableWrapAround="0" zPosition="1" scrollbarMode="showOnDemand" transparent="3" />\n\t\t\t<widget  backgroundColor="#26181d20" foregroundColor="#9e9e9a" position="70,675" size="565,262" halign="center" name="description" font="' + aciklamafont + '" zPosition="4" transparent="1" />\n\t\t\t<widget  name="playlist" position="754,75" zPosition="4" size="1155,38" halign="left" font="TURKvodRegular;36" transparent="5" foregroundColor="#b0af81" backgroundColor="#21000000"  />\n\t\t\t<widget  name="poster"   position="160,160"  size="375,470" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget  name="version"  position="300,90" zPosition="4" size="130,38" halign="left" font="RegularTURKvod;22" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" text="" />\n\t\t\t<widget name="filme_don" font="' + menufontt + '" position="1677,992" size="250,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cekis" font="' + menufontt + '" position="797,992" size="250,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="lokal" font="' + menufontt + '" position="1346,992" size="250,38" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="hdd" font="' + menufontt + '" position="1000,992" size="250,38" zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="520,990" size="180,68" foregroundColor="#9e9e9a" zPosition="2" font="TURKvodRegular;50" halign="left" transparent="2" >\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t</screen>'
    if themarengi == 'metrixhd' or versiyon == 'uhd':
        skin = ' <screen name="TURKvodPlaylist" title="Playlist" position="0,0" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(720 * ver_carpan)) + '" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="' + str(int(51 * ver_carpan)) + ',' + str(int(51 * ver_carpan)) + '" zPosition="-10" size="' + str(int(340 * ver_carpan)) + ',' + str(int(536 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <widget name="playlist" position="' + str(int(464 * ver_carpan)) + ',' + str(int(72 * ver_carpan)) + '" size="' + str(int(736 * ver_carpan)) + ',' + str(int(45 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(24 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget name="Listbox1" position="' + str(int(440 * ver_carpan)) + ',' + str(int(116 * ver_carpan)) + '" size="' + str(int(760 * ver_carpan)) + ',' + str(int(360 * ver_carpan)) + '" scrollbarMode="showOnDemand" font="RegularTURKvod;' + str(int(26 * ver_carpan)) + '" itemHeight="' + str(int(30 * ver_carpan)) + '" transparent="1" foregroundColorSelected="' + str(menufont) + '" backgroundColor="' + metrixBackground + '" backgroundColorSelected="' + metrixBackground + '" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/line_' + versiyon + '.png" foregroundColor="' + str(menuust) + '" />\n    <widget name="description" position="' + str(int(462 * ver_carpan)) + ',' + str(int(510 * ver_carpan)) + '" size="' + str(int(740 * ver_carpan)) + ',' + str(int(120 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" halign="left" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" transparent="1" />\n    <widget name="poster" position="' + str(int(64 * ver_carpan)) + ',' + str(int(61 * ver_carpan)) + '" size="' + str(int(316 * ver_carpan)) + ',' + str(int(450 * ver_carpan)) + '" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" backgroundColor="' + metrixBackground + '" transparent="1" valign="center" alphatest="blend" />\n    <widget name="version" position="' + str(int(246 * ver_carpan)) + ',' + str(int(550 * ver_carpan)) + '" size="' + str(int(150 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" halign="leff" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="3" zPosition="6" alphatest="blend" />\n    <widget name="filme_don" position="' + str(int(1044 * ver_carpan)) + ',' + str(int(635 * ver_carpan)) + '" size="' + str(int(160 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="1" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget name="cekis" position="' + str(int(453 * ver_carpan)) + ',' + str(int(635 * ver_carpan)) + '" size="' + str(int(160 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="1" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget name="lokal" position="' + str(int(848 * ver_carpan)) + ',' + str(int(635 * ver_carpan)) + '" size="' + str(int(160 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="1" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget name="hdd" position="' + str(int(650 * ver_carpan)) + ',' + str(int(635 * ver_carpan)) + '" size="' + str(int(160 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="1" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/red_' + versiyon + '.png" position="' + str(int(415 * ver_carpan)) + ',' + str(int(630 * ver_carpan)) + '" size="' + str(int(30 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" alphatest="blend" />\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/green_' + versiyon + '.png" position="' + str(int(612 * ver_carpan)) + ',' + str(int(630 * ver_carpan)) + '" size="' + str(int(30 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" alphatest="blend" />\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/yellow_' + versiyon + '.png" position="' + str(int(811 * ver_carpan)) + ',' + str(int(630 * ver_carpan)) + '" size="' + str(int(30 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" alphatest="blend" />\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/blue_' + versiyon + '.png" position="' + str(int(1006 * ver_carpan)) + ',' + str(int(630 * ver_carpan)) + '" size="' + str(int(30 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" alphatest="blend" />\n    <eLabel position="' + str(int(417 * ver_carpan)) + ',' + str(int(52 * ver_carpan)) + '" zPosition="-10" size="' + str(int(810 * ver_carpan)) + ',' + str(int(432 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <eLabel position="' + str(int(417 * ver_carpan)) + ',' + str(int(489 * ver_carpan)) + '" zPosition="-10" size="' + str(int(810 * ver_carpan)) + ',' + str(int(182 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\t\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(239 * ver_carpan)) + ',' + str(int(610 * ver_carpan)) + '" size="' + str(int(169 * ver_carpan)) + ',' + str(int(80 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(60 * ver_carpan)) + '" halign="left" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1" valign="top">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(83 * ver_carpan)) + ',' + str(int(640 * ver_carpan)) + '" size="' + str(int(148 * ver_carpan)) + ',' + str(int(29 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%e. %b</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(107 * ver_carpan)) + ',' + str(int(616 * ver_carpan)) + '" size="' + str(int(125 * ver_carpan)) + ',' + str(int(30 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%A</convert>\n    </widget>\n    <eLabel position="' + str(int(51 * ver_carpan)) + ',' + str(int(599 * ver_carpan)) + '" zPosition="-1" size="' + str(int(340 * ver_carpan)) + ',' + str(int(70 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="0" />\n    <ePixmap name="" position="' + str(int(64 * ver_carpan)) + ',' + str(int(520 * ver_carpan)) + '" size="' + str(int(316 * ver_carpan)) + ',' + str(int(59 * ver_carpan)) + '" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/logo_' + versiyon + '.png" alphatest="blend" transparent="1" zPosition="5" />\n  </screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        self.channel_list = TURKVOD.iptv_list
        self.index = TURKVOD.list_index
        self['version'] = Label('')
        self['version'].setText('v. %s' % VERSION)
        self.banned = False
        self.banned_text = ''
        self.mlist = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
        self.mlist.l.setFont(0, gFont(TURKVOD.FONT_0[0], TURKVOD.FONT_0[1]))
        self.mlist.l.setFont(1, gFont(TURKVOD.FONT_1[0], TURKVOD.FONT_1[1]))
        if DESKHEIGHT < 1000:
            self.mlist.l.setItemHeight(int(config.plugins.TURKVOD.fontliste.value) + 6)
        else:
            self.mlist.l.setItemHeight(int(config.plugins.TURKVOD.fontliste.value) + 6)
        self['Listbox1'] = self.mlist
        self.mlist.setList(map(channelEntryIPTVplaylist, self.channel_list))
        self.mlist.onSelectionChanged.append(self.update_description)
        self['description'] = ScrollLabel('')
        self['info'] = Label()
        self['playlist'] = Label()
        self['chplus'] = Label()
        self['chminus'] = Label()
        self['stop'] = Label()
        self['menu'] = Label(par.get(Dil, '0'))
        self['gecmis'] = Label(par.get(Dil, '121'))
        self['filme_don'] = Label(par.get(Dil, '133'))
        self['tuslar'] = Label(par.get(Dil, '134'))
        self['lokal'] = Label(par.get(Dil, '135'))
        self['indirilen'] = Label(par.get(Dil, '136'))
        self['hdd'] = Label(par.get(Dil, '80'))
        self['cekis'] = Label(par.get(Dil, '131'))
        self['favori'] = Label(par.get(Dil, '1'))
        self.onShown.append(self.show_all)
        self['poster'] = Pixmap()
        self['poster'].hide()
        self.picload = ePicLoad()
        self.picfile = ''
        self.update_desc = True
        self.pass_ok = False
        self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
        self['actions'] = HelpableActionMap(self, 'TURKvodPlayerPlaylis', {'KEY_GREEN': self.taskManager,
         'KEY_GREEN_UZUN': self.turkvodFileList,
         'KEY_EXIT': self.start_history,
         'KEY_EXIT_UZUN': self.start_history_list,
         'KEY_OK': self.ok,
         'KEY_RED': self.exit_box,
         'KEY_CHANNELUP': self.prevPlaylist,
         'KEY_CHANNELDOWN': self.nextPlaylist,
         'KEY_STOP': self.show_more_info,
         'KEY_TV': self.colorfontcolo,
         'KEY_NEXT': self.addChannelToFavorites_box,
         'KEY_PREVIOUS': self.removeChannelFromFavorites_box,
         'KEY_MENU': self.start_portal,
         'KEY_POWER': self.power,
         'KEY_BLUE': self.back_to_video,
         'KEY_TEXT': self.search,
         'KEY_YELLOW': self.module,
         'KEY_INFO_UZUN': self.apla,
         'KEY_VIDEO': self.exportchannels,
         '9': self.kay,
         '8': self.start_history_list,
         '1': self.PageUp,
         '7': self.PageDown,
         '0': self.panikyok,
         '6': self.channel_tv}, -1)
        self.temp_index = 0
        self.temp_channel_list = None
        self.temp_playlistname = None
        self.url_tmp = None
        self.work_with_favorites = False
        self.search_on = None
        self.video_back = False
        self.passwd_ok = False
        self.history_enable = False
        return

    def PageUp(self):
        self['description'].pageUp()

    def PageDown(self):
        self['description'].pageDown()

    def panikyok(self):
        self.liste_vod_id = 0
        TURKVOD.play_vod = False
        self.session.nav.stopService()
        self.session.nav.playService(FIRST_SESSION)
        self.close(self.session.close(self.oldService))

    def channel_tv(self):
        try:
            sel_chan = self.channel_list[self.mlist.getSelectionIndex()]
            if sel_chan[4] != None:
                self.session.openWithCallback(self.channel_tvt, MessageBox, _('%s\n\n' + str(par.get(Dil, '155'))) % sel_chan[1], MessageBox.TYPE_YESNO, timeout=15)
            else:
                self.session.open(MessageBox, ('%s\n\n' + str(par.get(Dil, '156'))) % sel_chan[1], type=MessageBox.TYPE_INFO, timeout=10)
        except Exception as ex:
            print ex
            print '1019 HATA'

        return

    def channel_tvt(self, answer):
        try:
            if answer is True:
                sel_chan = self.channel_list[self.mlist.getSelectionIndex()]
                if sel_chan[4] != None:
                    f = open(PLUGIN_PATH + '/tv', 'a')
                    f.write('<tr>' + sel_chan[1] + '</tr>' + '\n')
                    f.write('<url>' + sel_chan[4] + '</url>' + '\n')
                    f.close()
        except Exception as ex:
            print ex
            print '1019 HATA'

        return

    def exportchannels(self):
        d_chan = TURKVOD.iptv_list[self.index]
        kanal = d_chan[4]
        text = d_chan[1]
        if kanal != '':
            url = kanal
            channelname = text
            error = addstream(url, channelname, 'TURKvod')
            if error == 'none':
                self.session.openWithCallback(self.res_, MessageBox, _('Kanal Bukete Ekledi. Evet: Restart, Hayir: Yeni Kanal Ekle'), MessageBox.TYPE_YESNO)
            else:
                self.session.open(MessageBox, error, type=MessageBox.TYPE_ERROR, timeout=5)

    def colorfontcolo(self):
        self.session.open(RenAy)

    def turkvodFileList(self):
        from Screens.InfoBar import InfoBar
        if InfoBar and InfoBar.instance:
            InfoBar.showMovies(InfoBar.instance)

    def taskManager(self):
        self.session.open(vodeScreen)

    def kay(self):
        if config.plugins.TURKVOD.sifreip.value == False:
            self.session.openWithCallback(self.modulle, InputBox, title=par.get(Dil, '11'), text='****', maxSize=4, type=Input.PIN)
        if config.plugins.TURKVOD.sifreip.value == True:
            self.session.open(plugin_ka)

    def modulle(self, number):
        try:
            a = '%s' % int(number)
            b = '%s' % config.plugins.TURKVOD.csifre.value
            if a == b:
                self.session.open(plugin_ka)
            else:
                self.session.open(MessageBox, par.get(Dil, '12'), type=MessageBox.TYPE_ERROR, timeout=5)
        except Exception as ex:
            print ex

    def addChannelToFavorites_box(self):
        try:
            self.url_tmp = TURKVOD.url
            self.temp_channel_list = self.channel_list
            self.temp_index = self.mlist.getSelectionIndex()
            self.selected_channel = self.channel_list[self.temp_index]
            self.session.openWithCallback(self.addChannelToFavorites, MessageBox, ('%s\n' + str(par.get(Dil, '13'))) % self.selected_channel[1], type=MessageBox.TYPE_YESNO)
        except Exception as ex:
            print ex

    def addChannelToFavorites(self, message = None):
        if message:
            try:
                selected_channel = self.temp_channel_list[self.temp_index]
                TURKVOD.my_favorites.append(selected_channel)
                self.session.open(MessageBox, ('%s\n' + str(par.get(Dil, '14'))) % selected_channel[1], type=MessageBox.TYPE_INFO, timeout=3)
                TURKVOD.write_favorites()
                self.work_with_favorites = True
            except Exception as ex:
                print ex
                print 'HATA'

    def removeChannelFromFavorites_box(self):
        try:
            if TURKVOD.playlistname == par.get(Dil, '1'):
                self.temp_index = self.mlist.getSelectionIndex()
                selected_channel = self.channel_list[self.temp_index]
                self.session.openWithCallback(self.removeChannelFromFavorites, MessageBox, ('%s\n' + str(par.get(Dil, '15'))) % selected_channel[1], type=MessageBox.TYPE_YESNO)
            else:
                self.start_favorites()
        except Exception as ex:
            print ex

    def removeChannelFromFavorites(self, message = None):
        if message:
            try:
                my_temp_fav = []
                selected_channel = self.channel_list[self.temp_index]
                for channel in TURKVOD.iptv_list:
                    if channel != selected_channel:
                        my_temp_fav.append(channel)
                    else:
                        print 'REMOVE'

                TURKVOD.my_favorites = my_temp_fav
                TURKVOD.write_favorites()
                self.iptv_list = my_temp_fav
                TURKVOD.get_list('favorites')
                self.channel_list = TURKVOD.iptv_list
                self.update_channellist()
                self.work_with_favorites = False
                self.session.open(MessageBox, ('%s ' + str(par.get(Dil, '16'))) % selected_channel[1], type=MessageBox.TYPE_INFO, timeout=3)
            except Exception as ex:
                print ex
                print 'HATA'

            print 'END REMOVE'

    def search(self):
        self.url_tmp = TURKVOD.url
        self.search_on = TURKVOD.search_on
        if TURKVOD.search_text != '':
            self.session.openWithCallback(self.searchResult, KeyBoard, title=_(par.get(Dil, '17') + '        [   ' + config.plugins.TURKVOD.klevye.value + '   ]'), text='')
        else:
            self.start_favorites()

    def searchResult(self, message = None):
        if message:
            try:
                TURKVOD.search_string = message
                TURKVOD.search_on = self.search_on
                TURKVOD.get_list(self.url_tmp)
                self.update_channellist()
            except Exception as ex:
                print ex
                print 'ARAMA SONUCU'

    def show_more_info(self):
        selected_channel = self.channel_list[self.mlist.getSelectionIndex()]
        text = re.compile('<[\\/\\!]*?[^<>]*?>')
        text_clear = text.sub('', selected_channel[2])
        self.session.open(MessageBox, text_clear, type=MessageBox.TYPE_INFO)

    def prevPlaylist(self):
        if TURKVOD.prev_page_url != None:
            TURKVOD.get_list(TURKVOD.prev_page_url)
            self.update_channellist()
        return

    def nextPlaylist(self):
        if TURKVOD.next_page_url != None:
            TURKVOD.get_list(TURKVOD.next_page_url)
            self.update_channellist()
        return

    def button_updater(self):
        self['chminus'].setText('')
        self['chplus'].setText('')
        self['stop'].setText('')
        if TURKVOD.next_page_url != None and TURKVOD.next_page_url != '':
            self['chminus'].setText(TURKVOD.next_page_text)
        if TURKVOD.prev_page_url != None and TURKVOD.prev_page_url != '':
            self['chplus'].setText(TURKVOD.prev_page_text[0:23])
        if TURKVOD.search_on != None and TURKVOD.search_on != '':
            self['stop'].setText(TURKVOD.search_text)
        self['playlist'].setText(TURKVOD.playlistname)
        return

    def decodeImage(self):
        x = self['poster'].instance.size().width()
        y = self['poster'].instance.size().height()
        picture = self.picfile
        picload = self.picload
        sc = AVSwitch().getFramebufferScale()
        picload.setPara((x,
         y,
         sc[0],
         sc[1],
         0,
         0,
         'transparent'))
        try:
            l = picload.PictureData.get()
            del l[:]
            l.append(boundFunction(self.showImage))
        except:
            self.picload_conn = self.picload.PictureData.connect(boundFunction(self.showImage))

        picload.startDecode(picture)

    def showImage(self, picInfo = None):
        self['poster'].show()
        try:
            ptr = self.picload.getData()
            if ptr:
                self['poster'].instance.setPixmap(ptr.__deref__())
        except Exception as ex:
            print ex
            print 'HATA showImage'

    def image_downloaded(self, id):
        self.decodeImage()

    def exit_box(self):
        try:
            self.session.openWithCallback(self.exit, MessageBox, _(par.get(Dil, '20')), type=MessageBox.TYPE_YESNO)
        except Exception as ex:
            print ex
            print 'Hata'

    def exit(self, message = None):
        self.liste_vod_id = 0
        TURKVOD.play_vod = False
        if message:
            if TURKVOD.use_rtmpw != False:
                try:
                    cmd = 'killall -9 rtmpgw'
                    os.popen(cmd)
                    debug(cmd)
                except Exception as ex:
                    print ex
                    print 'exit_rtmp'

            if TURKVOD.ar_id_end:
                eAVSwitch.getInstance().setAspectRatio(TURKVOD.ar_id_end)
            else:
                print 'SET A-RATIO OFF'
            if TURKVOD.delete_images != None:
                debug('DELETE .JPG')
                path = config.plugins.TURKVOD.images_tmp_path.value
                cmd = 'rm -f %s/*.jpg' % path
                debug(cmd, 'CMD')
                try:
                    status = os.popen(cmd).read()
                    debug(status, 'delete 1')
                except Exception as ex:
                    print ex
                    print 'ex delete 1'
                    try:
                        result = commands.getoutput(cmd)
                        debug(result, 'delete 2')
                    except Exception as ex:
                        print ex
                        print 'ex delete 2'

            self.session.nav.stopService()
            self.session.nav.playService(FIRST_SESSION)
            self.close(self.session.close(self.oldService))
        return

    def new_debug(self):
        print 'new_debug-----------------------------------------'
        print 'TURKVOD.playlistname           : %s' % TURKVOD.playlistname
        print 'TURKVOD.list_index             : %s' % TURKVOD.list_index
        print 'LEN(TURKVOD.iptv_list)         : %s' % len(TURKVOD.iptv_list)
        print 'self.index                     : %s' % self.index
        print 'self.mlist.getSelectionIndex() : %s' % self.mlist.getSelectionIndex()
        print 'new_debug-----------------------------------------'

    def update_description(self):
        self.index = self.mlist.getSelectionIndex()
        if self.update_desc:
            try:
                self['info'].setText('')
                self['description'].setText('')
                self['poster'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/clear.png')
                selected_channel = self.channel_list[self.index]
                if selected_channel[7] != '':
                    if selected_channel[7].find('http') == -1:
                        self.picfile = PLUGIN_PATH + '/img/' + selected_channel[7]
                        self.decodeImage()
                        print 'LOCAL DESCR IMG'
                    else:
                        if TURKVOD.img_loader == False:
                            self.picfile = '%s/turkvod_tmp_pic.jpg' % config.plugins.TURKVOD.images_tmp_path.value
                        else:
                            m = hashlib.md5()
                            m.update(selected_channel[7])
                            cover_md5 = m.hexdigest()
                            self.picfile = '%s/%s.jpg' % (config.plugins.TURKVOD.images_tmp_path.value, cover_md5)
                        if os.path.exists(self.picfile) == False or TURKVOD.img_loader == False:
                            if TWIST == 1:
                                image_url = selected_channel[7]
                                localfile = self.picfile
                                host = re.findall('//(.*?)/', image_url, re.IGNORECASE)[0]
                                sniFactory = SNIFactory(host)
                                client.downloadPage(image_url, localfile, sniFactory).addCallback(self.image_downloaded)
                            elif selected_channel[7].startswith('https') and config.plugins.TURKVOD.httpsposter.value == True:
                                cookiejar = cookielib.CookieJar()
                                _opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
                                _opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57')]
                                op = _opener.open(selected_channel[7])
                                out_file = open(self.picfile, 'wb')
                                out_file.write(op.read())
                                out_file.close()
                                self.decodeImage()
                            else:
                                downloadPage(selected_channel[7], self.picfile).addCallback(self.image_downloaded)
                        else:
                            self.decodeImage()
                if selected_channel[2] != None:
                    description = selected_channel[2]
                    description_2 = description.split(' #-# ')
                    if description_2:
                        self['description'].setText(description_2[0])
                        if selected_channel[3] != 'search':
                            self['favori'].setText(par.get(Dil, '1'))
                        if selected_channel[3] == 'search':
                            self['favori'].setText(par.get(Dil, '17'))
                        if len(description_2) > 1:
                            self['info'].setText(description_2[1])
                    else:
                        self['description'].setText(description)
            except Exception as ex:
                print ex
                print 'exe update_description'

        return

    def start_portal(self):
        self.index = 0
        TURKVOD.iptv_list_history = []
        TURKVOD.get_list(TURKVOD.startportal)
        self.update_channellist()

    def start_history_list(self):
        self.index = 0
        TURKVOD.get_list('playlist_history')
        self.update_channellist()

    def start_history(self):
        self.index = 0
        if len(TURKVOD.iptv_list_history) <= 1:
            self.exit_box()
        if len(TURKVOD.iptv_list_history) > 2:
            selected_channel = TURKVOD.iptv_list_history[len(TURKVOD.iptv_list_history) - 2]
            del TURKVOD.iptv_list_history[len(TURKVOD.iptv_list_history) - 1]
            playlist_url = selected_channel
            TURKVOD.get_list(playlist_url)
            self.update_channellist()
        else:
            self.start_portal()

    def start_favorites(self):
        self.index = 0
        TURKVOD.get_list('favorites')
        self.update_channellist()

    def module(self):
        self.index = 0
        TURKVOD.get_list('module')
        self.update_channellist()

    def update_channellist(self):
        try:
            print '--------------------- UPDATE CHANNEL LIST ----------------------------------------'
            if TURKVOD.xml_error != '':
                print '### update_channellist ######URL#############'
                print TURKVOD.clear_url
                self.session.open(MessageBox, self.vod, type=MessageBox.TYPE_ERROR, timeout=3)
            self['chminus'].setText('')
            self['chplus'].setText('')
            self['stop'].setText('')
            self.channel_list = TURKVOD.iptv_list
            self.update_desc = False
            self.mlist.setList(map(channelEntryIPTVplaylist, self.channel_list))
            self.mlist.moveToIndex(0)
            self.update_desc = True
            self.update_description()
            self.button_updater()
        except Exception as ex:
            print ex
            print 'HATA'

    def show_all(self):
        try:
            if self.passwd_ok == False:
                self['version'].setText('v. %s' % VERSION)
                if self.video_back == False and TURKVOD.video_status == True and TURKVOD.search_string == '' and self.work_with_favorites == False:
                    debug('SHOW ----- TMP CH LIST')
                    self.load_from_tmp()
                    self.video_back = True
                elif self.work_with_favorites == True and TURKVOD.search_string == '':
                    debug('SHOW ----- FAV LIST')
                    self.index = self.temp_index
                    self.channel_list = self.temp_channel_list
                    TURKVOD.playlistname = self.temp_playlistname
                    self.work_with_favorites = False
                else:
                    debug('SHOW ----- NEW CH LIST')
                    self.channel_list = TURKVOD.iptv_list
                self.mlist.moveToIndex(self.index)
                self.mlist.setList(map(channelEntryIPTVplaylist, self.channel_list))
                self.mlist.selectionEnabled(1)
                self.button_updater()
            self.passwd_ok = False
        except Exception as ex:
            print ex
            print 'HATA'

    def back_to_video(self):
        try:
            if TURKVOD.video_status:
                self.video_back = False
                self.load_from_tmp()
                self.channel_list = TURKVOD.iptv_list
                if TURKVOD.play_vod == True:
                    self.session.open(TURKvodVideoPlayer)
                elif TURKVOD.play_iptv == True:
                    self.session.open(TURKvodVideoPlayer)
        except Exception as ex:
            print ex
            print 'EXC back_to_video'

    def ok(self):
        self.index_tmp = self.mlist.getSelectionIndex()
        if self.banned == True:
            self.session.open(MessageBox, self.banned_text, type=MessageBox.TYPE_ERROR, timeout=5)
        else:
            selected_channel = self.channel_list[self.mlist.getSelectionIndex()]
            TURKVOD.list_index = self.mlist.getSelectionIndex()
            selected_channel = self.channel_list[self.index]
            title = selected_channel[1]
            title = re.compile('<[\\/\\!]*?[^<>]*?>').sub('', title)
            if selected_channel[0] != '[G]':
                title = selected_channel[1]
            selected_channel_history = ('[G]',
             title,
             selected_channel[2],
             selected_channel[3],
             selected_channel[4],
             selected_channel[5],
             selected_channel[6],
             selected_channel[7],
             selected_channel[8],
             selected_channel[9])
            TURKVOD.iptv_list_history_list.append(selected_channel_history)
            self.temp_index = -1
            self.aktar = selected_channel[5]
            if selected_channel[9] != None:
                self.temp_index = self.index
                self.myPassInput()
            else:
                self.ok_checked()
            if selected_channel[3] == 'search':
                self.search()
            if selected_channel[5] == 'USB':
                self.usb_open()
            if selected_channel[5] == 'HDD':
                self.usb_open()
        return

    def ok_checked(self):
        try:
            if self.temp_index > -1:
                self.index = self.temp_index
            selected_channel = TURKVOD.iptv_list[self.index]
            stream_url = selected_channel[4]
            playlist_url = selected_channel[5]
            self.title = selected_channel[1]
            self.resim = selected_channel[7]
            if playlist_url != None:
                TURKVOD.get_list(playlist_url)
                self.update_channellist()
            elif stream_url != None:
                self.set_tmp_list()
                TURKVOD.video_status = True
                TURKVOD.play_vod = False
                self.session.openWithCallback(self.check_standby, TURKvodVideoPlayer)
        except Exception as ex:
            print ex
            print 'ok_checked'

        return

    def usb_open(self):
        try:
            if self.aktar == 'USB':
                hddusb = ''
                hddusb = '/media/usb/'
                xml = '/usb.xml'
                adi = 'TURKvod USB'
                img = '"usb.png"'
            if self.aktar == 'HDD':
                hddusb = ''
                hddusb = '/media/hdd/TURKvodXML/'
                xml = '/hdd.xml'
                adi = 'TURKvod HDD'
                img = '"hdd.png"'
            if os.path.exists(hddusb) == False:
                self.session.open(MessageBox, par.get(Dil, '84'), type=MessageBox.TYPE_ERROR, timeout=5)
            if os.path.exists(hddusb) == True:
                dirusb = hddusb
                for root, dirs, files in os.walk(dirusb, topdown=False):
                    vodfile = open(PLUGIN_PATH + xml, 'w')
                    vodfile.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
                    vodfile.write('<items>\n')
                    vodfile.write('<playlist_name>' + adi + '</playlist_name>\n')
                    for name in files:
                        if name.find('xml') > 0:
                            bilgiler = os.path.join(hddusb, name)
                            vodfile.write('\t<channel>\n')
                            vodfile.write('\t\t\t<title><![CDATA[%s]]></title>\n' % bilgiler.replace(hddusb, '').replace('.xml', '').replace('_', ' ').upper().encode('utf-8'))
                            vodfile.write('\t\t\t<description><![CDATA[<img src=' + img + '>' + adi + ']]></description>\n')
                            vodfile.write('\t\t\t<playlist_url><![CDATA[%s]]></playlist_url>\n' % bilgiler)
                            vodfile.write('\t</channel>\n\n\n')

                    vodfile.write('</items>\n')
                    vodfile.close()
                    self.index = 0
                    if self.aktar == 'USB':
                        TURKVOD.get_list('usb')
                        self.update_channellist()
                    if self.aktar == 'HDD':
                        TURKVOD.get_list('hdd')
                        self.update_channellist()

        except Exception as ex:
            print ex
            print 'USB OKUMA HATASI'

    def myPassInput(self):
        self.passwd_ok = True
        if config.plugins.TURKVOD.sifreip.value == False:
            self.session.openWithCallback(self.checkPasswort, InputBox, title=par.get(Dil, '11'), text='****', maxSize=4, type=Input.PIN)
        if config.plugins.TURKVOD.sifreip.value == True:
            self.ok_checked()

    def checkPasswort(self, number):
        a = '%s' % number
        b = '%s' % config.plugins.TURKVOD.csifre.value
        if a == b:
            debug(self.passwd_ok, 'self.passwd_ok')
            self.ok_checked()
        else:
            self.passwd_ok = False
            self.session.open(MessageBox, par.get(Dil, '12'), type=MessageBox.TYPE_ERROR, timeout=5)

    def play_iptv(self):
        try:
            if self.banned == True:
                self.session.open(MessageBox, self.banned_text, type=MessageBox.TYPE_ERROR, timeout=5)
            else:
                self.set_tmp_list()
                selected_channel = self.channel_list[self.index]
                stream_url = selected_channel[4]
                if stream_url != None:
                    TURKVOD.video_status = True
                    TURKVOD.play_iptv = False
                    self.session.openWithCallback(self.check_standby, TURKvodVideoPlayer)
        except Exception as ex:
            print ex
            print 'MESAJ HATASI'

        return

    def apla(self):
        self.session.open(MessageBox, par.get(Dil, '81') + '  ' + config.plugins.TURKVOD.csifre.value, type=MessageBox.TYPE_INFO, timeout=5)

    def check_standby(self, myparam = None):
        debug(myparam, 'check_standby')
        if myparam:
            self.power()

    def power(self):
        self.session.nav.stopService()
        self.session.open(Standby)

    def res_(self, answer):
        if answer is True:
            self.session.open(TryQuitMainloop, 3)
        else:
            return

    def checker(self):
        print '-----------------------------------------'
        print 'TURKVOD.playlistname           : %s' % TURKVOD.playlistname
        print 'TURKVOD.list_index             : %s' % TURKVOD.list_index
        print 'LEN(TURKVOD.iptv_list)         : %s' % len(TURKVOD.iptv_list)
        print '-----------------------------------------'
        print 'TURKVOD.playlistname_tmp       : %s' % TURKVOD.playlistname_tmp
        print 'TURKVOD.list_index_tmp         : %s' % TURKVOD.list_index_tmp
        print 'LEN(TURKVOD.iptv_list_tmp)     : %s' % len(TURKVOD.iptv_list_tmp)
        print '-----------------------------------------'
        print 'self.mlist.getSelectionIndex() : %s' % self.mlist.getSelectionIndex()
        print 'self.index                     : %s' % self.index
        print 'LEN(self.channel_list)         : %s' % len(self.channel_list)
        print '-----------------------------------------'
        print 'self.temp_index                : %s' % self.temp_index
        print ''
        print ''
        print ''
        print ''

    def set_tmp_list(self):
        self.index = self.mlist.getSelectionIndex()
        TURKVOD.list_index = self.index
        TURKVOD.list_index_tmp = TURKVOD.list_index
        TURKVOD.iptv_list_tmp = TURKVOD.iptv_list
        TURKVOD.playlistname_tmp = TURKVOD.playlistname
        TURKVOD.url_tmp = TURKVOD.url
        TURKVOD.next_page_url_tmp = TURKVOD.next_page_url
        TURKVOD.next_page_text_tmp = TURKVOD.next_page_text
        TURKVOD.prev_page_url_tmp = TURKVOD.prev_page_url
        TURKVOD.prev_page_text_tmp = TURKVOD.prev_page_text
        TURKVOD.search_text_tmp = TURKVOD.search_text
        TURKVOD.search_on_tmp = TURKVOD.search_on

    def load_from_tmp(self):
        debug('load_from_tmp')
        TURKVOD.iptv_list = TURKVOD.iptv_list_tmp
        TURKVOD.list_index = TURKVOD.list_index_tmp
        TURKVOD.playlistname = TURKVOD.playlistname_tmp
        TURKVOD.url = TURKVOD.url_tmp
        TURKVOD.next_page_url = TURKVOD.next_page_url_tmp
        TURKVOD.next_page_text = TURKVOD.next_page_text_tmp
        TURKVOD.prev_page_url = TURKVOD.prev_page_url_tmp
        TURKVOD.prev_page_text = TURKVOD.prev_page_text_tmp
        TURKVOD.search_text = TURKVOD.search_text_tmp
        TURKVOD.search_on = TURKVOD.search_on_tmp
        self.index = TURKVOD.list_index


class m3u8_downloader():

    def __init__(self, m3u8_tulpe, rec_m3u8_url, title):
        self.PauseTimer = eTimer()
        self.PauseTimer.callback.append(self.pause)
        self.m3u8_tulpe = m3u8_tulpe
        self.rec_m3u8_url = rec_m3u8_url
        self.title = title
        self.useragent = "--header='User-Agent: QuickTime/7.6.2 (qtver=7.6.2;os=Windows NT 5.1Service Pack 3)'"
        self.filename = self.title + '.ts'
        self.fm3u8 = open(self.rec_m3u8_url + self.filename, 'wb')
        self.cnt = -1
        self.cntApp = 0
        self.download()

    def download(self):
        self.pause()
        for m3u8_frag in self.m3u8_tulpe:
            self.cnt += 1
            cmd = "wget %s -c '%s' -O '%s/%s'" % (self.useragent,
             m3u8_frag,
             self.rec_m3u8_url,
             'm3u8_tmp-' + str(self.cnt))
            JobManager.AddJob(downloadJob(self, cmd, self.rec_m3u8_url + 'm3u8_tmp-' + str(self.cnt), 'm3u8_tmp-' + str(self.cnt)))

    def m3uAdd(self):
        self.PauseTimer.start(100)
        if os.path.exists(self.rec_m3u8_url + 'm3u8_tmp-' + str(self.cntApp + 1)) == True:
            self.cntApp += 1
            try:
                tmp = open(self.rec_m3u8_url + 'm3u8_tmp-' + str(self.cntApp - 1), 'rb')
                self.fm3u8.write(tmp.read())
                tmp.close()
                os.remove(self.rec_m3u8_url + 'm3u8_tmp-' + str(self.cntApp - 1))
            except Exception as ex:
                print ex

        if self.cntApp >= len(self.m3u8_tulpe) - 1 or len(JobManager.getPendingJobs()) == 0:
            try:
                tmp = open(self.rec_m3u8_url + 'm3u8_tmp-' + str(self.cntApp), 'rb')
                self.fm3u8.write(tmp.read())
                tmp.close()
                os.remove(self.rec_m3u8_url + 'm3u8_tmp-' + str(self.cntApp))
                del self.PauseTimer
                self.fm3u8.close()
            except Exception as ex:
                print ex

    def m3u8_init(self):
        self.PauseTimer.start(100)

    def pause(self):
        self.PauseTimer.stop()
        if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 2:
            self.m3uAdd()
        else:
            self.m3u8_init()


if SUBS == 1:

    class TURKvodVideoPlayer(Screen, InfoBarBase, IPTVInfoBarShowHide, SubsSupport, InfoBarSeek, InfoBarAudioSelection, InfoBarSubtitleSupport):
        fontcolor = fontcolorfont
        menufont = menufontcolor
        menuust = menuustfontcolor
        menufontt = mfont
        aciklamafont = fontaciklama
        if themarengi == 'red':
            if versiyon == 'hd':
                skin = '\n\t\t<screen position="0,460" size="1280,720" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1280,260" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;20" position="460,105" size="100,24" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="245,129" size="14,14" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="40,30" size="130,194" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="RegularTURKvod;20" position="757,199" size="200,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="RegularTURKvod;20" position="280,199" size="200,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="552,199" zPosition="4" size="200,25" halign="left" font="RegularTURKvod;20" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="418,199" size="220,28" font="RegularTURKvod;20" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1160,120" size="150,50" font="TURKvodRegular;36" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbg' + themarengi + '.png" position="268,135" size="800,20" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="268,124" size="800,20" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfg' + themarengi + '.png:800,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="268,105"  size="200,30" zPosition="2" font="RegularTURKvod;22" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="660,105" size="200,30" zPosition="2" font="RegularTURKvod;22" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="968,105" size="100,30" zPosition="2" font="RegularTURKvod;22" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="268,150" size="800,100" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="840,104" size="29,20" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="840,104" size="29,20" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="750,105" size="80,25" halign="right" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="875,105" size="80,25" halign="left" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t</screen>'
            if versiyon == 'fhd':
                skin = '\n\t\t<screen position="0,690" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1920,390" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_fhd' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;30" position="690,158" size="150,36" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="368,194" size="21,21" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="60,45" size="192,291" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="RegularTURKvod;28" position="1136,299" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="RegularTURKvod;28" position="420,299" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="828,299" zPosition="4" size="300,38" halign="left" font="RegularTURKvod;28" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="627,299" size="220,42" font="RegularTURKvod;28" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1740,180" size="225,75" font="TURKvodRegular;54" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbgfhd' + themarengi + '.png" position="402,203" size="1200,30" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="402,186" size="1200,30" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfgfhd' + themarengi + '.png:1200,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="402,158"  size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="990,158" size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="1452,158" size="150,45" zPosition="2" font="RegularTURKvod;28" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="402,225" size="1200,150" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="1260,161" size="44,30" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="1260,161" size="44,30" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1125,158" size="120,38" halign="right" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1313,158" size="120,38" halign="left" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t</screen>'
        if themarengi == 'black' or themarengi == 'seffaf':
            if versiyon == 'hd':
                skin = '\n\t\t<screen position="0,460" size="1280,720" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1280,260" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;20" position="460,105" size="100,24" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="245,130" size="21,21" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="40,30" size="128,194" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="' + menufontt + '" position="854,197" size="300,30"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="' + menufontt + '" position="307,197" size="300,30"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="614,197" zPosition="4" size="300,30" halign="left" font="' + menufontt + '" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="448,197" size="300,30" font="' + menufontt + '" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1160,120" size="225,75" font="TURKvodRegular;36" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbg' + themarengi + '.png" position="268,134" size="800,20" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="268,127" size="800,20" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfg' + themarengi + '.png:800,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="268,105"  size="200,30" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="660,105" size="200,30" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="968,105" size="100,30" zPosition="2" font="RegularTURKvod;20" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="750,105" size="80,26" halign="right" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="875,105" size="80,26" halign="left" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="268,150" size="800,100" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="840,107" size="30,24" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="840,107" size="30,24" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t</screen>'
            if versiyon == 'fhd':
                skin = '\n\t\t<screen position="0,690" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1920,390" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_fhd' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;30" position="690,158" size="150,36" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="368,194" size="21,21" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="60,45" size="192,291" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="' + menufontt + '" position="1280,295" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="' + menufontt + '" position="460,295" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="921,295" zPosition="4" size="300,38" halign="left" font="' + menufontt + '" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="673,295" size="220,42" font="' + menufontt + '" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1740,180" size="225,75" font="TURKvodRegular;54" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbgfhd' + themarengi + '.png" position="402,200" size="1200,30" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="402,186" size="1200,30" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfgfhd' + themarengi + '.png:1200,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="402,158"  size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="990,158" size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="1452,158" size="150,45" zPosition="2" font="RegularTURKvod;28" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="402,225" size="1200,150" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="1260,161" size="44,30" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="1260,161" size="44,30" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1125,158" size="120,38" halign="right" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1313,158" size="120,38" halign="left" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t</screen>'
        if themarengi == 'metrixhd' or versiyon == 'uhd':
            skin = '<screen name="TURKvodVideoPlayer" position="0,0" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(720 * ver_carpan)) + '" title="" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="0,' + str(int(570 * ver_carpan)) + '" zPosition="-2" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(150 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(1081 * ver_carpan)) + ',' + str(int(50 * ver_carpan)) + '" size="' + str(int(169 * ver_carpan)) + ',' + str(int(80 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(60 * ver_carpan)) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1" valign="top">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(921 * ver_carpan)) + ',' + str(int(80 * ver_carpan)) + '" size="' + str(int(148 * ver_carpan)) + ',' + str(int(29 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%e. %b</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(943 * ver_carpan)) + ',' + str(int(54 * ver_carpan)) + '" size="' + str(int(125 * ver_carpan)) + ',' + str(int(30 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%A</convert>\n    </widget>\n    <eLabel name="new eLabel" position="' + str(int(149 * ver_carpan)) + ',' + str(int(670 * ver_carpan)) + '" size="' + str(int(980 * ver_carpan)) + ',' + str(int(1 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" zPosition="-1" />\n    <eLabel position="' + str(int(913 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" zPosition="-1" size="' + str(int(320 * ver_carpan)) + ',' + str(int(70 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="0" />\n    <widget source="session.CurrentService" render="PositionGauge" position="' + str(int(151 * ver_carpan)) + ',' + str(int(667 * ver_carpan)) + '" size="' + str(int(980 * ver_carpan)) + ',' + str(int(7 * ver_carpan)) + '" transparent="1">\n      <convert type="ServicePosition">Gauge</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(40 * ver_carpan)) + ',' + str(int(656 * ver_carpan)) + '" size="' + str(int(100 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(24 * ver_carpan)) + '" halign="right" valign="center" backgroundColor="' + metrixBackground + '" shadowColor="' + metrixBackground + '" shadowOffset="-1,-1" transparent="1">\n      <convert type="ServicePosition">Position</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Progress" position="' + str(int(151 * ver_carpan)) + ',' + str(int(669 * ver_carpan)) + '" size="' + str(int(980 * ver_carpan)) + ',' + str(int(3 * ver_carpan)) + '" backgroundColor="#00dade92" borderWidth="0" transparent="1">\n      <convert type="ServicePosition">Position</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(1138 * ver_carpan)) + ',' + str(int(657 * ver_carpan)) + '" size="' + str(int(100 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(24 * ver_carpan)) + '" halign="left" valign="center" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServicePosition">Remaining</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(3 * ver_carpan)) + ',' + str(int(595 * ver_carpan)) + '" size="' + str(int(137 * ver_carpan)) + ',' + str(int(56 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(40 * ver_carpan)) + '" halign="center" valign="top" backgroundColor="' + metrixBackground + '" transparent="1" foregroundColor="' + str(fontcolor) + '">\n      <convert type="ServicePosition">Length</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(149 * ver_carpan)) + ',' + str(int(595 * ver_carpan)) + '" size="' + str(int(892 * ver_carpan)) + ',' + str(int(56 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(40 * ver_carpan)) + '" valign="top" noWrap="1" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServiceName">Name</convert>\n    </widget>\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_dolby_off_' + versiyon + '.png" position="' + str(int(1051 * ver_carpan)) + ',' + str(int(616 * ver_carpan)) + '" size="' + str(int(64 * ver_carpan)) + ',' + str(int(23 * ver_carpan)) + '" zPosition="1" alphatest="blend" />\n    <widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_dolby_on_' + versiyon + '.png" position="' + str(int(1051 * ver_carpan)) + ',' + str(int(616 * ver_carpan)) + '" size="' + str(int(64 * ver_carpan)) + ',' + str(int(23 * ver_carpan)) + '" zPosition="2" alphatest="blend">\n      <convert type="ServiceInfo">IsMultichannel</convert>\n      <convert type="ConditionalShowHide" />\n    </widget>\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_format_off_' + versiyon + '.png" position="' + str(int(1110 * ver_carpan)) + ',' + str(int(615 * ver_carpan)) + '" size="' + str(int(60 * ver_carpan)) + ',' + str(int(26 * ver_carpan)) + '" zPosition="1" alphatest="blend" />\n    <widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_format_on_' + versiyon + '.png" position="' + str(int(1110 * ver_carpan)) + ',' + str(int(615 * ver_carpan)) + '" size="' + str(int(60 * ver_carpan)) + ',' + str(int(26 * ver_carpan)) + '" zPosition="2" alphatest="blend">\n      <convert type="ServiceInfo">IsWidescreen</convert>\n      <convert type="ConditionalShowHide" />\n    </widget>\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/icon_hd_off_' + versiyon + '.png" position="' + str(int(1188 * ver_carpan)) + ',' + str(int(617 * ver_carpan)) + '" size="' + str(int(49 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="1" alphatest="blend" />\n    <widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/icon_hd_on_' + versiyon + '.png" position="' + str(int(1188 * ver_carpan)) + ',' + str(int(617 * ver_carpan)) + '" size="' + str(int(49 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="2" alphatest="blend">\n      <convert type="ServiceInfo">VideoWidth</convert>\n      <convert type="ValueRange">721,1980</convert>\n      <convert type="ConditionalShowHide" />\n    </widget>\n    <widget source="session.CurrentService" render="Label" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" position="' + str(int(1070 * ver_carpan)) + ',' + str(int(590 * ver_carpan)) + '" size="' + str(int(55 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" halign="right" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServiceInfo">VideoWidth</convert>\n    </widget>\n    <eLabel text="x" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" position="' + str(int(1129 * ver_carpan)) + ',' + str(int(590 * ver_carpan)) + '" size="' + str(int(15 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" halign="center" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget source="session.CurrentService" render="Label" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" position="' + str(int(1146 * ver_carpan)) + ',' + str(int(590 * ver_carpan)) + '" size="' + str(int(55 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" halign="left" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServiceInfo">VideoHeight</convert>\n    </widget>\n  </screen>'
        STATE_IDLE = 0
        STATE_PLAYING = 1
        STATE_PAUSED = 2
        ENABLE_RESUME_SUPPORT = True
        ALLOW_SUSPEND = True

        def __init__(self, session, recorder_sref = None, subtitles = None):
            Screen.__init__(self, session)
            InfoBarBase.__init__(self, steal_current_service=True)
            IPTVInfoBarShowHide.__init__(self)
            SubsSupport.__init__(self, embeddedSupport=True, searchSupport=True)
            InfoBarSeek.__init__(self, actionmap='InfobarSeekActions')
            if TURKVOD.disable_audioselector == False:
                InfoBarAudioSelection.__init__(self)
            self.InfoBar_NabDialog = Label()
            self.session = session
            self.service = None
            self['state'] = Label('')
            self['cont_play'] = Label('')
            self['kaydet'] = Label('')
            self['chplus'] = Label('')
            self['altyazi'] = Label('')
            self['altyazi'].setText(par.get(Dil, '82'))
            self['chplus'].setText(TURKVOD.prev_page_text[0:23])
            self.cont_play = TURKVOD.cont_play
            TURKVOD.play_iptv = False
            self.film_quality = None
            self.video_tulpe = None
            self.recorder_sref = None
            self['cover'] = Pixmap()
            self['pico'] = Pixmap()
            self['tsre'] = Pixmap()
            self.picload = ePicLoad()
            self.picfile = ''
            if recorder_sref:
                self.recorder_sref = recorder_sref
                self.session.nav.playService(recorder_sref)
            else:
                self.vod_entry = TURKVOD.iptv_list[TURKVOD.list_index]
                self.vod_url = self.vod_entry[4]
                self.title = self.vod_entry[1]
                self.descr = self.vod_entry[2]
            print 'evEOF=%d' % iPlayableService.evEOF
            self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
             iPlayableService.evStart: self.__serviceStarted,
             iPlayableService.evEOF: self.__evEOF})
            self['actions'] = HelpableActionMap(self, 'TURKvodPlayerVod', {'KEY_EXIT': self.exit,
             'KEY_INFO': self.show_more_info,
             'KEY_NEXT': self.nextAR,
             'KEY_PREVIOUS': self.prevAR,
             'kayit': self.record,
             'KEY_STOP': self.stopnew,
             'KEY_TV': self.stopnew,
             'KEY_BLUE': self.timeshift_autoplay,
             'KEY_RECORD': self.timeshift,
             'KEY_BLUE': self.autoplay,
             'KEY_CHANNELDOWN': self.prevVideo,
             'KEY_CHANNELUP': self.nextVideo,
             'KEY_GREEN': self.startTS,
             'KEY_VIDEO_UZUN': self.timeshift,
             '0': self.panikyok,
             'KEY_POWER': self.power_off}, -1)
            self.onFirstExecBegin.append(self.play_vod)
            self.onShown.append(self.setCover)
            self.onPlayStateChanged.append(self.__playStateChanged)
            self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
            self.state = self.STATE_PLAYING
            self.timeshift_url = None
            self.timeshift_title = None
            self.onShown.append(self.show_info)
            self.error_message = ''
            self.recEnable = True
            self.Timer = eTimer()
            self.Timer.callback.append(self.TimerFire)
            self['tsenable'] = Label('')
            self['tsenable'].setText('TIME SHIFT')
            self['tsclock'] = Label('')
            self.tvPlay = False
            self.tit = False
            self.on_off = False
            self.decodeImage()
            self.moviefolder = config.plugins.TURKVOD.cachefold.value
            return

        def panikyok(self):
            self.liste_vod_id = 0
            TURKVOD.play_vod = False
            self.session.nav.stopService()
            self.session.nav.playService(FIRST_SESSION)
            self.close(self.session.close(self.oldService))

        def showAfterSeek(self):
            if isinstance(self, IPTVInfoBarShowHide):
                self.doShow()

        def timeshift_autoplay(self):
            if self.timeshift_url:
                try:
                    self.reference = eServiceReference(4097, 0, self.timeshift_url)
                    self.reference.setName(self.timeshift_title)
                    self.session.nav.playService(self.reference)
                except Exception as ex:
                    print ex
                    print 'EXC timeshift 1'

            else:
                if self.cont_play:
                    self.cont_play = False
                    self['cont_play'].setText(par.get(Dil, '21'))
                    self.session.open(MessageBox, par.get(Dil, '22'), type=MessageBox.TYPE_INFO, timeout=3)
                else:
                    self.cont_play = True
                    self['cont_play'].setText(par.get(Dil, '23'))
                    self.session.open(MessageBox, par.get(Dil, '24'), type=MessageBox.TYPE_INFO, timeout=3)
                TURKVOD.cont_play = self.cont_play

        def timeshift(self):
            if self.timeshift_url:
                try:
                    self.reference = eServiceReference(4097, 0, self.timeshift_url)
                    self.reference.setName(self.timeshift_title)
                    self.session.nav.playService(self.reference)
                except Exception as ex:
                    print ex
                    print 'EXC timeshift 2'

        def startTS(self):
            hdd = os.path.isdir('/media/hdd')
            usb = os.path.isdir('/media/usb')
            if hdd == True or usb == True:
                self.startT()
            else:
                self.session.open(MessageBox, par.get(Dil, '98'), type=MessageBox.TYPE_INFO, timeout=3)

        def startT(self):
            self.ar_job()
            if self.ts_progress == None and self.timeshift_url == None and self.vod_url.find('m3u8') < 0:
                self['tsenable'].setText('')
                self.recEnable = False
                self.tvPlay = False
                try:
                    self.session.open(MessageBox, par.get(Dil, '83'), type=MessageBox.TYPE_INFO, timeout=3)
                    self.session.nav.stopService()
                    filename = 'TURKvod'
                    self.timeshift_url = TURKVOD.moviefolder + filename + '.ts'
                    if os.path.exists(self.timeshift_url) == True:
                        os.remove(self.timeshift_url)
                    self.timeshift_title = '[TS] ' + self.title
                    cmd = "wget -c '%s' -O '%s'" % (self.vod_url, self.timeshift_url)
                    print 'cmd ', str(cmd)
                    JobManager.AddJob(downloadJob(self, cmd, self.timeshift_url, self.title))
                    self.counter = 0
                    self.TimerFire()
                except Exception as ex:
                    print ex
                    print 'ERROR TS'

            elif self.vod_url.find('m3u8') > -1:
                self['tsenable'].setText('')
                self['tsclock'].setText('3')
                self.recEnable = False
                self.tvPlay = False
                try:
                    self.session.open(MessageBox, 'TimeShift running Please wait', type=MessageBox.TYPE_INFO, timeout=3)
                    self.session.nav.stopService()
                    useragent = "--header='User-Agent: QuickTime/7.6.2 (qtver=7.6.2;os=Windows NT 5.1Service Pack 3)'"
                    filename = 'TURKvod'
                    self.timeshift_url = TURKVOD.moviefolder + filename
                    if os.path.exists(self.timeshift_url) == True:
                        os.remove(self.timeshift_url)
                    self.timeshift_title = '[TS] ' + self.title
                    self.m3u8_tulpe = self.m3u8_descriptor()
                    if len(self.m3u8_tulpe) > 0:
                        m3u8_downloader(self.m3u8_tulpe, TURKVOD.moviefolder, filename)
                    self.counter = 0
                    self.TimerFire()
                except Exception as ex:
                    print ex
                    print 'ERROR m3u8 TS'

            else:
                try:
                    self.session.openWithCallback(stopnew, MessageBox, par.get(Dil, '79'), type=MessageBox.TYPE_YESNO)
                except Exception as ex:
                    print ex

            return

        def run_m3u8_shift(self):
            self.counter += 1
            self.Timer.startLongTimer(3)
            try:
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 1:
                    self['tsclock'].setText('2')
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 2:
                    self['tsclock'].setText('1')
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 3:
                    self['tsclock'].setText('0')
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 4:
                    self['tsclock'].setText('')
                    self.tsPlay = True
                    self.timeshift()
                    del self.Timer
            except Exception as ex:
                print ex

        def TimerFire(self):
            self.counter += 1
            self.Timer.stop()
            if self.vod_url.find('m3u8') > -1:
                self.run_m3u8_shift()
            else:
                self.getTaskProgress()

        def ar_job(self):
            self.ts_progress = None
            for job in JobManager.getPendingJobs():
                self.ts_progress = job.progress

            return

        def getTaskProgress(self):
            self.ar_job()
            if self.ts_progress != None:
                self['state'].setText('TS = ' + str(self.ts_progress) + ' % ' + self.seekstate[3])
                if self.counter > int(TURKVOD.use_ts_percent) and self.tvPlay == False:
                    self.tvPlay = True
                    self.timeshift()
                self.Timer.startLongTimer(1)
            else:
                del self.Timer
                self['state'].setText('TS = 100 % ' + self.seekstate[3])
            return

        def autoplay(self):
            if self.timeshift_url == None:
                if self.cont_play:
                    self.cont_play = False
                    self['cont_play'].setText(par.get(Dil, '21'))
                    self.session.open(MessageBox, par.get(Dil, '22'), type=MessageBox.TYPE_INFO, timeout=3)
                else:
                    self.cont_play = True
                    self['cont_play'].setText(par.get(Dil, '23'))
                    self.session.open(MessageBox, par.get(Dil, '24'), type=MessageBox.TYPE_INFO, timeout=3)
                TURKVOD.cont_play = self.cont_play
            return

        def show_info(self):
            if TURKVOD.play_vod == True:
                self['state'].setText(par.get(Dil, '27'))
                self['kaydet'].setText(par.get(Dil, '142'))
                self['pico'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/ico_mp_play.png')
            self.hideTimer.start(1000, True)
            if self.cont_play:
                self['cont_play'].setText(par.get(Dil, '23'))
            else:
                self['cont_play'].setText(par.get(Dil, '21'))

        def playnextvideo_box(self):
            index = TURKVOD.list_index + 1
            video_counter = len(TURKVOD.iptv_list)
            if index < video_counter and TURKVOD.iptv_list[index][4] != None:
                descr = ''
                if TURKVOD.iptv_list[index][2]:
                    descr = TURKVOD.iptv_list[index][2]
                title = TURKVOD.iptv_list[index][1] + '\n\n' + str(descr)
                self.session.openWithCallback(self.playnextvideo, MessageBox, _(par.get(Dil, '24') + '\n%s') % title, type=MessageBox.TYPE_YESNO)
            return

        def playnextvideo(self, message = None):
            if message:
                try:
                    self.nextVideo()
                except Exception as ex:
                    print ex
                    print 'EXC playnextvideo'

        def nextVideo(self):
            if self.timeshift_url == None:
                try:
                    index = TURKVOD.list_index + 1
                    video_counter = len(TURKVOD.iptv_list)
                    if index < video_counter:
                        if TURKVOD.iptv_list[index][4] != None:
                            TURKVOD.list_index = index
                            self.player_helper()
                except Exception as ex:
                    print ex
                    print 'EXC nextVideo'

            return

        def prevVideo(self):
            if self.timeshift_url == None:
                try:
                    index = TURKVOD.list_index - 1
                    if index > -1:
                        if TURKVOD.iptv_list[index][4] != None:
                            TURKVOD.list_index = index
                            self.player_helper()
                except Exception as ex:
                    print ex
                    print 'EXC prevVideo'

            return

        def player_helper(self):
            self.show_info()
            if self.vod_entry:
                self.vod_entry = TURKVOD.iptv_list[TURKVOD.list_index]
                self.vod_url = self.vod_entry[4]
                self.title = self.vod_entry[1]
                self.descr = self.vod_entry[2]
            self.session.nav.stopService()
            TURKVOD.play_vod = False
            TURKVOD.list_index_tmp = TURKVOD.list_index
            self.setCover()
            self.play_vod()

        def setCover(self):
            try:
                vod_entry = TURKVOD.iptv_list[TURKVOD.list_index]
                self['cover'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/clear.png')
                if self.vod_entry[7] != '':
                    if vod_entry[7].find('http') == -1:
                        self.picfile = PLUGIN_PATH + '/img/' + vod_entry[3]
                        self.decodeImage()
                        print 'LOCAL IMG VOD'
                    else:
                        if TURKVOD.img_loader == False:
                            self.picfile = '%s/turkvod_tmp_pic.jpg' % config.plugins.TURKVOD.images_tmp_path.value
                        else:
                            m = hashlib.md5()
                            m.update(self.vod_entry[7])
                            cover_md5 = m.hexdigest()
                            self.picfile = '%s/%s.jpg' % (config.plugins.TURKVOD.images_tmp_path.value, cover_md5)
                        if os.path.exists(self.picfile) == False or TURKVOD.img_loader == False:
                            if TWIST == 1:
                                image_url = self.vod_entry[7]
                                localfile = self.picfile
                                host = re.findall('//(.*?)/', image_url, re.IGNORECASE)[0]
                                sniFactory = SNIFactory(host)
                                client.downloadPage(image_url, localfile, sniFactory).addCallback(self.image_downloaded).addErrback(self.image_error)
                            elif self.vod_entry[7].startswith('https') and config.plugins.TURKVOD.httpsposter.value == True:
                                cookiejar = cookielib.CookieJar()
                                _opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
                                _opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57')]
                                op = _opener.open(self.vod_entry[7])
                                out_file = open(self.picfile, 'wb')
                                out_file.write(op.read())
                                out_file.close()
                                self.decodeImage()
                            else:
                                downloadPage(self.vod_entry[7], self.picfile).addCallback(self.image_downloaded).addErrback(self.image_error)
                        else:
                            self.decodeImage()
            except Exception as ex:
                print ex
                print 'update COVER'

        def decodeImage(self):
            try:
                x = self['cover'].instance.size().width()
                y = self['cover'].instance.size().height()
                picture = self.picfile
                picload = self.picload
                sc = AVSwitch().getFramebufferScale()
                picload.setPara((x,
                 y,
                 sc[0],
                 sc[1],
                 0,
                 0,
                 'transparent'))
                l = picload.PictureData.get()
                del l[:]
                l.append(boundFunction(self.showImage))
                picload.startDecode(picture)
            except Exception as ex:
                print ex
                print 'ERROR decodeImage'

        def showImage(self, picInfo = None):
            self['cover'].show()
            try:
                ptr = self.picload.getData()
                if ptr:
                    self['cover'].instance.setPixmap(ptr.__deref__())
            except Exception as ex:
                print ex
                print 'ERROR showImage'

        def image_downloaded(self, id):
            self.decodeImage()

        def image_error(self, id):
            i = 0

        def record(self):
            if self.vod_url.find('m3u8') < 0:
                if self.recEnable == True:
                    try:
                        self.session.open(MessageBox, par.get(Dil, '25'), type=MessageBox.TYPE_INFO, timeout=3)
                        self.session.nav.stopService()
                        self['state'].setText(par.get(Dil, '137'))
                        ende = str(self.vod_url.split('.')[-1].lower())
                        if ende != 'mp4' or ende != 'flv' or ende != 'ts' or ende != 'avi' or ende != 'mkv' or ende != 'wmv':
                            ende = 'mp4'
                        today = datetime.fromtimestamp(time()).strftime('[%d.%m_%H:%M:%S]')
                        title_translit = cyr2lat(self.title)
                        filename = today + ASCIItranslit.legacyEncode(title_translit + '.') + ende
                        cmd = "wget -c '%s' -O '%s%s'" % (self.vod_url, TURKVOD.moviefolder, filename)
                        print 'cmd ', cmd
                        JobManager.AddJob(downloadJob(self, cmd, TURKVOD.moviefolder + filename, self.title))
                        self.createMetaFile(filename)
                        self.LastJobView()
                        self.timeshift_url = TURKVOD.moviefolder + filename
                        self.timeshift_title = '[REC] ' + self.title
                        TURKVOD.play_vod = False
                        self.close()
                    except Exception as ex:
                        print ex
                        print 'ERROR record'

                else:
                    self.session.openWithCallback(self.exit, MessageBox, ' TimeShift calisiyor, durdurulsunmu?', type=MessageBox.TYPE_YESNO)
            elif self.recEnable == True:
                try:
                    self.session.open(MessageBox, 'REC ON', type=MessageBox.TYPE_INFO, timeout=3)
                    today = datetime.fromtimestamp(time()).strftime('%d.%m_%H:%M:%S - ')
                    self.m3u8_tulpe = self.m3u8_descriptor()
                    if len(self.m3u8_tulpe) > 0:
                        self.session.nav.stopService()
                        self.session.nav.playService(FIRST_SESSION)
                        ende = str(self.m3u8_tulpe[0].split('.')[-1].lower())
                        filename = today + self.title + '.' + ende
                        m3u8_downloader(self.m3u8_tulpe, TURKVOD.moviefolder, self.title)
                        TURKVOD.play_vod = False
                        self.close()
                except Exception as ex:
                    print ex
                    print 'ERROR m3u8 record'

        def m3u8_descriptor(self):
            m3u8_tulpe = []
            m3u8_tulpe_tmp = []
            url_m3u8 = ''
            try:
                m3u8_split = self.vod_url.split('/')[:-1]
                for m3u8_frag in m3u8_split:
                    url_m3u8 = url_m3u8 + (m3u8_frag + '/')

                req = urllib2.Request(url=self.vod_url, data=None, headers={'User-agent': 'QuickTime/7.6.2 (qtver=7.6.2;os=Windows NT 5.1 Service Pack 3)'})
                resp = urllib2.urlopen(req)
                m3u8page = resp.read()
                fragmented = re.findall('#EXTINF:(.*),.*', m3u8page)
                if fragmented:
                    m3u8_tulpe_tmp = re.findall('#EXTINF:.*\\s(.*)', m3u8page)
                    if m3u8_tulpe_tmp[0].find('http') < 0:
                        for tulpe in m3u8_tulpe_tmp:
                            m3u8_tulpe.append(url_m3u8 + tulpe)

                    else:
                        m3u8_tulpe = m3u8_tulpe_tmp
                else:
                    m3u8_tulpe = []
                return m3u8_tulpe
            except Exception as ex:
                print ex

            return

        def LastJobView(self):
            currentjob = None
            for job in JobManager.getPendingJobs():
                currentjob = job

            if currentjob is not None:
                self.session.open(JobView, currentjob)
            return

        def createMetaFile(self, filename):
            try:
                text = re.compile('<[\\/\\!]*?[^<>]*?>')
                text_clear = ''
                if self.vod_entry[2] != None:
                    text_clear = text.sub('', self.vod_entry[2])
                serviceref = eServiceReference(4097, 0, TURKVOD.moviefolder + filename)
                metafile = open('%s/%s.meta' % (TURKVOD.moviefolder, filename), 'w')
                metafile.write('%s\n%s\n%s\n%i\n' % (serviceref.toString(),
                 self.title.replace('\n', ''),
                 text_clear.replace('\n', ''),
                 time()))
                metafile.close()
            except Exception as ex:
                print ex
                print 'ERROR metaFile'

            return

        def __evEOF(self):
            if self.timeshift_url == None:
                if self.cont_play:
                    self.nextVideo()
                else:
                    self.playnextvideo_box()
            return

        def __seekableStatusChanged(self):
            print 'seekable status changed!'

        def __serviceStarted(self):
            self['state'].setText(' ' + par.get(Dil, '27'))
            self['cont_play'].setText(par.get(Dil, '28'))
            self.state = self.STATE_PLAYING

        def doEofInternal(self, playing):
            if not self.execing:
                return
            if not playing:
                return
            print 'doEofInternal EXIT OR NEXT'

        def exit(self):
            if self.timeshift_url:
                self.session.openWithCallback(self.stops, MessageBox, par.get(Dil, '79'), type=MessageBox.TYPE_YESNO)
            else:
                self.close()

        def stopnew(self):
            if self.timeshift_url:
                self.session.openWithCallback(self.stops, MessageBox, par.get(Dil, '79'), type=MessageBox.TYPE_YESNO)
            else:
                self.session.nav.stopService()
                TURKVOD.play_vod = False
                print 'FIRST_SESSION'
                self.session.nav.playService(FIRST_SESSION)
                self.close(None)
            return

        def stops(self, message = None):
            if message:
                self.on_off = False
                job = None
                for currentjob in JobManager.getPendingJobs():
                    job = currentjob
                    if job is not None:
                        Job.cancel(job)

                if self.timeshift_url:
                    self.BgFileEraser = eBackgroundFileEraser.getInstance()
                    self.BgFileEraser.erase(self.timeshift_url)
                    self.timeshift_url = None
                    self.timeshift_title = None
                self.session.nav.stopService()
                TURKVOD.play_vod = False
                print 'FIRST_SESSION'
                self.session.nav.playService(FIRST_SESSION)
                self.close(None)
            return

        def nextAR(self):
            message = nextAR()
            self.session.open(MessageBox, message, type=MessageBox.TYPE_INFO, timeout=3)

        def prevAR(self):
            message = prevAR()
            self.session.open(MessageBox, message, type=MessageBox.TYPE_INFO, timeout=3)

        def show_more_info(self):
            self.session.open(MessageBox, self.vod_url, type=MessageBox.TYPE_INFO)

        def __playStateChanged(self, state):
            self.hideTimer.start(1000, True)
            print 'self.seekstate[3] ' + self.seekstate[3]
            text = ' ' + self.seekstate[3]
            if self.seekstate[3] == '>':
                text = ' ' + par.get(Dil, '27')
                self['pico'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/ico_mp_play.png')
            if self.seekstate[3] == '||':
                text = par.get(Dil, '29')
                self['pico'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/ico_mp_pause.png')
            if self.seekstate[3] == '>> 2x':
                text = '    x2     >>'
            if self.seekstate[3] == '>> 4x':
                text = '    x4     >>'
            if self.seekstate[3] == '>> 8x':
                text = '    x8     >>'
            self['state'].setText(text)

        def quality_selector(self):
            try:
                self.session.openWithCallback(self.cbSelectQuality, turkQuality, film_quality=self.film_quality)
            except Exception as ex:
                print ex
                print 'q_selector'

        def cbSelectQuality(self, position = None):
            print 'cbSelectQuality'
            print self.vod_url
            try:
                if position > -1:
                    print 'position*** ', position
                    if self.vod_url.find('.m3u8') > 0:
                        self.vod_url = self.video_tulpe[position]
                        self.title = self.title + ' m3u8:' + self.film_quality[position]
                        self.reference = eServiceReference(4097, 0, self.vod_url)
                        self.reference.setName(self.title)
                        try:
                            self.session.nav.playService(self.reference)
                        except Exception as ex:
                            print ex

                    elif self.film_quality:
                        self.vod_url = self.video_tulpe[position]
                        self.title = self.title + self.film_quality[position]
                        parts = self.vod_url.split('|', 1)
                        self.vod_url = parts[0]
                        if len(parts) > 1:
                            config.mediaplayer.extraHeaders = NoSave(ConfigText(default=''))
                            config.mediaplayer.extraHeaders.setValue('')
                            headersString = str(parts[1])
                            print '***self.headersString:***' + headersString
                            config.mediaplayer.extraHeaders.setValue(headersString)
                        self.reference = eServiceReference(4097, 0, self.vod_url)
                        self.reference.setName(self.title)
                        try:
                            self.session.nav.playService(self.reference)
                        except Exception as ex:
                            print ex

                    else:
                        self.title = self.title + '**'
                        self.reference = eServiceReference(4097, 0, self.vod_url)
                        self.reference.setName(self.title)
                        try:
                            self.session.nav.playService(self.reference)
                        except Exception as ex:
                            print 'vod play error 11'
                            print ex

                elif self.vod_url:
                    print 'position yok', self.vod_url
                    self.title = self.title + '**'
                    self.reference = eServiceReference(4097, 0, self.vod_url)
                    self.reference.setName(self.title)
                    try:
                        self.session.nav.playService(self.reference)
                    except Exception as ex:
                        print 'vod play error 11'
                        print ex

                else:
                    print 'position yok', position
                    self.exit()
            except Exception as ex:
                print ex
                print 'vod play error 2'

        def play_vod(self):
            try:
                if TURKVOD.play_vod == False or TURKVOD.play_iptv == True:
                    TURKVOD.play_vod = True
                    self.vod_url = str(self.vod_url)
                    self.vod_url = self.parse_url()
                    print 'self.vod_url:' + str(self.vod_url)
                    if len(self.film_quality) >= 1:
                        self.quality_selector()
                    else:
                        try:
                            if self.vod_url != '' and self.vod_url != None and len(self.vod_url) > 5:
                                print '--->' + self.vod_url + '<------'
                                try:
                                    parts = self.vod_url.split('|', 1)
                                    vurl = parts[0]
                                    config.mediaplayer.extraHeaders = NoSave(ConfigText(default=''))
                                    config.mediaplayer.extraHeaders.setValue('')
                                    if len(parts) > 1:
                                        headersString = str(parts[1])
                                        print 'self.headersString:' + headersString
                                        config.mediaplayer.extraHeaders.setValue(headersString)
                                    if vurl.find('127.0.0.1') > 0:
                                        self.reference = eServiceReference(vurl.replace('http://127.0.0.1:8001/', ''))
                                        self.reference.setName(self.title)
                                        self.session.nav.playService(self.reference)
                                    else:
                                        self.reference = eServiceReference(4097, 0, vurl)
                                        self.reference.setName(self.title)
                                        self.session.nav.playService(self.reference)
                                except Exception as ex:
                                    print 'oynatma hatasi'
                                    print ex

                            else:
                                if self.error_message:
                                    self.session.open(MessageBox, self.error_message.encode('utf-8'), type=MessageBox.TYPE_ERROR)
                                else:
                                    self.session.open(MessageBox, par.get(Dil, '30').encode('utf-8'), type=MessageBox.TYPE_ERROR)
                                self.close()
                        except Exception as ex:
                            print 'vod play error 2'
                            print ex

            except Exception as ex:
                print 'vod play error 0'
                print ex

            return

        def parse_url(self):
            if TURKVOD.playhack != '':
                self.vod_url = TURKVOD.playhack
            print '++++++++++parse_url+++++++++++'
            print 'self.vod_url', self.vod_url
            try:
                self.video_tulpe = []
                self.film_quality = []
                play_url = TURKVOD_PARSER.get_parsed_link(self.vod_url)
                print 'solved :', play_url
                if play_url:
                    if type(play_url) == str:
                        self.vod_url = play_url
                    elif type(play_url) == tuple:
                        if play_url[0]:
                            self.error_message = play_url[0]
                            self.vod_url = 'none'
                        else:
                            self.video_tulpe = play_url[1]
                            self.film_quality = play_url[2]
            except Exception as ex:
                print 'ERROR+++++++++++++++++parse_url++++++++++++++++++++++ERROR'
                print ex

            debug(self.vod_url, '#### self.vod_url ####')
            print 'video_tulpe: ', self.video_tulpe
            print 'film_quality: ', self.film_quality
            if self.error_message == True:
                self.session.open(MessageBox, par.get(Dil, '30').encode('utf-8'), type=MessageBox.TYPE_ERROR)
                self.close()
            else:
                return self.vod_url

        def power_off(self):
            self.close(1)


if SUBS == 0:

    class TURKvodVideoPlayer(Screen, InfoBarBase, IPTVInfoBarShowHide, InfoBarSeek, InfoBarAudioSelection, InfoBarSubtitleSupport):
        fontcolor = fontcolorfont
        menufont = menufontcolor
        menuust = menuustfontcolor
        menufontt = mfont
        aciklamafont = fontaciklama
        if themarengi == 'red':
            if versiyon == 'hd':
                skin = '\n\t\t<screen position="0,460" size="1280,720" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1280,260" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;20" position="460,105" size="100,24" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="245,129" size="14,14" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="40,30" size="130,194" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="RegularTURKvod;20" position="757,199" size="200,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="RegularTURKvod;20" position="280,199" size="200,25"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="552,199" zPosition="4" size="200,25" halign="left" font="RegularTURKvod;20" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="418,199" size="220,28" font="RegularTURKvod;20" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1160,120" size="150,50" font="TURKvodRegular;36" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbg' + themarengi + '.png" position="268,135" size="800,20" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="268,124" size="800,20" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfg' + themarengi + '.png:800,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="268,105"  size="200,30" zPosition="2" font="RegularTURKvod;22" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="660,105" size="200,30" zPosition="2" font="RegularTURKvod;22" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="968,105" size="100,30" zPosition="2" font="RegularTURKvod;22" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="268,150" size="800,100" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="840,104" size="29,20" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="840,104" size="29,20" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="750,105" size="80,25" halign="right" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="875,105" size="80,25" halign="left" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t</screen>'
            if versiyon == 'fhd':
                skin = '\n\t\t<screen position="0,690" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1920,390" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_fhd' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;30" position="690,158" size="150,36" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="368,194" size="21,21" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="60,45" size="192,291" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="RegularTURKvod;28" position="1136,299" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="RegularTURKvod;28" position="420,299" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="828,299" zPosition="4" size="300,38" halign="left" font="RegularTURKvod;28" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="627,299" size="220,42" font="RegularTURKvod;28" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1740,180" size="225,75" font="TURKvodRegular;54" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbgfhd' + themarengi + '.png" position="402,203" size="1200,30" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="402,186" size="1200,30" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfgfhd' + themarengi + '.png:1200,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="402,158"  size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="990,158" size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="1452,158" size="150,45" zPosition="2" font="RegularTURKvod;28" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="402,225" size="1200,150" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="1260,161" size="44,30" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="1260,161" size="44,30" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1125,158" size="120,38" halign="right" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1313,158" size="120,38" halign="left" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t</screen>'
        if themarengi == 'black' or themarengi == 'seffaf':
            if versiyon == 'hd':
                skin = '\n\t\t<screen position="0,460" size="1280,720" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1280,260" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;20" position="460,105" size="100,24" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="245,130" size="21,21" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="40,30" size="128,194" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="' + menufontt + '" position="854,197" size="300,30"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="' + menufontt + '" position="307,197" size="300,30"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="614,197" zPosition="4" size="300,30" halign="left" font="' + menufontt + '" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="448,197" size="300,30" font="' + menufontt + '" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1160,120" size="225,75" font="TURKvodRegular;36" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbg' + themarengi + '.png" position="268,134" size="800,20" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="268,127" size="800,20" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfg' + themarengi + '.png:800,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="268,105"  size="200,30" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="660,105" size="200,30" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="968,105" size="100,30" zPosition="2" font="RegularTURKvod;20" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="750,105" size="80,26" halign="right" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="875,105" size="80,26" halign="left" font="TURKvodRegular;20" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="268,150" size="800,100" zPosition="2" font="RegularTURKvod;20" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="840,107" size="30,24" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="840,107" size="30,24" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t</screen>'
            if versiyon == 'fhd':
                skin = '\n\t\t<screen position="0,690" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder" title="">\n\t\t\t<ePixmap position="0,0" size="1920,390" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/info_fhd' + themarengi + '.png" zPosition="0" transparent="1" alphatest="blend" />\n\t\t\t<widget name="state" font="TURKvodRegular;30" position="690,158" size="150,36" transparent="1" backgroundColor="#21000000" foregroundColor="#e6c15c" halign="left" zPosition="10" />\n\t\t\t<widget name="pico" position="368,194" size="21,21" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="cover" position="60,45" size="192,291" zPosition="1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="altyazi" font="' + menufontt + '" position="1280,295" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="kaydet" font="' + menufontt + '" position="460,295" size="300,38"  zPosition="4" transparent="2" foregroundColor="' + str(fontcolor) + '" backgroundColor="#21000000"/>\n\t\t\t<widget name="cont_play" position="921,295" zPosition="4" size="300,38" halign="left" font="' + menufontt + '" foregroundColor="' + str(fontcolor) + '" transparent="1" backgroundColor="background" text="" />\n\t\t\t<widget name="tsenable" backgroundColor="#00000000" zPosition="1" transparent="1" foregroundColor="' + str(fontcolor) + '" position="673,295" size="220,42" font="' + menufontt + '" halign="left" />\n\t\t\t<widget source="global.CurrentTime" render="Label" position="1740,180" size="225,75" font="TURKvodRegular;54" halign="left" zPosition="2" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ClockToText">Format:%H:%M</convert>\n\t\t\t</widget>\n\t\t\t<ePixmap  pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hbgfhd' + themarengi + '.png" position="402,200" size="1200,30" zPosition="1" />\n\t\t\t<widget source="session.CurrentService" render="PositionGauge" backgroundColor="#f39400" position="402,186" size="1200,30" zPosition="2" pointer="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/slider_1280x10_hfgfhd' + themarengi + '.png:1200,0" transparent="1">\n\t\t\t<convert type="ServicePosition">Gauge</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="402,158"  size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Position</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="990,158" size="300,45" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Length</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#ffffff" render="Label" position="1452,158" size="150,45" zPosition="2" font="RegularTURKvod;28" halign="right" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServicePosition">Remaining</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" foregroundColor="#e6c15c" render="Label" position="402,225" size="1200,150" zPosition="2" font="RegularTURKvod;28" halign="left" backgroundColor="#21000000" transparent="1">\n\t\t\t<convert type="ServiceName">Name</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_off.png" \tposition="1260,161" size="44,30" zPosition="1" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">0,720</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_hd_on.png" \tposition="1260,161" size="44,30" zPosition="2" alphatest="blend">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t<convert type="ValueRange">721,1980</convert>\n\t\t\t<convert type="ConditionalShowHide" />\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1125,158" size="120,38" halign="right" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoWidth</convert>\n\t\t\t</widget>\n\t\t\t<widget source="session.CurrentService" render="Label" zPosition="4" position="1313,158" size="120,38" halign="left" font="TURKvodRegular;30" foregroundColor="#e6c15c" transparent="1" backgroundColor="background">\n\t\t\t<convert type="ServiceInfo">VideoHeight</convert>\n\t\t\t</widget>\n\t\t</screen>'
        if themarengi == 'metrixhd' or versiyon == 'uhd':
            skin = '<screen name="TURKvodVideoPlayer" position="0,0" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(720 * ver_carpan)) + '" title="" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="0,' + str(int(570 * ver_carpan)) + '" zPosition="-2" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(150 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(1081 * ver_carpan)) + ',' + str(int(50 * ver_carpan)) + '" size="' + str(int(169 * ver_carpan)) + ',' + str(int(80 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(60 * ver_carpan)) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1" valign="top">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(921 * ver_carpan)) + ',' + str(int(80 * ver_carpan)) + '" size="' + str(int(148 * ver_carpan)) + ',' + str(int(29 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%e. %b</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(943 * ver_carpan)) + ',' + str(int(54 * ver_carpan)) + '" size="' + str(int(125 * ver_carpan)) + ',' + str(int(30 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%A</convert>\n    </widget>\n    <eLabel name="new eLabel" position="' + str(int(149 * ver_carpan)) + ',' + str(int(670 * ver_carpan)) + '" size="' + str(int(980 * ver_carpan)) + ',' + str(int(1 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" zPosition="-1" />\n    <eLabel position="' + str(int(913 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" zPosition="-1" size="' + str(int(320 * ver_carpan)) + ',' + str(int(70 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="0" />\n    <widget source="session.CurrentService" render="PositionGauge" position="' + str(int(151 * ver_carpan)) + ',' + str(int(667 * ver_carpan)) + '" size="' + str(int(980 * ver_carpan)) + ',' + str(int(7 * ver_carpan)) + '" transparent="1">\n      <convert type="ServicePosition">Gauge</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(40 * ver_carpan)) + ',' + str(int(656 * ver_carpan)) + '" size="' + str(int(100 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(24 * ver_carpan)) + '" halign="right" valign="center" backgroundColor="' + metrixBackground + '" shadowColor="' + metrixBackground + '" shadowOffset="-1,-1" transparent="1">\n      <convert type="ServicePosition">Position</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Progress" position="' + str(int(151 * ver_carpan)) + ',' + str(int(669 * ver_carpan)) + '" size="' + str(int(980 * ver_carpan)) + ',' + str(int(3 * ver_carpan)) + '" backgroundColor="#00dade92" borderWidth="0" transparent="1">\n      <convert type="ServicePosition">Position</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(1138 * ver_carpan)) + ',' + str(int(657 * ver_carpan)) + '" size="' + str(int(100 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(24 * ver_carpan)) + '" halign="left" valign="center" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServicePosition">Remaining</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(3 * ver_carpan)) + ',' + str(int(595 * ver_carpan)) + '" size="' + str(int(137 * ver_carpan)) + ',' + str(int(56 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(40 * ver_carpan)) + '" halign="center" valign="top" backgroundColor="' + metrixBackground + '" transparent="1" foregroundColor="' + str(fontcolor) + '">\n      <convert type="ServicePosition">Length</convert>\n    </widget>\n    <widget source="session.CurrentService" render="Label" position="' + str(int(149 * ver_carpan)) + ',' + str(int(595 * ver_carpan)) + '" size="' + str(int(892 * ver_carpan)) + ',' + str(int(56 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(40 * ver_carpan)) + '" valign="top" noWrap="1" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServiceName">Name</convert>\n    </widget>\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_dolby_off_' + versiyon + '.png" position="' + str(int(1051 * ver_carpan)) + ',' + str(int(616 * ver_carpan)) + '" size="' + str(int(64 * ver_carpan)) + ',' + str(int(23 * ver_carpan)) + '" zPosition="1" alphatest="blend" />\n    <widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_dolby_on_' + versiyon + '.png" position="' + str(int(1051 * ver_carpan)) + ',' + str(int(616 * ver_carpan)) + '" size="' + str(int(64 * ver_carpan)) + ',' + str(int(23 * ver_carpan)) + '" zPosition="2" alphatest="blend">\n      <convert type="ServiceInfo">IsMultichannel</convert>\n      <convert type="ConditionalShowHide" />\n    </widget>\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_format_off_' + versiyon + '.png" position="' + str(int(1110 * ver_carpan)) + ',' + str(int(615 * ver_carpan)) + '" size="' + str(int(60 * ver_carpan)) + ',' + str(int(26 * ver_carpan)) + '" zPosition="1" alphatest="blend" />\n    <widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/ico_format_on_' + versiyon + '.png" position="' + str(int(1110 * ver_carpan)) + ',' + str(int(615 * ver_carpan)) + '" size="' + str(int(60 * ver_carpan)) + ',' + str(int(26 * ver_carpan)) + '" zPosition="2" alphatest="blend">\n      <convert type="ServiceInfo">IsWidescreen</convert>\n      <convert type="ConditionalShowHide" />\n    </widget>\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/icon_hd_off_' + versiyon + '.png" position="' + str(int(1188 * ver_carpan)) + ',' + str(int(617 * ver_carpan)) + '" size="' + str(int(49 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="1" alphatest="blend" />\n    <widget source="session.CurrentService" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/icon_hd_on_' + versiyon + '.png" position="' + str(int(1188 * ver_carpan)) + ',' + str(int(617 * ver_carpan)) + '" size="' + str(int(49 * ver_carpan)) + ',' + str(int(24 * ver_carpan)) + '" zPosition="2" alphatest="blend">\n      <convert type="ServiceInfo">VideoWidth</convert>\n      <convert type="ValueRange">721,1980</convert>\n      <convert type="ConditionalShowHide" />\n    </widget>\n    <widget source="session.CurrentService" render="Label" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" position="' + str(int(1070 * ver_carpan)) + ',' + str(int(590 * ver_carpan)) + '" size="' + str(int(55 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" halign="right" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServiceInfo">VideoWidth</convert>\n    </widget>\n    <eLabel text="x" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" position="' + str(int(1129 * ver_carpan)) + ',' + str(int(590 * ver_carpan)) + '" size="' + str(int(15 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" halign="center" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget source="session.CurrentService" render="Label" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" position="' + str(int(1146 * ver_carpan)) + ',' + str(int(590 * ver_carpan)) + '" size="' + str(int(55 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" halign="left" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ServiceInfo">VideoHeight</convert>\n    </widget>\n  </screen>'
        STATE_IDLE = 0
        STATE_PLAYING = 1
        STATE_PAUSED = 2
        ENABLE_RESUME_SUPPORT = True
        ALLOW_SUSPEND = True

        def __init__(self, session, recorder_sref = None, subtitles = None):
            Screen.__init__(self, session)
            InfoBarBase.__init__(self, steal_current_service=True)
            IPTVInfoBarShowHide.__init__(self)
            InfoBarSeek.__init__(self, actionmap='InfobarSeekActions')
            if TURKVOD.disable_audioselector == False:
                InfoBarAudioSelection.__init__(self)
            self.InfoBar_NabDialog = Label()
            self.session = session
            self.service = None
            self['state'] = Label('')
            self['cont_play'] = Label('')
            self['kaydet'] = Label('')
            self['chplus'] = Label('')
            self['altyazi'] = Label('')
            self['altyazi'].setText(par.get(Dil, '82'))
            self['chplus'].setText(TURKVOD.prev_page_text[0:23])
            self.cont_play = TURKVOD.cont_play
            TURKVOD.play_iptv = False
            self.film_quality = None
            self.video_tulpe = None
            self.recorder_sref = None
            self['cover'] = Pixmap()
            self['pico'] = Pixmap()
            self['tsre'] = Pixmap()
            self.picload = ePicLoad()
            self.picfile = ''
            if recorder_sref:
                self.recorder_sref = recorder_sref
                self.session.nav.playService(recorder_sref)
            else:
                self.vod_entry = TURKVOD.iptv_list[TURKVOD.list_index]
                self.vod_url = self.vod_entry[4]
                self.title = self.vod_entry[1]
                self.descr = self.vod_entry[2]
            print 'evEOF=%d' % iPlayableService.evEOF
            self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
             iPlayableService.evStart: self.__serviceStarted,
             iPlayableService.evEOF: self.__evEOF})
            self['actions'] = HelpableActionMap(self, 'TURKvodPlayerVod', {'KEY_EXIT': self.exit,
             'KEY_INFO': self.show_more_info,
             'KEY_NEXT': self.nextAR,
             'KEY_PREVIOUS': self.prevAR,
             'kayit': self.record,
             'KEY_STOP': self.stopnew,
             'KEY_TV': self.stopnew,
             'KEY_BLUE': self.timeshift_autoplay,
             'KEY_RECORD': self.timeshift,
             'KEY_BLUE': self.autoplay,
             'KEY_CHANNELDOWN': self.prevVideo,
             'KEY_CHANNELUP': self.nextVideo,
             'KEY_GREEN': self.startTS,
             'KEY_VIDEO_UZUN': self.timeshift,
             '0': self.panikyok,
             'KEY_POWER': self.power_off}, -1)
            self.onFirstExecBegin.append(self.play_vod)
            self.onShown.append(self.setCover)
            self.onPlayStateChanged.append(self.__playStateChanged)
            self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
            self.state = self.STATE_PLAYING
            self.timeshift_url = None
            self.timeshift_title = None
            self.onShown.append(self.show_info)
            self.error_message = ''
            self.recEnable = True
            self.Timer = eTimer()
            self.Timer.callback.append(self.TimerFire)
            self['tsenable'] = Label('')
            self['tsenable'].setText('TIME SHIFT')
            self['tsclock'] = Label('')
            self.tvPlay = False
            self.tit = False
            self.on_off = False
            self.decodeImage()
            self.moviefolder = config.plugins.TURKVOD.cachefold.value
            return

        def panikyok(self):
            self.liste_vod_id = 0
            TURKVOD.play_vod = False
            self.session.nav.stopService()
            self.session.nav.playService(FIRST_SESSION)
            self.close(self.session.close(self.oldService))

        def showAfterSeek(self):
            if isinstance(self, IPTVInfoBarShowHide):
                self.doShow()

        def timeshift_autoplay(self):
            if self.timeshift_url:
                try:
                    self.reference = eServiceReference(4097, 0, self.timeshift_url)
                    self.reference.setName(self.timeshift_title)
                    self.session.nav.playService(self.reference)
                except Exception as ex:
                    print ex
                    print 'EXC timeshift 1'

            else:
                if self.cont_play:
                    self.cont_play = False
                    self['cont_play'].setText(par.get(Dil, '21'))
                    self.session.open(MessageBox, par.get(Dil, '22'), type=MessageBox.TYPE_INFO, timeout=3)
                else:
                    self.cont_play = True
                    self['cont_play'].setText(par.get(Dil, '23'))
                    self.session.open(MessageBox, par.get(Dil, '24'), type=MessageBox.TYPE_INFO, timeout=3)
                TURKVOD.cont_play = self.cont_play

        def timeshift(self):
            if self.timeshift_url:
                try:
                    self.reference = eServiceReference(4097, 0, self.timeshift_url)
                    self.reference.setName(self.timeshift_title)
                    self.session.nav.playService(self.reference)
                except Exception as ex:
                    print ex
                    print 'EXC timeshift 2'

        def startTS(self):
            hdd = os.path.isdir('/media/hdd')
            usb = os.path.isdir('/media/usb')
            if hdd == True or usb == True:
                self.startT()
            else:
                self.session.open(MessageBox, par.get(Dil, '98'), type=MessageBox.TYPE_INFO, timeout=3)

        def startT(self):
            self.ar_job()
            if self.ts_progress == None and self.timeshift_url == None and self.vod_url.find('m3u8') < 0:
                self['tsenable'].setText('')
                self.recEnable = False
                self.tvPlay = False
                try:
                    self.session.open(MessageBox, par.get(Dil, '83'), type=MessageBox.TYPE_INFO, timeout=3)
                    self.session.nav.stopService()
                    filename = 'TURKvod'
                    self.timeshift_url = TURKVOD.moviefolder + filename + '.ts'
                    if os.path.exists(self.timeshift_url) == True:
                        os.remove(self.timeshift_url)
                    self.timeshift_title = '[TS] ' + self.title
                    cmd = "wget -c '%s' -O '%s'" % (self.vod_url, self.timeshift_url)
                    print 'cmd ', str(cmd)
                    JobManager.AddJob(downloadJob(self, cmd, self.timeshift_url, self.title))
                    self.counter = 0
                    self.TimerFire()
                except Exception as ex:
                    print ex
                    print 'ERROR TS'

            elif self.vod_url.find('m3u8') > -1:
                self['tsenable'].setText('')
                self['tsclock'].setText('3')
                self.recEnable = False
                self.tvPlay = False
                try:
                    self.session.open(MessageBox, 'TimeShift running Please wait', type=MessageBox.TYPE_INFO, timeout=3)
                    self.session.nav.stopService()
                    useragent = "--header='User-Agent: QuickTime/7.6.2 (qtver=7.6.2;os=Windows NT 5.1Service Pack 3)'"
                    filename = 'TURKvod'
                    self.timeshift_url = TURKVOD.moviefolder + filename
                    if os.path.exists(self.timeshift_url) == True:
                        os.remove(self.timeshift_url)
                    self.timeshift_title = '[TS] ' + self.title
                    self.m3u8_tulpe = self.m3u8_descriptor()
                    if len(self.m3u8_tulpe) > 0:
                        m3u8_downloader(self.m3u8_tulpe, TURKVOD.moviefolder, filename)
                    self.counter = 0
                    self.TimerFire()
                except Exception as ex:
                    print ex
                    print 'ERROR m3u8 TS'

            else:
                try:
                    self.session.openWithCallback(stopnew, MessageBox, par.get(Dil, '79'), type=MessageBox.TYPE_YESNO)
                except Exception as ex:
                    print ex

            return

        def run_m3u8_shift(self):
            self.counter += 1
            self.Timer.startLongTimer(3)
            try:
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 1:
                    self['tsclock'].setText('2')
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 2:
                    self['tsclock'].setText('1')
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 3:
                    self['tsclock'].setText('0')
                if len(JobManager.getPendingJobs()) < len(self.m3u8_tulpe) - 4:
                    self['tsclock'].setText('')
                    self.tsPlay = True
                    self.timeshift()
                    del self.Timer
            except Exception as ex:
                print ex

        def TimerFire(self):
            self.counter += 1
            self.Timer.stop()
            if self.vod_url.find('m3u8') > -1:
                self.run_m3u8_shift()
            else:
                self.getTaskProgress()

        def ar_job(self):
            self.ts_progress = None
            for job in JobManager.getPendingJobs():
                self.ts_progress = job.progress

            return

        def getTaskProgress(self):
            self.ar_job()
            if self.ts_progress != None:
                self['state'].setText('TS = ' + str(self.ts_progress) + ' % ' + self.seekstate[3])
                if self.counter > int(TURKVOD.use_ts_percent) and self.tvPlay == False:
                    self.tvPlay = True
                    self.timeshift()
                self.Timer.startLongTimer(1)
            else:
                del self.Timer
                self['state'].setText('TS = 100 % ' + self.seekstate[3])
            return

        def autoplay(self):
            if self.timeshift_url == None:
                if self.cont_play:
                    self.cont_play = False
                    self['cont_play'].setText(par.get(Dil, '21'))
                    self.session.open(MessageBox, par.get(Dil, '22'), type=MessageBox.TYPE_INFO, timeout=3)
                else:
                    self.cont_play = True
                    self['cont_play'].setText(par.get(Dil, '23'))
                    self.session.open(MessageBox, par.get(Dil, '24'), type=MessageBox.TYPE_INFO, timeout=3)
                TURKVOD.cont_play = self.cont_play
            return

        def show_info(self):
            if TURKVOD.play_vod == True:
                self['state'].setText(par.get(Dil, '27'))
                self['kaydet'].setText(par.get(Dil, '142'))
                self['pico'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/ico_mp_play.png')
            self.hideTimer.start(1000, True)
            if self.cont_play:
                self['cont_play'].setText(par.get(Dil, '23'))
            else:
                self['cont_play'].setText(par.get(Dil, '21'))

        def playnextvideo_box(self):
            index = TURKVOD.list_index + 1
            video_counter = len(TURKVOD.iptv_list)
            if index < video_counter and TURKVOD.iptv_list[index][4] != None:
                descr = ''
                if TURKVOD.iptv_list[index][2]:
                    descr = TURKVOD.iptv_list[index][2]
                title = TURKVOD.iptv_list[index][1] + '\n\n' + str(descr)
                self.session.openWithCallback(self.playnextvideo, MessageBox, _(par.get(Dil, '24') + '\n%s') % title, type=MessageBox.TYPE_YESNO)
            return

        def playnextvideo(self, message = None):
            if message:
                try:
                    self.nextVideo()
                except Exception as ex:
                    print ex
                    print 'EXC playnextvideo'

        def nextVideo(self):
            if self.timeshift_url == None:
                try:
                    index = TURKVOD.list_index + 1
                    video_counter = len(TURKVOD.iptv_list)
                    if index < video_counter:
                        if TURKVOD.iptv_list[index][4] != None:
                            TURKVOD.list_index = index
                            self.player_helper()
                except Exception as ex:
                    print ex
                    print 'EXC nextVideo'

            return

        def prevVideo(self):
            if self.timeshift_url == None:
                try:
                    index = TURKVOD.list_index - 1
                    if index > -1:
                        if TURKVOD.iptv_list[index][4] != None:
                            TURKVOD.list_index = index
                            self.player_helper()
                except Exception as ex:
                    print ex
                    print 'EXC prevVideo'

            return

        def player_helper(self):
            self.show_info()
            if self.vod_entry:
                self.vod_entry = TURKVOD.iptv_list[TURKVOD.list_index]
                self.vod_url = self.vod_entry[4]
                self.title = self.vod_entry[1]
                self.descr = self.vod_entry[2]
            self.session.nav.stopService()
            TURKVOD.play_vod = False
            TURKVOD.list_index_tmp = TURKVOD.list_index
            self.setCover()
            self.play_vod()

        def setCover(self):
            try:
                vod_entry = TURKVOD.iptv_list[TURKVOD.list_index]
                self['cover'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/clear.png')
                if self.vod_entry[7] != '':
                    if vod_entry[7].find('http') == -1:
                        self.picfile = PLUGIN_PATH + '/img/' + vod_entry[3]
                        self.decodeImage()
                        print 'LOCAL IMG VOD'
                    else:
                        if TURKVOD.img_loader == False:
                            self.picfile = '%s/turkvod_tmp_pic.jpg' % config.plugins.TURKVOD.images_tmp_path.value
                        else:
                            m = hashlib.md5()
                            m.update(self.vod_entry[7])
                            cover_md5 = m.hexdigest()
                            self.picfile = '%s/%s.jpg' % (config.plugins.TURKVOD.images_tmp_path.value, cover_md5)
                        if os.path.exists(self.picfile) == False or TURKVOD.img_loader == False:
                            if TWIST == 1:
                                image_url = self.vod_entry[7]
                                localfile = self.picfile
                                host = re.findall('//(.*?)/', image_url, re.IGNORECASE)[0]
                                sniFactory = SNIFactory(host)
                                client.downloadPage(image_url, localfile, sniFactory).addCallback(self.image_downloaded).addErrback(self.image_error)
                            elif self.vod_entry[7].startswith('https') and config.plugins.TURKVOD.httpsposter.value == True:
                                cookiejar = cookielib.CookieJar()
                                _opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
                                _opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57')]
                                op = _opener.open(self.vod_entry[7])
                                out_file = open(self.picfile, 'wb')
                                out_file.write(op.read())
                                out_file.close()
                                self.decodeImage()
                            else:
                                downloadPage(self.vod_entry[7], self.picfile).addCallback(self.image_downloaded).addErrback(self.image_error)
                        else:
                            self.decodeImage()
            except Exception as ex:
                print ex
                print 'update COVER'

        def decodeImage(self):
            try:
                x = self['cover'].instance.size().width()
                y = self['cover'].instance.size().height()
                picture = self.picfile
                picload = self.picload
                sc = AVSwitch().getFramebufferScale()
                picload.setPara((x,
                 y,
                 sc[0],
                 sc[1],
                 0,
                 0,
                 'transparent'))
                l = picload.PictureData.get()
                del l[:]
                l.append(boundFunction(self.showImage))
                picload.startDecode(picture)
            except Exception as ex:
                print ex
                print 'ERROR decodeImage'

        def showImage(self, picInfo = None):
            self['cover'].show()
            try:
                ptr = self.picload.getData()
                if ptr:
                    self['cover'].instance.setPixmap(ptr.__deref__())
            except Exception as ex:
                print ex
                print 'ERROR showImage'

        def image_downloaded(self, id):
            self.decodeImage()

        def image_error(self, id):
            i = 0

        def record(self):
            if self.vod_url.find('m3u8') < 0:
                if self.recEnable == True:
                    try:
                        self.session.open(MessageBox, par.get(Dil, '25'), type=MessageBox.TYPE_INFO, timeout=3)
                        self.session.nav.stopService()
                        self['state'].setText(par.get(Dil, '137'))
                        ende = str(self.vod_url.split('.')[-1].lower())
                        if ende != 'mp4' or ende != 'flv' or ende != 'ts' or ende != 'avi' or ende != 'mkv' or ende != 'wmv':
                            ende = 'mp4'
                        today = datetime.fromtimestamp(time()).strftime('[%d.%m_%H:%M:%S]')
                        title_translit = cyr2lat(self.title)
                        filename = today + ASCIItranslit.legacyEncode(title_translit + '.') + ende
                        cmd = "wget -c '%s' -O '%s%s'" % (self.vod_url, TURKVOD.moviefolder, filename)
                        print 'cmd ', cmd
                        JobManager.AddJob(downloadJob(self, cmd, TURKVOD.moviefolder + filename, self.title))
                        self.createMetaFile(filename)
                        self.LastJobView()
                        self.timeshift_url = TURKVOD.moviefolder + filename
                        self.timeshift_title = '[REC] ' + self.title
                        TURKVOD.play_vod = False
                        self.close()
                    except Exception as ex:
                        print ex
                        print 'ERROR record'

                else:
                    self.session.openWithCallback(self.exit, MessageBox, ' TimeShift calisiyor, durdurulsunmu?', type=MessageBox.TYPE_YESNO)
            elif self.recEnable == True:
                try:
                    self.session.open(MessageBox, 'REC ON', type=MessageBox.TYPE_INFO, timeout=3)
                    today = datetime.fromtimestamp(time()).strftime('%d.%m_%H:%M:%S - ')
                    self.m3u8_tulpe = self.m3u8_descriptor()
                    if len(self.m3u8_tulpe) > 0:
                        self.session.nav.stopService()
                        self.session.nav.playService(FIRST_SESSION)
                        ende = str(self.m3u8_tulpe[0].split('.')[-1].lower())
                        filename = today + self.title + '.' + ende
                        m3u8_downloader(self.m3u8_tulpe, TURKVOD.moviefolder, self.title)
                        TURKVOD.play_vod = False
                        self.close()
                except Exception as ex:
                    print ex
                    print 'ERROR m3u8 record'

        def m3u8_descriptor(self):
            m3u8_tulpe = []
            m3u8_tulpe_tmp = []
            url_m3u8 = ''
            try:
                m3u8_split = self.vod_url.split('/')[:-1]
                for m3u8_frag in m3u8_split:
                    url_m3u8 = url_m3u8 + (m3u8_frag + '/')

                req = urllib2.Request(url=self.vod_url, data=None, headers={'User-agent': 'QuickTime/7.6.2 (qtver=7.6.2;os=Windows NT 5.1 Service Pack 3)'})
                resp = urllib2.urlopen(req)
                m3u8page = resp.read()
                fragmented = re.findall('#EXTINF:(.*),.*', m3u8page)
                if fragmented:
                    m3u8_tulpe_tmp = re.findall('#EXTINF:.*\\s(.*)', m3u8page)
                    if m3u8_tulpe_tmp[0].find('http') < 0:
                        for tulpe in m3u8_tulpe_tmp:
                            m3u8_tulpe.append(url_m3u8 + tulpe)

                    else:
                        m3u8_tulpe = m3u8_tulpe_tmp
                else:
                    m3u8_tulpe = []
                return m3u8_tulpe
            except Exception as ex:
                print ex

            return

        def LastJobView(self):
            currentjob = None
            for job in JobManager.getPendingJobs():
                currentjob = job

            if currentjob is not None:
                self.session.open(JobView, currentjob)
            return

        def createMetaFile(self, filename):
            try:
                text = re.compile('<[\\/\\!]*?[^<>]*?>')
                text_clear = ''
                if self.vod_entry[2] != None:
                    text_clear = text.sub('', self.vod_entry[2])
                serviceref = eServiceReference(4097, 0, TURKVOD.moviefolder + filename)
                metafile = open('%s/%s.meta' % (TURKVOD.moviefolder, filename), 'w')
                metafile.write('%s\n%s\n%s\n%i\n' % (serviceref.toString(),
                 self.title.replace('\n', ''),
                 text_clear.replace('\n', ''),
                 time()))
                metafile.close()
            except Exception as ex:
                print ex
                print 'ERROR metaFile'

            return

        def __evEOF(self):
            if self.timeshift_url == None:
                if self.cont_play:
                    self.nextVideo()
                else:
                    self.playnextvideo_box()
            return

        def __seekableStatusChanged(self):
            print 'seekable status changed!'

        def __serviceStarted(self):
            self['state'].setText(' ' + par.get(Dil, '27'))
            self['cont_play'].setText(par.get(Dil, '28'))
            self.state = self.STATE_PLAYING

        def doEofInternal(self, playing):
            if not self.execing:
                return
            if not playing:
                return
            print 'doEofInternal EXIT OR NEXT'

        def exit(self):
            if self.timeshift_url:
                self.session.openWithCallback(self.stops, MessageBox, par.get(Dil, '79'), type=MessageBox.TYPE_YESNO)
            else:
                self.close()

        def stopnew(self):
            if self.timeshift_url:
                self.session.openWithCallback(self.stops, MessageBox, par.get(Dil, '79'), type=MessageBox.TYPE_YESNO)
            else:
                self.session.nav.stopService()
                TURKVOD.play_vod = False
                print 'FIRST_SESSION'
                self.session.nav.playService(FIRST_SESSION)
                self.close(None)
            return

        def stops(self, message = None):
            if message:
                self.on_off = False
                job = None
                for currentjob in JobManager.getPendingJobs():
                    job = currentjob
                    if job is not None:
                        Job.cancel(job)

                if self.timeshift_url:
                    self.BgFileEraser = eBackgroundFileEraser.getInstance()
                    self.BgFileEraser.erase(self.timeshift_url)
                    self.timeshift_url = None
                    self.timeshift_title = None
                self.session.nav.stopService()
                TURKVOD.play_vod = False
                print 'FIRST_SESSION'
                self.session.nav.playService(FIRST_SESSION)
                self.close(None)
            return

        def nextAR(self):
            message = nextAR()
            self.session.open(MessageBox, message, type=MessageBox.TYPE_INFO, timeout=3)

        def prevAR(self):
            message = prevAR()
            self.session.open(MessageBox, message, type=MessageBox.TYPE_INFO, timeout=3)

        def show_more_info(self):
            self.session.open(MessageBox, self.vod_url, type=MessageBox.TYPE_INFO)

        def __playStateChanged(self, state):
            self.hideTimer.start(1000, True)
            print 'self.seekstate[3] ' + self.seekstate[3]
            text = ' ' + self.seekstate[3]
            if self.seekstate[3] == '>':
                text = ' ' + par.get(Dil, '27')
                self['pico'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/ico_mp_play.png')
            if self.seekstate[3] == '||':
                text = par.get(Dil, '29')
                self['pico'].instance.setPixmapFromFile(PLUGIN_PATH + '/img/ico_mp_pause.png')
            if self.seekstate[3] == '>> 2x':
                text = '    x2     >>'
            if self.seekstate[3] == '>> 4x':
                text = '    x4     >>'
            if self.seekstate[3] == '>> 8x':
                text = '    x8     >>'
            self['state'].setText(text)

        def quality_selector(self):
            try:
                self.session.openWithCallback(self.cbSelectQuality, turkQuality, film_quality=self.film_quality)
            except Exception as ex:
                print ex
                print 'q_selector'

        def cbSelectQuality(self, position = None):
            print 'cbSelectQuality'
            print self.vod_url
            try:
                if position > -1:
                    print 'position*** ', position
                    if self.vod_url.find('.m3u8') > 0:
                        self.vod_url = self.video_tulpe[position]
                        self.title = self.title + ' m3u8:' + self.film_quality[position]
                        self.reference = eServiceReference(4097, 0, self.vod_url)
                        self.reference.setName(self.title)
                        try:
                            self.session.nav.playService(self.reference)
                        except Exception as ex:
                            print ex

                    elif self.film_quality:
                        self.vod_url = self.video_tulpe[position]
                        self.title = self.title + self.film_quality[position]
                        parts = self.vod_url.split('|', 1)
                        self.vod_url = parts[0]
                        if len(parts) > 1:
                            config.mediaplayer.extraHeaders = NoSave(ConfigText(default=''))
                            config.mediaplayer.extraHeaders.setValue('')
                            headersString = str(parts[1])
                            print '***self.headersString:***' + headersString
                            config.mediaplayer.extraHeaders.setValue(headersString)
                        self.reference = eServiceReference(4097, 0, self.vod_url)
                        self.reference.setName(self.title)
                        try:
                            self.session.nav.playService(self.reference)
                        except Exception as ex:
                            print ex

                    else:
                        self.title = self.title + '**'
                        self.reference = eServiceReference(4097, 0, self.vod_url)
                        self.reference.setName(self.title)
                        try:
                            self.session.nav.playService(self.reference)
                        except Exception as ex:
                            print 'vod play error 11'
                            print ex

                elif self.vod_url:
                    print 'position yok', self.vod_url
                    self.title = self.title + '**'
                    self.reference = eServiceReference(4097, 0, self.vod_url)
                    self.reference.setName(self.title)
                    try:
                        self.session.nav.playService(self.reference)
                    except Exception as ex:
                        print 'vod play error 11'
                        print ex

                else:
                    print 'position yok', position
                    self.exit()
            except Exception as ex:
                print ex
                print 'vod play error 2'

        def play_vod(self):
            try:
                if TURKVOD.play_vod == False or TURKVOD.play_iptv == True:
                    TURKVOD.play_vod = True
                    self.vod_url = str(self.vod_url)
                    self.vod_url = self.parse_url()
                    print 'self.vod_url:' + str(self.vod_url)
                    if len(self.film_quality) >= 1:
                        self.quality_selector()
                    else:
                        try:
                            if self.vod_url != '' and self.vod_url != None and len(self.vod_url) > 5:
                                print '--->' + self.vod_url + '<------'
                                try:
                                    parts = self.vod_url.split('|', 1)
                                    vurl = parts[0]
                                    config.mediaplayer.extraHeaders = NoSave(ConfigText(default=''))
                                    config.mediaplayer.extraHeaders.setValue('')
                                    if len(parts) > 1:
                                        headersString = str(parts[1])
                                        print 'self.headersString:' + headersString
                                        config.mediaplayer.extraHeaders.setValue(headersString)
                                    if vurl.find('127.0.0.1') > 0:
                                        self.reference = eServiceReference(vurl.replace('http://127.0.0.1:8001/', ''))
                                        self.reference.setName(self.title)
                                        self.session.nav.playService(self.reference)
                                    else:
                                        self.reference = eServiceReference(4097, 0, vurl)
                                        self.reference.setName(self.title)
                                        self.session.nav.playService(self.reference)
                                except Exception as ex:
                                    print 'oynatma hatasi'
                                    print ex

                            else:
                                if self.error_message:
                                    self.session.open(MessageBox, self.error_message.encode('utf-8'), type=MessageBox.TYPE_ERROR)
                                else:
                                    self.session.open(MessageBox, par.get(Dil, '30').encode('utf-8'), type=MessageBox.TYPE_ERROR)
                                self.close()
                        except Exception as ex:
                            print 'vod play error 2'
                            print ex

            except Exception as ex:
                print 'vod play error 0'
                print ex

            return

        def parse_url(self):
            if TURKVOD.playhack != '':
                self.vod_url = TURKVOD.playhack
            print '++++++++++parse_url+++++++++++'
            print 'self.vod_url', self.vod_url
            try:
                self.video_tulpe = []
                self.film_quality = []
                play_url = TURKVOD_PARSER.get_parsed_link(self.vod_url)
                print 'solved :', play_url
                if play_url:
                    if type(play_url) == str:
                        self.vod_url = play_url
                    elif type(play_url) == tuple:
                        if play_url[0]:
                            self.error_message = play_url[0]
                            self.vod_url = 'none'
                        else:
                            self.video_tulpe = play_url[1]
                            self.film_quality = play_url[2]
            except Exception as ex:
                print 'ERROR+++++++++++++++++parse_url++++++++++++++++++++++ERROR'
                print ex

            debug(self.vod_url, '#### self.vod_url ####')
            print 'video_tulpe: ', self.video_tulpe
            print 'film_quality: ', self.film_quality
            if self.error_message == True:
                self.session.open(MessageBox, par.get(Dil, '30').encode('utf-8'), type=MessageBox.TYPE_ERROR)
                self.close()
            else:
                return self.vod_url

        def power_off(self):
            self.close(1)


class turkQuality(Screen):
    fontcolor = fontcolorfont
    menufont = menufontcolor
    menuust = menuustfontcolor
    menufontt = mfont
    aciklamafont = fontaciklama
    skin = '<screen name="turkQuality" position="' + str(int(880 * ver_carpan)) + ',0" size="' + str(int(400 * ver_carpan)) + ',' + str(int(723 * ver_carpan)) + '" title="Episode selector" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="0,0" zPosition="-10" size="' + str(int(400 * ver_carpan)) + ',' + str(int(723 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <eLabel name="menulabel" text="Kalite Secimi" position="' + str(int(24 * ver_carpan)) + ',' + str(int(44 * ver_carpan)) + '" size="' + str(int(350 * ver_carpan)) + ',' + str(int(43 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(35 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget name="menulist" position="' + str(int(24 * ver_carpan)) + ',' + str(int(120 * ver_carpan)) + '" size="' + str(int(350 * ver_carpan)) + ',' + str(int(520 * ver_carpan)) + '" zPosition="3" itemHeight="' + str(int(30 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" foregroundColor="' + str(menuust) + '" foregroundColorSelected="' + str(menufont) + '" scrollbarMode="showOnDemand" enableWrapAround="1" transparent="1" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" />\n  </screen>'

    def __init__(self, session, film_quality = None):
        Screen.__init__(self, session)
        self.film_quality = []
        self['actions'] = HelpableActionMap(self, 'TURKvodPlayerPlaylis', {'KEY_EXIT': self.exi,
         'KEY_OK': self.ok}, -1)
        for x in range(len(film_quality)):
            listele = film_quality[x].strip()
            self.film_quality.append('%i   %s   ' % (x + 1, listele))

        self['menulist'] = MenuList(self.film_quality)
        self['menulabel'] = Label(par.get(Dil, '31') + '  v. ' + VERSION)

    def ok(self):
        self.close(self['menulist'].l.getCurrentSelectionIndex())

    def exi(self):
        self.close(None)
        return


def channelEntryIPTVplaylist(entry):
    menu_entry = [entry, (eListboxPythonMultiContent.TYPE_TEXT,
      CHANNEL_NUMBER[0],
      CHANNEL_NUMBER[1],
      CHANNEL_NUMBER[2],
      CHANNEL_NUMBER[3],
      CHANNEL_NUMBER[4],
      RT_HALIGN_CENTER,
      '%s' % entry[0]), (eListboxPythonMultiContent.TYPE_TEXT,
      CHANNEL_NAME[0],
      CHANNEL_NAME[1],
      CHANNEL_NAME[2],
      CHANNEL_NAME[3],
      CHANNEL_NAME[4],
      RT_HALIGN_LEFT,
      entry[1])]
    return menu_entry


def Plugins(**kwargs):
    return [PluginDescriptor(name='TURKvod VOD & IPTV', description='VOD & IPTV Player', where=PluginDescriptor.WHERE_MENU, fnc=menu), PluginDescriptor(name='TURKvod VOD & IPTV', description='TURKvod VOD & IPTV', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=Start_iptv_palyer, icon='plugin.png')]


conversion = {unicode('\xd0\xb0'): 'a',
 unicode('\xd0\x90'): 'A',
 unicode('\xd0\xb1'): 'b',
 unicode('\xd0\x91'): 'B',
 unicode('\xd0\xb2'): 'v',
 unicode('\xd0\x92'): 'V',
 unicode('\xd0\xb3'): 'g',
 unicode('\xd0\x93'): 'G',
 unicode('\xd0\xb4'): 'd',
 unicode('\xd0\x94'): 'D',
 unicode('\xd0\xb5'): 'e',
 unicode('\xd0\x95'): 'E',
 unicode('\xd1\x91'): 'jo',
 unicode('\xd0\x81'): 'jo',
 unicode('\xd0\xb6'): 'zh',
 unicode('\xd0\x96'): 'ZH',
 unicode('\xd0\xb7'): 'z',
 unicode('\xd0\x97'): 'Z',
 unicode('\xd0\xb8'): 'i',
 unicode('\xd0\x98'): 'I',
 unicode('\xd0\xb9'): 'j',
 unicode('\xd0\x99'): 'J',
 unicode('\xd0\xba'): 'k',
 unicode('\xd0\x9a'): 'K',
 unicode('\xd0\xbb'): 'l',
 unicode('\xd0\x9b'): 'L',
 unicode('\xd0\xbc'): 'm',
 unicode('\xd0\x9c'): 'M',
 unicode('\xd0\xbd'): 'n',
 unicode('\xd0\x9d'): 'N',
 unicode('\xd0\xbe'): 'o',
 unicode('\xd0\x9e'): 'O',
 unicode('\xd0\xbf'): 'p',
 unicode('\xd0\x9f'): 'P',
 unicode('\xd1\x80'): 'r',
 unicode('\xd0\xa0'): 'R',
 unicode('\xd1\x81'): 's',
 unicode('\xd0\xa1'): 'S',
 unicode('\xd1\x82'): 't',
 unicode('\xd0\xa2'): 'T',
 unicode('\xd1\x83'): 'u',
 unicode('\xd0\xa3'): 'U',
 unicode('\xd1\x84'): 'f',
 unicode('\xd0\xa4'): 'F',
 unicode('\xd1\x85'): 'h',
 unicode('\xd0\xa5'): 'H',
 unicode('\xd1\x86'): 'c',
 unicode('\xd0\xa6'): 'C',
 unicode('\xd1\x87'): 'ch',
 unicode('\xd0\xa7'): 'CH',
 unicode('\xd1\x88'): 'sh',
 unicode('\xd0\xa8'): 'SH',
 unicode('\xd1\x89'): 'sh',
 unicode('\xd0\xa9'): 'SH',
 unicode('\xd1\x8a'): '',
 unicode('\xd0\xaa'): '',
 unicode('\xd1\x8b'): 'y',
 unicode('\xd0\xab'): 'Y',
 unicode('\xd1\x8c'): 'j',
 unicode('\xd0\xac'): 'J',
 unicode('\xd1\x8d'): 'je',
 unicode('\xd0\xad'): 'JE',
 unicode('\xd1\x8e'): 'ju',
 unicode('\xd0\xae'): 'JU',
 unicode('\xd1\x8f'): 'ja',
 unicode('\xd0\xaf'): 'JA',
 unicode('\\u011f'): '\xc4\x9f',
 unicode('\\u011e'): '\xc4\x9e',
 unicode('\\u0131'): '\xc4\xb1',
 unicode('\\u0130'): '\xc4\xb0',
 unicode('\\u00f6'): '\xc3\xb6',
 unicode('\\u00d6'): '\xc3\x96',
 unicode('\\u00fc'): '\xc3\xbc',
 unicode('\\u00dc'): '\xc3\x9c',
 unicode('\\u015f'): '\xc5\x9f',
 unicode('\\u015e'): '\xc5\x9e',
 unicode('\\u00e7'): '\xc3\xa7',
 unicode('\\u00c7'): '\xc3\x87'}

def cyr2lat(text):
    i = 0
    text = text.strip(' \t\n\r')
    text = unicode(text)
    retval = ''
    bukva_translit = ''
    bukva_original = ''
    while i < len(text):
        bukva_original = text[i]
        try:
            bukva_translit = conversion[bukva_original]
        except:
            bukva_translit = bukva_original

        i = i + 1
        retval += bukva_translit

    return retval


class vodeScreen(Screen):
    fontcolor = fontcolorfont
    menufont = menufontcolor
    menuust = menuustfontcolor
    menufontt = mfont
    aciklamafont = fontaciklama
    skin = '<screen name="vodeScreen" position="0,0" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(720 * ver_carpan)) + '" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="' + str(int(40 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" zPosition="-10" size="' + str(int(1205 * ver_carpan)) + ',' + str(int(650 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(1103 * ver_carpan)) + ',' + str(int(46 * ver_carpan)) + '" size="' + str(int(140 * ver_carpan)) + ',' + str(int(60 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(50 * ver_carpan)) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(49 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(27 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(15 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" transparent="1" foregroundColor="' + str(fontcolor) + '">\n      <convert type="ClockToText">Format:%A</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(72 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(29 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(16 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%e. %b</convert>\n    </widget>\n    <eLabel text="TURKvod Video Download Listesi" position="' + str(int(70 * ver_carpan)) + ',' + str(int(47 * ver_carpan)) + '" size="' + str(int(800 * ver_carpan)) + ',' + str(int(43 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(34 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget source="movielist" render="Listbox" position="' + str(int(70 * ver_carpan)) + ',' + str(int(110 * ver_carpan)) + '" size="' + str(int(700 * ver_carpan)) + ',' + str(int(510 * ver_carpan)) + '" itemHeight="' + str(int(30 * ver_carpan)) + '" scrollbarMode="showOnDemand" foregroundColor="' + str(menuust) + '" backgroundColor="' + metrixBackground + '" foregroundColorSelected="' + str(menufont) + '" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" transparent="1">\n      <convert type="TemplatedMultiContent">          \n\t\t{"template": [\n\t\t\tMultiContentEntryText(pos = (0, 1), size = (' + str(int(710 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '), font=1, flags = RT_HALIGN_LEFT, text = 1), # index 1 is the name\n\t\t\tMultiContentEntryText(pos = (' + str(int(720 * ver_carpan)) + ', 1), size = (' + str(int(150 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '), font=1, flags = RT_HALIGN_RIGHT, text = 2), # index 2 is the state\n\t\t\tMultiContentEntryProgress(pos = (' + str(int(880 * ver_carpan)) + ', 1), size = (' + str(int(100 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '), percent = -3), # index 3 should be progress\n\t\t\tMultiContentEntryText(pos = (' + str(int(990 * ver_carpan)) + ', 1), size = (' + str(int(60 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '), font=1, flags = RT_HALIGN_RIGHT, text = 4), # index 4 is the percentage\n\t\t\t],\n\t\t\t"fonts": [gFont("RegularTURKvod", ' + str(int(26 * ver_carpan)) + '),gFont("RegularTURKvod", ' + str(int(22 * ver_carpan)) + ')],\n\t\t"itemHeight": ' + str(int(29 * ver_carpan)) + '\n\t\t}\n\t    </convert>\n    </widget>\n    <ePixmap position="' + str(int(920 * ver_carpan)) + ',' + str(int(230 * ver_carpan)) + '" size="' + str(int(256 * ver_carpan)) + ',' + str(int(256 * ver_carpan)) + '" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/hdd_' + versiyon + '.png" transparent="1" alphatest="blend" />\n  </screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        self['shortcuts'] = ActionMap(['OkCancelActions'], {'ok': self.keyOK,
         'cancel': self.keyClose}, -1)
        self['movielist'] = List([])
        self.Timer = eTimer()
        self.Timer.callback.append(self.TimerFire)
        self.onLayoutFinish.append(self.layoutFinished)
        self.onClose.append(self.__onClose)

    def __onClose(self):
        del self.Timer

    def layoutFinished(self):
        self.Timer.startLongTimer(2)

    def TimerFire(self):
        self.Timer.stop()
        self.rebuildMovieList()

    def rebuildMovieList(self):
        self.movielist = []
        self.getTaskList()
        self.getMovieList()
        self['movielist'].setList(self.movielist)
        self['movielist'].updateList(self.movielist)

    def getTaskList(self):
        for job in JobManager.getPendingJobs():
            self.movielist.append((job,
             job.name,
             job.getStatustext(),
             int(100 * job.progress / float(job.end)),
             str(100 * job.progress / float(job.end)) + '%'))

        if len(self.movielist) >= 1:
            self.Timer.startLongTimer(10)

    def getMovieList(self):
        filelist = os_listdir(config.plugins.TURKVOD.cachefold.value)
        if filelist is not None:
            filelist.sort()
            for filename in filelist:
                if os_path.isfile(config.plugins.TURKVOD.cachefold.value + filename) and filename.endswith('.meta') is False:
                    self.movielist.append(('movie',
                     filename,
                     _('Finished'),
                     100,
                     '100%'))

        return

    def keyOK(self):
        current = self['movielist'].getCurrent()
        if current:
            if current[0] == 'movie':
                sref = eServiceReference(4097, 0, config.plugins.TURKVOD.cachefold.value + current[1])
                sref.setName(current[1])
                self.session.open(TURKvodVideoPlayer, sref)
            else:
                job = current[0]
                self.session.openWithCallback(self.JobViewCB, JobView, job)

    def JobViewCB(self, why):
        print ''

    def keyClose(self):
        self.close()


class plugin_ka(Screen, ConfigListScreen):
    fontcolor = fontcolorfont
    menufont = menufontcolor
    menuust = menuustfontcolor
    menufontt = mfont
    aciklamafont = fontaciklama
    skin = '<screen name="plugin_ka" position="0,0" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(720 * ver_carpan)) + '" title="Ayarlar" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="' + str(int(40 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" zPosition="-10" size="' + str(int(1205 * ver_carpan)) + ',' + str(int(650 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <widget source="Title" render="Label" position="' + str(int(70 * ver_carpan)) + ',' + str(int(47 * ver_carpan)) + '" size="' + str(int(800 * ver_carpan)) + ',' + str(int(43 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(35 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(1103 * ver_carpan)) + ',' + str(int(46 * ver_carpan)) + '" size="' + str(int(140 * ver_carpan)) + ',' + str(int(60 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(50 * ver_carpan)) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(49 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(27 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(15 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" transparent="1" foregroundColor="' + str(fontcolor) + '">\n      <convert type="ClockToText">Format:%A</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(72 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(29 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(16 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%e. %b</convert>\n    </widget>\n    <widget name="config" position="' + str(int(70 * ver_carpan)) + ',' + str(int(120 * ver_carpan)) + '" size="' + str(int(710 * ver_carpan)) + ',' + str(int(320 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(22 * ver_carpan)) + '" itemHeight="' + str(int(32 * ver_carpan)) + '" zPosition="3" foregroundColor="' + str(menuust) + '" foregroundColorSelected="' + str(menufont) + '" scrollbarMode="showOnDemand" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" transparent="1" />\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/green_' + versiyon + '.png" position="' + str(int(70 * ver_carpan)) + ',' + str(int(635 * ver_carpan)) + '" size="' + str(int(30 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" alphatest="blend" />\n    <eLabel name="ayarlari_kaydet" text="KAYDET / SAVE" position="' + str(int(105 * ver_carpan)) + ',' + str(int(637 * ver_carpan)) + '" size="' + str(int(250 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="left" valign="top" transparent="1" />\n    <ePixmap position="' + str(int(911 * ver_carpan)) + ',' + str(int(252 * ver_carpan)) + '" size="' + str(int(256 * ver_carpan)) + ',' + str(int(256 * ver_carpan)) + '" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/setup_' + versiyon + '.png" transparent="1" alphatest="blend" />\n  </screen>'

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
        self['actions'] = HelpableActionMap(self, 'turkvod', {'green': self.save,
         'back': self.back}, -1)
        self['ayarlari_kaydet'] = Label(par.get(Dil, '58'))
        self['baslik'] = Label(par.get(Dil, '46'))
        self.list = []
        self.list.append(getConfigListEntry(_('1    ' + par.get(Dil, '48')), config.plugins.TURKVOD.csifre))
        self.list.append(getConfigListEntry(_('2    ' + par.get(Dil, '91')), config.plugins.TURKVOD.sifreip))
        self.list.append(getConfigListEntry(_('3    ' + par.get(Dil, '122')), config.plugins.TURKVOD.mod))
        self.list.append(getConfigListEntry(_('4    ' + par.get(Dil, '92')), config.plugins.TURKVOD.thema))
        self.list.append(getConfigListEntry(_('5    ' + par.get(Dil, '93')), config.plugins.TURKVOD.httpsposter))
        self.list.append(getConfigListEntry(_('6    ' + par.get(Dil, '120')), config.plugins.TURKVOD.dortka))
        self.list.append(getConfigListEntry(_('7    ' + par.get(Dil, '78')), config.plugins.TURKVOD.use_ts_percent))
        self.list.append(getConfigListEntry(_('8    ' + par.get(Dil, '57')), config.plugins.TURKVOD.server))
        self.list.append(getConfigListEntry(_('9    ' + par.get(Dil, '49')), config.plugins.TURKVOD.cachefold))
        self.list.append(getConfigListEntry(_('10   ' + par.get(Dil, '88')), config.plugins.TURKVOD.language))
        self.list.append(getConfigListEntry(_('11   ' + par.get(Dil, '138')), config.plugins.TURKVOD.klevye))
        self.list.append(getConfigListEntry(_('12   ' + par.get(Dil, '56')), config.plugins.TURKVOD.images_tmp))
        self.list.append(getConfigListEntry(_('13   ' + par.get(Dil, '50')), config.plugins.TURKVOD.images_tmp_path))
        self.list.append(getConfigListEntry(_('14   ' + par.get(Dil, '51')), config.plugins.TURKVOD.use_rtmpw))
        self.list.append(getConfigListEntry(_('15   ' + par.get(Dil, '53')), config.plugins.TURKVOD.start_scale))
        self.list.append(getConfigListEntry(_('16   ' + par.get(Dil, '54')), config.plugins.TURKVOD.end_scale))
        self.list.append(getConfigListEntry(_('17   ' + par.get(Dil, '55')), config.plugins.TURKVOD.security_key))
        self.list.append(getConfigListEntry(_('18   ' + par.get(Dil, '157')), config.plugins.TURKVOD.mac_id))
        ConfigListScreen.__init__(self, self.list, session)

    def save(self):
        self.close()
        for x in self['config'].list:
            x[1].save()

    def back(self):
        self.close()


class RenAy(Screen, ConfigListScreen):
    fontcolor = fontcolorfont
    menufont = menufontcolor
    menuust = menuustfontcolor
    menufontt = mfont
    aciklamafont = fontaciklama
    skin = '<screen name="RenAy" position="0,0" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(720 * ver_carpan)) + '" title="Arayuz Ayarlari" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="' + str(int(40 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" zPosition="-10" size="' + str(int(1205 * ver_carpan)) + ',' + str(int(650 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <widget source="Title" render="Label" position="' + str(int(70 * ver_carpan)) + ',' + str(int(47 * ver_carpan)) + '" size="' + str(int(800 * ver_carpan)) + ',' + str(int(43 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(35 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(1103 * ver_carpan)) + ',' + str(int(46 * ver_carpan)) + '" size="' + str(int(140 * ver_carpan)) + ',' + str(int(60 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(50 * ver_carpan)) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(49 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(27 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(15 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" transparent="1" foregroundColor="' + str(fontcolor) + '">\n      <convert type="ClockToText">Format:%A</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(72 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(29 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(16 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%e. %b</convert>\n    </widget>\n    <widget name="config" position="' + str(int(70 * ver_carpan)) + ',' + str(int(120 * ver_carpan)) + '" size="' + str(int(710 * ver_carpan)) + ',' + str(int(490 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" itemHeight="' + str(int(32 * ver_carpan)) + '" zPosition="3" foregroundColor="' + str(menuust) + '" foregroundColorSelected="' + str(menufont) + '" scrollbarMode="showOnDemand" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" transparent="1" />\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/green_' + versiyon + '.png" position="' + str(int(70 * ver_carpan)) + ',' + str(int(635 * ver_carpan)) + '" size="' + str(int(30 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" alphatest="blend" />\n    <eLabel name="ayarlari_kaydet" text="KAYDET / SAVE" position="' + str(int(105 * ver_carpan)) + ',' + str(int(637 * ver_carpan)) + '" size="' + str(int(250 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" font="RegularTURKvod;' + str(int(20 * ver_carpan)) + '" halign="left" valign="top" transparent="1" />\n    <ePixmap position="' + str(int(911 * ver_carpan)) + ',' + str(int(252 * ver_carpan)) + '" size="' + str(int(256 * ver_carpan)) + ',' + str(int(256 * ver_carpan)) + '" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/skin_selector_' + versiyon + '.png" transparent="1" alphatest="blend" />\n  </screen>'

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
        self['actions'] = HelpableActionMap(self, 'turkvod', {'green': self.save,
         'back': self.back}, -1)
        self['ayarlari_kaydet'] = Label(par.get(Dil, '58'))
        self.list = []
        self['baslik'] = Label('                ' + par.get(Dil, '46'))
        self.list.append(getConfigListEntry(_('1  ' + par.get(Dil, '94')), config.plugins.TURKVOD.metrixzemin))
        self.list.append(getConfigListEntry(_('2  ' + par.get(Dil, '96')), config.plugins.TURKVOD.metrixrenk))
        self.list.append(getConfigListEntry(_('3  ' + par.get(Dil, '85')), config.plugins.TURKVOD.fontcolor))
        self.list.append(getConfigListEntry(_('4  ' + par.get(Dil, '99')), config.plugins.TURKVOD.fontlar))
        self.list.append(getConfigListEntry(_('5  ' + par.get(Dil, '86')), config.plugins.TURKVOD.menualtfontcolor))
        self.list.append(getConfigListEntry(_('6  ' + par.get(Dil, '87')), config.plugins.TURKVOD.menufontcolor))
        self.list.append(getConfigListEntry(_('7  ' + par.get(Dil, '89')), config.plugins.TURKVOD.fontliste))
        self.list.append(getConfigListEntry(_('8  ' + par.get(Dil, '90')), config.plugins.TURKVOD.fontaciklama))
        ConfigListScreen.__init__(self, self.list, session)

    def save(self):
        self.close()
        for x in self['config'].list:
            x[1].save()

    def back(self):
        self.close()
        for x in self['config'].list:
            x[1].save()


class modu():

    def __init__(self):
        self.video_liste = []
        self.next_page_url = ''
        self.next_page_text = ''
        self.prev_page_url = ''
        self.prev_page_text = ''
        self.search_text = ''
        self.playlistname = ''
        self.error = ''

    def reset_buttons(self):
        self.next_page_url = None
        self.next_page_text = ''
        self.prev_page_url = None
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = None
        return

    def get_list(self, url):
        debug(url, 'MODUL URL: ')
        self.reset_buttons()
        if url.find('m3u') > -1:
            parts = url.split('@')
            filename = parts[0]
            name = parts[2].encode('utf-8')
            self.playlistname = name
            ts = None
            if url.find('TS') > -1:
                ts = 'True'
            try:
                video_list_temp = []
                chan_counter = 0
                if filename.find('http') > -1:
                    url = filename.replace('http://', '')
                    myfile = mod_request(url)
                else:
                    myfile = open('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/%s' % filename, 'r').read()
                regex = re.findall('#EXTINF.*,(.*\\s)\\s*(.*)', myfile)
                if not len(regex) > 0:
                    regex = re.findall('((.*.+)(.*))', myfile)
                for text in regex:
                    title = text[0].strip()
                    url = text[1].strip()
                    chan_counter += 1
                    chan_tulpe = (chan_counter,
                     title,
                     '',
                     'xxx.png',
                     url,
                     None,
                     None,
                     '',
                     '',
                     None,
                     ts)
                    video_list_temp.append(chan_tulpe)
                    if len(video_list_temp) < 1:
                        print 'ERROR m3u CAT LIST_LEN = %s' % len(video_list_temp)

            except:
                print 'ERROR m3u'

            return video_list_temp
        elif url.find('TVTuner') > -1:
            try:
                debug(url, 'MODUL URL: ')
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                list = []
                video_list_temp = []
                self.playlistname = TURKvod + '  ' + 'TV'
                servis = eServiceCenter.getInstance()
                services = servis.list(eServiceReference('1:7:1:0:0:0:0:0:0:0:(type == 1) || (type == 17) || (type == 195) || (type == 25) FROM BOUQUET "bouquets.tv" ORDER BY bouquet'))
                if services:
                    pan = services.getContent('SN', True)
                    if page == 'start':
                        ne = (1, 'TURKvod FAVORILER', None, None, None, 'TURKvodModul@favoriler@start@modu@TURKvod', None, None, None, None, None)
                        video_list_temp.append(ne)
                    if page == 'start':
                        ne = (1, 'GENEL TV LISTESI', None, None, None, 'TURKvodModul@GenelTvTuner@start@modu@TURKvod', None, None, None, None, None)
                        video_list_temp.append(ne)
                    if page == 'start':
                        say = 2
                        ne = (2, 'GENEL RADIO LISTESI', None, None, None, 'TURKvodModul@TVRadio@start@modu@TURKvod', None, None, None, None, None)
                        video_list_temp.append(ne)
                        for bot in pan:
                            bo = bot[1].replace(':', '').replace('=', '').replace('-', '').replace('>', '').replace('<', '')
                            say = say + 1
                            lis = (say,
                             bo.strip(),
                             TURKvod + '  ' + 'TV',
                             None,
                             None,
                             'TURKvodModul@TVTuner' + bot[0] + '@vode',
                             None,
                             '',
                             '',
                             None,
                             None)
                            video_list_temp.append(lis)

                        return video_list_temp
                    services = page == 'vode' and servis.list(eServiceReference(url[7:]))
                    channels = services and services.getContent('SN', True)
                    self.playlistname = channels
                    for channel in channels:
                        if not channel[0].startswith('1:64:'):
                            list.append(channel[1].replace('\xc2\x86', '').replace('\xc2\x87', ''))

                    say = 0
                    for channel in channels:
                        try:
                            png = channel[0][:channel[0].index('::') + 1]
                        except:
                            png = channel[0]

                        say = say + 1
                        lis = (say,
                         channel[1],
                         TURKvod,
                         TURKvod_PATS + 'picons/' + png[:-1].replace(':', '_') + '.png',
                         'http://127.0.0.1:8001/' + channel[0],
                         None,
                         None,
                         TURKvod_PATS + 'picons/' + png[:-1].replace(':', '_') + '.png',
                         '',
                         None,
                         None)
                        video_list_temp.append(lis)

                    self.next_page_url = 'TURKvodModul@TVTuner@start@TURKvod'
                    self.next_page_text = 'Listeye Don'
            except:
                print 'ERROR'

            return video_list_temp
        elif url.find('TVRadio') > -1:
            try:
                debug(url, 'MODUL URL: ')
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                list = []
                video_list_temp = []
                self.playlistname = TURKvod + '  ' + 'RADIO'
                s_type = service_types_radio
                idbouquet = '%s ORDER BY bouquet' % s_type
                serviceHandler = eServiceCenter.getInstance()
                servis = eServiceCenter.getInstance()
                services = servis.list(eServiceReference(idbouquet))
                if services:
                    if page == 'start':
                        chan = services.getContent('SN', True)
                        say = 0
                        for channel in chan:
                            say = say + 1
                            name = channel[1].replace('\xc2\x86', '').replace('\xc2\x87', '')
                            ref = quote(channel[0], safe=" ~@%#$&()*!+=:;,.?/'")
                            lis = (say,
                             name,
                             None,
                             None,
                             'http://127.0.0.1:8001/' + ref,
                             None,
                             None,
                             None,
                             None,
                             None)
                            video_list_temp.append(lis)

                        self.next_page_url = 'TURKvodModul@TVTuner@start@TURKvod'
                        self.next_page_text = 'Listeye Don'
            except:
                print 'ERROR'

            return video_list_temp
        elif url.find('GenelTvTuner') > -1:
            try:
                debug(url, 'MODUL URL: ')
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                video_list_temp = []
                self.playlistname = TURKvod + '  ' + 'TV GENEL LISTE'
                s_type = service_types_tv
                idbouquet = '%s ORDER BY bouquet' % s_type
                serviceHandler = eServiceCenter.getInstance()
                servis = eServiceCenter.getInstance()
                services = servis.list(eServiceReference(idbouquet))
                if services:
                    if page == 'start':
                        chan = services.getContent('SN', True)
                        say = 0
                        for channel in chan:
                            say = say + 1
                            name = channel[1].replace('\xc2\x86', '').replace('\xc2\x87', '')
                            ref = quote(channel[0], safe=" ~@%#$&()*!+=:;,.?/'")
                            lis = (say,
                             name,
                             None,
                             None,
                             'http://127.0.0.1:8001/' + ref,
                             None,
                             None,
                             None,
                             None,
                             None)
                            video_list_temp.append(lis)

                        self.next_page_url = 'TURKvodModul@TVTuner@start@TURKvod'
                        self.next_page_text = 'Listeye Don'
            except:
                print 'ERROR'

            return video_list_temp
        elif url.find('favoriler') > -1:
            try:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                video_list_temp = []
                self.playlistname = TURKvod + '  ' + 'FAVORILER'
                if page == 'start':
                    f = open(PLUGIN_PATH + '/tv', 'r')
                    op = f.read()
                    f.close()
                    regex2 = re.findall('<tr>(.*?)</tr>\\W*<url>(.*?)</url>', op)
                    say = 0
                    for text in regex2:
                        png = text[1].replace('http://127.0.0.1:8001/', '')
                        name = text[0]
                        ref = text[1]
                        res = png[:-1].replace(':', '_') + '.png'
                        say += 1
                        lis = (say,
                         name,
                         TURKvod,
                         TURKvod_PATS + 'picons/' + res,
                         ref,
                         None,
                         None,
                         TURKvod_PATS + 'picons/' + res,
                         None,
                         None,
                         None)
                        video_list_temp.append(lis)

            except:
                print 'ERROR'

            return video_list_temp
        else:
            return
            return


class VirtualKeyBoardList(MenuList):

    def __init__(self, list, enableWrapAround = False):
        MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
        self.l.setFont(0, gFont('RegularTURKvod', int(18 * ver_carpan)))
        self.l.setItemHeight(int(35 * ver_carpan))


def VirtualKeyBoardEntryComponent(keys, selectedKey, shiftMode = False):
    key_backspace = LoadPixmap(cached=True, path='%s/img/vkey_backspace.png' % PLUGIN_PATH)
    key_bg = LoadPixmap(cached=True, path='%s/img/vkey_bg.png' % PLUGIN_PATH)
    key_clr = LoadPixmap(cached=True, path='%s/img/vkey_clr.png' % PLUGIN_PATH)
    key_esc = LoadPixmap(cached=True, path='%s/img/vkey_esc.png' % PLUGIN_PATH)
    key_ok = LoadPixmap(cached=True, path='%s/img/vkey_ok.png' % PLUGIN_PATH)
    key_info = LoadPixmap(cached=True, path='%s/img/vkey_info.png' % PLUGIN_PATH)
    key_sel = LoadPixmap(cached=True, path='%s/img/vkey_sel.png' % PLUGIN_PATH)
    key_shift = LoadPixmap(cached=True, path='%s/img/vkey_shift_sel.png' % PLUGIN_PATH)
    key_shift_sel = LoadPixmap(cached=True, path='%s/img/vkey_shift.png' % PLUGIN_PATH)
    key_space = LoadPixmap(cached=True, path='%s/img/vkey_space.png' % PLUGIN_PATH)
    res = [keys]
    x = 0
    count = 0
    if shiftMode:
        shiftkey_png = key_shift_sel
    else:
        shiftkey_png = key_shift
    for key in keys:
        width = None
        if key == 'EXIT':
            width = key_esc.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_esc))
        elif key == 'BACKSPACE':
            width = key_backspace.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_backspace))
        elif key == 'CLEAR':
            width = key_clr.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_clr))
        elif key == 'SHIFT':
            width = shiftkey_png.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=shiftkey_png))
        elif key == 'SPACE':
            width = key_space.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_space))
        elif key == 'OK':
            width = key_ok.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_ok))
        elif key == 'INFO':
            width = key_info.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_info))
        else:
            width = key_bg.size().width()
            res.extend((MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_bg), MultiContentEntryText(pos=(x, 0), size=(width, int(45 * ver_carpan)), font=0, text=key.encode('utf-8'), flags=RT_HALIGN_CENTER | RT_VALIGN_CENTER)))
        if selectedKey == count:
            width = key_sel.size().width()
            res.append(MultiContentEntryPixmapAlphaTest(pos=(x, 0), size=(width, int(45 * ver_carpan)), png=key_sel))
        if width is not None:
            x += width
        else:
            x += int(45 * ver_carpan)
        count += 1

    return res


dos = PLUGIN_PATH + '/list.bk'

class KeyBoard(Screen):
    fontcolor = fontcolorfont
    menufont = menufontcolor
    menuust = menuustfontcolor
    menufontt = mfont
    aciklamafont = fontaciklama
    skin = '<screen name="KeyBoard" position="0,0" size="' + str(int(1280 * ver_carpan)) + ',' + str(int(720 * ver_carpan)) + '" zPosition="99" title="Virtual KeyBoard" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="' + str(int(40 * ver_carpan)) + ',' + str(int(25 * ver_carpan)) + '" zPosition="-10" size="' + str(int(1205 * ver_carpan)) + ',' + str(int(650 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(1103 * ver_carpan)) + ',' + str(int(46 * ver_carpan)) + '" size="' + str(int(140 * ver_carpan)) + ',' + str(int(60 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(50 * ver_carpan)) + '" halign="left" backgroundColor="' + metrixBackground + '" transparent="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(49 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(27 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(15 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" transparent="1" foregroundColor="' + str(fontcolor) + '">\n      <convert type="ClockToText">Format:%A</convert>\n    </widget>\n    <widget source="global.CurrentTime" render="Label" position="' + str(int(931 * ver_carpan)) + ',' + str(int(72 * ver_carpan)) + '" size="' + str(int(161 * ver_carpan)) + ',' + str(int(29 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(16 * ver_carpan)) + '" halign="right" backgroundColor="' + metrixBackground + '" foregroundColor="' + str(fontcolor) + '" transparent="1">\n      <convert type="ClockToText">Format:%e. %b</convert>\n    </widget>\n    <eLabel text="Virtual KeyBoard" position="' + str(int(70 * ver_carpan)) + ',' + str(int(47 * ver_carpan)) + '" size="' + str(int(800 * ver_carpan)) + ',' + str(int(43 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(35 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget name="header" position="' + str(int(70 * ver_carpan)) + ',' + str(int(130 * ver_carpan)) + '" size="' + str(int(700 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(28 * ver_carpan)) + '" halign="center" transparent="1" noWrap="1" />\n    <eLabel position="' + str(int(70 * ver_carpan)) + ',' + str(int(210 * ver_carpan)) + '" size="' + str(int(700 * ver_carpan)) + ',' + str(int(60 * ver_carpan)) + '" zPosition="1" backgroundColor="#00ffffff" />\n    <eLabel position="' + str(int(72 * ver_carpan)) + ',' + str(int(212 * ver_carpan)) + '" size="' + str(int(696 * ver_carpan)) + ',' + str(int(56 * ver_carpan)) + '" zPosition="2" backgroundColor="' + metrixBackground + '" />\n    <widget name="text" position="' + str(int(80 * ver_carpan)) + ',' + str(int(224 * ver_carpan)) + '" size="' + str(int(680 * ver_carpan)) + ',' + str(int(44 * ver_carpan)) + '" zPosition="3" font="RegularTURKvod;' + str(int(30 * ver_carpan)) + '" noWrap="1" halign="right" />\n    <widget name="list" position="' + str(int(72 * ver_carpan)) + ',' + str(int(330 * ver_carpan)) + '" size="' + str(int(820 * ver_carpan)) + ',' + str(int(350 * ver_carpan)) + '" selectionDisabled="1" transparent="1" />\n    <ePixmap position="' + str(int(920 * ver_carpan)) + ',' + str(int(230 * ver_carpan)) + '" size="' + str(int(256 * ver_carpan)) + ',' + str(int(256 * ver_carpan)) + '" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/keyb_' + versiyon + '.png" transparent="1" alphatest="blend" />\n  </screen>'

    def __init__(self, session, title = '', text = ''):
        Screen.__init__(self, session)
        self.keys_list = []
        self.shiftkeys_list = []
        self.lang = language.getLanguage()
        if config.plugins.TURKVOD.klevye.value == 'TR':
            self.keys_list = [[u'EXIT',
              u'1',
              u'2',
              u'3',
              u'4',
              u'5',
              u'6',
              u'7',
              u'8',
              u'9',
              u'0',
              u'BACKSPACE'],
             [u'A',
              u'B',
              u'C',
              u'\xc7',
              u'D',
              u'E',
              u'F',
              u'G',
              u'\u011e',
              u'H',
              u'I',
              u'\u0130'],
             [u'J',
              u'K',
              u'L',
              u'M',
              u'N',
              u'O',
              u'\xd6',
              u'P',
              u'R',
              u'S',
              u'\u015e',
              u'T'],
             [u'U',
              u'\xdc',
              u'V',
              u'Y',
              u'Z',
              u'W',
              u'Q',
              u'X',
              u'/',
              u'.',
              u'+',
              u'-'],
             [u'SHIFT',
              u'SPACE',
              u'OK',
              u'INFO']]
            self.shiftkeys_list = [[u'EXIT',
              u'1',
              u'2',
              u'3',
              u'4',
              u'5',
              u'6',
              u'7',
              u'8',
              u'9',
              u'0',
              u'BACKSPACE'],
             [u'a',
              u'b',
              u'c',
              u'\xe7',
              u'd',
              u'e',
              u'f',
              u'g',
              u'\u011f',
              u'h',
              u'\u0131',
              u'i'],
             [u'j',
              u'k',
              u'l',
              u'm',
              u'n',
              u'o',
              u'\xf6',
              u'p',
              u'r',
              u's',
              u'\u015f',
              u't'],
             [u'u',
              u'\xfc',
              u'v',
              u'y',
              u'z',
              u'w',
              u'q',
              u'x',
              u'/',
              u'.',
              u'+',
              u'-'],
             [u'SHIFT',
              u'SPACE',
              u'OK',
              u'INFO']]
        if config.plugins.TURKVOD.klevye.value == 'EN':
            self.keys_list = [[u'EXIT',
              u'1',
              u'2',
              u'3',
              u'4',
              u'5',
              u'6',
              u'7',
              u'8',
              u'9',
              u'0',
              u'BACKSPACE'],
             [u'q',
              u'w',
              u'e',
              u'r',
              u't',
              u'z',
              u'u',
              u'i',
              u'o',
              u'p',
              u'+',
              u'@'],
             [u'a',
              u's',
              u'd',
              u'f',
              u'g',
              u'h',
              u'j',
              u'k',
              u'l',
              u'#',
              u'\\'],
             [u'<',
              u'y',
              u'x',
              u'c',
              u'v',
              u'b',
              u'n',
              u'm',
              u',',
              '.',
              u'-',
              u'CLEAR'],
             [u'SHIFT',
              u'SPACE',
              u'OK',
              u'INFO']]
            self.shiftkeys_list = [[u'EXIT',
              u'!',
              u'"',
              u'\xa7',
              u'$',
              u'%',
              u'&',
              u'/',
              u'(',
              u')',
              u'=',
              u'BACKSPACE'],
             [u'Q',
              u'W',
              u'E',
              u'R',
              u'T',
              u'Z',
              u'U',
              u'I',
              u'O',
              u'P',
              u'*'],
             [u'A',
              u'S',
              u'D',
              u'F',
              u'G',
              u'H',
              u'J',
              u'K',
              u'L',
              u"'",
              u'?'],
             [u'>',
              u'Y',
              u'X',
              u'C',
              u'V',
              u'B',
              u'N',
              u'M',
              u';',
              u':',
              u'_',
              u'CLEAR'],
             [u'SHIFT',
              u'SPACE',
              u'OK',
              u'INFO']]
        if config.plugins.TURKVOD.klevye.value == 'RUS':
            self.keys_list = [[u'EXIT',
              u'1',
              u'2',
              u'3',
              u'4',
              u'5',
              u'6',
              u'7',
              u'8',
              u'9',
              u'0',
              u'BACKSPACE'],
             ['\xd0\x90',
              '\xd0\x91',
              '\xd0\x92',
              '\xd0\x93',
              '\xd0\x94',
              '\xd0\x95',
              '\xd0\x96',
              '\xd0\x97',
              '\xd0\x98',
              '\xd0\x99',
              '\xd0\x9a',
              '\xd0\x9b'],
             ['\xd0\x9c',
              '\xd0\x9d',
              '\xd0\x9e',
              '\xd0\x9f',
              '\xd0\xa0',
              '\xd0\xa1',
              '\xd0\xa2',
              '\xd0\xa3',
              '\xd0\xa4',
              '\xd0\xa5',
              '\xd0\xa6',
              '\xd0\xa7'],
             ['\xd0\xa8',
              '\xd0\xa9',
              '\xd0\xaa',
              '\xd0\xab',
              '\xd0\xac',
              '\xd0\xad',
              '\xd0\xae',
              '\xd0\xaf',
              u'.',
              u',',
              u'*',
              u'CLEAR'],
             [u'SHIFT',
              u'SPACE',
              u'OK',
              u'INFO']]
            self.shiftkeys_list = [[u'EXIT',
              u'!',
              u'"',
              u'\xa7',
              u'$',
              u'%',
              u'&',
              u'/',
              u'(',
              u')',
              u'=',
              u'BACKSPACE'],
             [u'Q',
              u'W',
              u'E',
              u'R',
              u'T',
              u'Z',
              u'U',
              u'I',
              u'O',
              u'P',
              u'?',
              u'#'],
             [u'A',
              u'S',
              u'D',
              u'F',
              u'G',
              u'H',
              u'J',
              u'K',
              u'L',
              u"'",
              u';',
              u':'],
             [u'>',
              u'Y',
              u'X',
              u'C',
              u'V',
              u'B',
              u'N',
              u'M',
              u'<',
              u'+',
              u'-',
              u'CLEAR'],
             [u'SHIFT', u'SPACE', u'OK'],
             u'INFO']
        self.shiftMode = False
        self.text = text
        self.selectedKey = 0
        self['header'] = Label(title)
        self['text'] = Label(self.text)
        self['list'] = VirtualKeyBoardList([])
        self['actions'] = ActionMap(['OkCancelActions', 'WizardActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.exit,
         'left': self.left,
         'right': self.right,
         'up': self.up,
         'down': self.down,
         'red': self.clear,
         'yellow': self.info,
         'green': self.ok,
         'blue': self.shiftClicked}, -2)
        self.onLayoutFinish.append(self.buildVirtualKeyBoard)
        self.max_key = 47 + len(self.keys_list[4])

    def shiftClicked(self):
        if self.shiftMode:
            self.shiftMode = False
        else:
            self.shiftMode = True
        self.buildVirtualKeyBoard(self.selectedKey)

    def buildVirtualKeyBoard(self, selectedKey = 0):
        list = []
        if self.shiftMode:
            self.k_list = self.shiftkeys_list
            for keys in self.k_list:
                if selectedKey < 12 and selectedKey > -1:
                    list.append(VirtualKeyBoardEntryComponent(keys, selectedKey, True))
                else:
                    list.append(VirtualKeyBoardEntryComponent(keys, -1, True))
                selectedKey -= 12

        else:
            self.k_list = self.keys_list
            for keys in self.k_list:
                if selectedKey < 12 and selectedKey > -1:
                    list.append(VirtualKeyBoardEntryComponent(keys, selectedKey))
                else:
                    list.append(VirtualKeyBoardEntryComponent(keys, -1))
                selectedKey -= 12

        self['list'].setList(list)

    def backClicked(self):
        self.text = self['text'].getText()
        self.text = unicode(self.text)[:-1]
        self.text = self.text.encode('utf-8')
        self['text'].setText(self.text)

    def okClicked(self):
        if self.shiftMode:
            list = self.shiftkeys_list
        else:
            list = self.keys_list
        selectedKey = self.selectedKey
        text = None
        for x in list:
            if selectedKey < 12:
                if selectedKey < len(x):
                    text = x[selectedKey]
                break
            else:
                selectedKey -= 12

        if text is None:
            return
        else:
            text = text.encode('utf-8')
            if text == 'EXIT':
                self.close(None)
            elif text == 'BACKSPACE':
                self.text = self['text'].getText()
                self.text = unicode(self.text)[:-1]
                self.text = self.text.encode('utf-8')
                self['text'].setText(self.text)
            elif text == 'CLEAR':
                self.text = ''
                self['text'].setText(self.text)
            elif text == 'SHIFT':
                if self.shiftMode:
                    self.shiftMode = False
                else:
                    self.shiftMode = True
                self.buildVirtualKeyBoard(self.selectedKey)
            elif text == 'SPACE':
                self.text += ' '
                self['text'].setText(self.text)
            elif text == 'OK':
                ac = open(dos, 'r')
                lines = ac.readlines()
                ac.close()
                ac = open(dos, 'w')
                current_search = self['text'].getText()
                count = 0
                ac.write(current_search + '\n')
                count += 1
                for line in lines:
                    count += 1
                    if line.strip('\n') != current_search and len(line) > 2 and count < 21:
                        ac.write(line)

                ac.close()
                self.close(current_search)
            elif text == 'INFO':
                ac = open(dos, 'r')
                self.texts = ac.readlines()
                ac.close()
                self.session.openWithCallback(self.acSel, TurkvodSearch, texts=self.texts)
            else:
                self.text = self['text'].getText()
                self.text += text
                self['text'].setText(self.text)
            return

    def ok(self):
        ac = open(dos, 'r')
        lines = ac.readlines()
        ac.close()
        ac = open(dos, 'w')
        current_search = self['text'].getText()
        count = 0
        ac.write(current_search + '\n')
        count += 1
        for line in lines:
            count += 1
            if line.strip('\n') != current_search and len(line) > 2 and count < 21:
                ac.write(line)

        ac.close()
        self.close(current_search)

    def exit(self):
        self.close(None)
        return

    def info(self):
        ac = open(dos, 'r')
        self.texts = ac.readlines()
        ac.close()
        self.session.openWithCallback(self.acSel, TurkvodSearch, texts=self.texts)

    def acSel(self, position = 0):
        try:
            if position > -1:
                self['text'].setText(self.texts[position].strip('\n'))
        except Exception as ex:
            print ex

    def clear(self):
        self.text = ''
        self['text'].setText(self.text)

    def left(self):
        self.selectedKey -= 1
        if self.selectedKey == -1:
            self.selectedKey = 11
        elif self.selectedKey == 11:
            self.selectedKey = 23
        elif self.selectedKey == 23:
            self.selectedKey = 35
        elif self.selectedKey == 35:
            self.selectedKey = 47
        elif self.selectedKey == 47:
            self.selectedKey = self.max_key
        self.showActiveKey()

    def right(self):
        self.selectedKey += 1
        if self.selectedKey == 12:
            self.selectedKey = 0
        elif self.selectedKey == 24:
            self.selectedKey = 12
        elif self.selectedKey == 36:
            self.selectedKey = 24
        elif self.selectedKey == 48:
            self.selectedKey = 36
        elif self.selectedKey > self.max_key:
            self.selectedKey = 48
        self.showActiveKey()

    def up(self):
        self.selectedKey -= 12
        if self.selectedKey < 0 and self.selectedKey > self.max_key - 60:
            self.selectedKey += 48
        elif self.selectedKey < 0:
            self.selectedKey += 60
        self.showActiveKey()

    def down(self):
        self.selectedKey += 12
        if self.selectedKey > self.max_key and self.selectedKey > 59:
            self.selectedKey -= 60
        elif self.selectedKey > self.max_key:
            self.selectedKey -= 48
        self.showActiveKey()

    def showActiveKey(self):
        self.buildVirtualKeyBoard(self.selectedKey)


class TurkvodSearch(Screen):
    fontcolor = fontcolorfont
    menufont = menufontcolor
    menuust = menuustfontcolor
    menufontt = mfont
    aciklamafont = fontaciklama
    skin = '<screen name="TurkvodSearch" position="' + str(int(880 * ver_carpan)) + ',0" size="' + str(int(400 * ver_carpan)) + ',' + str(int(723 * ver_carpan)) + '" title="ARAMA LISTESI" flags="wfNoBorder" backgroundColor="transparent">\n    <eLabel position="0,0" zPosition="-10" size="' + str(int(400 * ver_carpan)) + ',' + str(int(723 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" />\n    <eLabel text="ARAMA LISTESI" position="' + str(int(22 * ver_carpan)) + ',' + str(int(44 * ver_carpan)) + '" size="' + str(int(350 * ver_carpan)) + ',' + str(int(43 * ver_carpan)) + '" font="RegularTURKvod;' + str(int(35 * ver_carpan)) + '" backgroundColor="' + metrixBackground + '" transparent="1" />\n    <widget name="selection" position="' + str(int(24 * ver_carpan)) + ',' + str(int(110 * ver_carpan)) + '" size="' + str(int(350 * ver_carpan)) + ',' + str(int(520 * ver_carpan)) + '" zPosition="3" font="RegularTURKvod;' + str(int(24 * ver_carpan)) + '" itemHeight="' + str(int(30 * ver_carpan)) + '" foregroundColorSelected="' + str(menufont) + '" scrollbarMode="showOnDemand" foregroundColor="' + str(menuust) + '" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/clear.png" enableWrapAround="1" transparent="1" />\n    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/img/red_' + versiyon + '.png" position="' + str(int(14 * ver_carpan)) + ',' + str(int(660 * ver_carpan)) + '" size="' + str(int(30 * ver_carpan)) + ',' + str(int(40 * ver_carpan)) + '" alphatest="blend" />\n    <eLabel text="Sil" position="' + str(int(56 * ver_carpan)) + ',' + str(int(660 * ver_carpan)) + '" size="' + str(int(250 * ver_carpan)) + ',' + str(int(28 * ver_carpan)) + '" zPosition="10" font="RegularTURKvod;' + str(int(24 * ver_carpan)) + '" foregroundColor="' + str(fontcolor) + '" halign="left" valign="top" transparent="1" />\n  </screen>'

    def __init__(self, session, texts = None):
        Screen.__init__(self, session)
        self.texts = []
        self['actions'] = HelpableActionMap(self, 'TURKvodPlayerVod', {'KEY_EXIT': self.exit,
         'kayit': self.deleter,
         'KEY_OK': self.ok}, -1)
        for x in range(len(texts)):
            self.texts.append('%i. %s' % (x + 1, texts[x]))

        self['selection'] = MenuList(self.texts)

    def ok(self):
        self.close(self['selection'].l.getCurrentSelectionIndex())

    def deleter(self):
        ac = open(dos, 'r')
        lines = ac.readlines()
        ac.close()
        ac = open(dos, 'w')
        count = -1
        selected_index = self['selection'].l.getCurrentSelectionIndex()
        for line in lines:
            count += 1
            if count != selected_index:
                ac.write(line)

        ac.close()
        self.close(None)
        return

    def exit(self):
        self.close(None)
        return