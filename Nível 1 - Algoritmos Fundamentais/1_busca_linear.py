# Busca Linear

# Percorre uma lista de elementos um a um até encontrar o valor desejado.
# Complexidade: O(n)
# Exemplo: Buscar um número dentro de uma lista desordenada.

lista_num_aleatorio = [816, 529, 715, 922, 691, 811, 242, 685, 537, 383, 
                       797, 981, 339, 415, 593, 351, 933, 720, 906, 135, 
                       713, 582, 523, 592, 922, 589, 364, 882, 245, 132, 
                       989, 114, 457, 998, 131, 409, 549, 828, 308, 268, 
                       101, 802, 179, 673, 793, 167, 944, 253, 611, 481, 
                       852, 782, 291, 739, 513, 785, 742, 382, 728, 207, 
                       777, 793, 573, 746, 928, 552, 608, 987, 691, 116, 
                       503, 400, 741, 447, 672, 322, 168, 432, 628, 340, 
                       813, 118, 902, 657, 722, 556, 403, 636, 624, 965]

busca = 777

for i in range(len(lista_num_aleatorio)):
    if lista_num_aleatorio[i] == busca:
        print(f"O número {busca} foi encontrado na posição {i}")
        break