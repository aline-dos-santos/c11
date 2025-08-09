
entrada = input("Digite o seu sexo (M) ou (F): ")

while entrada != 'M' or 'F':
    entrada = input("Digite o seu sexo (M) ou (F): ")

    if entrada == 'F':
        print('Sexo feminino')
    else:
        print('Sexo masculino')
