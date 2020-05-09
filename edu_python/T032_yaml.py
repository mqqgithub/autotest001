import yaml


# 读取yaml文件
with open(r"T032_yaml.yaml", encoding='utf-8') as file:
    data = yaml.full_load(file)
    print(data)


