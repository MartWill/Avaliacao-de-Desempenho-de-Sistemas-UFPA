# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:07:04 2019

@author: fredl
"""
import csv
import matplotlib.pyplot as plt
import numpy  as np
from scipy.stats import norm

#leitura do arquivo
#para leroutro arquivo, mude o path eo nome do aruivo
with open (r'C:\Users\fredl\Downloads\Claro_BR_2019.09.25_11.48.15.txt','r') as f:
    #extrai as informações dos dados, row[0]= timestamp,row[1]=longtude,row[2] = latitude, row[3] = operadora, row[4] = tipo,row[5] = level,row[6] = spee,row[7] = altitude, 
    arr = [row[6] for row in csv.reader(f,delimiter='\t')]

#selciona do segundo ao ultimo,pq o primeiro é o nome da categoria
arr = arr[1:-1]
#transforma os valores pra int
arr = list(map(int,arr))
#tira o maximo e o minimo
a = (min(arr))
b = (max(arr))

#print (arr)

#plotagem
plt.figure()
#az o histograma
result = plt.hist(arr,bins=5,alpha=0.75)
plt.xlim(a, b)
#criando uma gaussiana para representar a distribuicao	 dados
mean = np.mean(arr)
variance = np.var(arr)
sigma = np.sqrt(variance)
x = np.linspace(min(arr), max(arr), 100)
dx = result[1][1] - result[1][0]
scale = len(arr)*dx

plt.title('Distribuição das velocidades sinal do 4G da operadora claro')
plt.xlabel('speed')
plt.ylabel('')
print(mean,variance)
plt.plot(x, norm.pdf(x, mean, sigma)*scale,linewidth=6.0)
plt.figtext(0.65, 0.75, 'média= %f' % mean,wrap=True)
plt.figtext(0.65,0.70, 'variância= %f' % variance)

