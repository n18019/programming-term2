print('  |  1  2  3  4  5  6  7  8  9')
print('--+---------------------------')
for a in range(1, 10):
    print(' {}|'.format(a), end='')
    for b in range(1, 10):
        print('{:3}'.format(a * b), end='')
    print()
