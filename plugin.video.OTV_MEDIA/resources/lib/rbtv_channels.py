import requests
import json
import string
import random
from base64 import b64decode


class rbtvChannels(object):
    def __init__(self, config, user=""):
        self.config = config
        self.user = user
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/NRD90M)"})

    @staticmethod
    def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))
                     
    def register_user(self):
        user_url =  "http://163.172.111.138:8030/rbtv/i/adduserinfo.nettv/"                                           
        data = {"api_level": "25", "android_id": "f01d2abd92e39541", "device_id": "abd92e39541f01d2", "device_name": "Samsung SM-N976N", "version": "1.9 (37)"}
        headers = {
            "Referer": "http://welcome.com/",
            "Authorization": "Basic aGVsbG9NRjpGdWNrb2Zm",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; LGM-V300K Build/N2G47H)",
            "Host": "163.172.111.138:8030",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "Content-Length": "115"
        }
        r = self.s.post(user_url, headers=headers, data=data)
        self.user = str(r.json().get("user_id"))


    def get_channel_list(self):
        check = "1"
        if not self.user:
            self.register_user()
            check = "8"
        list_url ="http://163.172.111.138:8030/rbtv/i/redbox.tv/"
        data = {"check": "8", "user_id": "6594921", "version": "37"}
        headers = {
            "Referer": "http://welcome.com/",
            "Authorization": "Basic aGVsbG9NRjpGdWNrb2Zm",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X)",
            "Host": "163.172.111.138:8030",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "Content-Length": "34"
        }
        r = self.s.post(list_url, headers=headers, data=data)
        return r.json()

