# -*- coding: utf-8 -*-
import re, sys, urllib, urllib2
from time import sleep
from urlparse import urlparse
import requests

def cf_sample_domain_function(func_expression, domain):
    parameter_start_index = func_expression.find('}(') + 2
    sample_index = cf_parse_expression(func_expression[parameter_start_index: func_expression.rfind(')))')])
    return ord(domain[int(sample_index)])


def cf_arithmetic_op(op, a, b):
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


def cf_parse_expression(expression, domain=None):
    def _get_jsfuck_number(section):
        digit_expressions = section.replace('!+[]', '1').replace('+!![]', '1').replace('+[]', '0').split('+')
        return int(''.join(str(sum(int(digit_char) for digit_char in digit_expression[1:-1]))
                           for digit_expression in digit_expressions))

    if '/' in expression:
        dividend, divisor = expression.split('/')
        dividend = dividend[2:-1]
        if domain:
            divisor_a, divisor_b = divisor.split('))+(')
            divisor_a = _get_jsfuck_number(divisor_a[5:])
            divisor_b = cf_sample_domain_function(divisor_b, domain)
            return _get_jsfuck_number(dividend) / float(divisor_a + divisor_b)
        else:
            divisor = divisor[2:-1]
            return _get_jsfuck_number(dividend) / float(_get_jsfuck_number(divisor))
    else:
        return _get_jsfuck_number(expression[2:-1])


class CFScrape:
    def resolve(self, url):
        Domain = re.sub(r'https*:\/\/([^/]+)(\/*.*)', '\\1', url)
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
                   'Referer': url, 'Host': Domain,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
                   'Accept-Encoding': 'gzip, deflate',
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1',
                   'Content-Type': 'text/html; charset=utf-8'}

       
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36', 'Upgrade-Insecure-Requests':'1', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Cookie': '__cfduid=d44cbf60c2d1aa34dccb03639ec3afd9b1588489679'}
        body = requests.get(url, headers = header).text
        
        
        parsed_url = urlparse(url)
        submit_url = "%s://%s/cdn-cgi/l/chk_jschl" % (parsed_url.scheme, parsed_url.netloc)
        params = {}

        try:
            params["jschl_vc"] = re.search(r'name="jschl_vc" value="(\w+)"', body).group(1)
            params["pass"] = re.search(r'name="pass" value="(.+?)"', body).group(1)
            params["s"] = re.search(r'name="s"\svalue="(?P<s_value>[^"]+)', body).group(1)
            js = self._extract_js(body, parsed_url.netloc)
        except:
            return None

        params["jschl_answer"] = js
        sParameters = urllib.urlencode(params, True)
        request = urllib2.Request("%s?%s" % (submit_url, sParameters))
        for key in headers:
            request.add_header(key, headers[key])
        sleep(5)

        try:
            response = opener.open(request)
        except urllib2.HTTPError as e:
            response = e
        return response

    @staticmethod
    def __checkCookie(cookieJar):
        for entry in cookieJar:
            if entry.expires > sys.maxint:
                entry.expires = sys.maxint

    @staticmethod
    def _extract_js(body, domain):
        form_index = body.find('id="challenge-form"')
        sub_body = body[form_index:]
        if body.find('id="cf-dn-', form_index) != -1:
            extra_div_expression = re.search('id="cf-dn-.*?>(.+?)<', sub_body).group(1)
        js_answer = cf_parse_expression(re.search('setTimeout\(function\(.*?:(.*?)}', body, re.DOTALL).group(1))
        builder = re.search("challenge-form'\);\s*;(.*);a.value", body, re.DOTALL).group(1)
        lines = builder.replace(' return +(p)}();', '', 1).split(';')

        for line in lines:
            if len(line) and '=' in line:
                heading, expression = line.split('=', 1)
                if 'eval(eval(' in expression:
                    expression_value = cf_parse_expression(extra_div_expression)
                elif 'function(p' in expression:
                    expression_value = cf_parse_expression(expression, domain)
                else:
                    expression_value = cf_parse_expression(expression)
                js_answer = cf_arithmetic_op(heading[-1], js_answer, expression_value)

        if '+ t.length' in body:
            js_answer += len(domain)
        ret = format(js_answer, '.10f')
        return (str(ret))
