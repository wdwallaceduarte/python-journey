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
).pack()

# Campo de Login
label_login = tk.Label(root, text='User Name:').pack()
entrada_login = tk.Entry(root)
entrada_login.pack()

# Campo de Password
label_password = tk.Label(root, text='Password:').pack()
entrada_password = tk.Entry(root, show='•')
entrada_password.pack()



# Campo que criar o botão
botao_login = tk.Button(root, text='Login', width=5).pack(pady=6)
# botao_login.grid(row=0, column=0, padx=5)
botao_cancel = tk.Button(root, text='Cancelar', width=5).pack()
# botao_cancel.grid(row=1, column=0)


root.mainloop()