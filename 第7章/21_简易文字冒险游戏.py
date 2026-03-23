import random


class Character:
    def __init__(self, name):
        self.name = name
        self.HP = 100
        self.atk = 10
        self.coin = 0
        self.pkg = []


def create_character():
    name = input("请输入玩家姓名：")
    character = Character(name)
    return character


def show_status(character):
    if character.pkg:
        pkg_display = character.pkg
    else:
        pkg_display = '空'
    print(f'勇者:{character.name}')
    print(f'HP:{character.HP}')
    print(f'攻击力:{character.atk}')
    print(f'金币:{character.coin}')
    print(f'背包:{pkg_display}')


villages = {"村庄": "宁静的起点", "森林": "危险的树林", "山洞": "神秘的洞穴", "市集": "买卖的市集",
            "Boss巢穴": "最后的终点"}


def show_map():
    print("【地图】 您现在可以前往：\n")
    for i, (location, desc) in enumerate(villages.items(), 1):
        print(f'{i}.{location} - {desc}')


def move(character):
    show_map()
    keys = list(villages.keys())
    choice = input(f'请玩家{character.name}选择目的地（输入数字，q退出）：')
    if choice == 'q':
        print("退出游戏。\n")
        return None
    elif choice.isdigit() and 1 <= int(choice) <= len(keys):
        print(f'\n勇者{character.name}来到了{keys[int(choice) - 1]}。\n')
        return keys[int(choice) - 1]
    else:
        print("输入无效，请您重新输入。")
        return 7


forest_enemy = [{'name': '史莱姆', 'HP': 30, 'atk': 5, 'coin_drop=': 15},
                {'name': '野狼', 'HP': 40, 'atk': 8, 'coin_drop=': 20}]
cave_enemy = [{'name': '哥布林', 'HP': 50, 'atk': 12, 'coin_drop=': 30},
              {'name': '蝙蝠', 'HP': 25, 'atk': 6, 'coin_drop=': 10}]


def encounter_enemy(location):
    if location == '森林':
        return random.choice(forest_enemy)
    elif location == '山洞':
        return random.choice(cave_enemy)
    else:
        print("其他地方没有敌人。")
        return None


def battle(character, enemy):
    # 展示敌人信息
    choice = int(input("玩家选择:1.攻击 / 2.逃跑"))
    while character.HP == 0 or enemy.HP == 0:
        if choice == 1:
            pass
        elif choice == 2:
            alter = random.choice(('逃跑成功', '逃跑失败'))
            print("您逃跑了，无法捡到金币。")
            break
        else:
            print("输入无效。")


p1 = create_character()
print('=' * 20)
show_status(p1)
print('=' * 20)
while True:
    destination = move(p1)
    if destination is None:
        break
