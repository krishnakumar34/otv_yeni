# -*- coding: utf-8 -*-
import sys
try:
    from urlparse import parse_qsl, urlsplit
    from urllib import unquote_plus, urlencode
except ImportError:
    from urllib.parse import parse_qsl, urlsplit, unquote_plus, urlencode


class ParamHandler:
    def __init__(self):
        params = dict()
        if len(sys.argv) >= 3 and len(sys.argv[2]) > 0:
            params = dict(parse_qsl(urlsplit(sys.argv[2]).query))
        self.__params = params

    def getAllParameters(self):
        # returns all parameters as dictionary
        return self.__params

    def getValue(self, paramName):
        # returns value of one parameter as string, if parameter does not exists "False" is returned
        if self.exist(paramName):
            return self.__params[paramName]
            # paramValue = self.__params[paramName]
            # return unquote_plus(paramValue)
        return False

    def exist(self, paramName):
        # checks if paramter with the name "paramName" exists
        return paramName in self.__params

    def setParam(self, paramName, paramValue):
        # set the value of the parameter with the name "paramName" to "paramValue"
        # if there is no such parameter, the parameter is created
        # if no value is given "paramValue" is set "None"
        paramValue = str(paramValue)
        self.__params.update({paramName: paramValue})

    def addParams(self, paramDict):
        # adds a whole dictionary {key1:value1,...,keyN:valueN} of parameters to the ParameterHandler
        # existing parameters are updated
        for key, value in paramDict.items():
            self.__params.update({key: str(value)})

    def getParameterAsUri(self):
        outParams = dict()
        # temp solution
        try:
            del self.__params['url']
        except:
            pass
        try:
            del self.__params['name']
        except:
            pass
        try:
            del self.__params['mode']
        except:
            pass
        try:
            del self.__params['iconimage']
        except:
            pass

        if len(self.__params) > 0:
            for param in self.__params:
                if len(self.__params[param]) < 1:
                    continue
                outParams[param] = unquote_plus(self.__params[param])
            return urlencode(outParams)
        return 'params=0'
