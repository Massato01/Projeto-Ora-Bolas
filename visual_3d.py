# ====================================================
# ------------------  BIBLIOTECAS --------------------
from robo    import *
# from graficos import *
from vpython import *
from sympy   import *
# ====================================================

# ====================================================
#        ORIENTAÇÕES PARA INICIAR A ANIMAÇÃO
# ====================================================
scene.caption = f'''
<h1>ORA BOLAS!</h1>
<h2><strong>Precione qualquer tecla para iniciar a animação!</strong></h2>
<h3>Coordenadas escolhidas para a posição inicial do robô:
[  X: {x_robo}  ]
[  Y: {y_robo}  ]</h3>
'''


# ====----====----====----====----====----====----====
#             CRIANDO O CAMPO DE FUTEBOL
# ====----====----====----====----====----====----====
CAMPO = box(pos = vector(4.25, 2.5, 0), width = 0.05, length = 9, height = 6,
            texture = './assets/campo.jpg')

# Campo de teste
# CAMPO = box(pos = vector(0, 1, 0), width = 60, length = 1, height = 90,
#             texture = './assets/campo.jpg')


# ====----====----====----====----====----====----====
#                   CRIANDO OS GOLS
# ====----====----====----====----====----====----====
# Gol da direita
# GOL_DIREITA = box(pos = vector(40, 4.5, 0), color = color.white,
#           width = 10, lenght = 1, height = 7)

# # Gol da esquerda
# GOL_ESQUERDA = box(pos = vector(-40, 4.5, 0), color = color.white,
#           width = 10, lenght = 1, height = 7)


# ====----====----====----====----====----====----====
#                    CRIANDO A BOLA
# ====----====----====----====----====----====----====
BOLA = sphere(pos = vector(bola_x_pos[0], bola_y_pos[0], 0.07), color = color.red,
              radius = 0.05,
              make_trail = True, trail_color = color.white, interval = 1)


# ====----====----====----====----====----====----====
#                    CRIANDO O ROBÔ
# ====----====----====----====----====----====----====
# X = 4.25   Y = 2.5
# x_robo /= 10
# y_robo /= 10

ROBO_CORPO = cylinder(pos = vector(x_robo + 0.2, y_robo, 0.3),
                      color = color.yellow,
                      width = 0.25, length = 0.25, height = 0.25)

RODA_DIREITA = cylinder(pos=vector(x_robo + 0.2, y_robo - 0.13, 0.142),
                         color = color.white,
                         width = 0.225, length = 0.01, height = 0.225)

RODA_ESQUERDA = cylinder(pos=vector(x_robo + 0.2, y_robo + 0.13, 0.142),
                        color = color.white,
                        width = 0.225, length = 0.01, height = 0.225)

# NECESSÁRIO ROTACIONAR OS OBJETOS 3D
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

        # [ Enquanto o contador for menor q "bola_x_pos" e não sair das dimensões 
        #   do campo ]
        while cont_bola < len(bola_x_pos) and BOLA.pos.x - BOLA.radius > -CAMPO.length / 2:

            # FPS (Frames Por Segundo) da animação
            rate(120)
            
            # [ AS DIMENSÕES USADAS NO CAMPO FORAM APENAS X E Z ]
            BOLA.pos.x += (bola_x_pos[cont_bola]) - BOLA.pos.x
            BOLA.pos.y += (bola_y_pos[cont_bola]) - BOLA.pos.y
            
            cont_bola += 1
        
        # ENCERRA O LOOP INFINITO
        break