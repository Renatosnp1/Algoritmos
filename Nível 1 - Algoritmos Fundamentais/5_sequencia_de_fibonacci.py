# Sequência de Fibonacci (Iterativo e Recursivo)

# Gera a sequência onde cada número é a soma dos dois anteriores.
# Complexidade: O(2ⁿ) (recursivo ingênuo), O(n) (iterativo ou com memoization)
# Exemplo: Determinar o 10º termo da sequência de Fibonacci.

def fibonacci_iterativo(n: int) -> int:
    """
    Calcula o n-ésimo termo da Sequência de Fibonacci utilizando iteração.
    Parâmetros:
        n (int): Posição na sequência (n >= 0).
    Retorna:
        int: O n-ésimo termo da Sequência de Fibonacci.
    Complexidade:
        O(n) - Executa um loop linearmente proporcional a n.
    Exceções:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("n deve ser um inteiro não negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursivo(n: int) -> int:
    """
    Calcula o n-ésimo termo da Sequência de Fibonacci utilizando recursão.
    Parâmetros:
        n (int): Posição na sequência (n >= 0).
    Retorna:
        int: O n-ésimo termo da Sequência de Fibonacci.
    Complexidade:
        O(2ⁿ) - Cada chamada gera duas novas chamadas recursivas (na forma ingênua).
    Exceções:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("n deve ser um inteiro não negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Exemplo de utilização
if __name__ == "__main__":
    posicao = 10  # Exemplo: calcular o 10º termo da sequência
    print(f"Fibonacci iterativo (posição {posicao}): {fibonacci_iterativo(posicao)}")
    print(f"Fibonacci recursivo (posição {posicao}): {fibonacci_recursivo(posicao)}")
