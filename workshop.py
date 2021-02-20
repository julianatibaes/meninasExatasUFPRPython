# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:19:37 2021

@author: Juliana Tibães

FONTES:
    https://medium.com/data-hackers/implementando-regress%C3%A3o-linear-simples-em-python-91df53b920a8
    https://neylsoncrepalde.github.io/2018-02-25-regressao-linear-python/
    https://imasters.com.br/back-end/data-science-regressoes-com-python
    https://www.w3schools.com/python/
    https://datahackers.com.br/
    https://github.com/PizzaDeDados/datascience-pizza
    
"""

'''
Operações básica
'''

a = 5
b = 9

#soma
soma = a + b
print(soma)

#subtração
sub = a - b
print(sub)

#multiplicação
mult = a * b
print(mult)

#divisão
div = a / b
print(div)

#resto
resto = a % b
print(resto)


'''
Matrizes
'''

# Array ... lista
l = [0, 1, 2, 3, 4]
print("lista = ", l)

# Matriz 2x2
m = [[0,1], [3,4]]
print("matriz = ", m)

# Matriz 2x2 também, mas agora vamos usar a biblioteca numpy.
# Essa biblioteca é bem bacana e tem várias funções para trabalhar com tabelas
import numpy as np
v = np.array([1,2,3,4]).reshape(2,2)
print(v)


'''
Laços e condicionais.
Vamos misturar algumas coisas e colocar em prática em alguns exercícios
que talvez você já tenha ouvido falar
'''

# O bloco abaixo é um verificador de números primos
'''
Como ele funciona?
Primeiro nós recebemos um número inteiro (int) digitado no console
Também declaramos uma variavel (mult) auxiliar para sabermos se o número
em algum momento apresentou ter algum multiplo

Ai declaramos um laço (for) que vai de 2 até n (que foi o número digitado)
para cada iteração ele vai jogar o número na variável count
E acada interação ele vai verificar se(if) o resto da divisão do número digitado
pelo contador do laço é ou não igual a zero.
Caso seja, será impresso no console o múltiplo do número e a variável mult receberá
o próprio valor somado ao valor 1

Depois de percorrer todo o laço, verificaremos se (if) a variável mult NÃO foi alterada
Caso seja verdadeiro, imprimierá que o número é primo
Senão (else) imprimirá a quantidade de números primos do número digitado
'''
n = int(input("Verificar número primo: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)
    
   
# O bloco abaixo mostrará todos os números primos existentes até o valor digitado
'''
Como ele funciona?
Primeiro nós recebemos um número inteiro (int) digitado no console
Vamos declarar numbers que irá juntar o número digitado com os valores 1 e -1
Também vamos definir uma lista (primers)

Enquanto estivermos percorrendo os valores até o número digitado
a variável p receberá numbers menos um valor digitado
a lista primers adicionará o valor p
a lista numbers calculará a diferença entre o valor p*2, n+2, pulando de p em p (o valor de p)
por fim, apresentará a lista dos números primos
'''
n = int(input("Informe até qual número você quer os n primos: "))
numbers = set(range(n, 1, -1))
primes = []
while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
print(primes)    

'''
Agora vamos complicar um pouco mais!

Você já parou para pensar como alguns elementos à nossa volta podem ter um padrão?
Por exemplo, se quiser calcular o valor de uma casa. Você pode fazer uma regressão linear
(aquela famosa equeção da reta...) onde cada variável representa um fator do problema 
a ser representado.
Por exemplo:
    x1 = área
    x2 = quartos
    x3 = localização

E a relação desses três fatores geram o preço.
Essa relação pode ser determinística ou não determinística

Uma relação determínistica, por exemplo, 
é quando queremos saber a distância percorrida por um carro, 
mantendo velocidade constante $v$ ao longo de $\Delta t$ segundos. 

Um exemplo de variáveis relacionadas de maneira não determinística é se 
quisessemos saber o tamanho do vocabulário de uma criança (y)
sabendo idade dessa criança (x). Não é algo exato.

Talvez seja mais fácil olhar um gráfico disso!

'''
# importar pacotes necessários
import numpy as np
import matplotlib.pyplot as plt
 
# exemplo de plots determinísticos
np.random.seed(42)
det_x = np.arange(0,10,0.1)
det_y = 2 * det_x + 3
 
# exemplo de plots não determinísticos
non_det_x = np.arange(0, 10, 0.1)
non_det_y = 2 * non_det_x + np.random.normal(size=100)
 
# plotar determinísticos vs. não determinísticos
fig, axs = plt.subplots(1, 2, figsize=(10,4), constrained_layout=True)
 
axs[0].scatter(det_x, det_y, s=2)
axs[0].set_title("Determinístico")
 
axs[1].scatter(non_det_x, non_det_y, s=2)
axs[1].set_title("Não Determinístico")
 
plt.show()


'''
Na vida real, termos um problema não deterministico é muito mais comum do que se imagina

Por isso, usamos um método para verificar se uma reta oferece um bom ajuste
aos dados, o Método dos Mínimos Quadrados

Através desse método é possível traçar uma reta  que tem o melhor ajuste possível 
 na qual se tem a menor soma possível de desvios quadrados
 
'''

'''
Na prática, nos vamos utilizar um conjunto de bibliotecas de machine learning
que irá realizar todos os cálculos estatísticos para nós sem grandes esforços
'''
from sklearn.linear_model import LinearRegression
 
# criar modelo linear e otimizar
lm_model = LinearRegression()
lm_model.fit(non_det_x.reshape(-1,1), non_det_y)
 
# extrair coeficientes
slope = lm_model.coef_
intercept = lm_model.intercept_


# imprimir os valores encontrados para os parâmetros
print("b0: \t{}".format(intercept))
print("b1: \t{}".format(slope[0]))


# plotar pontos e retas com parâmetros otimizados
plt.scatter(non_det_x, non_det_y, s=3)
plt.plot(non_det_x, (non_det_x * slope + intercept), color='r')
 
plt.show()


'''
Neste exemplo, nós utilizamos os dados gerados aleatóriamente,
porém podemos utilizar dados gerados por outras fontes, 
como um conjunto de dados de pacientes em uma clínica, em uma escola, em uma estação meteorológica, etc.
E esses dados podem estar armazenados em tabelas Excel ou CSV, por exemplo =]

Não se esqueça de que ao utilizar dados de pessoas, é necessário o concentimento delas e cuidar para que nenhum dado pessoal seja exposto de forma indevida.
'''
