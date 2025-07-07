serie_a_pontos = {
    "Flamengo": 24,
    "Cruzeiro": 24,
    "Red Bull Bragantino": 23,
    "Palmeiras": 22,
    "Bahia": 21,
    "Fluminense": 20,
    "Atlético‑MG": 20,
    "Botafogo": 18,
    "Mirassol": 17,
    "Corinthians": 16,
    "Grêmio": 16,
    "Ceará": 15,
    "Vasco da Gama": 13,
    "São Paulo": 12,
    "Santos": 11,
    "Vitória": 11,
    "Internacional": 11,
    "Fortaleza": 10,
    "Juventude": 8,
    "Sport": 3,
}

print(f'Essas são as pontuações do times ANTES de remover os quatro últimos: {serie_a_pontos}.')

del serie_a_pontos["Internacional"]
del serie_a_pontos["Fortaleza"]
del serie_a_pontos["Juventude"]
del serie_a_pontos["Sport"]


print(f'Essas são as pontuações do times DEPOIS de remover os quatro últimos: {serie_a_pontos}.')