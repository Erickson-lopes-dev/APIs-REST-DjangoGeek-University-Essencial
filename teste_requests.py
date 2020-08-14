import requests

# get Avaliações

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# exibindo dados da resposta
print(avaliacoes.json())

print(avaliacoes.status_code)

# Acessando a quantidade de registros
print(avaliacoes.json()['count'])

# acessando a próxima página
p_pagina = avaliacoes.json()['next']

n_avaliacoes = requests.get(p_pagina)

print(n_avaliacoes.json())

# pegando primerio elemento
print(n_avaliacoes.json()['results'][0])