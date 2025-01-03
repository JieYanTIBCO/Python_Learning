def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


lst = list(range(0, 101))
n = 8

# chunks = list(chunk(lst, 10))


chunks2 = [lst[i:i+n] for i in range(0, len(lst), n)]

print(chunks2)
