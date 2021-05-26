import time

from src.display.map import Map

mapa = Map()

while mapa.countMelhorCaminho<=200:
  mapa.logic()

mapa.robo.porcentagem = 100

while True:
  mapa.render()
  mapa.logic()
  mapa.window.update_idletasks()
  mapa.window.update()
  time.sleep(0.5)

