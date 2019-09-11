import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import csv
import pandas as pd
import io
from numpy import genfromtxt

#leitura dos arquivos
path = raw_input("digite o path do arquivo desejado:\n")
arr = genfromtxt(str(path), delimiter=',',dtype=int)
arr = arr[1].flatten()

#criacao dos histograma dos dados
a = (min(arr))
b = (max(arr))
plt.figure(1)
result = plt.hist(arr)
plt.xlim(a, b)
#criando uma gaussiana para representar a distribuicao	 dados
mean = np.mean(arr)
variance = np.var(arr)
sigma = np.sqrt(variance)
x = np.linspace(min(arr), max(arr), 100)
dx = result[1][1] - result[1][0]
scale = len(arr)*dx
plt.plot(x, mlab.normpdf(x, mean, sigma)*scale)

plt.show()
