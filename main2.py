import matplotlib.pyplot as plt
list_in=[]
s=''
f = open('data2.csv')
f.readline()
for str in f:
    s = str.strip().split(',')
    print(s)
    a = list(map(float, s))
    list_in.append(a)
f.close()
tmp_Q_0 = 0.0
tmp_Q_1 = 0.0
learningRate = 0.05

def estimatePrice(mileage, q_0, q_1):
    return (q_0 + (q_1 * mileage))

for i in range(10):
    sum0 = 0.0
    sum1 = 0.0
    for j in range(len(list_in)):
        sum0 = sum0 + estimatePrice(list_in[j][0], tmp_Q_0, tmp_Q_1) - list_in[j][1]
        sum1 = sum1 + (estimatePrice(list_in[j][0], tmp_Q_0, tmp_Q_1) - list_in[j][1]) * list_in[j][0]
    tmp_Q_0 = learningRate * sum0 / len(list_in)
    tmp_Q_1 = learningRate * sum1 / len(list_in)
    print(f'{tmp_Q_0}, {tmp_Q_1}')  
    
with open('tmp.csv', 'w') as f_k:
    f_k.write(f'{tmp_Q_0},{tmp_Q_1}')
