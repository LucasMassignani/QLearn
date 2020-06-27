import time

from src.display.map import Map
from src.ia.robo import Robo

mapa = Map()
while True:
  mapa.render()
  mapa.logic()
  mapa.window.update_idletasks()
  mapa.window.update()
  time.sleep(0.5)

