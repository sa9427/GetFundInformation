import configparser


class Config():
    def CreateConfig(self):
        self.config = configparser.ConfigParser()
        self.config['data'] = dict()
        self.config['data']['fundListPath'] = 'data/fundList.feather'
        self.config['data']['myselfSelectFundPath'] = 'data/myselfSelectionFund.csv'

    def SaveConfig(self):
        with open('../config.ini', 'w+', encoding='utf-8') as f:
            self.config.write(f)

    @staticmethod
    def GetConfig():
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.sections()
        return config

if __name__ == "__main__":
    config = Config()
    config.CreateConfig()
    config.SaveConfig()

    config = Config.GetConfig()

    print(config)