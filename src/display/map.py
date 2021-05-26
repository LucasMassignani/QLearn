import Tkinter as tk 

from src.util import width, height,listaObjeto
from src.ia.robo import Robo

pixels = 60
    
class Map:
    def __init__(self):
        self.menorPontuacao = 10000
        self.countMelhorCaminho = 0
        self.robo = Robo()

        self.verde = [0,0]
        self.vermelho = [0,0]

        self.window = tk.Tk()
        self.window.title("QLearning")
        self.canvas_widget = tk.Canvas(
            self.window, 
            bg='white', 
            height=height * pixels, 
            width=width * pixels
        )
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


    def render(self):
        self.canvas_widget.delete('all')
        for linha in range(width):
            for coluna in range(height):
                objeto = listaObjeto[linha][coluna]

                x1, y1, x2, y2 = linha*pixels, coluna*pixels, linha*pixels+pixels, coluna*pixels+pixels
                self.canvas_widget.create_rectangle(x1, y1, x2, y2, fill=objeto.color, outline="gray")
        
        y1, x1, y2, x2 = self.robo.x*pixels, self.robo.y*pixels, self.robo.x*pixels+pixels, self.robo.y*pixels+pixels
        self.canvas_widget.create_rectangle(x1+10, y1+10, x2-10, y2-10, fill=self.robo.color, outline="gray")
  
        self.canvas_widget.pack()
