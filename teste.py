import pygame
import os
from tkinter import simpledialog
import tkinter as tk
import math 

pygame.init()
pygame.font.init()
# Configuracoes da tela
tamanho = (1000, 563)
fps = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Universe")
#Icone e fundo
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load("assets/bg.jpg")
# Cores e fonte
branco = (255, 255, 255)
fonte = pygame.font.SysFont("comicsans", 15)
# Dicionario para armazenar estrelas
estrelas = {}

# Inicializa o Tkinter
root = tk.Tk()
root.withdraw()
#calcular a distancia entre as estrelas
def distancia(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#marcar as estrelas    
def marcar():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:  # Botão esquerdo do mouse para adicionar estrelas
                    x, y = pygame.mouse.get_pos()
                    item = simpledialog.askstring("Space", "Nome da estrela:")
                    if not item:
                        item = f"Indefinido ({x}, {y})"
                    estrelas[(x, y)] = item
                elif evento.button == pygame.MOUSEBUTTONDOWN:  # Botão direito do mouse para remover estrelas
                    x, y = pygame.mouse.get_pos()
                    # Verificar se o clique está próximo de alguma estrela existente
                    for pos in list(estrelas.keys()):  # Convertendo para lista para evitar RuntimeError
                        if distancia(pos, (x, y)) <= 10:  # Verifica se está dentro de um raio de 10 pixels
                            del estrelas[pos]
                elif evento.type == pygame.K_BACKSPACE:  # Tecla Backspace para deletar todas as estrelas
                            estrelas.clear()

        # Preenche a tela com o fundo
        tela.blit(fundo, (0, 0))

        # Desenha todas as estrelas
        for xyEstrela, nome in estrelas.items():
            pygame.draw.circle(tela, branco, xyEstrela, 4)
            imgTexto = fonte.render(nome, True, branco)
            tela.blit(imgTexto, (xyEstrela[0] + 10, xyEstrela[1] - 10))

        desenhar_tracado_sequencial()
        # Atualiza a tela
        pygame.display.update()
        fps.tick(60)

def desenhar_tracado_sequencial():
    # Ordena as estrelas pela ordem em que foram marcadas
    estrelasOrdenadas = list(estrelas.keys())
    if len(estrelasOrdenadas) > 1:
        for i in range(len(estrelasOrdenadas) - 1):
            estrela1 = estrelasOrdenadas[i]
            estrela2 = estrelasOrdenadas[i + 1]
            pygame.draw.line(tela, branco, estrela1, estrela2, 1)
            # Calcula a distância entre as estrelas marcadas
            distancia_entre_estrelas = distancia(estrela1, estrela2)
            # Coordenadas entre as estrelas
            mediaX = (estrela1[0] + estrela2[0]) / 2
            mediaY = (estrela1[1] + estrela2[1]) / 2
            # Calcula o ângulo da linha entre as estrelas
            angulo = math.atan2(estrela2[1] - estrela1[1], estrela2[0] - estrela1[0])
            # INdentifica a posição das estrelas para exibir a distancia entre elas 
            texto1 = mediaX + angulo
            texto2 = mediaY+ angulo
            # Exibe a distância sobre o traçado
            texto_distancia = fonte.render(f"Distância: {distancia_entre_estrelas:.2f}", True, branco)
            tela.blit(texto_distancia, (texto1, texto2))

 
        pygame.display.update()
        fps.tick(60)


# Inicia o loop principal
marcar()

