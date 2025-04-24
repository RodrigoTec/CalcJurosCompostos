import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_juros_compostos():
    try:
        principal = float(entry_principal.get())
        taxa = float(entry_taxa.get()) / 100
        periodos = int(entry_periodos.get())
        tipo = combo_tipo.get()

        if tipo == "Anual":
            taxa_efetiva = taxa
        elif tipo == "Mensal":
            taxa_efetiva = taxa / 12
        else:
            messagebox.showerror("Erro", "Selecione o tipo de juros.")
            return

        montante = principal * ((1 + taxa_efetiva) ** periodos)
        label_resultado.config(text=f"Valor Futuro: R$ {montante:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Juros Compostos")
janela.geometry("350x300")
janela.resizable(False, False)

# Valor inicial
tk.Label(janela, text="Valor Inicial (R$):").pack(pady=5)
entry_principal = tk.Entry(janela)
entry_principal.pack()

# Taxa de juros
tk.Label(janela, text="Taxa de Juros a.a(%):").pack(pady=5)
entry_taxa = tk.Entry(janela)
entry_taxa.pack()

# Número de períodos
tk.Label(janela, text="Número de Períodos:").pack(pady=5)
entry_periodos = tk.Entry(janela)
entry_periodos.pack()

# Tipo de juros
tk.Label(janela, text="Tipo de Juros:").pack(pady=5)
combo_tipo = ttk.Combobox(janela, values=["Mensal", "Anual"], state="readonly")
combo_tipo.pack()
combo_tipo.current(0)

# Botão calcular
tk.Button(janela, text="Calcular", command=calcular_juros_compostos).pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="Valor Futuro: R$ 0.00", font=("Helvetica", 12, "bold"))
label_resultado.pack(pady=10)

# Iniciar loop da interface
janela.mainloop()
