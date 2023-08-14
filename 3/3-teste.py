import json
import pandas as pd

with open("3\dados_compras.json") as f:
    data = json.load(f)

tabela = pd.DataFrame(data)
tabela_agrupada = (
    tabela.groupby("Login")
    .agg({"Idade": "unique", "Sexo": "unique", "Valor": "sum"})
    .reset_index()
)
print(tabela_agrupada)
