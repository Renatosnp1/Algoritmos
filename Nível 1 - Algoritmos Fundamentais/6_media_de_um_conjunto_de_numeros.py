# Média de um Conjunto de Números

# Soma todos os números e divide pela quantidade total.
# Complexidade: O(n)
# Exemplo: Calcular a média das notas de uma turma.

def media_conjunto(numeros: list[float]) -> float:
    """
    Calcula a média de um conjunto de números.
    Parâmetros:
        numeros (list[float]): Lista contendo números (inteiros ou floats).
    Retorna:
        float: A média dos números na lista.
    Complexidade:
        O(n) - Itera uma vez sobre a lista para calcular a soma dos elementos.
    Exceções:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia.")

    soma = sum(numeros)    # A função sum itera sobre a lista, resultando em O(n)
    quantidade = len(numeros)  # len() é O(1) em Python
    return soma / quantidade


if __name__ == "__main__":
    conjunto = [10, 20, 30, 40, 50]
    media = media_conjunto(conjunto)
    print(f"A média do conjunto {conjunto} é {media}")
