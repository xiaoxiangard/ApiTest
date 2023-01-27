# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import allure
import pytest
from BaseApis.meetingroom import MeetingRoom


@allure.feature("��ҵ΢�Ż���������")
class TestMeetingRoom:

    def setup_class(self):
        self.MeetingRoom = MeetingRoom()

    @allure.story("�ɹ���������")
    @pytest.mark.parametrize("name", ["�Ͼ��з�����", "�Ϻ��з�����", "�����з�����"])
    def test_create_success(self, name):
        with allure.step("ƴ��_id"):
            # ��ȡΨһ���Ƶ�ƴ��
            _id = self.MeetingRoom.get_union_id()
        with allure.step("��װ����"):
            # ��װ�����½�������
            data = {
                "name": f"{name}_{_id}",
                "capacity": 8,
                "equipment": [1, 2, 3]
            }
        with allure.step("�����½���������"):
            r = self.MeetingRoom.create(data=data)
        with allure.step("���Դ����������ǲ������б���"):
            assert self.MeetingRoom.is_in_meetingroom_list(r.json().get("meetingroom_id"))

    @allure.story("��������ʧ��")
    @pytest.mark.parametrize("name,expect", [("", 40058), ("�Ͼ��з������Ͼ��з������Ͼ��з������Ͼ��з������Ͼ��з�������", 40058)])
    def test_create_fail(self, name, expect):
        # ��ȡΨһ���Ƶ�ƴ��
        _id = self.MeetingRoom.get_union_id()
        # ��װ�����½�������
        data = {
            "name": f"{name}_{_id}" if name else "",
            "capacity": 8,
            "equipment": [1, 2, 3]
        }
        r = self.MeetingRoom.create(data=data)
        assert r.json().get("errcode") == expect

    @allure.story("�ɹ�ɾ������")
    def test_delete_success(self):
        with allure.step("��ѯ����id"):
            meetingid_list = self.MeetingRoom.search_meetingroom_list()
        with allure.step("����ɾ����������"):
            for meetingid_list in meetingid_list:
                # ��װ����ɾ��������
                data = {
                    "meetingroom_id": meetingid_list
                }
                r = self.MeetingRoom.delete(data)
        with allure.step("���Բ�ѯ�����Ƿ�Ϊ��"):
            assert not self.MeetingRoom.is_in_meetingroom_list("1")
