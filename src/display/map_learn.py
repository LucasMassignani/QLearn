import numpy as np    
import tkinter as tk 

from src.util import width, height,listaObjeto
from src.ia.robo import Robo

class MapLearn:
    def __init__(self):
        self.menorPontuacao = 10000
        self.countMelhorCaminho = 0
        self.robo = Robo()
        
        self.verde = [0,0]
        self.vermelho = [0,0]

        self.init()
                

    def init(self):
        for linha in range(width):
            for coluna in range(height):
                objeto = listaObjeto[linha][coluna]
                if objeto.color == 'green':
                    self.verde = [coluna,linha]

                if objeto.color == 'red':
                    self.robo.y = linha
                    self.robo.x = coluna
                    self.vermelho = [coluna,linha]
                

    def logic(self):
        self.robo.logic()    
        if self.robo.x == self.verde[0] and self.robo.y == self.verde[1]:
            self.robo.x = self.vermelho[0]
            self.robo.y = self.vermelho[1]
            
            if(self.robo.pontos == self.menorPontuacao):
                self.countMelhorCaminho += 1
            elif(self.robo.pontos < self.menorPontuacao):
                self.menorPontuacao = self.robo.pontos
                self.countMelhorCaminho = 1
        self.robo.pontos = 0
