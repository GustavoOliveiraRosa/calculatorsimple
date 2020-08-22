import os
from adicao import adicao_function
from subtracao import subtracao_function
from multiplicacao import multiplicacao_function
from divisao import divisao_function


def menu():
    # Após o usuário colocar o nome.

    os.system("clear")

    print("\n")
    print("\033[1;36m--------------------------------------------\033[0;0m")
    print("\033[1;94m")

    print("██╗  ██╗██╗███████╗ ██████╗ ██╗  ██╗ █████╗ ")
    print("██║  ██║██║██╔════╝██╔═══██╗██║ ██╔╝██╔══██╗")
    print("███████║██║███████╗██║   ██║█████╔╝ ███████║")
    print("██╔══██║██║╚════██║██║   ██║██╔═██╗ ██╔══██║")
    print("██║  ██║██║███████║╚██████╔╝██║  ██╗██║  ██║")
    print("╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ - Calculator")
    print("\n\033[0;0m") 
    print("\033[;1m\033[1;97m Seja bem vindo! \033[0;0m \n\n\n\n")
    print("\033[;1m\033[1;97m Escolha uma opção:\033[0;0m \n\n\n\n")
    print("\033[;1m\033[1;97m 1 - Adição \033[0;0m")
    print("\033[;1m\033[1;97m 2 - Subtração \033[0;0m")
    print("\033[;1m\033[1;97m 3 - Multiplicação \033[0;0m")
    print("\033[;1m\033[1;97m 4 - Divisão \033[0;0m")
    print("\033[;1m\033[1;97m 5 - Sair \033[0;0m")
    print("\033[1;36m--------------------------------------------\n\033[0;0m")
    escolha = int(input("Digite uma opção >"))

    # Verificando se o usuário inseriu ou não uma escolha válida.

    if escolha <= 5 and escolha >= 1:

        if escolha == 1:
            comando = adicao_function()
            if comando == True:
                menu()

        if escolha == 2:
            comando = subtracao_function()
            if comando == True:
                menu()


        if escolha == 3:
            comando = multiplicacao_function()
            if comando == True:
                menu()
        
        if escolha == 4:
            comando = divisao_function()
            if comando == True:
                menu()

        if escolha == 5:
            print("Muito obrigado por usar nossa calculadora!")
            exit()

    else:
        menu()

