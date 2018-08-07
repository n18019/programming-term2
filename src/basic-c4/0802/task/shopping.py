from calc_tax import calc_incl_tax as ctx

def exec():
    """
    メインロジックを実行する
    Parameters
    ----------
    なし
    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    # 単価を管理するdictionary
    unit_dc = {
        'Banana': 100,
        'Apple': 200,
        'Orange': 150
    }
    # 個数を管理するdictionary
    nums_dc = {
        'Banana': 2,
        'Apple': 1,
        'Orange': 3
    }
    money = 2000    # 所持金
    res_list = []   # 結果として返すリスト
    money_list = [] # お金の合計を求めるためのリスト
    res_list.append("所持金2000円")
    for name, price in unit_dc.items():
        kazu = nums_dc[name]
        ryoukin = price * kazu
        money_list.append(ryoukin)
        s = "{}を{}個買いました。商品計{}円です。".format(name, kazu, ryoukin)
        res_list.append(s)
    total = sum(money_list)
    tax_v = round(ctx(total))
    kk = "税抜き総額{}円、消費税込み{}円です。".format(total, tax_v)
    res_list.append(kk)
    pp = '残金は{}円です。'.format(money-tax_v)
    res_list.append(pp)

    return res_list


def display(msgs):
    """
    結果を表示する
    Parameters
    ----------
    msgs: list
        表示するメッセージが格納されたリスト
    Returns
    -------
    なし
    """
    print("\n".join(msgs))

# メイン処理
if __name__ == '__main__':
    display(exec())
