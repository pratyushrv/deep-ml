def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means=[]
	if mode=='row':
		for i in matrix:
			means.append(sum(i)/len(i))
		return means
	if mode=='column':
		for i in range(len(matrix[0])):
			col=[]
			for j in range(len(matrix)):
				col.append(matrix[j][i])
			means.append(sum(col)/len(col))
		return means