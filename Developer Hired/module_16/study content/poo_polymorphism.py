class Animal:

    def fazer_barulho(self):
        pass

class Pinto(Animal):

    def fazer_barulho(self):
        print('Piu')

class Galinha(Animal):

    def fazer_barulho(self):
        print('Có')

class Galo(Animal):

    def fazer_barulho(self):
        print('Corococó')

pinto = Pinto()
galinha = Galinha()
galo = Galo()

animais = [pinto,galinha,galo]
for animal in animais:
    animal.fazer_barulho()