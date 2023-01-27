# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import os

import yaml


class FileTool:

    @classmethod
    def get_interface_dir(cls):
        # ��ȡapi_object���ļ���·��
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def read_yaml(cls, file_name):
        # ��ȡapi_object���ļ���·��
        _path = cls.get_interface_dir()
        # ƴ��yaml�ļ����ڵľ���·�� sep �൱�� win�� \ linux��/ sep.join ��Ҫ�Ĳ�����һ���б�
        yaml_file = os.sep.join([_path, "Data", file_name + ".yaml"])
        # �� yaml�ļ� ��ʹ��yaml.safe_load �����ݷ��س�ȥ
        with open(yaml_file, encoding="utf-8") as f:
            return yaml.safe_load(f)
