# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;

import time, requests
from tomorrow import threads


@threads(5)  # 使用装饰器，这个函数异步执行
def download(url):
    return requests.get(url)


def main():
    start = time.time()
    urls = [
        'https://pypi.org/project/tomorrow/0.2.0/',
        'https://www.cnblogs.com/pyld/p/4716744.html',
        'http://www.xicidaili.com/nn/10',
        'http://baidu.com',
        'http://www.bubuko.com/infodetail-1028793.html?yyue=a21bo.50862.201879',
    ]
    responses = [download(i) for i in urls]
    end = time.time()
    print("Time: %f seconds" % (end - start))


if __name__ == "__main__":
    main()