

import matplotlib.pyplot as plt

import TP1 as TP


# Permet de transposer une matrice dans le but de tracer une forme
def transpose(A):
    C=[]
    for j in range (len(A[0])):
        B=[]
        for i in range (len(A)):
            B.append(A[i][j])
        C.append(B)
    return C

# Génère la montagne
def montagne(n,xmin,xmax,ymin,ymax) :
    r=int(n**(1/2))
    dx=(xmax-xmin)/(r+1)
    dy=(ymax-ymin)/(r+1)
    W=[]
    for i in range(r+1):
        for j in range(r+1):
            x=xmin+dx*i
            y=ymin+dy*j
            W.append([x,y,0.5*x-0.3*y+1])
    return(transpose(W))


# Génère le nuage
def nuage(n,xmin,xmax,ymin,ymax) :
    r=int(n**(1/2))
    dx=(xmax-xmin)/(r+1)
    dy=(ymax-ymin)/(r+1)
    W=[]
    for i in range(r+1):
        for j in range(r+1):
            x=xmin+dx*i
            y=ymin+dy*j
            W.append([x,y,0.5*x-0.3*y+8])
    return(transpose(W))






def mat_projection(n,d):
    
    k = [-n[0] ,-n[1] ,- n[2]]

    X1= [1 + d[0]*k[0],d[0]*k[1],d[0]*k[2]  ]
    Y1= [ d[1]*k[0],1+d[1]*k[1],d[1]*k[2] ]
    Z1= [d[2]*k[0],d[2]*k[1],1+d[2]*k[2] ]
    


    MP = [X1,Y1,Z1]

    return MP





(X,Y,Z)=montagne(10000,-6,6,-4,4)
(X1,Y1,Z1)=nuage(10000,-2,2,-2,2)

plt.figure(" Ombre d'un nuage ")
axes = plt.axes(projection= "3d")
print(axes, type(axes))
print(mat_projection([1,-2,0],[1,0,1]))

# Trace les listes en 3D
axes.plot(X,Y,Z)
axes.plot(X1,Y1,Z1)

# Ajoute des étiquettes pour les axes
axes.set_xlabel("X")
axes.set_ylabel("Y" )
axes.set_zlabel("Z")

plt.show()

