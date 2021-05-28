# -*- coding: utf-8 -*-

	
import re, urllib, urllib2, os, cookielib, base64, sys, random
from urlparse import parse_qs, urlparse, urljoin, urlsplit, urlunsplit
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
from resources.lib.handler.requestHandler3 import cRequestHandler
from resources.lib.parser import Parser as cParser
from resources.hosters.hoster import iHoster
from resources.lib.packer import cPacker

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'	
import re, urllib, urllib2, os, cookielib, base64, sys, random
from urlparse import parse_qs, urlparse, urljoin, urlsplit, urlunsplit
#from platformcode import logger
 
from resources.lib.handler.requestHandler3 import cRequestHandler
from resources.lib.parser import cParser
from resources.hosters.hoster import iHoster

from resources.lib.aadecode import AADecoder
from resources.lib.jjdecode import JJDecoder
from resources.lib.packer import cPacker

from resources.lib.comaddon import dialog, VSlog, xbmc
#Pour le futur
from resources.lib.jsparser import JsParser

import re, urllib2, urllib, base64, math
   
try:
    from decimal import Decimal
except:
    pass
import time
import os.path
import urlparse
try:
    import json
    import math
    from urllib2 import HTTPError, URLError
    import htmlentitydefs
    import string
    import httplib
except:
    pass
try:
    import inspect
    import gzip
    from StringIO import StringIO
    from threading import Lock
except:
    pass	
try:
    import xbmc, xbmcaddon, xbmcplugin
except:
    pass

try:
    import traceback
    import json
    from mycrypt import decrypt
    from xppod import decode_hls
except:
    pass
	
VER = '10.96'
# -*- coding: utf-8 -*-
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
	
import re, urllib, urllib2, os, cookielib, base64, sys, random
from urlparse import parse_qs, urlparse, urljoin, urlsplit, urlunsplit
sys.path.append('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod')
try:
    from decimal import Decimal
except:
    pass
import time
import os.path
try:
    import json
    import operator
    import math
    from urllib2 import HTTPError, URLError
    import htmlentitydefs
    import string
    import httplib
except:
    pass
try:
    import inspect
    import gzip
    from StringIO import StringIO
    from threading import Lock
except:
    pass	
try:
    import xbmc, xbmcaddon, xbmcplugin
except:
    pass
try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.sessions import Session
    from requests.packages.urllib3.util.ssl_ import create_urllib3_context
    from collections import OrderedDict
    REQUST = 1
except:
    REQUST = 0

VER = '10.94'
UA = 'Mozilla/5.0 TURKvod-10'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
HEADERS = {"User-Agent":FF_USER_AGENT}
PY3 = False
if sys.version_info[0] >= 3: PY3 = True; unicode = str; unichr = chr; long = int

_OPERATORS = [
    ('|', operator.or_),
    ('^', operator.xor),
    ('&', operator.and_),
    ('>>', operator.rshift),
    ('<<', operator.lshift),
    ('-', operator.sub),
    ('+', operator.add),
    ('%', operator.mod),
    ('/', operator.truediv),
    ('*', operator.mul),
]

_ASSIGN_OPERATORS = []
for op, opfunc in _OPERATORS:
    _ASSIGN_OPERATORS.append([op + '=', opfunc])
_ASSIGN_OPERATORS.append(('=', lambda cur, right: right))

_NAME_RE = r'[a-zA-Z_$][a-zA-Z_$0-9]*'

class JSInterpreter(object):
    def __init__(self, code, objects=None):
        if objects is None:
            objects = {}
        self.code = code
        self._functions = {}
        self._objects = objects

    def interpret_statement(self, stmt, local_vars, allow_recursion=100):

        should_abort = False
        stmt = stmt.lstrip()
        stmt_m = re.match(r'var\s', stmt)
        if stmt_m:
            expr = stmt[len(stmt_m.group(0)):]
        else:
            return_m = re.match(r'return(?:\s+|$)', stmt)
            if return_m:
                expr = stmt[len(return_m.group(0)):]
                should_abort = True
            else:
                # Try interpreting it as an expression
                expr = stmt

        v = self.interpret_expression(expr, local_vars, allow_recursion)
        return v, should_abort

    def interpret_expression(self, expr, local_vars, allow_recursion):
        expr = expr.strip()

        if expr == '':  # Empty expression
            return None

        if expr.startswith('('):
            parens_count = 0
            for m in re.finditer(r'[()]', expr):
                if m.group(0) == '(':
                    parens_count += 1
                else:
                    parens_count -= 1
                    if parens_count == 0:
                        sub_expr = expr[1:m.start()]
                        sub_result = self.interpret_expression(
                            sub_expr, local_vars, allow_recursion)
                        remaining_expr = expr[m.end():].strip()
                        if not remaining_expr:
                            return sub_result
                        else:
                            expr = json.dumps(sub_result) + remaining_expr
                        break

        for op, opfunc in _ASSIGN_OPERATORS:
            m = re.match(r'''(?x)
                (?P<out>%s)(?:\[(?P<index>[^\]]+?)\])?
                \s*%s
                (?P<expr>.*)$''' % (_NAME_RE, re.escape(op)), expr)
            if not m:
                continue
            right_val = self.interpret_expression(
                m.group('expr'), local_vars, allow_recursion - 1)

            if m.groupdict().get('index'):
                lvar = local_vars[m.group('out')]
                idx = self.interpret_expression(
                    m.group('index'), local_vars, allow_recursion)
                assert isinstance(idx, int)
                cur = lvar[idx]
                val = opfunc(cur, right_val)
                lvar[idx] = val
                return val
            else:
                cur = local_vars.get(m.group('out'))
                val = opfunc(cur, right_val)
                local_vars[m.group('out')] = val
                return val

        if expr.isdigit():
            return int(expr)

        var_m = re.match(
            r'(?!if|return|true|false)(?P<name>%s)$' % _NAME_RE,
            expr)
        if var_m:
            return local_vars[var_m.group('name')]

        try:
            return json.loads(expr)
        except ValueError:
            pass

        m = re.match(
            r'(?P<var>%s)\.(?P<member>[^(]+)(?:\(+(?P<args>[^()]*)\))?$' % _NAME_RE,
            expr)
        if m:
            variable = m.group('var')
            member = m.group('member')
            arg_str = m.group('args')

            if variable in local_vars:
                obj = local_vars[variable]
            else:
                if variable not in self._objects:
                    self._objects[variable] = self.extract_object(variable)
                obj = self._objects[variable]

            if arg_str is None:
                # Member access
                if member == 'length':
                    return len(obj)
                return obj[member]

            assert expr.endswith(')')
            # Function call
            if arg_str == '':
                argvals = tuple()
            else:
                argvals = []
                for v in arg_str.split(','):
                    argvals.extend([self.interpret_expression(v, local_vars, allow_recursion)])
            if member == 'split':
                assert len(argvals) == 1
                return list(obj)
            if member == 'join':
                assert len(argvals) == 1
                return argvals[0].join(obj)
            if member == 'reverse':
                assert len(argvals) == 0
                obj.reverse()
                return obj
            if member == 'slice':
                assert len(argvals) == 1
                return obj[argvals[0]:]
            if member == 'splice':
                assert isinstance(obj, list)
                index, howMany = argvals
                res = []
                for i in range(index, min(index + howMany, len(obj))):
                    res.append(obj.pop(index))
                return res

            return obj[member](argvals)

        m = re.match(
            r'(?P<in>%s)\[(?P<idx>.+)\]$' % _NAME_RE, expr)
        if m:
            val = local_vars[m.group('in')]
            idx = self.interpret_expression(
                m.group('idx'), local_vars, allow_recursion - 1)
            return val[idx]

        for op, opfunc in _OPERATORS:
            m = re.match(r'(?P<x>.+?)%s(?P<y>.+)' % re.escape(op), expr)
            if not m:
                continue
            x, abort = self.interpret_statement(
                m.group('x'), local_vars, allow_recursion - 1)
            y, abort = self.interpret_statement(
                m.group('y'), local_vars, allow_recursion - 1)
            return opfunc(x, y)

        m = re.match(
            r'^(?P<func>%s)\((?P<args>[a-zA-Z0-9_$,]+)\)$' % _NAME_RE, expr)
        if m:
            fname = m.group('func')
            argvals = []
            for v in m.group('args').split(','):
                if v.isdigit():
                    argvals.append([int(v)])
                else:
                    argvals.append([local_vars[v]])

            if fname not in self._functions:
                self._functions[fname] = self.extract_function(fname)
            return self._functions[fname](argvals)


    def extract_object(self, objname):
        obj = {}
        obj_m = re.search(
            (r'(?:var\s+)?%s\s*=\s*\{' % re.escape(objname)) +
            r'\s*(?P<fields>([a-zA-Z$0-9]+\s*:\s*function\(.*?\)\s*\{.*?\}(?:,\s*)?)*)' +
            r'\}\s*;',
            self.code)
        fields = obj_m.group('fields')
        # Currently, it only supports function definitions
        fields_m = re.finditer(
            r'(?P<key>[a-zA-Z$0-9]+)\s*:\s*function'
            r'\((?P<args>[a-z,]+)\){(?P<code>[^}]+)}',
            fields)
        for f in fields_m:
            argnames = f.group('args').split(',')
            obj[f.group('key')] = self.build_function(argnames, f.group('code'))

        return obj

    def extract_function(self, funcname):
        func_m = re.search(
            r'''(?x)
                (?:function\s+%s|[{;,]\s*%s\s*=\s*function|var\s+%s\s*=\s*function)\s*
                \((?P<args>[^)]*)\)\s*
                \{(?P<code>[^}]+)\}''' % (
                re.escape(funcname), re.escape(funcname), re.escape(funcname)),
            self.code)
        argnames = func_m.group('args').split(',')

        return self.build_function(argnames, func_m.group('code'))

    def call_function(self, funcname, *args):
        f = self.extract_function(funcname)
        return f(args)

    def build_function(self, argnames, code):
        def resf(args):
            local_vars = dict(zip(argnames, args))
            for stmt in code.split(';'):
                res, abort = self.interpret_statement(stmt, local_vars)
                if abort:
                    break
            return res
        return resf

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
        return dct.decode('utf-8')
    else:
        return dct


def load(*args, **kwargs):
    if "object_hook" not in kwargs:
        kwargs["object_hook"] = to_utf8

    try:
        value = json.loads(*args, **kwargs)
    except:
        value = {}

    return value

itag_list = {18: "mp4 360p",
             22: "mp4 720p",
             336: "webm 1440p hdr"}

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)
    
if REQUST == 1:

    ########## Cookie ##########

    class GetCookie():

        try:
            addonId = "plugin.video.turkvod"
            PathCache = xbmc.translatePath('special://profile/addon_data/%s' % (addonId))
        except:
            PathCache = ""

        def DeleteCookie(self,Domain):
            file = os.path.join(self.PathCache,'Cookie_'+ str(Domain) +'.txt')
            os.remove(os.path.join(self.PathCache,file))

        def SaveCookie(self,Domain,data):
            Name = os.path.join(self.PathCache,'Cookie_'+ str(Domain) +'.txt')
            file = open(Name,'w')
            file.write(data)
            file.close()

        def Readcookie(self,Domain):
            Name = os.path.join(self.PathCache,'Cookie_'+ str(Domain) +'.txt')
            try:
                file = open(Name,'r')
                data = file.read()
                file.close()
            except:
                return ''
            return data

        def AddCookies(self):
            cookies = self.Readcookie(self.__sHosterIdentifier)
            return 'Cookie=' + cookies

    ########## Cookie ##########

    ########## jsunfuck ##########

    class JSUnfuck(object):
        numbers = None
        words = {
            "(![]+[])": "false",
            "([]+{})": "[object Object]",
            "(!![]+[])": "true",
            "([][[]]+[])": "undefined",
            "(+{}+[])": "NaN",
            "([![]]+[][[]])": "falseundefined",
            "([][f+i+l+t+e+r]+[])": "function filter() { [native code] }",
            "(!![]+[][f+i+l+t+e+r])": "truefunction filter() { [native code] }",
            "(+![]+([]+[])[c+o+n+s+t+r+u+c+t+o+r])": "0function String() { [native code] }",
            "(+![]+[![]]+([]+[])[c+o+n+s+t+r+u+c+t+o+r])": "0falsefunction String() { [native code] }",
            "([]+[][s+o+r+t][c+o+n+s+t+r+u+c+t+o+r](r+e+t+u+r+n+ +l+o+c+a+t+i+o+n)())": "https://123movies.to",
            "([]+[])[f+o+n+t+c+o+l+o+r]()": '<font color="undefined"></font>',
            "(+(+!![]+e+1+0+0+0)+[])": "Infinity",
            "(+[![]]+[][f+i+l+t+e+r])": 'NaNfunction filter() { [native code] }',
            '(+[![]]+[+(+!+[]+(!+[]+[])[3]+[1]+[0]+[0]+[0])])': 'NaNInfinity',
            '([]+[])[i+t+a+l+i+c+s]()': '<i></i>',
            '[[]][c+o+n+c+a+t]([[]])+[]': ',',
            '([][f+i+l+l]+[])': 'function fill() {    [native code]}',
            '(!![]+[][f+i+l+l])': 'truefunction fill() {    [native code]}',
            '((+[])[c+o+n+s+t+r+u+c+t+o+r]+[])': 'function Number() {[native code]}  _display:45:1',
            '(+(+!+[]+[1]+e+[2]+[0])+[])': '1.1e+21',
            '([]+[])[c+o+n+s+t+r+u+c+t+o+r][n+a+m+e]': 'S+t+r+i+n+g',
            '([][e+n+t+r+i+e+s]()+[])': '[object Array Iterator]',
            '([]+[])[l+i+n+k](")': '<a href="&quot;"></a>',
            '(![]+[0])[i+t+a+l+i+c+s]()': '<i>false0</i>',
            # dummy to force array dereference
            'DUMMY1': '6p',
            'DUMMY2': '2x',
            'DUMMY3': '%3C',
            'DUMMY4': '%5B',
            'DUMMY5': '6q',
            'DUMMY6': '4h',
        }
        
        uniqs = {
            '[t+o+S+t+r+i+n+g]': 1,
            '[][f+i+l+t+e+r][c+o+n+s+t+r+u+c+t+o+r](r+e+t+u+r+n+ +e+s+c+a+p+e)()': 2,
            '[][f+i+l+t+e+r][c+o+n+s+t+r+u+c+t+o+r](r+e+t+u+r+n+ +u+n+e+s+c+a+p+e)()': 3,
            '[][s+o+r+t][c+o+n+s+t+r+u+c+t+o+r](r+e+t+u+r+n+ +e+s+c+a+p+e)()': 2,
            '[][s+o+r+t][c+o+n+s+t+r+u+c+t+o+r](r+e+t+u+r+n+ +u+n+e+s+c+a+p+e)()': 3,
        }
        
        def __init__(self, js):
            self.js = js
            
        def decode(self, replace_plus=True):
            while True:
                start_js = self.js
                self.repl_words(self.words)
                self.repl_numbers()
                self.repl_arrays(self.words)
                self.repl_uniqs(self.uniqs)
                if start_js == self.js:
                    break
        
            if replace_plus:
                self.js = self.js.replace('+', '')
            self.js = re.sub('\[[A-Za-z]*\]', '', self.js)
            self.js = re.sub('\[(\d+)\]', '\\1', self.js)
            self.js = self.js.replace('(+)','0')
            self.js = self.js.replace('(+!!)','1')
            
            return self.js
        
        def repl_words(self, words):
            while True:
                start_js = self.js
                for key, value in sorted(words.items(), key=lambda x: len(x[0]), reverse=True):
                    self.js = self.js.replace(key, value)
        
                if self.js == start_js:
                    break
        
        def repl_arrays(self, words):
            for word in sorted(words.values(), key=lambda x: len(x), reverse=True):
                for index in range(0, 100):
                    try:
                        repl = word[index]
                        self.js = self.js.replace('%s[%d]' % (word, index), repl)
                    except:
                        pass
            
        def repl_numbers(self):
            if self.numbers is None:
                self.numbers = self.__gen_numbers()
                
            while True:
                start_js = self.js
                for key, value in sorted(self.numbers.items(), key=lambda x: len(x[0]), reverse=True):
                    self.js = self.js.replace(key, value)
        
                if self.js == start_js:
                    break
            
        def repl_uniqs(self, uniqs):
            for key, value in uniqs.items():
                if key in self.js:
                    if value == 1:
                        self.__handle_tostring()
                    elif value == 2:
                        self.__handle_escape(key)
                    elif value == 3:
                        self.__handle_unescape(key)
                                                    
        def __handle_tostring(self):
            for match in re.finditer('(\d+)\[t\+o\+S\+t\+r\+i\+n\+g\](\d+)', self.js):
                repl = to_base(match.group(1), match.group(2))
                self.js = self.js.replace(match.group(0), repl)
        
        def __handle_escape(self, key):
            while True:
                start_js = self.js
                offset = self.js.find(key) + len(key)
                if self.js[offset] == '(' and self.js[offset + 2] == ')':
                    c = self.js[offset + 1]
                    self.js = self.js.replace('%s(%s)' % (key, c), urllib.quote(c))
                
                if start_js == self.js:
                    break
        
        def __handle_unescape(self, key):
            start = 0
            while True:
                start_js = self.js
                offset = self.js.find(key, start)
                if offset == -1: break
                
                offset += len(key)
                expr = ''
                extra = ''
                last_c = self.js[offset - 1]
                abort = False
                for i, c in enumerate(self.js[offset:]):
                    extra += c
                    if c == ')':
                        break
                    elif (i > 0 and c == '(') or (c == '[' and last_c != '+'):
                        abort = True
                        break
                    elif c == '%' or c in string.hexdigits:
                        expr += c
                    last_c = c
                     
                if not abort:
                    self.js = self.js.replace(key + extra, urllib.unquote(expr))
                
                    if start_js == self.js:
                        break
                else:
                    start = offset
            
        def __gen_numbers(self):
            n = {'(+[]+[])': '0', '(+![]+([]+[]))': '0', '[+[]]': '[0]',
                 '(+!![]+[])': '1', '[+!+[]]': '[1]', '[+!![]]': '[1]', 
                 '[+!+[]+[+[]]]': '[10]', '+(1+1)': '11', '(+20)': '20'}
            
            for i in range(2, 20):
                key = '+!![]' * (i - 1)
                key = '!+[]' + key
                n['(' + key + ')'] = str(i)
                key += '+[]'
                n['(' + key + ')'] = str(i)
                n['[' + key + ']'] = '[' + str(i) + ']'
         
            for i in range(2, 10):
                key = '!+[]+' * (i - 1) + '!+[]'
                n['(' + key + ')'] = str(i)
                n['[' + key + ']'] = '[' + str(i) + ']'
                 
                key = '!+[]' + '+!![]' * (i - 1)
                n['[' + key + ']'] = '[' + str(i) + ']'
                    
            for i in range(0, 10):
                key = '(+(+!+[]+[%d]))' % (i)
                n[key] = str(i + 10)
                key = '[+!+[]+[%s]]' % (i)
                n[key] = '[' + str(i + 10) + ']'
                
            for tens in range(2, 10):
                for ones in range(0, 10):
                    key = '!+[]+' * (tens) + '[%d]' % (ones)
                    n['(' + key + ')'] = str(tens * 10 + ones)
                    n['[' + key + ']'] = '[' + str(tens * 10 + ones) + ']'
            
            for hundreds in range(1, 10):
                for tens in range(0, 10):
                    for ones in range(0, 10):
                        key = '+!+[]' * hundreds + '+[%d]+[%d]))' % (tens, ones)
                        if hundreds > 1: key = key[1:]
                        key = '(+(' + key
                        n[key] = str(hundreds * 100 + tens * 10 + ones)
            return n
        
    def to_base(n, base, digits="0123456789abcdefghijklmnopqrstuvwxyz"):
        n, base = int(n), int(base)
        if n < base:
            return digits[n]
        else:
            return to_base(n // base, base, digits).lstrip(digits[0]) + digits[n % base]


    ########## jsunfuck ##########

    ########## cloudflare ##########

    class CipherSuiteAdapter(HTTPAdapter):

        def __init__(self, cipherSuite=None, **kwargs):
            self.cipherSuite = cipherSuite

            if hasattr(ssl, 'PROTOCOL_TLS'):
                self.ssl_context = create_urllib3_context(
                    ssl_version=getattr(ssl, 'PROTOCOL_TLSv1_3', ssl.PROTOCOL_TLSv1_2),
                    ciphers=self.cipherSuite
                )
            else:
                self.ssl_context = create_urllib3_context(ssl_version=ssl.PROTOCOL_TLSv1)

            super(CipherSuiteAdapter, self).__init__(**kwargs)

        def init_poolmanager(self, *args, **kwargs):
            kwargs['ssl_context'] = self.ssl_context
            return super(CipherSuiteAdapter, self).init_poolmanager(*args, **kwargs)

        def proxy_manager_for(self, *args, **kwargs):
            kwargs['ssl_context'] = self.ssl_context
            return super(CipherSuiteAdapter, self).proxy_manager_for(*args, **kwargs)

    UAG = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'

    def checklowerkey(key,dict):
        for i in dict:
            if str(i.lower()) == str(key.lower()):
                return i
        return False

    def solvecharcode(chain,t):

        v = chain.find('t.charCodeAt') + 12
        if v == 11:
            return chain
            
        dat = checkpart(chain[v:],')')

        r = parseInt(dat)
        v = ord(t[int(r)])
        chain = chain.replace('t.charCodeAt' + dat, '+' + str(v) )
        chain = chain.replace( '(' + '+' + str(v) + ')' , '+' + str(v))

        return chain

    def checkpart(s,end='+'):
        p = 0
        pos = 0

        try:
            while (1):
                c = s[pos]
                
                if (c == '('):
                    p = p + 1
                if (c == ')'):
                    p = p - 1
                    
                pos = pos + 1
                    
                if (c == end) and (p == 0) and (pos > 1):
                    break   
        except:
            pass

        return s[:pos]

    def parseInt(s):
        v = JSUnfuck(s).decode(False)
        v = re.sub('([^\(\)])\++', '\\1', v)
        v = eval(v)
        return v

    def CheckIfActive(data):
        if 'Checking your browser before accessing' in str(data):
            return True
        return False

    def showInfo(sTitle, sDescription, iSeconds=0):
        if (iSeconds == 0):
            iSeconds = 1000
        else:
            iSeconds = iSeconds * 1000

    class CloudflareBypass(object):

        def __init__(self):
            self.state = False
            self.HttpReponse = None
            self.Memorised_Headers = None
            self.Memorised_PostData = None
            self.Memorised_Cookies = None
            self.Header = None
            self.RedirectionUrl = None

        def GetHeadercookie(self,url):
            Domain = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',url)
            cook = GetCookie().Readcookie(Domain.replace('.','_'))
            if cook == '':
                return ''
            return '|' + urllib.urlencode({'User-Agent':UAG,'Cookie': cook })

        def ParseCookies(self,data):
            list = {}
            sPattern = '(?:^|[,;]) *([^;,]+?)=([^;,\/]+)'
            aResult = re.findall(sPattern,data)
            if (aResult):
                for cook in aResult:
                    if 'deleted' in cook[1]:
                        continue
                    list[cook[0]]= cook[1]
            return list

        def SetHeader(self):
            head = OrderedDict()
            h = ['User-Agent','Accept','Accept-Language','Accept-Encoding','Connection','Upgrade-Insecure-Requests']
            v = [UAG,'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','en-US,en;q=0.5','gzip, deflate','close','1']
            for i in enumerate(h):
                k = checklowerkey(i[1],self.Memorised_Headers)
                if k:
                    head[i[1]] = self.Memorised_Headers[k]
                else:
                    head[i[1]] = v[i[0]]
            if 'Referer' in self.Memorised_Headers:
                head['Referer'] = self.Memorised_Headers['Referer']
            
            if (False):
                Headers = ['User-Agent','Accept','Accept-Language','Accept-Encoding','Cache-Control','Dnt','Pragma','Connexion']
                Headers_l = [x.lower() for x in Headers]
                head2 = dict(head)
                for key in head2:
                    if not key in Headers and key.lower() in Headers_l:
                        p  = Headers_l.index(key.lower())
                        head[Headers[p]] = head[key]
                        del head[key]

            return head

        def GetResponse(self,htmlcontent,domain):
            rq = re.search('<div style="display:none;visibility:hidden;" id="(.*?)">(.*?)<\/div>', str(htmlcontent),re.MULTILINE | re.DOTALL)
            id = rq.group(1)
            val = rq.group(2)
            htmlcontent = re.sub(
                r'function\(p\){var p = eval\(eval\(.+?return \+\(p\)}\(\);',
                "{};".format(rq.group(2)),
                str(htmlcontent)
            )
            if '+ t.length' not in htmlcontent:
                pass

            line1 = re.findall('var s,t,o,p,b,r,e,a,k,i,n,g,f, (.+?)={"(.+?)":\+*(.+?)};',str(htmlcontent))

            varname = line1[0][0] + '.' + line1[0][1]
            calcul = parseInt(line1[0][2])
            t = domain
            js = htmlcontent
            js = re.sub(r"a\.value = ((.+).toFixed\(10\))?", r"\1", js)
            js = re.sub(r"\s{3,}[a-z](?: = |\.).+", "", js).replace("t.length", str(len(domain)))
            js = js.replace('; 121', '')
            js = re.sub(r'function\(p\){return eval\(\(true\+.+?}', 't.charCodeAt',js)
            js = re.sub(r"[\n\\']", "", js)
            js = solvecharcode(js,t)
            htmlcontent = js
            AllLines = re.findall(';' + varname + '([*\-+])=([^;]+)',str(htmlcontent))
            for aEntry in AllLines:
                s = str(aEntry[0])
                v = parseInt(aEntry[1])
                calcul = eval( format(calcul,'.17g') + str(aEntry[0]) + format(v,'.17g'))
            rep = calcul
            ret = format(rep,'.10f')
            return (str(ret))

        def GetReponseInfo(self):
            return self.RedirectionUrl, self.Header

        def GetHtml(self,url,htmlcontent = '',cookies = '',postdata = None,Gived_headers = ''):

            self.Memorised_Headers = Gived_headers
            self.Memorised_PostData = postdata
            self.Memorised_Cookies = cookies
            if Gived_headers != '':
                if Gived_headers.get('Cookie',None):
                    if cookies:
                        self.Memorised_Cookies = cookies + '; ' + Gived_headers.get('Cookie')
                    else:
                        self.Memorised_Cookies = Gived_headers['Cookie']

            self.hostComplet = re.sub(r'(https*:\/\/[^/]+)(\/*.*)','\\1',url)
            self.host = re.sub(r'https*:\/\/','',self.hostComplet)
            self.url = url

            cookieMem = GetCookie().Readcookie(self.host.replace('.', '_'))
            if not (cookieMem == ''):
                if not (self.Memorised_Cookies):
                    cookies = cookieMem
                else:
                    cookies = self.Memorised_Cookies + '; ' + cookieMem
            else:
                pass
                    
            data = {}
            if postdata:
                method = 'POST'
                d = postdata.split('&')
                for dd in d:
                    ddd = dd.split('=')
                    data[ddd[0]] = ddd[1]
            else:
                method = 'GET'

            s = CloudflareScraper()
            
            r = s.request(method,url,headers = self.SetHeader() , cookies = self.ParseCookies(cookies) , data = data )
            if r:
                sContent = r.text.encode("utf-8")
                self.RedirectionUrl = r.url
                self.Header = r.headers
            else:
                sContent = ''
                s.MemCookie = ''
                GetCookie().DeleteCookie(self.host.replace('.', '_'))
            c = ''
            cookie = s.MemCookie
            if cookie:
                for i in cookie:
                    c = c + i + '=' + cookie[i] + ';'
                GetCookie().SaveCookie(self.host.replace('.', '_'),c)
            
            return sContent

    class CloudflareScraper(Session):
        def __init__(self, *args, **kwargs):
        
            super(CloudflareScraper, self).__init__(*args, **kwargs)
            self.cf_tries = 0
            self.GetCaptha = False
            
            self.firsturl = ''
            
            self.headers = {
                    'User-Agent': UAG,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'close',
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache',
                    'DNT': '1'
                }
                
            self.cipherHeader = {
                    'cipherSuite': [
                        "TLS_AES_128_GCM_SHA256",
                        "TLS_CHACHA20_POLY1305_SHA256",
                        "TLS_AES_256_GCM_SHA384",
                        "ECDHE-ECDSA-AES128-GCM-SHA256",
                        "ECDHE-RSA-AES128-GCM-SHA256",
                        "ECDHE-ECDSA-CHACHA20-POLY1305",
                        "ECDHE-RSA-CHACHA20-POLY1305",
                        "ECDHE-ECDSA-AES256-GCM-SHA384",
                        "ECDHE-RSA-AES256-GCM-SHA384",
                        "ECDHE-ECDSA-AES256-SHA",
                        "ECDHE-ECDSA-AES128-SHA",
                        "ECDHE-RSA-AES128-SHA",
                        "ECDHE-RSA-AES256-SHA",
                        "DHE-RSA-AES128-SHA",
                        "AES128-SHA",
                        "AES256-SHA"
                    ],
                }

            self.MemCookie = {}
            
            self.cipherSuite = None
            self.mount('https://', CipherSuiteAdapter(self.loadCipherSuite()))

        def loadCipherSuite(self):
            if self.cipherSuite:
                return self.cipherSuite

            self.cipherSuite = ''

            if hasattr(ssl, 'PROTOCOL_TLS'):
                ciphers = [
                    'ECDHE-ECDSA-AES128-GCM-SHA256', 'ECDHE-ECDSA-CHACHA20-POLY1305-SHA256', 'ECDHE-RSA-CHACHA20-POLY1305-SHA256',
                    'ECDHE-RSA-AES128-CBC-SHA', 'ECDHE-RSA-AES256-CBC-SHA', 'RSA-AES128-GCM-SHA256',
                    'RSA-AES256-GCM-SHA384', 'RSA-AES256-SHA', '3DES-EDE-CBC'
                ]

                if hasattr(ssl, 'PROTOCOL_TLSv1_3'):
                    ciphers.insert(0, ['GREASE_3A', 'GREASE_6A', 'AES128-GCM-SHA256', 'AES256-GCM-SHA256', 'AES256-GCM-SHA384', 'CHACHA20-POLY1305-SHA256'])

                ctx = ssl.SSLContext(getattr(ssl, 'PROTOCOL_TLSv1_3', ssl.PROTOCOL_TLSv1_2))

                for cipher in ciphers:
                    try:
                        ctx.set_ciphers(cipher)
                        self.cipherSuite = '{}:{}'.format(self.cipherSuite, cipher).rstrip(':')
                    except ssl.SSLError:
                        pass

            return self.cipherSuite

        def request(self, method, url, *args, **kwargs):
            
            if self.firsturl == '':
                self.firsturl = url
            
            if 'cookies' in kwargs:
                self.MemCookie.update( kwargs['cookies'] )
            resp = super(CloudflareScraper, self).request(method, url, *args, **kwargs)
            self.MemCookie.update( resp.cookies.get_dict() )
            kwargs['cookies'].update( resp.cookies.get_dict() )
            if self.ifCloudflare(resp):
                resp2 = self.solve_cf_challenge(resp, **kwargs)
                return resp2
            return resp

        def ifCloudflare(self, resp):
            if resp.headers.get('Server', '').startswith('cloudflare'):
                if self.cf_tries >= 3:
                    print ('Failed to solve Cloudflare challenge!' )
                elif b'/cdn-cgi/l/chk_captcha' in resp.content:
                    if not self.GetCaptha:
                        self.GetCaptha = True
                        self.cf_tries = 0
                elif resp.status_code == 503:
                    return True
                elif resp.status_code == 403:
                    print ('403 Forbidden' )
                resp = False
                return False
            else:
                return False

        def solve_cf_challenge(self, resp, **original_kwargs):
            self.cf_tries += 1
            body = resp.text
            parsed_url = urlparse(resp.url)
            domain = parsed_url.netloc
            submit_url = "%s://%s/cdn-cgi/l/chk_jschl" % (parsed_url.scheme, domain)

            cloudflare_kwargs = original_kwargs.copy( )
            params = cloudflare_kwargs.setdefault("params", OrderedDict())
            headers = cloudflare_kwargs.setdefault("headers", {})
            headers["Referer"] = str(resp.url)
            try:
                cf_delay = float(re.search('submit.*?(\d+)', body, re.DOTALL).group(1)) / 1000.0

                form_index = body.find('id="challenge-form"')
                if form_index == -1:
                    raise Exception('CF form not found')
                sub_body = body[form_index:]

                s_match = re.search('name="s" value="(.+?)"', sub_body)
                if s_match:
                    params["s"] = s_match.group(1)
                params["jschl_vc"] = str(re.search(r'name="jschl_vc" value="(\w+)"', sub_body).group(1))
                params["pass"] = str(re.search(r'name="pass" value="(.+?)"', sub_body).group(1))

                if body.find('id="cf-dn-', form_index) != -1:
                    extra_div_expression = re.search('id="cf-dn-.*?>(.+?)<', sub_body).group(1)
                js_answer = self.cf_parse_expression(
                    re.search('setTimeout\(function\(.*?:(.*?)}', body, re.DOTALL).group(1)
                )
                builder = re.search("challenge-form'\);\s*;(.*);a.value", body, re.DOTALL).group(1)
                lines = builder.replace(' return +(p)}();', '', 1).split(';')

                for line in lines:
                    if len(line) and '=' in line:
                        heading, expression = line.split('=', 1)
                        if 'eval(eval(' in expression:
                            expression_value = self.cf_parse_expression(extra_div_expression)
                        elif 'function(p' in expression:
                            expression_value = self.cf_parse_expression(expression, domain)
                        else:
                            expression_value = self.cf_parse_expression(expression)
                        js_answer = self.cf_arithmetic_op(heading[-1], js_answer, expression_value)

                if '+ t.length' in body:
                    js_answer += len(domain) 

                params["jschl_answer"] = '%.10f' % js_answer

            except Exception as e:
                raise
            time.sleep(cf_delay + 1.0)
            method = resp.request.method
            cloudflare_kwargs["allow_redirects"] = False
            redirect = self.request(method, submit_url, **cloudflare_kwargs) 
            
            if not redirect:
                return False
            if 'Location' in redirect.headers:
                redirect_location = urlparse(redirect.headers["Location"])
                if not redirect.headers["Location"].startswith('http'):
                    redirect = 'https://'+domain+redirect.headers["Location"]
                else:
                    redirect = redirect.headers["Location"]

                response = self.request(method, redirect, **original_kwargs)
            else:
                response = redirect
            self.cf_tries = 0
            return response

        def cf_sample_domain_function(self, func_expression, domain):
            parameter_start_index = func_expression.find('}(') + 2
            sample_index = self.cf_parse_expression(
                func_expression[parameter_start_index : func_expression.rfind(')))')]
            )
            return ord(domain[int(sample_index)])

        def cf_arithmetic_op(self, op, a, b):
            if op == '+':
                return a + b
            elif op == '/':
                return a / float(b)
            elif op == '*':
                return a * float(b)
            elif op == '-':
                return a - b
            else:
                raise Exception('Unknown operation')

        def cf_parse_expression(self, expression, domain=None):

            def _get_jsfuck_number(section):
                digit_expressions = section.replace('!+[]', '1').replace('+!![]', '1').replace('+[]', '0').split('+')
                return int(
                    ''.join(
                        str(sum(int(digit_char) for digit_char in digit_expression[1:-1])) 
                        for digit_expression in digit_expressions
                    )
                )

            if '/' in expression:
                dividend, divisor = expression.split('/')
                dividend = dividend[2:-1] 

                if domain:
                    divisor_a, divisor_b = divisor.split('))+(')
                    divisor_a = _get_jsfuck_number(divisor_a[5:])
                    divisor_b = self.cf_sample_domain_function(divisor_b, domain)
                    return _get_jsfuck_number(dividend) / float(divisor_a + divisor_b)
                else:
                    divisor = divisor[2:-1]
                    return _get_jsfuck_number(dividend) / float(_get_jsfuck_number(divisor))
            else:
                return _get_jsfuck_number(expression[2:-1])


    ########## cloudflare ##########


    ########## httptools-vs ##########

     ########## httptools-vs ##########
    
class cPacker():
    def detect(self, source):
        """Detects whether `source` is P.A.C.K.E.R. coded."""
        return source.replace(' ', '').startswith('eval(function(p,a,c,k,e,')

    def unpack(self, source):
        """Unpacks P.A.C.K.E.R. packed js code."""
        payload, symtab, radix, count = self._filterargs(source)

        if count != len(symtab):
            raise UnpackingError('Malformed p.a.c.k.e.r. symtab.')
        
        try:
            unbase = Unbaser(radix)
        except TypeError:
            raise UnpackingError('Unknown p.a.c.k.e.r. encoding.')

        def lookup(match):
            """Look up symbols in the synthetic symtab."""
            word  = match.group(0)
            return symtab[unbase(word)] or word

        source = re.sub(r'\b\w+\b', lookup, payload)
        return self._replacestrings(source)

    def _cleanstr(self, str):
        str = str.strip()
        if str.find("function") == 0:
            pattern = (r"=\"([^\"]+).*}\s*\((\d+)\)")
            args = re.search(pattern, str, re.DOTALL)
            if args:
                a = args.groups()
                def openload_re(match):
                    c = match.group(0)
                    b = ord(c) + int(a[1])
                    return chr(b if (90 if c <= "Z" else 122) >= b else b - 26)

                str = re.sub(r"[a-zA-Z]", openload_re, a[0]);
                str = urllib2.unquote(str)

        elif str.find("decodeURIComponent") == 0:
            str = re.sub(r"(^decodeURIComponent\s*\(\s*('|\"))|(('|\")\s*\)$)", "", str);
            str = urllib2.unquote(str)
        elif str.find("\"") == 0:
            str = re.sub(r"(^\")|(\"$)|(\".*?\")", "", str);
        elif str.find("'") == 0:
            str = re.sub(r"(^')|('$)|('.*?')", "", str);

        return str

    def _filterargs(self, source):
        """Juice from a source file the four args needed by decoder."""
        
        source = source.replace(',[],',',0,')

        juicer = (r"}\s*\(\s*(.*?)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*\((.*?)\).split\((.*?)\)")
        args = re.search(juicer, source, re.DOTALL)
        if args:
            a = args.groups()
            try:
                return self._cleanstr(a[0]), self._cleanstr(a[3]).split(self._cleanstr(a[4])), int(a[1]), int(a[2])
            except ValueError:
                raise UnpackingError('Corrupted p.a.c.k.e.r. data.')

        juicer = (r"}\('(.*)', *(\d+), *(\d+), *'(.*)'\.split\('(.*?)'\)")
        args = re.search(juicer, source, re.DOTALL)
        if args:
            a = args.groups()
            try:
                return a[0], a[3].split(a[4]), int(a[1]), int(a[2])
            except ValueError:
                raise UnpackingError('Corrupted p.a.c.k.e.r. data.')

        # could not find a satisfying regex
        raise UnpackingError('Could not make sense of p.a.c.k.e.r data (unexpected code structure)')



    def _replacestrings(self, source):
        """Strip string lookup table (list) and replace values in source."""
        match = re.search(r'var *(_\w+)\=\["(.*?)"\];', source, re.DOTALL)

        if match:
            varname, strings = match.groups()
            startpoint = len(match.group(0))
            lookup = strings.split('","')
            variable = '%s[%%d]' % varname
            for index, value in enumerate(lookup):
                source = source.replace(variable % index, '"%s"' % value)
            return source[startpoint:]
        return source
        
def UnpackingError(Exception):
    #Badly packed source or general error.#
    #xbmc.log(str(Exception))
    print Exception
    pass

class Unbaser(object):
    """Functor for a given base. Will efficiently convert
    strings to natural numbers."""
    ALPHABET = {
        62: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        95: (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             '[\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
    }

    def __init__(self, base):
        self.base = base
        
        #Error not possible, use 36 by defaut
        if base == 0 :
            base = 36
        
        # If base can be handled by int() builtin, let it do it for us
        if 2 <= base <= 36:
            self.unbase = lambda string: int(string, base)
        else:
            if base < 62:
                self.ALPHABET[base] = self.ALPHABET[62][0:base]
            elif 62 < base < 95:
                self.ALPHABET[base] = self.ALPHABET[95][0:base]
            # Build conversion dictionary cache
            try:
                self.dictionary = dict((cipher, index) for index, cipher in enumerate(self.ALPHABET[base]))
            except KeyError:
                raise TypeError('Unsupported base encoding.')

            self.unbase = self._dictunbaser

    def __call__(self, string):
        return self.unbase(string)

    def _dictunbaser(self, string):
        """Decodes a  value to an integer."""
        ret = 0
        
        for index, cipher in enumerate(string[::-1]):
            ret += (self.base ** index) * self.dictionary[cipher]
        return ret

def tr_buyuk(metin):
    metin = metin.replace('ç','C').replace('i','I').replace('ı','I').replace('ğ','G').replace('ö','O').replace('ş','S').replace('ü','U').replace('İ','I')
    metin = metin.upper()
    return metin
			
class urlKap(object):
    """
        urlKap(url).result
        urlKap(url, output = 'geturl').result
        urlKap(url, output = 'cookie').result
        urlKap(url, timeout='30').result
        post = {'hash':media_id}
        urlKap(url, post = post).result
        url = 'http://www.diziizleyin.net/index.php?x=isyan'
        postfields = {'pid' : 'p2x29464a434'}
        txheaders = {'X-Requested-With':'XMLHttpRequest'}
        urlKap(url, postfields, headers, loc)
    """

    def __init__(self, url, close = True, proxy = None, post = None, mobile = False, referer = None, cookie = None, output = '', timeout = '10'):
        if not proxy == None:
            proxy_handler = urllib2.ProxyHandler({'http': '%s' % proxy})
            opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or output == 'kukili' or not close == True:
            import cookielib
            cookie_handler = urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar())
            opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
            opener = urllib2.install_opener(opener)
        if not post == None:
            import urllib
            post = urllib.urlencode(post)
            request = urllib2.Request(url, post)
        else:
            request = urllib2.Request(url, None)
        if mobile == True:
            request.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7')
        else:
            request.add_header('User-Agent', UA)
        if not referer == None:
            request.add_header('Referer', referer)
        if not cookie == None:
            request.add_header('cookie', cookie)
        response = urllib2.urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = str(response.headers.get('Set-Cookie'))
        elif output == 'kukili':
            result = response.read() + 'kuki :' + str(response.headers.get('Set-Cookie'))
        elif output == 'geturl':
            result = response.geturl()
        elif output == 'lenght':
            result = str(response.headers.get('Content-Length'))
        else:
            result = response.read()
        if close == True:
            response.close()
        self.result = result

########## downloadpage ##########
	
def downloadpage(url):
    if '720pizle' in url:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
            'Accept': '*/*',
            'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest'}
        req = urllib2.Request(url, None, headers)
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        return html
    elif REQUST == 1:
        oRequestHandler = cRequestHandler(url)
        html = oRequestHandler.request()
        return html
    else:
        html = urlKap(url).result
        return html
    
########## downloadpage ##########

            
#chan_tulpe = (chan_counter,
#1 = name
#2 = imdb + description
#3 = piconname
#4 = stream_url
#5 = playlist_url
#6 = category_id
#7 = img
#8 = ...
#9 = protected
#10 = ts_stream )
	
class modules():

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
		
    def get_categories(self, url, pattern, sonraki=None):
        o = urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        img = None
        try:
            page = downloadpage(url)
            video_list_temp = []
            chan_counter = 1
            new = (chan_counter, '** EN SON EKLENENLER **', None, None, None, 'TRModules@' + domain + '@category@** EN SON EKLENENLER **', None, None, None, None, None)
            video_list_temp.append(new)
            cat_regex = re.finditer(pattern, page)
            for text in cat_regex:
                if "(?P<title>" in pattern :  
                    title = tr_buyuk(text.group('title'))
                if "(?P<url>" in pattern :  
                    url = text.group('url')
                    if url.startswith("/"):
                        url = domain + url
                if "(?P<img>" in pattern :  
                    img = text.group('img')
                    if img.startswith("/"):
                        img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url, 'TRModules@' + url + '@category@' + title, None, img, None, None, None)
                video_list_temp.append(chan_tulpe)
            self.prev_page_url = ''
            self.prev_page_text = ''
            try:
                s_sayfa = re.findall(sonraki, page)
                next = s_sayfa[0]
                if next.startswith("/"):
                    next = domain + next
                if len(next):
                    self.next_page_url = 'TRModules@' + next + '@start@'
                    self.next_page_text = 'SONRAKI'
            except:
                self.next_page_url = ''
                self.next_page_text = ''
            if len(video_list_temp) < 1:
                print 'ERROR CAT LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_categories'

    def get_films(self, url, pattern_1, pattern_2, sonraki=None):
        o = urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        try:        
            img = None
            subj = ""
            imdb = ""
            secton = "film"
            if "fullhdfilmizlesene" in url or "koreanturk" in url or "dizigold" in url or "dizimag" in url:  
                secton = "parts"
            if url =="https://dizimag.cc/":
                page = ""
                for a in range(1, 5):
                    import urllib
                    data = urllib.urlencode({"a": a, "t":"_noads"})
                    host = "https://dizimag.cc/service/yenie"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "*/*",
                        "Referer": url,
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-Requested-With": "XMLHttpRequest"}
                    req = urllib2.Request(host, data , headers)
                    response = urllib2.urlopen(req)
                    s = response.read()
                    response.close()
                    page = page+s
            else:
                page = downloadpage(url)
            video_list_temp = []
            chan_counter = 0
            if pattern_2=='' or re.search(pattern_1, page):    
                pattern = pattern_1
            else:
                pattern = pattern_2
            films_regex = re.finditer(pattern, page) # finditer
            for text in films_regex:
                if "(?P<title>" in pattern :  
                    title = tr_buyuk(text.group('title').replace('/',' ').replace('izle','').replace('dizi','').replace('-',' '))
                if "(?P<subj>" in pattern :  
                    subj = text.group('subj')
                if "(?P<imdb>" in pattern :  
                    imdb = 'IMDB: ' + text.group('imdb')
                if "(?P<url>" in pattern :  
                    url = text.group('url')
                    if url.startswith("/"):
                        url = domain + url
                if "(?P<img>" in pattern :  
                    img = text.group('img')
                    if img.startswith("/"):
                        img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, imdb+' - '+subj, None, None, 'TRModules@' + url + '@'+secton+'@' + title, None,  img, '',  None,  None)
                video_list_temp.append(chan_tulpe)
            try:        
                s_sayfa = re.findall(sonraki, page)
                next = s_sayfa[0]
                if next.startswith("/"):
                    next = domain + next
                if len(next):
                    self.next_page_url = 'TRModules@' + next + '@category@' + self.playlist_cat_name
                    self.next_page_text = 'SONRAKI'
            except:
                pass
            self.prev_page_url = 'TRModules@' + domain + '@start@KATEGORILER'
            self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_films'
            
    def get_sezon(self, url, pattern):
        o = urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        try:        
            img = None
            subj = ""
            imdb = ""
            page = downloadpage(url)
            video_list_temp = []
            chan_counter = 0
            films_regex = re.finditer(pattern, page) # finditer
            for text in films_regex:
                if "(?P<title>" in pattern :  
                    title = tr_buyuk(text.group('title'))
                if "(?P<subj>" in pattern :  
                    subj = text.group('subj')
                if "(?P<imdb>" in pattern :  
                    imdb = 'IMDB: ' + text.group('imdb')
                if "(?P<url>" in pattern :  
                    url = text.group('url')
                    if url.startswith("/"):
                        url = domain + url
                if "(?P<img>" in pattern :  
                    img = text.group('img')
                    if img.startswith("/"):
                        img = domain + img
                chan_counter += 1
                chan_tulpe = (chan_counter, title, imdb+' - '+subj, None, None, 'TRModules@' + url + '@category@' + title, None,  img, '',  None,  None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_sezon'
            
    def get_stlkr(self, url):
        try:        
            portal_url, mac = re.findall('stlkr::url=(.*?)::mac=(.*?)$', url, re.IGNORECASE)[0]
            stlkr='==QPjFWbmYHdp1TZwlHdmsmbpx2XlRXYlJ3Y942bpR3Yh9DcoBnLkF2bs9iclZnclN3L'
            headers = {"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                "X-User-Agent": "Model: MAG250; Link: WiFi",
                "Authorization": "Bearer ",
                "Cookie": "PHPSESSID=null; sn=""; mac="+mac+"; stb_lang=en; timezone=Europe/Vilnius"}
            url2 = portal_url + base64.b64decode(stlkr[::-1]) + mac
            req = urllib2.Request(url2,None,headers)
            response = urllib2.urlopen(req)
            html = response.read()
            response.close()
            html = html.replace('\\','')
            tkn = re.findall (r'(https?://.*?/)(.*?)/(.*?)/', html, re.IGNORECASE)[0]
            url = tkn[0] + 'get.php?username='+tkn[1]+'&password='+tkn[2]+'&type=m3u'
            title = self.playlistname
            video_list_temp = [('1', 'LISTEYI AL : E2', None, None, None, 'TURKvodModul@'+ url +'@m3u@TURKvod', None, None, None, None, None), ('2', 'LISTEYI AL : KODI', None, None, None, url, None, None, None, None, None)]
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
            
    def get_stl_kr(self, portal_url, mac, token, random):
        try:
            import urllib
            url = portal_url + '/server/load.php'
            data = urllib.urlencode({"type":"stb", "action":"get_profile","auth_second_step":"1","metrics":'{"mac":mac,"random":random}',"hw_version_2":"1"})
            headers = { "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                        "X-User-Agent": "Model: MAG250; Link: WiFi",
                        "Authorization": "Bearer "+token,
                        "Cookie": "mac="+urllib.quote(mac)+"; stb_lang=en; timezone=Asia%2FShanghai;"}
            req = urllib2.Request(url, data ,headers)
            response = urllib2.urlopen(req)
            page = response.read()
            response.close()
            try:
                login, password = re.findall('"login":"([^"]+)","password":"([^"]+)"', page)[0]
            except:
                login = ""
                password = ""
            video_list_temp = []
            chan_counter = 0
            data = urllib.urlencode({"type":"itv","action":"get_genres","login":login,"password":password})
            req = urllib2.Request(url, data ,headers)
            response = urllib2.urlopen(req)
            page = response.read().replace('\\','')
            response.close()
            data = urllib.urlencode({"type":"vod","action":"get_categories","login":login,"password":password})
            req = urllib2.Request(url, data ,headers)
            response = urllib2.urlopen(req)
            page2 = response.read().replace('\\','')
            response.close()
            cat_regex = re.findall('"id":"(\d+)","title":"([^"]+)"', page)
            for text in cat_regex:
                title = tr_buyuk(text[1])
                url = "stlkr::tv::portal_url="+portal_url+"::mac="+mac+"::cat="+text[0]+"::pg=1"
                chan_counter += 1
                chan_tulpe = (chan_counter, 'TV : '+title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            cat_regex = re.findall('"id":"(\d+)","title":"([^"]+)"', page2)
            for text in cat_regex:
                title = tr_buyuk(text[1])
                url = "stlkr::vod::portal_url="+portal_url+"::mac="+mac+"::cat="+text[0]+"::pg=1"
                chan_counter += 1
                chan_tulpe = (chan_counter, 'VOD : '+title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            self.next_page_url = ''
            self.next_page_text = ''
            self.prev_page_url = ''
            self.prev_page_text = ''
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
            
    def get_stl_kr_link(self, url):
        try:
            import urllib
            portal_url, mac, cat, pg = re.findall('portal_url=(.*?)::mac=(.*?)::cat=(.*?)::pg=(.*?)$', url)[0]
            url1 = portal_url + '/server/load.php?type=stb&action=handshake&prehash=0&token='
            headers = { "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                        "X-User-Agent": "Model: MAG250; Link: WiFi",
                        "Authorization": "Bearer ",
                        "Referer": portal_url,
                        "Cookie": "mac="+urllib.quote(mac)+"; stb_lang=en; timezone=Asia%2FShanghai;"}
            req = urllib2.Request(url1, None ,headers)
            response = urllib2.urlopen(req)
            page = response.read()
            response.close()
            if '"random"' not in page:
                token = re.findall('"token":"([^"]+)"', page)[0]
                random = ""
            if '"random"' in page:
                token, random = re.findall('"token":"([^"]+)","random":"([^"]+)"', page)[0]
            data = urllib.urlencode({"type":"stb", "action":"get_profile","auth_second_step":"1","metrics":'{"mac":mac,"random":random}',"hw_version_2":"1"})
            headers = { "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                        "X-User-Agent": "Model: MAG250; Link: WiFi",
                        "Authorization": "Bearer "+token,
                        "Cookie": "mac="+urllib.quote(mac)+"; stb_lang=en; timezone=Asia%2FShanghai;"}
            url2 = portal_url + '/server/load.php'
            req = urllib2.Request(url2, data ,headers)
            response = urllib2.urlopen(req)
            page = response.read()
            response.close()
            try:
                login, password = re.findall('"login":"([^"]+)","password":"([^"]+)"', page)[0]
            except:
                login = ""
                password = ""
            headers = { "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                        "X-User-Agent": "Model: MAG250; Link: WiFi",
                        "Authorization": "Bearer "+token,
                        "Cookie": "mac="+urllib.quote(mac)+"; stb_lang=en; timezone=Asia%2FShanghai;"}
            if '::tv::' in url:
                page=""
                for a in range(1, 100):
                    data = urllib.urlencode({"type":"itv","action":"get_ordered_list","genre":cat, "p": a, "login":login,"password":password})
                    req = urllib2.Request(url2, data ,headers)
                    response = urllib2.urlopen(req)
                    sayfa = response.read().replace('\\','')
                    response.close()
                    page = page+sayfa.replace('\\','')
                    if '"id"' not in sayfa:
                        break
            if '::vod::' in url:
                data = urllib.urlencode({'type':'vod','action':'get_ordered_list','category':cat, 'sortby' : 'added', 'p' : pg, 'not_ended' : '0', "login":login,"password":password})
                req = urllib2.Request(url2, data ,headers)
                response = urllib2.urlopen(req)
                page = response.read().replace('\\','')
                response.close()
            video_list_temp = []
            chan_counter = 0
            if '::tv::' in url:
                tur = "itv"
                cat_regex = re.findall('"name":"([^"]+)".*?"tv_genre_id":"'+cat+'".*?"url":"([^"]+)"', page)
            if '::vod::' in url:
                cat_regex = re.findall('"name":"([^"]+)".*?"cmd":"([^"]+)"', page)
                tur = "vod"
            for text in cat_regex:
                title = tr_buyuk(text[0])
                cmd = text[1].replace('localhost','lclhst')
                url3 = "stlkr::portal_url="+portal_url+"::mac="+mac+"::name="+text[0]+"::cmd="+cmd+"::tur="+tur
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url3, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if '::vod::' in url:
                pg = int(pg)
                pg += 1
                pg = str(pg)
                url4 = "stlkr::vod::portal_url="+portal_url+"::mac="+mac+"::cat="+cat+"::pg="+pg
                chan_counter += 1
                chan_tulpe = (chan_counter, "Sonraki sayfa  >>", None, None, None,'TRModules@' + url4 + '@parts@' + "Sonraki", None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
            
    def get_parts(self, url, ilk_pattern, parts_pattern):
        o = urlparse(url)
        domain = o.scheme+"://"+o.hostname+"/"
        try:
            page = downloadpage(url)
            video_list_temp = []
            chan_counter = 1	
            if ilk_pattern !='':
                ilk_parca = re.findall(ilk_pattern, page)
                title = tr_buyuk(ilk_parca[0])
                ilk = (chan_counter, title, None,  None, None,  'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(ilk)
            parts_regex = re.finditer(parts_pattern, page)
            for text in parts_regex:
                if "(?P<title>" in parts_pattern :  
                    title = text.group('title').upper()
                if "(?P<url>" in parts_pattern :  
                    url = text.group('url')
                    if url.startswith("/"):
                        url = domain + url
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, None, 'TRModules@' + url + '@parts@' + title, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_parts'
				
    def get_videos(self, url, pattern):
        try:
            page = downloadpage(url)
            video_list_temp = []
            chan_counter = 0
            vid_link = re.finditer(pattern, page)
            for text in vid_link:
                title = self.playlistname
                if "(?P<title>" in pattern :  
                    title = text.group('title').upper()
                if "(?P<url>" in pattern :  
                    url = text.group('url')
                chan_counter += 1
                chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
                
    def get_videos_base_u(self, url, pattern_1, pattern_2):
        try:
            page = downloadpage(url)
            video_list_temp = []
            chan_counter = 0
            video_page = re.findall(pattern_1, page)
            video_link = re.findall(pattern_2, video_page[0])
            link = decode_base64(video_link[0])
            if 'youtube' in link:
                url = re.findall('["\'](https://www.youtube.com/embed/.*?)["\']', link, re.IGNORECASE)[0]
                title = 'YOUTUBE FRAGMAN'
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif 'rapidrame' in link:
                link = re.findall('(https://rapidrame.com/embed.*?)["\']', link, re.IGNORECASE)[0]
                title = 'RAPIDRAME'
                url = link+'::ref::'+url
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            elif 'p4p.php' in link:
                url = 'cdnstreamcdn::' + re.findall('src=["\'](.*?)["\']', link, re.IGNORECASE)[0]
                title = 'HDF PLAYER'
                video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            else:
                uri, key = re.findall('(https://.*?/).*?(?:key|id)=(.*?)"', link, re.IGNORECASE)[0]
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                            'Connection': 'keep-alive',
                            'Referer': url,
                            'X-Requested-With': 'XMLHttpRequest'}
                data = ""
                url2 = uri + 'initPlayer/' + key
                req = urllib2.Request(url2, data , headers)
                response = urllib2.urlopen(req)
                html = response.read()
                availablePlayers = re.findall('"availablePlayers":\[(.*?)\]', html, re.IGNORECASE)[0]
                vid_link = re.findall('"(.*?)"', availablePlayers)
                for text in vid_link:
                    chan_counter += 1			
                    url = 'VanLongStream::'+uri + 'getDataPlayer/'+text+'/'+key
                    title = text.upper()
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
		
    def get_videos_parse_fullhdfilmizlesene(self, url):
        try:
            page = downloadpage(url)
            video_list_temp = []
            chan_counter = 0
            vid_link = re.findall('"vidid":"([^"]+)","name":"([^"]+)","nameTxt":"([^"]+)".*?"tx":(\d),', page)
            for text in vid_link:
                vidid = text[0]
                name = text[1]
                nameTxt = text[2].upper()
                if text[3]=='2':
                    chan_counter += 1			
                    chan_tulpe = (chan_counter, nameTxt+' - TR', None, None, 'fullhdfilmizlesene_parse:https://www.fullhdfilmizlesene.com/player/api.php?id='+vidid+'&type=t&name='+name+'&get=video&pno=tr&format=json&ssl=true', None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
                    chan_counter += 1			
                    chan_tulpe = (chan_counter, nameTxt+' - ENG', None, None, 'fullhdfilmizlesene_parse:https://www.fullhdfilmizlesene.com/player/api.php?id='+vidid+'&type=t&name='+name+'&get=video&pno=en&format=json&ssl=true', None, None, None, None, None, None)					
                    video_list_temp.append(chan_tulpe)
                else:
                    chan_counter += 1			
                    chan_tulpe = (chan_counter, nameTxt, None, None, 'fullhdfilmizlesene_parse:https://www.fullhdfilmizlesene.com/player/api.php?id='+vidid+'&type=t&name='+name+'&get=video&format=json&ssl=true', None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
        
    def get_videos_decodedlink(self, url):
        try:
            url = 'decodedlink:' + url
            title = self.playlistname
            video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'

    def get_videos_posted(self, url, pattern):
        ref = url
        try:
            page = downloadpage(url)
            video_list_temp = []
            chan_counter = 0
            if re.search('youtube.com/embed', page):
                url = re.findall('["\'](https://www.youtube.com/embed/.*?)["\'\?]', page, re.IGNORECASE)[0]
                title = 'YOUTUBE FRAGMAN'
                you = ('1', title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(you)
            if re.search('\?player=', page):
                vid_link = re.findall(pattern, page)
                for text in vid_link:
                    chan_counter += 1			
                    host = text[0]
                    player = text[1]
                    url = 'posted720plink:host:'+host+':params:player='+player+':ref:'+ref
                    title = text[1].upper()
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
            
    def get_parts_dizigold(self, url):
        ref = url
        try:
            import urllib
            page = downloadpage(url)            
            video_list_temp = []
            chan_counter = 0
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
            host, id, dil, sezon_id = re.findall('var url = "([^"]+)";\s+var view_id="([^"]+)";\s+var dil="([^"]+)"[\s\S]*?var sezon_id="([^"]+)"', page, re.IGNORECASE)[0]
            data = urllib.urlencode({"id": id, "dil": dil, "sezon_id": sezon_id, "tip": "view"})
            req = urllib2.Request(host, data, headers)
            response = urllib2.urlopen(req)
            html = response.read() 
            response.close()
            html = html.replace('\\','').replace('u0130','I')
            video_list_temp = []
            chan_counter = 0
            vid_link = re.findall('{"trigger":(\d+),"lang":"([^"]+)".*?ame":"([^"]+)"}', html)
            for text in vid_link:
                chan_counter += 1			
                url = "https://player.dizigold1.net/?id="+id+"&s="+text[0]+"&dil="+text[1]+"&ref="+text[2].lower().replace(" ","-")
                title = text[2]
                chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'
            
    def get_dizibox_videos(self, url):
        try:
            page = downloadpage(url)
            if re.search('(https://\S+stream/embed/[^"]+)"', page):
                url = re.findall('(https://\S+stream/embed/[^"]+)"', page)[0]
                html = downloadpage(url)
                url = re.findall('(http\S+m3u8)', html)[0]
            if re.search('https://www.dizibox.pw/player/', page):
                host = re.findall('(https://www.dizibox.pw/player/[^"]+)"', page)
                link = host[0]
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "Referer": url}
                req = urllib2.Request(link, None, headers)
                response = urllib2.urlopen(req)
                html = response.read() 
                response.close()
                if re.search('atob\(unescape\("([^"]+)"', html):
                    txx = re.findall('atob\(unescape\("([^"]+)"', html)
                    hex = decode_base64(urllib.unquote(txx[0]))
                    moly = re.findall('(https://vidmoly\S+/embed[^"]+)"', hex)
                    url = moly[0]
                if re.search('<iframe src="([^"]+)"', html):
                    txx = re.findall('<iframe src="([^"]+)"', html)
                    url = txx[0]
                if re.search('file"?: ?"[^"]+"', html):
                    txx = re.findall('file"?: ?"([^"]+)"', html)
                    url = txx[0]
                    if 'indifiles' in url:
                        url = txx[0] + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0&Referer=' + link
            title = self.playlistname
            video_list_temp = [('1', title, None, None, url, None, None, None, None, None, None)]
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'

    def get_dizimag_videos(self, url):
        try:
            import urllib
            page = downloadpage(url)
            link = re.findall('(https://dizimag.cc/videoapi/[^"]+)', page)[0]
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "Referer": url}
            req = urllib2.Request(link, None, headers)
            response = urllib2.urlopen(req)
            html = response.read() 
            response.close()
            id_links = re.findall('"part_id":"(\d+)"', html)
            video_list_temp = []
            chan_counter = 0
            for id in id_links:
                chan_counter += 1			
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "*/*",
                    "Referer": link,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-Requested-With": "XMLHttpRequest"}
                host = 'https://dizimag.cc/videoapipost'
                data = urllib.urlencode({"id": id})
                req = urllib2.Request(host, data, headers)
                response = urllib2.urlopen(req)
                html2 = response.read() 
                response.close()
                html2 = html2.replace('\\','')
                if re.search('"iframe":"(http[^"]+)"', html2):
                    link2 = re.findall('"iframe":"(http[^"]+)"', html2)[0]
                    url = link2
                    title = "LINK " + str(chan_counter)
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'

    def get_dizilab_videos(self, url):
        try:
            import urllib
            page = downloadpage(url)
            id_links = re.findall("loadVideo\('([^']+)'", page)
            video_list_temp = []
            chan_counter = 0
            for vid in id_links:
                chan_counter += 1			
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "*/*",
                    "Referer": url,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-Requested-With": "XMLHttpRequest"}
                host = 'https://dizilab.pw/request/php/'
                data = urllib.urlencode({"vid": vid, "tip": "0", "type": "loadVideo"})
                req = urllib2.Request(host, data, headers)
                response = urllib2.urlopen(req)
                html2 = response.read()
                response.close()
                html2 = html2.replace('\\','')
                if re.search('sources', html2):
                    link2, kalite = re.findall('file":"([^"]+)","label":"([^"]+)"', html2, re.IGNORECASE)[0]
                    url = link2 + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
                    title = kalite
                    chan_tulpe = (chan_counter, title, None, None, url, None, None, None, None, None, None)
                    video_list_temp.append(chan_tulpe)
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
            return video_list_temp
        except:
            print 'ERROR get_videos'

    def get_list(self, url):
        self.reset_buttons()
        video_list_temp = []
        parts = url.split('@')
        url = parts[0]
        section = parts[1]
        name = parts[2]
		
        if url.find("720pizle") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'class="oval">(\s+)?<a href="(?P<url>[^"]+)" title="(?P<title>[^"]+)"'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<div class="film-kategori-resim">(\s+)?<a href="(?P<url>[^"]+)" title="(?P<title>[^"]+)">(\s+)?<img src="(?P<img>[^"]+)"'
                pattern_2 = ''
                sonraki = 'href="(?P<next>[^"]+)"(?: title="|>)Sonraki'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = 'https://www.(youtube).com/embed/'
                parts_pattern = '<a href="(?P<url>(https://720pizle.org)?/izle/(?P<title>[^/]+)/[^"]+)"'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)				
            if section == 'parts':
                self.playlistname = name
                #host = 'https://720p-izle.com/api/dataEmbed3.asp'
                #pattern = 'data-id="([^"]+)">([^<]+)<b class="alternatifrip"'
                pattern = '<a href="(https://720pizle.org/izle[^\?]+)\?player=([^"]+)" class="text-small"'
                self.video_liste = self.get_videos_posted(url, pattern)
            return self.video_liste

        if url.find("dizibox") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'href="(?P<url>https?://www.dizibox.pw/diziler/[^"]+)"(?:|[^<]+)><[^<]+></i>(?P<title>[^<]+)</a>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                if '/diziler/' in url :
                    pattern = "<a href='(?P<url>[^']+)' class='btn btn-s btn-default-light '>(?P<title>[^<]+)</a>"
                pattern_1 = "<article class=\"article-episode-card pull-left grid-five[\s\S]*?href=\"(?P<url>https?://www.dizibox.pw/[^\"]+)\" class='figure-link' title=\"\">\s+<img src='(?P<img>[^']+)' alt='(?P<title>[^']+)'"
                pattern_2 = 'href="(?P<url>https?://www.dizibox.pw/(?P<title>.*?)/)" class="season-episode'
                sonraki = "href=[\"'](?P<next>[^\"']+)[\"'] class=[\"']next[\"']>"
                if '/diziler/' in url :
                    self.video_liste = self.get_sezon(url, pattern) + self.get_films(url, pattern_1, pattern_2, sonraki)
                else:
                    self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = "selected='selected'>([^<]+)<"
                parts_pattern = "<option value='(?P<url>[^<']*)'>(?P<title>[^<]+)</option>"
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_dizibox_videos(url)
            return self.video_liste

        if url.find("dizilab") > -1:
            if section == 'start':
                if url == "https://dizilab.pw/":
                    url = "https://dizilab.pw/arsiv?tur=&orderby=ad&yil=&ulke=&order=ASC"
                self.playlistname = name
                sonraki = 'class="active"><a href="[^"]+">\d+</a></li><li class=""><a href="([^"]+)"'
                pattern = 'class="tv-series-single">\s+<a href="(?P<url>[^"]+)" class="film-image">\s+<img src="[^"]+" alt="(?P<title>[^"]+)"'
                self.video_liste = self.get_categories(url, pattern, sonraki)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<li id="\d+" class="[^"]+">\s+(<span[^>]+></span>\s+)?<a href="(?P<url>https://dizilab.pw/(?P<title>[^"]+))">\s+<img width="\d+" height="\d+" src="(?P<img>[^"]+)"'
                pattern_2 = '(?:<a class="episode" |<div class="tv-series-single">\s+)href="(?P<url>https://dizilab.pw/(?P<title>[^"]+))"'
                self.video_liste = self.get_films(url, pattern_1, pattern_2)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = 'class="active">\s+<a href="[^"]+">\s+<span class="[^"]+"></span>\s+([^<]+)</a>'
                parts_pattern = 'class="">\s+<a href="(?P<url>[^"]+)">\s+<span class="[^"]+"></span>\s+(?P<title>[^<]+)</a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_dizilab_videos(url)
            return self.video_liste

        if url.find("dizimag") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = '<a href="(?P<url>.*?)" title="(?P<title>.*?)" class="'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<td valign=top><a href=(?P<url>https?://dizimag.cc/(?P<title>.*?))\s+style[\s\S]*?<img src=(?P<img>.*?(jpg|png))'
                pattern_2 = 'href="(?P<url>[^"]+)" style="[^"]+">(?P<title>[^<]+)<span class="gizle">'
                self.video_liste = self.get_films(url, pattern_1, pattern_2)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_dizimag_videos(url)
            return self.video_liste

        if url.find("dizigold") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = '<a href="(?P<url>[^"]+)">(?P<title>[^<]+)<div class="oyside"'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<li id="konuid_\d+">\s+<a href="(?P<url>/(?P<title>[^"]+))">\s+<img class="resk" src="(?P<img>[^"]+)"'
                pattern_2 = '<a href="(?P<url>https?://[^/]+/(?P<title>[^"]+))" class="realcuf"'
                sonraki = 'href="([^"]+)">Sonraki'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_parts_dizigold(url)
            return self.video_liste
            
        if url.find("filmakinesi") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'menu-item-\d+"><a href="?(?P<url>[^>"]+)"?>(?P<title>[^<]+)</a>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = 'class="post-[^>]+>\s+<a href="?(?P<url>.*?html).*?rel="?bookmark"? title="(?P<title>[^"]+)">[\s\S]*?data-src="?(?P<img>.*?jpg)[\s\S]*?class="?puan_1"?>(?P<imdb>[^<]+)<'
                pattern_2 = ''
                sonraki = 'href="?(?P<next>\S+)(?:" | )rel="?next'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = '<span>(?P<title>[^<]*)</span> <a'
                parts_pattern = '<a href="?(?P<url>\S+)(?:"| class="?post-page-numbers"?)><span>(?P<title>[^<]+)</span></a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':
                self.playlistname = name            
                pattern = "<p><iframe.*?src=(?P<url>[-=?:/.0-9a-zA-Z]+)"
                self.video_liste = self.get_videos(url, pattern)
            return self.video_liste        
        if url.find("fullhdfilmizlesene") > -1:
            if section == 'start':                           
                self.playlistname = name
                pattern = '<li><a href="(?P<url>https://www.fullhdfilmizlesene.com/(?:filmizle|yil)[^"]+)"[^>]+>(?P<title>[^<]+)</a></li>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<li>(?:|\s+)<img (?:|src="[^"]+" data-)src="(?P<img>[^"]+)" alt="(?P<title>[^"]+)" width="[^"]+" height="[^"]+" class="afis[\s\S]*?<a href="(?P<url>[^"]+)"[\s\S]*?<span>IMDB(?P<imdb>[^<]+)</span>'
                pattern_2 = ''
                sonraki = "class='ileri'><a href='(?P<next>[^']+)"
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'parts':
                self.playlistname = name
                self.video_liste = self.get_videos_parse_fullhdfilmizlesene(url)
            return self.video_liste
        
        if url.find("hdfilmcehennemi") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = '<li id="menu-item-\d+" class="menu-item [^>]+>(?:|\s+)<a href="(?P<url>(?:|https?://[^/]+)/(?:dil|tur|yil)/[^"]+)">(?P<title>[^<]+)</a>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = 'class="col-xs-6 col-sm-4 poster-container">(?:|\s+)<div class="poster poster-pop" data-original-title="(?P<title>[^"]+)"[\s\S]*?data-content="<p>(?P<subj>[\s\S]*?)</p>[\s\S]*?href="(?P<url>[^"]+)">[\s\S]*?(?P<img>http[^"]+)"[\s\S]*?<span>IMDb</span>(?P<imdb>\S+)'
                pattern_2 = ''
                sonraki = 'rel="next" href="(?P<next>[^"]+)"'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = '<li class="selected"><a href="[^"]+"><span class="text">(?P<title>[^<]+)</span>'
                parts_pattern = '<li><a href="(?P<url>[^"]+)"><span class="text">(?P<title>[^<]+)</span></a></li>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)
            if section == 'parts':
                self.playlistname = name
                video_pattern_1 = '<div class="player-container"([\s\S]*?)<div class="facebook-like">'
                video_pattern_2 = "<div id=\"player\"[\s\S]*?<script>[\s\S]*?'([^']+)'"
                self.video_liste = self.get_videos_base_u(url, video_pattern_1, video_pattern_2)
            return self.video_liste
            
        if url.find("stlkr::") > -1:
            if section == 'start':
                portal_url, mac = re.findall('stlkr::url=(.*?)::mac=(.*?)$', url, re.IGNORECASE)[0]
                url1 = portal_url + '/server/load.php?type=stb&action=handshake&prehash=0&token='
                headers = { "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                        "X-User-Agent": "Model: MAG250; Link: WiFi",
                        "Authorization": "Bearer ",
                        "Referer": portal_url,
                        "Cookie": "mac="+urllib.quote(mac)+"; stb_lang=en; timezone=Asia%2FShanghai;"}
                req = urllib2.Request(url1, None ,headers)
                response = urllib2.urlopen(req)
                page = response.read()
                response.close()
                #if '"random"' not in page:
                #    self.playlistname = name
                #    self.video_liste = self.get_stlkr(url)
                if '"random"' not in page:
                    token = re.findall('"token":"([^"]+)"', page)[0]
                    random = ""
                    self.playlistname = name
                    self.video_liste = self.get_stl_kr(portal_url, mac, token, random)
                if '"random"' in page:
                    token, random = re.findall('"token":"([^"]+)","random":"([^"]+)"', page)[0]
                    self.playlistname = name
                    self.video_liste = self.get_stl_kr(portal_url, mac, token, random)
            if section == 'parts':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                self.video_liste = self.get_stl_kr_link(url)
            return self.video_liste
			        
        if url.find("filmizlesene") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'class="cat-item cat-item-\d+"><a href="(?P<url>[^"]+)"(?:|[^>]+)>(?P<title>[^<]+)</a>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = '<div class="ykutu2">\s+<a href="(?P<url>[^"]+)"[\s\S]*?<span>(?P<title>[^"]+)</span>[\s\S]*?"(?P<img>http[^"]+jpg)"'
                pattern_2 = 'class="mkutu2">\s+<a href="(?P<url>[^"]+)" title="(?P<title>[^"]+)">[\s\S]*?<img src="(?P<img>[^"]+)"'
                sonraki = "rel=[\"']next[\"'] href=[\"']([^\"']+)[\"']"
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = ''
                parts_pattern = '<a href="(?P<url>https://[^/]+/[^/]+/\d+)">(?P<title>(?:Moly|MRu)[^<]+)</a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)			
            if section == 'parts':
                self.playlistname = name
                pattern = "(?P<url>(?:https://vidmoly|https://my.mail.ru)[^'\"]+)['\"]"
                self.video_liste = self.get_videos(url, pattern)
            return self.video_liste
                    
        if url.find("jetfilmizle") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'menu-item-\d+"><a title="[^"]+" href="(?P<url>[^"]+)">(?P<title>[^<]+)</a></li>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = 'class="movie[^>]+>\s+<a href="(?P<url>[^"]+)" rel="bookmark" title="(?P<title>[^"]+)">\s+<img.*?src="(?P<img>[^"]+jpg)"'
                pattern_2 = ''
                sonraki = 'rel="next" href="(?P<next>[^"]+)"'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'film':
                self.playlistname = name
                ilk_pattern = 'class="film_part">\s+<span>(?P<title>[^<]+)</span>'
                parts_pattern = '<a href="(?P<url>[^<]+)" class="post-page-numbers"><span>(?P<title>[^<]+)</span></a>'
                self.video_liste = self.get_parts(url, ilk_pattern, parts_pattern)				
            if section == 'parts':
                self.playlistname = name
                pattern = "<iframe.*?src=[\"'](?P<url>[^\"']+)[\"']"
                self.video_liste = self.get_videos(url, pattern)
            return self.video_liste

        if url.find("koreanturk") > -1:
            if section == 'start':
                self.playlistname = name
                pattern = 'class="cat-item cat-item-\d+"><a href="(?P<url>https?://www.koreanturk.com/[^"]+)"[^>]+>(?P<title>[^<]+)</a>'
                self.video_liste = self.get_categories(url, pattern)
            if section == 'category':
                self.playlist_cat_name = name
                self.playlistname = self.playlist_cat_name
                pattern_1 = 'href="(?P<url>https?://www.koreanturk.com/[^"]+)">\s*<div class="resimcik">\s*<img.*?src="(?P<img>[^"]+)".*?alt="(?P<title>[^"]+)"'
                pattern_2 = ''
                sonraki = 'next"><a href="(?P<next>[^"]+)"'
                self.video_liste = self.get_films(url, pattern_1, pattern_2, sonraki)
            if section == 'parts':
                self.playlistname = name
                pattern = 'id="(?P<title>[^"]+)"><(?:iframe.*?src|a href)="(?P<url>[^"]+)"'
                self.video_liste = self.get_videos(url, pattern)
            return self.video_liste
class parsers:

    def __init__(self):
        self.quality = ''
       

    def get_parsed_link(self, url):
        son_url = ''
        film_quality = []
        video_tulpe = []
        error = None
        try:
            if 'csst.online' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    page = response.read() 
                    response.close()
                    if re.search('file:"\[\d+p\]', page):
                        for match in re.finditer('\[(\d+p)\](http[^,]+),', page):
                            film_quality.append(match.group(1))
                            video_tulpe.append(match.group(2))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
                    
            if 'sandup.co' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    page = response.read() 
                    response.close()
                    if re.search('mp4', page):
                        for match in re.finditer('"label":"([^"]+)","type":"video/mp4","file":"([^"]+)"', page):
                            film_quality.append(match.group(1))
                            video_tulpe.append(match.group(2)+ "#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0&Referer=" + url)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
                   
            if 'u-play' in url:
                try:
                    hash, id = re.findall('/start/(.*?)/(.*?)$', url)[0]
                    link = "https://ustore.bz/getContentJson.php?hash="+hash+"&id="+id
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = urllib2.Request(link, None, headers)
                    response = urllib2.urlopen(req)
                    page = response.read() 
                    response.close()
                    if re.search('mp4', page):
                        for match in re.finditer('"(http[^"]+mp4)"', page):
                            if "480-" in match.group(1) : 
                                kalite = "480p"
                            elif "720-" in match.group(1) : 
                                kalite = "720p"
                            elif "1080-" in match.group(1) : 
                                kalite = "1080p"
                            else:
                                kalite = "360p"
                            film_quality.append(kalite)
                            video_tulpe.append(match.group(1)+ "#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0&Referer=" + url)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'ownerity' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    page = response.read() 
                    response.close()
                    if re.search("vidmoly", page):
                        vidlink = re.findall('(https://vidmoly[^"]+)"', page, re.IGNORECASE)[0]
                        son_url = self.get_parsed_link(vidlink)
                    if re.search('"file":"([^"]+)", ?"label":"([^"]+)"', page):
                        for match in re.finditer('"file":"([^"]+)", ?"label":"([^"]+)"', page):
                            link = match.group(1)
                            if '\\x' in link:
                                link = link.decode('unicode-escape').encode('ASCII')
                            film_quality.append(match.group(2))
                            video_tulpe.append(link)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'stlkr::portal_url' in url:
                try:
                    portal_url, mac, name, cmd, tur = re.findall('portal_url=(.*?)::mac=(.*?)::name=(.*?)::cmd=(.*?)::tur=(.*?)$', url)[0]
                    if tur == "itv":
                        cmd = cmd.replace('lclhst','localhost')
                        cmd = "ffmpeg http:"+re.findall('(//.*?)$', cmd)[0]
                    url1 = portal_url + '/server/load.php?type=stb&action=handshake&prehash=0&token='
                    headers = { "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                        "X-User-Agent": "Model: MAG250; Link: WiFi",
                        "Authorization": "Bearer ",
                        "Referer": portal_url,
                        "Cookie": "mac="+urllib.quote(mac)+"; stb_lang=en; timezone=Asia%2FShanghai;"}
                    req = urllib2.Request(url1, None ,headers)
                    response = urllib2.urlopen(req)
                    page = response.read()
                    response.close()
                    if '"random"' not in page:
                        token = re.findall('"token":"([^"]+)"', page)[0]
                        random = ""
                    if '"random"' in page:
                        token, random = re.findall('"token":"([^"]+)","random":"([^"]+)"', page)[0]
                    url = portal_url + '/server/load.php'
                    data = urllib.urlencode({"type":"stb", "action":"get_profile","auth_second_step":"1","metrics":'{"mac":mac,"random":random}',"hw_version_2":"1"})
                    headers = { "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                                "X-User-Agent": "Model: MAG250; Link: WiFi",
                                "Authorization": "Bearer "+token,
                                "Cookie": "mac="+urllib.quote(mac)+"; stb_lang=en; timezone=Asia%2FShanghai;"}
                    req = urllib2.Request(url, data ,headers)
                    response = urllib2.urlopen(req)
                    page = response.read()
                    response.close()
                    try:
                        login, password = re.findall('"login":"([^"]+)","password":"([^"]+)"', page)[0]
                    except:
                        login = ""
                        password = ""
                    data = urllib.urlencode({"type":tur,"action":"create_link","login":login,"password":password,"cmd":cmd})
                    req = urllib2.Request(url, data ,headers)
                    response = urllib2.urlopen(req)
                    page = response.read().replace('\\','')
                    response.close()
                    if re.search('"cmd":""', page):
                        try: 
                            movie_id = re.findall('/(\d+)\.', cmd)[0]
                            data = urllib.urlencode({"type":tur,"action":"get_ordered_list","login":login,"password":password, 'movie_id':movie_id})
                            req = urllib2.Request(url, data ,headers)
                            response = urllib2.urlopen(req)
                            page = response.read().replace('\\','')
                            response.close()
                        except:
                            pass
                    if re.search('"cmd":""', page):
                        son_url = re.findall('(http.*?)$', cmd)[0] + '#User-Agent=Lavf53.32.100'
                    else:
                        if tur == "itv":
                            son1, son2 = re.findall('"cmd":"(?:|.*?)(http://[^\/]+/[^\/]+/[^\/]+/)(?:|.*?)(\d+\?play_token=[^"]+)"', page)[0]
                            son_url = son1+son2
                        else:
                            son_url = re.findall('"cmd":"(?:|.*?)(http[^"]+)"', page)[0]
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'dizigold' in url:
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "X-Requested-With": "XMLHttpRequest", "Referer": url}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    page = response.read() 
                    response.close()
                    if re.search("<iframe.*?src=", page):
                        vidlink = re.findall('<iframe.*?src="(?://|https?://)([^"]+)"', page, re.IGNORECASE)[0]
                        if 'api.dizigold' in vidlink:
                            vidlink = "http://" + vidlink.replace('/play/gd/','/streaming/file/')
                            son_url = vidlink + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                        else:    
                            vidlink = "http://" + vidlink
                            son_url = self.get_parsed_link(vidlink)
                    if re.search('"file":"([^"]+)", ?"label":"([^"]+)"', page):
                        for match in re.finditer('"file":"([^"]+)", "label":"([^"]+)"', page):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'jetcdn.co' in url or 'api.ocdn' in url and 'postedlink' not in url or 'jetv.xyz' in url or 'yjco.xyz' in url:
                if url.startswith("//"):
                    url = "http:" + url
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': 'https://jetfilmizle.live/',
                        'X-Requested-With': 'XMLHttpRequest'}
                    if 'gp.jetcdn' in url or 'jetv.xyz' in url or 'yjco.xyz' in url:
                        req = urllib2.Request(url, None , headers)
                        response = urllib2.urlopen(req)
                        link = response.read()
                        response.close()
                        for match in re.finditer('"file" ?: ?"([^"]+)","(?:type|label)": ?"([^"]+)"', link):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1))
                    if 'hls.jetcdn' in url:
                        data = ""
                        key = re.findall('(?:key|id)=(.*?)$', url, re.IGNORECASE)[0]
                        url2 = 'https://hls.jetcdn.co/getHost/' + key
                        req = urllib2.Request(url2, data , headers)
                        response = urllib2.urlopen(req)
                        link = response.read()
                        response.close()
                        son_url = decode_base64(link)
                    if 'api.ocdn' in url:
                        if '/fe/' in url:
                            params = ":params:r="+url+"&d=jetcdn.top";
                            ref = ":ref:"+url
                            host = "host:"+url.replace('https://api.ocdn.top/fe/embed-', 'https://jetcdn.top/api/source/').replace('.html','')
                            finalID = "postedlink:"+host+params+ref
                            son_url = self.get_parsed_link(finalID)
                        if '/clo/' in url:
                            key = re.findall('embed-(.*?).html', url, re.IGNORECASE)[0]
                            data = "vars="+ key
                            req = urllib2.Request('https://api.ocdn.top/clo/api.php', data , headers)
                            response = urllib2.urlopen(req)
                            link = response.read()
                            response.close()
                            link2 = re.findall(r'src="(\S+)[\s|\.]', link)[0] + '.html'
                            son_url = self.get_parsed_link(link2)
                        if '/o1/' in url:
                            req = urllib2.Request(url, None , headers)
                            response = urllib2.urlopen(req)
                            link = response.read()
                            response.close()
                            link2 = re.findall(r'src="(\S+)[\s|\.]', link)[0] + '.html'
                            son_url = self.get_parsed_link(link2)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'vipporns' in url:
                def decodevip(video_url, license_code, _size=16):
                    d = video_url.split("/")[1:]
                    h = d[6][:2 * _size]
                    v = evip(license_code, _size)
                    if v and h:
                        t = h
                        u = len(h)-1
                        for u in range(u, -1, -1):
                            ind = u
                            k = u
                            for k in range(k, len(v)):
                               ind += int(v[k])
                            while ind >= len(h):
                               ind -= len(h)
                            a = ""
                            for i in range(len(h)):
                                if i == u:
                                   a += h[ind]
                                elif i == ind:
                                   a += h[u]
                                else:
                                   a += h[i]
                            h = a
                        d[6] = d[6].replace(t, h);
                        d.pop(0);
                        video_url = "/".join(d);
                    return video_url
                def evip(license_code, _size):
                    p = license_code
                    d = p
                    s = ""
                    for i in range(1,len(d)):
                        if d[i]:
                            s += str(d[i])
                        else:
                            s += str(1)
                    p = int(len(s)/2)
                    n = int(s[:p + 1])
                    m = int(s[p:])
                    i = m - n;
                    if i < 0:
                        i = -i
                    s = i
                    i = m - n
                    if i < 0:
                        i = -i;
                    s += i;
                    s *= 2;
                    s = str(s);
                    rate = _size / 2 + 2
                    res = ""
                    for i in range(p+1):
                        for x in range(1,5):
                            num = int(d[i+x]) + int(s[i])
                            if num >= rate:
                                num -= rate
                            res += str(num)
                    return res
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    license_code = re.findall("license_code: ?'([^']+)'", html, re.IGNORECASE)[0]
                    video_url = re.findall("video_url: ?'([^']+)'", html, re.IGNORECASE)[0]
                    son_url =  decodevip(video_url, license_code)+'#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'playvidto' in url:
                try:
                    html = urlKap(url).result
                    packed = re.findall(">(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                    html4 = cPacker().unpack(packed)
                    if re.search('src:"[^"]+".*?label:"\d+"', html4):
                        for match in re.finditer('src:"([^"]+)".*?label:"(\d+)"', html4):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1)+'p')
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'woof.tube' in url:
                try:
                    req = urllib2.Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    vidlink = re.findall('id="videolink">(.*?)</p>', html, re.IGNORECASE)[0]
                    son_url = 'https://woof.tube/gettoken/' + vidlink + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
        
            if 'onlystream' in url or 'uqload' in url or 'videobin' in url or 'fastplay.to' in url:
                try:
                    req = urllib2.Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    if re.search('"([^"]+(mp4|m3u8))"', html):
                        if re.search('"([^"]+(?:mp4|m3u8))".*?label: ?"([^"]+)"', html):
                            for match in re.finditer('"([^"]+(?:mp4|m3u8))".*?label: ?"([^"]+)"', html):
                                film_quality.append(match.group(2))
                                video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=' + url)
                        else:
                            for match in re.finditer('"([^"]+(mp4|m3u8))"', html):
                                 film_quality.append(match.group(2))
                                 video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=' + url)
                    else:
                        packed = re.findall('(eval\(function\(p,a,c,k,e,d.*?\)\)\))', html, re.IGNORECASE)[0]
                        html = cPacker().unpack(packed)
                        for match in re.finditer('file: ?"([^"]+(mp4|m3u8))"', html):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=' + url)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'puhhhhhutv' in url:
                try:
                    host = re.findall('(.*?/hls/)', url, re.IGNORECASE)[0]			
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    for match in re.finditer('((\d+p)\S+)', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(host + match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0&Referer=https://puhutv.com/')
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		  
            if 'fembed.net' in url or 'feurl.com' in url and 'postedlink' not in url:
                try:
                    url = url.replace('/v/','/api/source/')
                    dt = re.findall('(?:www.fembed.net|fembed.net|feurl.com)', url, re.IGNORECASE)[0]
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = "r=&d="+dt
                    req = urllib2.Request(url, data , headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    html = html.replace('\\','')
                    for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		  
            if 'vidmo.cc' in url:
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = ""
                    req = urllib2.Request(url, data , headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    if re.search("getJSON\('/source.php\?h=", html):
                        key = re.findall("getJSON\('/source.php\?h=(.*?)[\"']", html, re.IGNORECASE)[0]
                        url2 = 'https://vidmo.cc/source.php?h=' + key
                        req = urllib2.Request(url2, data , headers)
                        response = urllib2.urlopen(req)
                        html = response.read()
                        html = html.replace('\\','')
                        for match in re.finditer('"label":"([^"]+)","file":"([^"]+)"', html):
                            film_quality.append(match.group(1))
                            video_tulpe.append(match.group(2).replace('https','http'))
                    if re.search("file: '/source.php\?h=", html):
                        key = re.findall("file: '/source.php\?h=(.*?)[\"']", html, re.IGNORECASE)[0]
                        finalID = 'https://vidmo.m3u8/source.php?h=' + key
                        son_url = self.get_parsed_link(finalID)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		  
            if 'fileru' in url:
                try:
                    url = url.replace('https', 'http')
                    headers = {'User-agent': 'Mozilla/5.0 TURKvod-10', 'Connection': 'Close'}
                    req = urllib2.Request(url, None , headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    url2 = re.findall("getJSON\('(.*?)'", html)[0]
                    req = urllib2.Request('http://fileru.net/'+url2, None , headers)
                    response = urllib2.urlopen(req)
                    html2 = response.read()
                    for match in re.finditer('"label":"([^"]+)","file":"([^"]+)"', html2):
                        film_quality.append(match.group(1).replace('\\',''))
                        video_tulpe.append(match.group(2).replace('\\',''))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
                    
            if 'VanLongStream' in url:
                url = url.replace('VanLongStream::','')
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = ""
                    if re.search('fembed', url):
                        req = urllib2.Request(url, data , headers)
                        response = urllib2.urlopen(req)
                        html = response.read()
                        fembed = re.findall('"data":"([^"]+)"', html, re.IGNORECASE)[0]
                        req = urllib2.Request(fembed, None , headers)
                        response = urllib2.urlopen(req)
                        html2 = response.read()
                        fembed = re.findall('https://www.fembed.net/v/([^"\']+)', html2, re.IGNORECASE)[0]
                        link = "https://www.fembed.net/api/source/"+fembed
                        son_url = self.get_parsed_link(link)
                    if re.search('gphoto', url):
                        req = urllib2.Request(url, data , headers)
                        response = urllib2.urlopen(req)
                        html2 = response.read()
                        serverID2 = re.findall('"data":"https://filmizle.hdfilmcehennemi.io/embedplay/(.*?)"', html2, re.IGNORECASE)[0]
                        serverID2 = "https://filmizle.hdfilmcehennemi.io/getLinkStreamMd5/"+serverID2
                        req = urllib2.Request(serverID2, None , headers)
                        response = urllib2.urlopen(req)
                        gphoto = response.read()
                        for match in re.finditer('"?file"?:"([^"]+)","?label"?:"([^"]+)"', gphoto):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1) + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('vidmoly', url):
                        req = urllib2.Request(url, data , headers)
                        response = urllib2.urlopen(req)
                        html3 = response.read()
                        serverID3 = re.findall('"data":"(.*?)"', html3, re.IGNORECASE)[0]
                        req = urllib2.Request(serverID3, None , headers)
                        response = urllib2.urlopen(req)
                        html33 = response.read()
                        finalID = re.findall('(https://vidmoly\S+/embed.*?)["\']', html33, re.IGNORECASE)[0]
                        son_url = self.get_parsed_link(finalID)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True


            if 'cdnstreamcdn' in url:
                url = re.findall('(?:embed/|\?v=)(.*?)$', url, re.IGNORECASE)[0]
                url = 'https://panel.streamcdn.xyz/embed/'+url
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    req = urllib2.Request(url, None , headers)
                    response = urllib2.urlopen(req)
                    html3 = response.read()
                    serverID3 = re.findall('file(?:\s+|"|):(?:\s+|)[\"\'](.*?)[\"\']', html3, re.IGNORECASE)[0]
                    if serverID3.startswith("/"):
                        serverID3 = "http:" + serverID3
                    video_tulpe_tmp = []
                    req = urllib2.Request(serverID3, None , headers)
                    response = urllib2.urlopen(req)
                    page = response.read()
                    if re.search('RESOLUTION=\d+x(\d+)', page):
                        film_quality = re.findall('RESOLUTION=\d+x(\d+).*?AUDIO="audio"', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=.*AUDIO="audio"\\s(.*)', page)
                            if len(video_tulpe_tmp) > 0:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        req = urllib2.Request(tulpe, None , headers)
                                        response = urllib2.urlopen(req)
                                        page = response.read()
                                        keto = re.findall('(http.*?)["\s]', page, re.IGNORECASE)[0]
                                        tulpe = keto + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                                        video_tulpe.append(tulpe.replace('\r', ''))
                        else:
                            son_url = serverID3 + '#Content-type=application/x-mpegURL&Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    else :
                        film_quality = re.findall('height="(\d+)"', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall(' height="\d+">\s+<BaseURL>(.*)</BaseURL>', page)
                            if len(video_tulpe_tmp) > 0:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        keto = tulpe + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                                        video_tulpe.append(keto.replace('\r', ''))
                        else:
                            son_url = serverID3 + '#Content-type=application/x-mpegURL&Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'foreverstream' in url:
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = ""
                    if 'hdfilmcehennemi' in url:
                        key = re.findall('\?id=(.*?)$', url, re.IGNORECASE)[0]
                        url2 = 'https://forever.hdfilmcehennemi1.com/get/' + key
                    else:
                        key = re.findall('/embed/(.*?)$', url, re.IGNORECASE)[0]
                        url2 = 'https://cdn.foreverstream.host/get/' + key
                    req = urllib2.Request(url2, None, headers)
                    response = urllib2.urlopen(req)
                    page = response.read()
                    video_tulpe_tmp = []
                    url_main = ''
                    url_main = '/'.join(url2.split('/')[:-2]) + '/'
                    if re.search('RESOLUTION=\d+x(\d+)', page):
                        film_quality = re.findall('RESOLUTION=\d+x(\d+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('RESOLUTION=.*\\s(.*)', page)
                            if len(video_tulpe_tmp) > 1:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe.replace('\r', ''))
                                else:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(url_main + tulpe.replace('\r', '').replace('/get', 'get')+ '#Referer=' + url)
                            else:
                                film_quality = []
                                son_url = url
                        else:
                            son_url = url
                        
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
                    
            if 'iframetoajax' in url:
                try:
                    link, host, ref = re.findall('((https?://.*?)/.*?):iframetoajax:(.*?)$', url, re.IGNORECASE)[0]
                    link = link.replace('iframe','ajax')
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': '*/*',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
						'Referer': ref}
                    js = host+"/video.js?"+str(int(time.time() * 1000))
                    req = urllib2.Request(js, None, headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    serverID, myip = re.findall("\(window,'(.*?)','(.*?)'", html, re.IGNORECASE)[0]
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': '*/*',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        serverID: myip}
                    req = urllib2.Request(link, None, headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    file, hash = re.findall('"file":"(.*?)","hash":"(.*?)"', html, re.IGNORECASE)[0]
                    son_url = file.replace('\\','') +"?"+hash
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'fullhdfilmizlesene_parse' in url:
                url = re.findall('fullhdfilmizlesene_parse:(.*?)$', url, re.IGNORECASE)[0]
                headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': 'https://www.fullhdfilmizlesene.com/'}
                req = urllib2.Request(url, None, headers)
                response = urllib2.urlopen(req)
                data = response.read()
                response.close()
                data = data.replace('\\','')
                if 'name=fast' in url:
                    try:
                        link = re.findall('src=["\'](.*?)["\']', data)[0]
                        req = urllib2.Request(link, None, headers)
                        response = urllib2.urlopen(req)
                        data2 = response.read()
                        response.close()
                        link2 = re.findall('skin:[\s\S]*?(eval[\s\S]*?}\)\));', data2)[0]
                        gg =  cPacker().unpack(link2)
                        gg = gg.replace("\\'","'").replace('\\\\\\\\','\\\\\\')
                        ff =  cPacker().unpack(gg)
                        cc = ff.replace("\\","").replace("x","")
                        if re.search('"file":".*?","label":.*?"file":".*?","label"', cc):
                            for match in re.finditer('"file":"(.*?)","label":"(.*?)"', html):
                                film_quality.append(match.group(2))
                                link = match.group(1).decode('hex')
                                if link.startswith("//"):
                                    link = "https:" + link
                                video_tulpe.append(link)
                        else:
                            link3 = re.findall('"file":"(.*?)"', cc)[0]
                            son_url = link3.decode('hex')
                    except Exception as e:
                        print 'link alinamadi : ' + str(e)
                        error = True
                else:
                    try:
                        if re.search('src=', data):
                            link = re.findall('src=["\'](.*?)["\']', data)[0]
                            if re.search('php\?id=.*?&', link):
                                link1 = re.findall('php\?id=(.*?)&', link)[0]
                                son_url = self.get_parsed_link('https://ok.ru/videoembed/'+link1)
                            if re.search('(?:oload|openload)', link):
                                link1 = link
                                son_url = self.get_parsed_link(link1)
                            if re.search('mail.ru/video', link):
                                link1 = link
                                son_url = self.get_parsed_link(link1)
                            if re.search('rx/plx.php', link):
                                link1 = re.findall('src=["\'](.*?)["\']', data)[0]
                                req = urllib2.Request(link1, None, headers)
                                response = urllib2.urlopen(req)
                                data2 = response.read()
                                response.close()
                                link2 = re.findall('(https://www.rapidvideo.com/e/.*?)["\']', data2)[0]
                                son_url = self.get_parsed_link(link2)
                            if re.search('/embed-', link):
                                link1 = re.findall('/embed-(.*?)["\']', data)[0]
                                link1 = 'https://vidmoly.me/embed-' + link1
                                son_url = self.get_parsed_link(link1)
                            else:    
                                link1 = re.findall('src=["\'](.*?)["\']', data)[0]
                                req = urllib2.Request(link1, None, headers)
                                response = urllib2.urlopen(req)
                                data2 = response.read()
                                response.close()
                                if re.search('"file":"', data2):
                                    for match in re.finditer('"file":"(.*?)","ql":"(.*?)"', data2):
                                        film_quality.append(match.group(2))
                                        link = match.group(1)
                                        if link.startswith("//"):
                                            link = "https:" + link
                                        video_tulpe.append(link)
                                if re.search('"hls":"', data2):
                                    videolink = re.findall('"hls":"([^"]+)"', data2.replace('\\',''))[0]
                                    if videolink.startswith("//"):
                                        videolink = "https:" + videolink
                                    son_url = videolink
                    except Exception as e:
                        print 'link alinamadi : ' + str(e)
                        error = True
		
            if 'decodedlink' in url:
                try:
                    url = re.findall('decodedlink:(.*?)$', url, re.IGNORECASE)[0]
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    response.close()
                    if 'vidplayer' in data:
                        link = re.findall('vidplayer\/embed-([^"\']+)["\']', data)[0]
                        url1 = 'https://vidmoly.to/embed-' + link
                        son_url = self.get_parsed_link(url1)
                    if 'vidplayer' not in data:
                        link = re.findall('((?:vidmoly.|oload.|closeload.com|ok.ru|uptostream.com).*?)["\']', data)[0]
                        url1 = 'https://' + link
                        son_url = self.get_parsed_link(url1)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'postedlink' in url:
                try:
                    host, params, ref = re.findall('host:(.*?):params:(.*?):ref:(.*?)$', url, re.IGNORECASE)[0]
                    req = urllib2.Request(host, params, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    if re.search('"file":"([^"]+)","label":"([^"]+)"', html):
                        for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link.replace("\\",""))
                    if re.search("<script>.*?\('[^']+'", html):
                        server, link = re.findall("<script>(.*?)\('([^']+)'", html)[0]
                        if server == "fembed":
                            link = "https://www.fembed.net/api/source/"+link
                        if server == "uptobox":
                            link = "http://uptostream.com/iframe/"+link
                        if server == "rapid":
                            link = "https://www.rapidvideo.com/e/"+link
                        if server == "mailru":
                            link = "https://videoapi.my.mail.ru/videos/embed/"+link+".html"
                        if server == "openload":
                            link = "https://oload.tv/embed/"+link
                        if server == "okru":
                            link = "http://odnoklassniki.ru/videoembed/"+link
                        if server == "vshare":
                            link = "https://vshare.io/v/"+link+"/width-835/height-425/"
                        son_url = self.get_parsed_link(link)
                    if re.search('vidmo.cc/iframe', html):
                        link = re.findall("(vidmo.cc/iframe.*?)[\"']", html)[0]
                        son_url = self.get_parsed_link('https://'+link)
                    if re.search('fileru.me/iframe', html):
                        link = re.findall("(fileru.me/iframe.*?)[\"']", html)[0]
                        son_url = self.get_parsed_link('https://'+link)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
                    
            if 'posted720plink' in url:
                try:
                    host, params, ref = re.findall('host:(.*?):params:(.*?):ref:(.*?)$', url, re.IGNORECASE)[0]
                    url = host+"?"+params
                    html = cRequestHandler(url).request()
                    if re.search('"file":"([^"]+)","label":"([^"]+)"', html):
                        for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link.replace("\\",""))
                    elif re.search("<div id=\"[^\"]+\">.</div><script>.*?\('[^']+'", html):
                        server, link = re.findall("<div id=\"[^\"]+\">.</div><script>(.*?)\('([^']+)'", html)[0]
                        if server == "fembed":
                            link = "https://www.fembed.net/api/source/"+link
                        if server == "uptobox":
                            link = "http://uptostream.com/iframe/"+link
                        if server == "rapid":
                            link = "https://www.rapidvideo.com/e/"+link
                        if server == "mailru":
                            link = "https://videoapi.my.mail.ru/videos/embed/"+link+".html"
                        if server == "openload":
                            link = "https://oload.tv/embed/"+link
                        if server == "okru":
                            link = "http://odnoklassniki.ru/videoembed/"+link
                        if server == "vshare":
                            link = "https://vshare.io/v/"+link+"/width-835/height-425/"
                        son_url = self.get_parsed_link(link)
                    elif re.search('vidmo.cc/iframe', html):
                        link = re.findall("(vidmo.cc/iframe.*?)[\"']", html)[0]
                        son_url = self.get_parsed_link('https://'+link)
                    elif re.search('fileru.me/iframe', html):
                        link = re.findall("(fileru.me/iframe.*?)[\"']", html)[0]
                        son_url = self.get_parsed_link('https://'+link)
                    elif re.search('vcdn.io', html):
                        link = re.findall("(vcdn.io.*?)[\"']", html)[0]
                        params = ":params:r="+host+"&d=vcdn.io"
                        ref = ":ref:"+host
                        host = "host:https://"+link.replace('vcdn.io/v/', 'vcdn.io/api/source/');
                        video_url= "postedlink:"+host+params+ref
                        son_url = self.get_parsed_link(video_url)
                    else :
                        try:
                            link = re.findall("<iframe src=[\"'](.*?)[\"']", html)[0]
                            son_url = self.get_parsed_link(link)
                        except Exception as e:
                            print 'link alinamadi : ' + str(e)
                            error = True
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
                    
            if 'withreflink' in url:
                try:
                    url, ref = re.findall('(.*?)withreflink(.*?)$', url, re.IGNORECASE)[0]
                    req = urllib2.Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    if re.search('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                        for match in re.finditer('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('source src="([^"]+)" type="application/x-mpegurl">', html):
                        videolink = re.findall('source src="([^"]+)" type="application/x-mpegurl">', html)[0]
                        son_url = videolink + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search('file:"[^"]+",label:"[^"]+"', html):
                        for match in re.finditer('file:"([^"]+)",label:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search("file[\"'\s+]?[\"'\s+]?[\"'\s+]?:(?:|\s+)[\"'].*?[\"']", html):                    
                        videolink = re.findall("file[\"'\s+]?[\"'\s+]?[\"'\s+]?:(?:|\s+)[\"'](.*?)[\"']", html)[0]
                        son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("(https?://[^/]+/lba/.*?)[\"']", html):
                        videolink = re.findall("(https?://[^/]+/lba/\S+m3u8\S+)[\"']", html)[0]
                        son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search('file:.*?(?:|\()"[^"]+"(?:|\)),\s+width:', html):
                        try:
                            videolink = re.findall('file: "([^"]+)"', html)[0]
                            son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                        except:
                            link1 = re.findall('file:[\s\S]*?\("([^"]+)"', html)[0]
                            link1 = link1 [::-1]
                            son_url1 = decode_base64(link1)
                            son_url = son_url1 + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("eval\\(function\(p,a,c,k,e,d", html):
                        try:
                            packed = re.findall('(eval\\(function\(p,a,c,k,e,d.*?)\\n', html, re.IGNORECASE)[0]
                            html = html+cPacker().unpack(packed)
                        except:
                            pass
                    if re.search('play.php\?vid=', html):
                        videolink, host, vid = re.findall('((https://\S+)play.php\?vid=([^"]+))"', html)[0]
                        ref = url
                        req = urllib2.Request(videolink, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                        response = urllib2.urlopen(req)
                        html = response.read()
                        response.close()
                        alternative, ord = re.findall('id="alternative" value="([^"]+)"[\S\s]*?id="order" value="([^"]+)"', html)[0]
                        data = urllib.urlencode({"vid": vid, "alternative": alternative, "ord": ord,})
                        req = urllib2.Request(host+'ajax_sources.php', data, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                        response = urllib2.urlopen(req)
                        html = response.read()
                        response.close()
                    if re.search('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                        for match in re.finditer('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('file"?:"[^"]+",(?:|\s+)"?label"?:"[^"]+"', html):
                        for match in re.finditer('file"?:"([^"]+)",(?:|\s+)"?label"?:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1).replace('\\','')
                            if link.startswith("//"):
                                link = "https:" + link
                            if 'dizigom' in url :                               
                                video_tulpe.append(link)
                            else:
                                video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search("(?:file|source_url)[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html):
                        videolink = re.findall("(?:file|source_url)[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html)[0]
                        son_url = videolink #+ '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("(https?://[^/]+/lba/.*?)[\"']", html):
                        videolink = re.findall("(https?://[^/]+/lba/\S+m3u8\S+)[\"']", html)[0]
                        son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'cloudvideo' in url:
                try:
                    html = urlKap(url).result
                    vid_link1 = re.findall('src="([^"]+m3u8)"', html, re.IGNORECASE)[0]
                    son_url = vid_link1 + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'streamit.ws' in url:
                try:
                    streamitVideo(url)
                    
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True		
		
            if 'dazplayer' in url:
                try:
                    HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Referer': 'http://dazplayer.com/tv/'}
                    html = urlKap('http://dazplayer.com/tv/', HTTP_HEADER).result
                    daz_link = re.findall('(.*?)::dazplayer', url, re.IGNORECASE)[0]
                    oldid = re.findall('http://[^/]+/[^/]+/([^/]+)/', daz_link, re.IGNORECASE)[0]
                    newid = re.findall('file: "http://[^/]+/[^/]+/([^/]+)/', html, re.IGNORECASE)[0]
                    vid_link1 = daz_link.replace(oldid, newid) + 'm3u8'
                    son_url = vid_link1 + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True		
		
            if 'vanlongstream' in url:
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
                        'Referer': url,
                        'X-Requested-With': 'XMLHttpRequest'}
                    data = ""
                    key = re.findall('key=(.*?)$', url, re.IGNORECASE)[0]
                    url2 = 'https://tplayer.vanlongstream.com/getDataPlayer/vidmoly/' + key
                    req = urllib2.Request(url2, data , headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    serverID = re.findall('"data":"(.*?)"', html, re.IGNORECASE)[0]
                    req = urllib2.Request(serverID, None , headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    finalID = re.findall('(https://vidmoly.me/embed.*?)["\']', html, re.IGNORECASE)[0]
                    son_url = self.get_parsed_link(finalID)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'iframetoajax' in url:
                try:
                    link, host, ref = re.findall('((https?://.*?)/.*?):iframetoajax:(.*?)$', url, re.IGNORECASE)[0]
                    link = link.replace('iframe','ajax')
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': '*/*',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Connection': 'keep-alive',
						'Referer': ref}
                    js = host+"/video.js?"+str(int(time.time() * 1000))
                    req = urllib2.Request(js, None, headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    serverID, myip = re.findall("\(window,'(.*?)','(.*?)'", html, re.IGNORECASE)[0]
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': '*/*',
                        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                        serverID: myip}
                    req = urllib2.Request(link, None, headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    file, hash = re.findall('"file":"(.*?)","hash":"(.*?)"', html, re.IGNORECASE)[0]
                    son_url = file.replace('\\','') +"?"+hash
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'fullhdfilmizlesene_parse' in url:
                if 'name=fast' in url:
                    try:
                        url = re.findall('fullhdfilmizlesene_parse:(.*?)$', url, re.IGNORECASE)[0]
                        headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': 'https://www.fullhdfilmizlesene.net/'}
                        req = urllib2.Request(url, None, headers)
                        response = urllib2.urlopen(req)
                        data = response.read()
                        response.close()
                        data = data.replace('\\','')
                        link = re.findall('src=["\'](.*?)["\']', data)[0]
                        req = urllib2.Request(link, None, headers)
                        response = urllib2.urlopen(req)
                        data2 = response.read()
                        response.close()
                        link2 = re.findall('skin:[\s\S]*?(eval[\s\S]*?}\)\));', data2)[0]
                        gg =  cPacker().unpack(link2)
                        gg = gg.replace("\\'","'").replace('\\\\\\\\','\\\\\\')
                        ff =  cPacker().unpack(gg)
                        cc = ff.replace("\\","").replace("x","")
                        if re.search('"file":".*?","label":.*?"file":".*?","label"', cc):
                            for match in re.finditer('"file":"(.*?)","label":"(.*?)"', html):
                                film_quality.append(match.group(2))
                                link = match.group(1).decode('hex')
                                if link.startswith("//"):
                                    link = "https:" + link
                                video_tulpe.append(link)
                        else:
                            link3 = re.findall('"file":"(.*?)"', cc)[0]
                            son_url = link3.decode('hex')
                    except Exception as e:
                        print 'link alinamadi : ' + str(e)
                        error = True
                else:
                    try:
                        url = re.findall('fullhdfilmizlesene_parse:(.*?)$', url, re.IGNORECASE)[0]
                        headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': 'https://www.fullhdfilmizlesene.net/'}
                        req = urllib2.Request(url, None, headers)
                        response = urllib2.urlopen(req)
                        data = response.read()
                        response.close()
                        if re.search('src=', data):
                            data = data.replace('\\','')
                            link = re.findall('src=["\'](.*?)["\']', data)[0]
                            if re.search('php\?id=.*?&', link):
                                link1 = re.findall('php\?id=(.*?)&', link)[0]
                                son_url = self.get_parsed_link('https://ok.ru/videoembed/'+link1)
                            if re.search('(?:oload|openload)', link):
                                link1 = link
                                son_url = self.get_parsed_link(link1)
                            if re.search('mail.ru/video', link):
                                link1 = link
                                son_url = self.get_parsed_link(link1)
                            if re.search('rx/plx.php', link):
                                link1 = re.findall('src=["\'](.*?)["\']', data)[0]
                                req = urllib2.Request(link1, None, headers)
                                response = urllib2.urlopen(req)
                                data2 = response.read()
                                response.close()
                                link2 = re.findall('(https://www.rapidvideo.com/e/.*?)["\']', data2)[0]
                                son_url = self.get_parsed_link(link2)
                    except Exception as e:
                        print 'link alinamadi : ' + str(e)
                        error = True
		
            if 'decodedlink' in url:
                try:
                    url = re.findall('decodedlink:(.*?)$', url, re.IGNORECASE)[0]
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    response.close()
                    if re.search('player/url/', data):				
                        link = re.findall('player/url/(.*?)["\']', data)[0]
                        decod = decode_base64(decode_base64(link)[::-1])
                        url = decod.replace('closeload/', 'https://closeload.com/video/embed/').replace('oload/', 'https://oload.tv/embed/').replace('ok/', 'https://ok.ru/videoembed/').replace('uptostream/', 'https://uptostream.com/iframe/')
                        son_url = self.get_parsed_link(url)
                    elif re.search('vokiea.cf', data):				
                        link = re.findall('vokiea.cf/(.*?)["\']', data)[0]
                        son_url = self.get_parsed_link('https://vidmoly.me/'+ link)
                    else:
                        url = re.findall('((?:youtube.com|vidmoly.me|oload.tv|closeload.com|ok.ru|uptostream.com).*?)["\']', data)[0]
                        url = 'https://' + url
                        son_url = self.get_parsed_link(url)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'postedlink' in url:
                try:
                    host, params, ref = re.findall('host:(.*?):params:(.*?):ref:(.*?)$', url, re.IGNORECASE)[0]
                    req = urllib2.Request(host, params, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    if re.search('"file":"([^"]+)","label":"([^"]+)"', html):
                        for match in re.finditer('"file":"([^"]+)","label":"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link.replace("\\",""))
                    if re.search("<script>.*?\('[^']+'", html):
                        server, link = re.findall("<script>(.*?)\('([^']+)'", html)[0]
                        if server == "uptobox":
                            link = "http://uptostream.com/iframe/"+link
                        if server == "rapid":
                            link = "https://www.rapidvideo.com/e/"+link
                        if server == "mailru":
                            link = "https://videoapi.my.mail.ru/videos/embed/"+link+".html"
                        if server == "openload":
                            link = "https://oload.tv/embed/"+link
                        if server == "okru":
                            link = "http://odnoklassniki.ru/videoembed/"+link
                        if server == "vshare":
                            link = "https://vshare.io/v/"+link+"/width-835/height-425/"
                        son_url = self.get_parsed_link(link)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'withreflink' in url:
                try:
                    url, ref = re.findall('(.*?)withreflink(.*?)$', url, re.IGNORECASE)[0]
                    req = urllib2.Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    if re.search('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                        for match in re.finditer('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('file:"[^"]+",label:"[^"]+"', html):
                        for match in re.finditer('file:"([^"]+)",label:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search("file[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html):
					    videolink = re.findall("file[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html)[0]
					    son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("(https?://[^/]+/lba/.*?)[\"']", html):
					    videolink = re.findall("(https?://[^/]+/lba/.*?)[\"']", html)[0]
					    son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search('file: "http\S+m3u8\S+"', html):
					    videolink = re.findall('file: "(http\S+m3u8\S+)"', html)[0]
					    son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search('file:.*?(?:|\()"[^"]+"(?:|\)),\s+width:', html):
                        try:
                            videolink = re.findall('file: "([^"]+)"', html)[0]
                            son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                        except:
                            link1 = re.findall('file:[\s\S]*?\("([^"]+)"', html)[0]
                            link1 = link1 [::-1]
                            son_url1 = decode_base64(link1)
                            son_url = son_url1 + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("eval\\(function", html):
                        packed = re.findall('(eval\\(function\(p,a,c,k,e,d.*?)\\n', html, re.IGNORECASE)[0]
                        html = cPacker().unpack(packed)
                    if re.search('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                        for match in re.finditer('source src="([^"]+)" type="[^"]+" label=\'([^\']+)', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('file:"[^"]+",label:"[^"]+"', html):
                        for match in re.finditer('file:"([^"]+)",label:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            link = match.group(1)
                            if link.startswith("//"):
                                link = "https:" + link
                            video_tulpe.append(link + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search("file[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html):
					    videolink = re.findall("file[|\"'](?:|\s+):(?:|\s+)[\"'](.*?)[\"']", html)[0]
					    son_url = videolink #+ '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    if re.search("(https?://[^/]+/lba/.*?)[\"']", html):
					    videolink = re.findall("(https?://[^/]+/lba/.*?)[\"']", html)[0]
					    son_url = videolink + '#Referer=' +ref+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if '/rbtv/' in url:
                try:
                    url = url.replace('/rbtv/','/') + 'playlist.m3u8'
                    link_id = url
                    data_url = 'http://163.172.181.152:8030/rbtv/token21.php'
                    headers = {'User-agent' : 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G935F Build/LMY48Z)'}
                    url = data_url
                    username  ='@yarapnakaamkaro#';
                    password = '@tungnakiakaro#';
                    request = urllib2.Request(url,None,headers)
                    base64string = base64.b64encode('%s:%s' % (username, password))
                    request.add_header("Authorization", "Basic %s" % base64string)   
                    response = urllib2.urlopen(request)
                    html = response.read()
                    response.close()
                    agent = 'User-Agent=stagefright/1.2 (Linux;Android 5.1.1)'
                    son_url = link_id + html + '#' + agent.encode('utf-8')
                except Exception as ex:
                    print ex

            if 'SwiftLive' in url:
                try:
                    media, token, data = re.findall('(.*?)::SwiftLive::(.*?)::(.*?)$', url, re.IGNORECASE)[0]			
                    media = media + 'playlist.m3u8'
                    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Connection': 'Keep-Alive'}
                    url = 'http://62.210.172.84/'+token+'.php'
                    data = urllib.urlencode({"data": data})
                    req = urllib2.Request(url, data ,headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    auth_token = html.partition('=')[2]
                    auth_token = ''.join([auth_token[:-59], auth_token[-58:-47], auth_token[-46:-35], auth_token[-34:-23], auth_token[-22:-11], auth_token[-10:]])
                    agent = 'User-Agent=Lavf/56.15.102'
                    media_url = media+'?wmsAuthSign='+auth_token+'#' + agent.encode('utf-8')
                    son_url = media_url
                except Exception as ex:
                    print ex
					
            if 'trftr-tv' in url:
                try:
                    try:
                        media = re.findall('(.*?)::trftr-tv', url, re.IGNORECASE)[0]			
                        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Connection': 'Keep-Alive'}
                        req = urllib2.Request(media,None,headers)
                        response = urllib2.urlopen(req)
                        html = response.read()
                        response.close()
                        html = html.replace('\\','')
                        vide, olink = re.findall('"url":"(.*?wmsAuthSign=)(?:\S+=)?([^"]+)"', html, re.IGNORECASE)[0]
                        son_url = vide + olink + '#User-Agent=Lavf/57.83.100'
                    except Exception as ex:
                        if 'Error 401' in str(ex):
                            username  ='admin';
                            password = '12345';
                            request = urllib2.Request(media,None,headers)
                            base64string = base64.b64encode('%s:%s' % (username, password))
                            request.add_header("Authorization", "Basic %s" % base64string)   
                            response = urllib2.urlopen(request)
                            html = response.read()
                            response.close()
                            html = html.replace('\\','')
                            vide, olink = re.findall('"url":"(.*?wmsAuthSign=)(?:\S+=)?([^"]+)"', html, re.IGNORECASE)[0]
                            son_url = vide + olink + '#User-Agent=Lavf/57.83.100'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'rapidrame' in url:
                try:
                    url, ref = re.findall('(.*?html)-ref:(.*?)$', url, re.IGNORECASE)[0]
                    req = urllib2.Request(url, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    if re.search("eval\\(function", html):
                        packed = re.findall('(eval\\(function.*?)\\n', html, re.IGNORECASE)[0]
                        html = cPacker().unpack(packed)
                        for match in re.finditer('file:"([^"]+)",label:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1) + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('file:"[^"]+",label:"[^"]+', html):
                        for match in re.finditer('file:"([^"]+)",label:"([^"]+)"', html):
                            film_quality.append(match.group(2))
                            video_tulpe.append(match.group(1) + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                    if re.search('file:"[^"]+"', html):
                        videolink = re.findall('file:"([^"]+)"', html, re.IGNORECASE)[0]
                        son_url = videolink + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'fastplayer' in url:
                try:
                    url1, ref = re.findall("(http.*?):refurl=(.*?)$", url, re.IGNORECASE)[0]
                    req = urllib2.Request(url1, None, { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': ref })
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    packed = re.findall('(eval\(function.*?}\)\))', html, re.IGNORECASE)[0]
                    html = cPacker().unpack(packed)
                    videolink = re.findall('"sources":\[{"file":"([^"]+)"', html, re.IGNORECASE)[0]
                    if videolink.startswith("//"):
                        videolink = "https:" + videolink
                    son_url = videolink + '#Referer=' + url1 + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'kodik' in url:
                try:
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    req = urllib2.Request(url,None,headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    url_kodik = re.findall('iframe.src = "([^"]+)"', html, re.IGNORECASE)[0]
                    url_kodik = 'http:' + url_kodik
                    req = urllib2.Request(url_kodik,None,headers)
                    response = urllib2.urlopen(req)
                    html_kodik = response.read()
                    response.close()
                    domain, d_sign, pd, pd_sign, ref_sign  = re.findall('var domain = "([^"]+)";\s+var d_sign = "([^"]+)";\s+var pd = "([^"]+)";\s+var pd_sign = "([^"]+)";\s+var ref = "";\s+var ref_sign = "([^"]+)"', html_kodik, re.IGNORECASE)[0]
                    type, hash, id = re.findall("type: '([^']+)',\s+hash: '([^']+)',\s+id: '([^']+)'", html_kodik, re.IGNORECASE)[0]
                    data = urllib.urlencode({
					    'd': domain, 
					    'd_sign': d_sign, 
					    'pd': pd, 
					    'pd_sign': pd_sign,
					    'ref': '', 
					    'pd_sign': pd_sign,
					    'bad_user': 'false',
					    'type': 'video', 
					    'hash': hash, 
					    'id': id })
                    url = 'http://kodik.cc/get-video'
                    req = urllib2.Request(url, data, headers)
                    response = urllib2.urlopen(req)
                    link = response.read()
                    response.close()
                    for match in re.finditer('"([^"]+)":\[\{"src":"(.*?mp4)', link):
                        film_quality.append(match.group(1))
                        video_tulpe.append('http:' + match.group(2))
                except Exception as ex:
                    print ex

            if 'onlinetvcanli' in url:
                try:
                    url = url.replace('-onlinetvcanli','')
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    req = urllib2.Request(url,None,headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()						
                    embedlink = re.findall('(embedlive.flexmmp.com[^"]+)"', html, re.IGNORECASE)[0]
                    embedlink = 'http://'+embedlink.replace('&#038;','&')
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer': url }
                    req = urllib2.Request(embedlink,None,headers)
                    response = urllib2.urlopen(req)
                    html1 = response.read()
                    response.close()
                    videolink = re.findall("hls: ?'([^']+)'", html1, re.IGNORECASE)[0]
                    son_url = 'https:' + videolink + '#Referer=' + url + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as ex:
                    print ex

            if 'idtbox' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    for match in re.finditer('src="([^"]+)" type=".*?label="([^"]+)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0' + '&Referer=' + url)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
		
            if 'canlitvplayer' in url:
                try:
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    req = urllib2.Request(url,None,headers)
                    response = urllib2.urlopen(req)
                    html = response.read(20000)
                    response.close()
                    embedlink = re.findall('(/tv/embed.php[^"]+)"', html, re.IGNORECASE)[0]
                    embedlink = 'https://www.canlitvplayer.com'+embedlink.replace('&#038;','&')
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer': url }
                    req = urllib2.Request(embedlink,None,headers)
                    response = urllib2.urlopen(req)
                    html1 = response.read()
                    response.close()
                    try:
                        videolink = re.findall('source src="([^"]+)"', html1, re.IGNORECASE)[0]
                        son_url = videolink
                    except:
                        videolink = re.findall("file: ?'([^']+)'", html1, re.IGNORECASE)[0]
                        son_url = videolink
                except Exception as ex:
                    print ex

            if 'vshare' in url:
                try:
                    headers = {'Referer': url}
                    html = urlKap(url, headers).result
                    packed = re.findall("(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                    js = cPacker().unpack(packed).split(';')
                    charcodes = [int(val) for val in js[1].split('=')[-1].replace('[', '').replace(']', '').split(',')]
                    sub = int(''.join(char for char in js[2].split('-')[1] if char.isdigit()))
                    charcodes = [val-sub for val in charcodes]
                    srcs = ''.join(map(unichr, charcodes))
                    for match in re.finditer(u'src="([^"]+)".*?label="([^"]+)"', srcs):
                        film_quality.append(match.group(2).encode('utf-8'))
                        video_tulpe.append(match.group(1).encode('utf-8'))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'vidlox' in url:
                try:
                    headers = {'User-Agent': FF_USER_AGENT, 'Referer': url}
                    url = url.replace('https', 'http')
                    html = urlKap(url, headers).result
                    for match in re.finditer('"(http[^"]+(m3u8|mp4))"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
					
            if 'strdef' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer': url }
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    link = re.findall('document.write\(dhYas638H\(dhYas638H\("([^"]+)"', data)[0]
                    dd = (decode_base64(link))
                    cc = (decode_base64(dd))
                    link2 = re.findall('document.write\(dhYas638H\(dhYas638H\("([^"]+)"', cc)[0]
                    ee = (decode_base64(link2))
                    ff = (decode_base64(ee))
                    url = re.search(r'iframe src="([^"]+)"', ff, re.IGNORECASE).group(1)					
                    son_url = self.get_parsed_link(url)

                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'bspor' in url:
                try:
                    html = urlKap(url).result
                    url3 = re.findall('(http://whostreams.net/embed/[^"]+)"', html, re.IGNORECASE)[0]
                    html2 = urlKap(url3).result
                    packed = re.findall(">(eval\\(function.*?)\\n", html2, re.IGNORECASE)[0]
                    html4 = cPacker().unpack(packed)
                    son_url = re.findall('source:(?:| )"([^"]+)"', html4, re.IGNORECASE)[0] + '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0' + '&Referer=' + url3
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True


            if 'izletv' in url or 'ozeltv' in url:
                try:
                    url = url.replace('/izletv/','').replace('/ozeltv/','')
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    req = urllib2.Request(url,None,headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    hash, id = re.findall('(?:watch|live)\("([^"]+)","([^"]+)"', html, re.IGNORECASE)[0]
                    data = urllib.urlencode({'hash': hash, 'id': id, 'e': '03BSTMTRKLR'})
                    req = urllib2.Request(url, data, headers) 
                    response = urllib2.urlopen(req)
                    link = response.read()
                    response.close()
                    link1 = link [::-1]
                    #link1 = link1.replace('_','=') + '=='
                    #first64, second64 = re.findall('(.*?=)(.*?==)', link1, re.IGNORECASE)[0]
                    #son_url1 = base64.b64decode(first64)+'?'+base64.b64decode(second64)
                    son_url1 = decode_base64(link1)
                    Header = '#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                    son_url = son_url1 + Header
                except Exception as ex:
                    print ex

            if '24video' in url:
                try:
                    media_id = re.findall('embedPlayer/([A-Za-z0-9]+)', url, re.IGNORECASE)[0]
                    weburl = 'http://24video.ws/video/xml/' + media_id + '?mode=play'
                    req = urllib2.Request(weburl, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    son_url = re.findall('video url=[\'|"](.*?)[\'|"]', html)[0]
                    url = 'http://24video.ws/embedPlayer' + media_id
                    son_url = son_url.replace('&amp;', '&') + '#Referer=' +url+ '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
                except Exception as ex:
                    print ex
					
            if 'bitporno' in url:
                try:
                    #url = url.replace('https', 'http')
                    html = urlKap(url).result
                    for match in re.finditer('"(http[^"]+)" type="[^"]+" data-res="([^"]+)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1).replace('\\', ''))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'canlitv.com' in url:
                try:
                    request = urllib2.Request(url, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                     'Connection': 'Close'})
                    response = urllib2.urlopen(request).read()
                    link = re.findall('file: "(.*?)"', response)
                    son_url1 = link[0]
                    if son_url1.startswith("//"):
                        son_url1 = "https:" + son_url1
                    son_url = son_url1

                except Exception as ex:
                    print ex

            if 'canlitvlive' in url or 'livetv' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    Header = '#Referer='+url+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
                    try:
                        stlink = re.findall('((?:web|www|tv).canlitvlive.(?:io|site)/tvizle.php\?t=[^"]+)"', html, re.IGNORECASE)[0]
                        stlink = 'http://' + stlink
                        request = urllib2.Request(stlink, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Connection': 'Close'})
                        response = urllib2.urlopen(request).read()
                        link = re.findall('file(?: |):(?: |)"(.*?)"', response)
                        son_url1 = link[0]
                        if son_url1.startswith("//"):
                            son_url1 = "http:" + son_url1
                            son_url = son_url1 + Header
                    except:
                        link = re.findall('file: ?"(.*?)"', html)
                        son_url1 = link[0]
                        if son_url1.startswith("//"):
                            son_url1 = "http:" + son_url1
                            son_url = son_url1 + Header
                        else:
                            son_url = link[0] + Header
                except Exception as ex:
                    print ex
					
            if 'closeload' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    #packed = re.findall('(eval\\(function.*?)\\n', html, re.IGNORECASE)[0]
                    
                    link = re.findall('"contentUrl": "([^"]+)"', html)
                    son_url = link[0] + "#Referer=%s" % url
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
            if 'flashx' in url:
                try:
                    
                    son_url =self.FLASHXgetMediaLink(url)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
					
            if 'daclips.in' in url:
                try:
                    request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    response = urllib2.urlopen(request).read()
                    link = re.findall("(?:file|src): ['|\"](.*?)['|\"],", response)
                    son_url = link[0]
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
					
            if 'dailymotion.com' in url:
                url = url.replace('dailymotion.com/video/', 'dailymotion.com/embed/video/')
                try:
                    HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Referer': url}
                    page = urlKap(url, HTTP_HEADER).result
                    page = page.replace('\\', '')
                    v_tulpe = re.findall('"(\d+)"\s*:.+?"url"\s*:\s*"([^"]+)', page)
                    if v_tulpe:
                        for q, v in v_tulpe:
                            video_tulpe.append(v)
                            film_quality.append(q + 'p m3u8')
                except Exception as ex:
                    print ex
                    error = True
					
            if 'verystream'  in url:
                try:
                    req = urllib2.Request(url, None, {'Referer': 'https://verystream.com/','User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    page = response.read()
                    response.close()
                    token = re.findall('videolink">([^<]+)', page)[0]
                    son_url = 'https://verystream.com/gettoken/' + token + '?mime=true'
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
            if 'nxload.com' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    #html=html.replace('\r',"").replace('\s',"").replace('\n',"")
                    response.close()
                    packed = re.findall('(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))', html, re.IGNORECASE)[0]
                    htmli = cPacker().unpack(packed)
                   # htmli=htmli.replace("player.src({src:'","src:'")
                    m = re.search("'(.+?)'", htmli)
                    lk='|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&Referer='+ url
   
                    son_url = m.groups(1)[0][: - 1]         
                        
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'http://tiko' in url or 'https://tiko' in url or 'betit' in url or 'kazansana' in url or 'yonjatv' in url:
                try:
                    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    link, id = re.findall('(https?://iframe.ollocdn.online/index.php\?id=(\d+))', data)[0]
                    media_link = 'https://ollocdn.online/edge/'+ id +'/playlist.m3u8'
                    ref = '#Referer='+ link
                    son_url = media_link + ref
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
					
            if 'channel/watch/' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer': url }
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    Header = 'Referer='+url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
                    try: 
                        link = re.findall("file: '(.*?m3u8[^']+)'", data)[0]
                        son_url = link + '#' + Header
                    except:
                        link = re.findall('atob\("([^"]+)"', data)[0]
                        dd = (base64.b64decode(link))
                        Header = 'Referer='+url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
                        son_url = re.findall('source:"([^"]+)",watermark', dd)[0] + '#' + Header
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'marsb' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer': url }
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    link = re.findall("file: '([^']+)',\s+width", data)[0]
                    Header = 'Referer='+url+'&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
                    son_url = link + '#' + Header
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'docs.google.com' in url or 'drive.google.com' in url:
                try:
                    media_id = re.findall(r'https?://(?:(?:docs|drive)\.google\.com/(?:uc\?.*?id=|file/d/)|video\.google\.com/get_player\?.*?docid=)(?P<id>[a-zA-Z0-9_-]{20,40})', url, re.IGNORECASE)[0]
                    url = 'https://drive.google.com/file/d/%s/view' % media_id
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0', 'Referer': url})
                    response = urllib2.urlopen(req)
                    sHtmlContent = response.read()
                    Headers = response.headers
                    response.close()
                    c = Headers['Set-Cookie']
                    c2 = re.findall('(?:^|,) *([^;,]+?)=([^;,\/]+?);',c)
                    if c2:
                        cookies = ''
                        for cook in c2:
                            cookies = cookies + cook[0] + '=' + cook[1] + ';'
                    links_parts = re.findall('"fmt_stream_map","(.*?)"', sHtmlContent.decode('unicode-escape'))[0]
                    links_part = re.findall('\\|(.*?)(?:,|$)', links_parts)
                    film_quality = []
                    for link_part in links_part:
                        if link_part.encode('utf_8').find('itag=18') > -1:
                            video_link = (link_part + "#User-Agent=" + FF_USER_AGENT + "&Referer=https://youtube.googleapis.com/" + "&Cookie=" + cookies).encode('utf_8')
                            video_tulpe.append(video_link)
                            film_quality.append('360p')
                        if link_part.encode('utf_8').find('itag=22') > -1:
                            video_link = (link_part + "#User-Agent=" + FF_USER_AGENT + "&Referer=https://youtube.googleapis.com/" + "&Cookie=" + cookies).encode('utf_8')
                            video_tulpe.append(video_link)
                            film_quality.append('720p')
                        if link_part.encode('utf_8').find('itag=37') > -1:
                            video_link = (link_part + "#User-Agent=" + FF_USER_AGENT + "&Referer=https://youtube.googleapis.com/" + "&Cookie=" + cookies).encode('utf_8')
                            video_tulpe.append(video_link)
                            film_quality.append('1080p')
                except Exception as ex:
                    print ex
                    error = True
										
            if 'estream' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    for match in re.finditer('"([^"]+)" type=\'video\/mp4\' label=\'\d+x(.*?)\'', html):
                        film_quality.append(match.group(2)+'p')
                        video_tulpe.append(match.group(1))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'hqq.tv' in url or 'hqq.watch' in url or 'netu.tv' in url or 'waaw.tv' in url:
                try:
			
                    def tb(b_m3u8_2):
                        j = 0
                        s2 = ""
                        while j < len(b_m3u8_2):
                            s2 += "\\u0" + b_m3u8_2[j:(j + 3)]
                            j += 3

                        return s2.decode('unicode-escape').encode('ASCII', 'ignore')

                    ## loop2unobfuscated
                    def jswise(wise):
                        while True:
                            wise = re.search("var\s.+?\('([^']+)','([^']+)','([^']+)','([^']+)'\)", wise, re.DOTALL)
                            if not wise: break
                            ret = wise = js_wise(wise.groups())

                        return ret

                    ## js2python
                    def js_wise(wise):
                        w, i, s, e = wise

                        v0 = 0;
                        v1 = 0;
                        v2 = 0
                        v3 = [];
                        v4 = []

                        while True:
                            if v0 < 5:
                                v4.append(w[v0])
                            elif v0 < len(w):
                                v3.append(w[v0])
                            v0 += 1
                            if v1 < 5:
                                v4.append(i[v1])
                            elif v1 < len(i):
                                v3.append(i[v1])
                            v1 += 1
                            if v2 < 5:
                                v4.append(s[v2])
                            elif v2 < len(s):
                                v3.append(s[v2])
                            v2 += 1
                            if len(w) + len(i) + len(s) + len(e) == len(v3) + len(v4) + len(e): break

                        v5 = "".join(v3);
                        v6 = "".join(v4)
                        v1 = 0
                        v7 = []

                        for v0 in range(0, len(v3), 2):
                            v8 = -1
                            if ord(v6[v1]) % 2: v8 = 1
                            v7.append(chr(int(v5[v0:v0 + 2], 36) - v8))
                            v1 += 1
                            if v1 >= len(v4): v1 = 0

                        return "".join(v7)

                    media_id = re.findall('php\?vid=([0-9a-zA-Z/-]+)', url, re.IGNORECASE)[0]
                    headers = {'User-Agent': FF_USER_AGENT,
                               'Referer': 'https://waaw.tv/watch_video.php?v=%s&post=1' % media_id}
                    html = urlKap(url, headers).result
                    wise = re.search('''<script type=["']text/javascript["']>\s*;?(eval.*?)</script>''', html,
                                     re.DOTALL | re.I).groups()[0]
                    data_unwise = jswise(wise).replace("\\", "")
                    try:
                        at = re.search('at=(\w+)', data_unwise, re.I).groups()[0]
                    except:
                        at = ""
                    try:
                        http_referer = re.search('http_referer=(.*?)&', data_unwise, re.I).groups()[0]
                    except:
                        http_referer = ""
                    player_url = "http://hqq.watch/sec/player/embed_player.php?iss=&vid=%s&at=%s&autoplayed=yes&referer=on&http_referer=%s&pass=&embed_from=&need_captcha=0&hash_from=&secured=0" % (
                    media_id, at, http_referer)
                    headers.update({'Referer': url})
                    data_player = urlKap(player_url, headers).result
                    data_unescape = re.findall('document.write\(unescape\("([^"]+)"', data_player)
                    data = ""
                    for d in data_unescape:
                        data += urllib.unquote(d)

                    data_unwise_player = ""
                    wise = ""
                    wise = re.search('''<script type=["']text/javascript["']>\s*;?(eval.*?)</script>''', data_player,
                                     re.DOTALL | re.I)
                    if wise:
                        data_unwise_player = jswise(wise.group(1)).replace("\\", "")

                    try:
                        vars_data = re.search('/player/get_md5.php",\s*\{(.*?)\}', data, re.DOTALL | re.I).groups()[0]
                    except:
                        vars_data = ""
                    matches = re.findall('\s*([^:]+):\s*([^,]*)[,"]', vars_data)
                    params = {}
                    for key, value in matches:
                        if key == "adb":
                            params[key] = "0/"
                        elif '"' in value:
                            params[key] = value.replace('"', '')
                        else:
                            try:
                                value_var = re.search('var\s*%s\s*=\s*"([^"]+)"' % value, data, re.I).groups()[0]
                            except:
                                value_var = ""
                            if not value_var and data_unwise_player:
                                try:
                                    value_var = \
                                    re.search('var\s*%s\s*=\s*"([^"]+)"' % value, data_unwise_player, re.I).groups()[0]
                                except:
                                    value_var = ""
                            params[key] = value_var

                    data = urllib.urlencode(params)

                    headers.update({'X-Requested-With': 'XMLHttpRequest', 'Referer': player_url})
                    url = "http://hqq.watch/player/get_md5.php?"

                    req = urllib2.Request(url, data, headers)
                    response = urllib2.urlopen(req)
                    link = response.read()
                    response.close()
                    url_data = json.loads(link)

                    media_url = "https:" + tb(url_data["obf_link"].replace("#", "")) + ".mp4.m3u8"

                    if media_url:
                        del headers['X-Requested-With']
                        headers.update({'Origin': 'https://hqq.watch'})

                    def append_headers(headers):
                        return '|%s' % '&'.join(['%s=%s' % (key, urllib.quote_plus(headers[key])) for key in headers])
                            
                    son_url = media_url + append_headers(headers)
						
                except:
                    print 'link alinamadi'
                    error = True

            if 'izlesene.com' in url:
                try:
                    request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    response = urllib2.urlopen(request).read()
                    page = response.replace('\\', '').replace('%3A', ':').replace('%2F', '/').replace('%3F', '?').replace('%3D', '=').replace('%26', '&')
                    for match in re.finditer('value":"([^"]+)","source":"([^"]+)"', page):
					    video_tulpe.append(match.group(2))
					    film_quality.append(match.group(1))
                except Exception as ex:
                    print ex
                    error = True
					
            if 'vidoza' in url:
                try:
                    
                 req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                 response = urllib2.urlopen(req)
                 html = response.read()
                 response.close()
                 for match in re.finditer('src: *"([^"]+)".+?label:"([^"]+)"', html):
                        
                    ref=match.group(1)
                    TIK='|User-Agent=VLC/3.0.4 LibVLC/3.0.4'
                    oParser = cParser()
                    oRequest = cRequestHandler(url)
                    sHtmlContent = oRequest.request()
                    #cookie= urlKap(url, output='cookie').result
                    sPattern =  'src: *"([^"]+)".+?label:"([^"]+)"'
                    oParser = cParser()
                    aResult = oParser.parse(sHtmlContent, sPattern)
                    if (aResult[0] == True):
                       for i in aResult[1]:
                          video_tulpe.append(str(i[0]+TIK)) 

                          film_quality.append(str(i[1]))  
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if '.m3u8' in url:
                error = None
                video_tulpe_tmp = []
                url_main = ''
                try:
                    page = urlKap(url).result
                    url_main = '/'.join(url.split('/')[:-1]) + '/'
                    film_quality = re.findall('BANDWIDTH=([0-9]+)', page)
                    if film_quality:
                        video_tulpe_tmp = re.findall('BANDWIDTH=.*\\s(.*)', page)
                        if len(video_tulpe_tmp) > 1:
                            if video_tulpe_tmp[0].find('http') > -1:
                                for tulpe in video_tulpe_tmp:
                                    video_tulpe.append(tulpe.replace('\r', ''))

                            else:
                                for tulpe in video_tulpe_tmp:
                                    video_tulpe.append(url_main + tulpe.replace('\r', ''))
                        else:
                            film_quality = []
                            son_url = url
                    else:
                        son_url = url
                except:
                    son_url = url
					
            if 'mail.ru' in url:
                try:
                    html = urlKap(url).result
                    metadataUrl = re.findall('(?:metadataUrl|metaUrl)":.*?(//my[^"]+)', html)
                    if metadataUrl:
                        nurl = 'https:%s?ver=0.2.123' % metadataUrl[0]
                        page = urlKap(nurl, output='cookie').result
                        video_key = re.findall('video_key[^;]+', page)
                        if video_key:
                            for match in re.finditer('url":"(//cdn[^"]+).+?(\\d+p)', page):
                                video_tulpe.append('http:' + match.group(1) + '#User-Agent=' + FF_USER_AGENT + '&Cookie=' + video_key[0])
                                film_quality.append(match.group(2))
                    else:
                        error = True
                except Exception as ex:
                    print ex
                    error = True
					
            if 'ok.ru/videoembed' in url or 'odnoklassniki.ru' in url:
                try:
                    id1 = re.findall('https?://(?:www.)?(?:odnoklassniki|ok).ru/(?:videoembed/|dk\\?cmd=videoPlayerMetadata&mid=)(\\d+)', url)[0]
                    nurl = 'https://m.ok.ru/video/' + id1
                    cookie = urlKap(nurl, output='cookie').result 
                    TIK='|Cookie='+ cookie  
                    link = urlKap(nurl).result
                    url = re.findall('data-objid=".+?" href="(.+?)"',link,re.DOTALL)[0]
                    
                    tarzlistesi= []
                    tarzlistesi.append(("fullHD", ""+url.replace('st.mq=2','st.mq=8').replace('amp;',"") ))  
                    tarzlistesi.append(("full", ""+url.replace('st.mq=2','st.mq=6').replace('amp;',"") ))  
                    tarzlistesi.append(("hd", "%s" % url.replace('st.mq=2','st.mq=5').replace('amp;',"") ))
                    tarzlistesi.append(("sd", "%s" % url.replace('st.mq=2','st.mq=3').replace('amp;',"") ))
                    tarzlistesi.append(("low", "%s" % url.replace('st.mq=2','st.mq=2').replace('amp;',"") ))
                    tarzlistesi.append(("lowes", "%s" % url.replace('st.mq=2','st.mq=1').replace('amp;',"") ))
                    tarzlistesi.append(("mobile", "%s" %url.replace('st.mq=2','st.mq=4').replace('amp;',"") ))
                    for sTitle,sUrl in tarzlistesi:
                        video_tulpe.append(sUrl+TIK)
	                film_quality.append(sTitle)
                except:
                    error = True
                    print 'link alinamadi'
		
					                                  
            if 'openload' in url or 'oload.' in url or 'oladblock.' in url or 'openloed.' in url or 'streamcherry.' in url:
                try:
                   
                   
                   media_id = re.findall('https?://[^/]+/[^/]+/(.*?)(?:/|$)', url, re.IGNORECASE)[0]
                   urll = 'https://openload.co/embed/' +media_id
                   
                   son_url =getMediaLinkForGuest(urll)
                  
                
                except Exception as ex:
                    print ex
                    error = True            
            if 'plus.google.com' in url:
               
                try:
                    request = urllib2.Request(url, None, HEADERS)
                    response = urllib2.urlopen(request).read()
                    response = response.replace('\\', '')
                    for match in re.finditer(r'\[\d+,(\d+),\d+,"([^"]+)"\]', response):
                        film_quality.append(match.group(1))
                        video_tulpe.append(match.group(2).replace('\\', '').replace('u003d', '='))
                except Exception as ex:
                    print ex
                    error = True
					
            if 'radio.de' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    page = response.read()
                    response.close()
                    if re.match('.*?"stream"', page, re.S):
                        pattern = re.compile('"stream":"(.*?)"')
                        stationStream = pattern.findall(page, re.S)
                        if stationStream:
                            film_quality = []
                            son_url = stationStream[0]
                except:
                    print 'link alinamadi'
                    error = True
					
            if 'rapidvideo' in url:
                try:
                    media_id = re.findall('rapidvideo.(?:org|com)/(?:\\?v=|e/|embed/)([A-z0-9]+)', url, re.IGNORECASE)[0]
                    web_url = 'https://www.rapidvideo.com/v/%s' % media_id
                    request = urllib2.Request(web_url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    response = urllib2.urlopen(request).read()
                    if '&q=' in response:
                        for match in re.finditer(r'"(http.*?%s&q=([^"]+))"' % media_id, response):
					        request2 = urllib2.Request(match.group(1), None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3','Connection': 'Close'})
					        response2 = urllib2.urlopen(request2).read()
					        for match2 in re.finditer(r'source src="([^"]+)" type="video/mp4" title="([^"]+)"', response2):
					            film_quality.append(match2.group(2))
					            video_tulpe.append(match2.group(1).replace('\\', ''))
                    elif 'type="video/mp4" label=' in response:
                        for match3 in re.finditer('src="([^"]+)" type="video/mp4" label="([^"]+)"', response):
                            film_quality.append(match3.group(2))
                            video_tulpe.append(match3.group(1).replace('\\', ''))
                    else:
                        for match4 in re.finditer('src="(http[^"]+)" type="video/mp4"', response):
                            son_url = match4.group(1)
                except Exception as ex:
                    print ex
                    error = True
				
            if 'raptu' in url:
                try:
                    url = url.replace("raptu", "bitporno")
                    son_url = self.get_parsed_link(url)
                    #media_id = re.findall('raptu.com/(?:\?v\=|embed/|.+?\u=)?([0-9a-zA-Z]+)', url, re.IGNORECASE)[0]
                    #web_url = 'https://www.raptu.com/?v=%s' % media_id
                    #request = urllib2.Request(web_url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                    # 'Connection': 'Close'})
                    #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
                    #info = urllib2.urlopen(request, context=gcontext).read()
                    #response = urllib2.urlopen(request).read()
                    #response = response.replace('\\', '')
                    #for match in re.finditer(r'"file":"([^"]+)","label":"([^"]+)"', response):
                    #    film_quality.append(match.group(2))
                    #    video_tulpe.append(match.group(1).replace('\\', ''))
						
                except Exception as ex:
                    print ex
                    error = True
					
            if 'sportstream365' in url:
                try:
                    id = re.findall('http://sportstream365/(.*?)/', url, re.IGNORECASE)[0]
                    #tk = 'http://sportstream-365.com/LiveFeed/GetGame?id='+id+'&partner=24'####>>>>>>>http://sportstream365.com/js/iframe.js
                    #html = urlKap(tk, referer='http://www.sportstream-365.com/').result
                    #file = re.findall('true,"VI":"(.*?)"',html)[0]
                    #file = re.findall('.*?VI[\'"]*[:,]\s*[\'"]([^\'"]+)[\'"].*',html)[0]
                    link = '"http://213.183.42.50/hls-live/xmlive/_definst_/' + id + '/' + id + '.m3u8?whence=1001":"Server 1", "http://93.189.63.194/hls-live/xmlive/_definst_/' + id + '/' + id + '.m3u8?whence=1001":"Server 2"'
                    for match in re.finditer('"(.*?)":"(.*?)"', link):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + '#User-Agent=Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36')
                    #son_url = 'http://213.183.46.114/hls-live/xmlive/_definst_/' + id + '/' + id + '.m3u8?whence=1001' + '#User-Agent=Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36'
                except Exception as ex:
                    print ex

            if 'startv.com' in url:
                try:
                    HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Referer': url}
                    html = urlKap(url, HTTP_HEADER).result
                    ol_id = re.search(r'"videoUrl": "([^"]+)"', html, re.IGNORECASE).group(1)
                    html1 = urlKap(ol_id, HTTP_HEADER).result
                    video_url = re.search(r'"hls":"([^"]+)"', html1, re.IGNORECASE).group(1)
                    son_url = video_url.replace('\\', '')
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
					
            if 'streamango' in url or 'streamcherry' in url or 'fruithosts' in url:
                try:
                    url = url.replace('http:','https:').replace('streamango','streamcherry')
                    if 'reffo' in url:
                        url, ref = re.findall('(.*?)reffo:(.*?)$', url, re.IGNORECASE)[0]
                    else:
                        ref = url
                    def decode(encoded, code):

                        _0x59b81a = ""
                        k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
                        k = k[::-1]

                        count = 0

                        for index in range(0, len(encoded) - 1):
                            while count <= len(encoded) - 1:
                                _0x4a2f3a = k.index(encoded[count])
                                count += 1
                                _0x29d5bf = k.index(encoded[count])
                                count += 1
                                _0x3b6833 = k.index(encoded[count])
                                count += 1
                                _0x426d70 = k.index(encoded[count])
                                count += 1

                                _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
                                _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
                                _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
                                _0x2e4782 = _0x2e4782 ^ code

                                _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

                                if _0x3b6833 != 64:
                                    _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
                                if _0x3b6833 != 64:
                                    _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

                        return _0x59b81a
				
                    HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Referer': ref}
                    html = downloadpage(url, headers=HTTP_HEADER).data
                    video_urls = []

                    matches = re.findall("type:\"video/([^\"]+)\",src:d\('([^']+)',(.*?)\).+?height:(\d+)", html, re.DOTALL | re.MULTILINE)

                    for ext, encoded, code, quality in matches:

                        media_url = decode(encoded, int(code))

                        if not media_url.startswith("http"):
                            media_url = "http:" + media_url
                        video_urls.append(["%sp" % (quality), media_url])

                    video_urls.reverse()
                    for video_url in video_urls:

                        son_url = video_url[1].replace("@", "")
                        
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'streamcloud' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    postdata = {}
                    for i in re.finditer('<input.*?name="(.*?)".*?value="(.*?)">', html):
                        postdata[i.group(1)] = i.group(2).replace("download1", "download2")
                    data = urllib.urlencode(postdata)
                    req = urllib2.Request(url, data, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    keto = response.read()
                    response.close()
                    r = re.search('file: "(.+?)",', keto)
                    if r:
                        son_url = r.group(1) + "#User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0&Referer=" + url
                except Exception as ex:
                    print ex
                    error = True

            if 'trt' in url:
                try:
                    request = urllib2.Request(url, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                     'Connection': 'Close'})
                    response = urllib2.urlopen(request).read()
                    link = re.findall('(http\S+m3u8\S+)["\']', response)
                    son_url = link[0].replace('amp;','')
                except Exception as ex:
                    print ex
					
            if 'uptostream' in url:
                try:
                    html = urlKap(url).result
                    try:
                        for i in re.finditer('"src":"([^"]+)","type":"[^"]+","label":"([^"]+)"', html):
                            film_quality.append(i.group(2))
                            video_tulpe.append(i.group(1).replace('\\', ''))
                    except:
                        for i in re.finditer('source src=[\'|"](.*?)[\'|"].*?data-res=[\'|"](.*?)[\'|"]', html):
                            film_quality.append(i.group(2))
                            video_tulpe.append('http:' + i.group(1))
                except:
                    print 'link alinamadi'
                    error = True
            if 'gounlimited' in url:
                try:
                    if not url.endswith('.mp4'):
                       oParser = cParser()
                       oRequest = cRequestHandler(url)
                       sHtmlContent = oRequest.request()

                       sPattern = '(\s*eval\s*\(\s*function\(p,a,c,k,e(?:.|\s)+?)<\/script>'
                       aResult = oParser.parse(sHtmlContent, sPattern)
                       if (aResult[0] == True):
                           sHtmlContent = cPacker().unpack(aResult[1][0])

                           sPattern =  '{sources:\["([^"]+)"\]'
                           aResult = oParser.parse(sHtmlContent, sPattern)
                           if (aResult[0] == True):
                               son_url = aResult[1][0]
                    else:
                        son_url =url

                    if (son_url):
                        son_url  + '|User-Agent=' + UA
                except Exception as ex:
                    print ex
					

            if 'userscloud' in url:
                try:
                    url = url.replace('https', 'http')
                    request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                     'Connection': 'Close'})
                    try:
					    page = urllib2.urlopen(request).read()
                    except httplib.IncompleteRead, e:
					    page = e.partial
                    video_url = re.findall('"(http[^"]+mp4)"', page)[0]
                    son_url = video_url
                except Exception as ex:
                    print ex
					
            if 'xsportv' in url or 'betestream' in url or 'queenbet' in url or 'betpark' in url:
                try:
                    html = urlKap(url).result
                    link = re.findall('(https?://matchservice[^"]+)', html, re.IGNORECASE)[0]
                    req = urllib2.Request(link, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0', 'Referer': url})
                    response = urllib2.urlopen(req)
                    sHtmlContent = response.read()
                    Headers = response.headers
                    response.close()
                    son_url1 = re.findall("source = '(.*?)'", sHtmlContent, re.IGNORECASE)[0]
                    son_url = son_url1 + "#User-Agent=Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/30.0.1599.12 Mobile/11A465 Safari/8536.25 (3B92C18B-D9DE-4CB7-A02A-22FD2AF17C8F)&Referer=" + link
                    if son_url.startswith("#"):
                        son_url = ''
                    else:
                        son_url = son_url
                except Exception as ex:
                    print ex
					
            if 'cccam' in url:
                try:
                    def get_html(link):
                            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                                'Accept-Encoding': 'none',
                                'Accept-Language': 'en-US,en;q=0.8',
                                'Referer': link}
                            req = urllib2.Request(link, None, headers)
                            try: 
                                response = urllib2.urlopen(req, timeout = 10)
                                html = response.read()
                                response.close()
                                return html
                            except:
                                pass
                    list = ('https://cccam4free.com/FREE/new0.php', 'http://bosscccam.co/Test.php', 'https://cccamyou.com/cccamfree/get.php',
                        'https://powerfullcccam.com/powerfull/get.php', 'https://cccamgate.net/24hcccam-test.php', 
                        'http://cccamstore.tv/free-server.php', 'http://cccambird.com/cccam48h.php', 'http://cccammania.com/free4/get2.php')
                    cccam_list = []
                    counter = 1
                    for link in list:
                        try:
                            html = get_html(link)
                            server, port, user, pasw = re.findall('(?:\s|>| )(?:c|C):\s+(\S+)\s+(\d+)\s+(\S+)\s+(.*?)(?:\s|<| )', html, re.IGNORECASE)[0]
                            server_list = (str(counter), server, port, user, pasw)
                            cccam_list.append(server_list)
                            counter += 1
                        except:
                            pass
                            
                    if 'path' in url:
                        try:
                            path = re.findall('path::(.*?)$', url, re.IGNORECASE)[0]
                            oscam = open ( path+'/oscam.server', 'w')
                            cccam = open ( path+'/CCcam.cfg', 'w')
                            for satir in cccam_list:
                                oscam_line = '\n\n[reader]\nlabel=TURKvod_server_'+satir[0]+'\nenable=1\nprotocol=cccam\ndevice=' + satir[1] + ',' + satir[2] + '\nuser=' + satir[3] + '\npassword=' + satir[4] +'\ncccversion=2.1.2\ngroup=1\ninactivitytimeout=1\nreconnecttimeout=30\nlb_weight=100\ncccmaxhops=10\nccckeepalive=1\ncccwantemu=0'
                                oscam.write(oscam_line)
                                cccam_line = 'C: ' + satir[1] + ' ' + satir[2] + ' ' + satir[3] + ' ' + satir[4] + '\n'
                                cccam.write(cccam_line)
                            cccam_end = '\n\n\nALLOW TELNETINFO: yes\nALLOW WEBINFO: yes\nWEBINFO LISTEN PORT : 16001\nSTATIC CW FILE : /usr/keys/constant.cw\nCAID PRIO FILE : /etc/CCcam.prio\nPROVIDERINFO FILE : /etc/CCcam.providers\nCHANNELINFO FILE : /etc/CCcam.channelinfo'
                            cccam.write(cccam_end)
                            oscam.close()
                            cccam.close()
                        except:
                            pass
                    else:
                        try:
                            cccam = open ('/usr/keys/CCcam.cfg', 'w')
                            oscam = open ('/usr/keys/oscam.server', 'w')
                            for satir in cccam_list:
                                oscam_line = '\n\n[reader]\nlabel=TURKvod_server_'+satir[0]+'\nenable=1\nprotocol=cccam\ndevice=' + satir[1] + ',' + satir[2] + '\nuser=' + satir[3] + '\npassword=' + satir[4] +'\ncccversion=2.1.2\ngroup=1\ninactivitytimeout=1\nreconnecttimeout=30\nlb_weight=100\ncccmaxhops=10\nccckeepalive=1\ncccwantemu=0'
                                oscam.write(oscam_line)
                                cccam_line = 'C: ' + satir[1] + ' ' + satir[2] + ' ' + satir[3] + ' ' + satir[4] + '\n'
                                cccam.write(cccam_line)
                            cccam.write('\n\n\nALLOW TELNETINFO: yes\nALLOW WEBINFO: yes\nWEBINFO LISTEN PORT : 16001\nSTATIC CW FILE : /usr/keys/constant.cw\nCAID PRIO FILE : /etc/CCcam.prio\nPROVIDERINFO FILE : /etc/CCcam.providers\nCHANNELINFO FILE : /etc/CCcam.channelinfo')
                            oscam.close()
                            cccam.close()
                        except:
                            pass
                        try:
                            cccam = open ('/etc/CCcam.cfg', 'w')
                            for satir in cccam_list:
                                cccam_line = 'C: ' + satir[1] + ' ' + satir[2] + ' ' + satir[3] + ' ' + satir[4] + '\n'
                                cccam.write(cccam_line)
                            cccam.write('\n\n\nALLOW TELNETINFO: yes\nALLOW WEBINFO: yes\nWEBINFO LISTEN PORT : 16001\nSTATIC CW FILE : /usr/keys/constant.cw\nCAID PRIO FILE : /etc/CCcam.prio\nPROVIDERINFO FILE : /etc/CCcam.providers\nCHANNELINFO FILE : /etc/CCcam.channelinfo')
                            cccam.close()
                        except:
                            pass
                        try:
                            oscam = open ('/etc/tuxbox/config/oscam/oscam.server', 'w')
                            for satir in cccam_list:
                                oscam_line = '\n\n[reader]\nlabel=TURKvod_server_'+satir[0]+'\nenable=1\nprotocol=cccam\ndevice=' + satir[1] + ',' + satir[2] + '\nuser=' + satir[3] + '\npassword=' + satir[4] +'\ncccversion=2.1.2\ngroup=1\ninactivitytimeout=1\nreconnecttimeout=30\nlb_weight=100\ncccmaxhops=10\nccckeepalive=1\ncccwantemu=0'
                                oscam.write(oscam_line)
                            oscam.close()
                        except:
                            pass
                        son_url = oscam_line
                except Exception as ex:
                    print ex
					
            if 'videojs.tmgrup.com' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer':'http://www.atv.com.tr/'}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    url2, url1 = re.findall('"VideoUrl":"([^"]+)".*?"VideoSmilUrl":"([^"]+)"', data, re.IGNORECASE)[0]
                    host = 'https://securevideotoken.tmgrup.com.tr/webtv/secure?url=' + url1 + '&url2=' + url2
                    req = urllib2.Request(host, None, headers)
                    response = urllib2.urlopen(req)
                    data2 = response.read()
                    url3 = re.findall('true,"Url":"([^"]+)"', data2, re.IGNORECASE)[0]
                    son_url = self.get_parsed_link(url3)
                except:
                    print 'link alinamadi'
                    error = True					
					
            if 'videotoken.tmgrup.com.tr' in url:
                try:
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
                            'Referer':'http://www.atv.com.tr/webtv/canli-yayin'}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    data = response.read()
                    match = re.findall('true,"Url":"(.+?)"', data, re.DOTALL | re.MULTILINE)
                    son_url = '**** '+match[0]
                    if match:
      	              url3 = match[0]
      	              son_url = self.get_parsed_link(url3)
                except:
                    print 'link alinamadi'
                    error = True					              
					
            if 'vidmoly' in url or 'venus/playm' in url or 'akar/playm' in url or 'flmplayer.online/vidplayer' in url:
                try:
                    cookie ='|Referer='+ url
                    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
                    req = urllib2.Request(url, None, headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    if re.search("type='text/javascript'>(eval\\(function.*?)\\n", html):
                        packed = re.findall("type='text/javascript'>(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                        html = cPacker().unpack(packed)
                    for match in re.finditer('"([^"]+(m3u8|mp4))"', html):
                        linko = match.group(1)
                        if linko.startswith("//"):
                            linko = "http:" + linko
                        film_quality.append(match.group(2))
                        video_tulpe.append(linko+cookie)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'mvidoza' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    for match in re.finditer('src: *"([^"]+)", type: "video/mp4", label:"SD", res:"720"', html):
                        
                       son_url=match.group(1)
                except Exception as ex:
                    print ex
                    error = True
				
            if 'vidto.me' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    link = response.read()
                    response.close()
                    ids = re.compile('<input type="hidden" name="id".*?value="(.*?)">').findall(link)[0]
                    fname = re.compile('<input type="hidden" name="fname".*?value="(.*?)">').findall(link)[0]
                    hash1 = re.compile('<input type="hidden" name="hash".*?value="(.*?)">').findall(link)[0]
                    postdata = {'op': 'download1',
                     'id': ids,
                     'fname': fname,
                     'hash': hash1,
                     'referer': '',
                     'imhuman': 'Proceed to video',
                     'usr_login': ''}
                    sleep_time = int(re.findall('>([0-9])</span> seconds<', link)[0])
                    time.sleep(sleep_time)
                    data = urllib.urlencode(postdata)
                    req = urllib2.Request(url, data, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    for match in re.finditer('file:"(.*?)",label:"(\d+p)"', html):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1))
                except Exception as ex:
                    print ex
                    error = True

            if 'vidup' in url:
                try:
                    media_id = re.findall("embed/([A-z0-9]+)", url, re.IGNORECASE)[0]
                    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
                    data = urllib.urlencode({})
                    url = 'https://vidup.io/api/serve/video/%s' % media_id
                    req = urllib2.Request(url, data, headers)
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    for match in re.finditer('"(\d+p)":"([^"]+)"', html):
                        film_quality.append(match.group(1))
                        video_tulpe.append(match.group(2))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'vidzi' in url:
                try:
                    req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    response.close()
                    if re.search("type='text/javascript'>(eval\\(function.*?)\\n", html):
                        packed = re.findall("type='text/javascript'>(eval\\(function.*?)\\n", html, re.IGNORECASE)[0]
                        html = cPacker().unpack(packed)
                    for match in re.finditer('file:?"([^"]+(m3u8|mp4))"', html):
                        film_quality.append(match.group(2).replace('v.mp', 'mp4'))
                        video_tulpe.append(match.group(1).replace('?embed=', ''))
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True

            if 'vk.com' in url:
                query = url.split('?', 1)[-1]
                query = parse_qs(query)
                x_m = '=smd6IXY6wWY60WY6IXY6smd9MWYt9FevJmJ'
                api_url = 'http://vk.com/al_video.php?act=show_inline&al=1&video=%s_%s' % (query['oid'][0], query['id'][0])
                v_k = '=0DZpZ3PwhGcusmdvIXYsFWbhJXYvATMvUWbuQ2b2tmc1R3LvoDc0RHa'
                media_id = 'https://vk.com/video%s_%s' % (query['oid'][0], query['id'][0])
                req = urllib2.Request(api_url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                response = urllib2.urlopen(req)
                html = response.read()
                response.close()
                if 'mp4' in html :
                    html = re.sub('\\\\', '', html)
                    html = html.replace('https://', 'http://')
                    for match in re.finditer('"url(\d+)":"(https?:[^"]+)"', html):
                        film_quality.append(match.group(1))
                        video_tulpe.append(match.group(2))
                else:
                    vk_link = base64.b64decode(v_k[::-1])+query['oid'][0]+"_"+query['id'][0]+base64.b64decode(x_m[::-1])
                    req = urllib2.Request(vk_link, None, {'User-agent': 'Mozilla/5.0 TURKvod-10'})
                    response = urllib2.urlopen(req)
                    html = response.read()
                    Headers = response.headers
                    response.close()
                    for match in re.finditer('<mp4_([^>]+)>([^>]+)<', html):
                        film_quality.append(match.group(1).replace('mp4_','')+'P')
                        video_tulpe.append(urllib2.unquote(match.group(2)))

            if 'vimeo.com' in url:
                try:
                    ids = re.findall('vimeo.com(?:/video)?/(\\d+)', url)[0]
                    url = 'http://player.vimeo.com/video/' + ids + '/config'
                    headers = {'Referer': 'https://vimeo.com/',
                               'Origin': 'https://vimeo.com'}
                    data = urlKap(url,headers).result
                    packed = re.findall('("progressive":\[{.+?}\]})', data, re.IGNORECASE)[0]
                    reg = re.findall(',"url":"(.+?)",.+?"quality":"(.+?)",', packed)
                    for src, quality in reg:
                        video_tulpe.append(src)
                        film_quality.append(quality)
                except:
                    error = True
                    print 'link alinamadi'

            if 'web.tv' in url:
                try:
                    request = urllib2.Request(url, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                     'Connection': 'Close'})
                    response = urllib2.urlopen(request).read()
                    link = re.findall('"src":"(.*?)"', response)
                    son_url = link[0]
                    son_url = son_url.replace('\\', '')
                except Exception as ex:
                    print ex
				
            if 'yourporn' in url:
                try:
                    request = urllib2.Request(url, None, {'User-agent': 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                     'Connection': 'Close'})
                    response = urllib2.urlopen(request).read()
                    link = re.findall("src='([^']+mp4)'", response)
                    son_url1 = link[0]
                    if son_url1.startswith("//"):
                        son_url1 = "http:" + son_url1
                    son_url = son_url1
                except Exception as ex:
                    print ex

            if 'youtube' in url:
                gecerli_url = '^\n                 (\n                     (?:https?://)?                                       # http(s):// (optional)\n                     (?:youtu\\.be/|(?:\\w+\\.)?youtube(?:-nocookie)?\\.com/|\n                        tube\\.majestyc\\.net/)                             # the various hostnames, with wildcard subdomains\n                     (?:.*?\\#/)?                                          # handle anchor (#/) redirect urls\n                     (?!view_play_list|my_playlists|artist|playlist)      # ignore playlist URLs\n                     (?:                                                  # the various things that can precede the ID:\n                         (?:(?:v|embed|e)/)                               # v/ or embed/ or e/\n                         |(?:                                             # or the v= param in all its forms\n                             (?:watch(?:_popup)?(?:\\.php)?)?              # preceding watch(_popup|.php) or nothing (like /?v=xxxx)\n                             (?:\\?|\\#!?)                                  # the params delimiter ? or # or #!\n                             (?:.*?&)?                                    # any other preceding param (like /?s=tuff&v=xxxx)\n                             v=\n                         )\n                     )?                                                   # optional -> youtube.com/xxxx is OK\n                 )?                                                       # all until now is optional -> you can pass the naked ID\n                 ([0-9A-Za-z_-]+)                                         # here is it! the YouTube video ID\n                 (?(1).+)?                                                # if we found the ID, everything can follow\n                 $'
                mobj = re.match(gecerli_url, url, re.VERBOSE)
                video_id = mobj.group(2)
                html = urlKap(url).result
                html = html.replace('\\','')
                try:
                    if 'm3u8' in html:
                        link = re.findall('"(http[^"]+m3u8)"', html, re.IGNORECASE)[0]
                        page = urlKap(link).result
                        url_main = '/'.join(link.split('/')[:-1]) + '/'
                        film_quality = re.findall('BANDWIDTH=([0-9]+)', page)
                        if film_quality:
                            video_tulpe_tmp = re.findall('BANDWIDTH=.*\\s(.*)', page)
                            if len(video_tulpe_tmp) > 1:
                                if video_tulpe_tmp[0].find('http') > -1:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(tulpe.replace('\r', ''))
                                else:
                                    for tulpe in video_tulpe_tmp:
                                        video_tulpe.append(url_main + tulpe.replace('\r', ''))
                            else:
                                film_quality = []
                                son_url = link
                        else:
                            son_url = link
                    else:
                        import urllib
                        import urlparse
                        def remove_additional_ending_delimiter(data):
                            pos = data.find("};")
                            if pos != -1:
                                data = data[:pos + 1]
                            return data

                        def normalize_url(url):
                            if url[0:2] == "//":
                                url = "http:" + url
                            return url

                        def extract_flashvars(data):
                            assets = 0
                            flashvars = {}
                            found = False
                            for line in data.split("\n"):
                                if line.strip().find(";ytplayer.config = ") > 0:
                                    found = True
                                    p1 = line.find(";ytplayer.config = ") + len(";ytplayer.config = ") - 1
                                    p2 = line.rfind(";")
                                    if p1 <= 0 or p2 <= 0:
                                        continue
                                    data = line[p1 + 1:p2]
                                    break
                            data = remove_additional_ending_delimiter(data)
                            if found:
                                data = load(data)
                                if assets:
                                    flashvars = data["assets"]
                                else:
                                    flashvars = data["args"]
                            for k in ["html", "css", "js"]:
                                if k in flashvars:
                                    flashvars[k] = normalize_url(flashvars[k])
                            return flashvars

                        def get_signature(youtube_page_data):
                            urljs = re.findall('"assets":.*?"js":\s*"([^"]+)"', youtube_page_data, re.IGNORECASE)[0]
                            urljs = urljs.replace("\\", "")
                            if urljs:
                                if not re.search(r'https?://', urljs):
                                    urljs = urlparse.urljoin("https://www.youtube.com", urljs)
                                req = urllib2.Request(urljs, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                                response = urllib2.urlopen(req)
                                data_js = response.read()
                                response.close()
                                
                            pattern = r'(?P<fname>\w+)=function\(\w+\){(\w)=\2\.split\(""\);.*?return\s+\2\.join\(""\)}'
                            funcname = re.search(pattern, data_js).group('fname')
                            jsi = JSInterpreter(data_js)
                            js_signature = jsi.extract_function(funcname)
                            return js_signature

                        def extract_videos(video_id):
                            url = 'https://www.youtube.com/get_video_info?video_id=%s&eurl=https://youtube.googleapis.com/v/%s&ssl_stream=1' % \
                                  (video_id, video_id)
                            req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                            response = urllib2.urlopen(req)
                            data = response.read()
                            response.close()
                            video_urls = []
                            params = dict(urlparse.parse_qsl(data))
                            if params.get('hlsvp'):
                                video_urls.append(["(LIVE .m3u8) [youtube]", params['hlsvp']])
                                return video_urls
                            req = urllib2.Request("https://www.youtube.com/watch?v=%s" % video_id, None, {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
                            response = urllib2.urlopen(req)
                            youtube_page_data = response.read()
                            response.close()
                            params = extract_flashvars(youtube_page_data)
                            if params.get('player_response'):
                                params = load(params.get('player_response'))
                                data_flashvars = params["streamingData"]
                                for s_data in data_flashvars:
                                    if s_data in ["adaptiveFormats", "formats"]:
                                        for opt in data_flashvars[s_data]:
                                            opt = dict(opt)
                                            if "audioQuality" not in opt:
                                                continue
                                            if "cipher" in opt:
                                                signature = get_signature(youtube_page_data)
                                                cipher = dict(urlparse.parse_qsl(urllib.unquote(opt["cipher"])))
                                                url = re.search('url=(.*)', opt["cipher"]).group(1)
                                                s = cipher.get('s')
                                                url = "%s&sig=%s" % (urllib.unquote(url), signature([s]))
                                                video_urls.append(["%s" % itag_list.get(opt["itag"], "video"), url])
                                            elif opt["itag"] in itag_list:
                                                video_urls.append(["%s" % itag_list.get(opt["itag"], "video"), opt["url"]])
                            return video_urls
                            
                        video_id = re.findall('(?:v=|embed/)([A-z0-9_-]{11})', url, re.IGNORECASE)[0]
                        page = extract_videos(video_id)
                        for quality, src in page:
                            if "mp4" in quality:
                                video_tulpe.append(src.encode('utf-8'))
                                film_quality.append(quality)
                except Exception as ex:
                    print ex
                    error = True
            if 'youwatch' in url or 'chouhaa' in url:
                
                try:
                    headers = {'User-Agent': FF_USER_AGENT, 'Referer': url}
                    media_id = re.findall('(?://|\.)(?:youwatch.org|chouhaa.info|voodaith7e.com|youwatch.to)/(?:embed-|)([a-z0-9]+)', url, re.IGNORECASE)[0]
                    page_url = 'http://youwatch.org/embed-%s.html' % media_id
                    html = urlKap(page_url, headers).result
                    html1 = re.findall('<iframe\s+src\s*=\s*"([^"]+)', html, re.IGNORECASE)[0]
                    html2 = urlKap(html1, headers).result
                    for match in re.finditer('file:"([^"]+)",label:"(\d+)"', html2):
                        film_quality.append(match.group(2))
                        video_tulpe.append(match.group(1) + "#Referer=" + html1)
                except Exception as e:
                    print 'link alinamadi : ' + str(e)
                    error = True
					
            if error:
                return (error, video_tulpe, film_quality)
            elif film_quality:
                return (error, video_tulpe, film_quality)
            else:
                return son_url
                
        except Exception as ex:
            print ex
            print 'html_parser ERROR'

    def FLASHXgetMediaLink(self,sUrl):
       try: 
        api_call = False

        oParser = cParser()

        #on recupere le host atuel
        HOST = GetHost(sUrl)
        
        #on recupere l'ID
        sId = __getIdFromUrl(sUrl)
        if sId == '':
            VSlog("Id prb")
            return False, False

        #on ne garde que les chiffres
        #sId = re.sub(r'-.+', '', sId)

        #on cherche la vraie url
        sHtmlContent = GetRedirectHtml(sUrl, sId)

        #fh = open('c:\\test.txt', "w")
        #fh.write(sHtmlContent)
        #fh.close()
        
        sPattern = 'href=["\'](https*:\/\/www\.flashx[^"\']+)'
        AllUrl = re.findall(sPattern, sHtmlContent, re.DOTALL)
        #VSlog(str(AllUrl))

       
        if (False):
            if AllUrl:
                # Need to find which one is the good link
                # Use the len don't work
                for i in AllUrl:
                    if i[0] == '':
                        web_url = i[1]
            else:
                return False,False
        else:
            web_url = AllUrl[0]

        web_url = AllUrl[0]
      
        #Requests to unlock video
        #unlock fake video
        LoadLinks(sHtmlContent)
        #unlock bubble
        unlock = False
        url2 = re.findall('["\']([^"\']+?\.js\?cache.+?)["\']', sHtmlContent, re.DOTALL)
        if not url2:
            VSlog('No special unlock url find')
        for i in url2:
            unlock = UnlockUrl(i)
            if unlock:
                break
     
        if not unlock:
            VSlog('No special unlock url working')
            return False, False

        #get the page
        sHtmlContent = GetRedirectHtml(web_url, sId, True)

        if sHtmlContent == False:
            VSlog('Passage en mode barbare')
            #ok ca a rate on passe toutes les url de AllUrl
            for i in AllUrl:
                if not i == web_url:
                    sHtmlContent = GetRedirectHtml(i, sId, True)
                    if sHtmlContent:
                        break
        
        if not sHtmlContent:
            return False, False
         
        if 'reload the page!' in sHtmlContent:
            #VSlog("page bloquée")

           
            sGoodUrl = web_url

           
            sPattern = 'reload the page! <a href="([^"]+)">!! <b>'
            aResult = re.findall(sPattern, sHtmlContent)
            if not aResult:
                return False, False
            sRefresh = aResult[0]


            
            sPattern = "<script type='text/javascript' src='([^']+)'><\/script>"
            aResult = re.findall(sPattern, sHtmlContent)
            if not aResult:
                return False, False

            deblockurl = aResult[0]
            if deblockurl.startswith('//'):
                deblockurl = 'http:' + deblockurl

           
            sHtmlContent = GetRedirectHtml(deblockurl, sId)

            #lien speciaux ?
            if sRefresh.startswith('./'):
                sRefresh = 'http://' + GetHost(sGoodUrl) + sRefresh[1:]
                
            #on rafraichit la page
            sHtmlContent = GetRedirectHtml(sRefresh, sId)
            #logger.info('sHtmlContent 2: ' + sHtmlContent)
            #et on re-recupere la page
            sHtmlContent = GetRedirectHtml(sGoodUrl, sId)
            #logger.info('sHtmlContent 3: ' + sHtmlContent)
        if (False):

            #A t on le lien code directement?
            sPattern = "(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>"
            aResult = re.findall(sPattern, sHtmlContent)

            if (aResult):
                #VSlog( "lien code")

                AllPacked = re.findall('(eval\(function\(p,a,c,k.*?)\s+<\/script>', sHtmlContent, re.DOTALL)
                if AllPacked:
                    for i in AllPacked:
                        sUnpacked = cPacker().unpack(i)
                        sHtmlContent = sUnpacked
                        if "file" in sHtmlContent:
                            break
                else:
                    return False, False

        #decodage classique
        sPattern = '{file:"([^",]+)",label:"([^"<>,]+)"}'
        sPattern = '{src: *\'([^"\',]+)\'.+?label: *\'([^"<>,\']+)\''
        aResult = oParser.parse(sHtmlContent, sPattern)

        #VSlog(str(aResult))
        #logger.info('aResult : ' + aResult )
        if (aResult[0] == True):
            #initialisation des tableaux
            url=[]
            qua=[]

            #logger.info('aResult : ' + aResult )
            for i in aResult[1]:
                #url.append(str(i[0]))
#                qua.append(str(i[1]))
               #logger.info('linko : ' + i )
            #Affichage du tableau
                 film_quality.append(str(i[1]))
                 video_tulpe.append(str(i[0]))

       except Exception as ex:
           print ex
           print 'html_parser ERROR'




def GetRedirectHtml( web_url, sId, NoEmbed = False):

        headers = {
        #'Host' : 'www.flashx.tv',
        'User-Agent': UA,
        #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'http://embed.flashx.tv/embed.php?c=' + sId,
        'Accept-Encoding': 'identity'
        }

        MaxRedirection = 3
        while MaxRedirection > 0:

            #generation headers
            #headers2 = headers
            #headers2['Host'] = self.GetHost(web_url)

            VSlog(str(MaxRedirection) + ' Test sur : ' + web_url)
            request = urllib2.Request(web_url, None, headers)

            redirection_target = web_url

            try:
                #ok ca a enfin marche
                reponse = urllib2.urlopen(request)
                sHtmlContent = reponse.read()
                reponse.close()

                if not (reponse.geturl() == web_url) and not (reponse.geturl() == ''):
                    redirection_target = reponse.geturl()
                else:
                    break
            except urllib2.URLError, e:
                if (e.code == 301) or  (e.code == 302):
                    redirection_target = e.headers['Location']
                else:
                    #VSlog(str(e.code))
                    #VSlog(str(e.read()))
                    return False

            web_url = redirection_target

            if 'embed' in redirection_target and NoEmbed:
                #rattage, on a pris la mauvaise url
                VSlog('2')
                return False

            MaxRedirection = MaxRedirection - 1

        return sHtmlContent

def __getIdFromUrl( sUrl):
        sPattern = "https*:\/\/((?:www.|play.)?flashx.+?)\/(?:playvid-)?(?:embed-)?(?:embed.+?=)?(-*[0-9a-zA-Z]+)?(?:.html)?"
        oParser = cParser()
        aResult = oParser.parse(sUrl, sPattern)
        if (aResult[0] == True):
            return aResult[1][0][1]

        return ''

def GetHost( sUrl):
        oParser = cParser()
        sPattern = 'https*:\/\/(.+?)\/'
        aResult = oParser.parse(sUrl, sPattern)
        if aResult[0]:
            return aResult[1][0]
        return ''

def setUrl( sUrl):
        sUrl = 'http://' + GetHost(sUrl) + '/embed.php?c=' + __getIdFromUrl(sUrl)
        return sUrl
def CheckGoodUrl( url):

        #VSlog('test de ' + url)
        headers = {'User-Agent': UA
                   #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   #'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                   #'Accept-Encoding': 'gzip, deflate, br',
                   #'Host': 'openload.co',
                   #'Referer': referer
        }

        req = urllib2.Request(url)#, None, headers)
        res = urllib2.urlopen(req)
        #pour afficher contenu
        #VSlog(res.read())
        #pour afficher header
        #VSlog(str(res.info()))
        #Pour afficher redirection
        #VSlog('red ' + res.geturl())

        if 'embed' is res.geturl():
            return false

        html = res.read()

        res.close()

        return res



def GetHtml(url, headers):
    request = urllib2.Request(url, None, headers)
    reponse = urllib2.urlopen(request)
    sCode = reponse.read()
    reponse.close()

    return sCode

def UnlockUrl(url2=None):
    headers9 = {
    'User-Agent': UA,
    'Referer': 'https://www.flashx.co/dl?playthis'
    }

    url1 = 'https://www.flashx.co/js/code.js'
    if url2:
        url1 = url2

    if not url1.startswith('http'):
        url1 = 'https:' + url1

    VSlog('Test unlock url :' + url1)

    oRequest = cRequestHandler(url1)
    oRequest.addParameters('User-Agent', UA)
    #oRequest.addParameters('Accept', '*/*')
    #oRequest.addParameters('Accept-Encoding', 'gzip, deflate, br')
    #oRequest.addParameters('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
    oRequest.addParameters('Referer', 'https://www.flashx.co/dl?playthis')
    code = oRequest.request()

    url = ''
    if not code:
        url = oRequest.getRealUrl()
        VSlog('Redirection :' + url)
    else:
        #VSlog(code)
        aResult = re.search("!= null\){\s*\$.get\('([^']+)', *{(.+?)}", code, re.DOTALL)
        if aResult:
            dat = aResult.group(2)
            dat = dat.replace("'", '')
            dat = dat.replace(" ", '')

            dat2 = dict(x.split(':') for x in dat.split(','))

            dat3 = aResult.group(1) + '?'
            for i,j in dat2.items():
                dat3 = dat3 + str(i)+ '=' + str(j) + '&'

            url = dat3[:-1]

    #url = 'https://www.flashx.tv/flashx.php?fxfx=6'

    if url:
        VSlog('Good Url :' + url1)
        VSlog(url)
        
        return GetHtml(url,headers9)

    VSlog('Bad Url :' + url1)

    return False

def LoadLinks(htmlcode):
        VSlog('Scan des liens')

        host = 'https://www.flashx.tv'
        sPattern ='[\("\'](https*:)*(\/[^,"\'\)\s]+)[\)\'"]'
        aResult = re.findall(sPattern, htmlcode, re.DOTALL)

        #VSlog(str(aResult))
        for http,urlspam in aResult:
            sUrl = urlspam

            if http:
                sUrl = http + sUrl

            sUrl = sUrl.replace('/\/', '//')
            sUrl = sUrl.replace('\/', '/')

            #filtrage mauvaise url
            if (sUrl.count('/') < 2) or ('<' in sUrl) or ('>' in sUrl) or (len(sUrl) < 15):
                continue
            if '[' in sUrl or ']' in sUrl:
                continue
            if '.jpg' in sUrl or '.png' in sUrl:
                continue

            #VSlog('test : ' + sUrl)

            if '\\x' in sUrl or '\\u' in sUrl:
                sUrl = ASCIIDecode(sUrl)
                if not sUrl:
                    continue

            if sUrl.startswith('//'):
                sUrl = 'http:' + sUrl

            if sUrl.startswith('/'):
                sUrl = host + sUrl

            #Url ou il ne faut pas aller
            if 'dok3v' in sUrl:
                continue

            #pour test
            if ('.js' not in sUrl) or ('.cgi' not in sUrl):
                continue
            #if 'flashx' in sUrl:
                #continue

            headers8 = {
            'User-Agent': UA,
            'Referer': 'https://www.flashx.tv/dl?playthis'
            }

            try:
                request = urllib2.Request(sUrl, None, headers8)
                reponse = urllib2.urlopen(request)
                sCode = reponse.read()
                reponse.close()
                #VSlog('Worked ' + sUrl)
            except urllib2.HTTPError, e:
                if not e.geturl() == sUrl:
                    try:
                        headers9 = {
                        'User-Agent': UA,
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate, br'
                        }
                        request = urllib2.Request(e.geturl().replace('https', 'http'), None, headers9)
                        reponse = urllib2.urlopen(request)
                        sCode = reponse.read()
                        reponse.close()
                        #VSlog('Worked ' + sUrl)
                    except urllib2.HTTPError, e:
                        VSlog(str(e.code))
                        #VSlog(e.read())
                        VSlog('Redirection Blocked ' + sUrl + ' Red ' + e.geturl())
                        pass
                else:
                    #VSlog('Blocked ' + sUrl)
                    VSlog(str(e.code))
                    VSlog('>>' + e.geturl())
                    VSlog(e.read())

        VSlog('fin des unlock')
def getHost(sUrl):
        parts = sUrl.split('//', 1)
        host = parts[0] + '//' + parts[1].split('/', 1)[0]
        return host
UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'            
def getMediaLinkForGuest(sUrl):
        
        oParser = cParser()
        #logger.info("Guest="+ sUrl)
        #recuperation de la page
        xbmc.log('url teste : ' + sUrl)
        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('referer', sUrl)
        oRequest.addHeaderEntry('User-Agent', UA)
        sHtmlContent1 = oRequest.request()
        #logger.info("sHtml="+ sHtmlContent1 )
        #fh = open('c:\\test.txt', "w")
        #fh.write(sHtmlContent1)
        #fh.close()

        #Recuperation url cachee
        TabUrl = []
        #sPattern = '<span style="".+?id="([^"]+)">([^<]+)<\/span>'
        sPattern = '<p id="([^"]+)" *style=\"\">([^<]+)<\/p>'
        aResult = re.findall(sPattern, sHtmlContent1)
        if not aResult:
            sPattern = '<p style="" *id="([^"]+)" *>([^<]+)<\/p>'
            aResult = re.findall(sPattern, sHtmlContent1)
        if (aResult):
            TabUrl = aResult
        else:
            VSlog('OPL er 1')
            return False, False

        #xbmc.log("Nbre d'url : " + str(len(TabUrl)))

        #on essait de situer le code
        sPattern = '<script src="\/assets\/js\/video-js\/video\.js.+?.js"(.+)*'

        aResult = re.findall(sPattern, sHtmlContent1, re.DOTALL)
        if (aResult):
            sHtmlContent3 = aResult[0]
        else:
            VSlog('OPL er 2')
            return False, False

        #Deobfuscation, a optimiser pour accelerer le traitement
        code = ''
        maxboucle = 4
        while (maxboucle > 0):
            sHtmlContent3 = CheckCpacker(sHtmlContent3)
            sHtmlContent3 = CheckJJDecoder(sHtmlContent3)
            sHtmlContent3 = CheckAADecoder(sHtmlContent3)

            maxboucle = maxboucle - 1

        code = sHtmlContent3

        #fh = open('c:\\html.txt', "w")
        #fh.write(code)
        #fh.close()

        id_final = ""
        sPattern = 'var srclink.*?\/stream\/.*?(#[^\'"]+).*?mime=true'
        aResult = re.findall(sPattern, code)
        if (aResult):
            id_final = aResult[0]
        else:
            VSlog('OPL er 9')
            return False, False

        if not (code):
            VSlog('OPL er 3')
            return False, False

        #Search the coded url
        Coded_url = ''
        for i in TabUrl:
            if len(i[1]) > 30:
                Coded_url = i[1]
                Item_url = '#' + i[0]
                VSlog( Item_url + ' : ' + Coded_url )

        if not(Coded_url):
            VSlog('Url codée non trouvée')
            return False, False

        #Nettoyage du code pr traitement
        code = CleanCode(code, Coded_url)

        #fh = open('c:\\JS.txt', "w")
        #fh.write(code)
        #fh.close()

#        VSlog('Code JS extrait')

#        dialog().VSinfo('Décodage: Peut durer plus d\'une minute.', self.__sDisplayName, 15)

        #interpreteur JS
        JP = JsParser()
        Liste_var = []
        JP.AddHackVar(Item_url, Coded_url)

        JP.ProcessJS(code, Liste_var)

        url = None
        #for name in [ '#streamurl', '#streamuri', '#streamurj']:
        #    if JP.IsVar( JP.HackVars, name ):
        #        url = JP.GetVarHack( name )
        #        VSlog( 'Decoded url ' + name + ' : ' + url )
        #        break
        url = JP.GetVarHack(id_final)

        if not(url):
            VSlog('Rate, debug: ' + str(Liste_var))
            return False, False

#        dialog().VSinfo('Ok, lien décodé.', self.__sDisplayName, 15)

        api_call =getHost(sUrl) + "/stream/" + url + "?mime=true"

        if '::' in api_call:
#            dialog().VSinfo('Possible problème d\'ip V6', self.__sDisplayName, 5)
            xbmc.sleep(5*1000)

        VSlog(api_call)

        if (api_call):
            return  api_call

        return False, False
            
            
            
def ASCIIDecode(string):

    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i + 2)] == '\\x':
            c = chr(int(string[(i + 2):(i + 4)], 16))
            i+= 3
        if string[i:(i + 2)] == '\\u':
            cc = int(string[(i + 2):(i + 6)], 16)
            if cc > 256:
                #ok c'est de l'unicode, pas du ascii
                return ''
            c = chr(cc)
            i+= 5
        ret = ret + c
        i = i + 1

    return ret

def SubHexa(g):
    return g.group(1) + Hexa(g.group(2))

def Hexa(string):
    return str(int(string, 0))

def parseInt(sin):
    return int(''.join([c for c in re.split(r'[,.]', str(sin))[0] if c.isdigit()])) if re.match(r'\d+', str(sin), re.M) and not callable(sin) else None

def CheckCpacker(str):

    sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
    aResult = re.findall(sPattern, str)
    if (aResult):
        str2 = aResult[0]
        if not str2.endswith(';'):
            str2 = str2 + ';'
        try:
            str = cPacker().unpack(str2)
            print('Cpacker encryption')
        except:
            pass

    return str

def CheckJJDecoder(str):

    sPattern = '([a-z]=.+?\(\)\)\(\);)'
    aResult = re.findall(sPattern, str)
    if (aResult):
        print('JJ encryption')
        return JJDecoder(aResult[0]).decode()

    return str

def CheckAADecoder(str):
    aResult = re.search('([>;]\s*)(ﾟωﾟ.+?\(\'_\'\);)', str, re.DOTALL | re.UNICODE)
    if (aResult):
        print('AA encryption')
        tmp = aResult.group(1) + AADecoder(aResult.group(2)).decode()
        return str[:aResult.start()] + tmp + str[aResult.end():]

    return str

def CleanCode(code,Coded_url):
    #extract complete code
    r = re.search(r'type="text\/javascript">(.+?)<\/script>', code, re.DOTALL)
    if r:
        code = r.group(1)

    #1 er decodage
    code = ASCIIDecode(code)

    #fh = open('c:\\html2.txt', "w")
    #fh.write(code)
    #fh.close()

    #extract first part
    P3 = "^(.+?)}\);\s*\$\(\"#videooverlay"
    r = re.search(P3, code, re.DOTALL)
    if r:
        code = r.group(1)
    else:
        VSlog('er1')
        return False

    #hack a virer dans le futur
    code = code.replace('!![]', 'true')
    P8 = '\$\(document\).+?\(function\(\){'
    code= re.sub(P8, '\n', code)
    P4 = 'if\(!_[0-9a-z_\[\(\'\)\]]+,document[^;]+\)\){'
    code = re.sub(P4, 'if (false) {', code)
    P4 = 'if\(+\'toString\'[^;]+document[^;]+\){'
    code = re.sub(P4, 'if (false) {', code)

    #hexa convertion
    code = re.sub('([^_])(0x[0-9a-f]+)', SubHexa, code)

    #Saut de ligne
    #code = code.replace(';', ';\n')
    code = code.replace('case', '\ncase')
    code = code.replace('}', '\n}\n')
    code = code.replace('{', '{\n')

    #tab
    code = code.replace('\t', '')

    #hack
    code = code.replace('!![]', 'true')

    return code

#************************************************************
#Fonctions non utilisées, juste la pour memoire
#************************************************************

def GetOpenloadUrl(url,referer):
    if 'openload.co/stream' in url:

        headers = {'User-Agent': UA,
                   #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   #'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                   #'Accept-Encoding': 'gzip, deflate, br',
                   #'Host': 'openload.co',
                   'Referer': referer
        }

        req = urllib2.Request(url, None, headers)
        res = urllib2.urlopen(req)
        #xbmc.log(res.read())
        finalurl = res.geturl()


        VSlog('Url decodee : ' + finalurl)

        #autres infos
        #xbmc.log(str(res.info()))
        #xbmc.log(res.info()['Content-Length'])

        if 'KDA_8nZ2av4/x.mp4' in finalurl:
            VSlog('pigeon url : ' + url)
            finalurl = ''
        if 'Content-Length' in res.info():
            if res.info()['Content-Length'] == '33410733':
                VSlog('pigeon url : ' + url)
                finalurl = ''
        if url == finalurl:
            VSlog('Bloquage')
            finalurl = ''

        return finalurl
    return url

#Code updated with code from https://gitlab.com/iptvplayer-for-e2
def decodek(k):
    y = ord(k[0])
    e = y - 0x37
    d = max(2, e)
    e = min(d, len(k) - 0x24 - 2)
    t = k[e:e + 0x24]
    h = 0
    g = []
    while h < len(t):
        f = t[h:h+3]
        g.append(int(f, 0x8))
        h += 3
    v = k[0:e] + k[e+0x24:]
    p = []
    i = 0
    h = 0
    while h < len(v):
        B = v[h:h + 2]
        C = v[h:h + 3]
        f = int(B, 0x10)
        h += 0x2

        if (i % 3) == 0:
            f = int(C, 8)
            h += 1
        elif i % 2 == 0 and i != 0 and ord(v[i-1]) < 0x3c:
            f = int(C, 0xa)
            h += 1

        A = g[i % 0xc]
        f = f ^ 0xd5
        f = f ^ A
        p.append(chr(f))
        i += 1

    return "".join(p)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            