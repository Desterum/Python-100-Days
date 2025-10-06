for i in range(1, 1000):
    hundreds = i // 100
    tens = (i // 10) % 10  
    units = i % 10
    if i == hundreds**3 + tens**3 + units**3:
        print(i)