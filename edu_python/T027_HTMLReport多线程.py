import HTMLReport
import unittest
import os, time, sys

# sys.path.append()

# 测试用例文件路径
# test_dir = os.path.join(os.getcwd(), 'edu_python')
test_dir = "./"  # 当前文件夹
discover = unittest.defaultTestLoader.discover(test_dir, pattern='T000*.py')
print('discover', discover)

# 测试报告文件路径
# 文件地址必须是同级或者是下一级
report_path = 'D:\\autotest001'
report_time = time.strftime("%Y_%m_%d_%H_%M_%S_")
report_name = report_path+report_time + "report.html"


def run():
    runner = HTMLReport.TestRunner(title="测试报告", description='测试deafult报告', output_path=report_path,
                                   report_file_name=report_name, thread_count=2)
    runner.run(discover)


if __name__ == '__main__':
    run()



