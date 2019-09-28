class Student(object):
    def __init__(self,name,*gender):
        self.name=name
        self.__gender=gender

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender in ['male','female']:
            self.__gender=gender
        else:
            raise ValueError('Gender must be female or male')


junyao=Student('Junyao')
junyao.set_gender('female')
print(junyao.get_gender())