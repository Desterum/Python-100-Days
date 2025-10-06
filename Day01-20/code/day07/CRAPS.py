import random

money = 1000

while money > 0:
    print(f'{money = :}')
    pour = int(input('请下注'))
    r0 = random.randrange(1,7) + random.randrange(1,7)
    print(f'{r0 = :}')
    match r0:
        case 7 | 11: 
            money += pour
            print('你赢了')
            continue
        case 2 | 3 | 12: 
            money -=pour
            print('你输了')
            continue
    
    while True:
        roll = random.randrange(1,7) + random.randrange(1,7)
        print(f'{roll = :}')
        if roll == 7:
            money -= pour
            print('你输了')
            break
        elif roll == r0:
            money += pour
            print('你赢了')
            break
    continue

print('你破产了')
