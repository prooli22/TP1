'''
    Fichier : Quadtree
    Projet  : TP1
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

import sys
from math import log
from Noeud import Noeud
from Bateau import Bateau
from ListQueue import ListQueue

class Quadtree():
    def __init__(self):
        self._root = Noeud(0, 16, 0, 16)

    def _inserer(self, bateau, noeud):

        #if not isinstance(bateau, Bateau) or not isinstance(noeud, Noeud):
            #return

        # Test des frontières maximales du noeud.
        if((bateau.x >= noeud.xmin and bateau.x <= noeud.xmax)
        and (bateau.y >= noeud.ymin and bateau.y <= noeud.ymax)):

            # Test quadrant NO.
            if(bateau.x <= noeud.x_centre and bateau.y <= noeud.y_centre):
                if(noeud.NO == None):
                    noeud.NO = bateau

                elif isinstance(noeud.NO, Bateau):
                    ancienBateau = noeud.NO
                    noeud.NO = Noeud(noeud.xmin,
                                     noeud.x_centre,
                                     noeud.ymin,
                                     noeud.y_centre,
                                     noeud)
                    self._inserer(ancienBateau, noeud.NO)
                    self._inserer(bateau, noeud.NO)

                else:
                    self._inserer(bateau, noeud.NO)

            # Test quadrant NE.
            elif(bateau.x >= noeud.x_centre and bateau.y <= noeud.y_centre):
                if(noeud.NE == None):
                    noeud.NE= bateau

                elif isinstance(noeud.NE, Bateau):
                    ancienBateau = noeud.NE
                    noeud.NE = Noeud(noeud.x_centre,
                                     noeud.xmax,
                                     noeud.ymin,
                                     noeud.y_centre,
                                     noeud)
                    self._inserer(ancienBateau, noeud.NE)
                    self._inserer(bateau, noeud.NE)

                else:
                    self._inserer(bateau, noeud.NE)

            # Test quadrant SE.
            elif(bateau.x >= noeud.x_centre and bateau.y >= noeud.y_centre):
                if(noeud.SE == None):
                    noeud.SE = bateau

                elif isinstance(noeud.SE, Bateau):
                    ancienBateau = noeud.SE
                    noeud.SE = Noeud(noeud.x_centre,
                                     noeud.xmax,
                                     noeud.y_centre,
                                     noeud.ymax,
                                     noeud)
                    self._inserer(ancienBateau, noeud.SE)
                    self._inserer(bateau, noeud.SE)

                else:
                    self._inserer(bateau, noeud.SE)

            # Test quadrant SO.
            elif(bateau.x <= noeud.x_centre and bateau.y >= noeud.y_centre):
                if(noeud.SO == None):
                    noeud.SO = bateau

                elif isinstance(noeud.SO, Bateau):
                    ancienBateau = noeud.SO
                    noeud.NO = Noeud(noeud.xmin,
                                     noeud.x_centre,
                                     noeud.y_centre,
                                     noeud.ymax,
                                     noeud)
                    self._inserer(ancienBateau, noeud.SO)
                    self._inserer(bateau, noeud.SO)

                else:
                    self._inserer(bateau, noeud.SO)


    def _placerBateaux(self):
        listeBateaux = open('bateaux.txt', 'r').read().splitlines()

        for i in listeBateaux:
            self._inserer(Bateau(int(i.split(' ')[0]), int(i.split(' ')[1])), self._root)


    def _supprimer(self):
        return


    def _detonnerBombes(self):
        return

    def _afficher(self):
        Q = ListQueue()
        Q.enqueue( self._root )
        Q.enqueue(None)
        while not Q.is_empty():
            p = Q.dequeue()
            if(p is not None):
                print(p, end='')
                if isinstance(p, Noeud):
                    for c in p.children():
                        if(c is not None):
                            Q.enqueue(c)
            elif(not Q.is_empty()):
                print()
                Q.enqueue(None)
        print()


    def jouer(self):
            self._placerBateaux()
            self._detonnerBombes()
            self._afficher()
