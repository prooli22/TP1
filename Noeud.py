'''
    Fichier : Noeud
    Projet  : TP1
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

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
        self.x_centre = (xmin + xmax) // 2.0
        self.y_centre = (ymin + ymax) // 2.0
        self.frontieres = {"NO" : None, "NE" : None, "SE" : None, "SO" : None}

    def __str__(self):
        return str('<' + ('0 ' if(self.NO is None) else '1 ') +
                         ('0 ' if(self.NE is None) else '1 ') +
                         ('0 ' if(self.SE is None) else '1 ') +
                         ('0'  if(self.SO is None) else '1') + '>')

    def enfants(self):
        return [ self.NO, self.NE, self.SE, self.SO ]

    def diviser(self):
       self.frontieres["NO"] = Noeud(self.x_min, self.x_centre, self.y_min, self.y_centre, self)
       self.frontieres["NE"] = Noeud(self.x_centre, self.x_max, self.y_min, self.y_centre, self)
       self.frontieres["SE"] = Noeud(self.x_centre, self.x_max, self.y_centre, self.y_max, self)
       self.frontieres["SO"] = Noeud(self.x_min, self.x_centre, self.y_centre, self.y_max, self)

    def dans_frontieres(self, bateau):
        if(bateau.x >= self.x_min and bateau.y >= self.y_min and bateau.x <= self.x_max and bateau.y <= self.y_max):
            return True
        else:
            return False

       