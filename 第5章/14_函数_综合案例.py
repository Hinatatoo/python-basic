def calc_total(*nums):
    """
    计算总运动量
    :param nums: 每一天的运动量
    :return: 总运动量
    """
    return sum(nums)


def calc_avg(total, days=7):
    """
    计算平均值
    :param total:总运动量
    :param days: 天数
    :return:平均值
    """
    return total / days


def check_success(total, goal=120):
    if total > goal:
        return "恭喜"
    else:
        return "抱歉，挑战失败"


def main(title, duration):
    print(f'{title}{duration}挑战赛')
    num1 = int(input(f'第1天：'))
    num2 = int(input(f'第2天：'))
    total = calc_total(num1, num2)
    avg = calc_avg(total)
    result = check_success(total)
    print(f'{title}{duration}健身总结')
    print(f'总数：{total},平均值:{avg:.1f}')
    print(result)


main('仰卧起坐', 7)
