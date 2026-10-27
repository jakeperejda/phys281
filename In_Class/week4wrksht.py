"""9/29/26
Worksheet practice :)
"""

import numpy as np
import matplotlib.pyplot as plt
#problem 3
def arrays():
    rr = int(input("rows? "))
    cc = int(input("cols? "))
    aa = np.zeros((rr,cc),int)
    x = 1
    for r in range(rr):
        for c in range(cc):
            aa[r,c] = x
            x+=1
    print('Array:\n',aa)
arrays()

#problem 4
def arrays2():
    rr = int(input("rows? "))
    cc = int(input("cols? "))
    aa = np.zeros((rr,cc),int)
    x = 1
    for r in range(rr):
        for c in range(cc):
            aa[r,c] = x
            x+=1
    print('Array:\n',aa)
    print('Third column:\n',aa[2])
    print('Upper left:\n',aa[:3,:3])
    print('Upper right:\n',aa[:3,-3:])
    print('Transpose:\n',aa.T)
#arrays2()

#problem 5
def arrays3():
    rr = int(input("rows? "))
    cc = int(input("cols? "))
    aa = np.zeros((rr,cc),int)
    x = 1
    for r in range(rr):
        for c in range(cc):
            aa[r,c] = x
            x+=1
    print('Array:\n',aa)
    #np.savetxt('foo.txt',aa,newline='\r\n')
#arrays3()

#problem 6
def plots():
    x = np.linspace(-20,20,200)
    f1 = np.cos(x)
    f2 = np.sin(x)
    plt.plot(x,f1)
    plt.show()
    plt.plot(x,f2)
    plt.show()
    plt.plot(x,f1,'m', label = 'cos(x)')
    plt.plot(x,f2,'b--', label = 'sin(x)')
    plt.legend(fontsize=12)
    plt.ylim(-1,1)
    plt.xlim(-5,5)
    plt.show()
#plots()

#question 7
def plots2():
    x = np.linspace(-20,20,100)
    f1 = np.cos(x)
    f2 = np.sin(x)
    plt.plot(x,f1,'s')
    plt.show()
    plt.plot(x,f2,'.')
    plt.show()
#plots2()

#question 8
def plots3():
    x = np.linspace(-10,10,100)
    f1 = np.cos(x)
    f2 = np.sin(x)
    plt.plot(x,f1,'b--',label=('cosx'))
    plt.plot(x,f2,'g-',label=("sinx"))
    plt.title('gaming plot',fontsize=10)
    plt.xlabel('x')
    plt.ylabel('cosx or sinx')
    plt.legend(fontsize=10)
    plt.xlim(0,8)
    plt.show()
#plots3()

#question 9 
def plots3():
    x = np.linspace(-10,10,100)
    f1 = np.sin(x)/np.cos(x)
    plt.plot(x,f1,'b--',label=(r'$\tan x$ or $\frac{\sin x}{\cos x}$'))
    plt.title('gaming plot',fontsize=10)
    plt.xlabel(r'$\delta$x')
    plt.ylabel(r'$\frac{\sin x}{\cos x}$')
    plt.legend(fontsize=10)
    plt.xlim(0,8)
    plt.show()
#plots3()