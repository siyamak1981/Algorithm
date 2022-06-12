# Function to find the cross over point
# (the point before which elements are
# smaller than or equal to x and after
# which greater than x)
def findCrossOver(arr, low, high, x) :
	# Base cases
	if (arr[high] <= x) : # x is greater than all
		return high

	if (arr[low] > x) : # x is smaller than all
		return low
	
	# Find the middle point
	mid = (low + high) // 2 # low + (high - low)// 2
	
	# If x is same as middle element,
	# then return mid
	if (arr[mid] <= x and arr[mid + 1] > x) :
		return mid
	
	# If x is greater than arr[mid], then
	# either arr[mid + 1] is ceiling of x
	# or ceiling lies in arr[mid+1...high]
	if(arr[mid] < x) :
		return findCrossOver(arr, mid + 1, high, x)
	return findCrossOver(arr, low, mid - 1, x)

# This function prints k closest elements to x
# in arr[]. n is the number of elements in arr[]
def printKclosest(arr, x, k):
	# Find the crossover point
	l = findCrossOver(arr, 0, len(arr) - 1, x)
	r = l + 1 # Right index to search
	count = 0 # To keep track of count of
			  # elements already printed

	# If x is present in arr[], then reduce
	# left index. Assumption: all elements
	# in arr[] are distinct
	if (arr[l] == x):
		l -= 1

	# Compare elements on left and right of crossover
	# point to find the k closest elements
	while (l >= 0 and r < len(arr) and count < k) :
		if (x - arr[l] < arr[r] - x) :
			print(arr[l], end = " ")
			l -= 1
		else :
			print(arr[r], end = " ")
			r += 1
		count += 1

	# If there are no more elements on right
	# side, then print left elements
	while (count < k and l >= 0) :
		print(arr[l], end = " ")
		l -= 1
		count += 1

	# If there are no more elements on left
	# side, then print right elements
	while (count < k and r < len(arr)) :
		print(arr[r], end = " ")
		r += 1
		count += 1

# printKclosest([12, 16, 29, 30, 35, 39, 42,
# 		45, 48, 50, 53, 55, 56], 35, 4)
	




# ------------------------------------------------
# def foo(x, k, target):
#     list = []
#     list2 = []
#     list3 = []
#     if target:
#         for i in range(len(x)):
#             if x[i] > target:
#                 list.append(x[i])

#     if target:
#         for i in range(len(x)):
#             if x[i] < target:
#                 list2.append(x[i])
  
#     z = list2[:k] + list[:k]

#     for i in range(len(z) - 1):
#         y = z[i]
#         y -= target
#         list3.append(y)
#     p = sorted(list3[-4:])
#     for ps in p:
#         ps = ps + 35
#         print(ps)

# foo([12, 16, 29, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 4, 35)




import heapq
class Solution:
   def printKClosest(self, arr, n, k, x):
       # code here
        heap = []
        result = []
        if x in arr:
            # result.remove(x)
            arr.remove(x)
        for i in arr:
            heapq.heappush(heap, (abs(i - x), -i))
        
        while k > 0:
            result.append((heapq.heappop(heap)[1])*-1)
            k-= 1
        
        return result
printKclosest([12, 16, 29, 30, 35, 39, 42,
		45, 48, 50, 53, 55, 56], 35, 4)