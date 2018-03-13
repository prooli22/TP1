'''
    Fichier : Noeud
    Projet  : TP1
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

class Noeud:
    def __init__(self, xmin, xmax, ymin, ymax, parents=None):
        self.NO = None
        self.NE = None
        self.SE = None
        self.SO = None
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.parents = parents
        self.x_centre = (self.xmin + self.xmax) / 2
        self.y_centre = (self.ymin + self.ymax) / 2

    def __str__(self):
        return str('<' + ('0 ' if(self.NO is None) else '1 ') +
                         ('0 ' if(self.NE is None) else '1 ') +
                         ('0 ' if(self.SE is None) else '1 ') +
                         ('0'  if(self.SO is None) else '1') + '>')


    def children (self):
        return [ self.NO, self.NE, self.SE, self.SO ]

    # def diviser(self):
    #    xmin, ymin = self.xmin, self.ymin
    #    xmax, ymax = self.xmax, self.ymax
    #    x_centre = (xmin + xmax) / 2.0
    #    y_centre = (ymin + ymax) / 2.0
    #    depth = self.max_depth - 1
    #    #Les 4 gros premiers quadrants séparés au milieu de la grille
    #    self.quadrants = [
    #        Noeud(xmin, ymin, x_centre, y_centre, depth, self),
    #        Noeud(x_centre, ymin, xmax, y_centre, depth, self),
    #        Noeud(xmin, y_centre, x_centre, ymax, depth, self),
    #        Noeud(x_centre, y_centre, xmax, ymax, depth, self)
    #    ]
