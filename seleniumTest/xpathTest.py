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


    time.sleep(2)
    bro.close()
