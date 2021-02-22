# import pandas as pd
import os
import csv
from tool.configCreation import Config


class MyselfSelectFund():
    def __init__(self):
        config = Config.GetConfig()

        self.myselfSelectFundDict = dict()
        self.myselfSelectFundPath = config['data']['myselfSelectFundPath']
        if not os.path.exists(self.myselfSelectFundPath):
            with open(self.myselfSelectFundPath, 'w+', encoding='utf-8') as f:
                f_csv = csv.writer(f)
                f_csv.writerow(['code', 'name'])
        else:
            with open(self.myselfSelectFundPath, 'r+', encoding='utf-8') as f:
                csvData = csv.reader(f)
                for datum in csvData:
                    if datum and datum[0] != 'code':
                        self.myselfSelectFundDict[datum[0]] = datum[1]

    def GetMyselfSelectFundDict(self):
        return self.myselfSelectFundDict

    def AddMyselfSelectFund(self, fundCode, fundName):
        if not fundCode in self.myselfSelectFundDict:
            with open(self.myselfSelectFundPath, 'a+', encoding='utf-8') as f:
                f_csv = csv.writer(f)
                f_csv.writerow([fundCode, fundName])
            self.myselfSelectFundDict[fundCode] = fundName
