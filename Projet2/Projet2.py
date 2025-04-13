


from asyncio import TaskGroup
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import pi
import main as main


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







def mat_projection2(n,d):
    
    PS = TP.prodscal_vect(d,n)

    MP = [ [1- ((n[0]*d[0])/PS),-((n[1]*d[0])/PS),- ((n[2]*d[0])/PS)],
         [- ((n[0]*d[1])/PS),1- ((n[1]*d[1])/PS),- ((n[2]*d[1])/PS)],
         [- ((n[0]*d[2])/PS),- ((n[1]*d[2])/PS),1- ((n[2]*d[2])/PS)]]

    return MP

def projection(n,d,d1,A):
    LP =  mat_projection2(n,d)
    
    T = [d1/n[0],0,0]

    InvI3 = [[-1,0,0],[0,-1,0],[0,0,-1]]

    AP = TP.prod_mat_vect( TP.somme_mat(LP,InvI3 ),T )

    A1 = TP.somme_vect(TP.prod_mat_vect(LP,A),AP)
    return A1


def mat_Rotation(n,d, teta):
    normeD =  ((d[0]**2)+(d[1]**2)+(d[2]**2))**(1/2)

    U1 = [d[0]/ normeD,d[1]/normeD,d[2]/normeD]


    dot_product = TP.prodscal_vect(n,U1)
    proj = [dot_product * U1[i] for i in range(len(U1))]     
    
    ortho = [n[i] - proj[i] for i in range(len(n))]
    normeOrtho =  ((ortho[0]**2)+(ortho[1]**2)+(ortho[2]**2))**(1/2)
    
    U2 = [ortho[0]/normeOrtho,ortho[1]/normeOrtho,ortho[2]/normeOrtho]

    U3 = TP.prod_vect(U1,U2)

    R = [U1,U2,U3]
    R1 = transpose(R)

    Mox = [[1,0,0],
           [0,main.cos(teta),-main.sin(teta)],
           [0,-main.sin(teta),main.cos(teta)]]

    M = TP.prod_mat_mat(TP.prod_mat_mat(R,Mox),R1)
    return M

def Rotation(n,d,d1, teta, M):
    MR =mat_Rotation(n,d, teta)
    InvI3 = [[-1,0,0],[0,-1,0],[0,0,-1]]
    T = [d1/n[0],0,0]
    A = TP.prod_mat_vect(TP.somme_mat(MR,InvI3),T)
    for i in range(len(M[0])):
        tmp = [M[0][i],M[1][i],M[2][i]]
        tmp = TP.somme_vect(TP.prod_mat_vect(MR,tmp),A) 

        M[0][i] = tmp[0]
        M[1][i] = tmp[1]
        M[2][i] = tmp[2]

    return M


def ombre(n,d1,S,W):
    W1 = [[],[],[]]

    M = [W[0][0],W[1][0],W[2][0]]
    N = [W[0][1],W[1][1],W[2][1]]

    DM = [M[0]-S[0],M[1]-S[1],M[2]-S[2]]
    DN = [N[0]-S[0],N[1]-S[1],N[2]-S[2]]

    N1 = projection([0.5,-0.3,-1.0],DN,1.0,N)
    M1 = projection([0.5,-0.3,-1.0],DM,1.0,M)

    M1N1 = [N1[0]- M1[0],N1[1]- M1[1],N1[2]- M1[2]]

    MN =  [N[0]-M[0],N[1]-M[1],N[2]-M[2]]

    Mnorme = ((MN[0]**2)+(MN[1]**2)+(MN[2]**2))**(1/2)
    M1norme = ((M1N1[0]**2)+(M1N1[1]**2)+(M1N1[2]**2))**(1/2)

    k = M1norme/Mnorme

    Lp = TP.identite(3)
    for i in range (len( Lp)):
        Lp[i][i] = Lp[i][i]*k
    
    InvI3 = [[-1,0,0],[0,-1,0],[0,0,-1]]

    Ap = TP.prod_mat_vect( TP.somme_mat(Lp,InvI3),[-N1[0],-N1[1],-N1[2]])


    for i in range (len (W[0])):
        tmp = projection(n,DN,d1,[W[0][i],W[1][i],W[2][i]])
        W1[0].append(tmp[0])
        W1[1].append(tmp[1])
        W1[2].append(tmp[2])
    
    W2 = [[],[],[]]

    for i in range (len (W1[0])):
        tmp = TP.prod_mat_vect(Lp,[W1[0][i],W1[1][i],W1[2][i]])
        tmp1 = TP.somme_vect(tmp,Ap)
        W2[0].append(tmp1[0])
        W2[1].append(tmp1[1])
        W2[2].append(tmp1[2])
    return W2,N,N1

#S[0]-W[0][i],S[1]-W[1][i], S[2]-W[2][i]
def update(val): 
    Sx = slider_sx.val
    Sy = slider_sy.val
    Sz = slider_sz.val
    soleil._offsets3d = ([Sx], [Sy], [Sz])

    (X4,Y4,Z4),(X2,Y2,Z2),(X3,Y3,Z3) =ombre([0.5,-0.3,-1.0],1.0, [Sx,Sy,Sz],[X1,Y1,Z1])

    ombre_pt1._offsets3d = ([X2], [Y2], [Z2])
    ombre_pt2._offsets3d = ([X3], [Y3], [Z3])

    ombre_line.set_data(X4, Y4)
    ombre_line.set_3d_properties(Z4)
    fig.canvas.draw_idle()

def updateRot(val): 
  
    (X,Y,Z) =Rotation([0.5,-0.3,-1.0],[0,0,1],1.0,val,[X1,Y1,Z1])


    nuage.set_data(X,Y)
    nuage.set_3d_properties(Z)

    (X4,Y4,Z4),(X2,Y2,Z2),(X3,Y3,Z3) =ombre([0.5,-0.3,-1.0],1.0, [Sx,Sy,Sz],[X1,Y1,Z1])

    ombre_pt1._offsets3d = ([X2], [Y2], [Z2])
    ombre_pt2._offsets3d = ([X3], [Y3], [Z3])

    ombre_line.set_data(X4, Y4)
    ombre_line.set_3d_properties(Z4)
    fig.canvas.draw_idle()





(Sx,Sy,Sz) = [10,10,20]

(X,Y,Z)=montagne(5000,-6,6,-4,4)
(X1,Y1,Z1)=nuage(5000,-2,2,-2,2)








(X4,Y4,Z4),(X2,Y2,Z2),(X3,Y3,Z3) =ombre([0.5,-0.3,-1.0],1.0, [Sx,Sy,Sz],[X1,Y1,Z1])


fig = plt.figure(" Ombre d'un nuage ")
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

axes = plt.axes(projection= "3d")

# Trace les listes en 3D
soleil  = axes.scatter(Sx, Sy, Sz, color="yellow", s=500)  # 's' définit la taille du point

# Axes labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim(-10, 20)
ax.set_ylim(-10, 20)
ax.set_zlim(0, 30)

# Sliders
ax_sx = plt.axes([0.2, 0.15, 0.6, 0.03])
ax_sy = plt.axes([0.2, 0.10, 0.6, 0.03])
ax_sz = plt.axes([0.2, 0.05, 0.6, 0.03])
ax_sRot = plt.axes([0.2, 0.0, 0.6, 0.03])

slider_sx = Slider(ax_sx, 'Sx', -10, 20, valinit=Sx)
slider_sy = Slider(ax_sy, 'Sy', -10, 20, valinit=Sy)
slider_sz = Slider(ax_sz, 'Sz', 0, 30, valinit=Sz)
slider_rot = Slider(ax_sRot, 'Sz', -1, 1, valinit=0)

axes.plot(X,Y,Z)
ombre_line, = axes.plot(X4,Y4,Z4, color="black", alpha=0.5)

nuage, = axes.plot(X1,Y1,Z1)
ombre_pt1 = axes.scatter(X2, Y2, Z2, color="red", s=100)  # 's' définit la taille du point
ombre_pt2 =axes.scatter(X3, Y3, Z3, color="green", s=100)  # 's' définit la taille du point






# Ajoute des étiquettes pour les axes
axes.set_xlabel("X")
axes.set_ylabel("Y" )
axes.set_zlabel("Z")

slider_sx.on_changed(update)
slider_sy.on_changed(update)
slider_sz.on_changed(update)
slider_rot.on_changed(updateRot)


plt.show()

