

# Question 3
def somme_vect(u,v):

    W = []

    for i in range(len(u)):
        W.append( u[i] + v[i])
    
    return W



# Question 4

def prodscal_vect(u,v):
    
    a = 0
    for i in range(len(u)):
        a+=  u[i] * v[i]
    
    return a
   


# Question 5



def identite(n):

    IdN = []
    for i in range(n):
        IdN.append([0 for x in range(n)])
        IdN[i][i] = 1
    

    return IdN


# Question 6
def somme_mat(A,B):
    C = []

    for i in range(len(A)):
        C.append(somme_vect(A[i], B[i]))
    
    return C
M=[[1,2,3],[4,5,6],[4,5,6]]
M2=[[1,2,3],[4,5,6],[4,5,6]]


# Question 7
def prod_mat_vect(A,u):
    v = []

    for i in range (len(u)):
        
        v.append( prodscal_vect(A[i],u))

    return v



# Question 8

def prod_mat_mat(A,B):
    C = []

    
    for i in range (len(A)):
        C.append([])    
        for j in range (len(A)):

            C[i].append( prodscal_vect(A[i],[B[z][j] for z in range(len(B))]))

    return C


def prod_vect(A,B):

    C= []

    C.append(A[1]*B[2]-A[2]*B[1])
    C.append(A[2]*B[0]-A[0]*B[2])
    C.append(A[0]*B[1]-A[1]*B[0])
    return C





