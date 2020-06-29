import random
from src.util import listaTabelaQ, listaObjeto

class Robo:
    def __init__(self):
      self.aux = 0
      self.color = 'blue'
      self.x = 0
      self.y = 0
      self.pontos = 0
      self.porcentagem = 70

    def logic(self):
      movimentos = []

      for item in listaTabelaQ.vetorTabelaQ:
        if(item.x == self.x and item.y == self.y):
          movimentos.append(item)   

      por = random.randint(0,100)
      
      if(por <= self.porcentagem):
        maximo = -1000
        for movimento in movimentos:
          if(movimento.recompensa > maximo):
            maximo = movimento.recompensa
        i = 0
        listaMaximo = []
        for movimento in movimentos:
          if movimento.recompensa == maximo:
            listaMaximo.append(i)
          i+=1
        
        j = random.randint(0,len(listaMaximo)-1)
        n = listaMaximo[j]

      else:
        n = random.randint(0,len(movimentos)-1)

      self.x, self.y = movimentos[n].mover()
      
      novosMovimentos = []
      for item in listaTabelaQ.vetorTabelaQ:
        if(item.x == self.x and item.y == self.y):
          novosMovimentos.append(item)

      maximo = novosMovimentos[0].recompensa
      for movimento in novosMovimentos:
        if(movimento.recompensa >= maximo):
          maximo = movimento.recompensa


      movimentos[n].recompensa = listaObjeto[self.y][self.x].recompensa + 0.5 * maximo

      self.pontos += listaObjeto[self.y][self.x].recompensa
