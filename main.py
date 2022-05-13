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
# ---- Classe da Janela Princiapal ----
class JanelaPrincipal:

    def __init__(self, janela = None):
        janela.geometry('600x500')
        janela.title('Projeto Ora Bolas')
        janela.configure(background = '#d9d9d9')
# =====================================


# =====================================
# ------- Inicializa Interface --------
def inicializa_interface():
    master = tk.Tk()
    janela = JanelaPrincipal(master)
    
    master.mainloop()


w = None
opcao_selecionada = None

def fechar_janela_principal():
    global w
    w.destroy()
# =====================================

# inicializa_interface()

if intercepto:
    plotar_trajetoria_intercepto(x_bola, y_bola, [x_robo, menor_distX], [y_robo, menor_distY], menor_distT, intercepto)
else:
    plotar_trajetoria_intercepto(bola_x_pos, bola_y_pos, [x_robo, menor_distX], [y_robo, menor_distY], menor_distT, intercepto)
