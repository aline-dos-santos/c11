pessoas = {}

for i in range (0, 3):
    nome = input('Digite seu nome: ')
    peso = float(input('Digite o seu peso: '))
    pessoas[nome] = peso

maximo = max(pessoas, key= pessoas.get)
minimo = min(pessoas, key = pessoas.get)

print('A pessoa mais pesada é: ', maximo)
print('A pessoa mais leve é: ', minimo)

