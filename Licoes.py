'''
teste


#nome = 'God is Lord'
#print(nome)

#print(dir(nome))

#Recebendo dado 
nome = input("Qual seu nome: ")
print(f'Seja bem vindo(a) {nome}')
idade = input('Qual sua idade: ')
print(f'Cliente {nome} tem {idade} anos')
AnoDeNascimento = input(2023 - int(idade))
print(f'Senhor(a) {nome} nasceu em {AnoDeNascimento}')

#manipulando variaveis

nun = input('Entre com valor entre 1 e 10 : ')
print(f'Valor inserido é: {nun}')
nun = int(nun)  

if nun <= 15:
    nun += 20
    nun *= 2 
    nun /= 1 **2
    
    print(nun)      
else:    
    print('Esta situação não foi atendida')    

num = [1, 2, 3, 4, 5, 6]
for num in num:
    print(num)
  
frutas = ['Abacaxi', 'Morango', 'Uva']
for frutas in frutas:
    print(frutas) 
     
palavra = "Vamos estudar Python"
for letra in palavra:
    print(letra)

palavra = 'God is My lord' 
print(palavra[0:15]) 

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
 
pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
                     ({'nome': 'Maria', 'cidade': 'São Paulo'}),
                     ({'nome': 'Pedro', 'cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Pedro': #neste caso pulará o nome setado
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])

 #range(início, parada, incremento)

for numero in range(4, 12): #se determino o range o print sairá conforme o range
                            #mas se eu não determino o inicio , fica implicito o tamanho do range
    if numero % 2 == 0:
        print("O número", numero, "é par")        

frutas = ['Abacaxi', 'Morango', 'Uva', ]
for fruta in frutas:
    print(fruta)
else:
    print("Laço de repetição finalizado.")

for numero_coluna1 in range(2, 5):
    print("Tabuada do ", numero_coluna1)
    for numero_coluna2 in range(11):
        print(numero_coluna1, "x", numero_coluna2, " = ", numero_coluna1 * numero_coluna2)    

for numero in range(4, 12): #se determino o range o print sairá conforme o range
                            #mas se eu não determino o inicio , fica implicito o tamanho do range
    if numero % 2 == 0:
        print("O número", numero, "é par") 


num  = int(input('Entre com valores inteiros: ')) 
for num in range(0, num+1, 5 ):
    print(num) 
Resultado:
0
5
10
             
for num in range(10, -1, -1):
    print(num)
    
#U+1F604
#U0001F604 , http://unicode.org/emoji/charts/full-emoji-list.html

num = int(input('Entrada de valores inteiros: '))
for _ in range(3):
    for num in range(1, 15):
        print('\U0001F604' * num)
Resultado:
Entrada de valores inteiros: 10
😄
😄😄
😄😄😄
😄😄😄😄
😄😄😄😄😄
😄😄😄😄😄😄
😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄😄😄
😄
😄😄
😄😄😄
😄😄😄😄
😄😄😄😄😄
😄😄😄😄😄😄
😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄😄😄
😄
😄😄
😄😄😄
😄😄😄😄
😄😄😄😄😄
😄😄😄😄😄😄
😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄😄😄            

num = int(input('Entrada de valores inteiros: '))
for _ in range(3):
    for num in range(15, -1, -3):
        print('\U0001F604' * num)
Resultado:
Entrada de valores inteiros: 20
😄😄😄😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄
😄😄😄

😄😄😄😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄
😄😄😄

😄😄😄😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄😄😄😄
😄😄😄😄😄😄
😄😄😄 

----------
#enumerate
drinks = ('tea', 'coffe', 'milk'),
enumerate_drinks  = enumerate(drinks) 
print(enumerate_drinks) 
resposta:
<enumerate object at 0x0000021558682480>  
 
#enumerate
drinks = ('tea', 'coffe', 'milk'),
dict_enumerated_drinks = dict(enumerated_drinks)
#print(dict_enumerated_drinks) 

print(dict_enumerated_drinks[0])
print(dict_enumerated_drinks[3])
#resposta:

enumerated_hello_world = enumerate('Hello, World!', start=10)
print(enumerated_hello_world) 
    
drinks = ['tea', 'coffee', 'cappuccino', 'lemonade']
enumerated_drinks = enumerate(drinks)
print(type(enumerated_drinks))
print(enumerated_drinks)   

drinks = ('tea', 'coffe', 'milk')
for _drinks in enumerate(drinks[0:3]): #defino a quantida de posições acessadas
    print(drinks[:])
resposta:
"c:/Informinas/meus/python/loop for,py"
('tea', 'coffe', 'milk')
PS C:\Informinas\meus\python> & C:/Users/Informinas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Informinas/meus/python/loop for,py"
('tea', 'coffe', 'milk')
('tea', 'coffe', 'milk')
PS C:\Informinas\meus\python> & C:/Users/Informinas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Informinas/meus/python/loop for,py"
('tea', 'coffe', 'milk')
('tea', 'coffe', 'milk')
('tea', 'coffe', 'milk')        

pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
                     ({'nome': 'Maria', 'cidade': 'São Paulo'}),
                     ({'nome': 'Pedro', 'cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Null':
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])   
 
#Loop while
#Ex.:1
num = 1
while num < 10:
    print(num)   # nesta situação entrará   em loop infinito

#corrigindo o loop infinito
numero = 1
while numero <10:
     print(numero)
     numero = numero + 1  
      
Resposta:
1
2
3
4
5
6
7
8
9

resposta =''
while resposta != 'sim':
    resposta = input('Já acabou o serviço?  ')
print('Serviço finalizado!') 
resultado:
Já acabou o serviço?  nao
Já acabou o serviço?  onde
Já acabou o serviço?  que
Já acabou o serviço?  sim
Serviço finalizado! 
_____________________
Saindo do loop com break
    

for num in range(1, 11):
    print(num)
    if num == 6:
        break
print('Saindo do loop com break') 
resultado:
1
2
3
4
5
6
Saindo do loop com break       

while True:
    comando = input('Digite: sair => ')
    if comando == 'sair':
        break
print('Saindo do loop com break')
resultado:
Digite: sair => sair
Saindo do loop com break        
    
num = int(input('Ensira valores inteiros? ') )
while num < 10 :
     print(num) 
     num = num + 1
#reposta:
Ensira valores inteiros? 5
5
6
7
8
9     

resposta = ''
while resposta != 'sim':
    resposta = input('O serviço não acabou? ' )
print('sair do loop em caso afirmativo')
#resultado:
O serviço não acabou? que
O serviço não acabou? não 
O serviço não acabou? sei la
O serviço não acabou? para ho
O serviço não acabou? sim
sair do loop em caso afirmativo 

#Saindo do loop com break
for num in range(1, 11):
    print(num)
    if num == 10:
        break
print('Saindo do Loop')
#resultado:
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
Saindo do Loop       

while True:
    comando =input('Digite: sair /loop será interrompido=> ')
    print(comando)
    break
print('Saindo do loop')             
 
print(list (range(1, 11)))
print(list ('Antonio Augusto')) 
print(list (range(15 + 1))) 
Resultado:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PS C:\Informinas\meus\python> & C:/Users/Informinas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Informinas/meus/python/loop for,py"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['A', 'n', 't', 'o', 'n', 'i', 'o', ' ', 'A', 'u', 'g', 'u', 's', 't', 'o']
PS C:\Informinas\meus\python> & C:/Users/Informinas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Informinas/meus/python/loop for,py"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['A', 'n', 't', 'o', 'n', 'i', 'o', ' ', 'A', 'u', 'g', 'u', 's', 't', 'o']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
PS C:\Informinas\meus\python> & C:/Users/Informinas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Informinas/meus/python/loop for,py"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['A', 'n', 't', 'o', 'n', 'i', 'o', ' ', 'A', 'u', 'g', 'u', 's', 't', 'o']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))

if 15 in lista5:
    print('O numero foi encotrado')
else:
    print('O numero não foi encotrado')
    

print (list(range(20)))
num  = int(input('Entre com um valor dentro do range: '))
if num in lista5:
    print(f'Número encontrado {num}') 
    print(f'O número digitado é {num}')
else:
    print('O valor esta fora do range') 
    
Resultado:
O numero foi encotrado
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Entre com um valor dentro do range: 15
Número encontrado 15
O número digitado é 15
PS C:\Informinas\meus\python> & C:/Users/Informinas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Informinas/meus/python/loop for,py"
O numero foi encotrado
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Entre com um valor dentro do range: 30
O valor esta fora do range    

lista6 = [30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23] 
lista6.sort()
print(lista6)
lista4 = list('Antonio Augusto')
lista4.sort()
print(lista4)
 
lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))
lista6 = [30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23]
print(lista4.count('A'))
print(lista2.count('a')) 
resultado:
 
lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))
lista6 = [30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23]
lista6.append(26)
print(lista6)
#resultado:[30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23, 26] 

lista6 = [30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23, 26]
lista6.append([21, 34, 45, 67,78,98])
print(lista6)
#resultado: [30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23, 26, [21, 34, 45, 67, 78, 98]]
'''
lista6 = [30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23, 26, [21, 34, 45, 67, 78, 98]]
lista6.extend([45, 123, 48,])
print(lista6)
#resposta:[30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23, 26, [21, 34, 45, 67, 78, 98], 45, 123, 48]
lista6.extend('antonio')
print(lista6)
#resposta:
[30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23, 26, [21, 34, 45, 67, 78, 98], 45, 123, 48]
[30, 6, 7, 10, 67, 50, 79, 55, 65, 73, 99, 23, 26, [21, 34, 45, 67, 78, 98], 45, 123, 48, 'a', 'n', 't', 'o', 'n', 'i', 'o']


              