#aula
'''aluno = {
    'nome':'lucas',
    'matricula': 123456789,
    'turma': '3e',
        'notas' :[9.9, 10, 8.9]
    }
aluno['nome'] = "Tiago"
print(aluno)
print(aluno['nome'])'''

#11

'''contato = {
    'nome': 'Tiago Araujo',
    'telefone': '3299999-8888',
    'email': 'tiago@gmail.com',
    'cidade': 'Rio Pomba'
}

for chave, valor in contato.items():
    print(f'{chave}: {valor}')

contato['instagram'] = '@tiago123'

del contato['telefone']

if 'email' in contato:
    print('A chave email existe no dicionário!')

print(contato)'''

#12

'''frase = 'o rato roeu a roupa do rei de roma'

palavras = frase.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)'''

#13
'''turma = {
    'Aniger': [8.0, 7.5, 9.0],
    'isabela': [5.0, 6.0, 5.5],
    'milena': [7.0, 8.0, 6.5],
    'tiago': [4.5, 5.0, 6.0]
}

for nome, notas in turma.items():
    media = sum(notas) / len(notas)
    
    if media >= 6.0:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    
    print(f'{nome} – Média: {media:.1f} – Situação: {situacao}')'''

#14

'''info1 = {'nome': 'Notebook', 'preco': 3500.00}
info2 = {'marca': 'TechBrand', 'estoque': 15}
produto = {**info1, **info2}

produto['preco'] = 3200.00
print(produto)'''

















