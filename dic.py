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

# Forma 2 - Shallow Copy
s = {1, 2, 3}
novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}


# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
#{'Gustavo', 'Ana', 'Pedro', 'Guilherme', 'Marcos', 'Ellen', 'Patricia', 'Julia', 'Fernando'}
unicos1 = estudantes_python | estudantes_java
print(unicos1)
#{'Gustavo', 'Ana', 'Pedro', 'Guilherme', 'Marcos', 'Ellen', 'Patricia', 'Julia', 'Fernando'}
unicos1 = estudantes_python.difference(estudantes_java) 
print(unicos1)
#{'Guilherme', 'Marcos', 'Ellen', 'Pedro'}
unicos1 = estudantes_java.difference(estudantes_python)
print(unicos1)
#{'Fernando', 'Gustavo', 'Ana'}
unicos1 = estudantes_python & estudantes_java
print(unicos1)
#{'Julia', 'Patricia'}
unicos1 =  estudantes_java & estudantes_python 
print(unicos1)
#{'Julia', 'Patricia'}
s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
""
21
6
1
6
"""

from collections import Counter
# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
res = Counter(lista)
print(res)
print(type(res))
#Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
#<class 'collections.Counter'>

texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet 
sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​, que todos possam editar 
e melhorar. O projeto é definido pelos princípios fundadores. O conteúdo é disponibilizado sob a licença Creative 
Commons BY-SA e pode ser copiado e reutilizado sob a mesma licença — mesmo para fins comerciais — desde que 
respeitando os termos e condições de uso. """

palavras = texto.split() # dividiu o texto em palavras
print(palavras)
resu = Counter(palavras)
print(resu)
"""
['A', 'Wikipédia', 'é', 'um', 'projeto', 'de', 'enciclopédia', 'colaborativa,', 'universal', 'e', 'multilíngue', 'estabelecido', 'na', 'internet', 'sob', 'o', 'princípio', 'wiki.', 'Tem', 'como', 'propósito', 'fornecer', 'um', 'conteúdo', 'livre,', 'objetivo', 'e', 'verificável\u200b\u200b,', 'que', 'todos', 'possam', 'editar', 'e', 'melhorar.', 'O', 'projeto', 'é', 'definido', 'pelos', 'princípios', 'fundadores.', 'O', 'conteúdo', 'é', 'disponibilizado', 'sob', 'a', 'licença', 'Creative', 'Commons', 'BY-SA', 'e', 'pode', 'ser', 'copiado', 'e', 'reutilizado', 'sob', 'a', 'mesma', 'licença', '—', 'mesmo', 'para', 'fins', 'comerciais', '—', 'desde', 'que', 'respeitando', 'os', 'termos', 'e', 'condições', 'de', 'uso.']
Counter({'e': 6, 'é': 3, 'sob': 3, 'um': 2, 'projeto': 2, 'de': 2, 'conteúdo': 2, 'que': 2, 'O': 2, 'a': 2, 'licença': 2, '—': 2, 'A': 1, 'Wikipédia': 1, 'enciclopédia': 1, 'colaborativa,': 1, 'universal': 1, 'multilíngue': 1, 'estabelecido': 1, 'na': 1, 'internet': 1, 'o': 1, 'princípio': 1, 'wiki.': 1, 'Tem': 1, 'como': 1, 'propósito': 1, 'fornecer': 1, 'livre,': 1, 'objetivo': 1, 'verificável\u200b\u200b,': 1, 'todos': 1, 'possam': 1, 'editar': 1, 'melhorar.': 1, 'definido': 1, 'pelos': 1, 'princípios': 1, 'fundadores.': 1, 'disponibilizado': 1, 'Creative': 1, 'Commons': 1, 'BY-SA': 1, 'pode': 1, 'ser': 1, 'copiado': 1, 'reutilizado': 1, 'mesma': 1, 'mesmo': 1, 'para': 1, 'fins': 1, 'comerciais': 1, 'desde': 1, 'respeitando': 1, 'os': 1, 'termos': 1, 'condições': 1, 'uso.': 1})
"""
print(resu.most_common(5))
#[('e', 6), ('é', 3), ('sob', 3), ('um', 2), ('projeto', 2)]
print(dir(resu))

from collections import defaultdict
dicionatio = defaultdict(lambda : 0)

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)
# {'curso': 'Programação em Python: Essencial'}
print(dicionario['curso'])
#Programação em Python: Essencial
print(dicionario['outro'])  
#Traceback (most recent call last):
#File "c:\Informinas\meus\python\dic.py", line 224, in <module>
#print(dicionario['outro'])  # ??? KeyError
'''
# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 4, 'c': 5, 'd': 2, 'e': 3}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""
chave=a:valor=1
chave=b:valor=4
chave=c:valor=5
chave=d:valor=2
chave=e:valor=3
"""
from collections import OrderedDict
dic1 =  {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dic1==dict2)
#True

dic1 = OrderedDict ({'a': 1, 'b': 2})
dict2 =OrderedDict({'b': 2, 'a': 1})
print(dic1==dict2)
#False

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')


#print(dir(dic1))
"""
    ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'move_to_end', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""