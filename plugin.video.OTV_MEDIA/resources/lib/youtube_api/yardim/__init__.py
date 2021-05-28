


import xbmc, xbmcgui, xbmcaddon, xbmcplugin, xbmcvfs
from .http_server import get_http_server, is_httpd_live, get_client_ip_address

from .function_cache import FunctionCache

from .data_cache import DataCache

def make_dirs(path):
    if not path.endswith('/'):
        path = ''.join([path, '/'])
    path = xbmc.translatePath(path)
    if not xbmcvfs.exists(path):
        try:
            _ = xbmcvfs.mkdirs(path)
        except:
            pass
        if not xbmcvfs.exists(path):
            try:
                os.makedirs(path)
            except:
                pass
        return xbmcvfs.exists(path)



__all__ = ['datetime_parser', 'get_http_server', 'is_httpd_live', 
           'make_dirs']

