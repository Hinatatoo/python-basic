class Person:
    max_age = 120

    def __init__(self, name, age, idcard):
        self.name = name
        self._age = age
        self.__idcard = idcard

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 120:
            self._age = value
        else:
            print(f'年龄非法，已将年龄变为最大值{Person.max_age}')
            self._age = Person.max_age

    @property
    def idcard(self):
        return self.__idcard[:6] + '********' + self.__idcard[-4:]

    @idcard.setter
    def idcard(self, value):
        print("抱歉，身份证不能随便修改")


p1 = Person('张三', 18, '450888866612104321')
print(p1.age)
print(p1.idcard)

p1.age = 20
print(p1.age)
p1.idcard = '124578326598258546'
print(p1.idcard)
