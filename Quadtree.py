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

        emplacement = noeud.recevoirEmplacement(bateau)
        # SI ON CATCH ---- RETURN

        if(emplacement[0] == None):
            emplacement[0] = bateau

        else:
            if isinstance(emplacement[0], Bateau):
                ancienBateau = emplacement[0]
                emplacement[0] = emplacement[1]
                self._inserer(emplacement[0], ancienBateau)

            self._inserer(emplacement[0], bateau)


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
