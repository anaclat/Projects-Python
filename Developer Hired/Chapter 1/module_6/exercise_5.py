from math import sin,cos, tan,radians

angulo = float(input("Digite um ângulo: "))
radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'O ângulo de {angulo} tem o seno de {seno}.')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno}.')
print(f'O ângulo de {angulo} tem a tangente de {tangente}.')
