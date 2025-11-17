import tkinter as tk
from tkinter import ttk, messagebox

TAXAS = {
    ("USD", "BRL"): 5.31,
    ("BRL", "USD"): 1/5.50,
    ("EUR", "BRL"): 6.00,
    ("BRL", "EUR"): 1/6.00,
    ("USD", "EUR"): 0.92,
    ("EUR", "USD"): 1/0.92,
}

def fazer_conversao():
    origem = combo_origem.get()
    destino = combo_destino.get()
    valor_txt = entrada_valor.get().replace(",", ".")

    try:
        valor = float(valor_txt)
    except:
        messagebox.showerror("Erro", "Digite um valor válido.")
        return

    if origem == destino:
        resultado = valor
    else:
        chave = (origem, destino)
        if chave not in TAXAS:
            messagebox.showerror("Erro", "Conversão não disponível.")
            return
        resultado = valor * TAXAS[chave]

    lbl_result.config(text=f"{valor} {origem} = {resultado:.2f} {destino}")

janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("300x180")

moedas = ["USD", "BRL", "EUR"]

combo_origem = ttk.Combobox(janela, values=moedas, state="readonly")
combo_origem.set("USD")
combo_origem.pack(pady=5)

combo_destino = ttk.Combobox(janela, values=moedas, state="readonly")
combo_destino.set("BRL")
combo_destino.pack(pady=5)

entrada_valor = tk.Entry(janela)
entrada_valor.pack(pady=5)

btn = tk.Button(janela, text="Converter", command=fazer_conversao)
btn.pack(pady=8)

lbl_result = tk.Label(janela, text="")
lbl_result.pack()

janela.mainloop()