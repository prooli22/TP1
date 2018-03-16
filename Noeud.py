'''
    Fichier : Noeud
    Projet  : TP1
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

import math

class Noeud:
    def __init__(self, xmin, xmax, ymin, ymax, parents=None):
        self.x_min = xmin
        self.x_max = xmax
        self.y_min = ymin
        self.y_max = ymax
        self.NO = None
        self.NE = None
        self.SE = None
        self.SO = None
        self.parents = parents
        self.x_centre = (xmin + xmax) / 2
        self.y_centre = (ymin + ymax) / 2
        self.frontieres = {"NO" : None, "NE" : None, "SE" : None, "SO" : None}

    def __str__(self):
        return str('<' + ('0 ' if(self.NO is None) else '1 ') +
                         ('0 ' if(self.NE is None) else '1 ') +
                         ('0 ' if(self.SE is None) else '1 ') +
                         ('0'  if(self.SO is None) else '1') + '>')

    def enfants(self):
        return [ self.NO, self.NE, self.SE, self.SO ]

    def creer_frontieres(self):
        # Si la frontière n'est pas divisible par 2, on prend le plafond de la moitié de celle-ci.
        if not isinstance(self.x_centre, int) or not isinstance(self.y_centre, int):
            self.x_centre = math.ceil(self.x_centre)
            self.y_centre = math.ceil(self.y_centre)

        # print('___________________________________________________')
        # print('Creer Frontiere :')
        # print('xmin : ' + str(self.x_min))
        # print('xmax : ' + str(self.x_max))
        # print('ymin : ' + str(self.y_min))
        # print('ymax : ' + str(self.y_max))
        # print('xcentre : ' + str(self.x_centre))
        # print('ycentre : ' + str(self.y_centre))
        # print('___________________________________________________')

        self.frontieres["NO"] = Noeud(self.x_min, self.x_centre, self.y_min, self.y_centre, self)
        self.frontieres["NE"] = Noeud(self.x_centre, self.x_max, self.y_min, self.y_centre, self)
        self.frontieres["SE"] = Noeud(self.x_centre, self.x_max, self.y_centre, self.y_max, self)
        self.frontieres["SO"] = Noeud(self.x_min, self.x_centre, self.y_centre, self.y_max, self)

    def dans_frontieres(self, bateau):
        if((bateau.x <= self.x_max and bateau.x >= self.x_min) and (bateau.y <= self.y_max and bateau.y >= self.y_min)):
            return True
        else:
            return False
