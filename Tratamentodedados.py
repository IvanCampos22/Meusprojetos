#dados inconsistentes
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('C:/Users/IvanS/OneDrive/Área de Trabalho/script/ML/credit_data.csv')

#base_credit.loc[base_credit['age'] <0] # exibe idade menor que 0.

#excluindo dados
'''base_credit[base_credit['age']<0]# indentificando
base_credit2 = base_credit.drop(base_credit[base_credit['age']<0].index)
#print(base_credit2)
#print(plt.hist(x=base_credit2['age']))'''

#aterando dado
'''base_credit['age'].mean()
base_credit.loc[base_credit['age'] <0].mean()
base_credit['age'][base_credit['age']>0].mean()
base_credit.loc[base_credit['age'] <0, 'age'] = 40.92
print(base_credit.head(27))'''

#Dados Faltantes
#base_credit.isnull()# informa se tem dados faltando true falta false não falta
base_credit.isnull().sum() # informa a soma de dados faltando por coluna.

base_credit.loc[pd.isnull(base_credit['age'])]
base_credit['age'].fillna(base_credit['age'].mean(), inplace=True)
base_credit.loc[base_credit['clientid'].isin([29,31,32])]
