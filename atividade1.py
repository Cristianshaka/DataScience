import pandas as pd

# Criando DataFrame
df = pd.DataFrame({'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]})

#Mostre quantas linhas e quantas colunas ele tem
print("Linhas e colunas:", df.shape)
 #Mostre os valores da segunda coluna
print(df['B'])
#Mostre os valores da segunda linha
print("Valores da segunda linha:")
print(df.iloc[1])
