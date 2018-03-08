'''
    Fichier : Quadtree
    Projet  : TP1
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

import sys
from Noeud import Noeud
from Bateau import Bateau
from ListQueue import ListQueue

class Quadtree():
    def __init__(self):
        self.root = Noeud(0, 16, 0, 16)

    def _inserer(self, bateau, noeud):
    
        # Test des frontières maximales du noeud.
        if((bateau.x >= noeud.frontiere.xmin and bateau.x <= noeud.frontiere.xmax) 
        and (bateau.y >= noeud.frontiere.ymin and bateau.y <= noeud.frontiere.ymax)):

            # Test quadrant NO.
            if(bateau.x <= noeud.x_centre and bateau.y <= noeud.y_centre):
                if(noeud.NO == None):
                    noeud.NO = bateau

                elif(isinstance(noeud.NO, Bateau))
                    ancienBateau = noeud.NO
                    noeud.NO = Noeud(noeud.frontiere.xmin, 
                                     noeud.x_centre, 
                                     noeud.frontiere.ymin, 
                                     noeud.y_centre,
                                     noeud)
                    self._inserer(ancienBateau, noeud.NO)
                    self._inserer(bateau, noeud.NO)

                else
                    self._inserer(bateau, noeud.NO)

            # Test quadrant NE.
            elif(bateau.x >= noeud.x_centre and bateau.y <= noeud.y_centre):
                if(noeud.NE == None):
                    noeud.NE= bateau

                elif(isinstance(noeud.NO, Bateau))
                    ancienBateau = noeud.NE
                    noeud.NE = Noeud(noeud.frontiere.xmin, 
                                     noeud.x_centre, 
                                     noeud.frontiere.ymin, 
                                     noeud.y_centre,
                                     noeud)
                    self._inserer(ancienBateau, noeud.NE)
                    self._inserer(bateau, noeud.NE)

                else
                    self._inserer(bateau, noeud.NE)

            # Test quadrant SE.
            elif(bateau.x >= noeud.x_centre and bateau.y >= noeud.y_centre):
                if(noeud.SE == None):
                    noeud.SE = bateau

                elif(isinstance(noeud.SE, Bateau))
                    ancienBateau = noeud.SE
                    noeud.SE = Noeud(noeud.frontiere.xmin, 
                                     noeud.x_centre, 
                                     noeud.frontiere.ymin, 
                                     noeud.y_centre,
                                     noeud)
                    self._inserer(ancienBateau, noeud.SE)
                    self._inserer(bateau, noeud.SE)

                else
                    self._inserer(bateau, noeud.SE)

            # Test quadrant SO.
            elif(bateau.x <= noeud.x_centre and bateau.y >= noeud.y_centre):
                if(noeud.SO == None):
                    noeud.SO = bateau

                elif(isinstance(noeud.NO, Bateau))
                    ancienBateau = noeud.SO
                    noeud.NO = Noeud(noeud.frontiere.xmin, 
                                     noeud.x_centre, 
                                     noeud.frontiere.ymin, 
                                     noeud.y_centre,
                                     noeud)
                    self._inserer(ancienBateau, noeud.SO)
                    self._inserer(bateau, noeud.SO)

                else
                    self._inserer(bateau, noeud.SO)

    
    def _placerBateaux(self, ):
        listeBateaux = open('bateaux.txt', 'r').read().splitlines()
        
        for i in listeBateaux:
            self.inserer(Bateau(int(i.split(' ')[0]), int(i.split(' ')[1])), self.root)


    def _supprimer(self):



    def _detonnerBombes(self):


    def _imprimer(self, p):
        if(isinstance(p, Bateau))
            print('[' + p.x + ' ' + p.y + ']')

        else
            print('<' + p.NO + ' ' + p.NE + ' ' + p.SE + ' ' + p.SO + '>')


    def _afficher(self):
        Q = ListQueue()
        Q.enqueue( self.root )
        while not Q.is_empty():
            p = Q.dequeue()
            self._imprimer( p )
            for c in p.children():
                Q.enqueue( c )


    def jouer(self):
            self._placerBateaux()
            self._detonnerBombes()
            self._afficher()
