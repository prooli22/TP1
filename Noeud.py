'''
    Fichier : Noeud
    Projet  : TP1
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

class Noeud:
    def __init__(self, xmin, xmax, ymin, ymax, parents=None):
        #self.quadrants = {"NO" = None, "NE" = None, "SE" = None, "SO" = None}
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.NO = None
        self.NE = None
        self.SE = None
        self.SO = None
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

    def diviser(self):
       xmin, ymin = self.xmin, self.ymin
       xmax, ymax = self.xmax, self.ymax
       x_centre = (xmin + xmax) / 2.0
       y_centre = (ymin + ymax) / 2.0
       #self.quadrants["NO"] = Noeud(xmin, ymin, x_centre, y_centre, self)
       #self.quadrants["NE"] = Noeud(xmin, ymin, x_centre, y_centre, self)
       #self.quadrants["SE"] = Noeud(xmin, ymin, x_centre, y_centre, self)
       #self.quadrants["SO"] = Noeud(xmin, ymin, x_centre, y_centre, self)


    def recevoirEmplacement(self, bateau):
        xmin, ymin = self.xmin, self.ymin
        xmax, ymax = self.xmax, self.ymax
        x_centre = (xmin + xmax) / 2.0
        y_centre = (ymin + ymax) / 2.0
         # Test des frontières maximales du noeud.
        if((bateau.x >= self.xmin and bateau.x <= self.xmax)
            and (bateau.y >= self.ymin and bateau.y <= self.ymax)):

            # Test quadrant NO.
            if(bateau.x <= self.x_centre and bateau.y <= self.y_centre):
                return [ self.NO, Noeud(xmin, ymin, x_centre, y_centre, self) ]

            # Test quadrant NE.
            elif(bateau.x >= self.x_centre and bateau.y <= self.y_centre):
                return [ self.NE, Noeud(x_centre, ymin, xmax, y_centre, self) ]

            # Test quadrant SE.
            elif(bateau.x >= self.x_centre and bateau.y >= self.y_centre):
                return [ self.SE, Noeud(x_centre, y_centre, xmax, ymax, self) ]

            # Test quadrant SO.
            elif(bateau.x <= self.x_centre and bateau.y >= self.y_centre):
                return [ self.SO, Noeud(xmin, y_centre, x_centre, ymax, self) ]

            #else:
                #THROW EXCEPTION
        #else:
            #THROW EXCEPTION

       