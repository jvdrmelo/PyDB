import sqlite3
import tkinter as tk
from tkinter import messagebox

def inicializando_db():
    conn = sqlite3.connect('Banco_original.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Pessoa
                 (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')
    conn.commit()
    conn.close()

def add_usuario(nome, idade):
    if not nome or not idade:
        messagebox.showwarning("Input Error", "Please provide both name and age")
        return
    
    conn = sqlite3.connect('Banco_original.db')
    c = conn.cursor()
    c.execute("INSERT INTO Pessoa (nome, idade) VALUES (?, ?)", (nome, int(idade)))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso!", "Usuário adicionado!")

def update_usuario(nome, idade):
    if not nome or not idade:
        messagebox.showwarning("Input Error", "Por favor! Isira o Nome ou a Idade na interface")
        return
    
    conn = sqlite3.connect('Banco_original.db')
    c = conn.cursor()
    c.execute("UPDATE Pessoa SET idade = ? WHERE nome = ?", (int(idade), nome))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso!", "Usuário adicionado!")

def del_usuario(nome):
    if not nome:
        messagebox.showwarning("Input Error", "Por favor, insira um nome!")
        return
    
    conn = sqlite3.connect('Banco_original.db')
    c = conn.cursor()
    c.execute("DELETE FROM Pessoa WHERE nome = ?", (nome,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso!", "Usuário deletado!")

def visualizar_usuarios():
    conn = sqlite3.connect('Banco_original.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Pessoa")
    rows = c.fetchall()
    conn.close()

    user_list = "Users:\n"
    for row in rows:
        user_list += f"ID: {row[0]}, Nome: {row[1]}, Idade: {row[2]}\n"
    
    messagebox.showinfo("User List", user_list)

def gui():
    window = tk.Tk()
    window.title("SQLite CRUD com GUI")
    window.geometry("600x300")

    # Frame for the form
    form_frame = tk.Frame(window)
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Nome").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="Idade").grid(row=1, column=0, padx=5, pady=5)

    name_entry = tk.Entry(form_frame)
    age_entry = tk.Entry(form_frame)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    age_entry.grid(row=1, column=1, padx=5, pady=5)

    # Frame for the buttons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Add um Usuário", command=lambda: add_usuario(name_entry.get(), age_entry.get())).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Update do Usuário", command=lambda: update_usuario(name_entry.get(), age_entry.get())).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(button_frame, text="Deletar um usuário (procure pelo nome)", command=lambda: del_usuario(name_entry.get())).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(button_frame, text="Visualizar os usuários", command=visualizar_usuarios).grid(row=0, column=3, padx=5, pady=5)

    window.mainloop()

inicializando_db()
gui()
