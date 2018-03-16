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
            self._inserer(bateau, noeud)

        elif isinstance(noeud, Noeud):
            self._inserer(bateau, noeud)

        return noeud


    def _inserer(self, bateau, noeud):

        # On crée les frontières.
        if(not noeud.frontiere):
            noeud.creer_frontieres()

        if(noeud.frontieres["NO"].dans_frontieres(bateau)):
            noeud.NO = self._tester_inserer(bateau, noeud.NO, noeud.frontieres["NO"])

        elif(noeud.frontieres["NE"].dans_frontieres(bateau)):
            noeud.NE = self._tester_inserer(bateau, noeud.NE, noeud.frontieres["NE"])

        elif(noeud.frontieres["SE"].dans_frontieres(bateau)):
            noeud.SE = self._tester_inserer(bateau, noeud.SE, noeud.frontieres["SE"])

        elif(noeud.frontieres["SO"].dans_frontieres(bateau)):
            noeud.SO = self._tester_inserer(bateau, noeud.SO, noeud.frontieres["SO"])

        # for cle, valeur in noeud.frontieres.items():
        #     if(valeur.dans_frontieres(bateau)):
        #         if(cle == "NO"):
        #             noeud.NO = self._tester_inserer(bateau, noeud.NO, valeur)
        #         elif(cle == "NE"):
        #             noeud.NE = self._tester_inserer(bateau, noeud.NE, valeur)
        #         elif(cle == "SE"):
        #             noeud.SE = self._tester_inserer(bateau, noeud.SE, valeur)
        #         elif(cle == "SO"):
        #             noeud.SO = self._tester_inserer(bateau, noeud.SO, valeur)
        #         return


    def _placer_bateaux(self):
        lst_bateaux = open('./tests/bateaux.txt', 'r').read().splitlines()

        for i in lst_bateaux:
            self._inserer(Bateau(int(i.split(' ')[0]), int(i.split(' ')[1])), self._root)


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
            self._detonner_bombes()
            self._afficher()
