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
'''
Country ={'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo', 'co': 'Croácia'}  
Country.pop('co')
print(Country)
# {'br': 'Brasil', 'us': 'Estados Unidos da America', 'sp': 'São Paulo'}
del Country['sp']    
print(Country) 
#{'br': 'Brasil', 'us': 'Estados Unidos da America
'''
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
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





