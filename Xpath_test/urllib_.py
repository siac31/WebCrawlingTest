import urllib.request as ur

ret = ur.urlopen('https://edu.csdn.net/').read() #读取此地址的html
print(ret)
with open('edu.html','wb') as f: #写入edu.html
    f.write(ret)
