rps = int

def addlogin():
    id = input("Insira qual aplicativo/site irá usar o login:")
    name = input("Insira o nome do usuário:")
    password = input("Insira a senha do usuário")
    outro = input("Gostaria de colocar alguma descrição do login?:").lower()
    if outro == "sim":
        print("descrição")
while True:
    senha=int(input("Bem vindo bruno, por favor, coloque sua senha:"))
    if senha == 12345:
            print("GERENCIADOR DE LOGINS") # a partir dessa linha até a linha 16 é o menu principal 
            print("1.Checar login\n")
            print("2.Adicionar login\n")
            print("3.Deletar login")
            rps = input("Digite sua opção:")
            if rps == 2:
                addlogin()
