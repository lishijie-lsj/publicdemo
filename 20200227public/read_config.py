import yaml


class ReadConfig:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            # 避免报警告需要加入：Loader=yaml.FullLoader
            my_dict = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            print(my_dict, type(my_dict))

    def write_yaml(self):
        with open(self.yaml_file, encoding='utf-8', mode='w') as f:
            data = "学习2: {name: lsj,age: 18}"
            # 有中文时避免写入unicode文字：allow_unicode=True
            yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    rc = ReadConfig('config.yaml')
    rc.write_yaml()
    # rc.read_yaml()
# 学习:
#   - name: lsj
#   - age: 18
#
# 学习2: {name: lsj,age: 18}

# {'学习': [{'name': 'lsj'}, {'age': 18}], '学习2': {'name': 'lsj', 'age': 18}} <class 'dict'>

# -
#   学习:
#     name: lsj
#     age: 18
# -
#   学习2: {name: lsj,age: 18}
# [{'学习': {'name': 'lsj', 'age': 18}}, {'学习2': {'name': 'lsj', 'age': 18}}] <class 'list'>
