import pytest
from common.common_util import CommonUtil
from common.requests_util import RequestUtil
from common.yaml_util import read_yaml


class TestMashang(CommonUtil):

    @pytest.mark.parametrize('caseinfo',read_yaml('testcases/yaml/get_token.yaml'))
    def test_baili(self,caseinfo):
        print(caseinfo)
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method, url=url, params=data)
        result = res.json()
        RequestUtil.access_token = result['access_token']
        print(result)
        assert 'access_token' in result

