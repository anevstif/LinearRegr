def estimatePrice(mileage, q_0, q_1):
    return (q_0 + (q_1 * mileage))

s=''
with open('tmp.csv') as f :
    try :
        for str in f:
            s = str.strip().split(',')
            a = list(map(float, s))
        if len(a) != 2 : OK = 1
    except :
        exit('File with theta is wrong')
f.close()


while True :
    print('Введите пробег в милях (целое число)')
    str = input() 
    try : 
        mileage = int(str.strip())
        if mileage > 0 :
            break
        else :
            print('Введите положительное число')
    except :
            print('Введие положительное число')

print('Прогнозируемая стоимость автомобиля:')
print(f'{estimatePrice(mileage, a[0], a[1])}')