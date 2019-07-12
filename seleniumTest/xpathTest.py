#xpath:标签
#1.有时候同一个属性，同名的比较多，这时候可以通过标签筛选下，定位更准一点
#2.如果不想制定标签名称，可以用*号表示任意标签
#3.如果想制定具体某个标签，就可以直接写标签名称'''
#bro.find_element_by_xpath("//input[@id='kw']").send_keys('java')
#bro.find_element_by_xpath("//input[@name='wd']").send_keys('c')
#bro.find_element_by_xpath("//input[@class='s_ipt']").send_keys('c++')
#bro.find_element_by_xpath("//input[@autocomplete='off']").send_keys('python')
#xpath:层级
#1.如果一个元素，它的属性不是很明显，无法直接定位到，这时候我们可以先找它老爸（父元素）
#2.找到它老爸后，再找下个层级就能定位到了
#<span id="s_kw_wrap" class="bg s_ipt_wr quickdelete-wrap">
# <span class="soutu-btn"></span>
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
# <a href="javascript:;" id="quickdelete" title="清空" class="quickdelete" style="top: 0px; right: 0px; display: none;">
# </a></span>
#bro.find_element_by_xpath("//span[@id='s_kw_wrap']/input[@id='kw']").send_keys('java')
#xpath('//div[contains(@class,"a") and contains(@class,"b")]') #它会取class含有有a和b的元素
#xpath('//div[contains(@class,"a") or contains(@class,"b")]') #它会取class 含有 a 或者 b满足时，或者同时满足时的元素
#https://www.cnblogs.com/zhongyehai/p/10646194.html

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/autotest001/seleniumTest/xpathTest.html')
#tag标签的内容定位，如果是唯一的
#t = driver.find_element_by_xpath("//li[contains(text(),任务类型)]").text
#driver.find_element_by_xpath("//div/a[contains(text(), 新闻)]")
#如果标签内容中含有欠他标签，则用这种形式
t = driver.find_element_by_xpath("//li[contains(.,'单纯')]").text

print(t)