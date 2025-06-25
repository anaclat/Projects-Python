prompt_genero = """Qual é o seu gênero?
[M] Masculino
[F] Feminino
"""

print(prompt_genero)
genero = input("Sua opção: ").strip().upper() 

while genero not in ('M', 'F'):
    print("\nValor incorreto. Por favor, digite 'M' para Masculino ou 'F' para Feminino.")
    print(prompt_genero)
    genero = input("Sua opção: ").strip().upper()

if genero == 'M':
    genero_exibicao = 'Masculino'
else:
    genero_exibicao = 'Feminino'

print(f"\nO gênero selecionado foi: {genero_exibicao}.")