import kodi
import os.path
import xbmc
if xbmc.getCondVisibility('system.platform.android') and int(xbmc.getInfoLabel('System.BuildVersion')[:2]) >= 18:
    import fixetzipfile as zipfile
else:
    import zipfile


def all(_in, _out, dp=None):
    if dp:
        return allWithProgress(_in, _out, dp)
    return allNoProgress(_in, _out)


def allNoProgress(_in, _out):
    import xbmcgui
    # xbmcgui.Dialog().ok('no progress', _in, _out)
    try:
        zin = zipfile.ZipFile(_in, 'r')
        zin.extractall(_out)

    except Exception as e:
        kodi.message("There was an error:", str(e), 'Please try again later, Attempting to continue...')
        return False
    return True


def allWithProgress(_in, _out, dp):
    import xbmcgui
    # xbmcgui.Dialog().ok('with progress', _in, _out)
    try:
        zin = zipfile.ZipFile(_in, 'r')
        nFiles = float(len(zin.infolist()))
        count = 0
    except Exception as e:
        kodi.message("There was an error:", str(e), 'Please try again later, Attempting to continue...')
        return False
    try:
        for item in zin.infolist():
            count += 1
            update = count / nFiles * 100
            dp.update(int(update))
            zin.extract(item, _out)
    except Exception as e:
        kodi.message("There was an error:", str(e), 'Please try again later, Attempting to continue...')
        return False
    return True
