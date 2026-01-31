#O que seu programa deve fazer:
#Exibir um menu com as opções:
#1. Adicionar aluno
#2. Listar todos os alunos
#3. Buscar aluno pelo nome
#4. Remover aluno
#5. Mostrar média geral das notas
#6. Sair
#✏️ Funcionalidades detalhadas:
#➕ Adicionar aluno
#Pedir o nome, a idade e a nota (0 a 10) do aluno.
#Salvar os dados em um dicionário.
#Adicionar o dicionário a uma lista de alunos.

#📋 Listar todos os alunos
#Mostrar todos os alunos cadastrados com nome, idade e nota.
#Exibir mensagem se não houver nenhum aluno.

#🔍 Buscar aluno pelo nome
#Perguntar um nome e procurar na lista.
#Exibir os dados se o aluno for encontrado.
#Se não existir, exibir uma mensagem de erro.

#🗑️ Remover aluno
#Perguntar o nome do aluno.
#Se existir, remover da lista.
#Se não existir, exibir aviso.

#📊 Média geral das notas
#Calcular e exibir a média de todas as notas dos alunos cadastrados.
#Se não houver alunos, exibir uma mensagem adequada.

#✅ Requisitos técnicos:
#Usar listas e dicionários para armazenar os dados.
#Separar funcionalidades em funções.
#Usar um loop principal com menu (while True) para manter o programa rodando até o usuário sair.
#Validar entradas (por exemplo: nota deve ser um número entre 0 e 10).


# Lista para salvar o cadastro
lista_alunos = []
# Funções

# ADICIONAR ALUNOS
def adicionar_aluno():
        nome = input('Digite o nome do aluno: ')
        idade = int(input('Digite sua idade: '))
        nota = float(input('Digite sua nota: '))
        if nota > 10:
            print('Nota inválida')
            return adicionar_aluno(nota)
        novo_aluno = {'nome':nome,
               'idade':idade,
               'nota':nota}
        lista_alunos.append(novo_aluno)
        print(f'Aluno Cadastrado com sucesso!')
# LISTAR ALUNOS CADASTRADOS
def listar_alunos():
    print('\n--- Alunos Cadastrados ---\n')
    if not lista_alunos:
         print('Ainda não há alunos cadastrados')
        
    for aluno in lista_alunos:
         print(f'Aluno: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}')
# BUSCAR PELO NOME
def buscar_aluno():
    pesquisa_aluno = input('Digite o nome que deseja pesquisar: ')
    encontrado = False

    for aluno in lista_alunos:
        if aluno['nome'].lower() == pesquisa_aluno.lower():
            print('Aluno encontrado!')
            print(f'Aluno: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}')
            encontrado = True
            break
    if not encontrado:
        print(f'O aluno {pesquisa_aluno}, não foi encontrado')
# REMOVER ALUNO
def remover_aluno():
    aluno_removido = input('Digite o nome do aluno que deseja excluir: ')
    for aluno in lista_alunos:
        excluido = False
        if aluno['nome'].lower() == aluno_removido.lower():
            lista_alunos.remove(aluno)
            print('Aluno removido')
            excluido = True
    if not excluido:
        print(f'Aluno {aluno_removido} não encontrado')
# CALCULANDO A MEDIA GERAL
def calcular_media():
    if not lista_alunos:
        print('Não há alunos cadastrados!')
        return
    somas_notas = 0
    for aluno in lista_alunos:
        somas_notas += aluno['nota']

    media_geral = somas_notas / len(lista_alunos)
    print(f'A média geral dos {len(lista_alunos)}, foi de: {media_geral:.2f}')
             
              


while True:
    print('1. Adicionar aluno\n2. Listar todos os alunos\n3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        adicionar_aluno()
    if opcao == 2:
        listar_alunos()
    if opcao == 3:
        buscar_aluno()
    if opcao == 4:
        remover_aluno()
    if opcao == 5:
        calcular_media()
    if opcao == 6:
        break
      


    

