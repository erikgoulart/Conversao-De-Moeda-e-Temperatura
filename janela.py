import tkinter as tk
from tkinter import ttk, messagebox
from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius, converter_moeda

class ConversorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor - Temperatura & Moeda")
        self.geometry("400x250")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        self.temp_frame = ttk.Frame(notebook)
        self.money_frame = ttk.Frame(notebook)
        notebook.add(self.temp_frame, text="Temperatura")
        notebook.add(self.money_frame, text="Moeda")
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.build_temp_tab()
        self.build_money_tab()

    # Aba de temperatura
    def build_temp_tab(self):
        frm = self.temp_frame
        ttk.Label(frm, text="Valor:").grid(column=0, row=0, padx=5, pady=5)
        self.temp_val = tk.StringVar()
        ttk.Entry(frm, textvariable=self.temp_val).grid(column=1, row=0)
        self.temp_dir = tk.StringVar(value="CtoF")
        ttk.Radiobutton(frm, text="Celsius → Fahrenheit", variable=self.temp_dir, value="CtoF").grid(column=0, row=1, columnspan=2, sticky="w")
        ttk.Radiobutton(frm, text="Fahrenheit → Celsius", variable=self.temp_dir, value="FtoC").grid(column=0, row=2, columnspan=2, sticky="w")
        ttk.Button(frm, text="Converter", command=self.on_convert_temp).grid(column=0, row=3, columnspan=2, pady=10)
        self.temp_result = ttk.Label(frm, text="Resultado: -")
        self.temp_result.grid(column=0, row=4, columnspan=2)

    def on_convert_temp(self):
        try:
            v = float(self.temp_val.get())
            if self.temp_dir.get() == "CtoF":
                r = celsius_para_fahrenheit(v)
                self.temp_result.config(text=f"Resultado: {r:.2f} °F")
            else:
                r = fahrenheit_para_celsius(v)
                self.temp_result.config(text=f"Resultado: {r:.2f} °C")
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido.")

    # Aba de moeda
    def build_money_tab(self):
        frm = self.money_frame
        ttk.Label(frm, text="Valor:").grid(column=0, row=0, padx=5, pady=5)
        self.money_val = tk.StringVar()
        ttk.Entry(frm, textvariable=self.money_val).grid(column=1, row=0)
        ttk.Label(frm, text="De:").grid(column=0, row=1)
        ttk.Label(frm, text="Para:").grid(column=0, row=2)
        currencies = ['BRL', 'USD', 'EUR']
        self.money_from = tk.StringVar(value="USD")
        self.money_to = tk.StringVar(value="BRL")
        ttk.OptionMenu(frm, self.money_from, self.money_from.get(), *currencies).grid(column=1, row=1)
        ttk.OptionMenu(frm, self.money_to, self.money_to.get(), *currencies).grid(column=1, row=2)
        ttk.Button(frm, text="Converter", command=self.on_convert_money).grid(column=0, row=3, columnspan=2, pady=10)
        self.money_result = ttk.Label(frm, text="Resultado: -")
        self.money_result.grid(column=0, row=4, columnspan=2)

    def on_convert_money(self):
        try:
            valor = float(self.money_val.get())
            de = self.money_from.get()
            para = self.money_to.get()
            resultado = converter_moeda(valor, de, para)
            if resultado:
                self.money_result.config(text=f"Resultado: {resultado:.2f} {para}")
            else:
                messagebox.showerror("Erro", f"Conversão não disponível: {de} → {para}")
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido.")

if __name__ == "__main__":
    app = ConversorApp()
    app.mainloop()
