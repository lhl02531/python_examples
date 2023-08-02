# -*- coding: utf-8 -*-
"""
    :author: allen lv
    pytest fixture 参数传递
"""
import pytest

test_data = [{
    'case_name': '登录成功测试',
    'username': 'admin',
    'password': 'lv123'
},{
    'case_name': '登录失败测试',
    'username': 'admin',
    'password': 'lv1234444'
},{
    'case_name': '用户名为空',
    'username': 'admin',
    'password': 'lv1234444'
}]

@pytest.fixture(params=test_data)
def para_data(request):
    # request 是 pytest 内置 fixture, 名称不能更改

    return request.param


def test_case(para_data):
    # print(para_data)
    username = para_data.get('username')
    print(username)
    case_name = para_data.get('case_name')
    print(case_name)
    password = para_data.get('password')
    print(password)
