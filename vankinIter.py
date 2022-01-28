
def vankinIter(A):
    n = len(A)
    highest = A[n-1][n-1] 

    for i in range(1, n):
	    A[0][i] = max(A[0][i], A[0][i - 1] + A[0][i])
    if highest < A[0][n-1]:
        highest = A[0][n-1]

    for j in range(1, n):
        A[j][0] = max(A[j][0], A[j - 1][0] + A[j][0])
        
    if highest < A[n-1][0]:
        highest = A[n-1][0]
        
    for k in range(1, n):
        for l in range(1, n):
            A[k][l] = max(A[k][l], A[k - 1][l] + A[k][l], A[k][l - 1] + A[k][l])
            if highest < A[k][l]:
                highest = A[k][l]
    return highest
    
A = [[-1, 7, -8, 10, -5], [-4, -9, 8, -6, 0], [5, -2, -6, -6, 7], [-7, 4, 7, -3, -3], [7, 1, -6, 4, -9]]

print(vankinIter(A))
