import pytest
import requests

from common.requests_util import RequestUtil
from common.yaml_util import read_yaml


class TestApi():
    # session可以自动cookie的关联
    session = requests.session()
    access_token = ""

    @pytest.mark.parametrize('caseinfo', read_yaml('testcases/yaml/get_token.yaml'))
    def test_01_get_token(self, caseinfo):
        print(caseinfo)
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method, url=url, params=data)
        result = res.json()
        TestApi.access_token = result['access_token']
        print(result)
        assert 'access_token' in result

    @pytest.mark.parametrize('caseinfo', read_yaml('testcases/yaml/edit_flag.yaml'))
    def test_02_edit_flag(self, caseinfo):
        print("编辑标签接口")
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url'] + TestApi.access_token
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method, url=url, json=data)
        result = res.json()
        print(result)
