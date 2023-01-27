# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
from BaseApis.base_api import BaseApi


class MeetingRoom(BaseApi):

    def create(self, data):
        """
        ��������
        :return:
        """
        # �½������url
        create_url = "/oa/meetingroom/add"
        # ��ȡ access_token
        parms = {"access_token": self.access_token}
        # ����base ��װ�� send ��������
        r = self.send("POST", create_url, json=data, params=parms)
        # �����ص���Ӧ���س�ȥ
        return r

    def delete(self, data):
        """
        ɾ������
        :return:
        """
        # ɾ�������url
        delete_url = "/oa/meetingroom/del"
        # ��ȡ access_token
        parms = {"access_token": self.access_token}
        # ����base ��װ�� send ��������
        r = self.send("POST", delete_url, json=data, params=parms)
        # �����ص���Ӧ���س�ȥ
        return r

    def update(self, data):
        """
        �޸Ļ���
        :return:
        """
        # ���»����url
        update_url = "/oa/meetingroom/edit"
        # ��ȡ access_token
        parms = {"access_token": self.access_token}
        # ����base ��װ�� send ��������
        r = self.send("POST", update_url, json=data, params=parms)
        # �����ص���Ӧ���س�ȥ
        return r

    def search(self):
        """
        ��ѯ����
        :return:
        """
        # �����ѯ��url
        search_url = "/oa/meetingroom/list"
        # ��ȡ access_token
        parms = {"access_token": self.access_token}
        # ����base ��װ�� send ��������
        r = self.send("POST", search_url, params=parms)
        # �����ص���Ӧ���س�ȥ
        return r

    def search_meetingroom_list(self):
        """
        ��ѯ�����б�id
        :return:
        """
        # ���ò�ѯ�ӿ�
        r = self.search()
        # ƴ��jsonpath �õ��� ����
        json_obj = r.json()
        expr = "$..meetingroom_id"
        # ʹ�÷�װ��jsonpath����json���ݵ�ƥ��
        meetingid_list = self.my_jsonpath(json_obj, expr)
        # ����ѯ�������ݷ��س�ȥ
        return meetingid_list

    def is_in_meetingroom_list(self, meetingroom_id):
        """
        �Ƿ��ڻ����б���
        :return:
        """
        # ���ò�ѯ�ӿ�
        r = self.search()
        # ƴ��jsonpath �õ��� ����
        json_obj = r.json()
        expr = "$..meetingroom_id"
        # ʹ�÷�װ��jsonpath����json���ݵ�ƥ��
        flag = self.my_jsonpath(json_obj, expr)
        # ���û��ƥ�䵽���ݾ�ֱ�ӷ���false
        if flag:
            # �����ݵĻ���ʹ��meetingroom_id�����б�������ж�
            if meetingroom_id in flag:
                return True
            else:
                return False
        else:
            return False
