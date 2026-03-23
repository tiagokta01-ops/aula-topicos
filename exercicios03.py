#exemplofeitonaaula
'''import csv
dados = [
    ['nome','nota','turma'],
    ['ana',8.5,'1E'],
    ['beto',7,'1E' ],
    ['carla',9.2, '1E'],
]
with open ('turma.csv','w',
           encoding='utf-8',
           newline='') as arquivo:
    escritor=csv.writer(arquivo)
    for linha in dados:
        escritor.writerow (linha) 

           
 #le o arquivo csv
with open ('turma.cvs','r',
           encoding='utf-8') as arquivo:
    leitor = cvs.reader(arquivo)
    for linha in leitor:
        print(linha)'''
#5
'''import csv

dados = []

dados.append(['nome', 'nota1', 'nota2'])

for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    
    dados.append([nome, nota1, nota2])

with open('turma.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    
    for linha in dados:
        escritor.writerow(linha)

print("Arquivo turma.csv criado com sucesso!")'''

#6
'''import csv

with open('notas.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for registro in leitor:
        nome = registro['nome']
        nota1 = float(registro['nota1'])
        nota2 = float(registro['nota2'])
        nota3 = float(registro['nota3'])
        
        media = (nota1 + nota2 + nota3) / 3
        
        if media >= 6:
            status = "Aprovada"
        else:
            status = "Reprovada"
        
        print(f"{nome} – Média: {media:.2f} – {status}")'''

#7
'''import csv

with open('notas.csv', 'r', encoding='utf-8') as entrada, \
     open('notas_com_media.csv', 'w', encoding='utf-8', newline='') as saida:
    
    leitor = csv.DictReader(entrada)
    
    # Criar cabeçalho novo (colunas antigas + media)
    campos = leitor.fieldnames + ['media']
    
    escritor = csv.DictWriter(saida, fieldnames=campos)
    escritor.writeheader()
    
    for registro in leitor:
        nota1 = float(registro['nota1'])
        nota2 = float(registro['nota2'])
        nota3 = float(registro['nota3'])
        
        media = (nota1 + nota2 + nota3) / 3
        
        # Adiciona a nova coluna no dicionário
        registro['media'] = f"{media:.2f}"
        
        escritor.writerow(registro)

print("Arquivo notas_com_media.csv criado com sucesso!")'''


#8
'''import csv

with open('notas.csv', 'r', encoding='utf-8') as entrada, \
     open('aprovados.csv', 'w', encoding='utf-8', newline='') as arq_aprovados, \
     open('reprovados.csv', 'w', encoding='utf-8', newline='') as arq_reprovados:
    
    leitor = csv.DictReader(entrada)
    
    # Cabeçalho dos novos arquivos
    campos = ['nome', 'media', 'situacao']
    
    escritor_aprovados = csv.DictWriter(arq_aprovados, fieldnames=campos)
    escritor_reprovados = csv.DictWriter(arq_reprovados, fieldnames=campos)
    
    escritor_aprovados.writeheader()
    escritor_reprovados.writeheader()
    
    for registro in leitor:
        nome = registro['nome']
        nota1 = float(registro['nota1'])
        nota2 = float(registro['nota2'])
        nota3 = float(registro['nota3'])
        
        media = (nota1 + nota2 + nota3) / 3
        
        if media >= 6:
            situacao = 'Aprovado'
            escritor_aprovados.writerow({
                'nome': nome,
                'media': f"{media:.2f}",
                'situacao': situacao
            })
        else:
            situacao = 'Reprovado'
            escritor_reprovados.writerow({
                'nome': nome,
                'media': f"{media:.2f}",
                'situacao': situacao
            })

print("Arquivos aprovados.csv e reprovados.csv criados!")'''




















