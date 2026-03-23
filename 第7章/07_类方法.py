from datetime import datetime


# 定义一个Person类
class Person:
    # 类属性
    max_age = 120
    planet = '地球'

    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # speak方法、run方法，它们都属于实例方法
    def speak(self, msg):
        print(f'我叫{self.name},我的年龄是{self.age},性别是{self.gender}')

    def run(self, distance):
        print(f'{self.name}现在跑了{distance}米。')

    # 使用@classmethod 装饰过的方法就叫类方法
    @classmethod
    def change_planet(cls, value):
        cls.planet = value

    @classmethod
    def create(cls, info_str):
        name, year, gender = info_str.split('-')
        current_year = datetime.now().year
        age = current_year - int(year)
        return cls(name, age, gender)


print(Person.__dict__)

Person.change_planet('月球')
print(Person.planet)
print(Person.__dict__)

p1 = Person('张三', 18, 'male')
p2 = Person('李四', 19, 'female')
print(p1.planet)
print(p2.planet)

p3 = Person.create('王五-2009-male')
print(p3.__dict__)
