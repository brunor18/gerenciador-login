import os
rps = str
desc= str


def addlogin(): #adicionar login
    global id
    global name 
    global password 
    global outro
    global info
    

    id = input("Insira qual aplicativo/site irá usar o login:")
    name = input("Insira o nome do usuário:")
    password = input("Insira a senha do usuário:")
    outro = input("Coloque uma descrição sobre o login:")
    
    
    with open("dadoslogin.txt", 'a', encoding="utf-8") as arquivo:
        info = f"\nSite/app: {id}\n Nome: {name}\n Senha: {password}\n Descrição: {outro}"
        arquivo.write(info)
    
                            
def deletar():  ## deletar login
    global kf
    kf = input("Você deseja mesmo deletar todos os seus logins?:").lower()
    if kf == "sim":
        os.remove("dadoslogin.txt")
        print("Logins deletados com sucesso")   
    if kf == "não" or "nao":
        menu_principal()

def check_do_login():
    while True:
            global pos
            f = open("dadoslogin.txt", "r", encoding="utf-8")
            conteudo = f.read()
            print(conteudo)


            pos = input("Digite 0 para voltar para o menu principal:")
            if pos == "0":
                 break
            else:
                 print("Resposta inválida")




        

def menu_principal():  ## menu principal
    while True:
            print("GERENCIADOR DE LOGINS")
            print("1.Checar login\n")
            print("2.Adicionar login\n")
            print("3.Deletar login")
            print("4.Sair")
            rps = input("Digite sua opção:")
            if rps == "1":
                check_do_login()
            elif rps == "2":
                addlogin()
            elif rps == "3":
                deletar()
            elif rps == "4":
                break
            else:
                print("Opção inválida")


while True: ## usuario coloca senha
    senha =int(input("Bem vindo bruno, por favor, coloque sua senha ou digite 0 para sair:"))
    if senha == 12345:
        menu_principal()
    elif senha == 0:
        break
    else:
        print("Opção inválida")
