#<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
#<a class="mnav" target="_blank" href="http://www.hao123.com">hao123</a>
'''

'''
from seleniumTest.webdriverTest import openbrowser
import time
class findelement():
    b = openbrowser().openChrome()
    b.get('https://www.baidu.com')
    def findId(self, id):
        return self.b.find_element_by_id(id)
    def findName(self, name):
        return self.b.find_element_by_name(name)
    def findClass(self, classname):
        return self.b.find_element_by_class_name(classname)
    def findLink(self, link):
        return self.b.find_element_by_partial_link_text(link)
    def findPartLink(self, link):
        return self.b.find_element_by_link_text(link)
    def findXpah(self, xpath):
        return self.b.find_element_by_xpath(xpath)
    def findCss(self, css):
        return self.b.findelement_by_css_selector(css)


if __name__=='__main__':
    bro = findelement().b
    id = findelement().findId('kw')
    id.send_keys('NBA')
    time.sleep(2)
    bro.close()

