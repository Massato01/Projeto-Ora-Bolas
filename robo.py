# ==================================================
# ------------------ BIBLIOTECAS -------------------
import tkinter  as tk
from   tkinter  import messagebox
from   sympy    import *

# Calculos da distancia, tempo e equacao da reta
from   equacoes import *
# ==================================================


def inicializar_janela_coordenadas():
    '''
    ============================================================
    INICIALIZA UMA JANELA DE ENTRADA PARA AS COORDENADAS DO ROBÔ
    ============================================================
    '''
    global y_bola, x_bola, x_robo, y_robo, menor_distX, menor_distY, menor_distT

    # listas das coordenadas da bola
    x_bola = []
    y_bola = []

    # ==========================================================
    # ---------------- BASE DA JANELA PRINCIPAL ----------------
    # ==========================================================

    master = tk.Tk()
    master.geometry('450x180')
    master.title('Posição inicial do Robô')
    master.configure(bg='#FAFBFF')

    # Cria as LABELS para que o usuário digite as coordenadas
    window_title = tk.Label(master, text="COORDENADAS INICIAIS DO ROBÔ")
    xLabel_coord = tk.Label(master, text="Digite a coordenada X do Robô:")
    yLabel_coord = tk.Label(master, text="Digite a coordenada Y do Robô:")

    window_title.place(relx=0.5, rely=0.20, anchor='center')
    xLabel_coord.place(relx=0.3, rely=0.4, anchor='center')
    yLabel_coord.place(relx=0.3, rely=0.55, anchor='center')

    window_title.configure(font=('Helvetica', 12, 'bold'), bg='#FAFBFF', fg='#2d2e30')
    xLabel_coord.configure(font=('Helvetica', 12, 'normal'), bg='#FAFBFF', fg='#2d2e30')
    yLabel_coord.configure(font=('Helvetica', 12, 'normal'), bg='#FAFBFF', fg='#2d2e30')


    # Cria duas caixas de diálogo, uma para cada coordenada
    xRobo_input = tk.Entry(master)
    yRobo_input = tk.Entry(master)

    # Separa os campos de entrada de X e de Y
    xRobo_input.place(relx=0.78, rely=0.4, anchor='center')
    yRobo_input.place(relx=0.78, rely=0.55, anchor='center')

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
        global x_bola, y_bola, x_robo, menor_distX, y_robo, menor_distY, menor_distT, intercepto, velocidade_robo, aceleracao_robo, lista_tempo

        
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
            elif x_robo == 1 and y_robo == 0.5:
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

                for i in range(len(bola_x_pos)):
                    # ========================================================
                    # Distância do robô até a bola em cada ponto da trajetória
                    # ========================================================
                    if bola_x_pos[i] >= 0.0 and bola_x_pos[i] <= 9.0 and bola_x_pos[i] >= 0.0 and bola_x_pos[i] <= 6.0:
                        distancia_total = (dist_robo_bola(x_robo,
                                                          y_robo,
                                                          bola_x_pos[i],
                                                          bola_y_pos[i])) - raio

                        # Armazena as coordenadas da bola enquanto ela estiver em campo
                        x_bola.append(bola_x_pos[i])
                        y_bola.append(bola_x_pos[i])

                        # armazena a mínima distância possível e o tempo levado para o robô realizá-la
                        if (distancia_total < distancia_maxima):
                            distancia_maxima = distancia_total
                            menor_distX = bola_x_pos[i]
                            menor_distY = bola_y_pos[i]
                            menor_distT = bola_t_pos[i]

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
                velocidade_robo = []
                aceleracao_robo = []
                lista_tempo = []

                # Capturando a Velocidade e Aceleração do Robô a cada 20ms (escolha do Pajé) até o instante de interceptação
                index = 0
                dv = 0

                while (bola_t_pos[index] != menor_distT):
                    velocidade_robo.append(dv)
                    lista_tempo.append(bola_t_pos[index])

                    if bola_t_pos[index] <= s_instante_vel_max:
                        dv += 0.08
                        aceleracao_robo.append(4)
                    else:
                        dv += 0
                        aceleracao_robo.append(0)
                    index += 1



                # Verificando se o tempo que o robô percorre a trajetória é menor ou igual ao tempo da bola no instante encontrado
                if tempo_const_robo <= menor_distT:

                    global intercepto
                    intercepto = True

                    # [ INFORMANDO QUE O ROBÔ INTERCEPTOU A BOLA ]
                    messagebox.showinfo('INTERCEPTOU!',
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
                                        lista_tempo)

                else:
                    # SE NÃO INTERCEPTAR:
                    messagebox.showinfo('NÃO INTERCEPTOU...',
                                        'O Robô FALHOU ao tentar interceptar a bola...')
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
                                    lista_tempo)


    # ====----====----====----====----====----====----====----====
    #   [ Botão para o envio dos dados fornecidos pelo usuário ]
    # ====----====----====----====----====----====----====----====

    btn = tk.Button(master, command = enviar_coordenadas)

    btn.place(relx=0.5, rely=0.8, anchor='center')
    btn.configure(text="Enviar", font = ('Helvetica', 11, 'normal'), bg='#FAFBFF', fg='#2d2e30')

    # Mantem a janela aberta
    master.mainloop()


inicializar_janela_coordenadas()


print(f'''
{y_bola = }\n
{x_bola = }\n
{x_robo = }\n
{y_robo = }\n
{menor_distX = }\n
{menor_distY = }\n
{menor_distT = }\n
{m = }\n
{cl = }\n
{lista_yRobo = }\n
{lista_xRobo = }\n
{lista_tempo = }\n
{velocidade_robo = }\n
{aceleracao_robo = }\n
{vx_robo = }\n
{ax_robo = }\n
{vy_robo = }\n
{ay_robo = }\n
{intercepto = }\n
''')