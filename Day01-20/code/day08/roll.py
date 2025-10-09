import random

result = {}

for _ in range(6000):
    r = str(random.randint(1,6))
    if r in result:
        result[r] += 1
    else:
        result[r] = 1

for key,value in sorted(result.items()):
    print(f'{key}:{value}')