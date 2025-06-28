import tkinter as tk
from tkinter import messagebox
from database import bd

class RegisterPage(tk.Toplevel):
    def __init__(self, parent, callback_login, callback_system):
        super().__init__(parent)
        self.title("System")
        self.callbackLogin = callback_login
        self.callbackSystem = callback_system

        # Centraliza janela
        larguraT = self.winfo_screenwidth()
        alturaT = self.winfo_screenheight()
        larguraJ = 500
        alturaJ = 600
        x = (larguraT - larguraJ) // 2
        y = (alturaT - alturaJ) // 2
        self.geometry(f"{larguraJ}x{alturaJ}+{x}+{y}")

        # Frame do texto
        frameHead = tk.Frame(self, bg="#ffffff", height=150)
        frameHead.pack(side="top", fill="both", expand=True)
        loginLabel = tk.Label(frameHead, text="Crie sua conta", font=("Segoe UI", 30, "bold"), bg="white", fg="#003856")
        loginLabel.place(relx=0.5, rely=0.8, anchor="center")

        #Frame das entrada
        frameEntrys = tk.Frame(self, bg="#ffffff", height=350)
        frameEntrys.pack(side="top", fill="both", expand=True)
        nameLabel = tk.Label(frameEntrys, text="Nome:", font=("Helvetica", 12), bg="white", fg="#003856")
        nameLabel.place(relx=0.1, rely=0.15)
        nameEntry = tk.Entry(frameEntrys, font=("Segoe UI", 12), bg="white")
        nameEntry.place(relx=0.1, rely=0.22, relwidth=0.8)
        userLabel = tk.Label(frameEntrys, text="Usuário:", font=("Helvetica", 12), bg="white", fg="#003856")
        userLabel.place(relx=0.1, rely=0.32)
        userEntry = tk.Entry(frameEntrys, font=("Segoe UI", 12), bg="white")
        userEntry.place(relx=0.1, rely=0.39, relwidth=0.8)
        passwordLabel = tk.Label(frameEntrys, text="Senha:", font=("Helvetica", 12), bg="white", fg="#003856")
        passwordLabel.place(relx=0.1, rely=0.5)
        passwordEntry = tk.Entry(frameEntrys, font=("Segoe UI", 12), bg="white", show="•")
        passwordEntry.place(relx=0.1, rely=0.57, relwidth=0.8)
        voltarloginLink = tk.Label(frameEntrys, text="Já tenho uma conta", font=("Helvetica", 10), fg="#003856", bg="#ffffff", cursor="hand2")
        voltarloginLink.place(relx=0.1, rely=0.7)
        voltarloginLink.bind("<Button-1>", lambda e: self.voltarLogin())

        #Frame do botão
        frameButton = tk.Frame(self, bg="#ffffff", height=100)
        frameButton.pack(side="top", fill="both", expand=True)
        entrarButton = tk.Button(frameButton,
                                 text="Criar", 
                                 font=("Helvetica", 18, "bold"), 
                                 bg="#003856", 
                                 fg="#ffffff", 
                                 borderwidth=0, 
                                 highlightthickness=0, 
                                 relief="flat",
                                 command=lambda: self.confRegister(nameEntry, userEntry, passwordEntry))
        entrarButton.place(relx=0.2, relwidth=0.6, relheight=0.4)

    def confRegister(self, n, u, p):
        name = n.get().strip()
        user = u.get().strip()
        password = p.get().strip()
        if not name or not user or not password:
            messagebox.showerror("Erro!", "Todos os campos são obrigatórios.")
            n.delete(0, tk.END)
            u.delete(0, tk.END)
            p.delete(0, tk.END)
            return
        for i in bd:
            if i['user'] == user:
                messagebox.showerror("Erro!", "Usuário já existente.")
                u.delete(0, tk.END)
                return
        if len(password) < 8:
            messagebox.showerror("Erro!", "A senha deve ter ao menos 8 caracteres.")
            p.delete(0, tk.END)
            return
        elif len(password) > 8:
            messagebox.showerror("Erro!", "A senha deve ter apenas 8 caracteres.")
            p.delete(0, tk.END)
            return
        cadastro = {
            'name': name,
            'user': user,
            'password': password
        }
        bd.append(cadastro)
        self.destroy()
        self.callbackSystem(name)

    def voltarLogin(self):
        self.destroy()
        self.callbackLogin()