serie_a = [
    "Flamengo",
    "Cruzeiro",
    "Red Bull Bragantino",
    "Palmeiras",
    "Bahia",
    "Fluminense",
    "Atlético-MG",
    "Botafogo",
    "Mirassol",
    "Corinthians",
    "Grêmio",
    "Ceará",
    "Vasco da Gama",
    "São Paulo",
    "Santos",
    "Vitória",
    "Internacional",
    "Fortaleza",
    "Juventude",
    "Sport"
]

print(f'Esses são os times ANTES da mudança: {serie_a}.')

quatro_primeiros = serie_a[:4]
quatro_ultimos = serie_a[-4:]

serie_a[:4]  = quatro_ultimos
serie_a[-4:] = quatro_primeiros

print(f'Esses são os times DEPOIS da mudança: {serie_a}.')