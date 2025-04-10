   
#TP2 Math
    

import matplotlib.pyplot as plt

import TP1 as t





def z(x,y):
    return(-(x**2)+3*y-2)


def Question2():
    X=[]
    Y=[]
    Z=[]
    n=1000 #nombre de points
    xmin=-4
    xmax=4 #bornes de x

    ymin=-4
    ymax=4 #bornes de x
    dx=(xmax-xmin)/(n-1) #variation de x
    dy=(ymax-ymin)/(n-1) #variation de y

    for i in range(n):
        x=xmin+dx*i
        y=x=ymin+dy*i

        X.append(x)
        Y.append(z(x,y))
        Z.append(0)

    fig = plt.figure() #Création de la figure
    ax = plt.axes(projection='3d') #Definition du tracé 3D
    ax.scatter3D(X, Y, Z); #Définition des axes
    plt.show()

#question 3

def transpose(A):

    T =[] 

    for i in range(len(A)):
        T.append([])
        for j in range(len(A)):
            if(i == j):
                T[i].append(A[i][j])
            elif(i > j):
                 T[i].append(A[j][i])
            elif(i < j):
                 T[i].append(A[j][i])

    return T



def Question3():

    A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
    print(transpose(A)) 




    return 0


#question 4


def carre(n,xmin,ymin,a):
    r=int(n**(1/2))
    dx=(a-xmin)/(r+1)
    dy=(a-ymin)/(r+1)
    W=[]
    for i in range(r+1):
        for j in range(r+1):
            x=xmin+dx*i
            y=ymin+dy*j
            W.append([x,y,-2*x+y+3])
    return(transpose(W))

#question 5

def cube(n,xmin,ymin,a):
    r=int(n**(1/2))
    dx=(a-xmin)/(r+1)
    dy=(a-ymin)/(r+1)
    W=[]
    for i in range(r+1):
        for h in range(r+1):
            for j in range(r+1):
                x=xmin+dx*h
                y=ymin+dy*j
                W.append([x,y+i,-2*x+y+3])
    return(transpose(W))


                