import tkinter as tk

# Função para adicionar despesas
def adicionar_despesas():
 descricao = entrada_descricao.get()
 valor = float(entrada_valor.get())
 lista_despesas.insert(tk.END, f"{descricao}: R$ {valor:.2f}")
 calcular_total()
 
# Função para calcular o total das despesas
def calcular_total():
 total = 0.0
 for item in lista_despesas.get(0, tk.END):
  _, valor = item.split(": R$")
  total += float(valor)
 resultado_total.config(text=f"Total: R${total: .2f}")
 

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora de Despesas")

# Criar elementos da interface, como rótulos, campos de entrada, botões, etc.
rotulo_descricao = tk.Label(janela, text="Descrição")
entrada_descricao = tk.Entry(janela)

rotulo_valor = tk.Label(janela, text="Valor")
entrada_valor = tk.Entry(janela)

botao_adicionar = tk.Button(janela, text="Adicionar Despesa", command=adicionar_despesas)
botao_calcular_total = tk.Button(janela, text="Calcular Total", command=calcular_total)

lista_despesas = tk.Listbox(janela)

# Organizar os elementos na janela
rotulo_descricao.pack()
entrada_descricao.pack()
rotulo_valor.pack()
entrada_valor.pack()
botao_adicionar.pack()
botao_calcular_total.pack()
lista_despesas.pack()

resultado_total = tk.Label(janela, text="Total: R$ 0.00")
resultado_total.pack()

# Iniciar a interface gráfica
janela.mainloop()