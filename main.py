# ==================================================
# ------------------ BIBLIOTECAS -------------------
import sys
import os.path
import tkinter     as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from   graficos    import *
from   visual_3d   import *
# ==================================================


# ======================================
# -------- INTERFACE PRINCIPAL ---------
def main():
    # ==========================
    #   ESTRUTURA DA INTERFACE
    # ==========================
    master = tk.Tk()
    master.geometry('600x500')
    master.title('Projeto Ora Bolas')
    master.configure(bg = '#d9d9d9')

    # ----------------------
    #         Fundo
    # ----------------------
    fundo = tk.Label(master)
    fundo.place(relx=-0.015, rely=-0.02, height=524, width=664)
    fundo.configure(background="#FAFBFF", disabledforeground="#a3a3a3",
                    foreground="#000000", text='''''', width=664)

    # ----------------------
    #        Titulo
    # ----------------------
    titulo = tk.Label(master, text = 'PROJETO ORA BOLAS',
                      font = ('Helvetica', 25, 'bold'),
                      bg = '#FAFBFF')
    titulo.place(relx = 0.5, rely = 0.08, anchor = 'center')
    
    # ----------------------
    # IMAGEM DO ROBO CENTRAL
    # ----------------------
    # img_path = './assets/smsize.png'
    # img_robo = ImageTk.PhotoImage(Image.open(img_path))
    # robo_central = ttk.Label(master, image = img_robo)
    
    # robo_central.place(relx = 0.1, rely = 0.5, anchor = 'center')
    # robo_central.configure(width = 10)
    # robo_central.pack()


    def visualizar_especificacoes():

        mensagem = '''Informaçoes do robô:
        Tipo: Small Size
        Velocidade máxima: 2.3m/s
        Aceleração: 4m/s²
        Raio: 0.021cm'''

        if intercepto == True:
            mensagem += f'''\n\nInformações da interceptação:\nO robô interceptou a bola nos pontos ({menor_distX}, {menor_distY}) no instante {menor_distT}'''
        
        else:
            mensagem += f'''Informações da interceptação
            O robô não conseguiu interceptar a bola'''

        print(messagebox.showinfo(f"Dados obtidos:", mensagem))

    # ------------------------
    # BOTÃO DAS ESPECIFICAÇÕES
    # ------------------------
    btn_espec = tk.Button(master, command=visualizar_especificacoes)
    btn_espec.place(relx=0.5, rely=0.2, height=44, width=260, anchor = 'center')
    btn_espec.configure(font = ('Helvetica', 13, 'normal'), background="#4A4747", fg = '#7eddd3', text='''Visualizar Especificações''', width=157)


    master.mainloop()



if __name__ == '__main__':
    main()
