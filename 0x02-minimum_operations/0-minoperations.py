#!/usr/bin/python3
'''minOperations challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    ND = 1
    # print('H', end='')
    while ND < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = ND
            ND += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * ND), end='')
        elif n - ND > 0 and (n - ND) % ND == 0:
            # copy all and paste
            clipboard = ND
            ND += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * ND), end='')
        elif clipboard > 0:
            # paste
            ND += clipboard
            ops_count += 1
            # print('-(01)->{}'.format('H' * ND), end='')
    # print('')
    return ops_count
