import os
import time

requivalente=0.0
fora=True
while(fora):
    os.system("clear")
    resistores=[0.0,0.0,0.0]
    requivalente=0.0
    print("Cálculo de 3 resistores em Série.")
    print("Se um dos valores do resistore for 0 o programa será encerrado.")
    for i in range(0,len(resistores)):
        print("Dibite o R",i+1)
        resistores.insert(i,float(input("Valor: ")))
        if resistores[i]==0:
            print("Você entrou valor nulo. O programa será finalizado.")
            time.sleep(2)
            fora=False
            break
        requivalente+=resistores[i]
    print("O resistor equivalente é: ", requivalente)
    time.sleep(5)

