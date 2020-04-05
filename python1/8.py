def print_table(n):

    # first line

    print('   ', end = '')
    for i in range(1, n + 1):
        print('{:4d}'.format(i), end = '')

    print()

    # second line

    print('  :', end = '')
    for _ in range(4*n):
        print('-', end = '')

    print()

    # other n lines
    
    for i in range(1, n + 1):
        print('{:2d}:'.format(i), end = '')
        for j in range(1, n + 1):
            print('{:4d}'.format(i*j), end = '')
        print()

    print()


print_table(14)