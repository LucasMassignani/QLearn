import time

from src.display.map import Map
from src.display.map_learn import MapLearn

mapa = MapLearn()

while mapa.countMelhorCaminho<=100:
  mapa.logic()

mapa = Map()

while True:
  mapa.render()
  mapa.logic()
  mapa.window.update_idletasks()
  mapa.window.update()
  time.sleep(0.5)

