def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a)!=len(b):
		return -1
	else:
		sum_list=[]
		for i in range(0,len(a)):
			sum_list.append(a[i]+b[i])
		return sum_list
	pass