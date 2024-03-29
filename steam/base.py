import json
from urllib.request import urlopen

class json_request(object):

    def _compose_url(self, base_url, use_ssl = False, **kwargs):
        """Composes a url used to download data"""
        api_key = '?key=' + _api_key
        url_list = [base_url, api_key]
        if not base_url[-1] == '/':
            base_url += '/'
        if not base_url[:8] == 'https://' or base_url[:7] == 'http://':
            temp_list = []
            if use_ssl:
                temp_list.append('https://')
            else:
                temp_list.append('http://')
            url_list = temp_list + url_list
        for k, v in kwargs.items():
            url_list.append(str('&' + k + '=' + v))
        self.url = ''.join(url_list)
        return self.url

    def _download(self, url = None):
        """Downloads json data of the passed url, or uses self.url"""
        if not url:
            url = self.url
        contents = urlopen(url).read()
        self.results = json.loads(contents.decode('utf-8'))
        return self.results

    def _get(self, values = None):
        """Gets passed values in results, if any. Otherwise returns the whole json object"""
        if not values:
            return self.results
        return_vals = []
        for value in values:
            vals = None
            for arg in value:
                if not vals:
                    vals = self.results[arg]
                else:
                    vals = vals[arg]
            return_vals.append(vals)
        return return_vals

def set_api_key(api_key):
    global _api_key
    _api_key = api_key
