from datetime import datetime


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'
        self.scores = {}

    # 添加成绩
    def add_score(self, subject, score):
        self.scores[subject] = score

    # 计算平均分
    def calcu_avg(self):
        if self.scores:
            avg = sum(self.scores.values()) / len(self.scores)
            return avg
        else:
            return 0

    # 魔法方法，打印
    def __str__(self):
        return f'{self.name}({self.age}-{self.gender}),成绩:{self.scores}，平均分：{self.calcu_avg():.1f}'


class Manage:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        gender = input('请输入性别：')

        stu = Student(name, age, gender)
        self.stu_list.append(stu)
        print(f'添加成功！学生的学号是:{stu.stu_id}')

    # 删除学生
    def del_student(self):
        sid = input("请输入要删除的学生的学号：")
        for stu in self.stu_list:
            if sid == stu.stu_id:
                self.stu_list.remove(stu)
                print(f'成功删除学号为{sid}的学生。\n')
                return
        print(f'未找到学号为{sid}的学生，删除失败。\n')

    # 展示所有学生
    def show_all_student(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print("暂无学生.\n")

    # 给指定的学生设置成绩
    def set_score(self):
        sid = input("请输入学生的学号：")
        for stu in self.stu_list:
            if sid == stu.stu_id:
                score_str = input("请输入学生的成绩（学科-分数，学科-分数）")
                score_list = score_str.replace('，', ',').split(',')
                for item in score_list:
                    subject, score = item.split('-')
                    subject = subject.strip()
                    score = float(score.strip())
                    stu.add_score(subject, score)
                print(f'成功录入学号为{sid}的学生成绩。\n')
                return
        print(f'未找到学号为{sid}的学生。\n')

    # 提供主菜单
    def run(self):
        while True:
            print('************学生管理************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')

            choice = input("请输入您的操作：")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.del_student()
            elif choice == '3':
                self.show_all_student()
            elif choice == '4':
                self.set_score()
            elif choice == '5':
                print('再见！\n')
                break
            else:
                print('输入有误！\n')


m1 = Manage()
m1.run()
