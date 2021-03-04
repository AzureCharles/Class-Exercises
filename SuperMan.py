import DownLoad
import SaveData
import UrlManage
import ParseHtml

class SuperMan:
    '''
    调度器类
    '''
    def __init__(self):
        self.download = DownLoad.DownLoad()
        self.SaveData = SaveData.SaveData()
        self.urlmanage = UrlManage.UrlMange()
        self.parsehtml = ParseHtml.ParseHtml()

    def crawl(self,start_url):
        '''
        爬虫启动器
        :param start_url:搜索
        '''
        kw = input("请输入你要查询的关键字：")
        pageindex = 1
        conent = self.download.downloadhtml(start_url,pageindex,kw)
        page_links,totalpage = self.parsehtml.paramspage(conent)
        self.urlmanage.add_urls(page_links)
        while self.urlmanage.urlsize and pageindex-totalpage<0:
            url = self.urlmanage.get_url()
            content = self.download.downloaddetail(url)
            detail_list, item = self.parsehtml.paramsdetail(content,url)
            self.SaveData.save_csv(detail_list)
            self.SaveData.save_mongo(item)#保存到mongodb注意mongodb启动
            pageindex += 1

if __name__ == "__main__":
    start_url = 'https://github.com/search'
    # 搜索url 带4个参数
    info = '''
    欢迎使用github简单爬虫脚本
    '''
    superman = SuperMan()
    superman.crawl(start_url)
