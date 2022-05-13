# ==================================================
# ------------------ BIBLIOTECAS -------------------
import math
import tkinter           as tk
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt
from   graficos        import *
from   tkinter           import messagebox
from   sympy             import *
from   numpy             import append, ones, vstack
from   numpy.linalg      import lstsq
# ==================================================


# ==================================================
# ----- VARIÁVEIS GLOBAIS -----
y_bola = x_bola = x_robo = y_robo = menor_distX = menor_distY = menor_distT = 0
m = c = 0
lista_xRobo = []
lista_yRobo = []
arr_t_aux = []
velocidade_robo = []
aceleracao_robo = []
vx_robo = []
ax_robo = []
vy_robo = []
ay_robo = []

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
    return math.sqrt( (xB - xR)**2 + (yB - yR)**2 )


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


def equacao_da_reta(pos_inicial_robo, pos_final_robo,
                    x_robo, y_robo,
                    menor_distX, menor_distY, menor_distT,
                    velocidade_robo, aceleracao_robo,
                    arr_t_aux):
    '''
    ==========================
    ENCONTRA A EQUAÇÃO DA RETA
    ==========================

    pos_inicial_robo: posição incial do robô
    pos_final_robo: posição final do robô
    xRobo: ponto X do robô
    yRobo: ponto Y do robô
    menor_distanciaX: menor distância entre o robô e a bola em X
    menor_distanciaY: menor distância entre o robô e a bola em Y
    menor_distanciaT: tempo da distância entre o robô e a bola
    velocidade_robo: velocidade do robô
    aceleracao_robo: aceleracao do robô
    arr_t_aux: ?

    return -> equação da reta que o robô percorrerá para interceptar a bola
    '''
    # Coeficientes Angular e Linear
    global m, c

    # Listas para armazenar as posições em X e Y do robô
    global lista_xRobo, lista_yRobo, vx_robo, vy_robo, ax_robo, ay_robo
    

    # Encontra a equação da reta da trajetória do robô em um plano
    pontos = [ (pos_inicial_robo[0], pos_inicial_robo[1]),
               (pos_final_robo[0],   pos_final_robo[1]) ]
    
    # link documentação vstack: https://numpy.org/doc/stable/reference/generated/numpy.vstack.html
    x_coords, y_coords = zip(*pontos)

    A_vstack = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A_vstack, y_coords, rcond = -1)[0]

    # print(f'Equação da Reta = {m}x + {c}')


    # Variável temporária para armazenar a posição incial do robô em X
    pos_inicial_xRobo_temp = x_robo


    # ====----====----====----====----====----====----====----====
    #    [ Encontra as componentes VX e AX, e VY e AY do robô ]
    # ====----====----====----====----====----====----====----====
    # Variáveis globais
    # vx_robo = []
    # ax_robo = []
    # vy_robo = []
    # ay_robo = []

    x = Symbol('x')

    # Derivada da posição da bola
    dx_pos_bola = diff(m * x + c, x)

    for index in range(len(velocidade_robo)):
        teta = atan(dx_pos_bola)
        
        # vx = v * cos(teta)            ax = a * cos(teta)
        vx_robo.append(velocidade_robo[index] * cos(teta))
        ax_robo.append(aceleracao_robo[index] * cos(teta))

        # vy = v * sen(teta)            ay = a * sen(teta)
        vy_robo.append(velocidade_robo[index] * sin(teta))
        ay_robo.append(aceleracao_robo[index] * sin(teta))
    
    # Novamente armazenando posição inicial do robô X em uma variável temporária
    pos_inicial_xRobo_temp = x_robo


    # ====----====----====----====----====----====
    #  [ Encontra as coordenadas X e Y do robô ]
    # ====----====----====----====----====----====
    #  Laço utilizado para capturar os valores de x e y (utilizando a equação encontrada)
    #  Cria-se uma lista para cada posição, X e Y, que serão utilizados no vPython

    cont = 0
    constante = 0

    constante = 0.02 if intercepto == 1 else 0.016

    if pos_inicial_xRobo_temp < menor_distX:
        while pos_inicial_xRobo_temp < menor_distX:
            lista_xRobo.append(pos_inicial_xRobo_temp)
            lista_yRobo.append(m * pos_inicial_xRobo_temp + c)

            if cont < len(vx_robo):
                # Incrementa a posição do robô de acordo com o VX encontrado
                pos_inicial_xRobo_temp += vx_robo[cont] * constante
            else:
                pos_inicial_xRobo_temp += vx_robo[len(velocidade_robo) - 1] * constante
            
            cont += 1
    
    else:
        while pos_inicial_xRobo_temp > menor_distX:
            lista_xRobo.append(pos_inicial_xRobo_temp)
            lista_yRobo.append(m * pos_inicial_xRobo_temp + c)

            if cont < len(vx_robo):
                pos_inicial_xRobo_temp -= vx_robo[cont] * constante
            else:
                # Decrementa a posição do robô de acordo com o VX encontrado
                pos_inicial_xRobo_temp -= vx_robo[len(velocidade_robo) - 1] * constante
            
            cont += 1
        
        for index in range(len(vx_robo)):
            vx_robo[index] *= -1
            vy_robo[index] *= -1
            ax_robo[index] *= -1
            ay_robo[index] *= -1
            




# ==================================================



# ====----====----====----====----====
#    [ COORDENADAS PARA O ROBÔ ]
# ====----====----====----====----====

# listas das coordenadas da bola
lista_xBola = []
lista_yBola = []


def inicializa_janela_coordenadas():
    '''
    ============================================================
    INICIALIZA UMA JANELA DE ENTRADA PARA AS COORDENADAS DO ROBÔ
    ============================================================
    '''

    # ==========================================================
    # ---------------- BASE DA JANELA PRINCIPAL ----------------
    # ==========================================================
    master = tk.Tk()
    master.geometry('450x100')
    master.title('Posição inicial do Robô')
    master.configure(bg = '#FAFBFF')

    # Cria as LABELS para que o usuário digite as coordenadas
    xLabel_coord = tk.Label(master, text="Digite a coordenada X do Robô:")
    yLabel_coord = tk.Label(master, text="Digite a coordenada Y do Robô:")

    xLabel_coord.place(relx=0.3, rely=0.15, anchor='center')
    yLabel_coord.place(relx=0.3, rely=0.38, anchor='center')

    xLabel_coord.configure(font=('Helvetica', 12, 'normal'), bg='#FAFBFF', fg='#2d2e30')
    yLabel_coord.configure(font=('Helvetica', 12, 'normal'), bg='#FAFBFF', fg='#2d2e30')

    # Cria duas caixas de diálogo, uma para cada coordenada
    xRobo_input = tk.Entry(master)
    yRobo_input = tk.Entry(master)

    # Separa os campos de entrada de X e de Y
    xRobo_input.place(relx=0.78, rely=0.15, anchor='center')
    yRobo_input.place(relx=0.78, rely=0.38, anchor='center')

    xRobo_input.configure(bg='white', fg='#2d2e30', font=('Helvetica', 10, 'bold'))
    yRobo_input.configure(bg='white', fg='#2d2e30', font=('Helvetica', 10, 'bold'))
    # ==========================================================



    def enviar_coordenadas():
        '''
        ============================================
        ENVIA AS COORDENADAS FORNECIDAS PELO USUÁRIO
        ============================================
        '''
        # Variáveis globais definidas no inicio do código
        global x_bola, y_bola, x_robo, y_robo, velocidade_robo, aceleracao_robo, menor_distX, menor_distT, intercepto, arr_t_aux

        # Verifica se as caixas de diálogo esão vazias
        if xRobo_input.get() == '' and yRobo_input.get() == '':
            messagebox.showinfo('Alerta!', 'Preencha TODOS os campos, por favor!')
        
        else:
            # Valores de X e Y inseridos
            x_robo = float(xRobo_input.get())
            y_robo = float(yRobo_input.get())

            # Verifica se as coordenadas digitadas estão dentro do limite das dimensões do campo (9.0 x 6.0)
            if x_robo < 0.0 or x_robo > 9.0 or y_robo < 0.0 or y_robo > 6.0:
                messagebox.showinfo('Alerta!',
                                    'Valores inválidos!\n'
                                    'Verifique se as coordenadas estão dentro das dimensões do campo.')
            
            # [ ! O robô não pode ter a mesma posição inicial que a bola ! ]
            elif x_robo == 1.0 and y_robo == 0.5:
                messagebox.showinfo('Alerta!',
                                    'O robô não pode ter a mesma posição inicial que a bola. \n'
                                    'Digite outras coordenadas, por favor!')
            
            # [ COORDENADAS ENVIADAS ]
            else:
                messagebox.showinfo('',
                                    'Coordenadas enviadas com SUCESSO! \n\n'
                                    f'X = {x_robo}\nY = {y_robo}\n\n'
                                    f'({x_robo}, {y_robo})')

                
                # ====----====----====----====----====----====
                #    [ VERIFICANDO SE HOUVE INTERCEPTAÇÃO ]
                # ====----====----====----====----====----====

                # RAIO DE INTERCEPTAÇÃO = ? (para exemplo usarei 0.12)
                raio = 0.12

                # [ ! VELOCIDADE DO ROBÔ ! --> INTEGRAL DA ACELERAÇÃO (4m/s²) ]
                # Declara as variáveis de posição e tempo como simbólicas
                var_posicao, var_tempo = symbols('s t')

                velocidade = integrate(4, var_tempo)

                # ================================================================
                # Calculando o instante em que o robô atinge sua velocidade máxima
                # ================================================================
                # [ Ponto em que ele passa a se movimentar com velocidade constante ]
                # [ VELOCIDADE MÁXIMA --> 2.3m/s ]
                # Igualando a velocidade máxima à equação da velocidade para calcularmos o instante
                instante_vel_max = solve(velocidade - 2.3, var_tempo)

                instante_vel_max = instante_vel_max[0]
                # print(instante_vel_max)

                
                # ==========================================================
                # Descobrindo a distância percorrida até a velocidade máxima
                # ==========================================================
                # [ Temos que integrar a equação da velocidade com os limites de integração de 0s até instante_vel_max(0.6)s ]
                s_instante_vel_max = integrate(velocidade,
                                               (var_tempo, 0, instante_vel_max))

                # Distância máxima do robô em campo
                distancia_maxima = 10.816653826391969

                for i in range(len(lista_x_pos)):
                    # ========================================================
                    # Distância do robô até a bola em cada ponto da trajetória
                    # ========================================================
                    if lista_x_pos[i] >= 0.0 and lista_x_pos[i] <= 9.0 and lista_y_pos[i] >= 0.0 and lista_y_pos[i] <= 6.0:
                        distancia_total = (dist_robo_bola(x_robo,
                                                          y_robo,
                                                          lista_x_pos[i],
                                                          lista_y_pos[i])) - raio

                        # Armazenando as coordenadas da bola enquanto estiver em campo
                        lista_xBola.append(lista_x_pos[i])
                        lista_yBola.append(lista_y_pos[i])

                        # Armazenando a mínima distância possível e o tempo levado pelo robô para percorre-la
                        if distancia_total < distancia_maxima:
                            distancia_maxima = distancia_total
                            menor_distX = lista_x_pos[i]
                            menor_distY = lista_y_pos[i]
                            menor_distT = lista_t_pos[i]


                        # ====================================================
                        # Descobrindo o tempo que o robô leva para completar a   
                        # trajetória em que possui velocidade constante
                        # ====================================================

                        # [ SUBTRAIR A MENOR DISÂNCIA ENCONTRADA PELA DISTÂNCIA 
                        #   QUE O ROBÔ POSSUI VELOCIDADE VARIADA ]
                        dist_velocidade_constante = distancia_maxima - s_instante_vel_max

                        # [ APLICAR A FÓRMULA DA VELOCIDADE MÉDIA PARA DESCOBRIR O 
                        #   TEMPO QUE O ROBÔ POSSUI VELOCIDADE CONSTANTE ]
                        tempo_const_robo = tempo_robo_bola(dist_velocidade_constante, 2.3)

                        # [ SOMAR OS DOIS TEMPOS PARA OBTER O TEMPO TOTAL ]
                        tempo_const_robo = tempo_const_robo + instante_vel_max
                        # print(tempo_const_robo)


                        # ===============================
                        # Velocidade e Aceleração do Robô
                        # ===============================
                        # VARIÁVEIS GLOBAIS
                        # velocidade_robo = []
                        # aceleracao_robo = []
                        # arr_t_aux = []

                        # Capturando a Velocidade e Aceleração do Robô a cada 20ms (escolha do Pajé) até o instante de interceptação
                        index = 0
                        dv = 0
                        
                        while (lista_t_pos[index] != menor_distT):
                            velocidade_robo.append(dv)
                            arr_t_aux.append(lista_t_pos[index])

                            if lista_t_pos[index] <= instante_vel_max[index]:
                                dv += 0.02
                                aceleracao_robo.append(4)
                            
                            else:
                                dv += 0
                                aceleracao_robo.append(0)
                            
                            index += 1
                        
                        
                        # Verificando se o tempo que o robô percorre a trajetória é menor ou igual ao tempo da bola no instante encontrado
                        if tempo_const_robo <= menor_distT:
                            intercepto = True

                            # [ INFORMANDO QUE O ROBÔ INTERCEPTOU A BOLA ]
                            messagebox.showinfo('Alerta!',
                                                      'O robô interceptou a bola com SUCESSO!')

                            # [ FECHA A CAIXA DE DIÁLOGO ]
                            master.destroy()

                            # ===================================================
                            # Encontrando a equação da reta que o robô percorrerá para interceptar a bola
                            # ===================================================
                            # [ Será utilizada para locomover o robô no vPython ]
                            equacao_da_reta([x_robo, y_robo],
                                            [menor_distX, menor_distY],
                                            x_robo, y_robo,
                                            menor_distX, menor_distY, menor_distT,
                                            velocidade_robo,
                                            aceleracao_robo,
                                            arr_t_aux)
                        
                        else:
                            # SE NÃO INTERCEPTAR:
                            messagebox.showinfo('Alerta',
                                                      'O Robô FALHOU ao interceptar a bola...')
                            # [ FECHA A CAIXA DE DIÁLOGO ]
                            master.destroy()
                            
                            # Encontrando a equação da reta que o robô percorrerá para interceptar a bola mesmo não conseguindo!
                            # [ Será utilizada para locomover o robô no vPython ]
                            equacao_da_reta([x_robo, y_robo],
                                            [menor_distX, menor_distY],
                                            x_robo, y_robo,
                                            menor_distX, menor_distY, menor_distT,
                                            velocidade_robo,
                                            aceleracao_robo,
                                            arr_t_aux)
                    else:
                        messagebox.showinfo('Alerta!',
                                            'Preencha TODOS os campos, por favor!')


    # ====----====----====----====----====----====----====----====
    #   [ Botão para o envio dos dados fornecidos pelo usuário ]
    # ====----====----====----====----====----====----====----====

    btn = tk.Button(master, command = enviar_coordenadas)

    btn.place(relx=0.5, rely=0.8, anchor='center')
    btn.configure(text="Enviar", font = ('Helvetica', 11, 'normal'), bg='#FAFBFF', fg='#2d2e30')

    # Mantem a janela aberta
    master.mainloop()


inicializa_janela_coordenadas()