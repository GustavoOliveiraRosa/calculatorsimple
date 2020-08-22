import os
import time

def divisao_function():
    x = int(input("Digite o valor X:"))
    y = int(input("Digite o valor Y:"))
    resultado = x / y
    print("Equacao: ",x,"/",y,"=",resultado)
    time.sleep(5)
    return True
