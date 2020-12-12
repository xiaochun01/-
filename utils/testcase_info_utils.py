
import os
from utils.excel_utils import ExcelUtils


excel_file_path = os.path.join(os.path.dirname(__file__),'../data/testcase_infos.xlsx')






class TestcaseDataUtils():
    def __init__(self):
        self.excel_data = ExcelUtils(excel_file_path,'Sheet1')

    def convert_testcase_data(self):
        '''把excel转换为业务数据'''
        testcase_dict = {}
        for row_dara in self.excel_data.get_all_data():
            if row_dara['用例执行'] == '是':
                testcase_dict.setdefault(row_dara['测试用例编号'],[]).append(row_dara)
        return testcase_dict



    def convert_testcase_data_to_list(self):
        testcase_data= self.convert_testcase_data()
        testcase_data_list = []
        for k,v in testcase_data.items():
            testcase_data_row_dict = {}
            testcase_data_row_dict['case_id'] = k
            testcase_data_row_dict['case_step'] = v
            testcase_data_list.append(testcase_data_row_dict)

        return testcase_data_list

if __name__ == "__main__":

    a=TestcaseDataUtils().convert_testcase_data_to_list()
    for a in a:
        print(a)