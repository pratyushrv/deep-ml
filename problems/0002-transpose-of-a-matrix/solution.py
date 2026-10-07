def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # ans=np.array(a)
    # return np.transpose((a)).tolist()
    pass
    temp=[[0 for i in a] for j in a[0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            temp[j][i]=(a[i][j])
    return temp