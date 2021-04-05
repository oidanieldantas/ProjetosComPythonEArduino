'''

'''
import os
import time

limite=10
os.system("clear")
print("Ordem reversa - Insira 10 números e veja a ordem reversa.")
numeros=[]
for i in range(0,limite):
    numeros.insert(i,float(input("Digite um número: ")))
numero_entrada_orig = numeros.copy()
numeros.reverse()
print("Os números inseridos foram:", numero_entrada_orig)
print("E a ordem inversa da entrada é:", numeros)

''' Fiz este bloco para testar os conceitos de dicionário ''''''
listaDeNumeros={}
for i in range(1,limite+1):
    listaDeNumeros[i]=[]
    listaDeNumeros[i].append(float(input("Digite um número: ")))
print(listaDeNumeros)
for i in range(limite,0,-1):
    print(listaDeNumeros[i])
'''''''''
