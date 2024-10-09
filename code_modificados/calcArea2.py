import math

def calcular_area_circulo(raio):
    return math.pi * raio**2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_retangulo(largura, altura):
    return largura * altura

def main():
    while True:
        print("Escolha a forma geométrica para calcular a área:")
        print("1. Círculo")
        print("2. Triângulo")
        print("3. Retângulo")
        print("4. Sair")
        
        escolha = input("Digite o número da sua escolha: ")
        
        if escolha == '1':
            try:
                raio = float(input("Digite o raio do círculo: "))
                area = calcular_area_circulo(raio)
                print(f"A área do círculo é: {area:.2f}")
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
        
        elif escolha == '2':
            try:
                base = float(input("Digite a base do triângulo: "))
                altura = float(input("Digite a altura do triângulo: "))
                area = calcular_area_triangulo(base, altura)
                print(f"A área do triângulo é: {area:.2f}")
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
        
        elif escolha == '3':
            try:
                largura = float(input("Digite a largura do retângulo: "))
                altura = float(input("Digite a altura do retângulo: "))
                area = calcular_area_retangulo(largura, altura)
                print(f"A área do retângulo é: {area:.2f}")
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
        
        elif escolha == '4':
            print("Saindo...")
            break
        
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()