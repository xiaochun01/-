import requests
import re
import jsonpath
import json
from utils.check_utils import CheckUtils
from utils.config_utils import local_config
from requests.exceptions import RequestException,ProxyError,ConnectionError
from  nb_log import LogManager


logger = LogManager('p3p4_api_test').get_logger_and_add_handlers(is_add_stream_handler=True,log_filename=local_config.LOG_NAME)




class RequestsUtils:
    def __init__(self):
        self.hosts = local_config.HOSRTS
        self.session = requests.session()
        self.tmp_variables = {}

    def __get(self,requests_info):
        try:
            url = self.hosts+requests_info['请求地址']
            variables_list = re.findall('\\${\w+}',requests_info['请求参数(get)'])
            for variable in variables_list:
                requests_info['请求参数(get)'] = requests_info['请求参数(get)'].\
                    replace(variable,'"s"'%self.stm_valueables[variable[2:-1]])


            response =self.session.get(
                url = url,
                params= json.loads(requests_info['请求参数(get)']),
                headers = requests_info['请求头部信息']
            )
            response.encoding= response.apparent_encoding



            if requests_info['取值方式'] == 'jsonpath取值':
                value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
                self.tmp_variables[requests_info['取值变量']]    =  value
            elif requests_info['取值方式'] == '正则取值':
                value = re.findall(requests_info['取值代码'],response.text)[0]
                self.tmp_variables[requests_info['取值变量']]    =  value
            result = CheckUtils(response).run_check(requests_info['断言类型'], requests_info['期望结果'])


        except ProxyError as e:
            result = {'code':3,'message':'接口调用[%s]时发生代理异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s' % (requests_info['接口名称'], e.__str__()))
        except ConnectionError as e:
            result = {'code':3,'message':'接口调用[%s]时发生代理异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s' % (requests_info['接口名称'], e.__str__()))

        except RequestException as e:
            result = {'code':3,'message':'接口调用[%s]时发生代理异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s' % (requests_info['接口名称'], e.__str__()))

        except Exception as e:
            result = {'code':3,'message':'接口调用[%s]时发生代理异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s' % (requests_info['接口名称'], e.__str__()))


        return result



    def __post(self,requests_info):
        try:
            url = self.hosts+requests_info['请求地址']
            get_variable_list = re.findall('\\${\w+}', requests_info['请求参数(get)'])
            for variable in get_variable_list:
                requests_info['请求参数(get)'] = requests_info['请求参数(get)'].replace(variable,
                                            '"%s"'%self.tmp_variables[variable[2:-1]])


            post_variable_list = re.findall('\\${\w+}', requests_info['请求参数(post)'])

            for post_variable_list in post_variable_list:
                requests_info['请求参数(post)'] = requests_info['请求参数(post)'].replace(post_variable_list,
                                                '"%s"'%self.tmp_variables[post_variable_list[2:-1]])




            response = self.session.post(url=url,
                                         headers=requests_info['请求头部信息'],
                                         params=json.loads(requests_info['请求参数(get)']),
                                         json = json.loads(requests_info['请求参数(post)']),
                                         data=json.dumps(json.loads(requests_info['请求参数(post)']),ensure_ascii=False).encode('utf-8')
                                        )

            response.encoding= response.apparent_encoding
            if requests_info['取值方式'] == 'jsonpath取值':
                value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
                self.tmp_variables[requests_info['取值变量']] = value
            elif requests_info['取值方式'] == '正则取值':
                value = re.findall(requests_info['取值代码'],response.text)[0]
                self.tmp_variables[requests_info['取值变量']]    =  value

            result = CheckUtils(response).run_check(requests_info['断言类型'], requests_info['期望结果'])

        except ProxyError as e:
            result = {'code':3,'message':'接口调用[%s]时发生代理异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s'%(requests_info['接口名称'],e.__str__()))

        except ConnectionError as e:
            result = {'code':3,'message':'接口调用[%s]时发生连接异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s' % (requests_info['接口名称'], e.__str__()))

        except RequestException as e:
            result = {'code':3,'message':'接口调用[%s]时发生代理异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s'%(requests_info['接口名称'],e.__str__()))

        except Exception as e:
            result = {'code':3,'message':'接口调用[%s]时发生代理异常，异常为%s'%(requests_info['接口名称'],e.__str__()),'check_result':'False'}
            logger.error('调用接口%s时发生异常，异常原因%s'%(requests_info['接口名称'],e.__str__()))

        return result

    def request(self,step_info):
        request_type = step_info['请求方式']
        logger.info('%s开始调用'%step_info['接口名称'])
        if  request_type  == 'get':
            result = self.__get(step_info)
        elif request_type == 'post':
            result = self.__post(step_info)
        else:
            result = {'code':2,'result':'请求方式不支持'}
            logger.error('%s 调用时%s'%(step_info['接口名称']),result['message'])
        logger.info('%s 调用结束'%step_info['接口名称'])

        return result

    def request_by_step(self,test_steps):
        for test_step in test_steps:
            result = self.request(test_step)
            if result['code'] != 0 :
                break
        return result









# 39_bG2wT9khjJhuReG1_mf5tHvMxrXYfN_lQoH7bYyAKA9_qY3XbUm3jtSQnsahS2vZueHu9E80_QtKNuoDgjkFmi1DH_M6h5cea8F3nuzQXNBV4pHjx9Otyj_LlWmma5HyGPzxncoCtd3P_tQ2FJJbACAYCC


if __name__ == "__main__":
    # tmp_list= {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01',
    #   '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token',
    #   '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
    #   '请求参数(post)': '', '取值方式': 'jsonpath取值', '取值代码': '$.access_token', '取值变量': ''}
    # # tmp_list = {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":"39_bG2wT9khjJhuReG1_mf5tHvMxrXYfN_lQoH7bYyAKA9_qY3XbUm3jtSQnsahS2vZueHu9E80_QtKNuoDgjkFmi1DH_M6h5cea8F3nuzQXNBV4pHjx9Otyj_LlWmma5HyGPzxncoCtd3P_tQ2FJJbACAYCC"}', '请求参数(post)': '{   "tag" : {     "name" : "广东007" } } ', '取值方式': '正则取值', '取值代码': '', '取值变量': ''}
    requestsUtils = RequestsUtils()
    # a= requestsUtils.request(tmp_list)
    step_list =[{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': '', '取值方式': '正则取值', '取值代码': '"access_token":"(.+?)"', '取值变量': 'token', '断言类型': 'json_key_value', '期望结果': '{"expires_in":7200}'}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '请求参数(post)': '{   "tag" : {     "name" : "关东12nkjk" } } ', '取值方式': '无', '取值代码': '', '取值变量': '', '断言类型': 'json_key', '期望结果': 'tag'}]
    a = requestsUtils.request_by_step(step_list)
    print(a)
