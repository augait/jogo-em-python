import tkinter as tk
from tkinter import messagebox
import pygame

screen_width, screen_height = 800,800
pygame.mixer.init()
music_chanel = pygame.mixer.Channel(2)


pygame.mixer.init()

def play_certo():
    pygame.mixer.music.load("acertou.mp3")
    pygame.mixer.music.play(loops=0)

def play_errado():
    pygame.mixer.music.load("erro.mp3")
    pygame.mixer.music.play(loops=0)
def play_perg():
    pygame.mixer.music.load("novaperg.mp3")
    music_chanel.play(pygame.mixer.Sound("novaperg.mp3"), loops=0)


# Dicionário com perguntas e respostas de história
perguntas_respostas = {
    "Quem foi o primeiro presidente dos Brasil?": "deodoro da fonseca",
    "Quando começou a segunda guerra mundial": "1939",
    "Quem descobriu o Brasil?": "pedro alvares cabral",
    "Quando o Brasil foi descoberto?": "1500",
    "o que os portugueses encontraram quando chegaram no Brasil?": "indigenas",
    # Adicione mais perguntas e respostas de história
}

class JogoHistoria:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo de História")

        self.pergunta_label = tk.Label(janela, text="Pergunta:")
        self.pergunta_label.pack()

        self.resposta_entry = tk.Entry(janela)
        self.resposta_entry.pack()

        self.botao_verificar = tk.Button(janela, text="Verificar", command=self.verificar_resposta)
        self.botao_verificar.pack()

        self.pergunta_atual = None
        self.resposta_correta = None

        self.proxima_pergunta()

    def proxima_pergunta(self):
        if perguntas_respostas:
            self.pergunta_atual, self.resposta_correta = perguntas_respostas.popitem()
            self.pergunta_label.config(text="Pergunta: " + self.pergunta_atual)
            play_perg()
        else:
            messagebox.showinfo("Parabéns", "Você respondeu todas as perguntas!")
            self.janela.quit()

    def verificar_resposta(self):
        resposta_usuario = self.resposta_entry.get()
        if resposta_usuario.lower() == self.resposta_correta.lower():
            messagebox.showinfo("Resposta Correta", "Você acertou!")
            play_certo()
        else:
            messagebox.showerror("Resposta Incorreta", "Você errou. A resposta correta é: " + self.resposta_correta)
            play_errado()
        self.resposta_entry.delete(0, "end")  # Limpa a entrada
        self.proxima_pergunta()

if __name__ == "__main__":
    janela = tk.Tk()
    app = JogoHistoria(janela)
    janela.mainloop()
