#-*- coding: utf-8 -*-
# Name:        otv-jsfuckdecoder
# Purpose:
# Version:     1.0
# Author:      orhan
#
# Created:     28.04.2021
# Copyright:   (c) orhan 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from resources.lib.logger import logger 
import re  ,sys
import hashlib
import binascii

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    # noinspection PyShadowingBuiltins
    unichr = chr
    # noinspection PyShadowingBuiltins
    unicode = str
    # noinspection PyShadowingBuiltins
    basestring = str
else:
    # noinspection PyUnresolvedReferences
    import __builtin__
    # noinspection PyShadowingBuiltins
    unichr = __builtin__.unichr
    # noinspection PyShadowingBuiltins
    unicode = __builtin__.unicode
    # noinspection PyShadowingBuiltins
    basestring = __builtin__.basestring


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
    

def to_utf8(dct):
    if isinstance(dct, dict):
        return dict((to_utf8(key), to_utf8(value)) for key, value in dct.items())
    elif isinstance(dct, list):
        return [to_utf8(element) for element in dct]
    elif isinstance(dct, unicode):
        dct = dct.encode("utf8")
        if PY3: dct = dct.decode("utf8")
        return dct
    elif PY3 and isinstance(dct, bytes):
        try:
            return dct.decode('utf-8')
        except:
            return dct.decode('ISO-8859-1')
    else:
        return dct

try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range

class OTVJSfuck(object):
    NUMMERS = None
    USE_CHAR_CODE = "USE_CHAR_CODE"

    MIN, MAX = 32, 126

    SIMPLE = {
        'false':      '![]',
        'true':       '!![]',
        'undefined':  '[][[]]',
        'NaN':        '+[![]]',
        'Infinity':   ('+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+'
                       '!+[]]+[+[]]+[+[]]+[+[]])')  # +"1e1000"
    }

    CONSTRUCTORS = {
      
        'Number':   '(+[])',
        'String':   '([]+[])',
        'Boolean':  '(![])',
        'Function': '[]["fill"]',
        'RegExp':   'Function("return/"+false+"/")()'
       
    }

    
    MAPPING = {
        'a':   '(!false+"")[1]',
        'b':   '([]["entries"]()+"")[2]',
        'c':   '([]["fill"]+"")[3]',
        'd':   '(undefined+"")[2]',
        'e':   '(true+"")[3]',
        'f':   '(!false+[][(false+"")[0]',
        'g':   '(false+[0]+String)[20]',                                  
        'h':   '(+(101))["to"+String["name"]](21)[1]',
        'i':   '([false]+undefined)[10]',
        'j':   '([]["entries"]()+"")[3]',
        'k':   '(+(20))["to"+String["name"]](21)',
        'l':   '(false+"")[2]])',
        'm':   '(Number+"")[11]',
        'n':   '(undefined+"")[1]',
        'o':   '(true+[]["fill"])[10]',
        'p':   '(+(211))["to"+String["name"]](31)[1]',
        'q':   '(+(212))["to"+String["name"]](31)[1]',
        'r':   '(true+"")[1]',
        's':   '(false+"")[3]',
        't':   '(true+"")[0]',
        'u':   '(undefined+"")[0]',
        'v':   '(+(31))["to"+String["name"]](32)',
        'w':   '(+(32))["to"+String["name"]](33)',
        'x':   '(+(101))["to"+String["name"]](34)[1]',
        'y':   '(NaN+[Infinity])[10]',
        'z':   '(+(35))["to"+String["name"]](36)',

        'A':   '(+[]+Array)[10]',
        'B':   '(+[]+Boolean)[10]',
        'C':   'Function("return escape")()(("")["italics"]())[2]',
        'D':   'Function("return escape")()([]["fill"])["slice"]("-1")',
        'E':   '(RegExp+"")[12]',
        'F':   '(+[]+Function)[10]',
        'G':   '(false+Function("return Date")()())[30]',
        'H':   USE_CHAR_CODE,
        'I':   '(Infinity+"")[0]',
        'J':   USE_CHAR_CODE,
        'K':   USE_CHAR_CODE,
        'L':   USE_CHAR_CODE,
        'M':   '(true+Function("return Date")()())[30]',
        'N':   '(NaN+"")[0]',
        'O':   '(NaN+Function("return{}")())[11]',
        'P':   USE_CHAR_CODE,
        'Q':   USE_CHAR_CODE,
        'R':   '(+[]+RegExp)[10]',
        'S':   '(+[]+String)[10]',
        'T':   '(NaN+Function("return Date")()())[30]',
        'U':   ('(NaN+Function("return{}")()["to"+String'
                '["name"]]["call"]())[11]'),
        'V':   USE_CHAR_CODE,
        'W':   USE_CHAR_CODE,
        'X':   USE_CHAR_CODE,
        'Y':   USE_CHAR_CODE,
        'Z':   USE_CHAR_CODE,
        ' ':   '(NaN+[]["fill"])[11]',
        '!':   USE_CHAR_CODE,
        '"':   '("")["fontcolor"]()[12]',
        '#':   USE_CHAR_CODE,
        '$':   USE_CHAR_CODE,
        '%':   'Function("return escape")()([]["fill"])[21]',
        '&':   '("")["link"](0+")[10]',
        '\'':  USE_CHAR_CODE,
        '(':   '(undefined+[]["fill"])[22]',
        ')':   '([0]+false+[]["fill"])[20]',
        '*':   USE_CHAR_CODE,
        '+':   ('(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]'
                '+[+!+[]]+[+[]]+[+[]])+[])[2]'),
        ',':   '([]["slice"]["call"](false+"")+"")[1]',
        '-':   '(+(.+[0000000001])+"")[2]',
        '.':   ('(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+'
                '[]+!+[]]+[+[]])+[])[+!+[]]'),
        '/':   '(false+[0])["italics"]()[10]',
        ':':   '(RegExp()+"")[3]',
        ';':   '("")["link"](")[14]',
        '<':   '("")["italics"]()[0]',
        '=':   '("")["fontcolor"]()[11]',
        '>':   '("")["italics"]()[2]',
        '?':   '(RegExp()+"")[2]',
        '@':   USE_CHAR_CODE,
        '[':   '([]["entries"]()+"")[0]',
        '\\':  USE_CHAR_CODE,
        ']':   '([]["entries"]()+"")[22]',
        '^':   USE_CHAR_CODE,
        '_':   USE_CHAR_CODE,
        '`':   USE_CHAR_CODE,
        '{':   '(true+[]["fill"])[20]',
        '|':   USE_CHAR_CODE,
        '}':   '([]["fill"]+"")["slice"]("-1")',
        '~':   USE_CHAR_CODE
        }

    
    GLOBAL = 'Function("return this")()'
    def __init__(self, js):
        self.js = js
        self.fillMissingDigits()
        self.fillMissingChars()
        self.replaceMap()

    def fuckend(self,js):                
              js =  js.replace('t101','A')  
              js =  js.replace('t102','B') 
              js =  js.replace('t103','C') 
              js =  js.replace('t104','D') 
              js =  js.replace('t105','E') 
              js =  js.replace('t106','F') 
              js =  js.replace('t107','G') 
              js =  js.replace('t110','H')  
              js =  js.replace('t111','I')  
              js =  js.replace('t112','J')  
              js =  js.replace('t113','K')  
              js =  js.replace('t114','L')  
              js =  js.replace('t115','M')  
              js =  js.replace('t117','O') 
              js =  js.replace('t120','P') 
              js =  js.replace('t121','Q') 
              js =  js.replace('t122','R') 
              js =  js.replace('t123','S')  
              js =  js.replace('t124','T')  
              js =  js.replace('t125','U')  
              js =  js.replace('t334','Ü')
              js =  js.replace('t126','V')  
              js =  js.replace('t127','W')  
              js =  js.replace('t130','X')  
              js =  js.replace('t131','Y')  
              js =  js.replace('t132','Z') 
              js =  js.replace('t142','b') 
              js =  js.replace('t143','c')                              
              js =  js.replace('t147','g')
              js =  js.replace('t150','h')    
              js =  js.replace('t152','j')  
              js =  js.replace('t153','k')   
              js =  js.replace('t155','m') 
              js =  js.replace('t157','o') 
              js =  js.replace('t160','p') 
              js =  js.replace('t161','q') 
              js =  js.replace('164a','r') 
              js =  js.replace('t164','t') 
              js =  js.replace('t166','v') 
              js =  js.replace('t167','w')               
              js =  js.replace('t170','x')  
              js =  js.replace('t171','z')          
              js =  js.replace('t72',':')
              js =  js.replace('t73',';')
              js =  js.replace('t133','[')
              js =  js.replace('t135',']')
              js =  js.replace('t173','{')
              js =  js.replace('t136','^')
              js =  js.replace('t175','}')
              js =  js.replace('t54',',')
              js =  js.replace('t74','<')
              js =  js.replace('t76','>')
              js =  js.replace('t140','`')
              js =  js.replace('t77','?')
              js =  js.replace('t75','=')
              js =  js.replace('t50','(')
              js =  js.replace('t40',' ')
              js =  js.replace('t51',')')
              js =  js.replace('t57','/')
              js =  js.replace('t134','\\') 
              js =  js.replace('t46','&')  
              js =  js.replace('t45','%')  
              js =  js.replace('t44','$')  
              js =  js.replace('t247','�') 
              js =  js.replace('t100','@')  
              js =  js.replace('t42','"')  
              js =  js.replace('t41','!')  
              js =  js.replace('t260','�') 
              js =  js.replace('t47',"'")   
              js =  js.replace('t52','*')    
              js =  js.replace('t53','+')   
              js =  js.replace('t264','�') 
              js =  js.replace('t337','�') 
              js =  js.replace('t137','_')  
              js =  js.replace('t176','~')   
              js =  js.replace('t52','*')   
              js =  js.replace('t55','-')      
              return js                                                                       
    def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
        '''
        Encodes vanilla Javascript to JSFuck obfuscated Javascript

        Keyword arguments:
        js                            -- string of unobfuscated Javascript

        wrapWithEval        -- boolean determines whether to wrap with an eval

        runInParentScope -- boolean determines whether to run in parents scope

        '''
        output = []

        if not js:
            js = self.js

            if not js:
                return ''

        regex = ''

        for i in self.SIMPLE:
            regex += i + '|'

        regex += '.'

        def inputReplacer(c):
            c = c.group()
            replacement = self.SIMPLE[c] if c in self.SIMPLE else False

            if replacement:
                output.append('[' + replacement + ']+[]')

            else:
                replacement = self.MAPPING[c] if c in self.MAPPING else False

                if replacement:
                    output.append(replacement)
                else:
                    replacement = (
                        '([]+[])[' + self.encode('constructor') + ']'
                        '[' + self.encode('fromCharCode') + ']'
                        '(' + self.encode(str(ord(c[0]))) + ')')

                    output.append(replacement)
                    self.MAPPING[c] = replacement

        re.sub(regex, inputReplacer, js)

        output = '+'.join(output)

        if re.search(r'^\d$', js):
            output += "+[]"

        if wrapWithEval:
            if runInParentScope:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + self.encode('return eval') + ')()'
                          '(' + output + ')')

            else:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + output + ')')

        self.js = output

        return output

    def uneval(self, js):
        '''
        Unevals a piece of Javascript wrapped with an encoded eval

        Keyword arguments:
        js -- string containing an eval wrapped string of Javascript

        Returns:
        js -- string with eval removed

        '''
        js = js.replace('[][fill][constructor](', '')
        js = js[:-2]

        ev = 'return eval)()('

        if ev in js:
            js = js[(js.find(ev) + len(ev)):]

        return js

    def mapping(self, js):
        '''
        Iterates over MAPPING and replaces every value found with
        its corresponding key

        Keyword arguments:
        js -- string containing Javascript encoded with JSFuck

        Returns:
        js -- string of decoded Javascript

        '''
        for key, value in sorted(
                list(self.MAPPING.items()), key=lambda x: len(x[1]), reverse=True):
            js = js.replace(value, key)

        return js

    def fillMissingDigits(self):
        '''
        Calculates 0-9's encoded value and adds it to MAPPING

        '''
        for number in range(10):
            output = '+[]'

            if number > 0:
                output = '+!' + output

            for i in range(number - 1):
                output = '+!+[]' + output

            if number > 1:
                output = output[1:]

            self.MAPPING[str(number)] = '[' + output + ']'

    def fillMissingChars(self):
        '''
        Iterates over MAPPING and fills missing character values with a string
        containing their ascii value represented in hex

        '''
        for key in self.MAPPING:
            if self.MAPPING[key] == self.USE_CHAR_CODE:
                hexidec = hex(ord(key[0]))[2:]

                digit_search = re.findall(r'\d+', hexidec)
                letter_search = re.findall(r'[^\d+]', hexidec)

                digit = digit_search[0] if digit_search else ''
                letter = letter_search[0] if letter_search else ''

                string = ('Function("return unescape")()("%%"+(%s)+"%s")'
                          % (digit, letter))

                self.MAPPING[key] = string

    def replaceMap(self):
        '''
        Iterates over MAPPING from MIN to MAX and replaces value with values
        found in CONSTRUCTORS and SIMPLE, as well as using digitalReplacer and
        numberReplacer to replace numeric values

        '''
        def replace(pattern, replacement):
            return re.sub(pattern, replacement, value, flags=re.I)

        def digitReplacer(x):
            return self.MAPPING[x.group(1)]

        def numberReplacer(y):
            values = list(y.group(1))
            head = int(values[0])
            output = '+[]'

            values.pop(0)

            if head > 0:
                output = '+!' + output

            for i in range(1, head):
                output = '+!+[]' + output

            if head > 1:
                output = output[1:]

            return re.sub(r'(\d)', digitReplacer, '+'.join([output] + values))

        for i in range(self.MIN, self.MAX + 1):
            character = chr(i)
            value = self.MAPPING[character]

            original = ''

            if not value:
                continue

            while value != original:
                original = value

                for key, val in self.CONSTRUCTORS.items():
                    value = replace(r'\b' + key, val + '["constructor"]')

                for key, val in self.SIMPLE.items():
                    value = replace(key, val)

            value = replace(r'(\d\d+)', numberReplacer)
            value = replace(r'\((\d)\)', digitReplacer)
            value = replace(r'\[(\d)\]', digitReplacer)

            value = replace(r'GLOBAL', self.GLOBAL)
            value = replace(r'\+""', '+[]')
            value = replace(r'""', '[]+[]')

            self.MAPPING[character] = value



    def decode2(self, replace_plus=True):
        while True:
            start_js = self.js
            self.repl_words()
            self.repl_numbers()
            if start_js == self.js:
                break
    
        if replace_plus:
            self.js = self.js.replace('+', '')
        return self.js    
    def repl_words(self):
        while True:
            start_js = self.js
            for key in sorted(self.MAPPING, key=lambda k: len(self.MAPPING[k]), reverse=True):
                if self.MAPPING.get(key) in  self.js:
                   self.js = self.js.replace(self.MAPPING.get(key), '{}'.format(key))
            for key in sorted(self.SIMPLE, key=lambda k: len(self.SIMPLE[k]), reverse=True):
                if self.SIMPLE.get(key) in  self.js:
                   self.js = self.js.replace(self.SIMPLE.get(key), '{}'.format(key))
            for key in sorted(self.CONSTRUCTORS, key=lambda k: len(self.CONSTRUCTORS[k]), reverse=True):
                if self.CONSTRUCTORS.get(key) in  self.js:
                   self.js = self.js.replace(self.CONSTRUCTORS.get(key), '{}'.format(key))
            if self.js == start_js:
                break
    
        
    def repl_numbers(self):
        if self.NUMMERS is None:
            self.NUMMERS = self.get_NUMMERS()
            
        while True:
            start_js = self.js
            for key, value in sorted(self.NUMMERS.items(), key=lambda x: len(x[0]), reverse=True):
                self.js = self.js.replace(key, value)
    
            if self.js == start_js:
                break
        
    def get_NUMMERS(self):
        n = {'!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]': '9',
             '!+[]+!![]+!![]+!![]+!![]': '5', '!+[]+!![]+!![]+!![]': '4',
             '!+[]+!![]+!![]+!![]+!![]+!![]': '6', '!+[]+!![]': '2',
             '!+[]+!![]+!![]': '3', '(+![]+([]+[]))': '0', '(+[]+[])': '0', 
             '(+!![]+[])': '1', '!+[]+!![]+!![]+!![]+!![]+!![]+!![]': '7',
             '!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]': '8', '+!![]': '1',
             '[+[]]': '[0]', '!+[]+!+[]': '2', '[+!+[]]': '[1]', '(+20)': '20',
             '[+!![]]': '[1]', '[+!+[]+[+[]]]': '[10]', '+(1+1)': '11'}
        
        for i in xrange(2, 20):
            key = '+!![]' * (i - 1)
            key = '!+[]' + key
            n['(' + key + ')'] = str(i)
            key += '+[]'
            n['(' + key + ')'] = str(i)
            n['[' + key + ']'] = '[' + str(i) + ']'
     
        for i in xrange(2, 10):
            key = '!+[]+' * (i - 1) + '!+[]'
            n['(' + key + ')'] = str(i)
            n['[' + key + ']'] = '[' + str(i) + ']'
             
            key = '!+[]' + '+!![]' * (i - 1)
            n['[' + key + ']'] = '[' + str(i) + ']'
                
        for i in xrange(0, 10):
            key = '(+(+!+[]+[%d]))' % (i)
            n[key] = str(i + 10)
            key = '[+!+[]+[%s]]' % (i)
            n[key] = '[' + str(i + 10) + ']'
            
        for tens in xrange(2, 10):
            for ones in xrange(0, 10):
                key = '!+[]+' * (tens) + '[%d]' % (ones)
                n['(' + key + ')'] = str(tens * 10 + ones)
                n['[' + key + ']'] = '[' + str(tens * 10 + ones) + ']'
        
        for hundreds in xrange(1, 10):
            for tens in xrange(0, 10):
                for ones in xrange(0, 10):
                    key = '+!+[]' * hundreds + '+[%d]+[%d]))' % (tens, ones)
                    if hundreds > 1: key = key[1:]
                    key = '(+(' + key
                    n[key] = str(hundreds * 100 + tens * 10 + ones)
        return n
    def decode(self, replace_plus=True):
        js=self.js 
        jsfuck =self.decode2(js)
        jsfuck  =self.jsfuckjsfuck(jsfuck)
        return jsfuck 

           
               

    def jsfuckjsfuck(self,jsfuck):                      
        jsfuck=  jsfuck.replace('![]', '1').replace('(false[])1', 'a')
        jsfuck = jsfuck.replace('(false[])2', 'l').replace('[([][(false[])0', 'f').replace('(false[])0', 'f').replace('flat])[10]', 'o')             
        jsfuck =  jsfuck.replace('(false[])3', 's')
        jsfuck =  jsfuck.replace('([][flat]flat][])3', 'c').replace('([][flat][])3', 'c').replace('flat][])3', 'c')                                                                                                 
        jsfuck =  jsfuck.replace('constauctoa](aetuanString[fontcoloa]()[12](', '')
        jsfuck =  jsfuck.replace(')[s((211))[toStringconstauctoa]', '')
        jsfuck =  jsfuck.replace('[na(Numberconstauctoa][])[11]e]](211)1lit](t)[join]', '')
        jsfuck =  jsfuck.replace('(constauctoa](aetuan(false0)[italics]()[10]false(false0)[italics]()[10])()', '')
        jsfuck =  jsfuck.replace('constauctoa]((false0)[italics]()[10])[])1)String[fontcoloa]()[12])()', '')
        jsfuck =self.fuckend(jsfuck)
        jsfuck=  jsfuck.replace('[(true[])[0]', 't').replace('(true[])[0]', 't').replace('(false[])[1]', 'a').replace('([]fill[])[3]', 'c').replace('([]fill[])[3]', 'c').replace('(undefined[])[2]', 'd').replace('(true[])[3]]]', 'e').replace('(true[])[3]', 'e') .replace('([false]undefined)[10]', 'i') 
        jsfuck = jsfuck.replace('(false[])[2]', 'l').replace('[(false[])[0]', 'f').replace('(true[][(false[])[0]', 'o').replace('(true[]fill)[10]', 'o').replace('[(undefined[])[1]', 'n').replace('(undefined[])[1]', 'n')             
        jsfuck =  jsfuck.replace('(false[])[3]', 's').replace('(true[]fill])[10]', 'o') 
        jsfuck =  jsfuck.replace('(true[])[1]]', 'r')
        jsfuck =  jsfuck.replace('(true[])[1]', 'r')
        jsfuck =  jsfuck.replace('(undefined[])[0]', 'u').replace('([]fill[])[3]', 'c').replace('([]fill][])[3]', 'c').replace('(true[]fill])[10]', 'o')                                                                                                  
        jsfuck =  jsfuck.replace('[constructorna(Number[constructor[])[11]e', '')
        jsfuck =  jsfuck.replace('(((101))toString(21)[1]', 'h')
        jsfuck =  jsfuck.replace('((101))toString(21)[1]', 'h')
        jsfuck =  jsfuck.replace('((211))toString(211)[1]', 'p')
        jsfuck =  jsfuck.replace('((215))toString(216)', 'z')
        jsfuck =  jsfuck.replace('((211))toString(212)', 'v')
        jsfuck =  jsfuck.replace('[constructor)', '').replace('[constructor[])', '')
        jsfuck =  jsfuck.replace('(false[0]String[20]', 'g')
        jsfuck =  jsfuck.replace('(Number[11]', 'm')
        jsfuck =  jsfuck.replace('Stringfontcolor()[11]', '=')
        jsfuck =  jsfuck.replace('(false[0])[italics]()[10]', '/').replace('([]fill][constructor(return/false/)()', '')
        jsfuck =  jsfuck.replace('[constructor()[])[3]', ':')
        jsfuck =  jsfuck.replace('[constructor()[])[2]', '?')
        jsfuck =  jsfuck.replace('(0Stringfontcolor()[12])', 'r')
        jsfuck =  jsfuck.replace('((20))toString(21)]', 'k')                     
        jsfuck =  jsfuck.replace('String[linkr[10]', '&')
        jsfuck =  jsfuck.replace('[constructor', '')
        jsfuck =  jsfuck.replace('([]String[10]', 'S')
        jsfuck =  jsfuck.replace('(String[italics]())[2]', 'C')
        jsfuck =  jsfuck.replace('((212))toString(211)[1]', 'q')
        jsfuck =  jsfuck.replace('((212))toString(213)', 'w')
        jsfuck =  jsfuck.replace('((20))toString(21)', 'k')
        jsfuck =  jsfuck.replace('toString[call]())[11]', 'U')
        jsfuck =  jsfuck.replace('([][entries]()[])[3]', 'j')
        jsfuck =  jsfuck.replace('(NaN[])[0]', 'N')                           
        jsfuck =  jsfuck.replace('((.[[]000000001])[])[2]', '-')
        jsfuck =  jsfuck.replace('([][entries]()[])[2]', 'b').replace('(false[])[0]', 'f').replace('(([]fill])[21]', '%')
        jsfuck =  jsfuck.replace('([][]fill][10]', 'F')
        jsfuck =  jsfuck.replace('([]fill])[21]', '%')
        jsfuck =  jsfuck.replace('([][]fill](return/false/)()[10][]fill](return(NaN[]fill]Ounescape)()', 'R')
        jsfuck =  jsfuck.replace('([]fill][])[slice](-1)))[11]', 'O')
        jsfuck =  jsfuck.replace('(%(228)[])', 'H')#.replace(')[11]', 'O')
        jsfuck =  jsfuck.replace('([])[10]', 'B')
        jsfuck =  jsfuck.replace('(NaN[]fill](return(NaN[]fill])[11][]fill](return(NaN[]fill])[11]escape)()([]fill])[slice](-1)ate)()())[210]', 'T')
        jsfuck =  jsfuck.replace('(true[]fill](return(NaN[]fill])[11][]fill](return(NaN[]fill])[11]escape)()([]fill])[slice](-1)ate)()())[210]', 'M')
        jsfuck =  jsfuck.replace('[]fill](return(NaN[]fill])[11]escape)()([]fill])[slice](-1)', 'D')
        jsfuck =  jsfuck.replace('(false[]fill](return(NaN[]fill])[11]Date)()())[210]', 'G')
        jsfuck =  jsfuck.replace('[]fill](return(NaN[]fill])[11]escape)()', '')
        jsfuck =  jsfuck.replace('[]fill]([]fill](return(NaN[]fill])[11]escape)()', '(')
        jsfuck =  jsfuck.replace('([](false)[10]', 'B')                   
        jsfuck =  jsfuck.replace('([][][10]', 'A')                                         
        jsfuck =  jsfuck.replace('((101))toString(214)[1]', 'x')

        jsfuck =  jsfuck.replace('((1(1[])31000)[])[0]', 'I').replace('[12]', 'E').replace('[(NaN([])[slice](-1))()', '').replace('(NaN([])[slice](-1))()', '')
        jsfuck =  jsfuck.replace(')[11]', 'O')
        jsfuck =  jsfuck.replace('([][]fill](return/false/)()[10][]fill](return(NaN[]fill]Ounescape)()', 'R').replace('[]fill](return(NaN[]fill]Ounescape)()', '').replace('(NaN[]fill](return(true[]fill])[20]([]fill][])[slice](-1))()', '')
        jsfuck =  jsfuck.replace('([][]fill](return/false/)()[10]', 'R')
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
        jsfuck =  jsfuck.replace('(%(2201)[])', 'G')                          
        jsfuck =  jsfuck.replace('(%(2202)[])', 'H')
        jsfuck =  jsfuck.replace('(%(2203)[])', 'I')
        jsfuck =  jsfuck.replace('(%(2204)[])', 'J')
        jsfuck =  jsfuck.replace('(%(2205)[])', 'K')
        jsfuck =  jsfuck.replace('(%(2206)[])', 'L')                          
        jsfuck =  jsfuck.replace('(%(2207)[])', 'M')
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
        jsfuck =  jsfuck.replace('[][flat]constructor](return(NaN[][flat]Oe((211))[toStringconstructor][na(Numberconstructor][]Oe]](212)al)()constructor](returnString[fontcolor]()E(', '')
        jsfuck =  jsfuck.replace(')[s((211))[toStringconstructor][na(Numberconstructor][]Oe]](211)1lit](t)[([][entries]()[])3oin](constructor](return(false0)[italics]()[10]false(false0)[italics]()[10])()constructor]((false0)[italics]()[10])[])1)String[fontcolor]()E)())', '')
        jsfuck =  jsfuck.replace('[][flat]constructor](returnString[fontcolor]()E(', '')
        jsfuck =  jsfuck.replace(')[s((211))[toStringconstructor][na(Numberconstructor][]Oe]](211)1lit](t)[([][entries]()[])3oin](constructor](return(false0)[italics]()[10]false(false0)[italics]()[10])()constructor]((false0)[italics]()[10])[])1)String[fontcolor]()E)()', '')
        return jsfuck                                                    
