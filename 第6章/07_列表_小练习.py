print('请输入学生成绩，输入“结束”停止录入')
score_list = []
while True:
    data = input("请输入成绩：")
    if data == '结束':
        break
    else:
        score_list.append(int(data))

total_count = len(score_list)
sum_score = sum(score_list)
avg_score = sum_score / total_count
pass_count = 0
excellent_count = 0

for item in score_list:
    if item > 60:
        pass_count += 1
    if item > 90:
        excellent_count += 1

pass_rate = pass_count / total_count * 100
excellent_rate = excellent_count / total_count * 100

print('********⬇️统计信息如下⬇️********')
print(f'🧑‍🎓总人数为：{len(score_list)}')
print(f'🔺最高分为：{max(score_list)}')
print(f'🔻最低分为：{min(score_list)}')
print(f'✅合格人数：{pass_count}人')
print(f'📈合格率为：{pass_rate:.1f}%')
print(f'🏆优秀人数：{excellent_count}人')
print(f'📈优秀率为：{excellent_rate:.1f}%')
print(f'📊平均分数：{avg_score:.1f}')
