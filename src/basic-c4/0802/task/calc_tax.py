# 消費税率
TAX_RATE = 8

def calc_incl_tax(excl_tax):
    '''
    金額に消費税をプラスさせる

    parameters
    ----------
    excl_tax : int
    消費税をプラスさせる金額

    Return
    ------
    消費税率を金額に掛ける
    '''

    return (1 + TAX_RATE / 100) * excl_tax
