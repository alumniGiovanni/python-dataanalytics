import pandas as pd


tabela = pd.read_csv("telecom_users.csv")
print(tabela)

# - Tratamento de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# deletando as colunas vazias
# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.dropna(how="all", axis=1)
# deletando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)
#dados
print(tabela.info())
#cancelamentos
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
