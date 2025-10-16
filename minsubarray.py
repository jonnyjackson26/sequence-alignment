"""
This is my first time doing dynamic programming. 
I find the minimum sum of continuous subarray in a given array. (linear time).
This is a challenge problem from the YouTube video "Dynamic Programming Explained (Practical Examples)" by Tech with Tim, which I watched

https://www.youtube.com/watch?v=Sz9yH-RDAgo&t=73s
"""

myArray = [1,-2,100,-15,100,4,-2,-4,1,-3]

def minsubarray(arr): #returns min and min_range
    min=arr[0]
    min_range=[0,0]
    for i in range(len(arr)):
        if min+arr[i]>arr[i]:
            min=arr[i]
            min_range[1]=i 
            min_range[0]=i
        else:
            min=min+arr[i]
            min_range[1]=i

    return min, min_range

print(minsubarray(myArray))







