import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())

        if operacao.get() == "Potência (P = V x I)":
            resultado = valor1 * valor2
            label_resultado.config(text=f"{resultado:.2f} W")

        elif operacao.get() == "Tensão (V = R x I)":
            resultado = valor1 * valor2
            label_resultado.config(text=f"{resultado:.2f} V")

    except:
        label_resultado.config(text="Valores inválidos")

# Janela
root = tk.Tk()
root.title("Calculadora Elétrica")
root.geometry("320x250")

# Escolha da operação
operacao = ttk.Combobox(root, values=[
    "Potência (P = V x I)",
    "Tensão (V = R x I)"
])
operacao.current(0)
operacao.pack(pady=10)

# Inputs
entrada1 = ttk.Entry(root)
entrada1.pack(pady=5)
entrada1.insert(0, "Valor 1")

entrada2 = ttk.Entry(root)
entrada2.pack(pady=5)
entrada2.insert(0, "Valor 2")

# Botão
ttk.Button(root, text="Calcular", command=calcular).pack(pady=10)

# Resultado
label_resultado = ttk.Label(root, text="Resultado")
label_resultado.pack(pady=10)

root.mainloop()