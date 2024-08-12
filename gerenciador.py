rps = str
desc= str

def addlogin():
    global id
    global name 
    global password ## aqui eu deixei as variáveis da função como públicas, irei usar elas no futuro
    global outro
    global info
    

    id = input("Insira qual aplicativo/site irá usar o login:")
    name = input("Insira o nome do usuário:")
    password = input("Insira a senha do usuário:")
    outro = input("Coloque uma descrição sobre o login:")
    
    
    with open("dadoslogin.txt", 'a', encoding="utf-8") as arquivo:
        info = f"\nSite/app: {id}\n Nome: {name}\n Senha: {password}\n Descrição: {outro}"
        arquivo.write(info)
    
                            
    ## esse espaço é rservado para as as futuras funções que eu irei adicionar no progama
    

        

def menu_principal():
    while True:
            print("GERENCIADOR DE LOGINS")
            print("1.Checar login\n")
            print("2.Adicionar login\n")
            print("3.Deletar login")
            print("4.Sair")
            rps = input("Digite sua opção:")
            if rps == "2":
                addlogin()
            if rps == "4":
                break

while True:
    senha =int(input("Bem vindo bruno, por favor, coloque sua senha ou digite 0 para sair:"))
    if senha == 12345:
        menu_principal()
    elif senha == 0:
        break
    else:
        print("Opção inválida")
