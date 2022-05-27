# ==================================================
# ------------------ BIBLIOTECAS -------------------
import tkinter     as     tk
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

    graficos_label = tk.Label(master, text = 'VISUALIZAR GRÁFICOS:',
                              font = ('Helvetica', 12, 'normal'))

    graficos_label.place(relx = 0.5, rely = 0.74, anchor = 'center')

    graficos_label.configure(bg="#FAFBFF", fg='black')

    
    # ==============================================
    # [ PLOTANDO OS GRÁFICOS DE ACORDO COM A OPÇÃO ]
    # ==============================================
    def plotar_grafico_escolhido():
        # ------------------------------------------
        #          TRAJETÓRIA DA BOLA

        # X e Y da Bola em fução do tempo
        plot_duplo('X da bola em função do Tempo', bola_t_pos, bola_x_pos,
                    't/s', 'x/m', 'x(t)',
                    
                   'Y da bola em função do Tempo', bola_t_pos, bola_y_pos,
                   't/s', 'y/m', 'y(t)')
        # ------------------------------------------

        # ------------------------------------------
        #            VELOCIDADE DA BOLA

        # EQUAÇÃO DO EXCEL: 
        #        x(t) = -0.002x² + 10.004x + 990.03
        #        y(t) = -0.0032x² + 7.5905x + 998.88

        # EQUAÇÃO DO PYTHON:
        #        x(t) = -0.002 * t ** 2 + 10.004 * t + 990.03
        #        y(t) = -0.0032 * t ** 2 + 7.5905 * t + 998.88

        #          [ DERIVA ]       [ DERIVA ]  
        #    POSIÇÃO   -->  VELOCIDADE  --> ACELERAÇÃO
        plotar_vxvy_axay('da Bola',
                         diff(-0.002 * t ** 2 + 10.004 * t + 990.03),
                         diff(-0.0032 * t ** 2 + 7.5905 * t + 998.88),
                         'V')
        # ------------------------------------------

        # ------------------------------------------
        #           ACELERAÇÃO DA BOLA

        # EQUAÇÃO DO EXCEL: 
        #        x(t) = -0.002x² + 10.004x + 990.03
        #        y(t) = -0.0032x² + 7.5905x + 998.88

        # EQUAÇÃO DO PYTHON:
        #        x(t) = -0.002 * t ** 2 + 10.004 * t + 990.03
        #        y(t) = -0.0032 * t ** 2 + 7.5905 * t + 998.88

        #          [ DERIVA ]       [ DERIVA ]  
        #    POSIÇÃO   -->  VELOCIDADE  --> ACELERAÇÃO
        plotar_vxvy_axay('da Bola',
                         diff(diff(-0.002 * t ** 2 + 10.004 * t + 990.03)),
                         diff(diff(-0.0032 * t ** 2 + 7.5905 * t + 998.88)),
                         'A')
        # ------------------------------------------

        # ------------------------------------------
        #           TRAJETÓRIA DO ROBÔ

        # X e Y do Robô em função do tempo
        plot_duplo('X do robô em função do Tempo',
                    intercepto_tRobo, intercepto_xRobo,
                    't/s', 'x/m', 'x(t)',
                    
                    'Y do robô em função do Tempo',
                    intercepto_tRobo, intercepto_yRobo,
                    't/s', 'x/m', 'x(t)')
        # ------------------------------------------

        # ------------------------------------------    
        #   VELOCIDADE DO ROBÔ EM FUNÇÃO DO TEMPO

        plotar_grafico('Velocidade do robô em função do Tempo',
                        lista_tempo, velocidade_robo, 'Segundos', 'm/s')
        # ------------------------------------------

        # ------------------------------------------
        #   ACELERAÇÃO DO ROBÔ EM FUNÇÃO DO TEMPO
        
        plotar_grafico('Aceleração do robô em função do Tempo',
                        lista_tempo, aceleracao_robo, 'Segundos', 'm/s²')
        # ------------------------------------------

        # ------------------------------------------
        #        VELOCIDADE DO ROBÔ VX/VY

        # VX e VY do Robô
        plot_duplo('VX do Robô', lista_tempo, vx_robo,
                   't(s)', 'Vx(m/s)', 'Vx(t)',
                    
                   'VY do Robô', lista_tempo, vy_robo,
                   't(s)', 'Vy(m/s)', 'Vy(t)')
        # ------------------------------------------

        # ------------------------------------------
        #        ACELERAÇÃO DO ROBÔ AX/AY

        # AX e AY do Robô
        plot_duplo('AX do Robô', lista_tempo, ax_robo,
                   't(s)', 'Ax(m/s²)', 'Ax(t)',
                    
                   'AY do Robô', lista_tempo, ay_robo,
                   't(s)', 'Ay(m/s²)', 'Ay(t)')
        # ------------------------------------------

        # ------------------------------------------    
        #        ROBÔ E A BOLA EM UM PLANO

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
        # ------------------------------------------

        # ------------------------------------------
        #      DISTÂNCIA ENTRE O ROBÔ E A BOLA

        plotar_grafico('Distância entre o robô e a bola em função do tempo',
                       intercepto_tRobo, distancia_robo_bola,
                       'Segundos', 'Metros')
        # ------------------------------------------

    # =============================
    # BOTÃO PARA PLOTAR OS GRÁFICOS
    # =============================
    btn_graficos = tk.Button(master, text='Visualizar', command = plotar_grafico_escolhido)
    btn_graficos.place(relx = 0.5, rely = 0.8, anchor = 'center')


    master.mainloop()



if __name__ == '__main__':
    main()
