# Função que inverte a palavra desejada
def inverte(string):
    tamanho = len(string)
    invertida = ""
    for i in range(tamanho-1, -1, -1):
        invertida += string[i]
    print(invertida)


# Usuário digita a palavra que deseja inverter
palavra = input("Digite a palavra que deseja inverter: ")

# Executa a função utilizando a palavra desejada
inverte(palavra)
