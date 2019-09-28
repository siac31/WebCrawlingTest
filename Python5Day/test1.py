#循环实现 99乘法表
num1=1
while num1<=9:
    num2=1
    while num2<=num1:
        print(str(num1),'*',str(num2),'=',str(num1*num2),end='   ')
        num2=num2+1
    print('\n')
    num1=num1+1


#def student(name,age,**kw):
 #   print('Name:', name, 'Age:', age, 'others:', kw)
#info_dict={'region':'China'}

def student(name,age,*,city):
    print('Name:', name, 'Age:', age, 'city:', city)

student('Xinrui',18,city='Beijing')