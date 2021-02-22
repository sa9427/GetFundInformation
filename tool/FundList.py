import requests
import pandas as pd
import os
import re

class FundList():
    def __init__(self):
        #获取配置文件信息
        from tool.configCreation import Config
        self.config = Config.GetConfig()
        self.config.sections()
        self.fundListPath = self.config['data']['fundListPath']

        #如果存在feather文件，则读取feather文件，不存在，则创建feather文件
        if os.path.exists(self.fundListPath):
            #对了，据说feather版本变更会影响编码，导致不同版本的feather文件不能相互读写，因此读取出现异常时
            #重新创建feather文件
            try:
                self.df = pd.read_feather(self.fundListPath)
            except:
                self.createFundList()
        else:
            self.createFundList()

    def createFundList(self):
        import requests
        result = requests.get('http://fund.eastmoney.com/js/fundcode_search.js').content.decode('utf-8').strip(
            '\ufeff var=;')
        result = eval(result)

        self.df = pd.DataFrame(result, columns=['code', 'abbreviation', 'name', 'type', 'phonetic'])
        self.df.to_feather(self.fundListPath)

    def updataFundList(self):
        self.createFundList()

    def getFundListFromType(self, type=''):
        if type == '':
            return self.df.values
        else:
            return self.df[self.df['type'] == type].values

    def getFundType(self):
        return list(self.df['type'].unique())

    def getFundListType(self):
        return list(self.df.columns)

    def getFundListFromFind(self, type, keyword):
        #如果纯数字，则进行基金代码查找
        if keyword:
            if type:
                # 使用当前type获取新的data
                data = self.df[self.df['type'] == type]
            else:
                data = self.df

            keyword = keyword.upper()

            if len(keyword) == len(re.findall('\d', keyword)):
                data = data[data['code'].str.contains(keyword)]
                return data.values
            elif len(keyword) == len(re.findall('[A-Z]', keyword)):
                phoneticIndex = data[data['phonetic'].str.contains(keyword)].index
                abbreviationIndex = data[data['abbreviation'].str.contains(keyword)].index
                index = list(set(phoneticIndex) | set(abbreviationIndex))
                return data.iloc[index].values
            else:
                data = data[data['name'].str.contains(keyword)]
                return data.values
        else:
            return self.df.values