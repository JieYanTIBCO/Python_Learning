# list = [13,-4,2,4,7,5,3,1,9,9,11,17,-8]
# sum = 15
# to find pair from list, their sum ==15.
# scan list one by one, check/search the rest(sum-element) see if it is in the hash set.
# if it can not be found, add this element into hash set, and continue.
# if it is found, return true and two as tuple.


def two_sum(lst, sum):
    set1 = set()
    for i in lst:
        if (sum-i) in set1:
            return (i, sum-i)  # type: ignore
        set1.add(i)
    return None


lst = [13, -4, 2, 4, 7, 5, 3, 1, 9, 9, 11, 17, -8]
sum = 15

print(two_sum(lst, sum))
