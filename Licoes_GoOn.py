
nome = ''
idade = ''
cidade = ''
print(f'Qual seu nome: {nome} ')
nome = input(nome)
print(f'seja bem vindo senhor(a) : {nome}')
print(f'Por favor entre com sua idade: {idade}')
idade = int(input(idade))
print(f'Por favor entre com o nome da cidade natal: {cidade}')
cidade = input(cidade)
print(f'O senhor(a) {nome} nasceu em {cidade} e o ano de nascimento é: {2023 - idade}')
'''
res:
Qual seu nome:  
Antonio
seja bem vindo senhor(a) : Antonio
Por favor entre com sua idade: 
53
Por favor entre com o nome da cidade natal: 
Belo Horizonte
O senhor(a) Antonio nasceu em Belo Horizonte e o ano de nascimento é: 1970    
'''
