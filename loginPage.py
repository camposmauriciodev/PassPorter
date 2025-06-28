import tkinter as tk
from tkinter import messagebox
from database import bd

class LoginPage(tk.Toplevel):
    def __init__(self, parent, callback_system, callback_register):
        super().__init__(parent)
        self.title("System")
        self.parent = parent
        self.callbackSystem = callback_system
        self.callbackRegister = callback_register

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
        loginLabel = tk.Label(frameHead, text="Inicie sua sessão", font=("Segoe UI", 30, "bold"), bg="white", fg="#003856")
        loginLabel.place(relx=0.5, rely=0.8, anchor="center")

        #Frame das entrada
        frameEntrys = tk.Frame(self, bg="#ffffff", height=350)
        frameEntrys.pack(side="top", fill="both", expand=True)
        userLabel = tk.Label(frameEntrys, text="Usuário:", font=("Helvetica", 12), bg="white", fg="#003856")
        userLabel.place(relx=0.1, rely=0.25)
        userEntry = tk.Entry(frameEntrys, font=("Segoe UI", 12), bg="white")
        userEntry.place(relx=0.1, rely=0.32, relwidth=0.8)
        passwordLabel = tk.Label(frameEntrys, text="Senha:", font=("Helvetica", 12), bg="white", fg="#003856")
        passwordLabel.place(relx=0.1, rely=0.4)
        passwordEntry = tk.Entry(frameEntrys, font=("Segoe UI", 12), bg="white", show="•")
        passwordEntry.place(relx=0.1, rely=0.47, relwidth=0.8)
        criarcontaLink = tk.Label(frameEntrys, text="Não tenho uma conta", font=("Helvetica", 10), fg="#003856", bg="#ffffff", cursor="hand2")
        criarcontaLink.place(relx=0.1, rely=0.6)
        criarcontaLink.bind("<Button-1>", lambda e: self.callbackRegister())

        #Frame do botão
        frameButton = tk.Frame(self, bg="#ffffff", height=100)
        frameButton.pack(side="top", fill="both", expand=True)
        entrarButton = tk.Button(frameButton, 
                                 text="Entrar", 
                                 font=("Helvetica", 18, "bold"), 
                                 bg="#003856", fg="#ffffff", 
                                 borderwidth=0, highlightthickness=0, 
                                 relief="flat",
                                 command=lambda: self.confLogin(userEntry, passwordEntry))
        entrarButton.place(relx=0.2, relwidth=0.6, relheight=0.4)

    def confLogin(self, u, p):
        login = u.get()
        senha = p.get()
        if not login.strip() or not senha.strip():
            messagebox.showerror("Erro!", "Todos os campos são obrigatórios.")
            return
        usuarioEncontrado = None
        for i in bd:
            if i['user'] == login and i['password'] == senha:
                usuarioEncontrado = i
                break
        if usuarioEncontrado:
            self.destroy()
            self.callbackSystem(i['name'])
        else:
            messagebox.showerror("Acesso Negado!", "Usuário ou senha incorretos, tente novamente!")
            u.delete(0, tk.END)
            p.delete(0, tk.END)