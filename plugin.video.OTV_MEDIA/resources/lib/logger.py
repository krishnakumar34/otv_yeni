# -*- coding: utf-8 -*-
PY3 = False
import xbmc, sys
from resources.lib import common
from resources.lib.handler.ParameterHandler import ParameterHandler



class logger:
    @staticmethod
    def info(sInfo):
        if sys.version_info[0] == 2:
            logger.__writeLog(sInfo, cLogLevel=xbmc.LOGNOTICE)
        else:
            logger.__writeLog(sInfo, cLogLevel=xbmc.LOGINFO)

    @staticmethod
    def debug(sInfo):
        logger.__writeLog(sInfo, cLogLevel=xbmc.LOGDEBUG)

    @staticmethod
    def error(sInfo):
        logger.__writeLog(sInfo, cLogLevel=xbmc.LOGERROR)

    @staticmethod
    def fatal(sInfo):
        logger.__writeLog(sInfo, cLogLevel=xbmc.LOGFATAL)

    @staticmethod
    def __writeLog(sLog, cLogLevel=xbmc.LOGDEBUG):
        params = ParameterHandler()
        try:
            if sys.version_info[0] == 2:
                if isinstance(sLog, unicode):
                    sLog = '%s (ENCODED)' % (sLog.encode('utf-8'))
            if params.exist('site'):
                site = params.getValue('site')
                sLog = "\t[%s] -> %s: %s" % (common.addonName, site, sLog)
            else:
                sLog = "\t[%s] %s" % (common.addonName, sLog)
            xbmc.log(sLog, cLogLevel)
        except Exception as e:
            xbmc.log('Logging Failure: %s' % e, cLogLevel)
            pass

