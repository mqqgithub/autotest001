import unittest
import os, time
from BeautifulReport import BeautifulReport

# 测试用例文件路径
test_dir = os.path.join(os.getcwd(), 'trademng_page_test')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
print('descover  ', discover)

# 测试报告文件路径
report_path = os.path.join(os.getcwd(), 'report_file')
report_time = time.strftime("%Y_%m_%d_%H_%M_%S_")
report_name = report_time + "report.html"
# fp = open(report_name, 'wb')
# 调用HTMLTestRunner


def run():
    result = BeautifulReport(discover)
    result.report(filename=report_name, description='测试deafult报告',
                  report_dir=report_path, theme='theme_default')


if __name__ == '__main__':
    run()

