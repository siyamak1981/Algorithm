# n = 2
# m = 2
# a = [[2,5], [1,7]]
# b = [[3,7], [2,9]]
# c = []
# for i in range(1,4):
#     z = []
#     for j in range(1,4):
#         x = a[i][j] - b[i][j]
#         z.append(x)
#     c.append(z)
        
# for i in range(n):
#     for j in range(m):
#         print(c[i][j], end = " ")
#     print()


# -----------------------------------------------------
# # A basic code for matrix input from user

# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))

# # Initialize matrix
# matrix = []
# print("Enter the entries rowwise:")

# # For user input
# for i in range(R):		 # A for loop for row entries
# 	a =[]
# 	for j in range(C):	 # A for loop for column entries
# 		a.append(int(input()))
# 	matrix.append(a)

# # For printing the matrix
# for i in range(R):
# 	for j in range(C):
# 		print(matrix[i][j], end = " ")
# 	print()

# --------------------------------------------------
# Python program to rotate a matrix
# Function to rotate a matrix
# def rotateMatrix(mat):
# 	if not len(mat):
# 		return
	
# 	"""
# 		top : starting row index
# 		bottom : ending row index
# 		left : starting column index
# 		right : ending column index
# 	"""

# 	top = 0
# 	bottom = len(mat)-1

# 	left = 0
# 	right = len(mat[0])-1

# 	while left < right and top < bottom:

# 		# Store the first element of next row,
# 		# this element will replace first element of
# 		# current row
# 		prev = mat[top+1][left] # 5 10 6 7 11 10 

# 		# Move elements of top row one step right
# 		for i in range(left, right+1):
# 			curr = mat[top][i]
# 			mat[top][i] = prev
# 			prev = curr

# 		top += 1

# 		# Move elements of rightmost column one step downwards
# 		for i in range(top, bottom+1):
# 			curr = mat[i][right]
# 			mat[i][right] = prev
# 			prev = curr

# 		right -= 1

# 		# Move elements of bottom row one step left
# 		for i in range(right, left-1, -1):
# 			curr = mat[bottom][i]
# 			mat[bottom][i] = prev
# 			prev = curr

# 		bottom -= 1

# 		# Move elements of leftmost column one step upwards
# 		for i in range(bottom, top-1, -1):
# 			curr = mat[i][left]
# 			mat[i][left] = prev
# 			prev = curr

# 		left += 1

# 	return mat

# # Utility Function
# def printMatrix(mat):
# 	for row in mat:
# 		print (row)


# # Test case 1
# matrix =[
# 			[1, 2, 3, 4 ],
# 			[5, 6, 7, 8 ],
# 			[9, 10, 11, 12 ],
# 			[13, 14, 15, 16 ]
# 		]
# # Test case 2
# """
# matrix =[
# 			[1, 2, 3],
# 			[4, 5, 6],
# 			[7, 8, 9]
# 		]
# """

# matrix = rotateMatrix(matrix)
# # Print modified matrix
# printMatrix(matrix)
# -----------------------------------------------------------

# from tkinter import Button


# class Solution:
# 	def formCoil(self, n):
# 		top = 0
# 		button = len(n) - 1
# 		left = 0
# 		right = len(n[0]) - 1
# 		while left < right:

		



# if __name__ == "__main__":
# 	t = int(input())
# 	for _ in range(t):
# 		n = int(input())
# 		ob = Solution()
# 		ptr = ob.formCoil(n)
# 		for i in range(2):
# 			print(*ptr[i])
# ---------------------------------------------------------------
def rotateMatrix(mat):
    for i in range(len(mat)):
        mat[i].reverse()
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
 
def displayMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            print(mat[i][j], end=' ')
        print()
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
 
rotateMatrix(mat)
displayMatrix(mat)


# output:
# 4 8 12 16 
# 3 7 11 15 
# 2 6 10 14 
# 1 5 9 13 
# -------------------------------------------------------------------

def printCoils(n):
	m = 8*n*n
	coil1 = [0]*m       # [0, 0, 0, 0, 0, 0, 0, 0]
	coil1[0] = 8*n*n + 2*n
	curr = coil1[0]
	nflg = 1
	step = 2
	index = 1
	while (index < m):
		for i in range(step):
			curr = coil1[index] = (curr - 4*n*nflg)
			index += 1
			if (index >= m):
				break
		if (index >= m):
			break

		for i in range(step):
			curr = coil1[index] = curr + nflg
			index += 1
			if (index >= m):
				break

		nflg = nflg*(-1)
		step += 2
	
	coil2 = [0]*m
	i = 0
	
	while(i < 8*n*n):
		coil2[i] = 16*n*n + 1 -coil1[i]
		i += 1

	print("Coil 1 :", end = " ")
	i = 0

	while(i < 8*n*n):
		print(coil1[i], end = " ")
		i += 1
	print("\nCoil 2 :", end = " ")
	i = 0

	while(i < 8*n*n):
		print(coil2[i], end = " ")
		i += 1
n = 1
printCoils(n)


