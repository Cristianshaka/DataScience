import pandas as pd
import numpy as np // arrays multidimensionais (armazenar dados em mais de uma dimensão por exemplo, matrizes, tensores) e funções matemáticas de alto desempenho
import seaborn as sns // Uma biblioteca de visualização de dados baseada no Matplotlib, que oferece uma interface de alto nível para criar gráficos estatísticos
import matplotlib.pyplot as plt // Uma biblioteca de visualização de dados que fornece uma maneira versátil de criar gráficos

sns.countplot(x='target', hue='target', data=df)
plt.title('Distribuição de Sentimentos')
plt.xlabel('Classes')
plt.ylabel('Frequência')
plt.legend(labels=[f'Negativo = {len(df[df["target"] == 0])}',
                   f'Positivo = {len(df[df["target"] == 4])}'])
plt.show()
