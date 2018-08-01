def gen0dd():
    i = 1
    while i <= 30:
        yield i
        i += 2

it = gen0dd()
for v in it:
    print(v, end=",")
