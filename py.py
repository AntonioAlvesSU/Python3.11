'''
Loop com While
'''
Ex.:1
num = 1
while num < 10:
    print(num)    # nesta situação entrará   em loop infinito
	
while num < 10:
    print(num)     #obs.: O loop infinito serve para varrer tela
	 num = num + 1 #Porém é muito importante que verifiquemos o  ponto de parada

num = int(input('Ensira valores inteiros? ') )
while num < 10 :
     print(num) 
     num = num + 1	 

Ex.:2
resposta = ''
while resposta != sim:
	resposta = input('Já acabou o serviço?  ')
	
'''
Saindo do loop com break
'''

Ex.:1
for num in range(1, 11):
    print(num)
    if num == 10:
        break
print('Saindo do Loop')

Ex.:2
while true:
    comando = input('Digite para sair do loop:  ')
        break
print('Saindo do Loop')		

'''
Listas
#>>> list('antonio augusto')
['a', 'n', 't', 'o', 'n', 'i', 'o', ' ', 'a', 'u', 'g', 'u', 's', 't', 'o']
#>>> list(range[11])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type 'range' is not subscriptable
#>>> list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#>>> type([])
<class 'list'>
#>>> type('Antonio')
<class 'str'>

lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))
#Podemos localizar facilemente um valor contido em uma lista

if 15 in lista5:
    print('O numero foi encotrado')
else:
    print('O numero não foi encotrado')
    
if 50 in lista5:
    print('O numero foi encotrado')
else:
    print('O numero não foi encotrado')   
    
num = input('Entre com valores reais:   ')
if num in lista5:
    print(f'O valor informado é {num}')
else:
    print(f' O caracter digitado não é o nuemro real que esta na lista5, o valor digitado é: {num}')
     
Resultado:
O numero foi encotrado
O numero não foi encotrado
Entre com valores reais:   5
O valor informado é 5
  
O numero foi encotrado
O numero não foi encotrado
Entre com valores reais:   l
 O caracter digitado não é o nuemro real que esta na lista5, o valor é: l

O numero foi encotrado
O numero não foi encotrado
Entre com valores reais:   a
 O caracter digitado não é o nuemro real que esta na lista5, o valor digitado é: a      

lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))

#lista1.sort()
lista2.sort()
print(lista2)
#resultado:
#lista1 = [1, 2, 4, 14, 19, 78]
#lista2 = ['a', 'i', 'n', 'o', 'o', 't']       

#podemos facilemte contar o número de ocorrências  de um valor em uma lista
lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))

print(lista1.count(1)) 
print(lista2.count('o'))
#Resultado:     
#1
#2   

lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))

print(lista1)
lista1.append(24) #com o apend nós podemos adicionar elementos na lista, apenas um por vez
print(lista1)
#Resultado:
#[1, 2, 4, 19, 78, 14]
#[1, 2, 4, 19, 78, 14, 24]  

lista1 = [1, 2 ,4 ,19 ,78, 14]
lista2 = ['a','n','t','o', 'i','o']
lista3 = []
lista4 = list('Antonio Augusto')
lista5 = list(range(20))       
  
lista1.append([21, 34, 45, 67,78,98]) #Coloca a lista como um unico elemento (sublista)
print(lista1)
#Resultado:[1, 2, 4, 19, 78, 14, [21, 34, 45, 67, 78, 98]]
if [21, 34, 45, 67,78,98] in lista1:
    print('Encontrei a lista')
else:
    print('não encotrei a  lista')
#Resultado:
#[1, 2, 4, 19, 78, 14, [21, 34, 45, 67, 78, 98]]
#Encontrei a lista 

lista1.extend([45, 123, 48,])
print(lista1)
#resultado =  [1, 2, 4, 19, 78, 14, [21, 34, 45, 67, 78, 98], 45, 123, 48] # Coloca cada elemento da lista como valor adicional a lista
'''
-------------------------------------------------------
#6-Leia a temperatura em graus 'C' e converta 'F', segue formula: F=C * (9.0 / 5.0) + 32.0 :

#25-Leia em acres   e converate em metros_quadrados, a formula é : M = A * 4048,48  :

print('Por favor digite uma velocidade em acres: ')
acres = float(input("O valor é : \n"))
metros_quadrados= (acres * 0.000247)
print('Resultado da conversão é : \n', metros_quadrados)

#26-Leia em metros_quadrados   e converate em hectares , a formula é : H = M * 0.0001  :

print('Por favor digite uma velocidade em metros_quadrados: ')
metros_quadrados = float(input("O valor é : \n"))
hectares= (metros_quadrados * 0.0001)
print('Resultado da conversão é : \n', hectares)

#27-Leia em hectares e converate em metros_quadrados , a formula é : M = H * 10000  :

print('Por favor digite uma velocidade em hectares: ')
hectares = float(input("O valor é : \n"))
metros_quadrados= (hectares * 10000)
print('Resultado da conversão é : \n', metros_quadrados)

#28-Leia três valores e represente a soma dos quadrados desses valores :

print('Por favor digite o valor1: ')
valor1 = float(input("O valor é : \n"))
valor1= (valor1 * valor1)
print('Por favor digite o valor2: ')
valor2 = float(input("O valor é : \n"))
valor2= (valor2 * valor2)
print('Por favor digite o valor3: ')
valor3 = float(input("O valor é : \n"))
valor3= (valor3 * valor3)
Total = valor1 + valor2 + valor3
print('Resultado da soma dos quadrados dos valores é : \n', Total)
---------------------------------
#29-Leia quatro valores e rcalcule a média aritimética e dê o reusltado:

print('Por favor digite o valor1: ')
valor1 = float(input("O valor é : \n"))
print('Por favor digite o valor2: ')
valor2 = float(input("O valor é : \n"))
print('Por favor digite o valor3: ')
valor3 = float(input("O valor é : \n"))
print('Por favor digite o valor4: ')
valor4 = float(input("O valor é : \n"))
Total = (valor1 + valor2 + valor3 + valor4) / 4
print('Resultado da soma dos quadrados dos valores é : \n', Total)

#30-Leia o valor em reais e a cotação do dolar e calcule o valor em dolar:

print('Por favor digite o valor em Reais: ')
Reais = float(input("O valor é : \n"))
print('Por favor digite a cotação do dolar_de_hoje: ')
Cotacao = float(input("O valor é : \n"))
Dolar = Reais / Cotacao
print('Resultado da soma dos quadrados dos valores é :  US$ ', round(Dolar,2))
---------------------------
#35-Leia os valores a e b são catetos de um triângulo, onde a hipotenusa é obtida pela equação =
#hipotenusa = √a²+ √b²
import math
print('Por favor digite o cateto A:')
catetoA = int(input("O valor é : "))
print('Por favor digite o cateto B:')
catetoB = int(input("O valor é : "))
hipotenusa = math.hypot(catetoA,catetoB)
print('A hipotenusa do triângulo :',round(hipotenusa,3))

#36-Leia altura e o raio de um cilindro circular e calcule o volume, formula : V = pi * raio² * altura, onde pi = 3,141592

import math
pi = 3.141592
print('Por favor digite o altura:')
altura = int(input("O valor é : "))
print('Por favor digite o raio:')
raio = int(input("O valor é : "))
volume = pi * raio** 2 * altura
print('O volume do cilindro é :',round(volume,3)

#37-Leia o valor do produto e imprima este valor com 12% de desconto:

import math

print('Por favor digite o valor do produto:')
valor = float(input("O valor é : "))
print('Por favor digite percentual de desconto:')
percentual = float(input("O valor é : "))
Valor_final_produto = valor * ((100 - percentual) / 100 )
print('O volume do cilindro é :',round(Valor_final_produto,3))

#38-Leia o valor do salario de um colaborador e imprima o novo_salario com 25% de aumento:

import math

print('Por favor digite o valor do salario:')
salario = float(input("O valor é : "))
print('Por favor digite percentual de aumento:')
percentual = float(input("O valor é : "))
novo_salario = salario * ((100 + percentual) / 100 )
print('O volume do cilindro é :',round(novo_salario,3))

#39-Leia o valor de R$ 780.000.00 será dividida em três, 1-parte receberá: 46%, 2-parte receberá 32% e 3-parte o restante:

import math
print('Por favor digite o valor do premio:')
premio = float(input("O valor é : "))
print('Por favor digite percentual do primeiro recebedor:')
primeiro = float(input("O valor é : "))
print('Por favor digite percentual do segundo recebedor:')
segundo = float(input("O valor é : "))
parte1 = premio * ((100 - primeiro)/100)
parte2 = (premio - parte1) * ((100-segundo) / 100)
parte3 = premio - parte1 - parte2
print('O valor da parte1 é : R$ ',round(parte1,2))
print('O valor da parte2 é : R$ ',round(parte2,2))
print('O valor da parte3 é : R$ ',round(parte3,2))

#40-uma empresa contrata um encanador a R$ 30.00 ao dia, faça um programa que solicite o numero de dias
# trabalhados pelo encanador e informe a quantia_liquida a ser paga já descontados 8% IR:

import math
diaria = 30.00
ir=8
print('Por favor digite os dias_trabalhados:')
dias_trabalhados = float(input("O valor é : "))
quantia_liquida_receber = dias_trabalhados * diaria * ((100 - ir)/100)
print('A quantia liquida a receber é : R$ ',quantia_liquida_receber)

_______

prog possua um vetor A que armazene 6 num inteiros. 
- atribua a sequencia ao vetor[1, 0, 5,-2,-5,7]
-Armazene em uma variável inteira(simples) a soma os valores das posições A[0],A[1] e A[5] do vetor e mostre na tela esta soma
-Modifique o vetor na posição 4, atribuindo a esta posição o valor 100
-Mostre na tela cada valor do vetor A, um em cada linha
------------
 *crie um prog que lê 6 valores inteiros e os mostre em tela
 *ler um conjunto de num reais , armazene em vetor , os conjuntos têm 10 elementos , imprimir em tela
 crie prog leia 8 posições e leia valores X e Y quaisquer correspondete ao vetor, ao final  seu prog escreverá a soma dos valores encontrados nas posições x e y
 

mensagem = input('Mensagem para alunos (Alunos separados por vírgula): ')
alunos = mensagem.split(',')
print(alunos)

print('1, 2, 3'.split(',') )