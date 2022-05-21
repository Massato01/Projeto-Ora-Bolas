# ==================================================
# ------------------ BIBLIOTECAS -------------------
import sys
import os.path
import tkinter     as tk
import tkinter.ttk as ttk
from   graficos    import *
from   vpython     import *
from   visual_3d   import *
from   PIL         import ImageTk, Image
# ==================================================


# =====================================
# ------- Inicializa Interface --------
def inicializaInterface():
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = JanelaPrincipal (root)
    root.resizable(0, 0)
    root.tk.call('wm', 'iconphoto', root._w)
    root.mainloop()


w = opcSelecionada = None

def create_JanelaPrincipal(root, *args, **kwargs):
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = JanelaPrincipal (w)
    return (w, top)


def destroy_JanelaPrincipal():
    global w
    w.destroy()
    w = None


class JanelaPrincipal:

    def __init__(self, top=None):
        top.geometry("647x499+340+115")
        top.title("Projeto Oras Bolas")
        top.configure(background="#d9d9d9")

        # =============================#
        #           FUNDO
        # =============================#
        # Plano de fundo dinâmico (variado se o robô interceptar ou não)
        # if intercept:
        #     imgFundo = os.path.join(prog_location,"assets/bg_success.png")
        # else:
        #     imgFundo = os.path.join(prog_location, "assets/bg_fail.png")
        # self._fundo = tk.PhotoImage(file=imgFundo)

        self.Fundo = tk.Label(top)
        self.Fundo.place(relx=-0.015, rely=-0.02, height=524, width=664)
        # self.Fundo.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", image=self._fundo,
        #                      text='''Label''', width=664)
        self.Fundo.configure(background="#2d2e30", disabledforeground="#a3a3a3", foreground="#000000", text='''''', width=664)

        # ============================= #
        #      TITULO DO PROJETO
        # ============================= #
        self.title = tk.Label(top, text = 'PROJETO ORA BOLAS', font = ('Cascadia Code', 25, 'bold'), fg = '#7eddd3')
        self.title.place(relx = 0.5, rely = 0.08, anchor = 'center')
        self.title.configure(background="#2d2e30")

        # ============================= #
        #    IMAGEM DO ROBO CENTRAL
        # ============================= #
        img_path = 'assets/root.png'
        img_robot = ImageTk.PhotoImage(Image.open(img_path))
        self.central_robot = ttk.Label(top, image = img_robot)
        self.central_robot.pack()
        # self.central_robot.place(relx = 0.5, rely = 0.3, anchor = 'center')
        # self.central_robot.configure(width = 100)

        # ============================= #
        #           RELATORIO
        # ============================= #
        def verRelatorio():

            mensagem =  "Dados sobre o robô: " \
                        "\n• Robô: Small Size" \
                        "\n• Raio da bola: 21 mm" \
                         "\n• Raio: 90mm" \
                        "\n• Velocidade máxima: 2.3 m/s" \
                        "\n• Aceleração: 4 m/s²"
            if intercepto:
                mensagem += "\n\nDados sobre a interceptação:"\
                            "\n• O robô interceptou a bola com sucesso! ;-)"\
                            "\n• Tempo de interceptação: {}s"\
                            "\n• Coordenada em X da interceptação: {}"\
                            "\n• Coordenada em Y da interceptação: {}".format(menor_distT, menor_distX, menor_distY)
            else:
                mensagem += "\n\nDados sobre a interceptação:"\
                            "\n• O robô não interceptou a bola :-("\

            mensagem += "\n\nSoftwares Utilizados: " \
                        "\n• Visual Studio Code - IDE para o desenvolvimento do código"\
                        "\n• EXCEL - x(t) da bola: x = -0,008t^3 - 0,15t^2 + 2,5t + 1"\
                        "\n• MATLAB - y(t) da bola: y = -0.2*t^(1.5) + 1.6*t + 1"

            print(messagebox.showinfo("Dados obtidos:", mensagem))



        # =============================================#
        #      RELATÓRIO (botão - abrirá outra janela)
        # =============================================#
        self.BotaoRelatorio = tk.Button(top, command=verRelatorio)
        self.BotaoRelatorio.place(relx=0.5, rely=0.521, height=44, width=260, anchor = 'center')
        self.BotaoRelatorio.configure(font = ('Cascadia Code', 13, 'normal'), background="#4A4747", fg = '#7eddd3', text='''Relatório de Dados''', width=157)


        # =============================#
        #      GRÁFICOS (combobox)
        # =============================#
        self.label_graph = tk.Label(top, text = 'GRÁFICOS:', font = ('Cascadia Code', 15, 'bold'))
        self.label_graph.place(relx = 0.16, rely = 0.72, anchor = 'center')
        self.label_graph.configure(bg = '#2d2e30', fg = '#7eddd3')

        self.box_value = tk.StringVar()
        self.box_value.set("Selecione um gráfico")

        # Definindo a cor de fundo do combobox
        self.style = ttk.Style()
        self.style.theme_use('alt')
        # the following alters the Combobox entry field
        self.style.map('TCombobox', fieldbackground=[('readonly', '#4A4747')])
        self.style.map('TCombobox', selectbackground=[('readonly', '#4A4747')])
        self.style.map('TCombobox', selectforeground=[('readonly', '#FFFFFF')])
        self.style.map('TCombobox', background=[('readonly', '#4A4747')])
        self.style.map('TCombobox', foreground=[('readonly', '#7eddd3')])

        self.OpcGraficos = ttk.Combobox(top, textvariable= self.box_value,
                                state='readonly')

        self.OpcGraficos.place(relx=0.263, rely=0.681, relheight=0.082
                , relwidth=0.553)
        self.OpcGraficos.configure(width=240, font = ('Cascadia Code', 11, 'normal'), background = '#4A4747', foreground = '#7eddd3')

        # Captura o valor selecionado no combobox (pelo primeiro caracter = número) e o retorna para a variável opcSelecionada
        def callback(eventObject):
            global opcSelecionada
            try:
                opcSelecionada = int(self.OpcGraficos.get().split()[0])
                self.viewGrafico['state'] = 'normal'
            except:
                self.viewGrafico['state'] = 'disabled' #Desativa o botão se o usuário selecionar uma opção inválida, como: "PARA O ROBÔ"

        # Lista as opções de gráficos no combobox
        self.OpcGraficos['values']=('-------------------- BOLA ----------------------',
                                    '1 - Deslocamento da Bola X(t) e Y(t)',
                                    '2 - Velocidade da Bola Vx(t) e Vy(t)',
                                    '3 - Aceleração da Bola Ax(t) e Ay(t)',
                                    '4 - Trajetória da Bola ao Gol',
                                    '-------------------- ROBÔ ----------------------',
                                    '5 - Deslocamento do Robô X(t) e Y(t)',
                                    '6 - Velocidade do Robô Vx(t) e Vy(t)',
                                    '7 - Aceleração do Robô Ax(t) e Ay(t)',
                                    '8 - Velocidade do robô em função do tempo',
                                    '9 - Aceleração do robô em função do tempo',
                                    '-------------------- AMBOS ---------------------',
                                    '10 - Trajetória da Bola e do Robô num plano',
                                    '11 - Distância entre o robô e a bola em função do tempo')

        self.OpcGraficos.current(0) # Varia as seleções do combobox
        self.OpcGraficos.bind("<<ComboboxSelected>>", callback)
        self.OpcGraficos.set("Selecione um gráfico") #Texto inicial - para quando não houver nada selecionado

        # ====================================================================#
        #      CHAMA GRÁFICOS - Através das numerações dadas no combobox
        # ====================================================================#

        def invocaGrafico():

            # global bolaX, bolaY, xRobo, menorDistX, yRobo, menorDistY, menorDistT, intercept

            if opcSelecionada == 1:
                plot_duplo(bola_t_pos, bola_x_pos, "x(t) da bola", 't/s', 'x/m', 'x(t)', # Gráfico da posição em X da bola em função do tempo
                           bola_t_pos, bola_y_pos, "y(t) da bola", 't/s', 'y/m', 'y(t)') # Gráfico da posição em Y da bola em função do tempo

            elif opcSelecionada == 2:
                # equações encontradas x(t) da bola: x = -0,008t^3 - 0,15t^2 + 2,5t + 1
                #                      y(t) = -0.2*t^(1.5) + 1.6*t + 1
                # Decompondo a VELOCIDADE, basta derivar uma vez
                plotar_vxvy_axay(diff(-0.008 * t ** 3 - 0.15 * t ** 2 + 2.5 * t + 1, t),
                            diff( -0.2*t**1.5 + 1.6*t + 1,t),
                            "da bola","v")

            elif opcSelecionada == 3:
                # Decompondo a ACELERAÇÃO, basta derivar duas vezes
                plotar_vxvy_axay(diff(diff( -0.008*t**3 - 0.15*t**2 + 2.5*t + 1,t),t),
                            diff(diff( -0.2*t**1.5 + 1.6*t + 1,t),t),
                            "da bola", "a")


            elif opcSelecionada == 4:
                # plotar_grafico(bolaGol_x,bolaGol_y, "Bola ao Gol", 'x/m', 'y/m')
                pass

            elif opcSelecionada == 5:
                # plot_duplo(tRoboIntercept, xRoboIntercept, "x(t) do Robô", "t/s", "x/m", 'x(t)',  # Gráfico x(t) do robô
                #            tRoboIntercept, yRoboIntercept, "y(t) do robô", "t/s", "y/m", 'y(t)')  # Gráfico y(t) do robô
                pass

            elif opcSelecionada == 6:
                plot_duplo(lista_tempo, vx_robo, "Vx(t) do robô", "t(s)", "Vx(m/s)", 'Vx(t)',  # Gráfico vx(t) do robô
                           lista_tempo, vy_robo, "Vy(t) do robô", "t(s)", "Vy(m/s)", 'Vy(t)')  # Gráfico vy(t) do robô

            elif opcSelecionada == 7:
                plot_duplo(lista_tempo, ax_robo, "Ax(t) do robô", "t(s)", "Ax(m/s^2)", 'Ax(t)',  # Gráfico sx(t) do robô
                           lista_tempo, ay_robo, "Ay(t) do robô", "t(s)", "Ay(m/s^2)", 'Ay(t)')  # Gráfico sy(t) do robô
    
            elif opcSelecionada == 8:
                plotar_grafico(lista_tempo, velocidade_robo, "V(t) do robô", 's', 'm/s')

            elif opcSelecionada == 9:
                plotar_grafico(lista_tempo, aceleracao_robo, "a(t) do robô", 's', 'm/s^2')

            elif opcSelecionada == 10:
                # Caso intercepte, analisa as coordenadas da bola até o menor tempo encontrado (instante de interceptação)
                if intercepto:
                    plotar_trajetoria_intercepto(x_bola, y_bola, [x_robo, menor_distX], [y_robo, menor_distY], menor_distT, intercepto)
                # senão analisa todas as coordenadas extreídas do arquivo trajetoria.txt
                else:
                    plotar_trajetoria_intercepto(bola_x_pos, bola_y_pos, [x_robo, menor_distX], [y_robo, menor_distY], menor_distT, intercepto)

            elif opcSelecionada == 11:
                # plotar_grafico(tRoboIntercept, distRoboBola, "Distância relativa entre o robô e a bola em função do tempo", 's', 'm')
                pass


        # ================= BOTÃO ===================

        # Botão para que o usuário informe o gráfico a ser exibido
        buttonImg = os.path.join(prog_location,"assets/cyan-circle.png")
        # self._img1 = tk.PhotoImage(file=eyeImg)
        self._img1 = tk.PhotoImage(file = buttonImg) # file = path to file

                            # O botão só é ativado quando a opção selecionada for um gráfico
        #                                             /\
        #                                             ||
        self.viewGrafico = tk.Button(top, state = 'disabled', command=invocaGrafico)

        self.viewGrafico.place(relx=0.84, rely=0.695)
        self.viewGrafico.configure(height=20, width=20, image=self._img1, text='''Visualizar''')
        # ===========================================
        
if __name__ == "__main__":
    inicializaInterface()