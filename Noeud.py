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
        #self.xmin = xmin
        #self.xmax = xmax
        #self.ymin = ymin
        #self.ymax = ymax
        self.parents = parents
        self.frontiere = (xmin, ymin, xmax, ymax)
        self.x_centre = (noeud.frontiere.xmin + noeud.frontiere.xmax) / 2
        self.y_centre = (noeud.frontiere.ymin + noeud.frontiere.ymax) / 2


    def children (self)
        return [ self.NE, self.NO, self.SE, self.SO ]

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


