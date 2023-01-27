# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import uuid
import jsonpath
import requests
from Utils.log_util import logger
from Utils.file_tools import FileTool


class BaseApi:
    BaseUrl = "https://qyapi.weixin.qq.com/cgi-bin"

    def __init__(self):
        # 获取 corp_info 的yaml数据
        yaml_data = FileTool.read_yaml("corp_info")
        # 提取 corpid 和 corpsecret
        corpid = yaml_data.get("corp_info").get("corp_id")
        corpsecret = yaml_data.get("corp_info").get("corpsecret")
        self.get_access_token(corpid, corpsecret)

    def send(self, method, url, **kwargs):
        """
        发起请求，使用那个工具去发起可被替换
        :return:
        """
        # 调用requests工具发起接口请求
        url = self.BaseUrl + url
        logger.info(f"接口请求操作，请求的url为：{url}")
        logger.info(f"接口请求操作，请求的参数为：{kwargs}")
        logger.info(f"接口请求操作，请求的params为：{kwargs.get('params')}")
        res = requests.request(method=method, url=url, **kwargs)
        logger.info(f"接口请求后，返回的参数为：{res.text}")
        return res

    def my_jsonpath(self, json_obj, expr):
        return jsonpath.jsonpath(json_obj, expr)

    def get_union_id(self):
        return str(uuid.uuid4()).split("-")[0]

    def get_access_token(self, corpid, corpsecret):
        """
        获取access_token
        :return:
        """
        # 从接口调用的时候传入 获取token的参数
        corpid = corpid
        corpsecret = corpsecret

        url = "/gettoken"

        # 定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # 发 get 请求
        r = self.send("GET", url, params=params)
        # 打印响应
        print(r.json())

        access_token = r.json()['access_token']
        self.access_token = access_token
