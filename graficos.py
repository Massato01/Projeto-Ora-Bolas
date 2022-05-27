# ==================================================
# ------------------ BIBLIOTECAS -------------------
import dash
import pandas             as pd
import matplotlib.pyplot  as plt
import matplotlib.patches as mpatches
import plotly.express     as px
import plotly.graph_objs  as go
from   math               import *
from   sympy              import *
from   sympy              import symbols
from   dash               import dcc, html
from   dash.dependencies  import Input, Output
# ==================================================


# ==================================================
# --------------- VARIÁVEIS GLOBAIS ----------------
bola_x_pos = None
bola_y_pos = None
bola_t_pos = None
# ==================================================


# ==================================================
# -------------------- FUNÇÕES ---------------------
def criar_listas_posicao():
    '''
    ==================================
    CRIA LISTAS PARA AS COORDENADAS DA
           TRAJETÓRIA DA BOLA
    ==================================
    '''

    global bola_x_pos, bola_y_pos, bola_t_pos

    trajetoria = pd.read_csv('./data/trajetoria-bola.csv')

    trajetoria = trajetoria.replace(',', '.', regex = True).astype(float)

    bola_x_pos = trajetoria.iloc[:, 1].values
    bola_y_pos = trajetoria.iloc[:, 2].values
    bola_t_pos = trajetoria.iloc[:, 0].values

    # print(bola_x_pos)
    # print(bola_y_pos)
    # print(bola_t_pos)


def plotar_grafico(titulo='Title', x=None, y=None, xlabel='x', ylabel='y'):
    '''
    ============================================
          PLOTA UM GRÁFICO COM MATPLOTLIB
    ============================================
    titulo: título do gráfico
    x: valores do eixo X
    y: valores do eixo Y
    xlabel: titulo do eixo X
    ylabel: titulo do eixo Y

    return -> gráfico de acordo com parâmetros
              passados
    '''
    plt.plot(x, y)     # -> plota o gráfico
    plt.title(titulo)  # -> título 
    plt.xlabel(xlabel) # -> título do eixo X
    plt.ylabel(ylabel) # -> título do eixo X
    plt.grid()         # -> linhas de grade
    
    plt.show()


def plotar_grafico_plotly(titulo='Title', x=None, y=None, xlabel='x', ylabel='y'):
    '''
    ============================================
            PLOTA UM GRÁFICO COM PLOTLY
    ============================================
    titulo: título do gráfico
    x: valores do eixo X
    y: valores do eixo Y
    xlabel: titulo do eixo X
    ylabel: titulo do eixo Y

    return -> gráfico de acordo com parâmetros
              passados
    '''
    fig = px.line(x = x, y = y, title = titulo)

    return fig.show()


def plot_duplo(titulo1='Title', x1=None, y1=None, xlabel1='x', ylabel1='y', legenda1='legenda1',
               titulo2='Title', x2=None, y2=None, xlabel2='x', ylabel2='y', legenda2='legenda2'):
    
    # Tamanho da area dos graficos
    plt.figure(figsize=(7, 5))

    # Area do primeiro grafico
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, color = 'royalblue')
    plt.title(titulo1)
    plt.xlabel(xlabel1)
    plt.ylabel(ylabel1)
    blue_patch = mpatches.Patch(color = 'royalblue', label = legenda1)
    plt.legend(handles = [blue_patch])
    plt.grid()

    # Area do segundo grafico
    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, color = 'purple')
    plt.title(titulo2)
    plt.xlabel(xlabel2)
    plt.ylabel(ylabel2)
    purple_patch = mpatches.Patch(color = 'purple', label = legenda2)
    plt.legend(handles = [purple_patch])
    plt.grid()

    plt.tight_layout()
    plt.show()
    

def plotar_trajetoria_intercepto(xB, yB, xR, yR, tempo_dist, intercepto):
    '''
    ==================================
    PLOTA A TRAJETÓRIA DO ROBÔ À BOLA
     ATÉ O INSTANTE DE INTERCEPTAÇÃO
    ==================================
    xB: coordenadas de X do robô
    yB: coordenadas de Y do robô
    xR: coordenadas de X do robô (de acordo com a menor distância até a interceptação)
    xR: coordenadas de Y do robô (de acordo com a menor distância até a interceptação)
    tempo_dist: tempo da distância até o momento de interceptação
    intercepto: intercepto (True / False)

    return -> gráfico da trajetória
    '''


    # [ GRÁFICO DA INTERCEPTAÇÃO DO ROBÔ ]
    if intercepto == True:
        
        bolaX_intercepto = []
        bolaY_intercepto = []

        # Armazenando as coordenadas até o instante de interceptação
        index = 0
        while (bola_t_pos[index] <= tempo_dist):
            bolaX_intercepto.append(bola_x_pos[index])
            bolaY_intercepto.append(bola_y_pos[index])

            index += 1
        
        # print(f'{bolaX_intercepto = }\n{bolaY_intercepto = }')

        # Plotando o gráfico da interceptação
        plt.plot(xR, yR, color = 'royalblue')
        plt.plot(bolaX_intercepto, bolaY_intercepto, color = 'red')
        plt.title('Trajetória do Robô à Bola até a INTERCEPTAÇÃO')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(0, 9) # -> limite inicial e final do eixo X
        plt.ylim(0, 6) # -> limite inicial e final do eixo Y
        plt.grid()

        blue_patch = mpatches.Patch(color = 'royalblue', label = 'Trajetória do Robô')
        red_patch = mpatches.Patch(color = 'red', label = 'Trajetória da Bola')
        plt.legend(handles = [red_patch, blue_patch])

        plt.show()

    # [ GRÁFICO DA NÃO INTERCEPTAÇÃO DO ROBÕ ]
    else:
        # plotando o gráfico da NÃO interceptação
        plt.plot(xR, yR, color = 'royalblue')
        plt.plot(xB, yB, color = 'red')
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.xlim(0, 9)
        plt.ylim(0, 6)
        plt.grid()

        blue_patch = mpatches.Patch(color = 'royalblue', label = 'Trajetória do Robô')
        red_patch = mpatches.Patch(color = 'red', label = 'Trajetória da Bola')
        plt.legend(handles = [red_patch, blue_patch])

        plt.show()


# Declarando as variáveis simbólicas para derivada
t, s = symbols('t s')
def plotar_vxvy_axay(titulo, derivadaX, derivadaY, componente_va):
    '''
    ==================================
           PLOTA VX/VY E AX/AY
    ==================================
    titulo: titulo do grafico
    derivadaX: derivada da equação de X
    derivadaY: derivada da equação de Y
    componente_va: componente da velodidade(V) ou aceleração(A)

    return -> um plot duplot com VX/VY e AX/AY
    '''
    componente_x = []
    componente_y = []

    for i in range(len(bola_t_pos)):
        # Encontrando a velocidade/aceleração instantânea
        coef_ang_x = derivadaX.subs(t, bola_t_pos[i])

        # Encontrando a velocidade/aceleração instantânea
        coef_ang_y = derivadaY.subs(t, bola_t_pos[i])

        componente_x.append(coef_ang_x)
        componente_y.append(coef_ang_y)
    
    plot_duplo(
        # Plotando VX/VY da bola em função do tempo
        f'{componente_va}x(t) {titulo}', bola_t_pos, componente_x, 's', 'm/s' if componente_va == 'V' else 'm/s²', f'{componente_va}x(t)',
        
        # Plotando AX/AY da bola em função do tempo
        f'{componente_va}y(t) {titulo}', bola_t_pos, componente_y, 's', 'm/s' if componente_va == 'V' else 'm/s²', f'{componente_va}y(t)'
        )
        
# ==================================================


# Criando listas com as posicoes da bola
criar_listas_posicao()
print(bola_x_pos[0])
print(bola_x_pos[::-1][0] - bola_x_pos[0] / bola_t_pos[::-1][0] - bola_t_pos[1])


# ==================================================
#      TESTES PRO PAJÉ E PEDRO N SE PERDEREM
# ==================================================

# # Plotando um grafico UNICO
# plotar_grafico('Plot Unico', bola_x_pos, bola_y_pos)

# # Plotando dois graficos
# plot_duplo('Plot Duplo 1', bola_x_pos, bola_y_pos, 'x', 'y', 'legenda1',
#            'Plot Duplo 2', bola_x_pos, bola_y_pos, 'x', 'y', 'legenda2')

# # # Plotando interceptacao (NO GRAFICO N TEM A INTERCEPTACAO, EH SOH UM EXEMPLO)
# xbola_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ybola_teste = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]

# xRobo_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# yRobo_teste = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]

# tempo_distT = 7.75

# intercepto = True

# plotar_trajetoria_intercepto(xbola_teste, ybola_teste, xRobo_teste, yRobo_teste, tempo_distT, intercepto)


# # Plotando VX/VY e AX/AY

# # Deriva uma vez = VELOCIDADE
# x1 = diff(-0.008 * t ** 3 - 0.15 * t ** 2 + 2.5 * t + 1, t)
# y1 = diff( -0.2*t**1.5 + 1.6*t + 1,t)

# # Deriva duas vezes = ACELERACAO
# x2 = diff(diff( -0.008*t**3 - 0.15*t**2 + 2.5*t + 1,t),t)
# y2 = diff(diff( -0.2*t**1.5 + 1.6*t + 1,t),t)

# # Velocidade instantanea
# plotar_vxvy_axay('Plot', x1, y1, 'V')

# # Aceleracao instantanea
# plotar_vxvy_axay('Plot', x2, y2, 'A')
