class Noeud:
   def __init__(self, xmin, xmax, ymin, ymax, max_depth=4, parents=None):
       self.xmin = xmin
       self.xmax = xmax
       self.ymin = ymin
       self.ymax = ymax
       self.max_depth = max_depth
       self.enfants_direct = []
       self.quadrants = []
       self.parents = parents
       self.bounds = (xmin, ymin, xmax, ymax)

    def diviser(self):
       xmin, ymin = self.xmin, self.ymin
       xmax, ymax = self.xmax, self.ymax
       x_centre = (xmin + xmax) / 2.0
       y_centre = (ymin + ymax) / 2.0
       depth = self.max_depth - 1
       #Les 4 gros premiers quadrants séparés au milieu de la grille
       self.quadrants = [
           Noeud(xmin, ymin, x_centre, y_centre, depth, self),
           Noeud(x_centre, ymin, xmax, y_centre, depth, self),
           Noeud(xmin, y_centre, x_centre, ymax, depth, self),
           Noeud(x_centre, y_centre, xmax, ymax, depth, self)
       ]
