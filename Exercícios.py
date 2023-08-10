'''
6-Leia a temperatura em graus 'C' e converta 'F', segue formula: F=C * (9.0 / 5.0) + 32.0 :
'''
"""
valorCelsius = float(input('Entre com em celsius: '))
res = valorCelsius * (9.0 / 5.0) + 32.0
print(f'O valor correspondente em Fharenheit é: {res} ')
Entre com em celsius: 38
O valor correspondente em Fharenheit é: 100.4
#or
valorCelsius = float(input('Entre com em celsius: '))
print(f'O valor correspondente em Fharenheit é: {valorCelsius * (9.0 / 5.0) + 32.0} \n')
Entre com em celsius: 38
O valor correspondente em Fharenheit é: 100.4

valorCelsius = float(input('\n Entre com em celsius: '))
print(f'\n O valor correspondente em Fharenheit é: {valorCelsius * (9.0 / 5.0) + 32.0} \n')
 Entre com em celsius: 38

 O valor correspondente em Fharenheit é: 100.4

PS C:\Informinas\meus\python> 

#28-Leia três valores e represente a soma dos quadrados desses valores :
v1 = float(input('entre com valor: '))
v2 = float(input('entre com valor: '))
v3 = float(input('entre com valor: '))
print(f'\n A soma dos quadrados das parcelas é: {v1**2 + v2**2 + v3**2} \n')
as/meus/python/Exercícios.py
entre com valor: 20
entre com valor: 65
entre com valor: -112

 A soma dos quadrados das parcelas é: 17169.0

#30-Leia o valor em reais e a cotação do dolar e calcule o valor em dolar:
#hipotenusa = √a²+ √b² / import math
# calculando hipotenusa
va= float(input('\nEntre com o valor: '))
vb= float(input('Entre com o valor: '))
calc_hip= (va**2) + (vb**2)
print(f'O valor de hipotenusa é : {calc_hip} \n')
Entre com o valor: 5
Entre com o valor: 10
O valor de hipotenusa é : 125.0 

#36-Leia altura e o raio de um cilindro circular e calcule o volume, 
# formula : V = pi * raio² * altura, onde pi = 3,141592
#calculando volume
import math
pi = 3,141592
raio = float(input('\n Entre com valor: '))
h = float(input('\n Entre com valor: '))
v= pi * raio** 2 * h
print(f'O volume é: {v}')
print(type(v))

import math
pi = 3.141592
print('Por favor digite o altura:')
altura = int(input("O valor é : "))
print('Por favor digite o raio:')
raio = int(input("O valor é : "))
volume = pi * raio** 2 * altura
print(f'O volume do cilindro é :{volume}',)

pi = 3.141592
raio = float(input('\n Entre com valor: '))
h = float(input('\n Entre com valor: '))
v= pi * raio** 2 * h
print(f'O volume é: {v}')
print(type(v))
 Entre com valor: 10

 Entre com valor: 20
O volume é: 6283.184
<class 'float'>
#print('1, 2, 3'.split(',') )
dict_enumerated_
dict_enumerated_drinks = dict(enumerated_drinks)

#resultado: ['01', '02', '-15', '120']
#Entre o valor: 1
#Entre o valor: 2
#Entre o valor: 3
#Entre o valor: 4
#<class 'enumerate'>
#('1', '2', '3', '4')
#criando um vetor com seis elementos
'''
Entre o valor: 1
Entre o valor: 0
Entre o valor: 5
Entre o valor: -2
Entre o valor: -5
Entre o valor: 7
<class 'enumerate'>
('1', '0', '5', '-2', '-5', '7')
PS C:\Informinas\meus\python> 

#num = ['01', '02', '-15', '120']
num1 = input('Entre o valor: ')
num2 = input('Entre o valor: ')
num3 = input('Entre o valor: ')
num4 = input('Entre o valor: ')
num5 = input('Entre o valor: ')
num6 = input('Entre o valor: ')
Va =num1,num2,num3,num4,num5,num6
enumerated_va = enumerate(Va)
#print(type(enumerated_va))
print(Va)


num1 = input('Entre o valor: ')
num2 = input('Entre o valor: ')
num3 = input('Entre o valor: ')
num4 = input('Entre o valor: ')
num5 = input('Entre o valor: ')
num6 = input('Entre o valor: ')
Va =num1,num2,num3,num4,num5,num6
enumerated_va = enumerate(Va)
#print(type(enumerated_va))
#print(Va)
Va.sort()
print(Va)

carrinho = []
produto = ''

while produto != 'sair':
    print("Adione um produto na lista ou digite 'sair' para sair: \n") 
    produto = input()
    if produto != 'sair':
      carrinho.append(produto)
for produto in carrinho:
    print(produto)
print(carrinho)    

Va = []
num = ''
while num != 'sair':
    print("Entre com valores ou digite 'sair' para sair: ")
    num = input()
    if num != 'sair':
        Va.append(num)
for num in Va:
    print(num)
print(Va)

Va = []
num = ''
while num != 'sair':
    print("Entre com valores ou digite 'sair' para sair: ")
    num = input()
    if num != 'sair':
        Va.append(num)
for num in Va:
    print(num)
print(Va)
res:
10
5
6
2
1
['10', '5', '6', '2', '1']    
            
Va = []
num = ''
while num != 'sair':
    print("\new val. ou digite 'sair' para sair: ")
    num = input()
    if num != 'sair':
        Va.append(num)
for num in Va:
    print(num)
print(Va)
Va.reverse()
print(f'Va => {Va}')
Va.sort()
print(f'Va => {Va}')
res:
sair
1
2
3
4
5
6
7
['1', '2', '3', '4', '5', '6', '7']
Va => ['7', '6', '5', '4', '3', '2', '1']
Va => ['1', '2', '3', '4', '5', '6', '7']
    
Va = []
num = ''

while num != 'sair':
    print("\new val. ou digite 'sair' para sair: ")
    num = input()
    if num != 'sair':
        Va.append(num)
soma = 0        
for num in Va:
    print(num)
    soma = soma + int(num)
    print(soma)
    print(Va)
Va.reverse()
print(f'Va => {Va}')
Va.sort()
print(f'Va => {Va}')
res:
ew val. ou digite 'sair' para sair: 
1

ew val. ou digite 'sair' para sair: 
2
PS C:\Informinas\meus\python> & C:/Users/Informinas/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Informinas/meus/python/Exercícios.py

ew val. ou digite 'sair' para sair: 
10              

ew val. ou digite 'sair' para sair: 
6

ew val. ou digite 'sair' para sair: 
1

ew val. ou digite 'sair' para sair:
5

ew val. ou digite 'sair' para sair:
4

ew val. ou digite 'sair' para sair:
sair
10
10
['10', '6', '1', '5', '4']
6
16
['10', '6', '1', '5', '4']
1
17
['10', '6', '1', '5', '4']
5
22
['10', '6', '1', '5', '4']
4
26
['10', '6', '1', '5', '4']
Va => ['4', '5', '1', '6', '10']
Va => ['1', '10', '4', '5', '6']    

#Selection Sort
lista = [10, 9, 8, 7, 5, 3, 4, 3, 1, 2, 11,0,-1,-5]
lista_ordenada = []
tam = len(lista)
print(tam)
for i in range(tam):
 menor = lista[0]
 for j in range(len(lista)):
     if lista[j] < menor:
         menor = lista[j]
print(menor)         
pos_menor = j
lista_ordenada.append(menor)
lista.remove(menor)
print(lista_ordenada)
res:
14
-5
[-5]

Atribuição com slices
} Quando se usa slices numa atribuição, os elementos que
estão na fatia são substituídos
lista = [1,2,3,4,5]
 lista[1:3] = [‘a’, ‘b’]
print(lista)
[1, ‘a’, ‘b’, 4, 5]

Exemplo sem erro
>>> lista = [1, 2, 3, 4, 5]
>>> lista[0::2] = [‘x’, ‘y’, ‘z’]
>>> lista
[‘x’, 2, ‘y’, 4, ‘z’] 
 """
 










