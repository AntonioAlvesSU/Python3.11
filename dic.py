#Dicionário é dado por {},
''' 
print(type({}))
Dicionarios = {'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo'}
print(type(Dicionarios))
print(Dicionarios)
print(Dicionarios['br'])
print(Dicionarios.get('br'))
'''
'''
Country = {'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo'}
print('br' in Country)
print('us' in Country)
print('sp' in Country)
print('op' in Country)

True
True
True
False
'''
'''
Country = {'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo'}
Country.update({'co':'Colombia'})
print(Country)
#{'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo', 'co': 'Colombia'}
Country['co'] = 'Coreia'
print(Country)
#{'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo', 'co': 'Coreia'}
Country.update({'co': 'Croácia'})
print(Country)
#{'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo', 'co': 'Croácia'}

Country ={'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo', 'co': 'Croácia'}  
Country.pop('co')
print(Country)
# {'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo'}
del Country['sp']    
print(Country) 
#{'br': 'Brasil', 'us': 'Estados Unidos da America

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
'''


'''
carrinho = []
produto1=['arroz', 4, 23,00]
produto2=['feijão', 5, 12,00]
carrinho= produto1 + produto2
print(carrinho)

carrinho = []
produto1=['arroz', 4, 23,00]
produto2=['feijão', 5, 12,00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

produto1=['arroz', 4, 23,00]
produto2=['feijão', 5, 12,00]
carrinho = (produto1, produto2)
print(carrinho)

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

s = set({1, 2, 3, 4, 5, 5,  6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s)
print(type(s))

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla}  com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario}  com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto}  com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
   
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))   
print(len(set(cidades)))

s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s) 

s.remove(3)  #  NÃO é índice! Informamos o valor a ser removido.

print(s)

#Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)
''' 
# Forma 2 - Shallow Copy
s = {1, 2, 3}
novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)