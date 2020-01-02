'''


'''
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class UnionQuery(BasePage):

    def __init__(self):
        # 查询管理
        self.loc_query_manage_a = (By.XPATH, "//a[contains(.'查询管理')]")
        # 联合查询
        self.loc_union_query_a = (By.XPATH, "//a[contains(.'联合查询')]")
        # 查询定义
        self.loc_defineId_select = ()
        # 订单提交时间-开始时间
        self.loc_startTime_input = ()
        # 订单提交时间-结束时间
        self.loc_endTime_input = ()
        # 订单号类型
        self.loc_orderType_select = ()
        # 订单号
        self.loc_orderNo_input = ()
        # 查询
        self.loc_query_btn = ()
        # 重置
        self.loc_reset_btn = ()
        # 查询有结果
        self.loc_result_table = ()
        # 查询无结果提示
        self.loc_no_result_div = ()

    def test_union_query(self, query_define, start_time, end_time, order_type, order_no):

        # 点击查询管理
        self.click_element(self.loc_query_manage_a, '点击查询管理')
        # 点击联合查询
        self.click_element(self.loc_union_query_a, '点击联合查询')
        # 下拉框选择查询定义
        self.input_query_define_select(self.loc_defineId_select, query_define, '下拉框选择查询定义')
        # 输入订单提交开始时间
        self.input_time_readonly(self.loc_startTime_input, start_time, '输入订单提交开始时间')
        # 输入订单提交结束时间
        self.input_time_readonly(self.loc_endTime_input, end_time, '输入订单提交结束时间')
        # 输入订单号类型
        self.input_select(self.loc_orderType_select, order_type, '输入订单号类型')
        # 输入订单号
        self.input_text(self.loc_orderNo_input, order_no, '输入订单号')
        # 单击查询
        self.click_element(self.loc_query_btn, '单击查询')
        # 断言查询结果
        return self.find_elem(self.loc_result_table, '查询有结果'), self.find_elem(self.loc_no_result_div, '查询无结果提示')
