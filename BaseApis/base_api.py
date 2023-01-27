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
        # ��ȡ corp_info ��yaml����
        yaml_data = FileTool.read_yaml("corp_info")
        # ��ȡ corpid �� corpsecret
        corpid = yaml_data.get("corp_info").get("corp_id")
        corpsecret = yaml_data.get("corp_info").get("corpsecret")
        self.get_access_token(corpid, corpsecret)

    def send(self, method, url, **kwargs):
        """
        ��������ʹ���Ǹ�����ȥ����ɱ��滻
        :return:
        """
        # ����requests���߷���ӿ�����
        url = self.BaseUrl + url
        logger.info(f"�ӿ���������������urlΪ��{url}")
        logger.info(f"�ӿ��������������Ĳ���Ϊ��{kwargs}")
        logger.info(f"�ӿ���������������paramsΪ��{kwargs.get('params')}")
        res = requests.request(method=method, url=url, **kwargs)
        logger.info(f"�ӿ�����󣬷��صĲ���Ϊ��{res.text}")
        return res

    def my_jsonpath(self, json_obj, expr):
        return jsonpath.jsonpath(json_obj, expr)

    def get_union_id(self):
        return str(uuid.uuid4()).split("-")[0]

    def get_access_token(self, corpid, corpsecret):
        """
        ��ȡaccess_token
        :return:
        """
        # �ӽӿڵ��õ�ʱ���� ��ȡtoken�Ĳ���
        corpid = corpid
        corpsecret = corpsecret

        url = "/gettoken"

        # �����������
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # �� get ����
        r = self.send("GET", url, params=params)
        # ��ӡ��Ӧ
        print(r.json())

        access_token = r.json()['access_token']
        self.access_token = access_token
