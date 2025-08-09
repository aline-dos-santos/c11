nome = input('Digite seu nome: ')

print(nome.upper())
print(nome.lower())
quantidade_letras = len(nome.replace(" ", ""))
print("Quantidade de letras no total:", quantidade_letras)

partes = nome.split()
if len(partes) > 1:
    partes[-1] = "do Inatel"
    novo_nome = " ".join(partes)
else:
    novo_nome = nome + " do Inatel"

print("Nome com último sobrenome trocado por 'do Inatel':", novo_nome)


