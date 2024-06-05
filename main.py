import pygame
import os
from tkinter import simpledialog
import tkinter as tk
pygame.init
tamanho = (1000 , 563)
fps = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Universe")
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
space = pygame.image.load("assets/bg.jpg")
tela.blit(space, (0,0) )
branco = (255, 255, 255)
tela = tk.Tk



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type ==  pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
               # posicao_mouse = pygame.mouse.get_pos()
                #print( posicao_mouse)
                #pygame.draw.circle(tela, branco, posicao_mouse, 6,0)
                
                tela =tk.Tk()
                tela.withdraw()
                nametag = simpledialog.askstring("input", "Qual o Nome da estrela?")

    pygame.display.update()
    fps.tick(60)