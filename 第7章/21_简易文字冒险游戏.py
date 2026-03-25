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


forest_enemy = [{'name': '史莱姆', 'HP': 30, 'atk': 5, 'coin_drop': 15},
                {'name': '野狼', 'HP': 40, 'atk': 8, 'coin_drop': 20}]
cave_enemy = [{'name': '哥布林', 'HP': 50, 'atk': 12, 'coin_drop': 30},
              {'name': '蝙蝠', 'HP': 25, 'atk': 6, 'coin_drop': 10}]


def encounter_enemy(location):
    if location == '森林':
        return random.choice(forest_enemy)
    elif location == '山洞':
        return random.choice(cave_enemy)
    else:
        print("其他地方没有敌人。")
        return None


def battle(character, enemy):
    print(f"遭遇了{enemy['name']}!HP:{enemy['HP']} 攻击力:{enemy['atk']}")
    while character.HP > 0 and enemy['HP'] > 0:
        choice = input("玩家选择:1.攻击 / 2.逃跑")
        if choice == '1':
            # 玩家攻击敌人
            enemy['HP'] -= character.atk
            print(f'对敌人造成{character.atk}点伤害')
            if enemy['HP'] > 0:
                character.HP -= enemy['atk']
                print(f"敌人对您造成{enemy['atk']}点伤害")

        elif choice == '2':
            result = random.choice(['成功', '失败'])
            if result == '成功':
                print("逃跑成功")
                return
            else:
                print("逃跑失败，敌人反击！")
                character.HP -= enemy['atk']
                print(f"敌人对您造成{enemy['atk']}点伤害，当前HP：{character.HP}")
        else:
            print("输入无效！")

    if enemy['HP'] <= 0:
        print(f"击败了{enemy['name']}!获得了{enemy['coin_drop']}金币!")
        character.coin += enemy['coin_drop']
    elif character.HP <= 0:
        print('您被击败了，游戏结束')
        return False


commodity = [{'name': '血瓶', 'price': 20, 'role': 'HP恢复30'},
             {'name': '武器', 'price': 50, 'role': '攻击力+5'}]


def shop(character):
    while True:
        print(f'\n您来到了集市！当前金币:{character.coin}')
        for i, item in enumerate(commodity, 1):
            print(f'{i}.{item["name"]}-{item["price"]}金币-{item["role"]}')
        print('q.离开集市')

        choice = input('请选择:')
        if choice == 'q':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(commodity):
            item=commodity[int(choice)-1]
            if character.coin>=item['price']:
                character.coin-=item['price']
                character.pkg.append(item['name'])
                print(f'购买成功！{item["name"]}已经存入背包。')
            else:
                print('金币不足！')
        else:
            print('输入无效')


def use_item(character):
    if not character.pkg:
        print('背包没有道具！')
    else:
        print('背包里面有以下东西：')
        for i,item in enumerate(character.pkg,1):
            print(f'{i}.{item}')
        choice=int(input('请选择需要使用哪一个：'))
        if character.pkg[choice-1]=='血瓶':
            character.HP+=30
            if character.HP>=100:
                character.HP=100
            character.pkg.pop(choice-1)
        elif character.pkg[choice-1]=='武器':
            character.atk+=5
            character.pkg.pop(choice-1)


p1 = create_character()
print('=' * 20)
show_status(p1)
print('=' * 20)
while True:
    destination = move(p1)
    if destination is None:
        break
    elif destination=='市集':
        shop(p1)
    elif destination=='村庄':
        print('村庄很安全，您可以休息一下。')
        use_item(p1)
    else:
        enemy = encounter_enemy(destination)
        if enemy:
            alive = battle(p1, enemy)
            show_status(p1)
            if not alive:
                break
