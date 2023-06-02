import pygame as pg
import random


# cores do jogo
rosa = (255, 218, 185)
preto = (0, 0, 0)

# setup da tela do jogo
window = pg.display.set_mode((1000, 600))

# iniciando fonte do jogo
pg.font.init()
# fonte e tamanho
font = pg.font.SysFont("courier New", 50)
font_rb = pg.font.SysFont("courier New", 30)


palavras = [
    "CAVALO",
    "COELHO",
    "SAPO",
]
tentativas_de_letras = ["", "-"]
palavra_escolhida = ""
palavra_camuflada = ""
end_game = True
chance = 0
letra = ""
click_last_status = False


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


def sorteando_palavra(palavras, palavra_escolhida, end_game):
    if end_game == True:
        palavra_n = random.randint(0, len(palavras) - 1)
        palavra_escolhida = palavras[palavra_n]
        end_game = False
    return palavra_escolhida, end_game


def camuflar_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n : n + 1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], "#")
    return palavra_camuflada


def tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras, chance


def palavra_do_jogo(window, palavra_camuflada):
    palavra = font.render(palavra_camuflada, True, preto)
    window.blit(palavra, (200, 500))


def proximo_do_jogo(
    palavra_camuflada,
    end_game,
    chance,
    letra,
    tentativas_de_letras,
    click_last_status,
    click,
    x,
    y,
):
    count = 0
    limit = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != "#":
            count += 1
    if count == limit and click_last_status == False and click[0] == True:
        if x >= 700 and x <= 900 and y <= 165:
            tentativas_de_letras = [" ", "-"]
            end_game = True
            chance = 0
            letra = " "
    return end_game, chance, tentativas_de_letras, letra


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()
            print(letra)

    # declarando variavel de posiçao do mouse
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # declarando variavel click do mouse
    click = pg.mouse.get_pressed()

    # jogo
    desenho_da_forca(window, chance)
    desenho_proximo_button(window)
    palavra_escolhida, end_game = sorteando_palavra(
        palavras, palavra_escolhida, end_game
    )
    palavra_camuflada = camuflar_palavra(
        palavra_escolhida, palavra_camuflada, tentativas_de_letras
    )
    tentativas_de_letras, chance = tentando_uma_letra(
        tentativas_de_letras, palavra_escolhida, letra, chance
    )
    palavra_do_jogo(window, palavra_camuflada)
    end_game, chance, tentativas_de_letras, letra = proximo_do_jogo(
        palavra_camuflada,
        end_game,
        chance,
        letra,
        tentativas_de_letras,
        click_last_status,
        click,
        mouse_position_x,
        mouse_position_y,
    )
    som_do_jogo(palavra_escolhida, chance)
    # click last status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()
