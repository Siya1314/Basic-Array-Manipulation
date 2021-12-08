# Write a function which takes in a matrix and computes the absolute difference between the sums of its diagonals (i.e.   
# left-to-right and right-to-left).

def diagonalDifference(arr):
    n=len(arr) #number of rows
    m=len(arr[0]) #number of columns
    sumright=0
    sumleft=0
    for i in range(0,n):
        
        if m==n:
            sumright=sumright+arr[i][i]
            sumleft=sumleft+arr[i][n-i-1]
            
            sol=abs(sumright-sumleft)
        if m!=n:
            sol='Not Square'
    return sol