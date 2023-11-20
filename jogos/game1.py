from pdb import run
from re import T
import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
from tkinter import messagebox
import os
import pygame
import subprocess
import time

pygame.mixer.init()


contador_end = 0

def play_certo():
    pygame.mixer.music.load("acertou.mp3")
    pygame.mixer.music.play(loops=0)

def play_errado():
    pygame.mixer.music.load("erro.mp3")
    pygame.mixer.music.play(loops=0)

music_chanel = pygame.mixer.Channel(2)
def final_audio():
    pygame.mixer.music.load("final_desafio.mp3")
    music_chanel.play(pygame.mixer.Sound("final_desafio.mp3"), loops=-1)

# Função para verificar a resposta selecionada
def verificar_resposta(resposta_correta):
    global contador_end
    resposta_selecionada = var_resposta.get()
    if resposta_selecionada == resposta_correta:
        global contador_end
        contador_end = contador_end + 1
        tk.messagebox.showinfo(title="Você Acertou!", message="Parabéns!")
        play_certo()
        if contador_end <= 5:
            avancar()
        elif contador_end <=5:
            root.destroy()

        else:
            print("acabou o jogo")
            root.destroy()
            #subprocess.run(["python", "python2.py"])

    else:
        tk.messagebox.showinfo(title="Você errou!", message="TENTE NOVAMENTE!")
        play_errado()

# Função para avançar para a próxima pergunta
def avancar():
    global index
    if index < len(perguntas) - 2:
        index += 1
        mostrar_pergunta()
    elif index <= 6:
        tk.messagebox.showinfo(title="PARABÉNS!", message="VOCÊ ACERTOU AS PERGUNTAS DO DESAFIO!")
        final_audio()
        time.sleep(3)
        root.destroy()

# Função para mostrar a pergunta atual
def mostrar_pergunta():
    pergunta = perguntas[index]
    imagem_path = pergunta['imagem']
    img = PhotoImage(file=imagem_path)
    label_imagem.config(image=img)
    label_imagem.image = img
    label_pergunta.config(text=pergunta['pergunta'])
    for i, resposta in enumerate(pergunta['respostas']):
        botoes_resposta[i].config(text=resposta, value=i)

def botao_quit():
    root.destroy()

# Criação da janela principal
root = tk.Tk()
root.title("Jogo de Perguntas e Respostas")

# Definição das perguntas e respostas
perguntas = [
    {
        'imagem': 'imagem1.png',
        'pergunta': 'Quanto é 1 + 1?',
        'respostas': ['1', '2', '3', '4'],
        'resposta_correta': 1,
    },
    {
        'imagem': 'imagem2.png',
        'pergunta': 'Quanto é 5 + 5??',
        'respostas': ['1', '3', '10', '4'],
        'resposta_correta': 2,
    },
    {
        'imagem': 'imagem3.png',
        'pergunta': 'Quanto é 5 + 5??',
        'respostas': ['1', '3', '10', '4'],
        'resposta_correta': 2,
    },
    {
        'imagem': 'imagem4.png',
        'pergunta': 'Quanto é 5 + 5??',
        'respostas': ['1', '3', '10', '4'],
        'resposta_correta': 2,
    },
    {
        'imagem': 'imagem5.png',
        'pergunta': 'Quanto é 5 + 5??',
        'respostas': ['1', '3', '10', '4'],
        'resposta_correta': 2,
    },
    {
        'imagem': 'imagem6.png',
        'pergunta': 'Quanto é 5 + 5??',
        'respostas': ['1', '3', '10', '4'],
        'resposta_correta': 2,
    }
]

# Inicialização de variáveis
index = 0

# Criação do widget de imagem
img = PhotoImage(file=perguntas[index]['imagem'])
label_imagem = tk.Label(root, image=img)
label_imagem.pack()

# Label para a pergunta
label_pergunta = tk.Label(root, text=perguntas[index]['pergunta'])
label_pergunta.pack()

# Variável para armazenar a resposta selecionada
var_resposta = tk.IntVar()

# Botões de resposta
botoes_resposta = []
for i, resposta in enumerate(perguntas[index]['respostas']):
    btn = tk.Radiobutton(root, text=resposta, variable=var_resposta, value=i)
    btn.pack()
    botoes_resposta.append(btn)

# Botão para verificar a resposta
btn_verificar = tk.Button(root, text="Verificar Resposta", command=lambda: verificar_resposta(perguntas[index]['resposta_correta']))
btn_verificar.pack()

# Inicialização da primeira pergunta
mostrar_pergunta()

root.mainloop()
