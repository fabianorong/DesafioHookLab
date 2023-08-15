import json
import pandas as pd

with open("3\dados_compras.json") as f:
    data = json.load(f)

tabela = pd.DataFrame(data)
tabela_agrupada = (
    tabela.groupby("Login")
    .agg(
        {
            "Idade": "unique",
            "Sexo": "unique",
            "Item ID": "unique",
            "Nome do Item": "unique",
            "Valor": "sum",
        }
    )
    .reset_index()
)
print(tabela_agrupada)

# Identifique a quantidade total de compras realizadas.
print(f"Quantidade total de compras realizadas: {len(tabela_agrupada)}")

# Calcule a média, o valor mínimo e máximo gasto por compra.
soma = tabela_agrupada["Valor"].sum()
media = soma / (len(tabela_agrupada))
print(f"Valor medio gasto por compra: {media}")

max_valor = tabela_agrupada["Valor"].max()
print(f"Valor maximo gasto por compra: {max_valor}")

min_valor = tabela_agrupada["Valor"].min()
print(f"Valor minimo gasto por compra: {min_valor}")
