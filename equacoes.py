# ==================================================
# ------------------ BIBLIOTECAS -------------------
import math
from   plot_graficos     import *
from   sympy             import *
from   numpy             import ones, vstack
from   numpy.linalg      import lstsq
# ==================================================


# ==================================================
#   CÁLCULOS:
#      - DISTÂNCIA ENTRE O ROBÔ E A BOLA
#      - TEMPO DA TRAJETÓRIA DO ROBÔ À BOLA
#      - EQUAÇÃO DA RETA
# ==================================================


# ==================================================
# --------------- VARIÁVEIS GLOBAIS ----------------
# Bola
x_bola = []
y_bola = []

# Robo
x_robo = 0
y_robo = 0
velocidade_robo = []
aceleracao_robo = []
lista_xRobo = []
lista_yRobo = []
lista_tempo = []
vx_robo = []
vy_robo = []
ax_robo = []
ay_robo = []

# Robo/Bola
menor_distX = 0
menor_distY = 0
menor_distT = 0
m = b = 0


intercepto = False
# ==================================================


# ==================================================
# -------------------- FUNÇÕES ---------------------
# ==================================================
def dist_robo_bola(xR, yR, xB, yB):
    '''
    =========================================
    CALCULA A DISTÂNCIA ENTRE O ROBÔ E A BOLA
    =========================================
    
    xR: posição X do robô
    yR: posição Y do robô
    xB: posição X da bola
    yB: posição Y da bola

    return -> fórmula da distância (pitágoras)
    '''
    return math.sqrt( (xB-xR)**2 + (yB-yR)**2 )


def tempo_robo_bola(distancia, velocidade):
    '''
    ============================================
    CALCULA O TEMPO DA TRAJETÓRIA DO ROBÔ À BOLA
    ============================================

    distancia: distância entre o robô e a bola
    velocidade: velocidade do robô

    return -> trajetória do robô à bola em função do tempo
    '''
    tempo = distancia / velocidade

    return tempo


def equacao_da_reta(pos_inicial_robo, pos_final_robo, x_robo, y_robo,
             menor_distX, menor_distY, menor_distT,
             velocidade_robo, aceleracao_robo, lista_tempo):
    '''
    ==========================
    ENCONTRA A EQUAÇÃO DA RETA
    ==========================

    pos_inicial_robo: posição incial do robô [x, y]
    pos_final_robo: posição final do robô [x, y]
    x_robo: ponto X do robô
    y_robo: ponto Y do robô
    menor_distX: menor distância entre o robô e a bola em X
    menor_distY: menor distância entre o robô e a bola em Y
    menor_distT: tempo da distância entre o robô e a bola
    velocidade_robo: velocidade do robô
    aceleracao_robo: aceleracao do robô
    lista_tempo: lista com o tempo armazenado

    return -> equação da reta que o robô percorrerá para interceptar a bola
    '''
    # Coeficientes Angular e Linear
    global m, b

    # Listas para armazenar as posições em X e Y do robô
    global lista_xRobo, lista_yRobo

    # VX/VY  &  AX/AY do robo
    global vx_robo, vy_robo, ax_robo, ay_robo


    # Pega os pontos X e Y da posição inicial e final
    pontos = [ (pos_inicial_robo[0], pos_inicial_robo[1]),
               (pos_final_robo[0], pos_final_robo[1]) ]
    
    # ====----====----====----====----====----====----====----====----====
    #   Encontrando a equação da reta da trajetória do robô em um plano
    # ====----====----====----====----====----====----====----====----====

    # link documentação vstack: https://numpy.org/doc/stable/reference/generated/numpy.vstack.html
    x_coords, y_coords = zip(*pontos)

    A = vstack([x_coords, ones(len(x_coords))]).T
    m, b = lstsq(A, y_coords, rcond=-1)[0]

    # --------------------------------------
    #    Visualizando a Equação da Reta
    # --------------------------------------
    print(f'Equação da Reta = {m}x + {b}')


    # ====----====----====----====----====----====----====----====
    #    [ Encontra as componentes VX/VY e AX/AY do robô ]
    # ====----====----====----====----====----====----====----====

    # Cálculo da direção:
    #     tan(teta) = Ry / Rx
    #     TETA = arctan(tan(teta))
    #
    #  -> [ Coeficiente Angular = tan(teta) -> "m". ]
    #     
    #     teta = arco tan(m)

    # Calculando VX/VY e AX/AY e armazenando nas listas acima
    for index in range(len(velocidade_robo)):
        teta = atan(m)
        
        # vx = v0 * cos(teta)          vy = v0 * sen(teta)
        vx_robo.append(velocidade_robo[index] * cos(teta))
        vy_robo.append(velocidade_robo[index] * sin(teta))

        # ax = a0 * cos(teta)          ay = a0 * sen(teta)
        ax_robo.append(aceleracao_robo[index] * cos(teta))
        ay_robo.append(aceleracao_robo[index] * sin(teta))
        # print(teta)
    
    
    # ====----====----====----====----====----====
    # [ Armazenando as coordenadas X e Y do robô ]
    # ====----====----====----====----====----====
    #  Cria-se uma lista para cada posição, X e Y, que serão utilizados no vPython (IGNORAR EM C)
    
    # [ Variável temporária para não interfirir na variável da função ] 
    pos_inicial_xRobo_temp = x_robo

    i = 0

    if pos_inicial_xRobo_temp < menor_distX:
        while pos_inicial_xRobo_temp < menor_distX:
            lista_xRobo.append(pos_inicial_xRobo_temp)
            lista_yRobo.append(m * pos_inicial_xRobo_temp + b)
            
            if i < len(vx_robo):
                # Incrementa a posição do robô de acordo com o VX encontrado
                pos_inicial_xRobo_temp += vx_robo[i] * 0.02

            else:
                pos_inicial_xRobo_temp += vx_robo[len(velocidade_robo) - 1] * 0.02
            
            i += 1
    
    else:
        while pos_inicial_xRobo_temp > menor_distX:
            lista_xRobo.append(pos_inicial_xRobo_temp)
            lista_yRobo.append(m * pos_inicial_xRobo_temp + b)
            
            if i < len(vx_robo):
                pos_inicial_xRobo_temp -= vx_robo[i] * 0.02

            else:
                # Decrementa a posição do robô de acordo com o VX encontrado
                pos_inicial_xRobo_temp -= vx_robo[len(vx_robo) - 1] * 0.02
            i += 1

        for i in range(len(vx_robo)):
            vx_robo[i] *= -1
            vy_robo[i] *= -1
            ax_robo[i] *= -1
            ay_robo[i] *= -1
# ==================================================