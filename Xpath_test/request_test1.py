import urllib.request as ur
import urllib.parse as up

url_address='https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=50'
'''
kw=英雄联盟&ie=utf-8&pn=100
'''
data ={
    'kw':'英雄联盟',
    'ie':'utf-8',
    'pn': '100'
}
data_1={
    'pn': '100',
    'ie':'utf-8',
    'kw': '英雄联盟'
}
data_url=up.urlencode(
    data
)
data_url_1=up.urlencode(
    data_1
)
print(data_url)
print(data_url_1)
ret=up.unquote(data_url)
ret_1=up.unquote(data_url_1)
print(ret)
print(ret_1)
request=ur.Request('https://tieba.baidu.com/f?'+data_url_1)
response=ur.urlopen(request).read()
with open('baiduLOL.html','wb') as f:
    f.write(response)
