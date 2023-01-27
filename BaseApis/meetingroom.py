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
        创建会议
        :return:
        """
        # 新建会议的url
        create_url = "/oa/meetingroom/add"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 调用base 封装的 send 发起请求
        r = self.send("POST", create_url, json=data, params=parms)
        # 将返回的响应返回出去
        return r

    def delete(self, data):
        """
        删除会议
        :return:
        """
        # 删除会议的url
        delete_url = "/oa/meetingroom/del"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 调用base 封装的 send 发起请求
        r = self.send("POST", delete_url, json=data, params=parms)
        # 将返回的响应返回出去
        return r

    def update(self, data):
        """
        修改会议
        :return:
        """
        # 更新会议的url
        update_url = "/oa/meetingroom/edit"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 调用base 封装的 send 发起请求
        r = self.send("POST", update_url, json=data, params=parms)
        # 将返回的响应返回出去
        return r

    def search(self):
        """
        查询会议
        :return:
        """
        # 发起查询的url
        search_url = "/oa/meetingroom/list"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 调用base 封装的 send 发起请求
        r = self.send("POST", search_url, params=parms)
        # 将返回的响应返回出去
        return r

    def search_meetingroom_list(self):
        """
        查询会议列表id
        :return:
        """
        # 调用查询接口
        r = self.search()
        # 拼接jsonpath 用到的 参数
        json_obj = r.json()
        expr = "$..meetingroom_id"
        # 使用封装的jsonpath进行json数据的匹配
        meetingid_list = self.my_jsonpath(json_obj, expr)
        # 将查询到的数据返回出去
        return meetingid_list

    def is_in_meetingroom_list(self, meetingroom_id):
        """
        是否在会议列表中
        :return:
        """
        # 调用查询接口
        r = self.search()
        # 拼接jsonpath 用到的 参数
        json_obj = r.json()
        expr = "$..meetingroom_id"
        # 使用封装的jsonpath进行json数据的匹配
        flag = self.my_jsonpath(json_obj, expr)
        # 如果没有匹配到数据就直接返回false
        if flag:
            # 有数据的话，使用meetingroom_id进行列表的数据判断
            if meetingroom_id in flag:
                return True
            else:
                return False
        else:
            return False
