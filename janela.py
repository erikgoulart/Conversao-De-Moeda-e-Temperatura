import tkinter as tk
from tkinter import ttk, messagebox
from conversor import converter

# ======== FUNÇÕES ========

def mostrar_tela_inicial():
    """Exibe a tela inicial."""
    limpar_tela()
    tk.Label(janela, text="Conversor Universal 🌍", font=("Arial", 14, "bold")).pack(pady=20)
    tk.Label(janela, text="O que você deseja converter?", font=("Arial", 11)).pack(pady=10)

    tk.Button(janela, text="💱 Moedas", font=("Arial", 11, "bold"),
              width=20, bg="#2E8B57", fg="white", command=mostrar_tela_moedas).pack(pady=5)
    tk.Button(janela, text="🌡️ Temperaturas", font=("Arial", 11, "bold"),
              width=20, bg="#1E90FF", fg="white", command=mostrar_tela_temperatura).pack(pady=5)
    tk.Button(janela, text="❌ Sair", font=("Arial", 10), command=janela.quit).pack(pady=20)


def mostrar_tela_moedas():
    """Tela de conversão de moedas."""
    limpar_tela()
    tk.Label(janela, text="Conversão de Moedas 💱", font=("Arial", 14, "bold")).pack(pady=15)

    tk.Label(janela, text="Valor:", font=("Arial", 11)).pack()
    entry_valor = tk.Entry(janela, font=("Arial", 11))
    entry_valor.pack(pady=5)

    frame = tk.Frame(janela)
    frame.pack(pady=10)

    moedas = ["BRL", "USD", "EUR"]

    tk.Label(frame, text="De:").grid(row=0, column=0)
    combo_de = ttk.Combobox(frame, values=moedas, width=10)
    combo_de.set("USD")
    combo_de.grid(row=0, column=1, padx=5)

    tk.Label(frame, text="Para:").grid(row=0, column=2)
    combo_para = ttk.Combobox(frame, values=moedas, width=10)
    combo_para.set("BRL")
    combo_para.grid(row=0, column=3, padx=5)

    label_resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"))
    label_resultado.pack(pady=10)

    def realizar_conversao():
        try:
            valor = float(entry_valor.get())
            de = combo_de.get()
            para = combo_para.get()
            resultado = converter(valor, de, para)
            if resultado is not None:
                label_resultado.config(text=f"{valor:.2f} {de} = {resultado:.2f} {para}")
            else:
                messagebox.showerror("Erro", f"Conversão de {de} para {para} não encontrada.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido.")

    tk.Button(janela, text="Converter", font=("Arial", 11, "bold"),
              bg="#2E8B57", fg="white", command=realizar_conversao).pack(pady=5)

    tk.Button(janela, text="⬅️ Voltar", command=mostrar_tela_inicial).pack(pady=10)


def mostrar_tela_temperatura():
    """Tela de conversão de temperatura."""
    limpar_tela()
    tk.Label(janela, text="Conversão de Temperatura 🌡️", font=("Arial", 14, "bold")).pack(pady=15)

    tk.Label(janela, text="Valor:", font=("Arial", 11)).pack()
    entry_valor = tk.Entry(janela, font=("Arial", 11))
    entry_valor.pack(pady=5)

    frame = tk.Frame(janela)
    frame.pack(pady=10)

    temperaturas = ["C", "F", "K"]

    tk.Label(frame, text="De:").grid(row=0, column=0)
    combo_de = ttk.Combobox(frame, values=temperaturas, width=10)
    combo_de.set("C")
    combo_de.grid(row=0, column=1, padx=5)

    tk.Label(frame, text="Para:").grid(row=0, column=2)
    combo_para = ttk.Combobox(frame, values=temperaturas, width=10)
    combo_para.set("F")
    combo_para.grid(row=0, column=3, padx=5)

    label_resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"))
    label_resultado.pack(pady=10)

    def realizar_conversao():
        try:
            valor = float(entry_valor.get())
            de = combo_de.get()
            para = combo_para.get()
            resultado = converter(valor, de, para)
            if resultado is not None:
                label_resultado.config(text=f"{valor:.2f}°{de} = {resultado:.2f}°{para}")
            else:
                messagebox.showerror("Erro", f"Conversão de {de} para {para} não encontrada.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido.")

    tk.Button(janela, text="Converter", font=("Arial", 11, "bold"),
              bg="#1E90FF", fg="white", command=realizar_conversao).pack(pady=5)

    tk.Button(janela, text="⬅️ Voltar", command=mostrar_tela_inicial).pack(pady=10)


def limpar_tela():
    """Remove todos os widgets da janela atual."""
    for widget in janela.winfo_children():
        widget.destroy()


# ======== INICIALIZAÇÃO ========

janela = tk.Tk()
janela.title("Conversor Universal 🌍")
janela.geometry("360x300")

mostrar_tela_inicial()

janela.mainloop()
