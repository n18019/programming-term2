def count_s(n):
    '''
    3の倍数と3のつく数字を取る

    Parameters
    ----------
    n : int
        max値が入る
    Return
    ------
    nに１０で割って３あまりのやつを
    また、３で割ってあまり０のやつを
    nにreturn
    '''
    return n // 10 == 3 or n % 3 == 0
# max値をnumsに
nums = range(1, 41)
count_nams = filter(count_s, nums)

print(list(count_nams))
