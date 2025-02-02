# Inversão de String

# Inverte os caracteres de uma string.
# Complexidade: O(n)
# Exemplo: Transformar "python" em "nohtyp".

def inverter_string(texto: str) -> str:
    """
    Inverte uma string utilizando slicing.
    Parâmetros:
        texto (str): A string que será invertida.
    Retorna:
        str: A string invertida.
    Complexidade:
        O(n) - A operação slicing percorre todos os caracteres uma única vez.
    """
    return texto[::-1]


# Exemplo de utilização
if __name__ == "__main__":
    exemplo = "ChatGPT é incrível!"
    resultado = inverter_string(exemplo)
    print(f"String original: {exemplo}")
    print(f"String invertida: {resultado}")
