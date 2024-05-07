#!/usr/bin/python3
""" Returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
   """
   Returns a list of lists of integers representing the Pascal’s triangle of n

   Args:
        n (int): The number of extent to go for pascal_triangle
   """
   ans = []
   for j in range(1, n + 1 ):
       if j == 1:
           ans.append([1])
       elif j == 2:
           ans.append([1, 1])
       else:
           arr = ans[-1]
           new_arr = []

           for i in range(len(arr)):
               if i != len(arr) - 1:
                   if i == 0:
                       new_arr.append(arr[i])
                       new_arr.append(arr[i] + arr[i+1])
                   else:
                       new_arr.append(arr[i] + arr[i+1])
               else:
                   new_arr.append(arr[i])
           ans.append(new_arr)
   return ans
