import pandas as pd

# Não esqueça de fornecer o nume das colunas
df_matriz = pd.DataFrame(matriz2, columns=['A', 'B', 'C'])
df_dicionario = pd.DataFrame({'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]})

#O pandas também permite fácil acesso a índices e operações com os DataFrames
print(df_dicionario.shape)
print(df_dicionario.columns)

# Acessando colunas e linhas especificas
print('Todas as linhas da coluna A:')
df_dicionario['A']

print("Todas as linhas da coluna B:")
df_dicionario.iloc[:, 1]

print("Todas as colunas da linha 0:")
df_dicionario.iloc[0, :]

