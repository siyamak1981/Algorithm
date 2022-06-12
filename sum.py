# x = [1,2,5,4]
# y = 0
# for i in x:
#     y +=i
# print(y)








# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


# Example 1:

# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.
# Example 2:

# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)





class Solution:
    def maxSubArraySum(self,arr,N):
        first = arr[0]
        sum = 0
        for i in range(N):
            sum = sum + arr[i]
            if sum > first  :
                first = sum
            if sum < 0:
                sum = 0  
        return first
            
import math
def main():
        T=int(input())
        while(T>0):        
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxSubArraySum(arr,n))
            T-=1
if __name__ == "__main__":
    main()