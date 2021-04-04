import os
import time

tensao=0.0
corrente=0.001
resistencia=0.0
prefixo=""

def ajustprefixo(resistencia):
    if resistencia>=1000 and resistencia<10**6:
        resistencia=resistencia/1000
        prefixo="K"
    elif resistencia>=10**6:
        resistencia=resistencia/10**6
        prefixo="M"
    else:
        prefixo=""
    return resistencia,prefixo

while(corrente>0):
    os.system("clear")
    print("Digite a corrente e a tensão para o calculo da resistência.")
    print("Caso deseje encerrar digite 0 para a corrente.")
    corrente=float(input("Digite a corrente: "))
    if corrente==0:
        print("Finalizando!")
        time.sleep(2)
        os.system("clear")
        break
    tensao=float(input("Digite a tensão: "))
    resistencia=tensao/corrente
    resistencia,prefixo=ajustprefixo(resistencia)
    print("A Resistência é: %.2f %s ohms"%(resistencia,prefixo))
    time.sleep(5)
