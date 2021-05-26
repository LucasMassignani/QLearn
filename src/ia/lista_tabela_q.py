from src.ia.tabela_q import TabelaQ
from src.image import height, width

class ListaTabelaQ:
    def __init__(self, objetos):
        self.vetorTabelaQ = []

        coluna_i = 0
        for coluna in objetos:
          linha_j = 0
          for item in coluna:
            if item.recompensa:
              # Cima
              
              auxX = linha_j - 1
              auxY = coluna_i

              if auxX >= 0:
                auxItem = objetos[auxY][auxX]
                if auxItem.recompensa:
                  tabelaQ = TabelaQ()
                  tabelaQ.x = linha_j
                  tabelaQ.y = coluna_i

                  tabelaQ.movimento = 'Cima'
                  self.vetorTabelaQ.append(tabelaQ)

              # End Cima

              # Baixo

              auxX = linha_j + 1 
              auxY = coluna_i

              if auxX <= height-1:
                auxItem = objetos[auxY][auxX]
                if auxItem.recompensa:
                  tabelaQ = TabelaQ()
                  tabelaQ.x = linha_j
                  tabelaQ.y = coluna_i

                  tabelaQ.movimento = 'Baixo'
                  self.vetorTabelaQ.append(tabelaQ)

              # End Baixo

              # Direita

              auxX = linha_j
              auxY = coluna_i + 1


              if auxY <= width-1:
                auxItem = objetos[auxY][auxX]
                if auxItem.recompensa:
                  tabelaQ = TabelaQ()
                  tabelaQ.x = linha_j
                  tabelaQ.y = coluna_i

                  tabelaQ.movimento = 'Direita'
                  self.vetorTabelaQ.append(tabelaQ)

              # End Direita

              # Esquerda

              auxX = linha_j
              auxY = coluna_i - 1

              if auxY >= 0:
                auxItem = objetos[auxY][auxX]
                if auxItem.recompensa:
                  tabelaQ = TabelaQ()
                  tabelaQ.x = linha_j
                  tabelaQ.y = coluna_i

                  tabelaQ.movimento = 'Esquerda'
                  self.vetorTabelaQ.append(tabelaQ)

              # End Esquerda

            linha_j+=1
          coluna_i+=1
