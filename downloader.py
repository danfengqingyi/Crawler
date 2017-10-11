import urllib2

import sys


class Downloader(object):

    def download(self, req):
        if req is None:
            return
        # response = urllib2.urlopen(url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(req, headers=headers)
        content = urllib2.urlopen(req).read()  # UTF-8

        # type = sys.getfilesystemencoding()  # local encode format
        # print content.decode("UTF-8").encode(type)  # convert encode format
        # if response.getCode()!=200:
        #     return None
        return content