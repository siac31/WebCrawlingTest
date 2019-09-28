import json

python_data=[
    {
        'username':'name1',
        'vip':True,
    },
    {
        'username':None,
        'vip':False
    }
]
# dumps用于把python对象转换成json对象
json_data =json.dumps(python_data) # None --> null False--> false
print(json_data)
print(type(json_data))


# loads 把jsonz转换成pzthon对象
python_data2=json.loads(json_data)
print(python_data2)
print(type(python_data2))

#q去掉s表示本地操作
# dump 用于把python数据类型转换成json类型的字符串，并保存到本地
json.dump(python_data,open('json.text','w'))

# load 用于读取本地json类型数据，并转换成python对象
python_data_3=json.load(open('json.text'))
print(python_data_3)
