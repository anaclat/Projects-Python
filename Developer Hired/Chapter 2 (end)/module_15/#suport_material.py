# =======================
# STRINGS
# =======================

# Variável do tipo string
nome = 'Ana Clara'

# Converte todos os caracteres da string para maiúsculo
print(nome.upper())

# Converte todos os caracteres da string para minúsculo
print(nome.lower())

# Remove espaços em branco do início e do fim da string
print(nome.strip())

# Conta quantas vezes o caractere 'a' aparece na string (case-sensitive)
print(nome.count('a'))

# Divide a string em uma lista, usando o espaço como separador
print(nome.split(' '))

# Retorna o índice da primeira ocorrência do caractere 'n'
print(nome.find('n'))

# Retorna o índice da última ocorrência do caractere 'n'
print(nome.rfind('n'))

# Verifica se a string é composta apenas por números
print(nome.isnumeric())

# Substitui o caractere 'C' por 'B' (case-sensitive)
print(nome.replace('C','B'))

# Imprime a string original
print(nome)


# =======================
# TUPLAS
# =======================

# Tupla: coleção imutável de elementos
letras = ('a','c','g','c')

# Conta quantas vezes o elemento 'c' aparece na tupla
print(letras.count('c'))

# Retorna o índice da primeira ocorrência do elemento 'a'
print(letras.index('a'))


# =======================
# LISTAS
# =======================

print()  # apenas separa visualmente a saída

# Lista: coleção mutável de elementos
letras_lista = ['f','i','h','j']

# Adiciona o elemento 'a' ao final da lista
letras_lista.append('a')

# Ordena os elementos da lista em ordem alfabética
letras_lista.sort()

# Insere o elemento 'b' na posição de índice 2
letras_lista.insert(2,'b')

# Remove o elemento no índice 3
letras_lista.pop(3)

# Remove a primeira ocorrência do elemento 'j'
letras_lista.remove('j')

# Imprime a lista resultante
print(letras_lista)


# =======================
# DICIONÁRIOS
# =======================

# Dicionário: estrutura que mapeia chave -> valor
letra_numero = {'a': 1, 'b': 2}

# Retorna todos os valores do dicionário
print(letra_numero.values())

# Itera sobre os valores do dicionário e os imprime
for value in letra_numero.values():
    print(value)

# Retorna todas as chaves do dicionário
print(letra_numero.keys())

# Itera sobre as chaves do dicionário e as imprime
for key in letra_numero.keys():
    print(key)

# Retorna todos os pares (chave, valor) do dicionário
print(letra_numero.items())

# Itera sobre os pares (chave, valor) do dicionário e imprime ambos
for key, value in letra_numero.items():
    print(key, value)
    # Acessa diretamente o valor associado à chave 'a'
    print(letra_numero['a'])

# Imprime o dicionário completo
print(letra_numero)