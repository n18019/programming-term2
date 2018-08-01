def genlto3():
    yield 1;
    yield 2;
    yield 3;

it = genlto3()

for i in it:
    print(i)
