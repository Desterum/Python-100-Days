i = 1
while True:
    j = 1
    
    if i == 7:
        i += 1
        continue

    while j <= i:
        print(f'{j} * {i} = {i * j}',end='\t')
        j += 1    
    i += 1
    print('')    

    if i > 9:
        break