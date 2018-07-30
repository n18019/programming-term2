# 畳を平米に変換

def convert_jpu(jou, unit='江戸門'):
    '''
    parameters
    ----------
    jou : int or float
         面積
    unit : str
          たたみの種類
    Returns
    -------
    無し
    '''

    if unit == '江戸門':
        base = 0.88 * 1.76
    elif unit == '京間':
        base == 0.955 * 1.91
    elif unit == '中京間':
        base = 0.91 * 1.82
    m2 = jou * base
    s = '{0}で{1}畳は{2}㎡'.format(unit, jou, m2)
    print(s)

# 関数を実行
convert_jpu(6, '江戸門')
convert_jpu(6, '京間')
convert_jpu(6)
