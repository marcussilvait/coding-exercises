
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
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('marcus'))
    print()
    print(contar_caracteres('banana'))