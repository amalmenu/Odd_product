def distinct(lst):
    D=[]
    for i in range(len(lst)):
        if lst[i] not in D:
             D.append(lst[i])
    return D

def product_of_distinct(A):

    C=[]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]!=A[j] and A[i]*A[j]%2!=0:
             C.append((A[i],A[j]))

    return C


