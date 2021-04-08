import requests
import json

class Fund():
    def __init__(self):
        self.fundTitleMap = {'fundcode': '基金代码',
                             'name': '基金名称',
                             'jzrq': '净值日期',
                             'dwjz': '单位净值',
                             'gsz': '当前净值',
                             'gszzl': '涨跌幅',
                             'gztime': '更新时间'}

    #获取当前的基金信息
    def GetFundCurrentInformation(self, fundCode):
        url = 'http://fundgz.1234567.com.cn/js/%s.js?rt=1463558676006' % fundCode

        try:
             content = requests.get(url).content
        except:
            return {'基金代码': fundCode, '错误': '超时'}

        try:
            fundCurrentInformation = content.decode('utf-8').strip('jsonpgz( );')
        except:
            try:
                fundCurrentInformation = content.decode('gb2312').strip('jsonpgz( );')
                print(fundCurrentInformation)
            except:
                return {}

        try:
            fundCurrentInformation = json.loads(fundCurrentInformation)
        except:
            return {'基金代码': fundCode,'错误': '获取不到基金信息'}

        result = dict()
        for key, value in fundCurrentInformation.items():
            result[self.fundTitleMap[key]] = value

        return result