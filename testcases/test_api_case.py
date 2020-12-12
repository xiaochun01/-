import os
import unittest
import warnings
import paramunittest
from utils.testcase_info_utils import TestcaseDataUtils
from utils.requests_utils import RequestsUtils
from  nb_log import LogManager
from utils.config_utils import local_config
from utils.mysql_utils import MysqlUtils


logger = LogManager('p3p4_api_test').get_logger_and_add_handlers(is_add_stream_handler=True,log_filename=local_config.LOG_NAME)


test_case_lists = TestcaseDataUtils().convert_testcase_data_to_list()
@paramunittest.parametrized(
    *test_case_lists
)

class TestApiCase(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)


    def setParameters(self, case_id, case_step):
        self.case_id = case_id
        self.case_step = case_step

    def test_api_case(self):
        logger.info('测试用例编号：%s开始执行'%self.case_step[0].get('测试用例编号'))
        self._testMethodName = self.case_step[0].get('测试用例编号')
        self._testMethodDoc = self.case_step[0].get('测试用例名称')
        test_result = RequestsUtils().request_by_step(self.case_step)
        logger.info('测试用例编号：%s执行结束'%self.case_step[0].get('测试用例编号'))

        self.assertTrue( test_result['check_result'],test_result['message'] )



if __name__ == '__main__':
    unittest.main(verbosity=2)

