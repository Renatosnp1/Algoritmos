# Contagem de Elementos em uma Lista

# Percorre a lista e conta quantas vezes determinado valor aparece.
# Complexidade: O(n)
# Exemplo: Contar quantas vezes "banana" aparece em uma lista de compras.

def contagem_elementos(lista: list) -> dict:
    """
    Realiza a contagem de ocorrências de cada elemento em uma lista.
    Parâmetros:
        lista (list): Lista de elementos.
    Retorna:
        dict: Um dicionário onde as chaves são os elementos da lista
              e os valores são as respectivas quantidades de ocorrência.
    Complexidade:
        O(n) - A função itera uma única vez sobre a lista.
    """
    contagem = {}
    for elemento in lista:
        contagem[elemento] = contagem.get(elemento, 0) + 1
    return contagem


if __name__ == "__main__":
    exemplo_lista = [3, 1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 1]
    resultado = contagem_elementos(exemplo_lista)
    print("Contagem dos elementos:", resultado)
