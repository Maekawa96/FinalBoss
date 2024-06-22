import pygame
import os
import sys
import pickle
from tkinter import simpledialog
import tkinter as tk
import math

pygame.init()
pygame.font.init()

# Configurações da tela
tamanho = (1000, 563)
fps = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Universe")

# Ícone e fundo
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load("assets/bg.jpg")

# Cores e fonte
branco = (255, 255, 255)
fonte = pygame.font.SysFont("comicsans", 15)

# Dicionário para armazenar estrelas
estrelas = {}

# Inicializa o Tkinter
root = tk.Tk()
root.withdraw()

# Teclas especiais
TECLA_SALVAR = pygame.K_F10
TECLA_CARREGAR = pygame.K_F11
TECLA_EXCLUIR = pygame.K_F12

# Arquivo de marcações
ARQUIVO_MARCACOES = "marcacoes.pkl"

def salvar_marcacoes():
    try:
        with open(ARQUIVO_MARCACOES, "wb") as arquivo:
            pickle.dump(estrelas, arquivo)
    except IOError as e:
        print("Erro ao salvar marcações:", e)

def carregar_marcacoes():
    global estrelas
    try:
        if os.path.exists(ARQUIVO_MARCACOES):
            with open(ARQUIVO_MARCACOES, "rb") as arquivo:
                estrelas = pickle.load(arquivo)
    except IOError as e:
        print("Erro ao carregar marcações:", e)

def excluir_marcacoes():
    estrelas.clear()

def distancia(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

def mostrar_mensagem(texto, pos):
    mensagem = fonte.render(texto, True, branco)
    tela.blit(mensagem, pos)

def desenhar_tracado_sequencial():
    estrelas_ordenadas = list(estrelas.keys())
    if len(estrelas_ordenadas) > 1:
        for i in range(len(estrelas_ordenadas) - 1):
            estrela1 = estrelas_ordenadas[i]
            estrela2 = estrelas_ordenadas[i + 1]
            pygame.draw.line(tela, branco, estrela1, estrela2, 1)
            distancia_entre_estrelas = distancia(estrela1, estrela2)
            mediaX = (estrela1[0] + estrela2[0]) / 2
            mediaY = (estrela1[1] + estrela2[1]) / 2
            texto_distancia = fonte.render(f"{distancia_entre_estrelas:.2f}", True, branco)
            tela.blit(texto_distancia, (mediaX, mediaY))

def marcar():
    carregar_marcacoes()
    mensagem_temporaria = None
    contador_tempo = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salvar_marcacoes()
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if evento.button == 1:  # Adicionar estrela
                    nome = simpledialog.askstring("Space", "Nome da estrela:")
                    if not nome:
                        nome = f"Indefinido ({x}, {y})"
                    estrelas[(x, y)] = nome
                elif evento.button == 3:  # Remover estrela
                    for pos in list(estrelas.keys()):
                        if distancia(pos, (x, y)) <= 10:
                            del estrelas[pos]
            elif evento.type == pygame.KEYDOWN:
                if evento.key == TECLA_SALVAR:
                    salvar_marcacoes()
                    mensagem_temporaria = "Marcações salvas (F10)."
                    contador_tempo = pygame.time.get_ticks()
                elif evento.key == TECLA_CARREGAR:
                    carregar_marcacoes()
                    mensagem_temporaria = "Marcações carregadas (F11)."
                    contador_tempo = pygame.time.get_ticks()
                elif evento.key == TECLA_EXCLUIR:
                    excluir_marcacoes()
                    mensagem_temporaria = "Marcações excluídas (F12)."
                    contador_tempo = pygame.time.get_ticks()

        tela.blit(fundo, (0, 0))

        for xyEstrela, nome in estrelas.items():
            pygame.draw.circle(tela, branco, xyEstrela, 4)
            mostrar_mensagem(nome, (xyEstrela[0] + 10, xyEstrela[1] - 10))

        desenhar_tracado_sequencial()

        if mensagem_temporaria:
            mostrar_mensagem(mensagem_temporaria, (10, 10))
            if pygame.time.get_ticks() - contador_tempo > 2000:
                mensagem_temporaria = None

        mostrar_mensagem("F10: Salvar | F11: Carregar | F12: Excluir | Botão direito: Excluir apenas uma | Botão esquerdo: Criar", (10, 40))

        pygame.display.update()
        fps.tick(60)

marcar()
