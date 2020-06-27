import numpy as np    
import tkinter as tk 
from PIL import Image

from src.ia.robo import Robo

from src.objects.no_color import NoColor
from src.objects.green import Green
from src.objects.red import Red
from src.objects.black import Black
from src.objects.white import White

robo = Robo()

pixels = 60

mapa = Image.open('src/assets/mapa.png')
width, height = mapa.size

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

objetos = [[0 for i in range(10)] for i in range(12)]

class Map:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("QLearning")
        self.canvas_widget = tk.Canvas(
            self.window, 
            bg='white', 
            height=height * pixels, 
            width=width * pixels
        )

        self.montarMapa()

    def montarMapa(self):
        pix = mapa.load()
        for linha in range(width):
            for coluna in range(height):
                r, g, b = pix[linha, coluna]
                posicao = rgb2hex(r, g, b)
                objeto = NoColor()
                
                if posicao=="#ba68c8":
                    objeto = White()
                elif posicao=='#000000':
                    objeto = Black()
                elif posicao=="#c62828":
                    objeto = Red()
                    robo.x = linha
                    robo.y = coluna
                elif posicao=="#4caf50":
                    objeto = Green()
                
                objetos[linha][coluna] = objeto
                

    def logic(self):
        robo.logic()                    

    def render(self):
        for linha in range(width):
            for coluna in range(height):
                objeto = objetos[linha][coluna]

                x1, y1, x2, y2 = linha*pixels, coluna*pixels, linha*pixels+pixels, coluna*pixels+pixels
                self.canvas_widget.create_rectangle(x1, y1, x2, y2, fill=objeto.color, outline="gray")
        

        x1, y1, x2, y2 = robo.x*pixels, robo.y*pixels, robo.x*pixels+pixels, robo.y*pixels+pixels
        self.canvas_widget.create_rectangle(x1+10, y1+10, x2-10, y2-10, fill=robo.color, outline="gray")
  
        self.canvas_widget.pack()
