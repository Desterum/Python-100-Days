import math

r = float(input("请输入圆的半径："))

area = math.pi * r ** 2
perimeter = 2 * math.pi * r

print(f'半径为{r:.1f}的圆的周长是{perimeter:.2f}')
print(f'半径为{r:.1f}的圆的面积是{area:.2f}')

print(f'{perimeter = :.2f}')
print(f'{area = :.2f}')
