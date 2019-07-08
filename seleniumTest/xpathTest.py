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
    #kw = findxpath().xpathId('kw')
    #kw = findxpath().xpathClass('s_ipt')
    #kw = findxpath().xpathName('wd')
    kw = findxpath().xpathAutocomplete('off')
    kw.send_keys('apple')
    time.sleep(2)
    bro.close()
