def validationlist(lst):
    for i in range(len(lst)):
        if not isinstance(lst[i], int) or lst[i] < 0:
            raise ValueError(
                f"The input list[{i}]={lst[i]}, "
                "which is not a non-negative integer!"
            )


a = [1, 2, 3, 4, 5, 7, -1]

try:
    validationlist(a)
    even_num = filter(lambda num: num % 2 != 0, a)
    print(list(even_num))
except Exception as e:
    print(f"Error:{e}")
