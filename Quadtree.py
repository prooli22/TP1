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
from Bombe import Bombe
from ListQueue import ListQueue

class Quadtree():
    def __init__(self):
        self._root = Noeud(0, 3, 0, 3)


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
        # On test si le bateau sera trop proche d'un autre.
        if((noeud.x_max - noeud.x_min < 2) or (noeud.y_max - noeud.y_min < 2)):
            print("noeud trop près")

            if()
                
                    
        # On crée les frontières.
        if(noeud.frontieres["NO"] is None):
            noeud.creer_frontieres()

        if(noeud.frontieres["NO"].dans_frontieres(bateau)):
            noeud.NO = self._tester_inserer(bateau, noeud.NO, noeud.frontieres["NO"])

        elif(noeud.frontieres["NE"].dans_frontieres(bateau)):
            noeud.NE = self._tester_inserer(bateau, noeud.NE, noeud.frontieres["NE"])

        elif(noeud.frontieres["SE"].dans_frontieres(bateau)):
            noeud.SE = self._tester_inserer(bateau, noeud.SE, noeud.frontieres["SE"])

        elif(noeud.frontieres["SO"].dans_frontieres(bateau)):
            noeud.SO = self._tester_inserer(bateau, noeud.SO, noeud.frontieres["SO"])


    def _placer_bateaux(self):
        lst_bateaux = open('bateaux.txt', 'r').read().splitlines()

        for i in lst_bateaux:
            coord = i.split(' ')
            self._inserer(Bateau(int(coord[0]), int(coord[1])), self._root)

    
    def _tester_supprimer(self, bombe, noeud):
        # Test pour (x1, y1).
        if((bombe.x1 <= noeud.x_max and bombe.x1 >= noeud.x_min) and (bombe.y1 <= noeud.y_max and bombe.y1 >= noeud.y_min)):
            return True

        # Test pour (x2, y1).
        elif((bombe.x2 <= noeud.x_max and bombe.x2 >= noeud.x_min) and (bombe.y1 <= noeud.y_max and bombe.y1 >= noeud.y_min)):
            return True

        # Test pour (x2, y2).
        elif((bombe.x2 <= noeud.x_max and bombe.x2 >= noeud.x_min) and (bombe.y2 <= noeud.y_max and bombe.y2 >= noeud.y_min)):
            return True

        # Test pour (x1, y2).
        elif((bombe.x1 <= noeud.x_max and bombe.x1 >= noeud.x_min) and (bombe.y2 <= noeud.y_max and bombe.y2 >= noeud.y_min)):
            return True

        # Test si la bombe recouvre tout le noeud.
        elif((noeud.x_min >= bombe.x1 and noeud.x_max <= bombe.x2) and (noeud.y_min >= bombe.y1 and noeud.y_max <= bombe.y2)):
            return True

        else:
            return False


    def _supprimer_nuls(self, enfant, noeud):
        if(enfant == noeud.NO and noeud.NO.enfants_nuls()):
            noeud.NO = None
        elif(enfant == noeud.NE and noeud.NE.enfants_nuls()):
            noeud.NE = None
        elif(enfant == noeud.SE and noeud.SE.enfants_nuls()):
            noeud.SE = None
        elif(enfant == noeud.SO and noeud.SO.enfants_nuls()):
            noeud.SO = None


    def _supprimer(self, bombe, noeud):
        
        for c in noeud.enfants():
            if isinstance(c, Noeud):
                if(self._tester_supprimer(bombe, c)):
                    self._supprimer(bombe, c)
                    self._supprimer_nuls(c, noeud)

            elif isinstance(c, Bateau):
                if((c.x <= bombe.x2 and c.x >= bombe.x1) and (c.y <= bombe.y2 and c.y >= bombe.y1)):
                    if(c == noeud.NO):
                        noeud.NO = None
                    elif(c == noeud.NE):
                        noeud.NE = None
                    elif(c == noeud.SE):
                        noeud.SE = None
                    elif(c == noeud.SO):
                        noeud.SO = None


    def _detonner_bombes(self):
        lst_bombes = open('./tests/bombes.txt', 'r').read().splitlines()

        for i in lst_bombes:
            coord = i.split('.')
            self._supprimer(Bombe(int(coord[0]), int(coord[1]), int(coord[2]), int(coord[3])), self._root)    


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
