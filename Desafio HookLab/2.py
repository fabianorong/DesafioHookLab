filmes = [
    {"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
    {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
    {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6},
]

# media das avaliaçoes

avaliacoes = [filme["avaliacao"] for filme in filmes]
soma = sum(avaliacoes)
media = soma / 3
print("A média das avaliaçoes dos filmes é:", (media))

# titulo do filme com maior avaliação
# ano de lançaento do filme com menor avaliação
