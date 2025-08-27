#CARREGANDO DATASET

import numpy as np

ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# SLICING 

companys = ds[1:, 1]
locations = ds[1:, 2]
datums = ds[1:, 3]
details = ds[1:, 4]
status = ds[1:, 5]
cost_ds = ds[1:, 6].astype(float)
status_missao = ds[1:, 7]

# QUESTÃO 1

missao_sucesso = np.char.find(status_missao, 'Success') >= 0
total_missao_sucesso = missao_sucesso[missao_sucesso == True].sum()

print('A porcentagem de missões com sucesso é: ', (total_missao_sucesso * 100)/status_missao.size)

# QUESTÃO 2

print('A média de gastos de uma missão espacial é:', cost_ds[cost_ds != 0].mean(), 'dólares.') 

# QUESTÃO 3

realizadas_eua = np.char.find(locations, 'USA') >= 0
total_eua = realizadas_eua[realizadas_eua == True].sum()
print(total_eua)

# QUESTÃO 4

cost_spacex = cost_ds[companys == 'SpaceX']
maximo = np.argmax(cost_spacex)

print('A missao mais cara realizada pela SpaceX custou: ', maximo, ' dólares')

# QUESTÃO 5

empresas, quantidade = np.unique(companys, return_counts=True)

i = 0
for nome in empresas:
    print('Empresa:', nome, 'realizou:', quantidade[i], 'missões.')
    i += 1

