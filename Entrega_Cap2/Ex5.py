totalIdade = 0
totalMulheres = 0

n = int(input('Digite quantas pessoas irá inserir: '))

for i in range(0, n):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo =  input('Digite o sexo (M/F): ')
    totalIdade += idade
    if sexo == 'F' and idade < 20:
            totalMulheres += 1


mediaIdade = totalIdade / n
print('A média das idades é: ', mediaIdade)
print('O total de mulheres com menos de 20 anos é: ', totalMulheres)


