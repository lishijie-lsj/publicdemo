# unittest里的DDT
# pytest里的parameters
import json
import unittest
import ddt
import requests

@ddt
class test_inter(unittest.TestCase):
    @ddt.file_data('config.yaml')
    def tets_01_get_token(self, **kwargs):
        # list of dict 字典列表
        print(kwargs, type(kwargs))
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        params = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }
        headers = {
            "Accept": "*/*",
            "Conten-Type": "application/json"
        }
        rep = requests.get(url=url, params=params, headers=headers)
        print(rep.text)
        result_dict = json.loads(rep.text)
        # 预期结果
        # 'assert':{'eq':{'expires_in':7200}}
        self.assertEqual(kwargs['assert']['eq']['expires_in'],result_dict)


if __name__ == '__main__':
    # Inter.tets_01_get_token()
    unittest.main()
