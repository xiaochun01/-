import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import shutil
import unittest
from utils import HTMLTestReportCN
from utils.config_utils import local_config
from  nb_log import LogManager
from utils.email_utils import EmailUtils

logger = LogManager('p3p4_api_test').get_logger_and_add_handlers(is_add_stream_handler=True,log_filename=local_config.LOG_NAME)



current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path,'../testcases')
result_path = os.path.join(current_path,'../%s'%local_config.REPORT_PATH)

def load_testcase():
    logger.info('加载接口测试用例')
    discover = unittest.defaultTestLoader.discover(
        start_dir=case_path,
        pattern='test_api_case.py'

    )

    all_case_suite = unittest.TestSuite()
    all_case_suite.addTest(discover)
    return all_case_suite


result_dir = HTMLTestReportCN.ReportDirectory(result_path)
result_dir.create_dir('接口自动化测试报告')
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
report_html_obj = open(report_html_path,"wb" )
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=report_html_obj,
    title='接口口自动化测试报告',
    description='数据驱动+关键字驱动测试框架',
    tester='扣你鸡娃'
)
logger.info('接口自动化测试开始执行')
runner.run(load_testcase())
report_html_obj.close()
# email_u = EmailUtils('test使用',report_html_path )
# email_u.send_mail()
# os.system('copy -f %s D:/jenkins/workspace/p3p4_demo01/接口自动化报告.html'%report_html_path)
# os.system('copy -f %s %s/接口自动化报告.html'%(report_html_path,sys.argv[1]))
shutil.copyfile(report_html_path,'%s/接口自动化报告.html'%sys.argv[1])
