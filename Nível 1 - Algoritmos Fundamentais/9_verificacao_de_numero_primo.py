# Verificação de Número Primo

# Verifica se um número é divisível apenas por 1 e por ele mesmo.
# Complexidade: O(√n)
# Exemplo: Checar se 17 é primo.

import math

def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.
    Parâmetros:
        n (int): Número inteiro a ser verificado.
    Retorna:
        bool: True se n for primo, False caso contrário.
    Complexidade:
        O(√n) - Verifica divisores de 2 até a raiz quadrada de n.
    """
    if n <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    if n <= 3:
        return True   # 2 e 3 são primos
    if n % 2 == 0 or n % 3 == 0:
        return False  # Elimina múltiplos de 2 e 3

    # Verifica divisores de 5 até √n, pulando números pares e múltiplos de 3.
    limite = int(math.sqrt(n)) + 1
    for i in range(5, limite, 2):
        if n % i == 0:
            return False
    return True


# Exemplo de utilização
if __name__ == "__main__":
    numeros_para_testar = [1, 2, 3, 4, 16, 17, 18, 19, 20, 23, 29, 31]
    for numero in numeros_para_testar:
        resultado = "primo" if is_prime(numero) else "não primo"
        print(f"O número {numero} é {resultado}.")
