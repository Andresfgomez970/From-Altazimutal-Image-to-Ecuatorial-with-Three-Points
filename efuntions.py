#!/usr/bin/python

########Description of the program############
###This program is the recopilation of all the useful funtions 

from __future__ import division
import math
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
from scipy.misc import*
from numpy import*
import numpy as np #This for a confution between to libraries 

#1.multilply 
def pow(x):
    return x*x

#2.To find the distance between two points 
def dist(a1,b1,a2,b2):   
    c=math.sqrt((a1-a2)**2+(b1-b2)**2)
    return c

#3.To solve a cuadratic ecuation 
def cuadratic(a,b,c):
        d = b*b-4*a*c 
        d1 = math.sqrt(d) 
        if d < 0:
               print ("This equation has no real solution")
        elif d == 0:
                x = (0.5)*(-b+d1)/(a)
                return x,x
        else:
                x1 = (0.5)*(-b+d1)/(a)
                x2 = (0.5)*(-b-d1)/(a)
                return x1,x2

#4.To solve the analytically for the angles of rotation
def equation(r0,r1,r2,t1,t2):
    A12 = pow(t1/t2)  
    Ap12 = pow(r1/r2)
    B1 = pow(r1)+pow(r0)
    B2 = pow(r2)+pow(r0)
    C1 = -2*r0*r1
    C2 = -2*r0*r2
    R1 = (A12*B2-B1)/C1
    R2 = (A12*C2)/C1
    R3 = A12/Ap12
    R4 = 2*R1*R2
    a = pow(R2) - R3
    b = R4
    c = pow(R1) + R3 -1
    
    #co=180/math.pi 

    #Here we are ignoring the solution of the prime (subp) variable 
    #because is a strange solution.
    u2 , u2p = cuadratic(a,b,c) 
    u1 = math.sqrt(1-R3*(1- u2**2))
    theta2=math.acos(u2)#*co
    theta1=math.acos(u1)#*co
    return theta1, theta2

#5.To find the center of the sun
def center(imagen):
    data=imread(imagen)

    #This convert the image in a matrix               
    #Rows, columns and layer                          
    
    imagen=data[:,:,0] #convert in a matrix    

    y,x = imagen.shape 
    subimagen = imagen[:,:]
    vcom = subimagen.max()*0.5

    condition2=subimagen>=vcom
    
    #create a matrix of x's and y's                   
    xa,ya=meshgrid(arange(x),arange(y))
    xm=xa[condition2].mean()/x
    ym=ya[condition2].mean()/y
    
    return xm,ym


#6.Find Mercury in the image
    
def findmer(imagen):
    
    data = imread(imagen)
    
    imagen=data[:,:,0]
    
    y,x = imagen.shape
    
    subimagen = imagen[:,:]
    
    vcom1 = subimagen.max()*0.5 
    vcom2 = subimagen.max()*0.6

    i=0
    points=[]
    while i<x-1:
        i=i+1
        j=0
        while j<y-1:
            j=j+1
            a=subimagen[j,i]
            while a>vcom2:
                j=j+1
                a=subimagen[j,i]
                temp=[] 
                while a<vcom1:
                    if j>y-2:
                        break
                    temp.append([(1.0*i/x),(1.0*j/y)]) #/y ,/x
                    j=j+1
                    a=subimagen[j,i]
                    while a>vcom2:    
                        points += temp  
                        return points[0]
                        
#7.Calculate the distant of Mercury to the center 
#in each imga 
def radii(ls):
    coo=[]
    cen=[]
    rad=[]
    for i in range(len(ls)):
        coo.append(findmer(ls[i]))
        cen.append(center(ls[i]))
        rad.append(dist(coo[i][0],coo[i][1],cen[i][0],cen[i][1]))
    return rad[0],rad[1],rad[2]


#8.To graph the circle
def graph(r0,r1,r2,th1,th2):
    xm = [r0,r1*np.cos(th1),r2*np.cos(th2)]
    ym =  [0,r1*np.sin(th1),r2*np.sin(th2)]
    x = np.arange(-1,1,0.001)
    #finally we can graph the alineation of the points                                                                
    # in a circle of radius 1                                                                                         
    plt.figure('The curve of Mercury',figsize=(10,12))
    for i in range(len(xm)):
        plt.plot(xm[i],ym[i],'.',label='point image'+str(i+1),ms=10)
    plt.plot(x,np.sqrt(1-x*x),'b-',x,-np.sqrt(1-x*x),'b-')
    plt.plot(x,(ym[0]-ym[1])/(xm[0]-xm[1])*(x-xm[0])+ym[0],'k-',label='reconstructed line')
    plt.grid()
    plt.legend()
    plt.savefig('Ejemplo1.png')
    plt.show()

