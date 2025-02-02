# Contagem de Dígitos de um Número

# Conta quantos dígitos um número tem.
# Complexidade: O(log n)
# Exemplo: O número 12345 tem 5 dígitos.

def contar_digitos(numero: int) -> int:
    """
    Conta a quantidade de dígitos de um número inteiro.
    Parâmetros:
        numero (int): Número inteiro (pode ser negativo).
    Retorna:
        int: A quantidade de dígitos do número.
    Complexidade:
        O(log n) - Em cada iteração, o número é dividido por 10, reduzindo
        seu tamanho de forma logarítmica.
    """
    if numero == 0:
        return 1  # O número 0 possui 1 dígito.

    numero = abs(numero)  # Garante que o número seja positivo.
    contador = 0
    while numero:
        contador += 1
        numero //= 10  # Divisão inteira por 10 para remover o último dígito.
    return contador


# Exemplo de utilização
if __name__ == "__main__":
    numeros_para_testar = [0, 7, 12345, -987654321]
    for num in numeros_para_testar:
        print(f"O número {num} possui {contar_digitos(num)} dígitos.")
