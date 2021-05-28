# -*- coding: utf-8 -*-
import base64
import re
import sys
import six
from six.moves.urllib.parse import urljoin, unquote_plus, quote_plus, quote, unquote
from six.moves import zip
import json
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
from resources.modules import control, client
from resources.sites.LIVETV2 import *
ADDON = xbmcaddon.Addon()
ADDON_DATA = ADDON.getAddonInfo('profile')
ADDON_PATH = ADDON.getAddonInfo('path')
DESCRIPTION = ADDON.getAddonInfo('description')
FANART = ADDON.getAddonInfo('fanart')
ICON = ADDON.getAddonInfo('icon')
ID = ADDON.getAddonInfo('id')
NAME = ADDON.getAddonInfo('name')
VERSION = ADDON.getAddonInfo('version')
Lang = ADDON.getLocalizedString
Dialog = xbmcgui.Dialog()
vers = VERSION
ART = ADDON_PATH + "/resources/icons/"

BASEURL = 'http://www.sporthd.live/'
Live_url = 'http://www.sporthd.live/index.php?'
headers = {'User-Agent': client.agent(),
           'Referer': BASEURL}

from dateutil.parser import parse
from dateutil.tz import gettz
from dateutil.tz import tzlocal
SITE_IDENTIFIER = 'ssport365'
# reload(sys)
# sys.setdefaultencoding("utf-8")
iconimage = ICON

fanart = FANART
description = DESCRIPTION
query = None

#######################################
# Time and Date Helpers
#######################################
try:
    local_tzinfo = tzlocal()
    locale_timezone = json.loads(xbmc.executeJSONRPC(
        '{"jsonrpc": "2.0", "method": "Settings.GetSettingValue", "params": {"setting": "locale.timezone"}, "id": 1}'))
    if locale_timezone['result']['value']:
        local_tzinfo = gettz(locale_timezone['result']['value'])
except:
    pass


def convDateUtil(timestring, newfrmt='default', in_zone='UTC'):
    if newfrmt == 'default':
        newfrmt = xbmc.getRegion('time').replace(':%S', '')
    try:
        in_time = parse(timestring)
        in_time_with_timezone = in_time.replace(tzinfo=gettz(in_zone))
        local_time = in_time_with_timezone.astimezone(local_tzinfo)
        return local_time.strftime(newfrmt)
    except:
        return timestring
           
              
def Main_menu():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', Live_url)
    oGui.addDir(SITE_IDENTIFIER, 'getevents', 'LIVE EVENTS', 'turkey-free-iptv.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', Live_url)
    oGui.addDir(SITE_IDENTIFIER, 'sportsmenu', 'SPORTS', 'turkey-free-iptv.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', Live_url)
    oGui.addDir(SITE_IDENTIFIER, 'leaguesmenu', 'BEST LEAGUES', 'turkey-free-iptv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def leaguesmenu():
    oGui = cGui()                           
    liste = []
    liste.append( ['Uefa Champions League','index.php?champ=uefa-champions-league','flags/uefa-champions-league.png'] )
    liste.append( ['Uefa Europa League','index.php?champ=uefa-europa-league','flags/uefa-europa-league.png'] )
    liste.append( ['Premier League','index.php?champ=premier-league','flags/premier-league.png'] )
    liste.append( ['Bundesliga','index.php?champ=bundesliga','flags/bundesliga.png'] )
    liste.append( ['Laliga','index.php?champ=laliga','flags/spanish-primera-division.png'] )
    liste.append( ['Serie A','index.php?champ=serie-a','flags/serie-a.png'] )
    liste.append( ['France Ligue 1','index.php?champ=france-ligue-1','flags/france-ligue-1.png'] )
    liste.append( ['Eredivisie','index.php?champ=eredivisie','flags/eredivisie.png'] )
    liste.append( ['Australian A League','index.php?champ=australian-a-league','flags/australian-a-league.png'] )
    liste.append( ['MLS','index.php?champ=mls','flags/mls.png'] )
    liste.append( ['Rugby Top 14','index.php?champ=rugby-top-14','flags/rugby-top-14.png'] )
    liste.append( ['Greece Super League','index.php?champ=greece-super-league','flags/greece-super-league.png'] )
    liste.append( ['Argentina Superliga','index.php?champ=argentina-superliga','flags/argentina-superliga.png'] )
    liste.append( ['Portuguese Primeira Liga','index.php?champ=portuguese-primeira-liga','flags/portuguese-primeira-liga.png'] )
    liste.append( ['Primera Division Apertura','index.php?champ=primera-division-apertura','flags/primera-division-apertura.png'] )
    liste.append( ['Bundesliga 2','index.php?champ=bundesliga-2','flags/bundesliga-2.png'] )
    liste.append( ['Greece Super League 2','index.php?champ=greece-super-league-2','flags/greece-super-league-2.png'] )
    liste.append( ['Belarus Vysheyshaya Liga','index.php?champ=belarus-vysheyshaya-liga','flags/belarus-vysheyshaya-liga.png'] )
    for sTitle,sUrl,Pic in liste:
        sUrl2= BASEURL +sUrl             
        sPicture= BASEURL + Pic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oGui.addTV(SITE_IDENTIFIER, 'getevents', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
                        
def sportsmenu():
    oGui = cGui()                           
    liste = []
    liste.append( ['Football', 'type=football','images/football.png'] )
    liste.append( ['Basketball','type=basketball', 'images/basketball.png'] )
    liste.append( ['MotorSport','type=motorsport', 'images/motorsport.png'] )
    liste.append( ['Handball','type=handball','images/handball.png'] )
    liste.append( ['Rugby','type=rugby','images/rugby.png'] )
    liste.append( ['NFL','type=nfl','images/nfl.png'] )
    liste.append( ['UFC','type=ufc','images/ufc.png'] )
    liste.append( ['Wrestling','type=wresling','images/wresling.png'] )
    liste.append( ['Hockey','type=hokey', 'images/hockey.png'] )
    liste.append( ['Volleyball','type=volleyball','images/volleyball.png'] )
    liste.append( ['Darts','type=darts','images/darts.png'] )
    liste.append( ['Tennis','type=tennis','images/tennis.png'] )
    liste.append( ['Boxing','type=boxing','images/boxing.png'] )
    liste.append( ['Cricket','type=cricket', 'images/cricket.png'] )
    liste.append( ['Baseball','type=baseball','images/baseball.png'] )
    liste.append( ['Snooker','type=snooker','images/snooker.png'] )
    liste.append( ['Chess','type=chess','images/chess.png'] )
    for sTitle,sUrl,Pic in liste:
        sUrl2= Live_url +sUrl             
        sPicture= BASEURL + Pic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oGui.addTV(SITE_IDENTIFIER, 'getevents', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
def getevents():  # 5
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')

    data = client.request(url)
    # xbmc.log('@#@EDATAAA: {}'.format(data), xbmc.LOGNOTICE)
    events = list(zip(client.parseDOM(str(data), 'li', attrs={'class': "item itemhov"}),
                      re.findall(r'<i class="material-icons">(.+?)</a> </li>', str(data), re.DOTALL)))
    # addDir('[COLORcyan]Time in GMT+2[/COLOR]', '', 'BUG', ICON, FANART, '')
    for event, streams in events:
        # xbmc.log('@#@EVENTTTTT:%s' % event, xbmc.LOGNOTICE)
        watch = '[COLORlime]*[/COLOR]' if '>Live<' in event else '[COLORred]*[/COLOR]'
        try:
            teams = client.parseDOM(event, 'td')
            # xbmc.log('@#@TEAMSSSS:%s' % str(teams), xbmc.LOGNOTICE)
            home, away = re.sub(r'\s*(<img.+?>)\s*', '', teams[0]), re.sub(r'\s*(<img.+?>)\s*', '', teams[2])
            if six.PY2:
                home = home.strip().encode('utf-8')
                away = away.strip().encode('utf-8')
            teams = '[B]{0} vs {1}[/B]'.format(home, away)
        except IndexError:
            teams = client.parseDOM(event, 'center')[0]
            teams = re.sub(r'<.+?>|\s{2}', '', teams)
            teams = teams.encode('utf-8') if six.PY2 else teams
            teams = '[B]{}[/B]'.format(teams)
        # xbmc.log('@#@TEAM-FINAL:%s' % str(teams), xbmc.LOGNOTICE)
        lname = client.parseDOM(event, 'a')[1]
        lname = re.sub(r'<.+?>', '', lname)
        time = client.parseDOM(event, 'span', attrs={'class': 'gmt_m_time'})[0]
        time = time.split('GMT')[0].strip()
        cov_time = convDateUtil(time, 'default', 'GMT{}'.format(str(control.setting('timezone'))))
        # xbmc.log('@#@COVTIMEEE:%s' % str(cov_time), xbmc.LOGNOTICE)
        ftime = '[COLORgold][I]{}[/COLOR][/I]'.format(cov_time)
        name = '{0}{1} {2} - [I]{3}[/I]'.format(watch, ftime, teams, lname)

        # links = re.findall(r'<a href="(.+?)".+?>( Link.+? )</a>', event, re.DOTALL)
        streams = str(quote(base64.b64encode(six.ensure_binary(streams))))

        icon = client.parseDOM(event, 'img', ret='src')[0]
        icon = urljoin(BASEURL, icon)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(name))
        oOutputParameterHandler.addParameter('siteUrl', streams)

        oGui.addMovie(SITE_IDENTIFIER, 'get_stream', name, icon, icon, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()                            




def get_stream():  # 4
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    data = base64.b64decode(unquote(url))
    # xbmc.log('@#@DATAAAA:%s' % data, xbmc.LOGINFO)
    if b'info_outline' in data:
        control.infoDialog("[COLOR gold]No Links available ATM.\n [COLOR lime]Try Again Later![/COLOR]", NAME,
                           iconimage, 5000)
        return
    else:
        links = list(zip(client.parseDOM(str(data), 'a', ret='href'), client.parseDOM(str(data), 'a')))
        # xbmc.log('@#@STREAMMMMMSSSSSS:%s' % links, xbmc.LOGINFO)
        titles = []
        streams = []
        for link, title in links:
            streams.append(link)
            titles.append(title)

        if len(streams) > 1:
            dialog = xbmcgui.Dialog()
            ret = dialog.select('[COLORgold][B]Choose Stream[/B][/COLOR]', titles)
            if ret == -1:
                return
            elif ret > -1:
                host = streams[ret]
                # xbmc.log('@#@STREAMMMMM:%s' % host, xbmc.LOGNOTICE)
                return resolve(host, name)
            else:
                return
        else:
            link = links[0][0]
            return resolve(link, name)


def idle():
    if float(xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')[:4]) > 17.6:
        xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
    else:
        xbmc.executebuiltin('Dialog.Close(busydialog)')


def busy():
    if float(xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')[:4]) > 17.6:
        xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    else:
        xbmc.executebuiltin('ActivateWindow(busydialog)')


def resolve(url, name):
    # xbmc.log('RESOLVE-URL: %s' % url, xbmc.LOGNOTICE)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    # dialog.notification(AddonTitle, '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]', icon, 5000)
    if 'acestream' in url:
        url1 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
        liz = xbmcgui.ListItem(name)
        liz.setArt({'poster': 'poster.png', 'banner': 'banner.png'})
        liz.setArt({'icon': iconimage, 'thumb': iconimage, 'poster': iconimage,
                    'fanart': fanart})
        liz.setPath(url)
        xbmc.Player().play(url1, liz, False)
        quit()
    if '/live.cdnz' in url:
        r = six.ensure_str(client.request(url, referer=BASEURL)).replace('\t', '')
        from resources.modules import jsunpack
        if 'script>eval' in r:
            unpack = re.findall(r'''<script>(eval.+?\{\}\)\))''', r, re.DOTALL)[0]
            r = jsunpack.unpack(unpack.strip())
        else:
            r = r
        if 'hfstream.js' in r:
            regex = '''<script type='text/javascript'> width=(.+?), height=(.+?), channel='(.+?)', g='(.+?)';</script>'''
            wid, heig, chan, ggg = re.findall(regex, r, re.DOTALL)[0]
            stream = 'https://www.playerfs.com/membedplayer/' + chan + '/' + ggg + '/' + wid + '/' + heig + ''
        else:
            if 'cbox.ws/box' in r:
                try:
                    stream = client.parseDOM(r, 'iframe', ret='src', attrs={'id': 'thatframe'})[0]
                except IndexError:
                    streams = client.parseDOM(r, 'iframe', ret='src')
                    stream = [i for i in streams if not 'adca.' in i][0]
            else:
                stream = client.parseDOM(r, 'iframe', ret='src')[-1]
        rr = client.request(stream, referer=url)
        rr = six.ensure_text(rr).replace('\t', '')
        if 'youtube' in rr:
            try:
                flink = client.parseDOM(r, 'iframe', ret='src')[0]
                fid = flink.split('/')[-1]
            except IndexError:
                fid = re.findall(r'''/watch\?v=(.+?)['"]''', r, re.DOTALL)[0]

            flink = 'plugin://plugin.video.youtube/play/?video_id={}'.format(str(fid))

        else:
            if '<script>eval' in rr and not '.m3u8?':
                unpack = re.findall(r'''<script>(eval.+?\{\}\)\))''', rr, re.DOTALL)[0].strip()
                rr = jsunpack.unpack(unpack)
            if 'player.src({src:' in str(rr):
                flink = re.findall(r'''player.src\(\{src:\s*["'](.+?)['"]\,''', rr, re.DOTALL)[0]
            elif 'new Clappr' in rr:
                flink = re.findall(r'''source\s*:\s*["'](.+?)['"]\,''', str(rr), re.DOTALL)[0]
            elif 'player.setSrc' in rr:
                flink = re.findall(r'''player.setSrc\(["'](.+?)['"]\)''', rr, re.DOTALL)[0]
            else:
                try:
                    flink = re.findall(r'''source:\s*["'](.+?)['"]''', rr, re.DOTALL)[0]
                except IndexError:
                    ea = re.findall(r'''ajax\(\{url:\s*['"](.+?)['"],''', rr, re.DOTALL)[0]
                    ea = six.ensure_text(client.request(ea)).split('=')[1]
                    flink = re.findall('''videoplayer.src = "(.+?)";''', ea, re.DOTALL)[0]
                    flink = flink.replace('" + ea + "', ea)
            flink += '|Referer={}'.format(quote(stream))
        stream_url = flink

    else:
        stream_url = url
    liz = xbmcgui.ListItem(name)
    liz.setArt({'poster': 'poster.png', 'banner': 'banner.png'})
    liz.setArt({'icon': iconimage, 'thumb': iconimage, 'poster': iconimage, 'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty("IsPlayable", "true")
    liz.setPath(str(stream_url))
    xbmc.Player().play(stream_url, liz, False)
    quit()


def Open_settings():
    control.openSettings()





