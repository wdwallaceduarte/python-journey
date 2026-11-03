
import tkinter as tk
from tkinter import messagebox

def login():
    pass

# Programa principal
root = tk.Tk()
root.title('Faça seu Login')
root.geometry('350x400')
root.resizable(False, False)

titulo = tk.Label(
    root,
    text='LOGIN',
    font=('Arial', 18, 'bold')
)
titulo.pack()

# Campo de Login
label_login = tk.Label(root, text='User Name:')
label_login.pack()

entrada_login = tk.Entry(root)
entrada_login.pack()

# Campo de Password
label_password = tk.Label(root, text='Password:')
label_password.pack()

entrada_password = tk.Entry(root, show='•')
entrada_password.pack()

# Campo dos botões
botao_login = tk.Button(root, text='Login', width=10)
botao_login.pack()

botao_cancel = tk.Button(root, text='Cancelar', width=10)
botao_cancel.pack()

root.mainloop()
