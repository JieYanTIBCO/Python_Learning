def sortdict(lst):
	dict1=dict()
	for element in lst:
		if element not in dict1:
			dict1[element]=1
		else:
			dict1[element]+=1
	return sorted(dict1.items(), key= lambda item: (-item[1],-(item[0][0]+item[0][1]),item[0][0]))

example_list = [(1, 2), (2, 2), (1, 2), (3, 1), (2, 2), (3, 1),(2, 2)]
result = sortdict(example_list)
print(result)