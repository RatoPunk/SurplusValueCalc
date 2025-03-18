import tkinter as tk
from tkinter import messagebox
import pygame

def calcular_mais_valia():
    try:
        vp = float(entry_vp.get())
        salario = float(entry_salario.get())

        mais_valia = vp - salario
        taxa_mais_valia = (mais_valia / salario) * 100 if salario != 0 else 0

        resultado = f"Mais-valia: R$ {mais_valia:.2f}\nTaxa de exploração: {taxa_mais_valia:.2f}%"
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Mais-Valia")
root.geometry("350x150")
# Criando os widgets
tk.Label(root, text="Valor Produzido (R$):").grid(row=0, column=0, padx=5, pady=10)
entry_vp = tk.Entry(root)
entry_vp.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Salário Pago (R$):").grid(row=1, column=0, padx=5, pady=10)
entry_salario = tk.Entry(root)
entry_salario.grid(row=1, column=1, padx=10, pady=5)

botao_calcular = tk.Button(root, text="Calcular", command=calcular_mais_valia)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)



# pygame init
pygame.mixer.init()

# load bgm
pygame.mixer.music.load("c:/Users/Public/Assets/music.mp3")  
pygame.mixer.music.play(-1) 


# Rodando a interface
root.mainloop()
