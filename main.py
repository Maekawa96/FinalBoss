import pygame
import os
from tkinter import simpledialog
import tkinter as tk

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

def marcar():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    # Obtem a posicao do clique
                    x, y = pygame.mouse.get_pos()
                    #caixa de dialogo
                    item = simpledialog.askstring("Space", "Nome da estrela:")
                    if not item:
                        item = f"desconhecido ({x}, {y})"
                    estrelas[(x, y)] = item
            
        # Preenche a tela com o fundo
        tela.blit(fundo, (0, 0))

        # Desenha todas as estrelas
        for posicaoEstrela, nome in estrelas.items():
            pygame.draw.circle(tela, branco, posicaoEstrela, 4)
            imgTexto = fonte.render(nome, True, branco)
            tela.blit(imgTexto, (posicaoEstrela[0] + 10, posicaoEstrela[1] - 10))

        desenhar_tracado_sequencial()
        # Atualiza a tela
        pygame.display.update()
        fps.tick(60)

def desenhar_tracado_sequencial():
    # Ordena as estrelas pela ordem em que foram marcadas
    estrelasOrdenadas = list(estrelas.keys())
    if len(estrelasOrdenadas) > 1:
        for i in range(len(estrelasOrdenadas) - 1):
            estrelaAtual = estrelasOrdenadas[i]
            proximaEstrela = estrelasOrdenadas[i + 1]
            pygame.draw.line(tela, branco, estrelaAtual, proximaEstrela, 1)       
        
        
        pygame.display.update()
        fps.tick(60)


# Inicia o loop principal
marcar()
