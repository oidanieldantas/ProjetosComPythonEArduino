import os
import time

qtdn=10
vetor=[]
os.system("clear")
for i in range(0,qtdn):
    print("Digite o", i+1,"o número real...")
    vetor.append(float(input(":> ")))
os.system("clear")
print("A diferença entre o maior (",max(vetor),") e o menor (",min(vetor),") valor é: ",max(vetor)-min(vetor))
