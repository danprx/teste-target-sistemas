# Função que calcula a sequência Fibonacci e verifica se o número desejado está ou não na sequência
def fibonacci(n):
    fibo = 0
    aux1 = 0
    aux2 = 1

    while fibo < n:
        fibo = aux1 + aux2
        aux1 = aux2
        aux2 = fibo
        print(fibo)

    if fibo == n:
        print("Seu número pertence à sequência Fibonacci! :D ")
    else:
        print("Seu não pertence à sequência Fibonacci! :(")


# Usuário digita o número que deseja verificar
numero = int(input("Escolha um número para verificar se está ou não na sequência Fibonnacci: "))

# Executa a função Fibonacci com o número escolhido e retorna o resultado
fibonacci(numero)
