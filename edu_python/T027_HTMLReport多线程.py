import HTMLReport
import unittest
import os, time, sys

# sys.path.append()增加模块查找路径相当于环境变量

# 测试用例文件路径
# test_dir = os.path.join(os.getcwd(), 'edu_python')
test_dir = "./"  # 当前文件夹
discover = unittest.defaultTestLoader.discover(test_dir, pattern='T000*.py')
print('discover', discover)

# 测试报告文件路径
# 文件地址必须是同级或者是下一级
report_path = r'D:\autotest001\report'
report_time = time.strftime("%Y_%m_%d_%H_%M_%S_")
report_name = report_time + "report"


def run():
    runner = HTMLReport.TestRunner(title="测试报告", description='测试deafult报告', output_path=report_path,
                                   report_file_name=report_name, thread_count=6)
    runner.run(discover)


if __name__ == '__main__':
    run()


'''
多线程是模块级别的，即每个线程执行一个模块，适合执行接口测试用例，如果要UI测试的话，还需要分布式
'''
