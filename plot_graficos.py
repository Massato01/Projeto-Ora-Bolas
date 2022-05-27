# ==================================================
# ------------------ BIBLIOTECAS -------------------
import pandas             as pd
import matplotlib.pyplot  as plt
import matplotlib.patches as mpatches
import plotly.express     as px
from   math               import *
from   sympy              import *
from   sympy              import symbols
from   logica_robo        import *
# ==================================================

# ==================================================
# -------------------- FUNÇÕES ---------------------
# def criar_listas_posicao():
#     '''
#     ==================================
#     CRIA LISTAS PARA AS COORDENADAS DA
#            TRAJETÓRIA DA BOLA
#     ==================================
#     '''

#     global bola_x_pos, bola_y_pos, bola_t_pos

#     trajetoria = pd.read_csv('./data/trajetoria-bola.csv')

#     trajetoria = trajetoria.replace(',', '.', regex = True).astype(float)

#     bola_x_pos = trajetoria.iloc[:, 1].values
#     bola_y_pos = trajetoria.iloc[:, 2].values
#     bola_t_pos = trajetoria.iloc[:, 0].values

#     # print(bola_x_pos)
#     # print(bola_y_pos)
#     # print(bola_t_pos)


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
    global bola_t_pos
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
