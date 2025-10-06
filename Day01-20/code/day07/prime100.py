n = int(input('请输入1-100的正整数: '))
is_prime = True
for i in range(2, int(n ** 0.5 + 1)):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{n}是素数')
else:
    print(f'{n}不是素数')