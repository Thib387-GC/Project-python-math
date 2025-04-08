

# Question 3
def somme_vect(u,v):

    W = []

    for i in range(len(u)):
        W.append( u[i] + v[i])
    
    return W

a = [0,1,10]

b = [15,10,-10]

print(somme_vect(a,b))

# Question 4

def prodscal_vect(u,v):
    
    a = 0
    for i in range(len(u)):
        a+= u[i] * v[i]
    
    return a
   

a = [0,1,0]

b = [41,0,480]

print(prodscal_vect(a,b))

# Question 5



def identite(n):

    IdN = []
    for i in range(n):
        IdN.append([0 for x in range(n)])
        IdN[i][i] = 1
    

    return IdN

print(identite(3))

# Question 6
def somme_mat(A,B):
    C = []

    for i in range(len(A)):
        C.append([somme_vect(A[i], B[i])])
    
    return C
M=[[1,2,3],[4,5,6],[4,5,6]]
M2=[[1,2,3],[4,5,6],[4,5,6]]

print(somme_mat(M,M2))

# Question 7
def prod_mat_vect(A,u):
    v = []

    for i in range (len(u)):
        
        v.append( prodscal_vect(A[i],u))

    return v

M=[[1,2,3],[4,5,6],[4,5,6]]

print(prod_mat_vect(M,a))

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


M=[[1,2,3],[4,5,6],[4,5,6]]

M2=[[1,2,3],[4,5,6],[4,5,6]]
print(prod_mat_mat(M,M2))



