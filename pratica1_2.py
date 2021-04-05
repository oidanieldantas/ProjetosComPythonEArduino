import os
import time

os.system("clear")
qtdnome=3
nome=[]
for i in range(0,qtdnome):
    print("Digite o", i+1," nome: ")
    nome.append(input())
nome.sort()
os.system("clear")
print("Os nomes ordenados...")
for i in nome:
    print(i)
    time.sleep(0.5)
print(nome)
