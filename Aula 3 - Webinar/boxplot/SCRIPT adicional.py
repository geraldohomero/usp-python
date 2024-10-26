# -*- coding: utf-8 -*-

#%%
##############################################################################
#                     IMPORTAÇÃO DOS PACOTES NECESSÁRIOS                     #
##############################################################################

import pandas as pd #manipulação de dado em formato de dataframe
import numpy as np #biblioteca para operações matemáticas multidimensionais
import matplotlib.pyplot as plt #biblioteca de visualização de dados
import seaborn as sns #biblioteca de visualização de informações estatísticas
import plotly.express as px #biblioteca para gráficos interativos
import plotly.io as pio #biblioteca para gráficos interativos
pio.renderers.default = 'browser' #biblioteca para gráficos interativos

#%%
##############################################################################
#                DESCRIÇÃO E EXPLORAÇÃO DO DATASET 'sacarose'                #
##############################################################################

# Carregamento da base de dados 'sacarose'
df_sacarose = pd.read_csv('sacarose.csv', delimiter=',')

# Visualização da base de dados 'sacarose'
print(df_sacarose)

#%%

# Programando um objeto com o banco de dados agrupado pelo critério
df_sacarose_grupo = df_sacarose.groupby(by=['fornecedor'])

# Gerando estatísticas com o banco de dados agrupado

#%%
print(df_sacarose_grupo.min()) # valor mínimo

#%%
print(df_sacarose_grupo.sum(['sacarose'])) # soma por grupo para dada variável

#%%
print(df_sacarose_grupo.mean(['sacarose'])) # média por grupo para dada variável

#%%
print(df_sacarose_grupo.sacarose.max()) # valor máximo

#%%
# Criando uma sequencia para exemplo
df_sacarose['variavel_exemplo'] = np.arange(1, 33) 

# Obtendo diferentes estatísticas no mesmo código
print(df_sacarose.groupby(['fornecedor']).agg({'sacarose':'mean','variavel_exemplo':'max'}))

#%%

# Contagem de observações
conta = sns.countplot(x="fornecedor", data=df_sacarose)
conta.bar_label(conta.containers[0])
plt.xlabel('Fornecedores',fontsize=12)
plt.ylabel('Contagem',fontsize=12)
plt.show()

#%% 

#Boxplot da variável completa
sns.boxplot(data=df_sacarose, x='sacarose',
            linewidth=2, color='darkorchid')

#%%
# Boxplots da variável 'sacarose' por 'fornecedor' - pacote matplotlib
array = np.array(df_sacarose['sacarose'])
array1 = array[df_sacarose['fornecedor'] == 1]
array2 = array[df_sacarose['fornecedor'] == 2]
array3 = array[df_sacarose['fornecedor'] == 3]

data = {'Fornecedor 1': array1,
        'Fornecedor 2': array2,
        'Fornecedor 3': array3}

fig, bp = plt.subplots()
bp.set_title('Boxplots de sacarose por fornecedor')
bp.boxplot(data.values())
bp.set_xticklabels(data.keys())
plt.show()


#%%
# Boxplots da variável 'sacarose' por 'fornecedor' - pacote seaborn
plt.figure(figsize=(15,10))
sns.boxplot(data=df_sacarose, x='fornecedor', y='sacarose',
            linewidth=2, orient='v', color='darkorchid')
sns.stripplot(data=df_sacarose, x='fornecedor', y='sacarose',
              color="orange", jitter=0.1, size=7)
plt.title('Boxplots de sacarose por fornecedor', fontsize=17)
plt.xlabel('Fornecedor', fontsize=16)
plt.ylabel('Sacarose', fontsize=16)
plt.show()

#%%
# Boxplots da variável 'sacarose' por 'fornecedor' - pacote plotly

fig = px.box(df_sacarose, x='fornecedor', y='sacarose')
fig.show()

##############################################################################