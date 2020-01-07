import time

import unittest
# from BeautifulReport import BeautifulReport
from trademng_page.login_page import LoginPage
from trademng_page.union_query_page import UnionQuery
from common.driver_type import DriverType
from test_utils.log import TestLog

log = TestLog().get_log()


class TestUnionQuery(unittest.TestCase):
    '''测试联合查询'''

    def setUp(self):
        self.driver = DriverType().get_url()
        self.p = UnionQuery(self.driver)
        self.p2 = LoginPage(self.driver)
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

    def test001(self):
        self.p2.login_to_system()
        self.result = self.p.test_union_query("全部", "2020-01-03 01:30:14", "2020-01-06 23:30:14",
                                              "交易凭证号", "101157829023092808873")
        print(self.result)
        #self.assertEqual(self.result[0], "101157829023092808873")

    def test002(self):
        self.result = self.p.test_union_query("全部", "2020-01-01 15:30:14", "2020-01-06 15:30:14",
                                              "交易凭证号", "123123")
        #self.assertEqual(self.result[1], "无符合条件记录")


if __name__ == "__main__":
    unittest.main(verbosity=2)
