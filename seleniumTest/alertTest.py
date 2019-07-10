'''
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
        <title></title>
    </head>
    <body>
        <div align="center">
        <h4>hello girl</h4>
        <input type="button" onclick="showPro()" value="输入框弹窗按钮"/>
        <input type="button" onclick="showAlert2()" value="提示弹窗按钮"/>
        <input type="button" onclick="showAlert()" value="确认弹窗按钮"/><br><br><br>
        <span id="textSpan"></span>

        </div>
    </body>
    <script>
        function showAlert(){
            document.getElementById("textSpan").innerHTML="";
            if(confirm("你是帅哥吗？")){
                document.getElementById("textSpan").innerHTML="<font style='color: red;'>您为何如此自信？</font>";
            }else{
                document.getElementById("textSpan").innerHTML="<font style='color: red;'>您为何如此谦虚？</font>";
            }

        }
        function showPro(){
            document.getElementById("textSpan").innerHTML="";
            con = prompt("输入1为强哥聪明，输入2为左哥笨");
            if(con==1){
                document.getElementById("textSpan").innerHTML="<font style='color: green;'>强哥是真聪明啊</font>";
            }else if(con==2){
                document.getElementById("textSpan").innerHTML="<font style='color: green;'>左哥是真笨啊</font>";
            }else{
                document.getElementById("textSpan").innerHTML="<font style='color: red;'>您没有按要求输入，请重新输入</font>";
            }
        }
        function showAlert2(){
            document.getElementById("textSpan").innerHTML="";
            alert("用我三世烟火，换你一世迷离");
        }
    </script>
</html>
'''
#-*-coding:utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/autotest001/seleniumTest/alertTest.html')
'''获取alert对话框的按钮,点击按钮,弹出alert对话框'''
driver.find_element_by_xpath('/html/body/div/input[2]').click()
'''获取alert对话框'''
alert = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
'''获取警告对话框的内容'''
print (alert.text)  #打印警告对话框内容
alert.accept()   #alert对话框属于警告对话框，我们这里只能接受弹窗
'''添加等待时间'''
time.sleep(2)

##################################################
'''获取confirm对话框的按钮,点击按钮,弹出confirm对话框'''
driver.find_element_by_xpath('/html/body/div/input[3]').click()
'''获取confirm对话框'''
dialog_box = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
'''获取对话框的内容'''
#打印警告对话框内容
print (dialog_box.text)
'''点击【确认】显示"您为何如此自信？"'''
dialog_box.accept()   #接受弹窗
#打印接受对话框后的提示信息
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)
time.sleep(2)

'''再次获取confirm对话框的按钮,点击按钮,弹出confirm对话框'''
driver.find_element_by_xpath('/html/body/div/input[3]').click()
'''再次获取confirm对话框'''
dialog_box = driver.switch_to_alert()
'''点击【取消】显示"您为何如此谦虚？"'''
time.sleep(2)
dialog_box.dismiss()  #关闭获取取消对话框
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)
##################################################33
'''获取prompt对话框的按钮,点击按钮,弹出confirm对话框'''
driver.find_element_by_xpath('/html/body/div/input[1]').click()
'''获取prompt对话框'''
dialog_box = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
'''获取对话框的内容'''
print (dialog_box.text)  #打印警告对话框内容
dialog_box.send_keys("2")  #弹出框内输入2
dialog_box.accept()  #接受
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)  #获取关闭弹窗结果  #获取确认弹窗结果
'''这里等待几秒在测试取消'''
time.sleep(2)
#************************点击【取消】,并且获取显示结果**********************
driver.find_element_by_xpath('/html/body/div/input[1]').click()
'''获取prompt对话框'''
dialog_box = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
dialog_box.dismiss()  #关闭对话框
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)  #获取关闭弹窗结果
time.sleep(2)



driver.quit()