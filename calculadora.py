# Calculadora Simples

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

# Loop principal
while True:
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Calculadora encerrada.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Tente novamente.")
        continue

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = somar(a, b)
            print("Resultado:", resultado)

        elif opcao == "2":
            resultado = subtrair(a, b)
            print("Resultado:", resultado)

        elif opcao == "3":
            resultado = multiplicar(a, b)
            print("Resultado:", resultado)

        elif opcao == "4":
            resultado = dividir(a, b)
            print("Resultado:", resultado)

    except ValueError:
        print("Erro: Digite apenas números!")