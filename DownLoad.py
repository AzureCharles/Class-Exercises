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
            "cookie": "your cookie",
            "pragma": "no - cache",
            "referer": "https://github.com/search?q=python&type=Repositories",
            "user-agent": "your user-agent"
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
