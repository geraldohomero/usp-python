# In[1]:

#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ANÁLISE DE DADOS COM PYTHON USP/ESALQ
# WEBINAR I
# Prof. Helder Prado Santos
# Prof. Wilson Tarantin Junior
# Prof. Luiz Paulo Fávero


# In[3]:


# importação dos pacotes necessários

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


# instalação de pacotes específicos

!pip install fiona==1.9.6
!pip install geopandas==0.14.0

# importação dos pacotes necessários

import geopandas as gpd


# In[5]:


# carregamento dos datasets que serão utilizados na análise

tb_pedidos = pd.read_csv("tb_pedidos.csv")
tb_produtos = pd.read_csv("tb_produtos.csv")
tb_clientes = pd.read_csv("tb_clientes.csv")


# In[6]:


# verificando as primeiras linhas do dataset de produtos

tb_produtos.head()


# In[7]:


# verificando as primeiras linhas do dataset de clientes

tb_clientes.head()


# In[8]:


# verificando as primeiras linhas do dataset de pedidos

tb_pedidos.head()


# In[9]:


# possibilidades de merge: left, right, inner e outer

# realizando o merge com a tabela de clientes
dataset = tb_pedidos.merge(tb_clientes, on='cliente_id', how='left')


# In[10]:


# realizando o merge com a tabela de produtos
dataset = dataset.merge(tb_produtos, on='produto_id', how='left')


# In[11]:


# dataset depois do merge com todas as tabelas auxiliares, também chamamos essa relação entre tabela fato e tabela dimensão

dataset.head()


# In[12]:


# verificando tipos das variáveis e se temos valores nulos
dataset.info()


# In[13]:


# percebam que as variáveis de data estão como tipo 'object', será necessário mudar para o tipo date

dataset['data_venda'] = pd.to_datetime(dataset['data_venda'])
dataset['data_entrega'] = pd.to_datetime(dataset['data_entrega'])


# In[14]:


# agora as variáveis de tempo estão com o tipo de dado esperado

dataset.info()


# In[15]:


# verificar uma amostra aleatória do dataset

dataset.sample(n=5)


# In[16]:


# verificar uma amostra aleatória do dataset que sempre vai ser igual por conta da fixagem do estado aleatório

dataset.sample(n=5, random_state=3)


# In[17]:


# verificando a soma do valor das vendas por categoria

dataset_agrupado_vendas_por_categoria = dataset.groupby('categoria').agg({'valor_vendas':'sum'})

dataset_agrupado_vendas_por_categoria


# In[18]:


# ajustando as opções para verificar os números sem notação científica

pd.options.display.float_format = '{:.2f}'.format


# In[19]:


dataset_agrupado_vendas_por_categoria


# In[20]:


# adicionando a variável lucro no dataset com os valores das vendas, desconto e custos dos itens dos pedidos

dataset['lucro'] = dataset['valor_vendas'] * (1 - dataset['desconto']) - dataset['custo_produto'] - dataset['custo_entrega']


# In[21]:


# verificando a variável no dataset

dataset.head()


# In[22]:


# verificando o dataset transposto, caso fique com muitas colunas

dataset.head().T


# In[23]:


# adicionando a variável ano e mês no dataset

dataset['ano'] = dataset['data_venda'].dt.year
dataset['mes'] = dataset['data_venda'].dt.month

dataset.head()


# In[24]:


# verificando as vendas agrupadas por ano e mês

dataset_agrupado_ano_mes = dataset.groupby(by=['ano','mes']).agg({'valor_vendas':'sum'}).reset_index()

dataset_agrupado_ano_mes.head()


# In[25]:


# verificando graficamente a evolução das vendas ao longo mês e dos anos

plt.figure(figsize=(12,8), dpi=600)
sns.lineplot(data=dataset_agrupado_ano_mes, x="mes", y="valor_vendas",
             hue="ano", palette='viridis')
plt.xlabel("Mês", fontsize=17)
plt.ylabel("Total vendido", fontsize=17)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=20)
plt.show()


# In[26]:


# verificando os valores únicos da variável categoria

valores_unicos_categorias = dataset.categoria.unique()

print(valores_unicos_categorias)


# In[27]:


# filtrando o dataset em uma única categoria

dataset[dataset['categoria'] == 'Furniture'].head()


# In[28]:


# carregando o dataset auxiliar com as coordenadas dos países

dataset_auxiliar_coordenadas = pd.read_csv("tb_coordenadas.csv")

dataset_auxiliar_coordenadas.head()


# In[29]:


# verificando o tipo de cada variável e se tem valores nulos para serem tratados

dataset_auxiliar_coordenadas.info()


# In[30]:


# ajustando alguns nomes de colunas para que fique de fácil entendimento

dataset_auxiliar_coordenadas = dataset_auxiliar_coordenadas.rename(columns={
    'Latitude (average)':'latitude_media',
    'Longitude (average)':'longitude_media'
})

# verificando as primeiras linhas

dataset_auxiliar_coordenadas.head()


# In[31]:


# carregando o dataset com os polígonos geométricos dos países utilizando a biblioteca GeoPandas
paises_geopandas = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# verificando as primeiras linhas desse dataset
paises_geopandas.head()


# In[32]:


# fazendo o merge do dataset de coordenadas com o dataset principal no pais e do tipo left

dataset = dataset.rename(columns={'pais':'Country'}).merge(
    dataset_auxiliar_coordenadas,
    on='Country',
    how='left'
)


# In[33]:


# verificando o resultado nas primeiras linhas
dataset.head()


# In[34]:


# verificando o valor de vendas total dos países agrupando latitude e longitude 
vendas_paises_por_coordenadas = dataset.groupby(['latitude_media','longitude_media']).agg({'valor_vendas':'sum'}).reset_index()

# verificando as primeiras linhas
vendas_paises_por_coordenadas.head()


# In[35]:


# plotando o gráfico das coordenadas e o ponto alterado pelo valor total de vendas

plt.figure(figsize=(10,7), dpi=600)
sns.scatterplot(data=vendas_paises_por_coordenadas,
                x="longitude_media", y="latitude_media",
                size="valor_vendas", sizes=(30, 300))
plt.xlabel('Longitude', fontsize=14)
plt.ylabel('Latitude', fontsize=14)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.legend(fontsize=11)
plt.show


# In[36]:


# dando vida ao gráfico utilizando o mapa do mundo como plano de fundo

fig, ax = plt.subplots(figsize=(12,10), dpi=600)
paises_geopandas.plot(color="lightgrey", ax=ax)
sns.scatterplot(data=vendas_paises_por_coordenadas,
                x="longitude_media", y="latitude_media",
                size="valor_vendas", sizes=(1, 200), color='#9b59b6')
plt.title('Total vendido por país', fontsize=17)
plt.xlabel("Longitude", fontsize=17)
plt.ylabel("Latitude", fontsize=17)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.show()


# In[37]:


# verificando o lucro resultante das vendas dos países agrupando latitude e longitude e resumindo pela soma do lucro
lucro_paises_por_coordenadas = dataset.groupby(['latitude_media','longitude_media']).agg({'lucro':'sum'}).reset_index()

# verificando as primeiras linhas
lucro_paises_por_coordenadas.head()


# In[38]:


# dando vida ao gráfico utilizando o mapa do mundo como plano de fundo

fig, ax = plt.subplots(figsize=(12,10), dpi=600)
paises_geopandas.plot(color="lightgrey", ax=ax)
sns.scatterplot(data=lucro_paises_por_coordenadas,
                x="longitude_media", y="latitude_media",
                hue='lucro', size='lucro', sizes=(1, 200), palette='viridis')
plt.title('Lucro total por país', fontsize=20)
plt.xlabel("Longitude", fontsize=17)
plt.ylabel("Latitude", fontsize=17)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)


################################## FIM ######################################
