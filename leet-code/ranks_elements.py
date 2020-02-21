def solution(s):
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 0
    max_int = max(caracteres_ordenados)

    for caracter in caracteres_ordenados:

        superior = caracter + 1

        if caracter != max_int:
            caracter_anterior = caracter
            for i in caracteres_ordenados:
                if i == superior:
                    contagem += 1

    return contagem


if __name__ == '__main__':
    s = [4,4,3,3,1,0]
    print(solution(s))
    a = [3,4,3,0,2,2,3,0,0]
    print(solution(a))

