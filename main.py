# ==================================================
# ------------------ BIBLIOTECAS -------------------
import tkinter     as     tk
import tkinter.ttk as     ttk
from   graficos    import *
from   visual_3d   import *
# ==================================================


# ======================================
# -------- INTERFACE PRINCIPAL ---------
def main():
    # ===============================
    #   ESTRUTURA DA INTERFACE
    # ===============================
    master = tk.Tk()
    master.geometry('600x500')
    master.title('Projeto Ora Bolas')
    master.configure(bg = '#d9d9d9')

    # -------------------------------
    #              FUNDO
    # -------------------------------
    fundo = tk.Label(master)

    fundo.place(relx=-0.015, rely=-0.02, height=524, width=664)

    fundo.configure(background="#FAFBFF", disabledforeground="#a3a3a3",
                    foreground="#000000", text='''''', width=664)

    # -------------------------------
    #             TÍTULO
    # -------------------------------
    titulo = tk.Label(master, text = 'PROJETO ORA BOLAS',
                      font = ('Helvetica', 25, 'bold'),
                      bg = '#FAFBFF')
    titulo.place(relx = 0.5, rely = 0.08, anchor = 'center')
    
    # -------------------------------
    #     ESPECIFICAÇÕES DO ROBÔ
    # -------------------------------
    especificacoes = tk.Label(master, text = '''Informaçoes do robô:
Tipo: Small Size
Velocidade máxima: 2.3m/s
Aceleração: 4m/s²
Raio: 0.21m''', font=('Helvetica', 12, 'bold'), bg = '#FAFBFF', relief='ridge')
    especificacoes.pack(fill = 'both')

    especificacoes.place(relx = 0.5, rely = 0.3, anchor = 'center')
    
    intercepto = True

    # -------------------------------
    #   MENSAGEM DE INTERCEPTACAO
    # -------------------------------
    # [ SE INTERCEPTAR ]
    if intercepto == True:
        intercepto_true = tk.Label(master, text = f'''O ROBÔ CONSEGUIU INTERCEPTAR A BOLA COM SUCESSO!\n\nInformações da interceptação:
Ponto X da interceptação: {menor_distX:.1f}
Ponto Y da interceptação: {menor_distY:.1f}
Instante de interceptação: {menor_distT:.1f}''', font = ('Helvetica', 12, 'bold'))

        intercepto_true.place(relx = 0.5, rely = 0.55, anchor = 'center')

        intercepto_true.configure(bg="#FAFBFF", fg = 'black')
    
    # [ SE NÃO INTERCEPTAR ]
    else:
        intercepto_false = tk.Label(master, text = f'''O robô não conseguiu interceptar a bola...''', font = ('Helvetica', 12, 'bold'))

        intercepto_false.place(relx = 0.5, rely = 0.5, anchor = 'center')

        intercepto_false.configure(bg="#FAFBFF", fg = 'black')
    
    # -------------------------------
    #            GRÁFICOS
    # -------------------------------
    escolha = None
    # def callback(eventObject):
    #     global escolha
    #     try:
    #         escolha = int(graficos_escolha.get().split()[0])
    #         btn_graficos['state'] = 'normal'
    #     except:
    #         btn_graficos['state'] = 'disabled'


    graficos_label = tk.Label(master, text = 'VISUALIZAR GRÁFICOS:',
                              font = ('Helvetica', 12, 'normal'))

    graficos_label.place(relx = 0.5, rely = 0.74, anchor = 'center')

    graficos_label.configure(bg="#FAFBFF", fg='black')


    # =====================================
    #               COMBOBOX
    # =====================================
    # # Texto padrão da caixa de escolhas
    # textbox = tk.StringVar()
    # textbox.set('Escolha uma opção')

    # # Escolha do gráfico
    # graficos_escolha = ttk.Combobox(master, textvariable='Escolha uma opção',
    #                                 state = 'readonly')

    # graficos_escolha.place(relx = 0.5, rely = 0.8, anchor = 'center',
    #                        relwidth = 0.5)
    
    # graficos_escolha.configure(font = ('Helvetica', 11, 'normal'),
    #                            background = '#4A4747', foreground = 'black',
    #                            values=(# '=============== BOLA ===============',
    #                                   '1 Trajetória da Bola',
    #                                   '2 Velocidade da Bola',
    #                                   '3 Aceleração da Bola',
    #                                 #   '',
    #                                 #   '================ ROBÔ ===============',
    #                                   '4 Trajetória do Robô',
    #                                   '5 Velocidade do Robô',
    #                                   '6 Aceleração do Robô',
    #                                   '7 VX e VY do Robô',
    #                                   '8 AX e AY do Robô',
    #                                 #   '',
    #                                 #   '============ ROBÔ E BOLA ============',
    #                                   '9 Robô e Bola em um plano',
    #                                   '10 Distância entre o Robô e a Bola em T'
    #                            ))
    # # ATUALIZANDO ESCOLHA DO USUÁRIO
    # graficos_escolha.current(3)
    # # graficos_escolha.bind("<<ComboboxSelected>>", callback)
    # escolha = int(graficos_escolha.get().split()[0])
    # graficos_escolha.set('Escolha uma opção')
    # =======================================

    
    # ----------------------------------------------
    # [ PLOTANDO OS GRÁFICOS DE ACORDO COM A OPÇÃO ]
    # ----------------------------------------------
    print(escolha)
    def plotar_grafico_escolhido():
        # Trajetória da Bola
        # if escolha == 1:
        # X e Y da Bola em fução do tempo
        plot_duplo('X da bola em função do Tempo', bola_t_pos, bola_x_pos,
                    't/s', 'x/m', 'x(t)',
                    
                    'Y da bola em função do Tempo', bola_t_pos, bola_y_pos,
                    't/s', 'y/m', 'y(t)')

        # Velocidade da Bola
            
        
        # Aceleração da Bola
        

        # Trajetória do Robô
        # elif escolha == 4:
        # X e Y do Robô em função do tempo
        plot_duplo('X do robô em função do Tempo',
                    intercepto_tRobo, intercepto_xRobo,
                    't/s', 'x/m', 'x(t)',
                    
                    'Y do robô em função do Tempo',
                    intercepto_tRobo, intercepto_yRobo,
                    't/s', 'x/m', 'x(t)')
    
        # Velocidade do Robô em função do Tempo
        # elif escolha == 5:
        plotar_grafico('Velocidade do robô em função do Tempo',
                        lista_tempo, velocidade_robo, 's', 'm/s')

        # Aceleração do Robô em função do Tempo
        # elif escolha == 6:
        plotar_grafico('Aceleração do robô em função do Tempo',
                        lista_tempo, aceleracao_robo, 's', 'm/s²')

        # Velocidade do Robô VX/VY
        # elif escolha == 7:
        # VX e VY do Robô
        plot_duplo('VX do Robô', lista_tempo, vx_robo,
                    't(s)', 'Vx(m/s)', 'Vx(t)',
                    
                    'VY do Robô', lista_tempo, vy_robo,
                    't(s)', 'Vy(m/s)', 'Vy(t)')

        # Aceleração do Robô AX/AY
        # elif escolha == 8:
        # AX e AY do Robô
        plot_duplo('AX do Robô', lista_tempo, ax_robo,
                    't(s)', 'Ax(m/s²)', 'Ax(t)',
                    
                    'AY do Robô', lista_tempo, ay_robo,
                    't(s)', 'Ay(m/s²)', 'Ay(t)')
    
        # Robô e Bola em um plano
        # elif escolha == 9:
        # SE INTERCEPTAR plota as coordenadas da bola até a interceptação
        if intercepto == True:
            plotar_trajetoria_intercepto(x_bola, y_bola,
                                            [x_robo, menor_distX],
                                            [y_robo, menor_distY],
                                            menor_distT, intercepto)
        # SE NÃO INTERCEPTAR plota a trajetória da bola
        else:
            plotar_trajetoria_intercepto(bola_x_pos, bola_y_pos,
                                            [x_robo, menor_distT],
                                            [y_robo, menor_distY],
                                            menor_distT, intercepto)

        # Distância ente o Robô e a Bola
        # elif escolha == 10:
        plotar_grafico('Distância entre o robô e a bola em função do tempo',
                        intercepto_tRobo, distancia_robo_bola,
                        's', 'm')
    # -----------------------------
    # BOTÃO PARA PLOTAR OS GRÁFICOS
    # -----------------------------
    btn_graficos = tk.Button(master, text='Visualizar', command = plotar_grafico_escolhido)
    btn_graficos.place(relx = 0.5, rely = 0.8, anchor = 'center')
    # btn_graficos.configure(text='Visualizar')

    master.mainloop()



if __name__ == '__main__':
    main()
