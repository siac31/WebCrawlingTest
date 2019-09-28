import re

with open('index.html','r',encoding='utf-8') as f:
    #html=f.read()
    # 替换换行符
    #html=re.sub('\n','',html)
    html=re.sub('\n','',f.read())
    print(html)
    pattern_1='<div class="email">(.*?)</div>'
    #提取pattern1
    ret_1=re.findall(pattern_1,html)
    #此时如果直接打印 ret1 是有空格的'     hsinjui@foxmail.com     '
    # 因此需要过滤掉前后的空格 字符串 strip
    print(ret_1[0].strip())



# Match RE
password_pattern = r'^[a-zA-Z][a-zA-Z0-9_]{5,15}$'
#password_pattern = r'^[a-zA-Z]{1}[a-zA-Z0-9_]{5-15}$'

pass_1 ='1234567'
pass_2 ='k123456'
pass_3 ='k123'


print(re.match(password_pattern,pass_1))
print(re.match(password_pattern,pass_2))
print(re.match(password_pattern,pass_3))



