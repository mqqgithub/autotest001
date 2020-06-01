'''
定义:匹配字符中的字符串
应用: 注册时候校验手机号邮箱合法性；从文件中查找特定的字符串
记忆: \d \w \s \t \n \D \W \S ;
      .任意字符  ^ 开头  $ 结尾  ;
      [12345][1-5][^1-5][0-9a-zA-Z]
      a|b  (a|b|c)
贪婪匹配：
      *  +   ?   {n}  {n,}  {n,m}  加上？变为非贪婪
*? 重复任意次，但尽可能少重复
+? 重复1次或更多次，但尽可能少重复
?? 重复0次或1次，但尽可能少重复
{n,m}? 重复n到m次，但尽可能少重复
{n,}? 重复n次以上，但尽可能少重复

.*?的用法：
. 是任意字符
* 是取 0 至 无限长度
? 是非贪婪模式。

何在一起就是 取尽量少的任意字符，一般不会这么单独写，他大多用在：
.*?x
就是取前面任意长度的字符，直到一个x出现


'''
import re


s = '_123456abc  deabc  ACBww.aa.com111www.bb.com222www.cc.com!@#$%^&*()11'

ret = re.findall(r'\d', s)
print(r'\d匹配数字', ret)

ret = re.findall(r'\w', s)
print(r'\w匹配数字-字母-下划线', ret)

ret = re.findall(r'\s', s)
print(r'\s匹配空格', ret)

ret = re.findall(r'\n', s)
print(r'\n匹配换行符enter', ret)

ret = re.findall(r'\t', s)
print(r'\t匹配制表符tab', ret)

ret = re.findall(r'.', s)
print(r'.匹配除了换行符的字符', ret)

ret = re.findall(r'^_12', s)
print(r'^匹配从字符串开头开始', ret)

ret = re.findall(r'..11$', s)
print(r'$匹配从字符串开头开始', ret)

ret = re.findall(r'\W', s)
print(r'\W匹配非字母数字下划线', ret)

ret = re.findall(r'\D', s)
print(r'\D匹配非数字下划线', ret)

ret = re.findall(r'\S', s)
print(r'\S匹配非空白符', ret)

ret = re.findall(r'a|b', s)
print(r'a|b匹配a或者b', ret)

ret = re.findall(r'www.(aa|bb|cc).com', s)
print(r'()括号内是一个组', ret)

ret = re.findall(r'[1ab]', s)
print(r'[]括号内的一个字符', ret)

ret = re.findall(r'[^1ab]', s)
print(r'[^]非括号内的一个字符', ret)

s = 'cabb3abcbbaca'
ret = re.findall(r'ab?', s)  # ？前一个字符是b，可以是0个b或1个b
print(r'?匹配前一个字符0次或者一次', ret)

ret = re.findall(r'ab*', s)
print(r'*匹配前一个字符0次或者多次', ret)

ret = re.findall(r'ab+', s)
print(r'+匹配前一次1次或者多次', ret)

ret = re.findall(r'a.?', s)  # ？前一个字符是b，可以是0个b或1个b
print(r'?匹配前一个字符0次或者一次', ret)

ret = re.findall(r'a.*', s)
print(r'*匹配前一个字符0次或者多次', ret)

ret = re.findall(r'a.+', s)
print(r'+匹配前一次1次或者多次', ret)

ret = re.findall(r'a.{1,2}', s)
print(r'+匹配前一次1次或者多次', ret)

ret = re.findall(r'ab*?', s)
print(r'*?\+?\??\{m}?\{n,}?\{n,m}?惰性匹配,最少匹配', ret)

ret = re.findall(r'ab+?', s)
print(r'*?\+?\??\{m}?\{n,}?\{n,m}?惰性匹配,最少匹配', ret)

ret = re.findall(r'ab??', s)
print(r'*?\+?\??\{m}?\{n,}?\{n,m}?惰性匹配,最少匹配', ret)




