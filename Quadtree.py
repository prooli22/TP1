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
        self._root = Noeud(0, 16, 0, 16)


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
        #On test si le bateau sera trop proche d'un autre.
        if((noeud.x_max - noeud.x_min < 2) or (noeud.y_max - noeud.y_min < 2)):
            return

        #On crée les frontières.
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
        lst_bateaux = open('./bateaux.txt', 'r').read().splitlines()

        for i in lst_bateaux:
            coord = i.split(' ')
            self._inserer(Bateau(int(coord[0]), int(coord[1])), self._root)

    
    def _tester_supprimer(self, bombe, noeud):
        # Test pour (x1, y1)
        if((bombe.x1 <= noeud.x_max and bombe.x1 >= noeud.x_min) and (bombe.y1 <= noeud.y_max and bombe.y1 >= noeud.y_min)):
            return True

        # Test pour (x2, y1)
        elif((bombe.x2 <= noeud.x_max and bombe.x2 >= noeud.x_min) and (bombe.y1 <= noeud.y_max and bombe.y1 >= noeud.y_min)):
            return True

        # Test pour (x2, y2)
        elif((bombe.x2 <= noeud.x_max and bombe.x2 >= noeud.x_min) and (bombe.y2 <= noeud.y_max and bombe.y2 >= noeud.y_min)):
            return True

        # Test pour (x1, y2)
        elif((bombe.x1 <= noeud.x_max and bombe.x1 >= noeud.x_min) and (bombe.y2 <= noeud.y_max and bombe.y2 >= noeud.y_min)):
            return True

        else:
            return False


    def _supprimer(self, bombe, noeud):
        
        # for c in noeud.enfants():
        #     if isinstance(c, Noeud):
        #         if(self._tester_supprimer(bombe, c)):
        #             c = self._supprimer(bombe, c)

        #     elif isinstance(c, Bateau):
        #         c = None

        #     return c

        # Test NO
        if isinstance(noeud.NO, Noeud):
            if(self._tester_supprimer(bombe, noeud.NO)):
                self._supprimer(bombe, noeud.NO)
                noeud.suicide()
        elif isinstance(noeud.NO, Bateau):
            if((noeud.NO.x <= bombe.x2 and noeud.NO.x >= bombe.x1) and (noeud.NO.y <= bombe.y2 and noeud.NO.y >= bombe.y1)):
                noeud.NO = None
                
        # Test NE
        if isinstance(noeud.NE, Noeud):
            if(self._tester_supprimer(bombe, noeud.NE)):
                self._supprimer(bombe, noeud.NE)
                noeud.suicide()
        elif isinstance(noeud.NE, Bateau):
            if((noeud.NE.x <= bombe.x2 and noeud.NE.x >= bombe.x1) and (noeud.NE.y <= bombe.y2 and noeud.NE.y >= bombe.y1)):            
                noeud.NE = None
                
        # Test SE
        if isinstance(noeud.SE, Noeud):
            if(self._tester_supprimer(bombe, noeud.SE)):
                self._supprimer(bombe, noeud.SE)
                noeud.suicide()
        elif isinstance(noeud.SE, Bateau):    
            if((noeud.SE.x <= bombe.x2 and noeud.SE.x >= bombe.x1) and (noeud.SE.y <= bombe.y2 and noeud.SE.y >= bombe.y1)):            
                noeud.SE = None
                
        # Test SO
        if isinstance(noeud.SO, Noeud):
            if(self._tester_supprimer(bombe, noeud.SO)):
                self._supprimer(bombe, noeud.SO)
                noeud.suicide()
        elif isinstance(noeud.SO, Bateau):
            if((noeud.SO.x <= bombe.x2 and noeud.SO.x >= bombe.x1) and (noeud.SO.y <= bombe.y2 and noeud.SO.y >= bombe.y1)):            
                noeud.SO = None

        self._tester_parents(noeud.parent)


    def _tester_parents(self, noeud):
        if isinstance(noeud, Noeud) and (noeud.NO is None and noeud.NE is None and noeud.SE is None and noeud.SO is None):
            del noeud


    def _detonner_bombes(self):
        lst_bombes = open('./bombes.txt', 'r').read().splitlines()

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
        self._afficher()
        print()
        self._detonner_bombes()
        self._afficher()
        #print("TERMINÉ!")
