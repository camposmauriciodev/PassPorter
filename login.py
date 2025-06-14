bd = []
confLogin = False

conf = int(input("Olá, já possui cadastro? Digite 1 e faça login. Não possui? Digite 0 e se cadastre agora!\n"))
match conf:
    case 0:
        user = input("Digite um usuário válido: ")
        password = input("Digite uma senha válida: ")
        cadastro = {
            'user': user,
            'password': password
        }
        bd.append(cadastro)
        while confLogin == False:
            login = input("Login: ")
            senha = input("Senha: ")
            for i in bd:
                if i['user'] == login and i['password'] == senha:
                    confLogin = True
                else:
                    print("Usuário ou senha inválidos, tente novamente!")
                    confLogin = False
    case 1:
        while confLogin == False:
            login = input("Login: ")
            senha = input("Senha: ")
            for i in bd:
                if i['user'] == login and i['password'] == senha:
                    confLogin = True
                else:
                    print("Usuário ou senha inválidos, tente novamente!")
                    confLogin = False
print("Seja Muito Bem-Vindo!")