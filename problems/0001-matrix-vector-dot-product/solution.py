def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]):
	temple=[0 for k in a]
	if len(a[0])==len(b):
		for i in range(len(a)):
			temp=0
			for j in range(len(a[i])):
				temp+=a[i][j]*b[j]
			temple[i]=temp
		return temple
	else:
		return -1
	pass