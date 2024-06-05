import sqlite3
import tkinter as tk
from tkinter import messagebox

def inicializando_db():
    conn = sqlite3.connect('Escola.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Aluno
                 (id INTEGER PRIMARY KEY, nome TEXT, curso TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Professor
                 (id INTEGER PRIMARY KEY, nome TEXT, curso TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Cursos
                 (id INTEGER PRIMARY KEY, nome TEXT, disciplinas TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Disciplinas
                 (id INTEGER PRIMARY KEY, nome TEXT, curso TEXT)''')
    conn.commit()
    conn.close()

def add_aluno(nome, curso):
    if not nome or not curso:
        messagebox.showwarning("Input Error", "Please provide both name and age")
        return
    
    conn = sqlite3.connect('Escola.db')
    c = conn.cursor()
    c.execute("INSERT INTO Aluno (nome, curso) VALUES (?, ?)", (nome, curso))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso!", "Aluno adicionado!")




def visualizar_usuarios():
    conn = sqlite3.connect('Banco_original.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Aluno")
    rows = c.fetchall()
    conn.close()

    user_list = "Alunos:\n"
    for row in rows:
        user_list += f"ID: {row[0]}, Nome: {row[1]}, Curso: {row[2]}\n"
    
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
    curso_entry = tk.Entry(form_frame)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    curso_entry.grid(row=1, column=1, padx=5, pady=5)

    # Frame for the buttons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Add um Aluno", command=lambda: add_aluno(name_entry.get(), curso_entry.get())).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Visualizar os usuários", command=visualizar_usuarios).grid(row=0, column=3, padx=5, pady=5)

    window.mainloop()

inicializando_db()
gui()