# 0,1,1,2,3,5
def fin(n: int) -> int:
    memo = dict()
    if n in memo:  # 如果已经计算过，直接取值返回
        return memo[n]

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        memo[n] = fin(n-1) + fin(n-2)
        return memo[n]


print(fin(40))
