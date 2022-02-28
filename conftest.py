# 读取数据方法
import pytest


def read_yaml():
    return ['成龙', 'zhengzidan', 'cai10']


@pytest.fixture(scope="function", autouse=False, params=read_yaml(), ids=['a', 'b', 'c'], name='db')
def exe_database_sql(request):
    print(request.param)
    print("执行SQL查询")
    # return "success"
    yield request.param
    print("关闭数据库连接")

@pytest.fixture(scope="session",autouse=True,name='all')
def all_exe():
    print("all_exe之前")
    yield "登录成功"
    print("all_exe之后")
