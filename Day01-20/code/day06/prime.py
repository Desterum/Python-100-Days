n = int(input('请输入一个整数: '))

for i in range(2, n ** 0.5 + 1):
    if n % i == 0:
        print(f'{n} 不是素数')
        break
    
print(f'{n} 是素数')