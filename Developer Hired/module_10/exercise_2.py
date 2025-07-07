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

print(f'Essas são as pontuações do times ANTES da mudança: {serie_a_pontos}.')

serie_a_pontos["Flamengo"] += 5
serie_a_pontos["Sport"] += 5

print(f'Essas são as pontuações do times APÓS a mudança: {serie_a_pontos}.')
