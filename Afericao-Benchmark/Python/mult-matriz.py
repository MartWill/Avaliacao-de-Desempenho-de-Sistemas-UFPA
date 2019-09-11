
import csv
import time


def mat_mul (A, B):

  num_linhas_A, num_colunas_A = len(A), len(A[0])
  num_linhas_B, num_colunas_B = len(B), len(B[0])
  assert num_colunas_A == num_linhas_B

  C = []
  for linha in range(num_linhas_A):
    C.append([])
    for coluna in range(num_colunas_B):
      C[linha].append(0)
      for k in range(num_colunas_A):
        C[linha][coluna] += A[linha][k] * B[k][coluna]
        
  return C 

if __name__ == '__main__':

  tempoDeInicio = time.time()

  '''Leitura da tabela 1'''
  with open('500_01.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    a = [row for row in csv_reader]

  for i in range(len(a)):
    for j in range(len(a[0])):
      a[i][j] = int(a[i][j])

  '''Leitura da tabela 2'''
  with open('500_02.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    b = [row for row in csv_reader]

  for i in range(len(b)):
    for j in range(len(b[0])):
      b[i][j] = int(b[i][j])

  with open('resultados.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(mat_mul(a,b))


  arquivo = open('time.txt', 'r')
  conteudo = arquivo.readlines()

  conteudo.append( str(time.time() - tempoDeInicio ) +  '\n')

  arquivo = open('time.txt', 'w')
  arquivo.writelines(conteudo)
  arquivo.close()






