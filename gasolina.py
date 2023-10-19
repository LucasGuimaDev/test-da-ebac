import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arquivo = '/content/test-da-ebac/gasolina.csv'
gasolina_df = pd.read_csv(arquivo)

gasolina_df.head(50)

sns.set(style="whitegrid")  
sns.lineplot(x='dia', y='venda', data=gasolina_df, color='red')


plt.title('Gráfico de valor da gasolina')
plt.xlabel('Dia')
plt.ylabel('Valor')

plt.show()

plt.savefig("gasolina.png")