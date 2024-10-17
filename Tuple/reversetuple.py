tuples = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
rev_string = ''.join(tuples[::-1])
rev_tuples = tuple(rev_string)
print(*rev_tuples,sep="")

print(rev_string[::-2])