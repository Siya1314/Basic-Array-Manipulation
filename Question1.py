# Write a function that takes as input a matrix and determines whether or not the matrix is symmetric. The function should 
# return the strings not symmetric or symmetric. You may not use any obvious builtin function.

def symCheck(A):
    n=len(A)
    m=len(A[0])
    countsym=0
    if m!=n:
        sol='not symmetric'
    else:
        for i in range(0,n):
            for j in range(0,n):
                if A[i][j]==A[j][i]:
                    countsym=countsym+1
        #print(countsym)
        if countsym==n*n:
            sol='symmetric'
        else:
            sol='not symmetric'
                
    return sol
    