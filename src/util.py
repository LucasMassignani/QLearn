from PIL import Image

from src.objects.no_color import NoColor
from src.objects.green import Green
from src.objects.red import Red
from src.objects.black import Black
from src.objects.white import White

from src.ia.lista_tabela_q import ListaTabelaQ


mapaImg = Image.open('src/assets/mapa.png')
width, height = mapaImg.size

listaObjeto = [[0 for i in range(10)] for i in range(12)]

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def montarMapa():
    pix = mapaImg.load()
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
            elif posicao=="#4caf50":
                objeto = Green()
            
            listaObjeto[linha][coluna] = objeto

montarMapa()

listaTabelaQ = ListaTabelaQ(listaObjeto)