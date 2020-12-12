import  pymysql

class MysqlUtils:
    def __init__(self):
        self.conn = pymysql.connect(
        host = '127.0.0.1',
        port= 3306,
        user = 'root',
        password='',
        database='interface_test_db',
        charset= 'utf8'
        )
        self.cousor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_cases_info(self):
        sql_str = '''
        select  case_info.case_id as '测试用例编号',case_info.case_name as '测试用例名称',case_info.is_run as '用例执行',case_step_info.case_step_id as '用例步骤', requests_info.requests_name  as '接口名称', requests_info.requests_type as '请求方式', requests_info.requests_header as '请求头部信息',requests_info.requests_url as '请求地址',requests_info.requests_url_params as '请求参数(get)',requests_info.requests_post_data as '请求参数(post)',case_step_info.get_value_type as '取值方式',case_step_info.get_value_code as '取值代码', case_step_info.get_value_variable as '取值变量',case_step_info.excepted_result_type as '断言类型',case_step_info.excepted_result as '期望结果'
        from case_info,case_step_info,requests_info 
        where case_info.case_id = case_step_info.case_id and case_step_info.requests_id = requests_info.requests_id and case_info.is_run = '是'
        order by case_info.case_id,case_step_info.case_step_id;
        '''
        self.cousor.execute(sql_str)
        cases_list = self.cousor.fetchall()
        self.cousor.close()
        self.conn.close()
        return cases_list

if __name__ == '__main__':
    pymysqldata = MysqlUtils()
    for i in pymysqldata.get_cases_info():
        print(i)