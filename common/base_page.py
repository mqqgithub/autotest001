# https://blog.csdn.net/qq_38741986/article/details/93237911
# https://testerhome.com/topics/19900
# driver作为类BasePage的一个属性
from common.driver_type import DriverType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from test_utils import config
from test_utils.log import TestLog

log = TestLog().get_log()


# 创建基础类
class BasePage(object):
    # 初始化
    def __init__(self):
        self.base_url = 'https://zui.kjtpay.com/window/login#'
        self.driver = DriverType().get_url()
        self.timeout = 30

    # 打开页面
    def _open(self):
        url = self.base_url
        self.driver.get(url)
        # self.driver.switch_to.frame('login_frame')  #切换到登录窗口的iframe

    def open(self):
        self._open()

    # 定位方法封装
    def find_ele(self, *loc):
        return self.driver.find_element(*loc)

    # 截图
    def save_img(self, img_name=None):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = config.Config.IMG_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        file_path = screenshot_path + '\\%s_%s.png' % (img_name, tm)

        try:
            self.driver.save_screenshot(file_path)
            log.info('截图成功，路径为{}'.format(file_path))
        except Exception as e:
            log.info('截图失败{}'.format(e))

    # 等待元素可见
    def wait_element_visible(self, loc, timeout=10, poll_frequency=0.5, img_name=None):
        """
            :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
            :param timeout:等待的上限
            :param poll_frequency:轮询频率
            :param img_name:等待失败时,截图操作,图片文件名描述
            :return:None
        """
        log.info('{}等待元素可见{}'.format(img_name, loc))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
            end = time.time()
            log.info('等待%.2f秒后元素可见' % (end - start))
        except Exception as e:
            log.info('{}等待元素可见失败{}'.format(img_name, loc))
            print(e)
            self.save_img(img_name)
            # raise

    # 等待元素不可见
    def wait_element_not_visible(self, loc, timeout=10, poll_frequency=0.5, img_name=None):
        """
            :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
            :param timeout:等待的上限
            :param poll_frequency:轮询频率
            :param img_name:等待失败时,截图操作,图片文件名描述
            :return:None
        """
        log.info('{}等待元素可见{}'.format(img_name, loc))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until_not(EC.visibility_of_element_located(loc))
            end = time.time()
            log.info('等待%.2f秒后元素不可见' % (end - start))
        except Exception as e:
            log.info('{}等待元素不可见失败{}'.format(img_name, loc))
            print(e)
            self.save_img(img_name)

    # 查找一个元素
    def find_elem(self, loc, img_name=None):
        log.info('{} 查找元素 {}'.format(img_name, loc))
        try:
            return self.driver.find_element(*loc)
        except Exception as e:
            log.info('查找元素失败.%s' % e)
            # 截图
            self.save_img(img_name)

    # 查找一组元素
    def find_elems(self, loc, img_name=None):
        log.info('{} 查找元素 {}'.format(img_name, loc))
        try:
            return self.driver.find_elements(*loc)
        except Exception as e:
            log.info('查找元素失败.%s' % e)
            # 截图
            self.save_img(img_name)

    # 输入文本操作
    def input_text(self, loc, text, img_name=None):
        # 查找元素
        ele = self.find_elem(loc, img_name)
        # 输入操作
        log.info('{} 在元素 {} 中输入文本: {}'.format(img_name, loc, text))
        try:
            ele.send_keys(text)
        except Exception as e:
            log.info(e)
            # 截图
            self.save_img()

    # 清除操作
    def clean_input_text(self, loc, img_name=None):
        ele = self.find_elem(loc, img_name)
        # 清除操作
        log.info('{} 在元素 {} 中清除'.format(img_name, loc))
        try:
            ele.clear()
        except:
            log.exception('清除操作失败')
            # 截图
            self.save_img(img_name)

    # 点击操作
    def click_element(self, loc, img_name=None):
        # 先查找元素在点击
        ele = self.find_elem(loc, img_name)
        # 点击操作
        log.info('{} 在元素 {} 中点击'.format(img_name, loc))
        try:
            ele.click()
        except:
            log.exception('点击操作失败')
            # 截图
            self.save_img(img_name)

    # 获取文本内容
    def get_text(self, loc, img_name=None):
        # 先查找元素在获取文本内容
        ele = self.find_elem(loc, img_name)
        # 获取文本
        log.info('{} 在元素 {} 中获取文本'.format(img_name, loc))
        try:
            text = ele.text
            log.info('{} 元素 {} 的文本内容为 {}'.format(img_name, loc, text))
            return text
        except:
            log.exception('获取元素 {} 的文本内容失败,报错信息如下:'.format(loc))
            # 截图
            self.save_img(img_name)

    # 获取属性值
    def get_element_attribute(self, loc, attr, img_name=None):
        # 先查找元素在去获取属性
        ele = self.find_elem(loc, img_name)
        # 获取元素属性值
        log.info('{} 在元素 {} 中获取属性值'.format(img_name, loc))
        try:
            ele_attribute = ele.get_attribute(attr)
            log.info('{} 元素 {} 的文本内容为 {}'.format(img_name, loc, ele_attribute))
            return ele_attribute
        except:
            log.exception('获取元素 {} 的属性值失败,报错信息如下:'.format(loc))
            self.save_img(img_name)

    # iframe 切换
    def switch_iframe(self, frame_refer, timeout=20, poll_frequency=0.5, img_name=None):
        # 等待 iframe 存在
        log.info('iframe 切换操作:')
        try:
            # 切换 == index\name\id\WebElement
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(frame_refer))
            time.sleep(0.5)
            log.info('切换成功')
        except:
            log.exception('iframe 切换失败!!!')
            # 截图
            self.save_img(img_name)

    # 窗口切换 = 如果是切换到新窗口,new. 如果是回到默认的窗口,default
    def switch_window(self, name, cur_handles=None, timeout=20, poll_frequency=0.5, img_name=None):
        """
        调用之前要获取window_handles
        :param name: new 代表最新打开的一个窗口. default 代表第一个窗口. 其他的值表示为窗口的 handles
        :param cur_handles:
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param img_name:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:
        """
        try:
            if name == 'new':
                if cur_handles is not None:
                    log.info('切换到最新打开的窗口')
                    WebDriverWait(self.driver, timeout, poll_frequency).until(EC.new_window_is_opened(cur_handles))
                    window_handles = self.driver.window_handles
                    self.driver.swich_to.window(window_handles[-1])
                else:
                    log.exception('切换失败,没有要切换窗口的信息!!!')
                    self.save_img(img_name)
            elif name == 'default':
                log.info('切换到默认页面')
                self.driver.switch_to.default()
            else:
                log.info('切换到为 handles 的窗口')
                self.driver.swich_to.window(name)
        except:
            log.exception('切换窗口失败!!!')
            # 截图
            self.save_img(img_name)

    # 执行js脚本
    def execute(self, js, *args):
        log.info('执行js脚本')
        try:
            self.driver.execute_script(js, *args)
        except Exception as e:
            log.info(e)

    # 移动到指定元素
    def move_to(self, element):
        log.info('鼠标移动到元素上')
        try:
           ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            log.info(e)

    # 关闭当前窗口
    def close(self):
        self.driver.close()

    # 关闭所哟窗口
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    page = BasePage()
    page.quit()