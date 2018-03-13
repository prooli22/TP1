'''
    Fichier : Bateaux
    Projet  : TP1
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

class Bateau :

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str('[' + str(self.x) + ' ' + str(self.y) + ']')
