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
        self._root = Noeud(0, 10315, 0, 10315)


    def _tester_inserer(self, bateau, noeud, frontiere):
        if(noeud is None):
            noeud = bateau

        elif isinstance(noeud, Bateau):
            ancien_bateau = noeud
            noeud = frontiere
            self._inserer(ancien_bateau, noeud)

            if(noeud.x_centre > 1 or noeud.y_centre > 1):
                self._inserer(bateau, noeud)

        elif isinstance(noeud, Noeud):
            self._inserer(bateau, noeud)

        return noeud


    def _inserer(self, bateau, noeud):
        #On test si le bateau sera trop proche d'un autre.
        #if(noeud.x_centre < 1 or noeud.y_centre < 1):
            #return

        #On crée les frontières.
        if(noeud.frontieres["NO"] is None):
            noeud.creer_frontieres()
            # try:
            # except RecursionError:
            #     print(bateau)
            #     return

        

        if(noeud.frontieres["NO"].dans_frontieres(bateau)):
            noeud.NO = self._tester_inserer(bateau, noeud.NO, noeud.frontieres["NO"])

        elif(noeud.frontieres["NE"].dans_frontieres(bateau)):
            noeud.NE = self._tester_inserer(bateau, noeud.NE, noeud.frontieres["NE"])

        elif(noeud.frontieres["SE"].dans_frontieres(bateau)):
            noeud.SE = self._tester_inserer(bateau, noeud.SE, noeud.frontieres["SE"])

        elif(noeud.frontieres["SO"].dans_frontieres(bateau)):
            noeud.SO = self._tester_inserer(bateau, noeud.SO, noeud.frontieres["SO"])


    def _placer_bateaux(self):
        lst_bateaux = open('./tests/bateaux.txt', 'r').read().splitlines()

        for i in lst_bateaux:
            coord = i.split(' ')
            self._inserer(Bateau(int(coord[0]), int(coord[1])), self._root)


    def _supprimer(self):
        return


    def _detonner_bombes(self):
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
                    for c in p.enfants():
                        if(c is not None):
                            Q.enqueue(c)
            elif(not Q.is_empty()):
                print()
                Q.enqueue(None)
        print()


    def jouer(self):
        self._placer_bateaux()
        #self._detonner_bombes()
        #self._afficher()
        print("TERMINÉ !")
