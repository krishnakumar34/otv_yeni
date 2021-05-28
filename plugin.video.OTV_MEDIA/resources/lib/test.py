#-*- coding: utf-8 -*-
import sys
import re
import re ,os ,sys

import xbmc, xbmcgui, xbmcaddon, xbmcplugin

import requests

from resources.lib.logger import logger 

import six

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
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

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


      
USE_CHAR_CODE = "USE_CHAR_CODE"

MIN, MAX = 32, 126




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
#        'Array':    '[]',
        'Number':   '(+[])',
        'String':   '([]+[])',
        'Boolean':  '(![])',
        'Function': '[]["fill"]',
        'RegExp':   'Function("return/"+false+"/")()'
}
             
MAPPING = {
        'a':   '(false+"")[1]',
        'b':   '([]["entries"]()+"")[2]',
        'c':   '([]["fill"]+"")[3]',
        'd':   '(undefined+"")[2]',
        'e':   '(true+"")[3]',
        'f':   '([][(false+[])[0]',
        'g':   '(false+[0]+String)[20]',
        'h':   '(+(101))["to"+String["name"]](21)[1]',
        'i':   '([false]+undefined)[10]',
        'j':   '([]["entries"]()+"")[3]',
        'k':   '(+(20))["to"+String["name"]](21)',
        'l':   '(false+"")[2]',
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

def __fillMissingDigits():
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

            MAPPING[str(number)] = '[' + output + ']'

def __fillMissingChars():
        '''
        Iterates over MAPPING and fills missing character values with a string
        containing their ascii value represented in hex

        '''
        for key in MAPPING:
            if MAPPING[key] == USE_CHAR_CODE:
                hexidec = hex(ord(key[0]))[2:]

                digit_search = re.findall(r'\d+', hexidec)
                letter_search = re.findall(r'[^\d+]', hexidec)

                digit = digit_search[0] if digit_search else ''
                letter = letter_search[0] if letter_search else ''

                string = ('Function("return unescape")()("%%"+(%s)+"%s")'
                          % (digit, letter))

                MAPPING[key] = string

def __replaceMap():
        '''
        Iterates over MAPPING from MIN to MAX and replaces value with values
        found in CONSTRUCTORS and SIMPLE, as well as using digitalReplacer and
        numberReplacer to replace numeric values

        '''
        def replace(pattern, replacement):
            return re.sub(pattern, replacement, value, flags=re.I)

        def digitReplacer(x):
            return MAPPING[x.group(1)]

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

        for i in range(MIN, MAX + 1):
            character = chr(i)
            value = MAPPING[character]

            original = ''

            if not value:
                continue

            while value != original:
                original = value

                for key, val in CONSTRUCTORS.items():
                    value = replace(r'\b' + key, val + '["constructor"]')

                for key, val in SIMPLE.items():
                    value = replace(key, val)

            value = replace(r'(\d\d+)', numberReplacer)
            value = replace(r'\((\d)\)', digitReplacer)
            value = replace(r'\[(\d)\]', digitReplacer)

            value = replace(r'GLOBAL', GLOBAL)
            value = replace(r'\+""', '+[]')
            value = replace(r'""', '[]+[]')

            MAPPING[character] = value
def __replaceStrings():
        '''
        Replaces strings added in __replaceMap with there encoded values

        '''
        regex = r'[^\[\]\(\)\!\+]'

        # determines if there are still characters to replace
        def findMissing():
            done = False
            # python 2 workaround for nonlocal
            findMissing.missing = {}

            for key, value in MAPPING.items():
                if re.findall(regex, value):
                    findMissing.missing[key] = value
                    done = True

            return done
def fillMissingChars():
    '''
    将 USE_CHAR_CODE 替换掉
    '''
    for key in MAPPING:
        if MAPPING[key] == USE_CHAR_CODE:
            s = str(hex(ord(key)))[2:]
            string = '''("%"+({})+"{}")'''.format( \
                re.findall('\d+', s)[0] if re.findall('\d', s)     else "", \
                re.findall('[a-zA-Z]+', s)[0] if re.findall('[a-zA-Z]', s) else "")
            MAPPING[key] = """Function("return unescape")()""" + string


def fillMissingDigits():
    '''
    填充MAPPING中 0-9 的数字
    '''
    for num in range(10):
        output = "+[]"
        if num > 0:
            output = "+!" + output
        for i in range(1, num):
            output = "+!+[]" + output
        if num > 1:
            output = output[1:]
        MAPPING[str(num)] = "[" + output + "]"

class replaceMap(object):
    '''
    替换 MAPPING中的
    '''

    def replace(self, pattern, replacement):
        self.value = re.sub(pattern, replacement, self.value)

    def digitReplacer(self, x):
        x = re.findall(r'\d', x.group())[0]
        ## 正则表达式 分组 
        ## python 匹配 \[(\d)\]   例如 [0]  并不是 选中分组\d 即0   而是 [0]
        return MAPPING[x]

    def numberReplacer(self, y):
        values = list(y.group())
        values.reverse()
        head = int(values.pop())
        values.reverse()
        output = "+[]"

        if head > 0:
            output = "+!" + output
        for i in range(1, head):
            output = "+!+[]" + output
        if head > 1:
            output = output[1:]
        output = [output] + values
        output = "+".join(output)
        output = re.sub(r'\d', self.digitReplacer, output)
        return output

    def __init__(self):
        self.character = ""
        self.value = ""
        self.original = ""

        for i in range(MIN, MAX + 1):
            self.character = chr(i)
            self.value = MAPPING[self.character]
            if not self.value:
                continue
            self.original = self.value

            for key in CONSTRUCTORS:
                self.value = re.sub(r'\b' + key, CONSTRUCTORS[key] + '["constructor"]', self.value)

            for key in SIMPLE:
                self.value = re.sub(key, SIMPLE[key], self.value)

            self.replace('(\\d\\d+)', self.numberReplacer)
            self.replace('\\((\\d)\\)', self.digitReplacer)
            self.replace('\\[(\\d)\\]', self.digitReplacer)
            ## python 和 js中正则表达式 () 分组 有区别?

            self.value = re.sub("GLOBAL", GLOBAL, self.value)
            self.value = re.sub(r'\+""', "+[]", self.value)
            self.value = re.sub('\"\"', "[]+[]", self.value)

            MAPPING[self.character] = self.value;
class replaceStrings(object):
    '''
    替换 字符串
    '''

    def findMissing(self):
        self.missing = {}
        done = False
        for m in MAPPING:
            value = MAPPING[m]
            if re.search(self.regEx, value):
                ### Python offers two different primitive operations based on regular expressions:
                ### re.match() checks for a match only at the beginning of the string,
                ### while re.search() checks for a match anywhere in the string (this is what Perl does by default).
                self.missing[m] = value
                done = True
        return done

    def mappingReplacer(self, b):
        return "+".join(list(b.group().strip('""')))
        ## strip去掉 “”

    def valueReplacer(self, c):
        c = c.group()
        return c if c in self.missing else MAPPING[c]
        # return c if self.missing[c] else MAPPING[c]
        ## js  missing[c] 不存在 为undefined
        ## python missing[c] 不存在 会报错

    def __init__(self):
        self.regEx = r'[^\[\]\(\)\!\+]{1}'
        self.missing = {}
        self.count = MAX - MIN

        for m in MAPPING:
            MAPPING[m] = re.sub(r'\"([^\"]+)\"', self.mappingReplacer, MAPPING[m])

        while self.findMissing():
            for m in self.missing:
                value = MAPPING[m]
                value = re.sub(self.regEx, self.valueReplacer, value)
                MAPPING[m] = value
                self.missing[m] = value
                ## for self.missing  此处修改了missing的值  but ok
            self.count -= 1
            if self.count == 0:
                print("Could not compile the following chars:", self.missing)
                break


def krepl_numbers(js):
        numbers = None
        if numbers is None: 
            numbers = k__gen_numbers()
        while True:
            start_js = js
            for key, value in sorted(numbers.items(), key=lambda x: len(x[0]), reverse=True):
                js = js.replace(key, value)
    
            if js == start_js:
               return js



def k__gen_numbers():
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
def decode( jsfuckString):                                                                                 
    
   
     
        
                                                                      #   
         
        #jsfuckString =krepl_numbers(jsfuckString)                                                         [[+!+[]]+0]
       # jsfuckString = re.sub('\+(?!\+)', '', jsfuckString)
       # jsfuckString=jsfuckString.replace('(+(+!+[]+[+[]]+[+!+[]]))', '(+([+!+[]]+[+[]]+[+!+[]]))').replace('[(', '(').replace(']]]])', ']]])')
       
       # __fillMissingDigits()
       # __fillMissingChars()
        #__replaceMap()                             
        #__replaceStrings()                                                                        
        #fillMissingDigits()                                                                  
#        fillMissingChars()             
        #replaceMap()
        #replaceStrings()
        
        
        import OTVJSfuckdec
        from OTVJSfuckdec import OTVJSfuck  
        jsfuck =OTVJSfuck(jsfuckString).decode()
        #jsfuck =jsfuckjsfuckk(jsfuck)
       # jsfuck = test1.decode(jsfuckString)
        #jsfuck =krepl_numbers(jsfuckString)
        # removes concatenation operators
      #  jsfuckString = re.sub('\+(?!\+)', '', jsfuckString)
        #jsfuckString = jsfuckString.replace('[])', '+""').replace('++', '+')

                                 
        return jsfuck 



                                                                                                              
def jsfuckjsfuckk(jsfuck):                      

        jsfuck=  jsfuck.replace('![]', '1').replace('(false[])1', 'a')
        jsfuck = jsfuck.replace('(false[])2', 'l').replace('[([][(false[])0', 'f').replace('(false[])0', 'f').replace('flat])[10]', 'o')             
        jsfuck =  jsfuck.replace('(false[])3', 's').replace('(true[]fill])[10]', 'o') 
        jsfuck =  jsfuck.replace('([][flat]flat][])3', 'c').replace('([][flat][])3', 'c').replace('flat][])3', 'c').replace('(true[]fill])[10]', 'o')                                                                                                  
        jsfuck =  jsfuck.replace('constauctoa](aetuanString[fontcoloa]()[12](', '')
        jsfuck =  jsfuck.replace(')[s((211))[toStringconstauctoa]', '')
        jsfuck =  jsfuck.replace('[na(Numberconstauctoa][])[11]e]](211)1lit](t)[join]', '')
        jsfuck =  jsfuck.replace('(constauctoa](aetuan(false0)[italics]()[10]false(false0)[italics]()[10])()', '')
        jsfuck =  jsfuck.replace('constauctoa]((false0)[italics]()[10])[])1)String[fontcoloa]()[12])()', '')
        return jsfuck                   
                                            
                                          
                                                                                            
def jsfuckjsfuck(jsfuck):                      
                                         
        jsfuck=  jsfuck.replace('![]', '1').replace('[(true[])[0]', 't').replace('(true[])[0]', 't').replace('(false[])[1]', 'a').replace('([]fill[])[3]', 'c').replace('([]fill[])[3]', 'c').replace('(undefined[])[2]', 'd').replace('(true[])[3]]]', 'e').replace('(true[])[3]', 'e') .replace('([false]undefined)[10]', 'i') 
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
        jsfuck =  jsfuck.replace('(0Stringfontcolor()[12])', '')
        jsfuck =  jsfuck.replace('((20))toString(21)]', 'k')
        jsfuck =  jsfuck.replace('String[link[10]', '&')
        jsfuck =  jsfuck.replace('(return(NaN[]fill])[11]escape)()', '')
        jsfuck =  jsfuck.replace('(true[]fill][constructor', '')
        jsfuck =  jsfuck.replace('(NaN[]fill][constructor', '')
        jsfuck =  jsfuck.replace('([][entries]()[])[2]', 'b').replace('(false[])[0]', 'f').replace('(([]fill])[21]', '%')
        jsfuck =  jsfuck.replace('([]fill])[slice](((.[[]000000001])[])[2]1)ate)()())', 'T')
        jsfuck =  jsfuck.replace('([]fill][])[slice](((.[[]000000001])[])[2]1))()', '')
        jsfuck =  jsfuck.replace('([]String[10]', 'S')
        jsfuck =  jsfuck.replace('(String[italics]())[2]', 'C')
        jsfuck =  jsfuck.replace('((212))toString(211)[1]', 'q')
        jsfuck =  jsfuck.replace('((212))toString(213)', 'w')
        jsfuck =  jsfuck.replace('((20))toString(21)', 'k')
        jsfuck =  jsfuck.replace('[]fill][constructor', '')
        jsfuck =  jsfuck.replace('toString[call]())[11]', 'U')
        jsfuck =  jsfuck.replace('(return(true[]fill])[20]', '')
        jsfuck =  jsfuck.replace('([][entries]()[])[3]', 'j')
        jsfuck =  jsfuck.replace('(NaN[])[0]', 'N')
        jsfuck =  jsfuck.replace('((.[[]000000001])[])[2]', '-')
        jsfuck =  jsfuck.replace('([]fill])[slice](-1)', 'D')
        jsfuck =  jsfuck.replace('([][]fill][10]', 'F')
        jsfuck =  jsfuck.replace('([]fill])[21]', '%')
        jsfuck =  jsfuck.replace('(return(NaN[]fill])[11]unescape)()', '')
        jsfuck =  jsfuck.replace('([](return/false/)()[10]', 'B')
        jsfuck =  jsfuck.replace('(return(NaN[]fill])[11]', '')
        #jsfuck =  jsfuck.replace('([](false)[10]', 'A')
        jsfuck =  jsfuck.replace('([][][10]', 'A')                                         
        jsfuck =  jsfuck.replace('((101))toString(214)[1]', 'x')
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
        jsfuck =  jsfuck.replace('((1(1[])31000)[])[0]', 'I')
        jsfuck =  jsfuck.replace('(-)[11]', '').replace('[210]', '')
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
        jsfuck =  jsfuck.replace('(%(2212)[])', 'R')
        jsfuck =  jsfuck.replace('(%(2213)[])', 'S')
        jsfuck =  jsfuck.replace('(%(2214)[])', 'T')
        jsfuck =  jsfuck.replace('(%(2215)[])', 'U')
        jsfuck =  jsfuck.replace('(%(2216)[])', 'V')
        jsfuck =  jsfuck.replace('(%(2217)[])', 'W')
        jsfuck =  jsfuck.replace('(%(2218)[])', 'X')
        jsfuck =  jsfuck.replace('(%(2219)[])', 'Y')
        jsfuck =  jsfuck.replace('(%(2220)[])', 'Z')
        jsfuck =  jsfuck.replace('(false', '')
        jsfuck =  jsfuck.replace('[12]', '').replace(')[11]', '')
        jsfuck =  jsfuck.replace('(%(228)[])', 'H')
        jsfuck =  jsfuck.replace('([])[10]', 'B')
        return jsfuck                                                    
                                              
#https://izle.canlitvlive.io/get.m3u8?pu=iA0dzqr%2A&sa=wiH%2Fy_fC&ha=1cdb2afae532286e2038b37eddf22ee9&ti=1619337794&ci=5ffc9fe7d1fcbe251d64ab04
#https://izle.canlitvlive.io/get.m3u8?pu=iA0dzqr%2A&sa=wiH%2Fy_fC&ha=1cdb2afae532286e2038b37eddf22ee9&ti=1619337794&ci=5ffc9fe7d1fcbe251d64ab04

#https://izle.canlitvlive.io/get.m3u8?pu=Ta855uKj&sa=A%2A%2A7m-lt&ha=d4bd54709a4a900c7ab80f4a269d57f8&ti=1619337244&ci=5ffc9fe7d1fcbe251d64abcc
#https://izle.canlitvlive.io/get.m3u8?pu=Ta855uKj&sa=A%2A%2A7m-lt&ha=d4bd54709a4a900c7ab80f4a269d57f8&ti=1619337244&ci=5ffc9fe7d1fcbe251d64abcc
#https://izle.canlitvlive.io/get.m3u8?pu=yi%2CCyhXd&sa=W8Zgc2nI&ha=3ccfed23b004db76a1304a20c9ec3a28&ti=1619336930&ci=5ffc9fe7d1fcbe251d64ab03
#https://izle.canlitvlive.io/get.m3u8?pu=yi%2CCyhXd&sa=W8Zgc2nI&ha=3ccfed23b004db76a1304a20c9ec3a28&ti=1619336930&ci=5ffc9fe7d1fcbe251d64ab03

#https://izle.canlitvlive.io/get.m3u8?pu=0eU%3Fs%2F%3Fp&sa=UK2mZCXU&ha=5783bda698a0f5062bd6a284ea702201&ti=1619335939&ci=5ffc9fe7d1fcbe251d64ab03
#https://izle.canlitvlive.io/get.m3u8?pu=0eU%3Fs%2F%3Fp&sa=UK2mZX{(-U&ha=5783bda698a0f5062bd6a284ea702201&ti=1619335939&ci=5ffc9fe7d1fcbe251d64ab03
#https://izle.canlitvlive.io/get.m3u8?pu=0e(-U%3Fs%2F%3Fp&sa=(-UK2mZCX(-U&ha=5783bda698a0f5062bd6a284ea702201&ti=1619335939&ci=5ffc9fe7d1fcbe251d64ab03
#https://izle.canlitvlive.io/get.m3u8?pu=0eU%3Fs%2F%3Fp&sa=UK2mZCXU&ha=5783bda698a0f5062bd6a284ea702201&ti=1619335939&ci=5ffc9fe7d1fcbe251d64ab03
def jsunfuck2(js):                                       #



        for key in sorted(KMAPPING, key=lambda k: len(KMAPPING[k]), reverse=True):
          if KMAPPING.get(key) in js:
             js = js.replace(KMAPPING.get(key), '{}'.format(key))
        for key in sorted(SIMPLE, key=lambda k: len(SIMPLE[k]), reverse=True):
          if SIMPLE.get(key) in js:
            js = js.replace(SIMPLE.get(key), '{}'.format(key))

        return js
def jsunfuck(js):
        for key in sorted(MAPPING, key=lambda k: len(MAPPING[k]), reverse=True):
          if MAPPING.get(key) in js:
             js = js.replace(MAPPING.get(key), '{}'.format(key))
        for key in sorted(SIMPLE, key=lambda k: len(SIMPLE[k]), reverse=True):
          if SIMPLE.get(key) in js:
            js = js.replace(SIMPLE.get(key), '{}'.format(key))
        for key in sorted(CONSTRUCTORS, key=lambda k: len(CONSTRUCTORS[k]), reverse=True):
          if CONSTRUCTORS.get(key) in js:
            js = js.replace(CONSTRUCTORS.get(key), '{}'.format(key))
#        for key, value in sorted(
#                list(MAPPING.items()), key=lambda x: len(x[1]), reverse=True):
#            js = js.replace(value, key)    
        return js
def repl_arrays( js):
        for word in sorted(MAPPING.values(), key=lambda x: len(x), reverse=True):
            for index in xrange(0, 100):
                try:
                    repl = word[index]
                    js = js.replace('%s[%d]' % (word, index), repl)
                    return js
                except:
                    pass

def repl_words( js):
        while True:
            start_js = js
            for key, value in sorted(MAPPING.items(), key=lambda x: len(x[0]), reverse=True):
                js = js.replace(value,key )
            for key, value in sorted(SIMPLE.items(), key=lambda x: len(x[0]), reverse=True):
                js = js.replace(value,key )
            for key, value in sorted(CONSTRUCTORS.items(), key=lambda x: len(x[0]), reverse=True):
                js = js.replace(value,key )

            if js == start_js:
                return js
 
 
           


def ddecode( js=None):                                                                                
        '''
        Decodes JSFuck'd Javascript

        Keyword arguments:
        js -- string containing the JSFuck to be decoded (defualt None)

        Returns:
        js -- string of decoded Javascript

        '''
  
        js = __2mapping(js)

        # removes concatenation operators
        js = re.sub('\+(?!\+)', '', js)
        js = js.replace('++', '+')

        # check to see if source js is eval'd
        if "[][fill][constructor]" in js:
            js = uneval(js)

        js = js

        return js



def encode( js=None, wrapWithEval=False, runInParentScope=False):
        '''
        Encodes vanilla Javascript to JSFuck obfuscated Javascript

        Keyword arguments:
        js                            -- string of unobfuscated Javascript

        wrapWithEval        -- boolean determines whether to wrap with an eval

        runInParentScope -- boolean determines whether to run in parents scope

        '''
        output = []

        if not js:
            js = js

            if not js:
                return ""

        regex = ""

        for i in SIMPLE:
            regex += i + "|"

        regex += "."
                 
        def inputReplacer(c):
            c = c.group()
            replacement = SIMPLE[c] if c in SIMPLE else False

            if replacement:
                output.append("[' + replacement + ']+[]")

            else:
                replacement = MAPPING[c] if c in MAPPING else False

                if replacement:
                    output.append(replacement)
                else:
                    replacement = (
                        "([]+[])[" + encode("constructor") + "]"
                        "[" + encode("fromCharCode") + "]"
                        "(" + encode(str(ord(c[0]))) + ")")

                    output.append(replacement)
                    MAPPING[c] = replacement

        re.sub(regex, inputReplacer, js)

        output = "+".join(output)

        if re.search(r"^\d$", js):
            output += "+[]"

        if wrapWithEval:
            if runInParentScope:
                output = ("[][" + encode("fill") + "]"
                          "[" + encode("constructor") + "]"
                          "(" + encode("return eval") + ")()"
                          "(" + output + ")")

            else:
                output = ("[][" + encode("fill") + "]"
                          "[" + encode("constructor") + "]"
                          "(" + output + ")")

        js = output

        return output
                                                                                                                                                                                                                 
def uneval(js):                                                                             


        js = js.replace("[][fill][constructor](", "")
        js = js[:-2]

        ev = "return eval)()("

        if ev in js:
            js = js[(js.find(ev) + len(ev)):]

        return js

def m__mapping( js):
        for key in sorted(MAPPING, key=lambda k: len(MAPPING[k]), reverse=True):
          if MAPPING.get(key) in js:
             js = js.replace(MAPPING.get(key), '{}'.format(key))
        for key in sorted(SIMPLE, key=lambda k: len(SIMPLE[k]), reverse=True):
          if SIMPLE.get(key) in js:
            js = js.replace(SIMPLE.get(key), '{}'.format(key))
           # js = js.replace("[])", ")").replace("[![]0]", "[0]")
        return js
                                               
                                                                                                                                                                                                                                                   
def mmjsunfuck(jsfuckString):                                                                                                                                                                                                                                       
                                                                                                                                                                                                 
        jsPayload= jsfuckString                    
        jsPayload =  jsPayload.replace('(true[])[0]', 't').replace('(false[])[1]', 'a').replace('([]["flat"][])[3]', 'c')
        jsPayload = jsPayload.replace('(false[])[2]', 'l').replace('(false[])[0]', 'f').replace('(false[])[1]', 'a').replace('(true+[]["flat"])[10]+', 'o')                                                                                                                                    
        jsPayload = jsPayload.replace('(+(31))["to"+String["name"]](32)', 'v').replace('("")["fontcolor"]()[12]', '"').replace('(RegExp("/")[])[1]', '\\')
        jsPayload = jsPayload.replace('([]["entries"]()[])[3]', 'j').replace('([false]+undefined)[10]', 'i').replace('((211))["to"+String["name"]](31)[1]', 'p').replace('(false[])[3]', 's')
        jsPayload = jsPayload.replace('(undefined[])[2]', 'd').replace('([][fill][])[3]', 'c').replace('([][entries]()[])[2])', 'b').replace('(([][])[italics]())[2]', 'C').replace('(true[][fill])[![]0]', 'o').replace('(NaN[][fill])[![]1]', ' ').replace('((![]![]11))', 'p').replace('[to([][])', 'e').replace('(false[0])[italics]()[![]0]', '/')
        jsPayload = jsPayload.replace('((![]![]![]1))', 'v').replace('e[constructor][na(([])[constructor][])[![]1]e]](![]![]![]2)', '').replace('(![]![]1)[1]', 'h').replace('((![]![]![]5))', 'z').replace('e[constructor][na(([])[constructor][])[![]1]e]](![]![]![]6)', '')
        jsPayload = jsPayload.replace('e[constructor][na(([])[constructor][])[![]1]e]](![]![]![]1)[1]', '').replace('([][fill]', ':').replace('[constructor](return/false/)()[constructor]()[])[3]', '').replace('(NaN[])[0]', 'N').replace('e[constructor][na(([])[constructor][])[![]1]e]](![]![]![]6)', '')
        jsPayload = jsPayload.replace('(false[0]()', 'g').replace('[constructor])[![]![]0]', '').replace('(([])', 'm').replace('([][])[fontcolor]()[![]1]', '=').replace('e[constructor][na(([])[constructor][])[![]1]e]](![]![]![]6)', '').replace('[constructor][])[![]1]', '').replace('(return/false/)()', '?').replace(':[constructor]', '')
        jsPayload = jsPayload.replace('([][])[lin((![]![]0))', '&').replace('((![]01))', '').replace('[constructor]()', '').replace('e[constructor][name]](![]![]1)](0([][])[fontcolor]()[![]2])[![]0]', '').replace('[][fill][constructor]', '').replace('e[constructor][name]]', '').replace('(return unescape)()', '').replace('(return escape)():)', '').replace('(true(return [slice](((.[[]000000001])[])[2]1)', '-')                    
        jsPayload = jsPayload.replace('[])[2]', '').replace('?[constructor][])[![]2]', '').replace('([][][constructor])[![]0]', '').replace('(return unescape)()', '').replace('(return escape)():)', '').replace('[constructor])[![]0]', '')                                                                                                                                                                                                      
        jsPayload = jsPayload.replace('([][entries]()[])[3]', 'J')                 
        jsPayload = jsPayload.replace('(NaN(return(true[][fill]', 'U') 
        jsPayload = jsPayload.replace('((![]![]![]2))', 'C')                                    
        jsPayload = jsPayload.replace('((![]![]![]3))', 'D') 
        jsPayload = jsPayload.replace('[slice](((.[[]000000001])1)', '%2A')                                                            
        jsPayload = jsPayload.replace('[constructor])[![]0])', '') 
        jsPayload = jsPayload.replace('(false(return [slice](((.[[]000000001])1)ate)()())', '%2C') 
        jsPayload = jsPayload.replace('(return escape)()', '') 
        jsPayload = jsPayload.replace('([][]fill][10]', '') 
        return jsPayload                                                                               


    
#logger.info("canlitvliv: %s" % userer)          
def peerstv(): #affiche les genres          
#    from  jsfuck3 import  JSUnfuckIt
    #from argparse import ArgumentParser
                              
    from resources.lib.jsfuck3 import JSFuck
    from resources.lib.jsunfuck import  MAPPING5
    #phpfuck = PHPFuck()
    Urrl = "https://izle.canlitvlive.io/kanal-d-canli-izle-210402"
    bod =  gegetHtml(Urrl)
    userer= re.search('mplayer.src\((.+?)\);', bod).group(1)
                      #ReadList2

#    jsfuck = JSUnfuckIt()
    #encoded =jsfuck.encode(userer)
#    encoded=MAPPING5(userer)
#    encoded = str(encoded).replace('se[]', 'se').replace('ue[]', 'ue').replace('ned[]', 'ned')
#    data =mmjsunfuck(encoded )
#    endcod=mjsunfuck(userer)
                       
    encoded =JSFuck(userer).encode()
    encoded=MAPPING5(encoded)
    logger.info("encoded: %s" % encoded )
    #this=[]
    #script = phpfuck.encode(string )
   # lines = script.split('/\n+/');
#    oded =JSFuck(data).encode()
   
#      if (lines[i] != ''): 
#         this.append(lines[i] + '\n')
    #data =MAPPING5(data)
 #   encoded = jsunfuck(data)
    
    #encoded = str(encoded).replace('+', '').replace('!', '').replace('(', '').replace(')', '').replace('(', '').replace(']', '').replace('[', '')
#    sPayload = beval(string)
#    regex = re.compile("([^\\+])\\+(?!\\+)", re.MULTILINE | re.DOTALL).findall(encoded)[0]
    #encoded = str(encoded).replace('+', '').replace('!', '').replace('(', '').replace(')', '').replace('(', '').replace(']', '').replace('[', '')
#    sPayload = beval(string)
#    regex = re.compile("([^\\+])\\+(?!\\+)", re.MULTILINE | re.DOTALL).findall(encoded)[0]
                # https://raw.githubusercontent.com/aemkei/jsfuck/master/jsfuck.js
#jsfuck_source = 'https://raw.githubusercontent.com/aemkei/jsfuck/master/jsfuck.js'
##jsfuck_test_source = 'https://raw.githubusercontent.com/aemkei/jsfuck/master/test/jsfuck_test.js'

#jsfuck = requests.get(jsfuck_source).text
#jsfuck = re.sub(r'^[\s\S]*?\(', 'jsfuck=(', jsfuck, 1)
#jsfuck = re.sub(r'fillMissingDigits\(\);[\s\S]*$',
#                'fillMissingDigits();return encode;})()', jsfuck, 1)

#jsfuck = re.sub(r'replaceMap\(\);[\s\S]*$',
#                'replaceMap();return encode;})()', jsfuck, 1)

#jsfuck = re.sub(r'replaceStrings\(\);[\s\S]*$',
#                'replaceStrings;return encode;})()', jsfuck, 1)




#context = execjs.get().compile(jsfuck)
#jsfuck_test = requests.get(jsfuck_test_source).text
#cases = re.findall(r"createTest\(('.*')\);", jsfuck_test) + \
#    [repr(chr(c)) for c in range(32, 127)]

#logger.info("cases: %s" % cases)
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)
ADDON_DATA_DIR = xbmc.translatePath(addon.getAddonInfo('path'))
RESOURCES_DIR = os.path.join(ADDON_DATA_DIR, 'resources')
#input_code = os.path.join(RESOURCES_DIR, 'jsfuck.js')
class JSFuckk():

    def __init__(self):
        f = open(input_code, 'r')
        jsf_code = f.read()
        
       # jsf_code = re.sub(r'^[\s\S]*?\(', 'jsfuck=(', jsf_code, 1)
        jsf_code = execjs.get(jsf_code)
        self.jsf_int = js.compile(jsf_code)
        pass

    def encode(self, code):
        return self.jsf_int.call(code,'1')

class JSFuckk():
#    def __init__(self):  
#    @parameterized.expand(cases)
    def eencode(self,string):
#        f = open(input_code, 'r')
       
#        sfuck = f.read()
       
#        sfuck = re.sub(r'fillMissingDigits\(\);[\s\S]*$',
#                'fillMissingDigits();return encode;})()', sfuck, 1)

#        sfuck = re.sub(r'replaceMap\(\);[\s\S]*$',
#                'replaceMap();return encode;})()',sfuck, 1)

#        sfuck = re.sub(r'replaceStrings\(\);[\s\S]*$',
#                'replaceStrings;return encode;})()', sfuck, 1)

        #jsfuck = re.sub(r'replaceStrings\(\);[\s\S]*$',
        #        'replaceStrings();return encode;})()', jsfuck, 1)
       # jsfuck = re.sub(r'encode\(\);[\s\S]*$',
 #       jsfuck, = re.sub(r'^[\s\S]*?\(', 'self.JSFuck = {', jsfuck, 1)
        #jsfuck = re.sub(r'encode\(\);\s+$',
               # 'encode());return encode;})()', jsfuck, 1)
                                         
        
                     
#               input=context.call('jsfuck', string, 1, 1)

        
        #ontext = execjs.get().compile(sfuck)
        #jsPayload =context.call('jsfuck', string, 1, 1)
        jsPayload = jsPayload.replace('(true[])[0]', 't').replace('(false[])[1]', 'a').replace('([]["flat"][])[3]', 'c')
        jsPayload = jsPayload.replace('(false[])[2]', 'l').replace('(false[])[0])', 'f').replace('(true+[]["flat"])[10]', 'o')
        jsPayload = jsPayload.replace('(undefined[])[1]', 'n').replace('(true[])[1]', 'r').replace('(undefined[])[0]', 'u')
        jsPayload = jsPayload.replace('(true[])[3]', 'e').replace('(undefined[])[1]', 'n').replace('(NaN+[]["flat"])[11]', ' ')
        jsPayload = jsPayload.replace('(+(31))["to"+String["name"]](32)', 'v').replace('("")["fontcolor"]()[12]', '"').replace('(RegExp("/")[])[1]', '\\')
        jsPayload = jsPayload.replace('([]["entries"]()[])[3]', 'j').replace('([false]+undefined)[10]', 'i').replace('(+(211))["to"+String["name"]](31)[1]', 'p').replace('(false[])[3]', 's')
        jsPayload = jsPayload.replace('((![]![]![]1)', 'v').replace('e[constructor][na(([])[constructor][])[![]1]e]](![]![]![]2)', '').replace('(return unescape)()', '').replace('(return escape)():)', '')

       # logger.info("sfuck: %s" % jsPayload)
        #fucked =(start_ev, fight(jsPayload).code, raw_string)
      
                                             
                                                                                                                                              
        #fucked =ntext.call('jsfuck',string,'1')
       # jsf = JSFuckk()                                           
        
       # fucked =jsf.encode( code , '1' )
        #fucked =context.call('jsfuck', code, 1, 1)
       # return fucked
        #string = (fucked)
# fight returns a JSCode object, whose code field is the equivalent javascript code
         # fight(jsfuck_code).code
        #logger.info("fucke: %s" % fucked)
        #js2py.disable_pyimport()
        #logger.info("fucke: %s" % raw_string)
        #fucke= fight(raw_string).value
       # logger.info("fucke: %s" % fucke)
       
