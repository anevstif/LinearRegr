def estimatePrice(mileage, q_0, q_1):
    return (q_0 + (q_1 * mileage))

list_in=[]
s=''
f = open('tmp.csv')
for str in f:
    s = str.strip().split(',')
    print(s)
    a = list(map(float, s))
f.close()
print('Введите пробег в милях')
str = input() 
mileage = int(str.strip('-'))
print('Прогнозируемая стоимость')
print(f'{estimatePrice(mileage, a[0], a[1])}')