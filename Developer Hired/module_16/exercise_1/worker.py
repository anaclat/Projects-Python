from datetime import datetime

class Trabalhador:

    def __init__(self, nome, ano_nascimento, clt, ano_contratacao=None, salario=None):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.clt = clt
        self.ano_contratacao = ano_contratacao
        self.salario = salario
        self.idade = self._calcular_idade()
        self.aposentadoria = self._calcular_aposentadoria()

    def _calcular_idade(self):
        #Calcula a idade atual do trabalhador.
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento

    def _calcular_aposentadoria(self):
        
        if self.clt != 0 and self.ano_contratacao is not None:
            tempo_contribuicao = datetime.now().year - self.ano_contratacao
            # Aposentadoria aos 45 anos de contribuição, ajustada pela idade atual.
            # Se a pessoa já contribuiu mais de 45 anos, a aposentadoria seria a idade atual.
            # Caso contrário, calcula-se quanto tempo falta para os 45 anos de contribuição
            # e adiciona-se isso à idade atual.
            anos_restantes_contribuicao = max(0, 45 - tempo_contribuicao)
            return self.idade + anos_restantes_contribuicao
        return None # Retorna None se não houver CLT ou ano de contratação para aposentadoria