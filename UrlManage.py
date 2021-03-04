class UrlMange:
    '''
    url管理器
    '''
    def __init__(self):
        self.urls = []

    def add_urls(self,urls):
        '''
        添加解析的地址
        :param urls:
        :return:
        '''
        for url in urls:
            self.urls.append(url)

    def get_url(self):
        '''
        获取地址
        :return:
        '''
        if self.urls != []:
            return self.urls.pop()

    def urlsize(self):
        '''
        获取还有多少没解析的地址
        :return:
        '''
        return len(self.urls)
