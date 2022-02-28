import pytest

from common.common_util import CommonUtil
from common.yaml_util import read_yaml


class TestApi(CommonUtil):

    def test_01_get_token(self, db):
        print("获取接口统一的鉴权码" + db)
        flag = True
        # assert flag is True

    @pytest.mark.parametrize('caseinfo', ['01', '02', '乌拉'])
    def test_02_kaicixn(self, caseinfo):
        print('tset:' + caseinfo)

    @pytest.mark.parametrize('arg1,arg2', [['name', 'bali'], ['age', '18']])
    def test_02_kaicixn(self, arg1, arg2):
        print('test:' + str(arg1),str(arg2))

    @pytest.mark.parametrize('caseinfo',read_yaml('testcases/yaml/get_token.yaml'))
    def test_01_get_hotcity(self,caseinfo):
        print("获取接口统一的鉴权码")
        print(caseinfo)
        print(caseinfo['name'])
        print(caseinfo['request']['method'])
        print(caseinfo['request']['url'])
        print(caseinfo['request']['data'])
        print(caseinfo['validate'])
