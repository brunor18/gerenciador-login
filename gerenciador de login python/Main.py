import mysql.connector
import os

dados_conexao = mysql.connector.connect(
    user='root',
    password="",
    host="localhost",
    database="logins"
)
cursor = dados_conexao.cursor()



def addlogin(): #adicionar login
    global id
    global name 
    global password 
    global outro
    

    id = input("Insira qual aplicativo/site irá usar o login:")
    name = input("Insira o nome do usuário:")
    password = input("Insira a senha do usuário:")
    outro = input("Coloque uma descrição sobre o login:")
    os.system("cls")
    print("Login adicionado com sucesso")

    adLogin = f'INSERT INTO logins_usuario(Nome_app, Nome, Senha, Descricao) VALUES ("{id}", "{name}", "{password}", "{outro}")'
    cursor.execute(adLogin)
    dados_conexao.commit()


                            
def deletar():  ## deletar login
    global kf
    kf = input("Insira o id do login para deletar:").lower()
    removerLogin = f'DELETE FROM logins_usuario WHERE id_Login = "{kf}"'
    cursor.execute(removerLogin)
    dados_conexao.commit()
    os.system("cls")
    print("Login deletado com sucesso")

def check_do_login():
    while True:
        checkLogin = f'SELECT * FROM logins_usuario'
        cursor.execute(checkLogin)
        leitura = cursor.fetchall()
        print("Aplicativo/Site | Usuário | Senha | Descrição | ID")
        print(leitura,'\n')
        exit = input("Pressione 1 para sair:")
        if exit == "1":
            os.system("cls")
            break
        else:
            print("Opção inválida")


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

menu_principal()

cursor.close()
dados_conexao.close()