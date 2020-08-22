import os
import time

def adicao_function():
    x = int(input("Digite o valor X:"))
    y = int(input("Digite o valor Y:"))
    resultado = x + y
    print("Equacao: ",x,"+",y,"=",resultado)
    time.sleep(5)
    return True