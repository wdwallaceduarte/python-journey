
# import tkinter as tk
# from tkinter import messagebox

# # Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha Calculadora")
# janela.geometry("340x450")
# janela.resizable(False, False)
# janela.configure(bg="#20232A")

# # Variáveis da calculadora
# expressao = ""

# # Função para adicionar valores ao visor
# def adicionar(valor):
#     global expressao
#     expressao += str(valor)
#     visor_var.set(expressao)

# # Função para limpar o visor
# def limpar():
#     global expressao
#     expressao = ""
#     visor_var.set("")

# # Função para calcular o resultado
# def calcular():
#     global expressao

#     try:
#         resultado = eval(expressao)

#         visor_var.set(str(resultado))
#         expressao = str(resultado)

#     except ZeroDivisionError:
#         messagebox.showerror(
#             "Erro", "Não é possível dividir por zero!"
#         )
#         limpar()

#     except Exception:
#         messagebox.showerror(
#             "Erro", "Digite uma expressão válida!"
#         )
#         limpar()

# # Criar o visor
# visor_var = tk.StringVar()

# visor = tk.Entry(
#     janela,
#     textvariable=visor_var,
#     font=("Arial", 24),
#     justify="right",
#     state="readonly",
#     readonlybackground="#FFFFFF",
#     fg="#20232A",
#     bd=10
# )
# visor.pack(fill="x", padx=15, pady=20, ipady=10)

# # Criar o espaço dos botões
# quadro = tk.Frame(janela, bg="#20232A")
# quadro.pack(expand=True, fill="both", padx=10, pady=5)

# # Lista dos botões
# botoes = [
#     ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
#     ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
#     ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
#     ("C", 3, 0), ("0", 3, 1), ("=", 3, 2), ("+", 3, 3)
# ]

# # Criar os botões automaticamente
# for texto, linha, coluna in botoes:

#     if texto == "C":
#         comando = limpar
#         cor = "#C0392B"

#     elif texto == "=":
#         comando = calcular
#         cor = "#27AE60"

#     elif texto in ["+", "-", "*", "/"]:
#         comando = lambda t=texto: adicionar(t)
#         cor = "#E67E22"

#     else:
#         comando = lambda t=texto: adicionar(t)
#         cor = "#34495E"

#     botao = tk.Button(
#         quadro,
#         text=texto,
#         font=("Arial", 16, "bold"),
#         bg=cor,
#         fg="white",
#         activebackground="#7F8C8D",
#         activeforeground="white",
#         bd=0,
#         command=comando
#     )

#     botao.grid(
#         row=linha,
#         column=coluna,
#         sticky="nsew",
#         padx=4,
#         pady=4
#     )

# # Ajustar o tamanho das linhas e colunas
# for i in range(4):
#     quadro.grid_rowconfigure(i, weight=1)
#     quadro.grid_columnconfigure(i, weight=1)

# # Executar a aplicação
# janela.mainloop()


## OUTRO MODEO DE CALCULADORA


import tkinter as tk

# 1. Criando a janela principal
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
titulo.pack(pady=15)

# 3. Campo para digitar o primeiro número
label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()

entrada_num1 = tk.Entry(root, justify="center")
entrada_num1.pack(pady=5)

# 4. Campo para digitar o segundo número
label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()

entrada_num2 = tk.Entry(root, justify="center")
entrada_num2.pack(pady=5)

# 5. Função para realizar os cálculos
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
        resultado_label.config(
            text="Digite números válidos!"
        )

# 6. Criando os botões das operações
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

# 7. Label para exibir o resultado
resultado_label = tk.Label(
    root,
    text="Resultado: ",
    font=("Arial", 12, "bold")
)
resultado_label.pack(pady=10)

# 8. Mantendo a janela aberta
root.mainloop()

