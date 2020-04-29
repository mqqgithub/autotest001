from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

size = driver.find_element_by_id("su").size
print(size)

text = driver.find_element_by_id("su").text
print(text)

value = driver.find_element_by_id("su").get_attribute('value')
print(value)

#返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
type = driver.find_element_by_id("su").get_attribute('type')
print(type)

#返回元素的结果是否可见，返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)
'''
第一种方法：通过绝对路径做定位（相信大家不会使用这种方式）

By.xpath("html/body/div/form/input")
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