
def subArraySum(arr, n, sum_):

	for i in range(n):
		x = arr[i]
		j = i + 1
		while j <= n:
			if x == sum_:
				print ("Sum found between")
				print("indexes % d and % d"%( i, j-1))
				return 1
				
			if x > sum_ or j == n:
				break
			
			x = x + arr[j]
			j += 1

	print ("No subarray found")
	return 0

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23
subArraySum(arr, n, sum_)
# ------------------------------------------------------
x = [15, 2, 4, 8, 9, 5, 10, 23]
for i in range(len(x)):
    sum = 23
    y = i + 1
    while i <= len(x):
        if x[i] == sum:
            print(f"sum found {i, y - 1}")


        if x[i] > sum or y == len(x):
            break
        
        x[i] = x[i] + x[y]
        y +=1

print("no")
        
        
