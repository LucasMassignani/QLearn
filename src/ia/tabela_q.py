class TabelaQ:
    def __init__(self):
        self.x = 0
        self.y = 0
        
        self.movimento = False

        self.recompensa = 0
    
    def mover(self):
        if(self.movimento=='Direita'):
            return self.x, self.y+1

        if(self.movimento=='Esquerda'):
            return self.x, self.y-1

        if(self.movimento=='Cima'):
            return self.x-1, self.y

        if(self.movimento=='Baixo'):
            return self.x+1, self.y

