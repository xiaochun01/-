import os
import configparser
import time


current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path,'../conf/localconfig.ini')

class ConfigUtils:
    def __init__(self,cfg_path= config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path,encoding='utf-8')
    @property
    def HOSRTS(self):
        hosts_value =self.cfg.get('default','hosts')
        return hosts_value
    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('path','REPORT_PATH')
        return report_path_value

    @property
    def LOG_NAME(self):
        log_name_value = '%s_%s'%(self.cfg.get('default','log_name'),time.strftime('%Y-%m-%d'))
        return log_name_value



local_config = ConfigUtils()

if __name__ == '__main__':
    print(local_config.LOG_NAME)