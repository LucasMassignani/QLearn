# Objetivo
Este programa tem como objetivo encontrar o caminho mais curto dentro de um mapa e evitar obstáculos.
 
# Como rodar:
Versão: Python 2.7
 
## Primeiro 
Instale todas as bibliotecas. Exemplo com pip: </br>
pip install numpy </br>
pip install tk </br>
pip install Pillow </br>
 
## Segundo
- O arquivo de entrada é o index.py </br>
- Executando ele você verá o robô seguindo o caminho e aprendendo </br>
- Quando ele encontrar o(s) melhor(res) caminhos o programa executa lentamente mostrando o caminho </br>
 
- Se você quiser pular a parte de ver o robô aprendendo pode usar o arquivo index_rapido.py como entrada </br>
- Ele tem a mesma funcionalidade do index.py, porém ele pula a parte de renderização durante a aprendizagem, economizando bastante tempo </br>
 
# Como criar mapas personalizados
- Dentro da pasta ./src/assets crie uma nova imagem (se preferir pode usar a imagem mapa.png como base); </br>
- Utilize o seu programa de preferência para editar a imagem, lembre-se cada pixel da imagem corresponde a uma nova posição no mapa; </br>
- Dentro do arquivo ./src/image.py atualize o nome "src/assets/mapa.png" para o nome da nova imagem; </br>
 
## Cores da imagem:
- #ba68c8 - Bloco branco, onde será possível do robô se mover; </br>
- #000000 - Bloco preto, é um obstáculo, o robô pode se mover por ele mas o ideal é que ele evite; </br>
- #c62828 - Bloco vermelho, é o ponto de partida do robô, deve existir somente um ponto vermelho; </br>
- #4caf50 - Bloco verde, é o ponto de chegada do robô. </br>
- Qualquer outra cor - Bloco cinza, é uma parede, o robô não poderá passar por ela. </br>
