vetor = [1, 2, 3, 4, 5]
vetor2 = [6, 7, 8, 9, 10]

matriz = [vetor, vetor2]
for linha in matriz:
  print(linha)
print('Número de linhas: ', len(matriz)) # exibe quantos arrays foram empilhados, ou o numero de linhas
print('Número de colunas: ', len(matriz[0])) # exibe quantos elementos existem dentro de cada array, ou as colunas

#              0          1          2
matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(matriz2)): # primeiro itera sobre o tamanho da matriz, duas linhas
  for j in range(len(matriz2[0])): # agora itera sobre quantos elementos temos em cada linha da matriz
    print(matriz2[i][j], end=' ') # adiciona espaço em brando para melhor vosualização
  print() # print para pular linha após exibir todos os valores de uma linha da matriz


