import re
from lxml import etree

class ParseHtml:
    '''
    解析类
    '''

    def paramspage(self,content):
        '''
        解析页面
        :return:page_link_list
        '''
        tree = etree.HTML(content)
        li_list = tree.xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li')
        page_link_list = []
        totalpage = tree.xpath('//*[@id="js-pjax-container"]/div/div[3]/div/div[2]/h3/text()')[0][0:-22]
        totalpage = re.sub('\s|\n|,','',totalpage)
        totalpage = int(float(totalpage)/10)
        for li in li_list:
            page_link_list.append('https://github.com' + li.xpath('./div/div/a/@href')[0])
        print(page_link_list)
        return page_link_list,totalpage

    def paramsdetail(self,content,detail_link):
        '''
        解析页面
        :return:
        '''
        tree = etree.HTML(content)
        item = {}
        detail_list = []
        title = tree.xpath('//span[@itemprop="author"]/a/text()')[0]
        author_link = 'https://github.com' + tree.xpath('//a[@rel="author"]/text()')[0]
        reposi_link = 'https://github.com' + detail_link
        star_num = tree.xpath('//a[@class="social-count js-social-count"]/text()')[0]
        fork_num = tree.xpath('//a[@class="social-count"]/text()')[0]
        item['title'] = tree.xpath('//span[@itemprop="author"]/a/text()')[0]
        item['author_link'] = 'https://github.com' + tree.xpath('//a[@rel="author"]/text()')[0]
        item['reposi_link'] = 'https://github.com' + detail_link
        item['star_num'] = tree.xpath('//a[@class="social-count js-social-count"]/text()')[0]
        item['fork_num'] = tree.xpath('//a[@class="social-count"]/text()')[0]
        detail_list.append(title)
        detail_list.append(author_link)
        detail_list.append(reposi_link)
        detail_list.append(star_num)
        detail_list.append(fork_num)
        return detail_list,item