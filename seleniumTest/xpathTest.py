#<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
#<a class="mnav" target="_blank" href="http://www.hao123.com">hao123</a>
'''

'''

from seleniumTest.webdriverTest import openbrowser
import time
class findxpath():
    b = openbrowser().openChrome()
    b.get('https://www.baidu.com')
    #元素id、name、class属性
    def xpathId(self, value):
        id = "//*[@id='"+value+"']"
        return self.b.find_element_by_xpath(id)

    def xpathName(self, value):
        name = "//*[@name='"+value+"']"
        return self.b.find_element_by_xpath(name)

    def xpathClass(self, value):
        cls = "//*[@class='"+value+"']"
        return self.b.find_element_by_xpath(cls)
    #
    def xpathAutocomplete(self, value):
        autocom = "//*[@autocomplete='"+value+"']"
        return self.b.find_element_by_xpath(autocom)

if __name__=='__main__':
    bro = findxpath().b
    #bro.get('https://www.baidu.com')
    #kw = findxpath().xpathId('kw')
    #kw = findxpath().xpathClass('s_ipt')
    #kw = findxpath().xpathName('wd')
    #kw = findxpath().xpathAutocomplete('off')
    #kw.send_keys('apple')
    '''xpath:标签
    1.有时候同一个属性，同名的比较多，这时候可以通过标签筛选下，定位更准一点
    2.如果不想制定标签名称，可以用*号表示任意标签
    3.如果想制定具体某个标签，就可以直接写标签名称'''
    #bro.find_element_by_xpath("//input[@id='kw']").send_keys('java')
    #bro.find_element_by_xpath("//input[@name='wd']").send_keys('c')
    #bro.find_element_by_xpath("//input[@class='s_ipt']").send_keys('c++')
    #bro.find_element_by_xpath("//input[@autocomplete='off']").send_keys('python')
    ''' xpath:层级
    1.如果一个元素，它的属性不是很明显，无法直接定位到，这时候我们可以先找它老爸（父元素）
    2.找到它老爸后，再找下个层级就能定位到了
    '''
    #<span id="s_kw_wrap" class="bg s_ipt_wr quickdelete-wrap">
    # <span class="soutu-btn"></span>
    # <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
    # <a href="javascript:;" id="quickdelete" title="清空" class="quickdelete" style="top: 0px; right: 0px; display: none;">
    # </a></span>
    bro.find_element_by_xpath("//span[@id='s_kw_wrap']/input[@id='kw']").send_keys('java')
    '''
    使用逻辑运算符
    如果一个属性不能唯一的区分一个元素，我们还可以使用逻辑运算符连接多个属性来区别于其它属性。'''
    bro.find_element_by_xpath("//input[@id='kw' and @class='su']/span/input")
    '''
    1.contains模糊匹配text：contains
     如，通过模糊匹配text属性，找到百度首页的“糯米”网站超链接
    2.模糊匹配某个属性：contains
    3.模糊匹配以xx开头：starts-with
    除了这个文本属性匹配是.//*[text()=‘文本’]这种格式(无@)
    其它的属性，如id,name,class等都是.//*[@id=‘xxx’] .//*[@name=‘xxx’]这种格式
    '''
    driver.find_element_by_xpath("//a[contains(text(),'糯')]").click()
    xpath("//input[contains(@id,‘xx')]")
    driver.find_element_by_xpath("//input[contains(@class,'s_ip')]").send_keys("hao")
    xpath("//input[starts-with(@id,‘xx') ]")
    driver.find_element_by_xpath("//input[starts-with(@class,'s_ip')]").send_keys("hao")
    '''
    1.表格
    Table表格固定格式：.//*[@id=‘表格id’]/tbody/tr[行数]/td[列数]/a
    .//*[@id='bugList']/tbody/tr[6]/td[4]/a
    2、参数化行和列
    x = 6
    y = 4
    table = f".//*[@id='bugList']/tbody/tr[{x}]/td[{y}]/a"
    driver.find_element_by_xpath(table).click()
    3、根据表格标题定位后面的按钮
    1.先通过bug的标题名称找到这一行
    2.再找到这一行的父节点
    3.通过父节点往下搜（编辑按钮都是固定位置）
    
    text = "上传多个附件"
    t = f'.//*[text()="{text}"]/../../td[@class="text-right"]/a[@title="编辑"]'
    driver.find_element_by_xpath(t).click()
    '''


    time.sleep(2)
    bro.close()
