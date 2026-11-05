import tkinter as tk

root = tk.Tk()

# Criando um Entry com algumas propriedades
var_texto = tk.StringVar(value="Texto inicial")

entrada = tk.Entry(
    root,
    textvariable=var_texto,
    width=30,
    font=("Helvetica", 11),
    fg="blue",
    bg="lightyellow",
    show="*",  # útil para senha
    relief="sunken",
    bd=3,
    justify="center",
)
entrada.pack(padx=10, pady=10)

root.mainloop()