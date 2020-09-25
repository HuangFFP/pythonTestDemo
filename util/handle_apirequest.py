# coding:utf-8
import sys
import os
import allure
import json

# sys.path.append('../')
# sys.path.append('C:/Users/huangfeipeng/PycharmProjects/demo')
curPath = os.path.abspath(os.path.dirname(__file__))
# BasePath = curPath[:curPath.find("demo\\") + len("demo\\")]
BasePath = os.path.abspath(os.path.join(os.getcwd()))
from base.base_request import baseRequest
from util.handle_log import run_log as logger


class ApiRequest:
    def api_request(self, base_url, test_case_data, case_data):
        get_name = None
        get_url = None
        get_method = None
        get_headers = None
        get_cookies = None
        get_case_name = None
        get_case_params = None
        response_data = None
        try:
            get_name = test_case_data['config']['name']
            get_url = base_url + test_case_data['config']['url']
            get_method = test_case_data['config']['method']
            get_headers = {"Content-Type":"application/json","userInfo": json.dumps({
                "orgId":"43bb32f248be4a4f80fdf6c0f4f79e8c",
                "orgName": "",
                "platformType": 0,
                "tenantId": "0529b6ce477e4f149eddd9f8faf5413d",
                "userId": "0730FEDEC1424BA3B47796D1EE63ECF5",
                "username": "ctadmin"
            })}
            get_cookies = test_case_data['config']['cookies']
        except Exception as e:
            logger.exception('获取用例基本信息失败，{}'.format(e))
        try:
            get_case_name = case_data['name']
            get_case_params = case_data['params']
        except Exception as e:
            logger.exception('获取测试用例信息失败，{}'.format(e))
        with allure.step("请求接口：%s,请求地址：%s,请求方法：%s,请求头：%s,请求Cookies：%s" % (
                get_name, get_url, get_method, get_headers, get_cookies)):
            allure.attach("接口用例描述：", "{0}".format(get_case_name))
            allure.attach("接口用例请求参数：", "{0}".format(get_case_params))
        logger.info(
            '请求接口名：%r，请求地址：%r，请求方法：%r，请求头：%r，请求Cookies：%r' % (get_name, get_url, get_method, get_headers, get_cookies))
        logger.info('请求接口名：%r，请求接口用例名：%r，接口用例请求参数：%r' % (get_name, get_case_name, get_case_params))
        try:
            response_data = baseRequest.run_main(get_method, get_url, get_case_params, get_headers)
        except Exception as e:
            logger.exception('用例请求返回失败，{}'.format(e))
        logger.info('请求接口名：%r，请求接口用例名：%r，返回参数：%r' % (get_name, get_case_name, response_data.json()))
        allure.attach("接口用例返回参数：", "{0}".format(response_data.json()))
        return response_data


apiRequest = ApiRequest()
