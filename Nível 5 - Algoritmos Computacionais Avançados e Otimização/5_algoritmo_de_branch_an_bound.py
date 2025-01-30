# Ordenação por Bolha (Bubble Sort)

# Compara e troca elementos adjacentes repetidamente até a lista estar ordenada.
# Complexidade: O(n²)
# Exemplo: Ordenar uma lista de preços de produtos.

lista_numeros = [816, 529, 715, 922, 691, 811, 242, 685, 537, 383, 
                     797, 981, 339, 415, 593, 351, 933, 720, 906, 135, 
                     713, 582, 523, 592, 922, 589, 364, 882, 245, 132, 
                     989, 114, 457, 998, 131, 409, 549, 828, 308, 268, 
                     101, 802, 179, 673, 793, 167, 944, 253, 611, 481, 
                     852, 782, 291, 739, 513, 785, 742, 382, 728, 207, 
                     777, 793, 573, 746, 928, 552, 608, 987, 691, 116, 
                     503, 400, 741, 447, 672, 322, 168, 432, 628, 340, 
                     813, 118, 902, 657, 722, 556, 403, 636, 624, 965]

n = len(lista_numeros)

swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if lista_numeros[i] > lista_numeros[i + 1]:  # Se estiver fora de ordem, troca
            lista_numeros[i], lista_numeros[i + 1] = lista_numeros[i + 1], lista_numeros[i]
            swapped = True  # Indica que houve troca


print(lista_numeros)