'''


'''
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from trademng_page.login_page import LoginPage


class UnionQuery(BasePage):


    # 查询管理
    loc_query_manage_a = (By.XPATH, "//a[contains(.'查询管理')]")
    # 联合查询
    loc_union_query_a = (By.XPATH, "//a[contains(.'联合查询')]")
    # 查询定义
    loc_defineId_select = (By.ID, "defineId")
    # 订单提交时间-开始时间
    loc_startTime_input = ("id", "startTime")
    # 订单提交时间-结束时间
    loc_endTime_input = ("id", "endTime")
    # 订单号类型
    loc_orderType_select = (By.ID, "orderType")
    # 订单号
    loc_orderNo_input = (By.ID, "partnerId")
    # 查询
    loc_query_btn = (By.ID, "btn-query")
    # 重置
    loc_reset_btn = (By.ID, "btn-reset")
    # 查询有结果
    loc_result_table = (By.XPATH, "")
    # 查询无结果提示
    loc_no_result_div = (By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div/div")
    # iframe
    loc_iframe = "iframe_848402AF9224068AE0530A07FF0A5102"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def test_union_query(self, query_define, start_time, end_time, order_type, order_no):
        # 点击查询管理
        self.click_element(self.loc_query_manage_a, '点击查询管理')
        # 点击联合查询
        self.click_element(self.loc_union_query_a, '点击联合查询')
        # 切换iframe
        self.switch_iframe(self.loc_iframe)
        # 下拉框选择查询定义
        self.select_element(self.loc_defineId_select, query_define, '下拉框选择查询定义')
        # 输入订单提交开始时间
        self.input_time_readonly(self.loc_startTime_input, start_time, '输入订单提交开始时间')
        # 输入订单提交结束时间
        self.input_time_readonly(self.loc_endTime_input, end_time, '输入订单提交结束时间')
        # 输入订单号类型
        self.select_element(self.loc_orderType_select, order_type, '输入订单号类型')
        # 输入订单号
        self.input_text(self.loc_orderNo_input, order_no, '输入订单号')
        # 单击查询
        self.click_element(self.loc_query_btn, '单击查询')
        # 断言查询结果
        return self.find_elem(self.loc_result_table, '查询有结果'), \
               self.find_elem(self.loc_no_result_div, '查询无结果提示')


if __name__=="__main__":
    p = UnionQuery()
    p.test_union_query("全部", "", "", "")