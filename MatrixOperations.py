import numpy as np
m1 = [[2,3,4],[7,9,2],[5,7,9]]
m2 = [[1,4/2,3],[1,2,3],[1,2,3]]
def Matrix_Mult(matrix1, matrix2):
	matrix1 = np.array(matrix1, float)
	matrix2 = np.array(matrix2, float)
	m = len(matrix1)
	n = len(matrix1[0])
	p = len(matrix2[0])
	result_mat = np.ndarray((m,p), dtype=float)

	if(n!=len(matrix2)):
		print("Can't be Multiplied.")
		exit()

	i = j = 0
	while(i<m):
		j=0
		while(j<p):
			k=0
			result_element=0
			while(k<n):
				result_element = result_element+(matrix1[i][k]*matrix2[k][j])
				k+=1
			result_mat[i][j] = result_element
			j+=1
		i+=1

	return result_mat

def MatrixScalarMult(scalar, matrix):
	i=j=0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j]=scalar*matrix[i][j]
	return np.array(matrix, float)

def MatrixAddition(mat1, mat2):
	try:
		result_mat = np.array(mat1, float) + np.array(mat2, float)
		return np.around(result_mat, decimals=1)
	except:
		return "Error occured. Take a look at the matrices."

def Determinant(mat1):
	try:
		np.set_printoptions(precision=1, floatmode='fixed')
		print(np.linalg.det(mat1))
		return 
	except:
		return "Error occured, take a look at your matrix."

# print(Matrix_Mult(m1,m2))
# print(MatrixScalarMult(2, m1))
print(MatrixAddition(m1, m2))
print(Determinant(m1))