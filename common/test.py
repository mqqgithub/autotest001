'''
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1

print(fab(6))
f = fab(5)
for i in f:
    print(id(f))
    print(i)'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
su = WebDriverWait(dr, 0.1, 10).until(lambda ele: dr.find_element_by_id('su'))
su.click()
dr.quit()