#-*- coding: utf-8 -*-
from resources.lib.comaddon import xbmc, isMatrix
try:
    import htmlentitydefs
    import urllib
    import urllib2

except ImportError:
    import html.entities as htmlentitydefs
    import urllib.parse as urllib
    import urllib.request as urllib2

import unicodedata
import re
# function util n'utilise pas xbmc, xbmcgui, xbmcaddon ect...

class cUtil:
    # reste a transformer la class en fonction distante.

    def CheckOrd(self, label):
        count = 0
        try:
            label = label.lower()
            label = label.strip()
            label = unicode(label, 'utf-8')
            label = unicodedata.normalize('NFKD', label).encode('ASCII', 'ignore')
            for i in label:
                count += ord(i)
        except:
            pass

        return count

    def CheckOccurence(self, str1, str2):
        ignoreListe = ['3d', 'la', 'le', 'les', 'un', 'une', 'de', 'des', 'du', 'en', 'a', 'au', 'aux', 'is', 'the', 'in', 'of', 'and', 'mais', 'ou', 'no', 'dr', 'contre', 'dans', 'qui',
                       'et', 'donc', 'or', 'ni', 'ne', 'pas', 'car', 'je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
                       'my', 'your', 'his', 'its', 'our']

        str1 = str1.replace('+', ' ').replace('%20', ' ').replace(':', ' ').replace('-', ' ')
        str2 = str2.replace(':', ' ').replace('-', ' ')
        
        #Inutile avec Python 3.
        if not isMatrix():
            str1 = self.CleanName(str1.replace('.', ' '))
            str2 = self.CleanName(str2.replace('.', ' '))

        i = 0
        list2 = str2.split(' ')     # Comparaison mot à mot
        for part in str1.split(' '):
            if part in ignoreListe: # Mots à ignorer
                continue
            if len(part) == 1:      # Ignorer une seule lettre
                continue
            if part in list2:
                i += 1              # Nombre de mots correspondants
        return i

    def removeHtmlTags(self, sValue, sReplace=''):
        p = re.compile(r'<.*?>')
        return p.sub(sReplace, sValue)

    def formatTime(self, iSeconds):
        iSeconds = int(iSeconds)

        iMinutes = int(iSeconds / 60)
        iSeconds = iSeconds - (iMinutes * 60)
        if (iSeconds < 10):
            iSeconds = '0' + str(iSeconds)

        if (iMinutes < 10):
            iMinutes = '0' + str(iMinutes)

        return str(iMinutes) + ':' + str(iSeconds)

    def DecoTitle2(self, string):

        # on vire ancienne deco en cas de bug
        string = re.sub('\[\/*COLOR.*?\]', '', str(string))

        # pr les tag Crochet
        string = re.sub('([\[].+?[\]])',' [COLOR coral]\\1[/COLOR] ', string)
        # pr les tag parentheses
        string = re.sub('([\(](?![0-9]{4}).{1,7}[\)])', ' [COLOR coral]\\1[/COLOR] ', string)
        # pr les series
        string = self.FormatSerie(string)
        string = re.sub('(?i)(.*) ((?:[S|E][0-9\.\-\_]+){1,2})', '\\1 [COLOR coral]\\2[/COLOR] ', string)

        # vire doubles espaces
        string = re.sub(' +', ' ', string)

        return string

    def unescape(self, text):
        def fixup(m):
            text = m.group(0)
            if text[:2] == '&#':
                # character reference
                try:
                    if text[:3] == '&#x':
                        return unichr(int(text[3:-1], 16))
                    else:
                        return unichr(int(text[2:-1]))
                except ValueError:
                    pass
                except NameError:
                    if text[:3] == '&#x':
                        return chr(int(text[3:-1], 16))
                    else:
                        return chr(int(text[2:-1]))
            else:
                # named entity
                try:
                    text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
                except KeyError:
                    pass
                except NameError:
                    text = chr(htmlentitydefs.name2codepoint[text[1:-1]])

            return text  # leave as is
        return re.sub('&#?\w+;', fixup, text)

    def CleanName(self, name):
        if not isMatrix:
            # vire accent et '\'
            try:
                name = unicode(name, 'utf-8')  # converti en unicode pour aider aux convertions
            except:
                pass

            try:
                name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('unicode_escape')
                name = name.encode('utf-8') #on repasse en utf-8
            except TypeError:
                #name = unicodedata.normalize('NFKD', name.decode("utf-8")).encode('ASCII', 'ignore')
                pass

        #on cherche l'annee
        annee = ''
        m = re.search('(\([0-9]{4}\))', name)
        if m:
            annee = str(m.group(0))
            name = name.replace(annee, '')

        # vire tag
        name = re.sub('[\(\[].+?[\)\]]', '', name)
        # les apostrophes remplacer par des espaces
        name = name.replace("'", " ")
        # vire caractere special
        # name = re.sub('[^a-zA-Z0-9 ]', '', name)
        name = re.sub('[^a-zA-Z0-9 : -]', '', name)
        # tout en minuscule
        name = name.lower()
        # vire espace debut et fin
        name = name.strip()
        # vire espace double au milieu
        name = re.sub(' +', ' ', name)

        # on remet l'annee
        if annee:
            name = name + ' ' + annee

        return name

    def FormatSerie(self, string):

        # vire doubles espaces
        string = re.sub(' +', ' ', string)

        # vire espace a la fin
        if string.endswith(' '):
            string = string[:-1]

        # vire espace au debut
        if string.startswith(' '):
            string = string[1:]

        SXEX = ''
        m = re.search('(?i)(\wpisode ([0-9\.\-\_]+))', string, re.UNICODE)
        if m:
            # ok y a des episodes
            string = string.replace(m.group(1), '')
            # SXEX + '%02d' % int(m.group(2))
            SXEX = m.group(2)
            if len(SXEX) < 2:
                SXEX = '0' + SXEX
            SXEX = 'E' + SXEX

            # pr les saisons
            m = re.search('(?i)(s(?:aison )*([0-9]+))', string)
            if m:
                string = string.replace(m.group(1), '')
                SXEX = 'S' + '%02d' % int(m.group(2)) + SXEX
            string = string + ' ' + SXEX

        else:
            # pas d'episode mais y a t il des saisons ?
            m = re.search('(?i)(s(?:aison )*([0-9]+))(?:$| )', string)
            if m:
                string = string.replace(m.group(1), '')
                SXEX = 'S' + '%02d' % int(m.group(2))

                string = string + ' ' + SXEX

        # reconvertion utf-8
        return string.encode('utf-8')

    def EvalJSString(self, s):
        s = s.replace(' ', '')
        try:
            s = s.replace('!+[]', '1').replace('!![]', '1').replace('[]', '0')
            s = re.sub(r'(\([^()]+)\+\[\]\)', '(\\1)*10)', s)  # si le bloc fini par +[] >> *10
            s = re.sub(r'\[([^\]]+)\]', 'str(\\1)', s)
            if s[0] == '+':
                s = s[1:]
            val = int(eval(s))
            return val
        except:
            return 0


"""
# ***********************
# Fonctions lights
# ***********************
# Pour les avoirs
# from resources.lib import util
# puis util.VSlog('test')
"""
def nquote():

        jsfuck =  jsfuck.replace('(%(3)a)', ':')
        jsfuck =  jsfuck.replace('(%(3)b)', ';')                               
        jsfuck =  jsfuck.replace('(%(3)c)', '<')
        jsfuck =  jsfuck.replace('(%(3)d)', '=')
        jsfuck =  jsfuck.replace('(%(3)e)', '>')
        jsfuck =  jsfuck.replace('(%(3)f)', '?')
        jsfuck =  jsfuck.replace('(%(4)0)', '@')
        jsfuck =  jsfuck.replace('(%(4)1)', 'A')
        jsfuck =  jsfuck.replace('(%(4)2)', 'B')
        jsfuck =  jsfuck.replace('(%(4)3)', 'C')                          
        jsfuck =  jsfuck.replace('(%(4)4)', 'D')
        jsfuck =  jsfuck.replace('(%(4)5)', 'E')
        jsfuck =  jsfuck.replace('(%(4)6)', 'F')
        jsfuck =  jsfuck.replace('(%(4)7)', 'G')                          
        jsfuck =  jsfuck.replace('(%(4)8)', 'H')
        jsfuck =  jsfuck.replace('(%(4)9)', 'I')
        jsfuck =  jsfuck.replace('(%(4)a)', 'J')
        jsfuck =  jsfuck.replace('(%(4)b)', 'K')
        jsfuck =  jsfuck.replace('(%(4)c)', 'L')                          
        jsfuck =  jsfuck.replace('(%(4)d)', 'M')
        jsfuck =  jsfuck.replace('(%(4)e)', 'N')
        jsfuck =  jsfuck.replace('(%(4)f)', 'O')
        jsfuck =  jsfuck.replace('(%(5)0)', 'P')        
        jsfuck =  jsfuck.replace('(%(5)1)', 'Q')
        jsfuck =  jsfuck.replace('(%(5)2)', 'R')
        jsfuck =  jsfuck.replace('(%(5)3)', 'S')
        jsfuck =  jsfuck.replace('(%(5)4)', 'T')
        jsfuck =  jsfuck.replace('(%(5)5)', 'U')
        jsfuck =  jsfuck.replace('(%(5)6)', 'V')
        jsfuck =  jsfuck.replace('(%(5)7)', 'W')
        jsfuck =  jsfuck.replace('(%(5)8)', 'X')
        jsfuck =  jsfuck.replace('(%(5)9)', 'Y')
        jsfuck =  jsfuck.replace('(%(5)a)', 'Z')
        jsfuck =  jsfuck.replace('(%(5)b)', '[')
        jsfuck =  jsfuck.replace('(%(5)c)', '\\')
        jsfuck =  jsfuck.replace('(%(5)d)', ']')
        jsfuck =  jsfuck.replace('(%(5)e)', '^')                      
        jsfuck =  jsfuck.replace('(%(5)f)', '_')
        jsfuck =  jsfuck.replace('(%(6)0)', '`')
        jsfuck =  jsfuck.replace('(%(2188)[])', ':')
        jsfuck =  jsfuck.replace('(%(2189)[])', ';')
        jsfuck =  jsfuck.replace('(%(2190)[])', '<')
        jsfuck =  jsfuck.replace('(%(2191)[])', '=')
        jsfuck =  jsfuck.replace('(%(2192)[])', '>')
        jsfuck =  jsfuck.replace('(%(2193)[])', '?')
        jsfuck =  jsfuck.replace('(%(2194)[])', '@')
        jsfuck =  jsfuck.replace('(%(2195)[])', 'A')
        jsfuck =  jsfuck.replace('(%(2196)[])', 'B')
        jsfuck =  jsfuck.replace('(%(2197)[])', 'C')                          
        jsfuck =  jsfuck.replace('(%(2198)[])', 'D')
        jsfuck =  jsfuck.replace('(%(2199)[])', 'E')
        jsfuck =  jsfuck.replace('(%(2200)[])', 'F')
        jsfuck =  jsfuck.replace('(%(2201)[])', 'T')                          
        jsfuck =  jsfuck.replace('(%(2202)[])', 'H')
        jsfuck =  jsfuck.replace('(%(2203)[])', 'I')
        jsfuck =  jsfuck.replace('(%(2204)[])', 'J')
        jsfuck =  jsfuck.replace('(%(2205)[])', 'K')
        jsfuck =  jsfuck.replace('(%(2206)[])', 'L')                          
        jsfuck =  jsfuck.replace('(%(2207)[])', 'G')
        jsfuck =  jsfuck.replace('(%(2208)[])', 'N')
        jsfuck =  jsfuck.replace('(%(2209)[])', 'O')
        jsfuck =  jsfuck.replace('(%(2210)[])', 'P')        
        jsfuck =  jsfuck.replace('(%(2211)[])', 'Q')
        jsfuck =  jsfuck.replace('(%(2212)[])', 'B')
        jsfuck =  jsfuck.replace('(%(2213)[])', 'S')
        jsfuck =  jsfuck.replace('(%(2214)[])', 'M')
        jsfuck =  jsfuck.replace('(%(2215)[])', 'U')
        jsfuck =  jsfuck.replace('(%(2216)[])', 'V')
        jsfuck =  jsfuck.replace('(%(2217)[])', 'W')
        jsfuck =  jsfuck.replace('(%(2218)[])', 'X')
        jsfuck =  jsfuck.replace('(%(2219)[])', 'Y')
        jsfuck =  jsfuck.replace('(%(2220)[])', 'Z')
        jsfuck =  jsfuck.replace('(%(2221)[])', '[')
        jsfuck =  jsfuck.replace('(%(2222)[])', '\\')
        jsfuck =  jsfuck.replace('(%(2223)[])', ']')
        jsfuck =  jsfuck.replace('(%(2224)[])', '^')
        jsfuck =  jsfuck.replace('(%(2225)[])', '_')
        jsfuck =  jsfuck.replace('(%(2226)[])', '`')
        jsfuck =  jsfuck.replace('(%(228)[])', 'H')

def Unquote(sUrl):
    return urllib.unquote(sUrl)


def Quote(sUrl):
    return urllib.quote(sUrl)


def UnquotePlus(sUrl):
    return urllib.unquote_plus(sUrl)


def QuotePlus(sUrl):
    return urllib.quote_plus(sUrl)


def QuoteSafe(sUrl):
    return urllib.quote(sUrl, safe=':/')


def urlEncode(sUrl):
    return urllib.urlencode(sUrl)


def Noredirection():
    class NoRedirection(urllib2.HTTPErrorProcessor):
        def http_response(self, request, response):
            return response

        https_response = http_response

    opener = urllib2.build_opener(NoRedirection)
    return opener

# deprecier utiliser comaddon dialog()
# def updateDialogSearch(dialog, total, site):
#     global COUNT
#     COUNT += 1
#     iPercent = int(float(COUNT * 100) / total)
#     dialog.update(iPercent, 'Chargement: ' + str(site))


# def VStranslatePath(location):
#     # ex util.VStranslatePath('special://logpath/') > http://kodi.wiki/view/Special_protocol
#     # d'apres Kodi ne doit pas etre utiliser sur les special://
#     return xbmc.translatePath(location).decode('utf-8')


def GetGooglUrl(url):
    if 'http://goo.gl' in url:
        try:
            headers = {'User-Agent': 'Mozilla 5.10', 'Host': 'goo.gl', 'Connection': 'keep-alive'}
            request = urllib2.Request(url, None, headers)
            reponse = urllib2.urlopen(request)
            url = reponse.geturl()
        except:
            pass
    return url
