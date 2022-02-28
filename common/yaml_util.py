import os
import yaml

# 获取项目的根目录
def get_obj_path():
    # D:\MyAll\pycharmprojecket\publicdemo\
    return os.path.dirname(__file__).split('common')[0]


# 读取yaml,需要安装pip install pyyaml
def read_yaml(yamlpath):
    # 'yaml文件的路径'
    with open(get_obj_path() + yamlpath, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    print(read_yaml('testcases/yaml/get_token.yaml'))
