import numpy as np
import matplotlib.pyplot as plt
import scipy
from dfit import Dfit
import pandas as pd

#question 3
x = (3+4j)/(5+6j)
#print(x)
#print(39/61,2/61)
y = np.exp(2j)
z=np.cos(3j)
#print(y)
#print(np.cos(2),np.sin(2))
#print(z)
#print((np.exp(-3)+np.exp(3))/2)
def graph(z):
    t=np.linspace(0,10,100)
    ft = []
    real=[]
    imag=[]
    for x in t:
        ft.append(np.exp(1j*z*x))
    for x in ft:
        real.append(np.real(x))
        imag.append(np.imag(x))
    plt.plot(t,real,'g')
    plt.plot(t,imag)
    plt.show()
    plt.figure()
    plt.plot(real,imag)
    plt.show()
#graph(5+.2j)

#question 4
def eq(x):
    return x*np.sin(x**2)
#print((np.cos(1)-np.cos(25))/2)
#print(scipy.integrate.quad(eq,1,5))

#question 5
def eq(x):
    return x*np.sin(x**2)
def trapezoid(a,b,f):
    nn = int(input("gimme n "))
    if nn<1:
        print("shut up")
    elif nn >=1:
        h = (b-a)/nn
        area = 0
        while True:
            s1 = a 
            s2 = a+h
            area += h*(.5*f(s1)+.5*f(s2))
            if s2 >= b:
                break
            elif s2 < b:
                a += h
                continue
        print((np.cos(1)-np.cos(25))/2)
        print(scipy.integrate.quad(eq,1,5))
        print(area)
#trapezoid(1,5,eq)

#question 6
def eq(x):
    return x*np.sin(x**2)
def simps(f,a,b,nn):
    if nn<1:
            print("shut up")
    elif nn%2!=0:
        print("yucky stinky odd number")
        nn+=1
    elif nn %2==0:
        xs = np.linspace (a,b,nn+1)
        h = (b-a)/nn
        w = np.full(nn+1,4.0)
        area = (h/3)*sum(w*f(xs))
        print(area)
simps(eq,1,5,1000)