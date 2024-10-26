#%% Apresentação do Python e Spyder

# Python é a linguagem de programação que vamos utilizar
# Spyder é um software que torna o uso do Python mais simples para o usuário

# Escolhendo esta interface atual: View -> Window Layouts -> Rstudio layout
# A interface do Spyder divide-se em 4 grandes partes, principalmente para:

# 1ª Parte: script com o histórico de códigos daquele projeto ou análise
# 2ª Parte: console onde os códigos podem ser digitados e são implementados
# 3ª Parte: um ambiente onde ficam listados os objetos e são gerados os plots
# 4ª Parte: onde aparecem helps de pacotes e os arquivos da pasta atual

# Sempre que iniciar uma nova análise, sugere-se criar um "project"

# Projects -> New Project -> New Directory -> Nomear -> Location -> Create

# O project cria uma pasta, o que facilita a organização e o compartilhamento
# Ajuda na importação de dados para o Spyder
# Auxilia na centralização dos arquivos específicos do seu projeto

# Normalmente, utiliza-se um script para guardar o histórico das análises

# File -> New File

# Em seguida, é possível editar o cabeçalho e salvá-lo na pasta do project

# Importante: perceba que os textos, neste script, se iniciam com #
# Os códigos são digitados diretamente e são identificados como comandos
# Se digitarmos os textos diretamente, o Python identificará um erro
# Da mesma forma, se um comando estiver incorreto, um erro aparecerá

# O elemento #%% utilizado tem o objetivo de organizar o script
# Cria células dentro do script
# Assim, é possível executar o conteúdo daquela célula com "shift + enter"

# Para retomar um projeto: Projects -> Open Project -> Seleciona a pasta

#%% Vamos conhecer algumas funções básicas no Python
#%% Adição

print(1 + 1)

# Note que foi utilizada a função "print"
# Tem o objetivo de mostrar no console o resultado da fórmula
# Também é possível digitar os comandos diretamente no console

#%% Subtração

print(10 - 2)

#%% Multiplicação

print(25 * 2)

#%% Divisão

print(100 / 10)

#%% Exponenciação

print(3 ** 3)

#%% Pacotes

# O Python possui uma linguagem básica, com alguns métodos prontos para uso
# Entretanto, os desenvolvimentos ocorrem por meio de "pacotes"
# Tais pacotes precisam ser instalados antes do uso
    
# No terminal pode ser escrito: pip install "nome_do_pacote"
# Assim é feito com pacotes que serão utilizados, mas ainda não foram instalados

# Por exemplo:

# pip install pandas
# pip install numpy
# pip install matplotlib

# Também é possível instalar pacotes via leitura de arquivo
# É uma boa prática nomear esse arquivo como requirements.txt
# Cada linha do requirements.txt é um pacote que deve ser instalado
# Os pacotes desse arquivo são instalados utilizando o comando no terminal
# O comando a seguir deve ser digitado no console (sem o #):

# pip install -r requirements.txt

# Todos os pacotes que constam no arquivo .txt serão instalados
# Caso o pacote já tenha sido instalado antes, retornará a mensagem:
# "Requirement already satisfied: " + "nome_do_pacote"

# Agora é possível importar o pacote instalado

#%% Importando um pacote (para obter uma fórmula para raiz quadrada)

# Antes de usar o pacote, é preciso carregá-lo com a função import
# A seguir, vamos carregar o pacote "math"

import math

# Após rodar este comando, as funções do math já podem ser utilizadas
# Caso execute o comando a seguir sem importar o pacote, ocorrerá um erro 

print(math.sqrt(25))

# Pode-se definir um apelido para o pacote no momento de sua importação
# Isso é feito para facilitar a declaração de pacotes com nomes grandes
# É boa prática importar todas as bibliotecas que serão utilizadas no início

import numpy as np
import pandas as pd
import statsmodels as sm

# A exclamação simboliza o pacote que foi importado, mas não foi utilizado

# O ambiente do Python Anaconda já possui vários pacotes já instalados
# Os pacotes dessa lista não precisam ser instalados para serem utilizados
# Por exemplo, é o caso do numpy

# Referência da lista de pacotes em cada sistema operacional: 
# https://docs.anaconda.com/anaconda/packages/pkg-docs/

#%% As funções

# Neste momento, é importante entendermos o objetivo das funções
# As funções indicam a ação que deve executada pelo script Python
# Portanto, as funções são algoritmos que executam uma ação pré-estabelecida

# A função math.sqrt() retorna a raiz quadrada e print() printa o resultado

# A mesma operação pode ser feita com uma função da biblioteca "numpy"

print(np.sqrt(25))

# As funções podem necessitar de mais de um argumento

#%% Objetos

# O Python funciona com base em objetos
# Quando utilizamos o Spyder, os objetos ficam listados no ambiente ao lado

# Vamos conhecer os objetos iniciando pelas séries
# Séries são objetos do pacote "pandas", muito utilizado em análise de dados
# As séries mais simples são numéricas, caracteres ou lógicas

#%% Numérico

# Lembrando: o primeiro passo é importar o pacote "pandas" (acima)
# A seguir, note que é comum atribuir apelidos aos pacotes "pd"
# A partir de agora, sempre que usarmos o pandas será com o nome "pd"

numeros = pd.Series([1,2,3,4,5])

# Acima, criamos uma série chamada "numeros" que contém números
# Para criar o "numeros", utilizamos o indicador = para atribuir os valores
# Na sequencia, indicamos a função "Series" que está no pacote "pd"

print(numeros)

# Em paralelo, também poderia ser criada uma lista (não é pandas)

numeros_lista = ([6,7,8,9,10])

#%% Caracteres

# Vamos criar um vetor com textos, isto é, com caracteres:

pessoas = pd.Series(["João", "Maria", "Pedro", "Paula"])

# Agora, foi criado um vetor de textos que foram colocados entre aspas duplas

print(pessoas)

#%% Argumentos lógicos

# Também poderíamos criar um vetor com argumentos lógicos, True ou False

logico = pd.Series([True, False, True, True, False, False])

print(logico)

#%% Classes de objetos

# Número inteiro ou "int"

print(type(1))

# Sequência de caracteres ou "string"

print(type("João"))

# Booleano (Verdadeiro ou falso) ou "bool"

print(type(True))

# Uma série que criamos por meio do pandas

print(type(pessoas))

#%% Comprimento das séries

# Para saber o comprimento de uma série, é possível utilizar len():

print(len(numeros))
print(len(pessoas))
print(len(logico))

# Pode ser interpretado como o número de observações em cada objeto

#%% Criando uma sequência de números

# Para gerar tal objeto, vamos utilizar outro pacote relevante do Python: numpy

sequencia_1 = np.arange(1, 10)

# Note que esta função "arange" inclui o número inicial, mas exclui o final

sequencia_2 = np.arange(1, 10, 0.5)

# Cada objeto tem seu nome e não há nomes iguais no ambiente
# Se atribuir o mesmo nome a outro objeto, o objeto antigo é substituído

sequencia_1 = np.arange(500, 600)

#%% Variados

# Existem séries que guardam informações de variadas classes:
    
varios = pd.Series([1, 2, 3, "Azul", "Verde", "Vermelho", True, False, True])

print(varios)

# Neste caso, a série fica toda identificada como texto

#%% Comparações

#É possível realizar operações com as séries. A seguir, alguns exemplos:
# Observe os operadores comumente utilizados na linguagem Python

#%% Igualdade

print(numeros == 1)

#%% Multiplicação

print(numeros * 2)

#%% Multiplicação e criação de objeto

triplo_numeros = numeros * 3

# Aqui foi criado um novo objeto contendo o tripo dos números

#%% Divisão e criação de objeto

metade_numeros = numeros / 2

#%% Comparando textos (verificando diferença)

print(pessoas != "João")

#%% Comparando números (maior)

print(sequencia_2 > 5)

#%% Comparando números (maior ou igual)

print(sequencia_2 >= 4.5)

#%% Série com dados categóricos

# Podemos criar uma variável definida como categórica, isto é, qualitativa

altura = pd.Series(["alto", "médio", "alto", "baixo", "médio", "alto"], dtype="category")

print(altura)

#%% Data frames
#%% Criando os bancos de dados

# Data frames são os objetos que guardam informações como nas bases de dados
# Assim, nos data frames estão colunas (variáveis) e linhas (observações)

banco_dados_um = pd.DataFrame({'var_1':["pessoa 1", "pessoa 2", "pessoa 3"],
                               'var_2':[42, 55, 28]})

print(banco_dados_um)

# Note que foi criado um objeto do tipo "DataFrame" no ambiente do Spyder
# Na função pd.DataFrame as variáveis devem ter o mesmo comprimento

#%% Vamos criar 3 variáveis para formar o dataset

variavel_um = np.arange(1,11)
variavel_dois = pd.Series([1,2,3,4,5,6,7,8,None,None])
variavel_tres = pd.Series(["a","b","c","d","e","f","g","h","i","j"])

print(variavel_um)
print(variavel_dois)
print(variavel_tres)

# Note que criamos um array pelo "numpy" e duas séries do "pandas"

# No caso acima foi adicionado um argumento relevante: None
# O None é a indicação do dado "não disponível", isto é, missing value (NA)
# Note que o None não é texto

#%% Vamos criar o banco de dados com nomes diferentes para as variáveis

banco_dados_dois =  pd.DataFrame({'posicao': variavel_um,
                                  'faltam' : variavel_dois,
                                  'letras' : variavel_tres})

                                  
print(banco_dados_dois)       
                     
#%% Importando os dados
#%% Excel

# Até o momento, criamos internamente os objetos utilizados
# Agora, vamos importar um tipo de objeto fundamental, as bases de dados

# Inicialmente, vamos importar um arquivo em Excel
# Fonte: preços históricos de 4 ações durante 48 meses

# Note que o pacote relevante para esta função é o pandas "pd"

preco = pd.read_excel("(2) precos_acao.xlsx")

#%% CSV

# Outro formato bastante comum é o (.csv)
# A seguir, vamos importar dados do Banco Mundial sobre o crescimento do PIB
# Fonte dos dados: https://databank.worldbank.org/

pib_paises = pd.read_csv("(2) pib_paises.csv", sep=",", decimal=".")

# Os argumentos adicionados nesta função foram:
# O separador (,) e a indicação de decimais (.)

#%% Link

# Uma ferramenta interessante é a coleta dos dados diretamente nos links
# Desembolsos do sistema BNDES - Total - em milhões de Reais
# Fonte: Banco Central do Brasil

bndes = pd.read_csv("http://api.bcb.gov.br/dados/serie/bcdata.sgs.7415/dados?formato=csv&dataInicial=01/01/2010&dataFinal=31/12/2020",
                 sep = ";")

# Os argumentos são: a indicação do link e o separador das variáveis (;)

#%% Salvando (exportando) os dados
#%% CSV

# Se alterarmos as bases, podemos exportar os bancos de dados utilizados

banco_dados_um.to_csv("banco_dados_um_salvo.csv", index=False)

# Aqui estamos configurando para exportar sem o index

#%% Excel

banco_dados_dois.to_excel("banco_dados_dois_salvo.xlsx", index=False)

#%% Funções e iterações
#%% Introdução

# Referência: (https://docs.python.org/3/tutorial/controlflow.html#defining-functions) / Referência dos Conceitos Teóricos: (https://r4ds.had.co.nz/functions.html)

# Uma função é uma forma de simplificar um código
# É adequada sempre que for necessário repetir o mesmo código várias vezes
# Então, funções automatizam tarefas que seriam repetitivas
# Permite que sejam criados e nomeados objetos contendo tais funções
# Funções e iterações são ferramentas que podem facilitar a escrita dos algoritmos


# Reduzir a duplicidade de códigos é importante, pois:
# Facilita a visualização (leitura do código)
# Facilita a mudança do código, caso necessário
# Evita erros durante a duplicação do código

# Para criar uma função, existem três etapas básicas:
# 1. Nomear a função
# 2. Indicar os argumentos (inputs) da função ficam dentro de def(x, y)
# 3. Indicar o código, a função, que será implementado fica identificado dentro do corpo da função

# Exemplo: todo dia atualizamos milhares de valores somando 17 e dividindo por 2
# Ao invés de repetir a mesma conta toda vez, poderíamos criar uma função:
   
def atualizar(histórico):
    atual = ((histórico + 17)/2)
    return atual

#%% Testando a função

# O input é o que nomeamos de "histórico", isto é, o valor que vamos atualizar
# O "atual" é o nome que demos ao código que será implementado (a função)
# O "return" é o que queremos que a função retorne, isto é, o valor atualizado

print(atualizar(1))

#%%

print(atualizar(2))

#%%

print(atualizar(3))

#%%

print(atualizar(4))

#%%

# Ainda menos repetitivo, poderíamos criar um vetor com todos os valores
# Em seguida, o vetor entra como input na função para retornar todos os valores

atualizar_hoje = np.arange(1, 16)

print(atualizar(atualizar_hoje))

#%% Função com vários inputs

# Poderíamos ter uma função com mais de um input. Por exemplo

def ajustar(valor1, valor2):
  ajuste = ((valor1 + 180)/(valor2 - 60))
  return ajuste

#%%

print(ajustar(100, 80))

#%%

print(ajustar(200, 80))

#%%

print(ajustar(200, 100))

#%% Condições

# Neste contexto de funções, as condições "if, elif e else" são importantes
# Primeiramente, estabelecemos a condição
# Logo após, no primeiro print(), vamos estabelecer o resultado caso if == TRUE
# Na sequência, estabelecemos o else, ou seja, o restante caso if == FALSE
# Portanto, o segundo print() indica o que retornar se a condição não for atendida

valor = 100000

#%% 

if valor >= 100000:
    print("número grande")
else:
    print("número pequeno")

#%% Múltiplas condições

# Também poderíamos ter múltiplos critérios utilizando o "elif"

valor = 650000

if valor >= 1000000:
  print("número grande")
elif valor >= 500000 and valor < 1000000:
  print("número intermediário")
else:
  print("número pequeno")
  
# Adicionamos uma condição intermediária (e seu respectivo retorno - print()) com o elif

#%% Funções e condições

# É possível integrar condições ("if") às funções apresentadas anteriormente
# Voltando ao exemplo, vamos supor que atualizamos valores só até o limite 100
# Valores que seriam atualizados acima dele, ficam no limite estabelecido = 100

# Adicionamos o if (condição) {o que retornar quando for satisfeita}
# Na sequência, o else {o que retornar quando NÃO for satisfeita}

def atualizar_teto(histórico):
    
    atual = ((histórico + 17)/2)
    
    if atual <= 100:
        return atual
    else:
        return("Atualizado no teto = 100")

#%%

print(atualizar_teto(44))

#%%

print(atualizar_teto(199))

#%%

def ajustar_mult(valor1,valor2):
    
    ajuste = ((valor1 + 180)/(valor2 - 60))
    
    if ajuste <= 100:
        return "baixo"
    elif ajuste > 100 and ajuste <= 1000:
        return "médio"
    else:
        return "alto"

#%%

print(ajustar_mult(500, 300)) # resultado = 2,8333)

#%%

print(ajustar_mult(50000,100)) # resultado = 1.254,50)

#%%

print(ajustar_mult(1000, 70)) # resultado = 118)

#%% Integrando novas funções e códigos existentes

# Nos exemplos acima, criamos nossas funções que utilizamos em cada código 
# Porém, também poderíamos utilizar funções já existentes
# Ou seja, o código pode conter uma grande diversidade de funções já existentes

def médias(x):
  media = np.mean(x)
  return media

#%%

valores = pd.Series([1, 4, 6, 9, 12, 16])

print(médias(valores))

#%% Exemplos de iterações

# A seguir, vamos analisar o funcionamento do "for" e do "while"

# Retomando o trabalho de atualizar valores diariamente, podemos usar o for

for i in atualizar_hoje:
    print((i + 17)/2)
    
# Interpretação: para todo valor i que consta no array "atualizar_hoje"
# Faça o print do resultado (valor i + 17)/2

#%%

# O while() permite que seja adicionada uma condição do tipo "enquanto"

valores = 2

while valores < 100:
    valores = valores + 20
    print(valores)

# Interpretação: enquanto o resultado de valores for menor do que 100, some 20

#%% Conceitos básicos de manipulação de dados
#%% Importando um banco de dados

# A manipulação dos dados consiste em organizar as variáveis e observações
# Na grande maioria dos casos, as bases de dados precisam ser preparadas

# Vamos utilizar como exemplo a base de dados de desempenho dos alunos
# Fonte: Fávero e Belfiore (2017, Capítulo 16)

desempenho_aluno_escola = pd.read_csv("(2) desempenho_aluno_escola.csv", delimiter=",")

#%% Visualizar os dados

# Vamos olhar apenas a parte inicial do banco de dados (10 primeiras linhas)

print(desempenho_aluno_escola.head(10))

#%% Variáveis do dataset

# Quais são os nomes das variáveis disponíveis?

print(desempenho_aluno_escola.columns)

#%% Removendo uma variável sem uso

# Por exemplo, supondo que a variável "texp" não será utilizada

desempenho_aluno_escola.drop(desempenho_aluno_escola.columns[[4]], axis=1, inplace=True)

# O argumento inplace=True indica que deve reescrever o objeto existente

#%% Número de observações

# Ao todo, quantas observações (linhas) existem no banco de dados

print(desempenho_aluno_escola.shape[0])

#%% Número de variáveis

# Ao todo, quantas variáveis (colunas) existem no banco de dados

print(desempenho_aluno_escola.shape[1])

#%% Número de observações e variáveis

print(desempenho_aluno_escola.shape)

#%% Detalhes das variáveis do dataset

# Qual é a estrutura do banco de dados?

print(desempenho_aluno_escola.info())

#%% Selecionando uma variável

# Em algumas funções, pode ser necessário especificar uma variável
# Indicaremos o nome_objeto_dados['variável']

print(desempenho_aluno_escola['desempenho'])

#%% Criando um objeto com a variável

desempenho = desempenho_aluno_escola['desempenho']

#%% Removendo um objeto do ambiente

# Para remover um objeto do ambiente, pode ser feito da seguinte forma:

del desempenho

#%% Identificando valores específicas

# O primeiro argumento é o número da linha e, após a vírgula, a posição da coluna 

# Qual é o valor do desempenho escolar (variável na 3ª coluna) do 1º aluno?

print(desempenho_aluno_escola.iloc[0, 2])

# Importante: tanto o index quanto as colunas começam contagem do zero no pandas

#%% Identificando observações específicas

# Quais são os valores de todas as variáveis do 5º aluno?

print(desempenho_aluno_escola.iloc[4,])

#%% Identificando algumas observações específicas

# Quais são os valores de todas as variáveis para os alunos de 7 a 12?

print(desempenho_aluno_escola.iloc[6:12, ])

# É necessário adicionar uma posição a mais no final

#%% Identificando variáveis específicas: posição

# Quais são as observações para a variável da 5ª coluna (tipo de escola?)?

print(desempenho_aluno_escola.iloc[:,4])

#%% Identificando variáveis específicas: nome da variável

# No caso acima, também poderia ser indicada pelo nome da variável

print(desempenho_aluno_escola.loc[:,'priv'])

#%% Reorganizando a posição das variáveis

reorganiza = desempenho_aluno_escola.reindex(['desempenho','estudante','horas','priv','escola'], axis=1)

#%% Selecionando algumas variáveis pelo nome

# Vamos armazenar somente as variáveis estudante (id), desempenho e horas

parte_dados_1 = desempenho_aluno_escola[["estudante", "desempenho", "horas"]]

#%% Excluindo algumas variáveis

# As variáveis "horas" e "priv" poderiam ser excluídas

novos_dados_1 = desempenho_aluno_escola.drop(columns=['horas', 'priv'])

#%% Excluindo algumas observações

# Supondo que não vamos analisar os estudantes números 476 até 522

# A contagem de linhas na biblioteca pandas sempre começa em 0, portanto:
# Estudante 476 está na linha 475
# Estudante 522 está na linha 521

novos_dados_2 = desempenho_aluno_escola.drop(desempenho_aluno_escola.index[475:522])

# Lembrando de adicionar uma posição a mais no final

#%% Gerando estatísticas descritivas

# Tabela de estatísticas descritivas para variáveis quantitativas

descritivas = desempenho_aluno_escola[['desempenho', 'horas']]

descritivas.describe()

# Tabela de frequências para variável qualitativa

desempenho_aluno_escola['priv'].value_counts()

#%% Filtrando observações por meio de operadores

# Também é possível filtrar observações por meio dos operadores:
# Alguns operadores úteis para realizar filtros:

# "== igual"
# "> maior"
# ">= maior ou igual"
# "< menor"
# "<= menor ou igual"
# "!= diferente"
# "& indica e"
# "| indica ou"

print(desempenho_aluno_escola[desempenho_aluno_escola['desempenho'] > 50])

# Poderia salvar como um objeto:

novos_dados_3 = desempenho_aluno_escola.loc[desempenho_aluno_escola['desempenho'] > 50]

#%%

print(desempenho_aluno_escola[desempenho_aluno_escola['priv'] == 'pública'])

#%%

print(desempenho_aluno_escola[(desempenho_aluno_escola['priv'] == 'pública') & (desempenho_aluno_escola['desempenho'] <= 20)])

#%%

print(desempenho_aluno_escola[desempenho_aluno_escola['escola'] != 'A'])

#%%

print(desempenho_aluno_escola[(desempenho_aluno_escola['escola'] == 'C') | (desempenho_aluno_escola['escola'] == 'H')])

# Poderia salvar como um objeto:

novos_dados_4 = (desempenho_aluno_escola[(desempenho_aluno_escola['escola'] == 'C') | (desempenho_aluno_escola['escola'] == 'H')])

#%% Agrupamento dos dados por algum critério

parte_dados_2 = desempenho_aluno_escola[["escola", "desempenho", "horas"]]

# Agrupando os dados e resumindo utilizando o método groupby

agrupamento_escola = parte_dados_2.groupby(by=['escola']).mean()

print(agrupamento_escola)

# O agrupamento_escola está agrupado e não pode mais ser manipulado como antes
# O index agora são as escolas - que foram o critério de agrupamento

print(agrupamento_escola['escola']) # gera um erro!

# Para manipular novamente a coluna escola, utiliza-se o método reset_index()

agrupamento_escola = agrupamento_escola.reset_index()

print(agrupamento_escola['escola'])

#%% Organizando o dataset com base em critérios

# É possível ordenar os valores baseados em uma ou várias colunas

print(desempenho_aluno_escola.sort_values(by=['desempenho'], ascending=False))

# Utilizando várias colunas na ordenação:

print(desempenho_aluno_escola.sort_values(by=['desempenho', 'horas'], ascending=False))

#%% Aplicação prática

# Como exemplo, vamos trabalhar no banco de dados do PIB dos países

# Podemos importar novamente o banco de dados

pib_paises = pd.read_csv("(2) pib_paises.csv", sep=",", decimal=".")

#%% Inicialmente, vamos excluir as últimas linhas 

# Serão as linhas do index 217 até 270

pib_paises.drop(pib_paises.index[217:271], inplace=True)

print(pib_paises)

#%% Excluir variáveis que não utilizaremos

pib_paises.drop(pib_paises.columns[[1,3]], axis=1, inplace=True)

print(pib_paises)

#%% Alterar os nomes das variáveis

nomes = ["ano", "paises", "var_pib_capita", "var_pib_total"]
pib_paises.columns = nomes

print(pib_paises)

#%% Formato das variáveis

print(pib_paises.info())

# Note que as variáveis que deveriam ser numéricas vieram como textos
# Vamos criar novas variáveis contendo os valores

#%% Ajustando variáveis

# Neste caso, utilizaremos a função "to_numeric"
# Um detalhe: note que os missings ".." serão substituídos por NaN

pib_paises['var_pib_capita_ajust'] = pd.to_numeric(pib_paises['var_pib_capita'], errors='coerce')
pib_paises['var_pib_total_ajust'] = pd.to_numeric(pib_paises['var_pib_total'], errors='coerce')

print(pib_paises)

#%% Excluindo linhas com dados faltantes

pib_paises = pib_paises.dropna()

print(pib_paises)

#%% Data Visualization
#%% Pacotes

# Para a visualização de dados, vamos utilizar principalmente os pacotes "matplotlib" e "seaborn"

import matplotlib.pyplot as plt
import seaborn as sns

# Caso esteja iniciando o Spyder novamente, é necessário carregar o pandas

import pandas as pd 

#%% Gráfico de Barras

# Vamos começar analisando uma variável qualitativa, o perfil do investidor

perfil_investidor = pd.read_excel("(2) perfil_investidor.xlsx")

# Como é uma variável categórica, vamos criar um gráfico de contagem (countplot)
# Neste caso, o gráfico apresentará a contagem em cada categoria da variável

sns.countplot(x="perfil", data=perfil_investidor)

#%%

# Poderíamos mudar a ordem de apresentação reorganizando os níveis da variável

sns.countplot(x="perfil", data=perfil_investidor, order=["Agressivo","Moderado","Conservador"])

#%%

sns.countplot(x="perfil", data=perfil_investidor, order=["Agressivo","Moderado","Conservador"], color="gray")

plt.title("Perfil dos Investidores")
plt.suptitle("Banco X")
plt.xlabel('Perfil do Investidor',fontsize=12)
plt.ylabel('Quantidade',fontsize=12)
plt.show()

#%%

sns.countplot(x="perfil", data=perfil_investidor, order=["Agressivo","Moderado","Conservador"], color="blue")

plt.title("Perfil dos Investidores")
plt.suptitle("Banco X")
plt.xlabel('Perfil do Investidor',fontsize=12)
plt.ylabel('Quantidade',fontsize=12)
plt.show()

#%%

# Conhecendo as paletas de cores do seaborn

# Conhecendo a paleta bright

palette = sns.color_palette("bright")

sns.palplot(palette)

#%%

# Conhecendo a paleta viridis

palette = sns.color_palette("viridis")

sns.palplot(palette)

#%%

# Vamos alterar o fundo do gráfico (theme)

sns.set_theme(style="whitegrid", palette="viridis")

ax = sns.countplot(x="perfil", data=perfil_investidor, order=["Agressivo","Moderado","Conservador"])
ax.bar_label(ax.containers[0])

plt.title("Perfil dos Investidores")
plt.suptitle("Banco X")
plt.xlabel('Perfil do Investidor',fontsize=12)
plt.ylabel('Quantidade',fontsize=12)
plt.show()

#%%

import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

#%%

# Também poderíamos apresentar o gráfico com os eixos invertidos

ax = sns.countplot(y="perfil", data=perfil_investidor, order=["Agressivo","Moderado","Conservador"], color="blue")

# Vamos adicionar um texto contendo os valores que foram contados
ax.bar_label(ax.containers[0])

plt.title("Perfil dos Investidores")
plt.suptitle("Banco X")
plt.xlabel('Perfil do Investidor',fontsize=12)
plt.ylabel('Quantidade',fontsize=12)
plt.show()

#%%

# A seguir, podemos apresentar um gráfico de barras ordenado

# Pode ser necessário importar o dataset "desempenho_aluno_escola"
# Se não estiver nos objetos já importados

agrupamento_desempenho = desempenho_aluno_escola[['escola','desempenho','priv']].groupby(by=['escola','priv']).mean()

agrupamento_desempenho_ordenado = agrupamento_desempenho.sort_values(by=['desempenho'], ascending=False).reset_index()

sns.barplot(x="escola", y="desempenho", data=agrupamento_desempenho_ordenado.head(10))

plt.title("Ranking dos desempenho da escola")
plt.xlabel('Escola',fontsize=12)
plt.ylabel('Desempenho',fontsize=12)
plt.show()

#%% Histograma

# A seguir, vamos elaborar o histograma de notas dos alunos (desempenho escolar)
# O banco de dados é o mesmo que já utilizamos anteriormente

# Iniciando com o gráfico básico utilizando o próprio pandas dataframe com o método "hist"

desempenho_aluno_escola['desempenho'].hist(bins=30)

#%%

# Podemos também utilizar a biblioteca do seaborn para fazer o histograma

sns.histplot(data=desempenho_aluno_escola, x="desempenho")

#%%

# Vamos adicionar algumas formatações

sns.histplot(data=desempenho_aluno_escola, x="desempenho")
plt.xlabel('Desempenho escolar',fontsize=12)
plt.ylabel('Frequência',fontsize=12)
plt.show()

#%%

# Algumas vezes pode ser importante formatar a quantidade de barras apresentadas

sns.histplot(data=desempenho_aluno_escola, x="desempenho", bins=50)
plt.xlabel('Desempenho escolar',fontsize=12)
plt.ylabel('Frequência',fontsize=12)
plt.show()

#%% Gráfico de Pontos

# Na sequência, vamos elaborar um gráfico de dispersão dos pontos
# Os dados são do atlas ambiental sobre distritos da cidade de São Paulo

atlas_ambiental = pd.read_excel("(2) atlas_ambiental.xlsx")

#%%

# Iniciando com o gráfico básico (scatterplot)
# Neste caso, devemos especificar as variáveis dos eixos x e y no

sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade")

#%%

# Como há variáveis nos dois eixos, podemos adicionar outras variáveis:

# Na forma de tamanho dos pontos ("size")

sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade")
plt.title("Indicadores dos Distritos do Município de São Paulo")
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Escolaridade',fontsize=12)
plt.show()

#%%

# Para separar no gráfico alguma condição, é necessário fazer uma distinção dos dados no dataframe

atlas_ambiental.loc[atlas_ambiental['favel']<6, "color"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['favel']>=6, "color"] = "Acima"

#%%

# Na cor por categoria dos pontos ("hue")

sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="color")
plt.title("Indicadores dos Distritos do Município de São Paulo")
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Escolaridade',fontsize=12)
plt.show()

#%%

# Para separar no gráfico alguma condição, é necessário fazer uma distinção dos dados no dataframe

atlas_ambiental.loc[atlas_ambiental['mortalidade'] < 18, "style"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['mortalidade'] >= 18, "style"] = "Acima"

#%%

# Na forma por categoria dos pontos ("style")

sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="color", style="style")
plt.title("Indicadores dos Distritos do Município de São Paulo")
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Escolaridade',fontsize=12)
plt.show()

#%% Gráfico de linhas

# Vamos elaborar um gráfico de linhas (lineplot) para dados ao longo do tempo
# Neste caso, vamos utilizar o banco de dados com preços de ações

preco_acao = pd.read_excel("(2) precos_acao.xlsx")

#%%

# Como temos 4 ações no banco de dados, vamos implementar o seguinte gráfico
# Note que vamos separar cada empresa por meio da cor do gráfico

sns.lineplot(data=preco_acao, x="data", y="preco", hue="acao")

#%%

# Vamos formatar um pouco mais o gráfico

sns.lineplot(data=preco_acao, x="data", y="preco", hue="acao", marker="o")

plt.title("Série Histórica das Ações")
plt.xlabel('Mês de Referência',fontsize=12)
plt.ylabel('Cotação de Fechamento',fontsize=12)
plt.legend(title='Empresa')
plt.show()

#%%

# A seguir, um gráfico interativo
# Vamos instalar o pacote plotly
# Digitar diretamente no console: pip install plotly

import plotly.express as px

import plotly.io as pio

pio.renderers.default = 'browser'

fig = px.line(preco_acao, 
              x='data', 
              y='preco', 
              color='acao', 
              markers=True, 
              title="Série Histórica das Ações",
              labels={
                     "data": "Mês de referência",
                     "preco": "Cotação de fechamento",
                     "acao": "Empresa"
                 })
fig.show()

#%% Gráfico de Calor

# Vamos gerar um gráfico de calor que distingue informações por meio de cores
# O banco de dados contém informações sobre o tempo para chegar à escola
# Fonte: Fávero & Belfiore (2017, Capítulo 12)

tempo_dist = pd.read_excel("(2) tempo_dist.xls")

#%%

# Inicialmente, vamos selecionar as variáveis quantitativas do banco de dados

tempo_dist = tempo_dist[['tempo','distancia','semaforos']]

# Vamos trabalhar o gráfico de calor no contexto das correlações entre variáveis
# Portanto, primeiramente, vamos criar a matriz de correlações (função "cor")
# Lembrando: selecionar apenas as variáveis quantitativas da base de dados

corr = tempo_dist.corr()

#%%

# Agora vamos elaborar um gráfico de calor (heatmap) com algumas formatações

sns.heatmap(corr, center=0)

#%%

# Poderíamos trocar as cores para facilitar a visualização
# Ao mesmo tempo, vamos adicionar rótulos aos dados

sns.heatmap(corr, center=0, annot=True, cmap="Greens")

# Algumas opções de cores:
    # cmap="YlGnBu"
    # cmap="Blues"
    # cmap="BuPu"
    # cmap="PiYG"
    # cmap="Greens"

#%%

# Vamos torná-lo mais informativo com o plotly

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Heatmap(
        x = corr.columns,
        y = corr.index,
        z = np.array(corr),
        text=corr.values,
        texttemplate='%{text:.2f}'
    )
)

fig.show()

#%% Gráficos Boxplot

# O boxplot apresenta medidas de posição das variáveis
# Mínimo, máximo, 1º quartil, mediana e 3º quartil
# Vemos a distribuição dos dados nas variáveis e eventuais outliers univariados

# Inicialmente, vamos apresentar o boxplot de uma única variável

var_boxplot = atlas_ambiental[['cód_ibge','renda']]

sns.boxplot(data=var_boxplot, y='renda')
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Valores',fontsize=12)
plt.show()

#%%

# Vamos torná-lo mais informativo

fig = px.box(var_boxplot, y="renda")
fig.show()

#%%

# Poderíamos fazer vários boxplot em um mesmo gráfico
# Vamos retomar o exemplo do desempenho dos alunos. Importando novamente:

desempenho_aluno_escola = pd.read_csv("(2) desempenho_aluno_escola.csv", delimiter=",")

# Faremos o boxplot das variáveis "desempenho", "horas" e "tempo de experiência"

# Primeiramente, o Z-Score de cada variável é obtido por meio da função "scale"
# Na sequência, juntaremos as variáveis padronizadas com o id original

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

desempenho_aluno_escola[['desempenho_z','horas_z','texp_z']] = scaler.fit_transform(desempenho_aluno_escola[['desempenho','horas','texp']])

#%%

# Vamos verificar o resultado do Z-Score na média e desvio padrão das variáveis

print(np.mean(desempenho_aluno_escola['desempenho_z']))
print(np.std(desempenho_aluno_escola['desempenho_z']))

#%%

print(np.mean(desempenho_aluno_escola['horas_z']))
print(np.std(desempenho_aluno_escola['horas_z']))

#%%

print(np.mean(desempenho_aluno_escola['texp_z']))
print(np.std(desempenho_aluno_escola['texp_z']))

#%%

# Agora vamos reorganizar o banco de dados da seguinte forma
# O procedimento colocará uma variável na sequência da outra

desemp_reorg_z = pd.melt(desempenho_aluno_escola, id_vars=['estudante'], value_vars=['desempenho_z','horas_z','texp_z'])

#%%

# Por fim, vamos gerar o boxplot

sns.boxplot(data=desemp_reorg_z, y='value', x='variable')
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Valores Z-Score',fontsize=12)
plt.show()

#%%

# Vamos torná-lo mais informativo

fig = px.box(desemp_reorg_z, y='value', x='variable')
fig.show()

#%% FIM!