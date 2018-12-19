Created on Tue Dec 18 21:53:23 2018


This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer 
(greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range 
        [−1,000,000..1,000,000].

@author: Sai Kamat
"""
# test cases.
A = {}
A[1] = [1, 3, 6, 4, 1, 2, 100]    # 5
A[2] = [-1, -3]   # 1
A[3] = [-10000, 5000]   #1
A[4] = [-1000000, 0, 1000000]   #1
A[5] = [-1000000, 2000, 1, 1000000]   #2
A[6] = [1, 2, 7, 8, 3]   #4
A[7] = [1, 2, 3]   #4
A[8] = [-3, -4, -2, 0, 1, 1, 2, 2, 3, -1]   #4


def solution(arr):
    arr.sort()
    minv = 1
    for ele in arr:
        if ele > 0:
            if ele != minv and minv not in arr:
                return minv
            else:
                minv = minv+1
    return minv


for i in range(len(A)):
    print(solution(A[i+1]))
