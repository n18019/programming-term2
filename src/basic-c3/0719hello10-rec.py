# 再帰関数の定義
def say_hello(i):
    '''
    繰り返しの作業
    Parameters
    ----------
    i: int

    Return
    なし
    '''

    if i <= 0:
        return
    print('ハロー', i)
    say_hello(i-1)
say_hello(10)
