import urllib.request as ur
request= ur.Request('https://edu.csdn.net/')
response =ur.urlopen(request).read()
print(response)