def CRT(nums, rems):

    res = 0
    prod = 1

    for n in nums:
        prod *= n

    for i, n in enumerate(nums):
        pp = prod // n
        res += pp *  rems[i] * pow(pp, -1, n)

    return res % prod