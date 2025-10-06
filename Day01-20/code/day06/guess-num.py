import random

n = random.randint(1, 100)
i = 0
while True:
    guess = int(input('请输入你猜的数字(1-100): '))
    i += 1
    if guess < n:
        print('太小了')
    elif guess > n:
        print('太大了')
    else:
        print('猜对了')
        print(f'你总共猜了{i}次')
        break