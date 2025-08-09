numero = int(input("Digite um número entre 1000 e 9999: "))
while 1000 > numero or numero > 9999:
    numero = int(input("Digite um número entre 1000 e 9999: "))

if 1000 <= numero <= 9999:

    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10

    print(f'Milhar: ', milhar)
    print(f'Centena: ', centena)
    print(f'Dezena: ', dezena)
    print(f'Unidade: ', unidade)
