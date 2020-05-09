# 元素定位的方法

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

'''id name tag_name class_name'''
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_name("wd").send_keys("python")
driver.find_element_by_tag_name("input").send_keys("python")
driver.find_element_by_class_name("s_ipt").send_keys("python")

'''link_text partial_link_text'''
driver.find_element_by_link_text("新闻").click()
driver.find_element_by_partial_link_text("新闻").click()

'''xpath'''
driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
driver.find_element_by_xpath("//*[@id='kw]").send_keys("python")
driver.find_element_by_xpath("//div[@id='u1']/a[0]").send_keys("1")
driver.find_element_by_xpath("//div[@id='hd' or @name=q']").send_keys("2")
driver.find_element_by_xpath("//input[contains(@id,'kw')]").send_keys("python")
'''用于知道超链接上显示的部分或全部 文本信息'''
driver.find_element_by_xpath("//*[contains(text(),'新闻')]").click()
'''用Text()，直接查找页面当中所有的退出二字，经常用于纯文字的查找'''
driver.find_element_by_xpath('//*[text()="新闻"]').click()
'''当标签里面含有其他标签+文字时   https://www.cnblogs.com/sschen/p/3612503.html'''
driver.find_element_by_xpath("//*[contains(.'新闻')]").click()  # 不行，待研究

'''css  单一属性的定位'''
driver.find_element_by_css_selector("input")
# id
driver.find_element_by_css_selector("#kw")
# class
driver.find_element_by_css_selector(".s_ipt")
# 其他属性
driver.find_element_by_css_selector("[name='wd']")
driver.find_element_by_css_selector("[type='text']")
# 组合属性
# id组合属性
driver.find_element_by_css_selector("input#kw")
# class组合属性
driver.find_element_by_css_selector("input.s_ipt")
# 其他属性组合定位
driver.find_element_by_css_selector("input[name='wd']")
# 仅有属性名，没有属性值
driver.find_element_by_css_selector("input[name]")
# 2个属性组合定位
driver.find_element_by_css_selector("[name='wd'][autocomplete='off']")

'''css 模糊匹配属性值的方法'''
# <input type="submit" id="su" value="百度一下" class="bg s_btn">
# 属性值由多个空格隔开，匹配其中一个值的方法
driver.find_element_by_css_selector("input[class~='btn']")
# 匹配属性值为字符串开头的方法
driver.find_element_by_css_selector("input[class^='btn']")
# 匹配属性值字符串结尾的方法
driver.find_element_by_css_selector("input[class$='s_btn']")
# 匹配被-分割的属性值的方法,如上图的class
driver.find_element_by_css_selector("input[class|='bg']")  #要求精确填写的属性值

# 层及定位
# E>F    E下面的F这个元素
driver.find_element_by_css_selector('from#form>span>input')#id是form的form下面的span下面的input
# E:nth-child(n)  如上图,
driver.find_element_by_css_selector('#u1>a:nth-child(1)').click()#id为u_sp的下面的第一个a标签。
# E:nth-last-child(n)，如字面意思：倒数第几个标签
driver.find_element_by_css_selector("#u1>a:nth-last-child(9)")
# 4：E:first-child,第一个标签
driver.find_element_by_css_selector("#u1>a:first-child")
# 5：E:last-child,最后一个标签
# 6：E:only-child,唯一的标签


''' 元素操作的几个方法'''
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("1")
driver.find_element_by_id("su").click()
driver.find_element_by_id("su").submit()
# submit()要求提交对象是一个form表单，更强调对信息的提交。click()更强调事件的独立性。（比如，一个文字链接就不能用 submit()方法。）

'''
https://www.cnblogs.com/constantince/p/4565261.html  chrome浏览器开发这使用指南
'''
'''
第一种方法：通过绝对路径做定位（相信大家不会使用这种方式）
By.xpath("html/body/div/form/input")
第二种方法：相对路径
By.xpath("//input")
第三种方法：通过元素索引定位
By.xpath("//input[4]")
第四种方法：使用xpath属性定位（结合第2、第3中方法可以使用）
By.xpath("//input[@id='kw1']")
By.xpath("//input[@type='name' and @name='kw1']")
第五种方法：使用部分属性值匹配（最强大的方法）
By.xpath("//input[start-with(@id,'nice')
By.xpath("//input[ends-with(@id,'很漂亮')
By.xpath("//input[contains(@id,'那么美')]")
前一个兄弟节点
//input[@name="sne.sysLnNumAdmin.category2"]/preceding-sibling::input
后一个兄弟节点
//div[text()="加密内容不能为空！"]/following-sibling::div//span[text()="确定"]
父节点定位
//span[text()="山东省"]/parent::a/preceding-sibling::span
'''