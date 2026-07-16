"""===============================================================================
Problem
-------------------------------------------------------------------------------
Find the Maximum Element in an Array

Given an array of integers, find and return the largest element present in the
array.

Example:
Input:
arr = {3, 8, 2, 10, 5}

Output:
10

-------------------------------------------------------------------------------
Technique
-------------------------------------------------------------------------------
Linear Scan

-------------------------------------------------------------------------------
Idea
-------------------------------------------------------------------------------
Assume the first element is the maximum.

Traverse the array from left to right.
Whenever a larger element is found, update the maximum.

After traversing the entire array, the maximum variable stores the answer.

-------------------------------------------------------------------------------
Algorithm
-------------------------------------------------------------------------------
1. Initialize maximum = first element.
2. Traverse the array starting from index 1.
3. If current element > maximum
       update maximum.
4. Return maximum.

-------------------------------------------------------------------------------
Dry Run
-------------------------------------------------------------------------------
Input:
{3, 8, 2, 10, 5}

Initial:
maximum = 3

i = 1
arr[1] = 8
8 > 3
maximum = 8

i = 2
arr[2] = 2
2 > 8 ? No

i = 3
arr[3] = 10
10 > 8
maximum = 10

i = 4
arr[4] = 5
5 > 10 ? No

Answer = 10

-------------------------------------------------------------------------------
Complexity
-------------------------------------------------------------------------------
Time Complexity : O(n)

Space Complexity: O(1)

===============================================================================
"""

def findMaxelement(ele_list):
    return max(ele_list)

def findMaxelementManually(ele_list:list):
       max = ele_list[0]
       for ele in ele_list[1:]:
            if ele>max:
                  max=ele
       return max

if __name__ == "__main__":
       elements = [3,8,2,10,5]
       max_ele = findMaxelement(elements)
       print("Max element from the list - elements(used python builtin max function) - is", max_ele)
       max_ele = findMaxelementManually(elements)
       print("Max element from the list - elements(manually) - is", max_ele)
