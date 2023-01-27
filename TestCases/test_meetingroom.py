# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import allure
import pytest
from BaseApis.meetingroom import MeetingRoom


@allure.feature("企业微信会议管理测试")
class TestMeetingRoom:

    def setup_class(self):
        self.MeetingRoom = MeetingRoom()

    @allure.story("成功创建会议")
    @pytest.mark.parametrize("name", ["南京研发会议", "上海研发会议", "杭州研发会议"])
    def test_create_success(self, name):
        with allure.step("拼接_id"):
            # 获取唯一名称的拼接
            _id = self.MeetingRoom.get_union_id()
        with allure.step("组装数据"):
            # 组装发起新建的数据
            data = {
                "name": f"{name}_{_id}",
                "capacity": 8,
                "equipment": [1, 2, 3]
            }
        with allure.step("发起新建会议请求"):
            r = self.MeetingRoom.create(data=data)
        with allure.step("断言创建的数据是不是在列表中"):
            assert self.MeetingRoom.is_in_meetingroom_list(r.json().get("meetingroom_id"))

    @allure.story("创建会议失败")
    @pytest.mark.parametrize("name,expect", [("", 40058), ("南京研发会议南京研发会议南京研发会议南京研发会议南京研发会议南", 40058)])
    def test_create_fail(self, name, expect):
        # 获取唯一名称的拼接
        _id = self.MeetingRoom.get_union_id()
        # 组装发起新建的数据
        data = {
            "name": f"{name}_{_id}" if name else "",
            "capacity": 8,
            "equipment": [1, 2, 3]
        }
        r = self.MeetingRoom.create(data=data)
        assert r.json().get("errcode") == expect

    @allure.story("成功删除会议")
    def test_delete_success(self):
        with allure.step("查询会议id"):
            meetingid_list = self.MeetingRoom.search_meetingroom_list()
        with allure.step("发起删除会议请求"):
            for meetingid_list in meetingid_list:
                # 组装发起删除的数据
                data = {
                    "meetingroom_id": meetingid_list
                }
                r = self.MeetingRoom.delete(data)
        with allure.step("断言查询数据是否为空"):
            assert not self.MeetingRoom.is_in_meetingroom_list("1")
