height = float(input('请输入身高(cm):'))
weight = float(input('请输入体重(kg):'))

bmi = weight / (height / 100) ** 2

print(f'{bmi = :.1f}')
if 18.5 <= bmi <= 24:
    print('你很健康')
elif bmi > 24:
    print('该健了')
else:
    print('该吃了')

