
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    
for i = 1 to 10
    print(i)
    
for <item> in <conjunto_de_itens>:
    <bloco_de_codigo>
    
frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
    print(fruta)
# Resultado
Abacaxi
Morango
Uva 

for fruta in ['Abacaxi', 'Morango', 'Uva']:
    print(fruta)
'''
Resultado:
Abacaxi
Morango
Uva
'''   

palavra = "Vamos estudar Python"
for letra in palavra:
    print(letra)    
    
for <item> in <conjunto_de_itens>:
    <bloco_de_codigo>
    if <condicao_verdadeira>:
         <outras_instrucoes>
         break    
     
pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
                     ({'nome': 'Maria', 'cidade': 'São Paulo'}),
                     ({'nome': 'Pedro', 'cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], "mora em", pessoa['cidade'])
        break
'''
Resultado:
1
2
Maria mora em São Paulo
'''
pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
                     ({'nome': 'Maria', 'cidade': 'São Paulo'}),
                     ({'nome': 'Pedro', 'cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Maria':
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])
'''
Resultado:
1
João mora em Belo Horizonte
3
Pedro mora em Curitiba
'''
 range(início, parada, incremento)

for numero in range(10):
    if numero % 2 == 0:
        print("O número", numero, "é par")
'''
Resultado:
O número 0 é par
O número 2 é par
O número 4 é par
O número 6 é par
O número 8 é par
'''

for numero in range(10, 21):
    if numero % 2 == 0:
        print("O número", numero, "é par")
Resultado:
O número 10 é par
O número 12 é par
O número 14 é par
O número 16 é par
O número 18 é par
O número 20 é par
'''    
for <item> in <conjunto_de_itens>:
   <bloco_de_codigo>
else:
   <novo_bloco_de_codigo>
Veja um pequeno exemplo:

frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
    print(fruta)
else:
    print("Laço de repetição finalizado.")
'''
Resultado:
Abacaxi
Morango
Uva
Laço de repetição finalizado.
'''
for numero_coluna1 in range(2, 5):
    print("Tabuada do ", numero_coluna1)
    for numero_coluna2 in range(11):
        print(numero_coluna1, "x", numero_coluna2, " = ", numero_coluna1 * numero_coluna2)
'''
 Resultado:
 Tabuada do 2
 2 x 0 = 0
 2 x 1 = 2
 2 x 2 = 4
 2 x 3 = 6
 2 x 4  = 8
 2 x 5 = 10
 2 x 6 = 12
 2 x 7 = 14
 2 x 8 = 16
 2 x 9 = 18
 2 x 10 = 20
 Tabuada do 3
 3 x 0 = 0
 3 x 1 = 3
 3 x 2 = 6
 3 x 3 = 9
 3 x 4 = 12
 3 x 5 = 15
 3 x 6 = 18
 3 x 7 = 21
 3 x 8 = 24
 3 x 9 = 27
 3 x 10 = 30
 Tabuada do 4
 4 x 0 = 0
 4 x 1 = 4
 4 x 2 = 8
 4 x 3 = 12
 4 x 4 = 16
 4 x 5 = 20
 4 x 6 = 24
 4 x 7 = 28
 4 x 8 = 32
 4 x 9 = 36
 4 x 10 = 40
 '''
 https://www.datacamp.com/tutorial/python-enumerate-tutorial?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=143216588537&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=665485585140&utm_targetid=dsa-1947282172981&utm_loc_interest_ms=&utm_loc_physical_ms=1001566&utm_content=dsa~page~community-tuto&utm_campaign=230119_1-sea~dsa~tutorials_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-ltsjul23&gclid=CjwKCAjw_aemBhBLEiwAT98FMj7fJgeex9oe0GAuckBVJI6vDmFiztwwY_oRc2COcB_Y7DLLz57aoxoC2mIQAvD_BwE
 drinks = ['tea', 'coffee', 'cappuccino', 'lemonade']
enumerated_drinks = enumerate(drinks)
print(type(enumerated_drinks))
print(enumerated_drinks)

 OpenAI
This code creates a list of drinks called drinks with four elements.
• Then, the enumerate() function is used to create an enumerated object called enumerated_drinks, which contains tuples of the form (index, value) for each element in the drinks list.
• The print() function is used to display the type of the enumerated_drinks object, which is a enumerate object, and the contents of the enumerated_drinks object.
• The output of the code will be:````The memory address will vary depending on the system running the code.

print(enumerated_drinks[0])

 OpenAI
This code uses the Python programming language to print the first element of a list called enumerated_drinks.
• The enumerated_drinks list has been created using the enumerate() function, which adds an index number to each element of another list.
• The [0] at the end of the code snippet accesses the first element of the enumerated_drinks list, which is a tuple containing the index number and the first element of the original list.
• The print() function then outputs this tuple to the console.

list_enumerated_drinks = list(enumerated_drinks)
print(list_enumerated_drinks)

 OpenAI
This code snippet is written in Python.
• The code creates a new list called list_enumerated_drinks by converting the enumerated_drinks object into a list using the list() function.
• The enumerated_drinks object is likely a Python enumerate object, which is created by calling the enumerate() function on a list or other iterable object.
• The print() function is then used to display the contents of the list_enumerated_drinks list.

[(0, 'tea'), (1, 'coffee'), (2, 'cappuccino'), (3, 'lemonade')]

 OpenAI
This code creates a list of tuples, where each tuple contains an integer and a string representing a beverage.
• The integers in the tuples are assigned automatically by Python, starting from 0 and incrementing by 1 for each tuple.
• The output of this code would be:``[(0, 'tea'), (1, 'coffee'), (2, 'cappuccino'), (3, 'lemonade')]``This list of tuples could be used to represent a menu of beverages in a coffee shop or restaurant, for example.

numerated_drinks = enumerate(drinks)
print(next(enumerated_drinks))
print(next(enumerated_drinks))
print(next(enumerated_drinks))
print(next(enumerated_drinks))
print(next(enumerated_drinks))

 OpenAI
This code uses the built-in enumerate() function in Python to create an iterator that pairs each element of the drinks list with its index.
• The enumerate() function takes an iterable (in this case, the drinks list) and returns an iterator that produces tuples containing the index of each element and the element itself.
• The next() function is then used to retrieve the next item from the iterator.
• In this case, it is called five times to retrieve the first five items from the enumerated_drinks iterator.
• Each call to next() returns a tuple containing the index and the corresponding element from the drinks list.
• The output of this code will be the first five elements of the drinks list, along with their indices.

print(list(enumerated_drinks))

 OpenAI
This code snippet is written in Python.
• The enumerated_drinks variable is assumed to be a list of drinks.
• The list() function is used to convert the enumerated_drinks object into a list.
• The enumerated_drinks object is created using the enumerate() function, which takes an iterable (in this case, a list of drinks) and returns an iterator that produces tuples containing the index and the value of each element in the iterable.
• The print() function is then used to output the resulting list of tuples, where each tuple contains the index and the corresponding drink.

drinks = ('tea', 'coffee', 'cappuccino', 'lemonade')
enumerated_drinks = enumerate(drinks)
print(enumerated_drinks)

<enumerate object at 0x000002DC3A098D40>

dict_enumerated_drinks = dict(enumerated_drinks)
print(dict_enumerated_drinks)

print(dict_enumerated_drinks[0])
print(dict_enumerated_drinks[3])

enumerated_hello_world = enumerate('Hello, World!', start=10)
print(enumerated_hello_world)

________________

http://unicode.org/emoji/charts/full-emoji-list.html
__________
______

'''
Ranges

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for
Ranges são utlizados para gerar sequências numéricas, não de forma aleatória mas sim de
maneira especificada.
formas gerais:
range (valor_de_parada)
OBS:
valor_de parada não inclusive (inicio padrão ) e passo de 1 em 1)


#ex.:1
for num in range(11):
    print(num)
    
Resultado:
0
1
2
3
4
5
6
7
8
9
10 

#ex.:2
OBS:
valor_de parada não inclusive (inicio especificado pelo usuário e passo de 1 em 1)
for num in range(1, 10):
    print(num)
    
Resultado:
1
2
3
4
5
6
7
8
9

ex.:3
OBS:
valor_de parada não inclusive (inicio especificado pelo usuário e passo especificado pelo 
usuário)
          
for num in range(1, 10, 2):
    print(num)
Resultado:
1
3
5
7
9 

# ex.:4 Inversar
OBS:
valor_de parada não inclusive (valor_inicio especificado pelo usuário e passo especificado pelo 
usuário)
           
for num in range(10, 1, -1):
    print(num)
#Resultado:                                                                                                                                                                 >>> 
'''