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

# Determine o produto mais caro e o produto mais barato.

df = tabela.explode("Valor").explode("Item ID").explode("Nome do Item")
max_valor = df["Valor"].max()
min_valor = df["Valor"].min()

produto_mais_caro = df.loc[
    df["Valor"] == max_valor, ["Valor", "Item ID", "Nome do Item"]
]

produto_mais_barato = df.loc[
    df["Valor"] == min_valor, ["Valor", "Item ID", "Nome do Item"]
]

df2 = produto_mais_caro.drop_duplicates("Item ID", keep="first")
df3 = produto_mais_barato.drop_duplicates("Item ID", keep="first")

print("Produto mais caro:")
print(df2)
print("Produto mais barato:")
print(df3)
