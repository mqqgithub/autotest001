import os
import sys
import unittest
# 表示导入当前路径的上层目录到搜索路径中

sys.path.append('..')
class runTest():
    def run(self, name):
        if name == u"全部":
            dir = os.path.join(os.path.dirname(os.getcwd()), "trademng_page_test")
            print(dir)
            discover = unittest.defaultTestLoader.discover(dir, '*test.py')
            runner = unittest.TextTestRunner()
            runner.run(discover)
        elif name == u"登录":
            dir = os.path.join(os.path.dirname(os.getcwd()), "trademng_page_test")
            print(dir)
            discover = unittest.defaultTestLoader.discover(dir, 'login_test.py')
            runner = unittest.TextTestRunner()
            runner.run(discover)



if __name__=="__main__":
    t = runTest()
    t.run("全部")
