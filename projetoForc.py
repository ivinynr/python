import pygame as pg
import random

# --- CORES DO JOGO ---
rosa = (255, 218, 185)
preto = (0, 0, 0)

# --- SETUP ---
pg.init()
window = pg.display.set_mode((1000, 600))

# fontes
pg.font.init()
font = pg.font.SysFont("courier New", 50)
font_rb = pg.font.SysFont("courier New", 30)

# --- VARIÁVEIS ---
palavras = ["CAVALO", "COELHO", "SAPO"]
tentativas_de_letras = ["", "-"]
palavra_escolhida = ""
palavra_camuflada = ""
end_game = True
chance = 0
letra = ""
click_last_status = False


# --- SISTEMA DE SOM ---
def som_do_jogo():
    pg.mixer.init()
    try:
        pg.mixer.music.load("som.mp3")
        pg.mixer.music.play(-1)  # loop infinito
    except:
        print("⚠️ Arquivo de som não encontrado.")


# --- DESENHOS DO JOGO ---
def desenho_da_forca(window, chance):
    pg.draw.rect(window, rosa, (0, 0, 1000, 600))
    pg.draw.line(window, preto, (100, 500), (100, 100), 10)
    pg.draw.line(window, preto, (50, 500), (150, 500), 10)
    pg.draw.line(window, preto, (100, 100), (300, 100), 10)
    pg.draw.line(window, preto, (300, 100), (300, 150), 10)
    if chance >= 1:
        pg.draw.circle(window, preto, (300, 200), 50, 10)
    if chance >= 2:
        pg.draw.line(window, preto, (300, 250), (300, 350), 10)
    if chance >= 3:
        pg.draw.line(window, preto, (300, 260), (225, 350), 10)
    if chance >= 4:
        pg.draw.line(window, preto, (300, 260), (375, 350), 10)
    if chance >= 5:
        pg.draw.line(window, preto, (300, 350), (375, 450), 10)
    if chance >= 6:
        pg.draw.line(window, preto, (300, 350), (225, 450), 10)


def desenho_proximo_button(window):
    pg.draw.rect(window, preto, (700, 100, 200, 65))
    texto = font_rb.render("PROXIMO", True, rosa)
    window.blit(texto, (740, 120))


# --- LÓGICA DO JOGO ---
def sorteando_palavra(palavras, palavra_escolhida, end_game):
    if end_game:
        palavra_escolhida = random.choice(palavras)
        end_game = False
    return palavra_escolhida, end_game


def camuflar_palavra(palavra_escolhida, palavra_camuflada, tentativas):
    palavra_camuflada = ""
    for letra in palavra_escolhida:
        if letra in tentativas:
            palavra_camuflada += letra
        else:
            palavra_camuflada += "#"
    return palavra_camuflada


def tentando_uma_letra(tentativas, palavra_escolhida, letra, chance):
    if letra not in tentativas:
        tentativas.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    return tentativas, chance


def palavra_do_jogo(window, palavra_camuflada):
    texto = font.render(palavra_camuflada, True, preto)
    window.blit(texto, (200, 500))


def proximo_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas, click_last_status, click, x, y):
    if "#" not in palavra_camuflada:  # venceu
        if click_last_status == False and click[0] == True:
            if 700 <= x <= 900 and y <= 165:
                tentativas = ["", "-"]
                end_game = True
                chance = 0
                letra = ""
    return end_game, chance, tentativas, letra


# --- INICIAR MÚSICA ---
som_do_jogo()

# --- LOOP PRINCIPAL ---
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = pg.key.name(event.key).upper()

    # mouse
    mouse_x, mouse_y = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # lógica do jogo
    desenho_da_forca(window, chance)
    desenho_proximo_button(window)

    palavra_escolhida, end_game = sorteando_palavra(palavras, palavra_escolhida, end_game)
    palavra_camuflada = camuflar_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras, chance = tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance)
    palavra_do_jogo(window, palavra_camuflada)

    end_game, chance, tentativas_de_letras, letra = proximo_do_jogo(
        palavra_camuflada,
        end_game,
        chance,
        letra,
        tentativas_de_letras,
        click_last_status,
        click,
        mouse_x,
        mouse_y,
    )

    # click status
    click_last_status = click[0]

    pg.display.update()
