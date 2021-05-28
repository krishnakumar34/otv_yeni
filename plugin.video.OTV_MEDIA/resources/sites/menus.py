# -*- coding: utf-8 -*-

'''
    AdultFlix XXX Addon (18+) for the Kodi Media Center
    Kodi is a registered trademark of the XBMC Foundation.
    We are not connected to or in any other way affiliated with Kodi - DMCA: legal@tvaddons.co
    Support: https://github.com/tvaddonsco/plugin.video.adultflix

        License summary below, for more details please read license.txt file

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

#-*- coding: utf-8 -*-
import urllib2, urllib,cookielib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
from resources.lib.otvhelper import  gegetUrl,getUrl ,alfabekodla
from resources.lib.config import cConfig
import requests
import re,xbmcgui,unicodedata              
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import Parser as cParser
from resources.lib.comaddon import progress, VSlog
from resources.lib.player import cPlayer
from resources.lib.kplayer  import Player
from resources.lib.gui.guiElement import cGuiElement
import os
from packlib import kodi
from resources.lib.modules import local_utils
from kodi_six import xbmc
from scrapers import *
from scrapers import __all__
SITE_IDENTIFIER = 'menus'
buildDirectory = local_utils.buildDir
specific_icon = xbmc.translatePath(os.path.join('special://home/addons/script.adultflix.artwork/resources/art/', '%s/icon.png'))
specific_fanart = xbmc.translatePath(os.path.join('special://home/addons/script.adultflix.artwork/resources/art/', '%s/fanart.jpg'))



def mainMenu():
    oGui = cGui()
    art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.OTV_MEDIA/resources/art/', 'main/%s.png'))



    liste = []
    liste.append( ['Search...','search','search'] ) 
    liste.append( ['Live Cams','cams','webcams'] ) 

    liste.append( ['Tubes','tubes','tubes'] )
    liste.append( ['Scenes','scenes','scenes']) 
    liste.append( ['Movies','movies','movies']) 
    liste.append( ['Virtual Reality','virtualReality','vr'] ) 
    liste.append( ['Hentai','hentai','hentai'] )
    liste.append( ['Vintage','vintage','vintage'] )
    liste.append( ['Fetish','fetish','fetish'] ) 
    liste.append( ['Pictures','pictures','pics'] )
    liste.append( ['Comics','comics','comics'] )
    for sTitle,sUrl,img in liste:

        icon = art % img
        fanart = kodi.addonfanart
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', icon)
        oGui.addMovie(SITE_IDENTIFIER,sUrl ,sTitle, icon , icon , '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


@local_utils.url_dispatcher.register('37')
def cams():
    sources = __all__
    cam_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources]
    for i in sources:
        try:
            if eval(i + ".type") == 'cam':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i)
                cam_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if cam_sources:
        dirlst = []
        for i in sorted(cam_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('4')
def tubes():
    sources = __all__
    video_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources if i != 'chaturbate']
    for i in sources:
        try:
            if eval(i + ".type") == 'video':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i)
                video_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if video_sources:
        dirlst = []
        for i in sorted(video_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('36')
def scenes():
    sources = __all__
    scene_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources if i != 'chaturbate']
    for i in sources:
        try:
            if eval(i + ".type") == 'scenes':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i)
                scene_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if scene_sources:
        dirlst = []
        for i in sorted(scene_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('43')
def movies():
    sources = __all__
    movies_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources]
    for i in sources:
        try:
            if eval(i + ".type") == 'movies':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i.replace('_movies', ''))
                movies_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if movies_sources:
        dirlst = []
        for i in sorted(movies_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[0].lower(),
                 'fanart': specific_fanart % i[0].lower(), 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('39')
def hentai():
    sources = __all__
    hentai_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources]
    for i in sources:
        try:
            if eval(i + ".type") == 'hentai':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i)
                hentai_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if hentai_sources:
        dirlst = []
        for i in sorted(hentai_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('41')
def comics():
    sources = __all__
    comics_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources]
    for i in sources:
        try:
            if eval(i + ".type") == 'comics':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".pic_men_mode"))
                art_dir.append(i)
                comics_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if comics_sources:
        dirlst = []
        for i in sorted(comics_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('40')
def fetish():
    sources = __all__
    fetish_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources]
    for i in sources:
        try:
            if eval(i + ".type") == 'fetish':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i)
                fetish_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if fetish_sources:
        dirlst = []
        for i in sorted(fetish_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('42')
def virtualReality():
    sources = __all__
    vr_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources]
    for i in sources:
        try:
            if eval(i + ".type") == 'vr':
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i)
                vr_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if vr_sources:
        dirlst = []
        for i in sorted(vr_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)


@local_utils.url_dispatcher.register('35')
def pictures():
    sources = __all__
    picture_sources = []
    base_name = []
    menu_mode = []
    art_dir = []
    sources = [i for i in sources if i != 'chaturbate']
    for i in sources:
        try:
            if eval(i + ".pictures_tag") == 1:
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".pic_men_mode"))
                art_dir.append(i)
                picture_sources = zip(base_name, menu_mode, art_dir)
        except:
            pass

    if picture_sources:
        dirlst = []
        for i in sorted(picture_sources):
            dirlst.append(
                {'name': kodi.giveColor(i[0], 'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2],
                 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)
