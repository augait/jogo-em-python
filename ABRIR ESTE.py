import pygame
import sys
import os
import tkinter as tk
from tkinter import PhotoImage


# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Configurações da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonte
font = pygame.font.Font(None, 36)

# Lista de itens do menu
menu_items = [
    "Jogo 1",
    "Jogo 2",
    "Sair"
]

# Diretório dos jogos
games_dir = "jogos"

music_channel = pygame.mixer.Channel(2)


def musica():
    pygame.mixer.music.load("musicbackground.mp3")
    music_channel.play(pygame.mixer.Sound("musicbackground.mp3"), loops=-1)


def efeito():
    pygame.mixer.music.load("select.mp3")
    pygame.mixer.music.play(loops=0)


musica()


# Função para desenhar o menu na tela
def draw_menu(selected_item):
    screen.fill(WHITE)
    for i, item in enumerate(menu_items):
        text = font.render(item, True, BLACK)
        text_rect = text.get_rect(center=(screen_width / 2, 200 + i * 50))
        screen.blit(text, text_rect)
        if i == selected_item:
            pygame.draw.rect(screen, BLACK,
                             (text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20), 2)


# Função principal
def main():
    selected_item = 0
    game_running = False  # Mova a declaração da variável para dentro da função

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                    efeito()
                elif event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                    efeito()
                elif event.key == pygame.K_RETURN:
                    if selected_item == len(menu_items) - 1:
                        efeito()
                        pygame.quit()
                        sys.exit()
                    else:
                        efeito()
                        game_file = os.path.join(games_dir, f"game{selected_item + 1}.py")
                        os.system(f"python {game_file}")
                        game_running = True

        if not game_running:
            draw_menu(selected_item)
            pygame.display.update()
        else:
            game_running = False


if __name__ == "__main__":
    main()

# Cria uma janela do tkinter para exibir a imagem de fundo
root = tk.Tk()
root.title("Menu com imagem de fundo")

# Carrega a imagem de fundo
background_image = PhotoImage(file="background.png")

# Cria um rótulo com a imagem de fundo
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Inicia a interface do tkinter
root.mainloop()
