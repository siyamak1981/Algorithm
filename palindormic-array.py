
# Input:
# 2
# 5
# 111 222 333 444 555
# 3
# 121 131 20

# Output:
# 1
# 0

# Explanation:
# For First test case.
# n=5;
# A[0] = 111    //which is a palindrome number.
# A[1] = 222   //which is a palindrome number.
# A[2] = 333   //which is a palindrome number.
# A[3] = 444  //which is a palindrome number.
# A[4] = 555  //which is a palindrome number.
# As all numbers are palindrome so This will return 1.

arr = [333,222]
for i in range(2):
    x = int(str(arr[i])[::-1])

    if x != arr[i]:
        print(0)
print(1)