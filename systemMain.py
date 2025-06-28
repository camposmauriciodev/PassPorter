import tkinter as tk
from loginPage import LoginPage
from registerPage import RegisterPage

class SystemPage:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("System")
        self.loginWindow = None
        self.registerWindow = None

        # Centraliza janela
        larguraT = self.janela.winfo_screenwidth()
        alturaT = self.janela.winfo_screenheight()
        # larguraJ = 900
        # alturaJ = 700
        # x = (larguraT - larguraJ) // 2
        # y = (alturaT - alturaJ) // 2
        self.janela.geometry(f"{larguraT}x{alturaT}")

        # Frame Bem-Vindo
        frameHead = tk.Frame(self.janela, height=300, bg="#003856")
        frameHead.pack(side="top", fill="both", expand=True)
        self.welcomeLabel = tk.Label(frameHead, text="Olá Admin!", font=("Segoe UI", 30, "bold"), bg="#003856", fg="white")
        self.welcomeLabel.place(relx=0.5, rely=0.5, anchor="center")
        sairButton = tk.Button(frameHead, 
                                 text="Sair", 
                                 font=("Helvetica", 18, "bold"), 
                                 bg="#C93838", fg="#ffffff", 
                                 borderwidth=0, highlightthickness=0, 
                                 relief="flat",
                                 width=6,
                                 height=1,
                                 command=self.sair)
        sairButton.place(relx=0.5, rely=0.6, anchor="center")

    def abrirLogin(self):
        if self.registerWindow and self.registerWindow.winfo_exists():
            self.registerWindow.destroy()
        if self.loginWindow and self.loginWindow.winfo_exists():
            self.loginWindow.deiconify()
        else:
            self.loginWindow = LoginPage(self.janela,
                                         lambda nomeUser: self.mostrarSystem(nomeUser),
                                         self.abrirRegister)
        self.janela.withdraw() #Esconde a tela do sistema

    def abrirRegister(self):
        if self.loginWindow and self.loginWindow.winfo_exists():
            self.loginWindow.withdraw()
        if self.registerWindow and self.registerWindow.winfo_exists():
            self.registerWindow.deiconify()
        else:
            self.registerWindow = RegisterPage(self.janela,
                                               self.abrirLogin,
                                               lambda nomeUser: self.mostrarSystem(nomeUser))

    def mostrarSystem(self, nomeUser):
        if self.loginWindow and self.loginWindow.winfo_exists():
            self.loginWindow.destroy() #Literalmente destrói a janela
        if self.registerWindow and self.registerWindow.winfo_exists():
            self.registerWindow.destroy()
        self.janela.deiconify() #Mostra a janela do sistema
        self.welcomeLabel.config(text=f"Olá {nomeUser}!")

    def iniciar(self):
        self.abrirLogin()
        self.janela.mainloop()

    def sair(self):
        self.janela.withdraw()
        self.abrirLogin()

if __name__ == "__main__":
    app = SystemPage()
    app.iniciar()