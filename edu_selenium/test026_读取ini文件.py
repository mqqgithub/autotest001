# 功能描述：读取配置文件
# 开发人员：
# 开发时间：
# 参数说明;

import configparser


def get_conf(para1, para2):
    conf = configparser.ConfigParser()
    conf.read("test026.ini", encoding='GB18030')
    # host = conf["host"]
    # print(host)  # Section
    return conf[para1][para2]


if __name__ == "__main__":
    host1 = get_conf('host', 'host1')
    user = get_conf('MysqlDB', 'user')
    print(host1)
    print(user)



