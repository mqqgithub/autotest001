# unittest

'''
unittest模块
    unittest.TestCase()类
        setUp()
        tearDown()
        assertEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，相等则测试用例通过。
        assertNotEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，不相等则测试用例通过。
        assertTrue(x，[msg='测试失败时打印的信息'])：断言x是否True，是True则测试用例通过。
        assertFalse(x，[msg='测试失败时打印的信息'])：断言x是否False，是False则测试用例通过。
        assertIs(a,b，[msg='测试失败时打印的信息']):断言a是否是b，是则测试用例通过。
        assertNotIs(a,b，[msg='测试失败时打印的信息']):断言a是否是b，不是则测试用例通过。
        assertIsNone(x，[msg='测试失败时打印的信息'])：断言x是否None，是None则测试用例通过。
        assertIsNotNone(x，[msg='测试失败时打印的信息'])：断言x是否None，不是None则测试用例通过。
        assertIn(a,b，[msg='测试失败时打印的信息'])：断言a是否在b中，在b中则测试用例通过。
        assertNotIn(a,b，[msg='测试失败时打印的信息'])：断言a是否在b中，不在b中则测试用例通过。
        assertIsInstance(a,b，[msg='测试失败时打印的信息'])：断言a是是b的一个实例，是则测试用例通过。
        assertNotIsInstance(a,b，[msg='测试失败时打印的信息'])：断言a是是b的一个实例，不是则测试用例通过
    unittest.TestSuite()
        addTest(): addTest()方法是将测试用例添加到测试套件中
            suite = unittest.TestSuite()
            suite.addTest(test_baidu.BaiduTest('test_baidu'))
    unittest.TextTestRunner()
        unittest.TextRunner().run()
            runner = unittest.TextTestRunner()
            runner.run(suite)
    unittest.defaultTestLoader()
        unittest.defaultTestLoader().discover(test_dir, pattern='test_*.py')
        
    unittest.skip():装饰器，当运行用例时，有些用例可能不想执行等，可用装饰器暂时屏蔽该条测试用例。一种常见的用法就是比如说想调试某一个测试用例，想先屏蔽其他用例就可以用装饰器屏蔽。
        @unittest.skip(reason): skip(reason)装饰器：无条件跳过装饰的测试，并说明跳过测试的原因。
        @unittest.skipIf(reason): skipIf(condition,reason)装饰器：条件为真时，跳过装饰的测试，并说明跳过测试的原因。
        @unittest.skipUnless(reason): skipUnless(condition,reason)装饰器：条件为假时，跳过装饰的测试，并说明跳过测试的原因。
        @unittest.expectedFailure(): expectedFailure()测试标记为失败。
    
'''
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
    def setUp(self):
        print('test start...')
        # self.number = input('Enter a number:')
        # self.number = int(self.number)

    # 6.定义测试用例，以“test_”开头命名的方法
    # 注意，方法的入参为self
    # 可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    # 可定义多个测试用例
    # 最重要的就是该部分
    def test_case1(self):
        # print(self.number)
        # self.assertEqual(self.number, 10, msg='Your input is not 10')
        self.assertIn('abc', 'abcdefg')
        self.assertNotIn('abc', 'abcdefg')

    def test_case2(self):
        # print(self.number)
        # self.assertEqual(self.number, 20, msg='Your input is not 20')
        self.assertEqual('a', 'a')
        self.assertNotEqual('a', 'b')

    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg='Your input is not 30')

    # 7.定义tearDown()方法用于测试用例执行之后的善后工作。
    # 注意，方法的入参为self
    def tearDown(self):
        print('Test over')


# 8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__ == '__main__':
    # 8.1执行测试用例方案一如下：
    # unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
    # 执行顺序是命名顺序：先执行test_case1，再执行test_case2
    # verbosity=1 0 2输出错误测试报告的详细程度
    # 方法1
    # unittest.main(verbosity=2）
    # 方法2
    '''
    suite = unittest.TestSuite()
    suite.addTest(Test('test_case1'))
    suite.addTest(Test('test_case2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    # 方法3
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, 'test*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)


'''
#8.2执行测试用例方案二如下：
#8.2.1先构造测试集
#8.2.1.1实例化测试套件
    suite=unittest.TestSuite()
#8.2.1.2将测试用例加载到测试套件中。
#执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
    suite.addTest(Test('test_case2'))
    suite.addTest(Test('test_case1'))
#8.2.2执行测试用例
#8.2.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(suite)
'''

'''
#8.3执行测试用例方案三如下：
#8.3.1构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
#执行顺序同方案一：执行顺序是命名顺序：先执行test_case1，再执行test_case2
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#8.3.2执行测试用例
#8.3.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.3.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)   
    
'''