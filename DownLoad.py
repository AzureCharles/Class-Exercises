import requests

class DownLoad:
    '''
    页面加载类
    '''
    def __init__(self):
        self.headers = {
            "authority": "github.com",
            "method": "GET",
            # "path": "/search?p=2&q=python&type=Repositories&_pjax=%23js-pjax-container",
            "scheme": "https",
            "accept": "text/html",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "cookie": "_octo=GH1.1.462742362.1601099943; _ga=GA1.2.1719568693.1601099978; _device_id=f01f160896d4b04463985e3cfbcff371; user_session=jidfQzukHC8oMPZ0OvcbhfAfDFamlvFbLVUxuMqFt5MwmQWk; __Host-user_session_same_site=jidfQzukHC8oMPZ0OvcbhfAfDFamlvFbLVUxuMqFt5MwmQWk; logged_in=yes; dotcom_user=AzureCharles; color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; _gh_sess=753rQgPNW4qGAgRBzAVZfYRnx6%2FCrZYl49QkSPus4FHG8v5kZi0b8Z96DGaXekbc%2FLqDHBrLBlo6%2BvSrtMHOTmSekgp58bBAq06DLKos3eOzcyf6YmYzXy3Xfq9JA18eI77rnRW0QVAjPv4fGRYn41Grm8LE7pmzlLcJ3Y0KR6PiATPTLj6N5hkKBCY%2BkY2B--O04R3HaCvH0wIDQl--nigzLZt78qD5n00UzuO1ig%3D%3D",
            "pragma": "no - cache",
            "referer": "https://github.com/search?q=python&type=Repositories",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"
        }
        # 此处cookie和user-agent来自真实抓取的请求表头，包含隐私信息，建议用户运行程序前自行修改

    def downloadhtml(self, url, pageIndex, kw):
        '''
        加载页面
        :return:搜索结果页面内容
        '''
        params = {
            'p': pageIndex,
            'q': kw,
            'type': 'Repositories',
            '_pjax': '# js-pjax-container',
        }
        resp = requests.get(url=url, headers=self.headers, params=params, timeout=20)
        print(resp.status_code)
        if resp.status_code == 200:
            return resp.text
        return None

    def downloaddetail(self, url):
        '''
        加载详细页面
        :return:详细页面内容
        '''
        resp = requests.get(url=url, headers=self.headers, timeout=20)
        print(resp.status_code)
        print(resp.url)
        if resp.status_code == 200:
            return resp.text
        return None
