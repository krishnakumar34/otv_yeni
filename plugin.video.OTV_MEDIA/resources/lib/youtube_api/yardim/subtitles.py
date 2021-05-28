# -*- coding: utf-8 -*-
"""

    Copyright (C) 2017-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""

import xbmc, xbmcgui, xbmcaddon, xbmcplugin, xbmcvfs
try:
    xbmc.translatePath = xbmcvfs.translatePath
except AttributeError:
    pass
from resources.lib.comaddon import addon
import weakref
import requests
from resources.lib.youtube_api.yardim import make_dirs
from resources.lib.logger import logger 
from six import PY2
try:
    from six.moves import html_parser

    unescape = html_parser.HTMLParser().unescape
except AttributeError:
    import html

    unescape = html.unescape
def log( text):
        logger.log(text)
def XbmcContextUI(_addon):
    return  _addon

def log_debug( text):
        log(text, logger.DEBUG)
_addon = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')

def get_ui():
       
        _ui = XbmcContextUI(_addon)
        return _ui
def get_home_window_property(property_id):
        property_id = ''.join(['plugin.video.OTV_MEDIA-', property_id])
        return xbmcgui.Window(10000).getProperty(property_id) or None
def clear_home_window_property(property_id):
        property_id = ''.join(['plugin.video.OTV_MEDIA-', property_id])
        xbmcgui.Window(10000).clearProperty(property_id)

log_debug = None
def localize( text_id, default_text=u''):
        result = None
        if isinstance(text_id, int):
            """
            We want to use all localization strings!
            Addons should only use the range 30000 thru 30999 (see: http://kodi.wiki/view/Language_support) but we
            do it anyway. I want some of the localized strings for the views of a skin.
            """
            if text_id >= 0 and (text_id < 30000 or text_id > 30999):
                result = xbmc.getLocalizedString(text_id)
                if result is not None and result:
                    result = utils.to_unicode(result)

        if not result:
            try:
                result = self._addon.getLocalizedString(int(text_id))
                if result is not None and result:
                    result = utils.to_unicode(result)
            except ValueError:
                pass

        if not result:
            result = default_text

        return result

def get_settings():
    
    
    return
class Subtitles(object):
    LANG_NONE = 0
    LANG_PROMPT = 1
    LANG_CURR_FALLBACK = 2
    LANG_CURR = 3
    LANG_CURR_NO_ASR = 4

    BASE_PATH = 'special://temp/plugin.video.OTV_MEDIA/'
    SRT_FILE = ''.join([BASE_PATH, '%s.%s.srt'])

    def __init__(self, context, video_id, captions):
        self.context = context
        self._verify = get_settings()
        self.video_id = video_id
        self.language = 'en-US'
        self.headers = {'Host': 'www.youtube.com',
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                        'Accept': '*/*',
                        'DNT': '1',
                        'Referer': 'https://www.youtube.com/tv',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.8,de;q=0.6'}

        self.caption_track = {}
        self.renderer = captions.get('playerCaptionsTracklistRenderer', {})
        self.caption_tracks = self.renderer.get('captionTracks', [])
        self.translation_langs = self.renderer.get('translationLanguages', [])

        default_audio = self.renderer.get('defaultAudioTrackIndex')
        if default_audio is not None:
            audio_tracks = self.renderer.get('audioTracks', [])
            try:
                audio_track = audio_tracks[default_audio]
            except:
                audio_track = None
            if audio_track:
                default_caption = audio_track.get('defaultCaptionTrackIndex')
                if default_caption is None:
                    default_caption = audio_track.get('captionTrackIndices')
                    if (default_caption is not None) and (isinstance(default_caption, list)):
                        default_caption = default_caption[0]
                if default_caption is not None:
                    try:
                        self.caption_track = self.caption_tracks[default_caption]
                    except:
                        pass

        ui = get_ui()
        self.prompt_override = get_home_window_property('prompt_for_subtitles') == video_id
        clear_home_window_property('prompt_for_subtitles')

    def srt_filename(self, sub_language):
        return self.SRT_FILE % (self.video_id, sub_language)

    def _write_file(self, _file, contents):
        if not make_dirs(self.BASE_PATH):
            log_debug('Failed to create directories: %s' % self.BASE_PATH)
            return False
        log_debug('Writing subtitle file: %s' % _file)
        try:
            f = xbmcvfs.File(_file, 'w')
            f.write(contents)
            f.close()
            return True
        except:
            log_debug('File write failed for: %s' % _file)
            return False

    def _unescape(self, text):
        try:
            text = text.decode('utf8', 'ignore')
        except:
            log_debug('Subtitle unescape: failed to decode utf-8')
        try:
            text = unescape(text)
        except:
            log_debug('Subtitle unescape: failed to unescape text')
        return text



    def _get_all(self):
        list_of_subs = []
        for language in self.translation_langs:
            list_of_subs.extend(self._get(language=language.get('languageCode')))
        return list(set(list_of_subs))

    def _prompt(self):
        tracks = [(track.get('languageCode'), self._get_language_name(track)) for track in self.caption_tracks]
        translations = [(track.get('languageCode'), self._get_language_name(track)) for track in self.translation_langs]
        languages = tracks + translations
        if languages:
            choice = get_ui().on_select(localize(30560), [language_name for language, language_name in languages])
            if choice != -1:
                return self._get(language=languages[choice][0], language_name=languages[choice][1])
            else:
                log_debug('Subtitle selection cancelled')
                return []
        else:
            log_debug('No subtitles found for prompt')
            return []

    def _get(self, language='en', language_name=None, no_asr=False):
        fname = self.srt_filename(language)
        if xbmcvfs.exists(fname):
            log_debug('Subtitle exists for: %s, filename: %s' % (language, fname))
            return [fname]

        caption_track = None
        asr_track = None
        has_translation = False
        for track in self.caption_tracks:
            if language == track.get('languageCode'):
                if language_name is not None:
                    if language_name == self._get_language_name(track):
                        caption_track = track
                        break
                else:
                    if no_asr and (track.get('kind') == 'asr'):
                        continue
                    elif track.get('kind') == 'asr':
                        asr_track = track
                    else:
                        caption_track = track

        if (caption_track is None) and (asr_track is not None):
            caption_track = asr_track

        for lang in self.translation_langs:
            if language == lang.get('languageCode'):
                has_translation = True
                break

        if (self.caption_track.get('languageCode') != language) and (not has_translation) and (caption_track is None):
            log_debug('No subtitles found for: %s' % language)
            return []

        subtitle_url = None
        if (caption_track is None) and has_translation:
            base_url = self.caption_track.get('baseUrl')
            if base_url:
                subtitle_url = ''.join([base_url, '&fmt=vtt&type=track&tlang=', language])
        elif caption_track is not None:
            base_url = caption_track.get('baseUrl')
            if base_url:
                subtitle_url = ''.join([base_url, '&fmt=vtt&type=track'])

        if subtitle_url:
            log_debug('Subtitle url: %s' % subtitle_url)
            if not get_settings().subtitle_download():
                return [subtitle_url]
            else:
                result_auto = requests.get(subtitle_url, headers=self.headers,
                                           allow_redirects=True)

                if result_auto.text:
                    log_debug('Subtitle found for: %s' % language)
                    self._write_file(fname, bytearray(self._unescape(result_auto.text), encoding='utf8', errors='ignore'))
                    return [fname]
                else:
                    log_debug('Failed to retrieve subtitles for: %s' % language)
                    return []
        else:
            log_debug('No subtitles found for: %s' % language)
            return []

    def _get_language_name(self, track):
        key = 'languageName' if 'languageName' in track else 'name'
        lang_name = track.get(key, {}).get('simpleText')
        if not lang_name:
            track_name = track.get(key, {}).get('runs', [{}])
            if isinstance(track_name, list) and len(track_name) >= 1:
                lang_name = track_name[0].get('text')

        if lang_name:
            return self._decode_language_name(lang_name)

        return None

    @staticmethod
    def _decode_language_name(language_name):
        language_name = language_name.encode('raw_unicode_escape')

        if PY2:
            language_name = language_name.decode('utf-8')

        else:
            language_name = language_name.decode('raw_unicode_escape')

        return language_name
