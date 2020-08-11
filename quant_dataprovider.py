# -*- coding: utf-8 -*-
# python 3.x
import requests
import json


class QuantDataProviderOptions:

    def __init__(self):
        self.api_host = 'dataprovider.quant.dachengtech.cn'
        self.api_port = 9003
        self.api_prefix = '/api/dataprovider'
        self.timeout = 10
        self.conn_pool_initial_size = 1
        self.conn_pool_maxsize = 10
        self.max_retries = 1


class QuantDataProvider():

    def __init__(self, options):
        self.options = options
        self.session = requests.Session()
        self.session.mount('http://', requests.adapters.HTTPAdapter(
            pool_connections=options.conn_pool_initial_size,
            pool_maxsize=options.conn_pool_maxsize,
            max_retries=options.max_retries)
                           )

    def gen_target_url(self, endpoint):
        target_url = 'http://' + self.options.api_host + ':' + str(
            self.options.api_port) + self.options.api_prefix + endpoint
        return target_url

    def get_stock_list(self, page, size):
        url = self.gen_target_url('/stock/name/招商银行')
        # 请求参数
        data = {'page': page, 'size': size}
        # 执行请求
        response = self.session.get(url, params=data, timeout=self.options.timeout)
        # 查看执行的url
        print('\n查看请求执行的url:\n', response.url)
        # 获得请求的内容
        print('\n获得请求的内容:\n', response.text)
        # 解析获取的json数据
        # data_json = json.loads(response.text)
        # print('\n解析获取json中data的值:\n', data_json['data'])

    def get_stock_by_name(self, name):
        url = self.gen_target_url('/stock/name/' + name)
        # 请求参数
        data = {}
        # 执行请求
        response = self.session.get(url, params=data, timeout=self.options.timeout)
        # 查看执行的url
        print('\n查看请求执行的url:\n', response.url)
        # 获得请求的内容
        print('\n获得请求的内容:\n', response.text)
        # 解析获取的json数据
        data_json = json.loads(response.text)
        #print('\n解析获取json中data的值:\n', data_json.length())
        return data_json

    def get_stock_by_code(self, code):
        url = self.gen_target_url('/stock/code/' + code)
        # 请求参数
        data = {}
        # 执行请求
        response = self.session.get(url, params=data, timeout=self.options.timeout)
        # 查看执行的url
        print('\n查看请求执行的url:\n', response.url)
        # 获得请求的内容
        print('\n获得请求的内容:\n', response.text)
        # 解析获取的json数据
        data_json = json.loads(response.text)
        #print('\n解析获取json中data的值:\n', data_json.length())
        return data_json
