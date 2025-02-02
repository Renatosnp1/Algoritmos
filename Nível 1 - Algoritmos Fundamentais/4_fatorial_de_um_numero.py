# Fatorial de um Número (Recursão e Iteração)

# Calcula o produto de todos os números inteiros positivos até n.
# Complexidade: O(n)
# Exemplo: Calcular 5! = 5 × 4 × 3 × 2 × 1.

def fatorial_iterativo(n: int) -> int:
    """
    Calcula o fatorial de n utilizando iteração.
    Parâmetros:
        n (int): Número inteiro não negativo.
    Retorna:
        int: O fatorial de n.
    Complexidade:
        O(n) - Realiza n iterações.
    Exceções:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("n deve ser um inteiro não negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def fatorial_recursivo(n: int) -> int:
    """
    Calcula o fatorial de n utilizando recursão.
    Parâmetros:
        n (int): Número inteiro não negativo.
    Retorna:
        int: O fatorial de n.
    Complexidade:
        O(n) - A função é chamada recursivamente n vezes.
    Exceções:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("n deve ser um inteiro não negativo")
    
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)


# Exemplo de utilização
if __name__ == "__main__":
    numero = 5
    print(f"Fatorial iterativo de {numero}: {fatorial_iterativo(numero)}")
    print(f"Fatorial recursivo de {numero}: {fatorial_recursivo(numero)}")
