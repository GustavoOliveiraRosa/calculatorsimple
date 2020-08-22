import os
import time

from inicio import menu

## Definindo página inicial
## Limpando terminal
os.system("clear")
## Exibindo tela de menu para o usuario
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
print("\033[;1m\033[1;97mOFICIAL SIMPLE CALCULATOR - https://github.com/GustavoOliveiraRosa/calculatorsimple \033[0;0m")
print("\033[1;36m--------------------------------------------\n\033[0;0m")
time.sleep(3)
menu()