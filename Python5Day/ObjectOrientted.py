####################################################
# 面向过程
'''
student1={'name':'Tom','score':98}
student2={'name':'Bob','score':100}

def print_score(stu):
    print('%s:%s' % (stu['name'],stu['score']))
'''
####################################################
# 面向对象
# 1 设计类 属性方法
#
#括号里表示此类继承于哪个对象，python3中所有类继承于object
'''
class Student(object):
    # 方法 self指向创建的实例本身
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s : %s' % (self.name,self.score))

    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

# Instance 1 每一个类的实例被分配一个内存
student1=Student('Tom',98)
student1.print_score()
print(id(student1))

# Instance 2
student2=Student('Tom',98)
student2.print_score()
print(id(student2))

'''
####################################################

'''
访问限制 实例的属性有一些不希望被修改
比如上述student1.score=100k可以修改
__var 私有化 python 其实没有真正的私有属性 可以用get set访问修改
实际项目 建议全部私有话属性

__name
__score
'''

class Student(object):
    # 方法 self指向创建的实例本身
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s : %s' % (self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
#s使用方法修改属性，封装，方便
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('Grade must be between 0 and 100')
# s使用方法对属性访问

    def get_score(self):
        return self.__score

xiaohu=Student('Hu',100)
print(xiaohu.get_score())
xiaohu.set_score(98)
print(xiaohu.get_score())

####################################################

'''
类属性
'''
# 实例属性 必须通过初始化或者实例化对象，通过对象去访问
# 有100个实例就有100个属性name
class Student(object):
    def __init__(self):
        self.name=name
s=Student('Bob')
print(s.name)

# 类属性 必须通过初始化或者实例化对象，通过对象去访问
# 100个实例都是同一个类属性 公有的 与实力无关 无需初始化
class Student(object):
    name='Student'

print(Student.name)