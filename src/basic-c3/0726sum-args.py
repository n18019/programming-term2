def sumArgs(*args):
    '''
    引数に指定された値を計算する
    
    Parametrs
    ---------
    args : int()
          合計したい数値

    Returns
    -------
    int
        合計された値
    '''
    v = 0
    for n in args:
        v += n
    return v

print(sumArgs(1, 2, 3))
print(sumArgs(1, 2, 3, 4, 5))
print(sumArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
