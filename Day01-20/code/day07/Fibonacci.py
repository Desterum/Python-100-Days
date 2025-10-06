i1 = 1
i2 = 1

print(i1)
print(i2)

for _ in range(18):
    print(i1 + i2)
    i1, i2 = i2, i1 + i2