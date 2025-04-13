

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

def mat_projection2(n,d):
    

    MP = [ [1- ((n[0]*d[0])/TP.prodscal_vect(d,n)),-((n[1]*d[0])/TP.prodscal_vect(d,n)),- ((n[2]*d[0])/TP.prodscal_vect(d,n))],
         [- ((n[0]*d[1])/TP.prodscal_vect(d,n)),1- ((n[1]*d[1])/TP.prodscal_vect(d,n)),- ((n[2]*d[1])/TP.prodscal_vect(d,n))],
         [- ((n[0]*d[2])/TP.prodscal_vect(d,n)),- ((n[1]*d[2])/TP.prodscal_vect(d,n)),1- ((n[2]*d[2])/TP.prodscal_vect(d,n))]]

    return MP

def projection(n,d,d1,A):
    LP =  mat_projection2(n,d)
    
    T = [d1/n[0],0,0]

    InvI3 = [[-1,0,0],[0,-1,0],[0,0,-1]]

    AP = TP.prod_mat_vect( TP.somme_mat(LP,InvI3 ),T )

    A1 = TP.somme_vect(TP.prod_mat_vect(LP,A),AP)
    return A1

def ombre(n,d1,S,W):
    W1 = [[],[],[]]
    for i in range (len (W[0])):
        tmp = projection(n,[-5,-5,-6],d1,[W[0][i],W[1][i],W[2][i]])
        W1[0].append(tmp[0])
        W1[1].append(tmp[1])
        W1[2].append(tmp[2])

    return W1

#S[0]-W[0][i],S[1]-W[1][i], S[2]-W[2][i]

(Sx,Sy,Sz) = [10,10,20]

(X,Y,Z)=montagne(10000,-6,6,-4,4)
(X1,Y1,Z1)=nuage(10000,-2,2,-2,2)

(X2,Y2,Z2) = projection([0.5,-0.3,-1.0],[-5.0,-5.0,-6.0],8.0,[0.0,0.0,8.0])

(X3,Y3,Z3) = projection([0.5,-0.3,-1.0],[-5.0,-5.0,-6.0],1.0,[0.0,0.0,8.0])

(X4,Y4,Z4) =ombre([0.5,-0.3,-1.0],1.0, [Sx,Sy,Sz],[X1,Y1,Z1])


plt.figure(" Ombre d'un nuage ")
axes = plt.axes(projection= "3d")
print(axes, type(axes))

# Trace les listes en 3D
axes.scatter(Sx, Sy, Sz, color="yellow", s=500)  # 's' définit la taille du point



axes.plot(X,Y,Z)
axes.plot(X4,Y4,Z4, color="black", alpha=0.5)

axes.plot(X1,Y1,Z1)
axes.scatter(X2, Y2, Z2, color="red", s=100)  # 's' définit la taille du point
axes.scatter(X3, Y3, Z3, color="green", s=100)  # 's' définit la taille du point

# Ajoute des étiquettes pour les axes
axes.set_xlabel("X")
axes.set_ylabel("Y" )
axes.set_zlabel("Z")

plt.show()

