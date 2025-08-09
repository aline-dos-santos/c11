entrada = float(input('Digite a quilometragem da viagem: '))

preco = 0

if entrada <= 200:
    preco = 0.5 * entrada
else:
    preco = 0.45 * entrada

print('A sua passagem custará: ', preco)