# 関数の外側でvalueに１００を代入
value = 100

def changeValue():
    '''
    値を変更する
     
     Parameters
     -----------
     なし

    Return
    ------
    なし
    '''
    #関数の内側でvalueを変更
    value = 20

changeValue()
print('value=',value)
