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
    #bro.find_element_by_xpath("//span[@id='s_kw_wrap']/input[@id='kw']").send_keys('java')
    '''
    xpath:索引
    ​1.如果一个元素它的兄弟元素跟它的标签一样，这时候无法通过层级定位到。因为都是一个父亲生的，多胞胎兄弟。
    ​2.虽然双胞胎兄弟很难识别，但是出生是有先后的，于是可以通过它在家里的排行老几定位到。
    3.用xpath定位老大、老二和老三（这里索引是从1开始算起的，跟Python的索引不一样）'''
    #driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()
    #driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()

    '''xpath:逻辑运算
    ​1.xpath还有一个比较强的功能，是可以多个属性逻辑运算的，可以支持与（and）、或（or）、非（not）
    ​2.一般用的比较多的是and运算，同时满足两个属性'''
    #bro.find_element_by_xpath("//input[@id='kw' and @autocomplete='off']").text = 'java'
    '''
    xpath:模糊匹配
    ​1.xpath还有一个非常强大的功能，模糊匹配
    ​2.掌握了模糊匹配功能，基本上没有定位不到的
    ​3.比如我要定位百度页面的超链接“hao123”,在上一篇中讲过可以通过by_link,也可以通过by_partial_link，模糊匹配定位到。当然xpath也可以有同样的功能，并且更为强大。'''
    #bro.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
    #bro.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys()

    time.sleep(2)
    bro.close()
