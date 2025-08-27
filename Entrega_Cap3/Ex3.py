nome_aluno = input('Digite seu nome: ')
media_aluno = int(input('Digite sua média: '))

aluno = {'Nome' : nome_aluno, 'Média' : media_aluno}

if media_aluno >= 50:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(aluno)

