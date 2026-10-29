import tkinter as tk
# Criação da janela principal
# root = tk.Tk()
# root.title('Olá!')
# root.geometry('800x600+100+300') # Especifica o tamnho da janela em pixel
# root.resizable(True,False) # Comando que libera ou impede de modificar o tamanho da janela

# # Rótulo simples
# label = tk.Label(root, text=f'Wallace Duarte\n Criando primeira janela usando TkInter.')
# label.pack()

# label1 = tk.Label(root, text='Qual seu nome?', bg='gray')
# label1.pack(side=tk.LEFT, padx=10, pady=10)

# label2 = tk.Label(root, text='Wallace', bg='green')
# label2.pack(side=tk.LEFT, padx=10, pady=10)


# Início do loop da janela principal
# root.mainloop()

# Criando uma janela que recebe o nome e mostra uma saludação
# root = tk.Tk()
# root.title('Janela de boas vindas.')
# root.geometry('800x600')

# label = tk.Label(root, text='Digite seu nome: ')
# label.pack()
# entrada = tk.Entry(root)
# entrada.pack()

# def exibir_nome():
#     nome = entrada.get()
#     # print(f'Nome digitado: {nome}') # recebe e imprimi no terminal
#     saudacao = tk.Label(root, text=f"Olá, {nome}")
#     saudacao.pack()
    
# botao = tk.Button(root, text='Enviar', command=exibir_nome)
# botao.pack()

# root.mainloop()

## Cirando uma calculadora com interface baisca
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Minha Calculadora")
root.geometry("350x400")
root.resizable(False, False)

# 2. Título da calculadora
titulo = tk.Label(
        root,
    text="Calculadora Básica",
    font=("Arial", 18, "bold")
)
titulo.pack()

label_num1 = tk.Label(root, text="Digite o primeiro número:").pack()

entrada_num1 = tk.Entry(root)
entrada_num1.pack()

label_num2 = tk.Label(root, text="Digite o segundo número:").pack()

entrada_num2 = tk.Entry(root)
entrada_num2.pack()

def calcular(operacao):
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                resultado_label.config(
                    text="Erro: divisão por zero!"
                )
                return
            resultado = num1 / num2
        resultado_label.config(
            text=f"Resultado: {resultado:g}"
        )
    except ValueError:
        # Comando para criar uma janela que motrará o erro
        
        messagebox.askretrycancel(title='Erro!', message="Digite números válidos!")

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=20)

botao_somar = tk.Button(
    frame_botoes,
    text="+",
    width=5,
    command=lambda: calcular("+")
)
botao_somar.grid(row=0, column=0, padx=5)

botao_subtrair = tk.Button(
    frame_botoes,
    text="-",
    width=5,
    command=lambda: calcular("-")
)
botao_subtrair.grid(row=0, column=1, padx=5)

botao_multiplicar = tk.Button(
    frame_botoes,
    text="×",
    width=5,
    command=lambda: calcular("*")
)
botao_multiplicar.grid(row=1, column=0, padx=5, pady=8)

botao_dividir = tk.Button(
    frame_botoes,
    text="÷",
    width=5,
    command=lambda: calcular("/")
)
botao_dividir.grid(row=1, column=1, padx=5, pady=8)

resultado_label = tk.Label(
    root,
    text="Resultado: ",
    font=("Arial", 12, "bold")
)
resultado_label.pack()

root.mainloop()
