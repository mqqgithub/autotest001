# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;

# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2016-7-27
@author: Jennifer
Project:使用unittest框架编写测试用例思路
'''
# 3.导入unittest模块
import unittest


# 4.定义测试类，父类为unittest.TestCase。
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法。
class Test(unittest.TestCase):

    # 5.定义setUp()方法用于测试用例执行前的初始化工作。
    # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    # 注意，输入的值为字符型的需要转为int型
    # @classmethod只执行一次
    @classmethod
    def setUp(self):
        print("test start!")
        self.number = 10


    # 6.定义测试用例，以“test_”开头命名的方法
    # 注意，方法的入参为self
    # 可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    # 可定义多个测试用例
    # 最重要的就是该部分
    def test_case1(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg='Your input is not 10')

    def test_case2(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg='Your input is not 20')

    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg='Your input is not 30')

    # 7.定义tearDown()方法用于测试用例执行之后的善后工作。
    # 注意，方法的入参为self
    def tearDown(self):
        print('Test over!')


# 8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__ == '__main__':
    # 8.1执行测试用例方案一如下：
    # unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
    # 执行顺序是命名顺序：先执行test_case1，再执行test_case2
    # verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
    # 0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
    # 1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
    # 2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
    # unittest.main(verbosity=2)


#8.2执行测试用例方案二如下：
#8.2.1先构造测试集
#8.2.1.1实例化测试套件
    suite = unittest.TestSuite()
#8.2.1.2将测试用例加载到测试套件中。
#执行顺序是安装加载顺序：先执行test_case2，再执行test_case1,Test('test_case2')=类名（方法名）
    suite.addTest(Test('test_case2'))
    suite.addTest(Test('test_case1'))
#8.2.2执行测试用例
#8.2.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(suite)


'''
#8.3执行测试用例方案三如下：
#8.3.1构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
#执行顺序同方案一：执行顺序是命名顺序：先执行test_case1，再执行test_case2
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    tip：discover是递归匹配文件的，如果设定的目录是测试用例的根目录的话，
    discover会去匹配每个子目录下的所有用例，匹配成功的用例就加载到discover，
    但是在这里需要注意一点，存放用例的目录属性必须是python package，必须要有__init__.py，不然不会获取成功。

#8.3.2执行测试用例
#8.3.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.3.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)   
'''
'''
测试固件可以分离出来
'''
from selenium import webdriver


class Test_Fixture(unittest):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()
