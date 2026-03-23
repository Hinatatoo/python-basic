def calc_total(nums):
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


def main(title, duration, goal):
    print(f'{title}{duration}天挑战赛')
    nums = []
    for index in range(duration):
        nums.append(int(input(f'请输入第{index + 1}天的数据：')))

    total = calc_total(nums)
    avg = calc_avg(total)
    result = check_success(total)
    print(f'{title}{duration}健身总结')
    print(f'总数：{total},平均值:{avg:.1f}，目标：{goal}个')
    print(result)


main('仰卧起坐', 8, 50)
