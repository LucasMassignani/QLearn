# from src.display.map import objetos

class Robo:
    def __init__(self):
      self.aux = 0
      self.color = 'blue'
      self.x = 0
      self.y = 0
      self.pontos = 0

    def logic(self):
      if(self.aux<=2):
        self.x += 1
        self.aux += 1
      elif(self.aux<=7):
        self.y -= 1
        self.aux += 1
      elif(self.aux<=11):
        self.x += 1
        self.aux += 1

      