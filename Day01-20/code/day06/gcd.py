x = int(input('请输入一个正整数: '))
y = int(input('请输入另一个正整数: '))

# for i in range(min(x, y), 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(f'{x}和{y}的最大公约数是{i}')
#         break

while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')