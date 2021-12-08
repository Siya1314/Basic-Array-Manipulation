# Write a function that takes in 3 inputs, a list of integers a, a integer k, and input q (which may be an integer or 
#list). The function should rotate the array a k times. For example, if ar =  [1, 2, 3] and k = 2, then we rotate the array 
#rightwards, resulting in [2, 3, 1]. THe function should then return the q indices of ar. Thus, in our example, in q = [1, 
#2], then the function should return the array [3, 1].


def indexRotation(a, k, q):
    out = [] 
    sol=q
    n=len(a) 
    for i in range(n - k, n): 
        out.append(a[i]) 
          
    for j in range(0, n - k):  
        out.append(a[j]) 
        
    if isinstance(q,list):
        for ii in range(0,len(q)):    
            sol[ii] = out[q[ii]]
    elif isinstance(q,int):
            sol=out[q]
    return sol