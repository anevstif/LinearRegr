import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


list_in=[]
s=''
f = pd.read_csv('data.csv')
X = np.array(f.get('km'))
Y = np.array(f.get('price'))

Xnorm = X / max(X)

tmp_Q_0 = 0.0
tmp_Q_1 = 0.0
learningRate = 0.05
iter = 1000

def estimatePrice(mileage, q_0, q_1):
    return (q_0 + (q_1 * mileage))

for i in range(iter):
    sum0 = 0.0
    sum1 = 0.0
    for j in range(len(X)):
        sum0 = sum0 + estimatePrice(Xnorm[j], tmp_Q_0, tmp_Q_1) - Y[j]
        sum1 = sum1 + (estimatePrice(Xnorm[j], tmp_Q_0, tmp_Q_1) - Y[j]) * Xnorm[j]
    tmp_Q_0 = tmp_Q_0 - learningRate * sum0 / len(X)
    tmp_Q_1 = tmp_Q_1 - learningRate * sum1 / len(X)
    
plt.plot(X, Y, 'b.')
plt.plot(X, tmp_Q_0 + Xnorm  * tmp_Q_1)
plt.xlabel('km')
plt.ylabel('price')
plt.title('Regr')
plt.show()

tmp_Q_1 = tmp_Q_1 / max(X)

with open('tmp.csv', 'w') as f_k:
    f_k.write(f'{tmp_Q_0}, {tmp_Q_1}')

e = (sum((estimatePrice(X, tmp_Q_0, tmp_Q_1) - Y)**(2)) / len(X))**(0.5)
print(f'Среднее квадратичное отклонение = {e}')
