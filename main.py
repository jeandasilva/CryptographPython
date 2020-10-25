import time

from cryptography.fernet import Fernet  # importa módulo de criptografia

alfabeto = "!$%'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_´abcdefghijklmnopqrstuvwxyz{|}~"


def criptografar(mensagem):
    # criptografa a mensagem

    indice_cont = int(len(mensagem) / 2)

    adicional = mensagem.count(mensagem[indice_cont])

    j = 0
    gerarChave()

    file = open('chave.key', 'r')
    chave = file.read()
    file.close()

    file = open('chave.key', 'a')
    file.write(str(adicional))
    file.close()

    cripto = ''

    for i in mensagem:
        if j > 43:
            j = 0

        if chave[j] not in alfabeto:
            j += 1
            continue

        if i in alfabeto:
            indice = alfabeto.index(i)
            cripto += alfabeto[(indice + (alfabeto.index(chave[j]) + adicional)) % len(alfabeto)]
            j += 1
        else:
            cripto += i
    return cripto


def descriptografar(mensagem):
    j = 0
    file = open('chave.key', 'r')
    chave = file.read()
    file.close()

    indice_chave = chave.find('=')

    adicional = int(chave[indice_chave + 1: len(chave)])

    cripto = ''

    for i in mensagem:
        if j > 43:
            j = 0

        if chave[j] not in alfabeto:
            j += 1
            continue
        if i in alfabeto:
            indice = alfabeto.index(i)
            cripto += alfabeto[(indice - (alfabeto.index(chave[j]) + adicional)) % len(alfabeto)]
            j += 1
        else:
            cripto += i
    return cripto


def recebeModo():
    # Função que pergunta se o usuário quer criptografar ou descriptografar

    while True:
        option = input("Deseja criptografar ou descriptografar? ")
        option = option.lower()
        if option == 'c' or option == 'criptografar':
            return 1
        elif option == 'descriptografar' or option == 'd':
            return 2
        print("Entrada inválida. Escolha entre ('criptografar', 'c') ou ('descriptografar', 'd')")


def gerarChave():
    chave = Fernet.generate_key()  # gera uma chave randômica
    file = open('chave.key', 'wb')
    file.write(chave)
    file.close()


def main():
    modo = recebeModo()
    if modo == 1:
        mensagem = list(input("Digite a mensagem: "))
        print(criptografar(mensagem))
    elif modo == 2:
        mensagem = list(input("Digite a mensagem: "))
        print(descriptografar(mensagem))


inicio = time.time()
main()
fim = time.time()
print(fim - inicio)
