# Biblioteca pra conexão com o drive
from google.colab import drive
drive.mount('/content/drive')

# Carregar o dataset para um dataframe no pandas
dataset_path = '/content/drive/MyDrive/Colab Notebooks/DataFrames/training.1600000.processed.noemoticon.csv'  # Substitua pelo seu caminho do arquivo CSV
df = pd.read_csv(dataset_path, encoding='latin-1') # enconding que suporta dados
                                  # de linguas ocidentais como ingles e portugues
display(df)

# Visualizando as primeiras linhas
df.head()

# Visualizando as ultimas linhas
df.tail()

# Visualizando as colunas
df.columns

# alterando o nome das colunas
df.columns = ['target', 'id', 'date', 'flag', 'user', 'text']
print(df.columns)
df.head()

# Resumo do DataFrame
df.info()

# Estatísticas descritivas sobre as colunas
df.describe()

# Formato do dataframe, linhas e colunas
print("Dimensões: ", df.shape)
print("Linhas: ", df.shape[0])
print("Colunas: ", df.shape[1])

 #axis=0 significa "ao longo das linhas" e, portanto, corresponde ao índice das linhas.
#axis=1 significa "ao longo das colunas", então corresponde ao índice das colunas.

# Tipagem dos dados, inteiros, booleanos e etc
df.dtypes
# Verificando ausência de valores
df.isnull().sum()
# Visualizando o balanceamento da coluna target
df['target'].value_counts()
