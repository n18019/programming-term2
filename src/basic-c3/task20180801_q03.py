fee = [13600, 14500, 16000, 11111, 11667]
# 消費税率
TAX_RATE = 8
tax = (1 + TAX_RATE / 100)

tax_v = lambda v: round(round((v * tax), -1))


print(list(map(tax_v, fee)))
