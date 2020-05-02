def somatorio(*lista_de_numeros):
    return sum(lista_de_numeros)

def find_key_with_max_value(**dic):

    key = list(dic.keys())[0]
    value = list(dic.values())[0]

    for k, v in dic.items():
        if v > value:
            value = v
            key = k

    return 'Chave \'{}\' tem o maior valor ({})'.format(key, value)

print('\nVamos somar um número desconhecidos de entradas: ')
print('1,2,3 = ', somatorio(1,2,3))
print('1,2,3,4,5,6 = ', somatorio(1,2,3,4,5,6))
print('31,1,1,5,1,3,5,2,5,2,5,23,5,23 = ', somatorio(31,1,1,5,1,3,5,2,5,2,5,23,5,23))


print('\nVamos achar a chave do argumento com maior valor')

print(
    find_key_with_max_value(
    a = 1,
    b = 3,
    c = 10,
    ad = 131,
    bb = 30,
    dc = 100,
    )
)