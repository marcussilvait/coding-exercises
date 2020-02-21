
def contar_caracteres(s):
    '''Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('marcus')
    {'a': 1, 'c': 1, 'm': 1, 'r': 1, 's': 1, 'u': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    '''

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('marcus'))
    print()
    print(contar_caracteres('banana'))