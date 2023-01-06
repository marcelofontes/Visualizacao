from random import randint

class Die():
    #classe que representa um ciclo de dado

    def __init__(self, num_sides=6):
    #supoe que seja um dado de 6 lados
        self.num_sides = num_sides


    def roll(self):
        #devolve um valor aleatorio entre 1 o numero de lados
        return randint(1, self.num_sides)