
from src.objects.no_color import NoColor
from src.objects.green import Green
from src.objects.red import Red
from src.objects.black import Black
from src.objects.white import White

from src.ia.lista_tabela_q import ListaTabelaQ
from src.image import height, width, mapaImg

listaObjeto = [[0 for i in range(height)] for i in range(width)]

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def montarMapa():
    pix = mapaImg.load()
    for linha in range(width):
        for coluna in range(height):
            try:
                r, g, b = pix[linha, coluna]
            except:
                r, g, b, a = pix[linha, coluna]

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