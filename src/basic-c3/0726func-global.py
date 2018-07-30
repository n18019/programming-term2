# 関数の外側でvalueに１００を代入

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
    # valueをグラーバル宣言
    global value
    #関数の内側でvalueを変更
    value = 20

changeValue()
value = 100
print('value=',value)
