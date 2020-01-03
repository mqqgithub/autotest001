import time

import unittest
from BeautifulReport import BeautifulReport

from trademng_page.union_query_page import UnionQuery
from test_utils.log import TestLog

log = TestLog().get_log()

class TestUnionQuery(unittest.TestCase):
    '''测试联合查询'''

    def setUp(self):
        self.p = UnionQuery()
        time.sleep(1)

    def tearDown(self):
        self.p.close()

    def test001(self):
        self.result = self.p.test_union_query("全部", "2020-01-03 01:30:14", "2020-01-01 23:30:14",
                                              "交易凭证号", "")
        self.assertEqual(self.result[0], "order_no")

    def test002(self):
        self.result = self.p.test_union_query("全部", "2019-12-27 15:30:14", "2019-12-28 15:30:14",
                                              "交易凭证号", "")
        self.assertEqual(self.result[1], "order_no")

