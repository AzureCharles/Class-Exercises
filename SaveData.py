import csv
from pymongo import MongoClient

class SaveData:
    '''
    保存数据类
    '''
    def __init__(self):
        with open('data.csv','w',newline='') as file:
            csv_file = csv.writer(file)
            head = ['仓库名','作者链接','仓库链接','star数','fork数']
            csv_file.writerow(head)

        self.conn = MongoClient('192.168.0.113', 27017)
        # 可在此更改mongodb的服务器地址
        self.collection = self.conn['gitdb']['git']


    def save_csv(self,data):
        '''
        保存到csv
        :param data:保存数据
        :return:
        '''
        with open('data.csv','a',newline='') as file:
            csv_file = csv.writer(file,dialect='excel')
            csv_file.writerow(data)

    def save_mongo(self,data):
        '''
        保存到mongodb
        :param data:保存数据
        :return:
        '''
        self.collection.insert(data)
