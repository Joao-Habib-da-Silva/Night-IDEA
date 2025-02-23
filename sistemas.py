import os as os
def tente():
    valor = input("Diga o diretório aqui...")
    nome = input("Nome da pasta")
    os.chdir(valor)
    os.mkdir(nome)
    print("feito!")
tente()
sim = input("Precisa criar mais um arquivo ou não?")
if sim == "não":
    print("Tchau!!!")
if sim == "sim" or sim == 'Sim':
    tente()