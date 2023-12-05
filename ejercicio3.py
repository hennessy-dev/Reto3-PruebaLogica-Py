def encontrar_divisores(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    return divisores

def es_amistoso(num1, num2):
    divisores_num1 = encontrar_divisores(num1)
    divisores_num2 = encontrar_divisores(num2)
    suma_divisores_num1 = sum(divisores_num1)
    suma_divisores_num2 = sum(divisores_num2)
    return suma_divisores_num1 == num2 and suma_divisores_num2 == num1

def imprimir_pares_amistosos(rango_inicial, rango_final):
    for num1 in range(rango_inicial, rango_final + 1):
        for num2 in range(num1 + 1, rango_final + 1):
            if es_amistoso(num1, num2):
                print(f"Los números {num1} y {num2} son amistosos.")

imprimir_pares_amistosos(1000, 1500)
