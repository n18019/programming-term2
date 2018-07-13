year = int(input("西暦何年？"))

# うるう年かどうか判定
is_leap = False
# (1) 4で割れたらうるう年 --(1)
if year % 4 == 0:
    # (2) 100で割れたらうるう年ではない--(2)
    if year % 100 == 0:
        # (3) 400で割れたらうるう年--(3)
        if year % 400 == 0:
            is_leap = True
        else:    # ------(3)と対応
            is_leap = False
    else:    # --------(2)と対応
        is_leap = True
else:     # ---------(1)と対応
    is_leap = False

# 結果を表示
if is_leap:    # ---(4)
    print("うるう年です")
else:
    print("平成です")
