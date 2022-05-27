# ====================================================
# ------------------  BIBLIOTECAS --------------------
from robo     import * 
from graficos import *
from vpython  import *
from sympy    import *
# ====================================================

# Listas para o momento de interceptação
intercepto_xRobo = []
intercepto_yRobo = []
intercepto_tRobo = []
distancia_robo_bola = [] # NÃO É A FUNÇÃO "dist_robo_bola()"


# ====================================================
#        ORIENTAÇÕES PARA INICIAR A ANIMAÇÃO
# ====================================================
scene = canvas(width = 800, height = 600)

scene.caption = f'''
<h1 style="text-align:center">ORA BOLAS!</h1>
<h3 style="text-align:center"><strong>Precione qualquer tecla para iniciar a animação!</strong>\n
Coordenadas escolhidas para a posição inicial do robô:
[  X: {x_robo}  ]
[  Y: {y_robo}  ]</h3>
'''


# BOLA DE REFERENCIA DOS PONTOS (0, 0)
# bola_referencia = sphere(pos = vector(0, 0, 0), radius = 0.1)

# ====----====----====----====----====----====----====
#             CRIANDO O CAMPO DE FUTEBOL
# ====----====----====----====----====----====----====
CAMPO = box(pos = vector(4.5, 3, 0), width = 0.05, length = 10, height = 7.2,
            texture = './assets/campo.jpg')

# -------------------------------------------
# CENTRALIZANDO A CAMERA COM RELAÇÃO AO CAMPO
scene.camera.follow(CAMPO)
# -------------------------------------------

# Campo de teste [ IGNORAR ]
# CAMPO = box(pos = vector(0, 1, 0), width = 60, length = 1, height = 90,
#             texture = './assets/campo.jpg')


# ====----====----====----====----====----====----====
#                   CRIANDO OS GOLS
# ====----====----====----====----====----====----====
# Gol da direita
GOL_DIREITA = box(pos = vector(8.95, 3, 0.26), color = color.white,
          width = 0.5, length = 1.24, height = 0.1)

# Gol da esquerda
GOL_ESQUERDA = box(pos = vector(0.05, 3, 0.26), color = color.white,
          width = 0.5, length = 1.24, height = 0.1)


# ====----====----====----====----====----====----====
#                    CRIANDO A BOLA
# ====----====----====----====----====----====----====
# raio da bola = 0.05
BOLA = sphere(pos = vector(bola_x_pos[0], bola_y_pos[0], 0.07), color = color.white,
              radius = 0.1,
              make_trail = True, trail_color = color.white, interval = 1,
              texture = './assets/dain.jpg')


# ====----====----====----====----====----====----====
#                    CRIANDO O ROBÔ
# ====----====----====----====----====----====----====
ROBO_CORPO = cylinder(pos = vector(x_robo, y_robo, 0.3),
                      color = color.black,
                      width = 0.35, length = 0.35, height = 0.35,
                      make_trail = True, trail_color = color.cyan,
                      interval = 1)

RODA_DIREITA = cylinder(pos=vector(x_robo, y_robo - 0.13, 0.142),
                         color = color.white,
                         width = 0.225, length = 0.01, height = 0.225)

RODA_ESQUERDA = cylinder(pos=vector(x_robo, y_robo + 0.13, 0.142),
                        color = color.white,
                        width = 0.225, length = 0.01, height = 0.225)


# NECESSÁRIO ROTACIONAR OS OBJETOS 3D
GOL_DIREITA.rotate(angle = 3.14 / 2, axis = vector(0, 0, 1))
GOL_ESQUERDA.rotate(angle = 3.14 / 2, axis = vector(0, 0, 1))

ROBO_CORPO.rotate(angle = 3.14 / 2, axis = vector(0, 1, 0))
RODA_DIREITA.rotate(angle = 3.14 / 2, axis = vector(0, 0, 1))
RODA_ESQUERDA.rotate(angle = 3.14 / 2, axis = vector(0, 0, 1))


while True:
    # Espera até q o usuário pressione alguma tecla
    comando = scene.waitfor('keydown')

    # [ SE ALGUMA TECLA FOR PRESSIONADA... ]
    if comando.event == 'keydown':
        
        # Contador para as coordenadas da bola
        cont_bola = 0

        # Contador para as coordenadas do robô
        cont_robo = 0

        # [ Enquanto o contador for menor q "bola_x_pos" e não sair das dimensões 
        #   do campo ]
        while cont_bola < len(bola_x_pos) and BOLA.pos.x - BOLA.radius > -CAMPO.length / 2:

            # FPS (Frames Por Segundo) da animação
            rate(120)
            
            # --------------------
            # MOVIMENTAÇÃO DA BOLA
            # --------------------
            BOLA.pos.x += (bola_x_pos[cont_bola]) - BOLA.pos.x
            BOLA.pos.y += (bola_y_pos[cont_bola]) - BOLA.pos.y
            
            cont_bola += 1

            # --------------------
            # MOVIMENTAÇÃO DO ROBÔ
            # --------------------
            if cont_robo < len(lista_xRobo):
                # Movimentação do corpo do robô
                ROBO_CORPO.pos.x = lista_xRobo[cont_robo]
                ROBO_CORPO.pos.y = lista_yRobo[cont_robo]

                # Movimentação das rodas do robô
                RODA_DIREITA.pos.x = lista_xRobo[cont_robo]
                RODA_DIREITA.pos.y = lista_yRobo[cont_robo] + ROBO_CORPO.height-0.12

                RODA_ESQUERDA.pos.x = lista_xRobo[cont_robo]
                RODA_ESQUERDA.pos.y = lista_yRobo[cont_robo] - ROBO_CORPO.height+0.12

                cont_robo += 1
            # -----------------------------------------
            # MOMENTO DA INTERCEPTAÇÃO DO ROBÔ E A BOLA
            # -----------------------------------------
            # if (BOLA.pos.x > ROBO_CORPO.pos.x - (ROBO_CORPO.height-0.15) and
            #     BOLA.pos.y >= (ROBO_CORPO.height-0.15)):
            if (BOLA.pos.x > ROBO_CORPO.pos.x - (ROBO_CORPO.height-0.15) and
                BOLA.pos.y >= ROBO_CORPO.pos.y - (ROBO_CORPO.length-0.15)):
                
                if intercepto == True:
                    intercepto_xRobo.append(ROBO_CORPO.pos.x)
                    intercepto_yRobo.append(ROBO_CORPO.pos.y)
                    intercepto_tRobo.append(bola_t_pos[cont_bola])

                    distancia_robo_bola.append(dist_robo_bola(
                        ROBO_CORPO.pos.x - ROBO_CORPO.width / 10,
                        ROBO_CORPO.pos.y,
                        BOLA.pos.x,
                        BOLA.pos.y
                    ))

                    scene.append_to_caption(
                        f'''<h2 style="border:2px solid black; text-align:center">INTERCEPTOU!\nPonto X da interceptação: {menor_distX:.2f}\nPonto Y da interceptação: {menor_distY:.2f}\nPonto T da interceptação: {menor_distT:.2f}</h2>'''
                    )
                
                else:
                    scene.append_to_caption(
                        f'''<h2 style="border:2px solid black; text-align:center">O Robô não conseguiu interceptar...'''
                    )

                break
            
            if BOLA.pos.x <= 6 and BOLA.pos.y <= 9:
                distancia_robo_bola.append(dist_robo_bola(
                    ROBO_CORPO.pos.x,
                    ROBO_CORPO.pos.y,
                    BOLA.pos.x,
                    BOLA.pos.y
                ))

                intercepto_xRobo.append(ROBO_CORPO.pos.x)
                intercepto_yRobo.append(ROBO_CORPO.pos.y)
                intercepto_tRobo.append(bola_t_pos[cont_bola])

        # ENCERRA O LOOP INFINITO
        break