import numpy as np
import matplotlib.pyplot as plt
#question 2
def plots():
    x = np.linspace(-5,5,10)
    plt.subplot(321)
    plt.plot(x,x)
    plt.title('x=y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.subplot(322)
    plt.plot(x**2,x)
    plt.title(r'$y=\sqrt{x}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.subplot(323)
    plt.plot(x,x**2)
    plt.title(r'$y=x^2$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.subplot(324)
    plt.plot(x,x**3)
    plt.title(r'$y=x^3$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.subplot(325)
    plt.plot(x,x**4)
    plt.title(r'$y=x^4$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.subplot(326)
    plt.plot(x,np.sin(x))
    plt.title(r'$y=\sin x$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.subplots_adjust(hspace=1,wspace=.25)
    plt.show()
#plots()

#question 3
def density():
    x = np.linspace(-1,1,100)
    y = np.linspace(-1,1,100)[:,np.newaxis]
    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(y,x)
    s = np.cos(r+theta)
    s2 = np.cos(r+theta/2)
    plt.imshow(s)
    plt.show()
    plt.imshow(s2)
    plt.show()
#density()

#question 4
def orbital():
    x = np.linspace(-20,20,100)
    y = np.linspace(-20,20,100)[:,np.newaxis]
    r = np.sqrt(x**2+y**2)
    psi = x*(6-r)*np.exp(-r/3)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x,y,psi,cmap='plasma')
    plt.title('weird ahh graph')
    plt.xlabel('x')
    plt.ylabel('y')
    ax.set_zlabel(r'$\psi(x,y)$')
    plt.show()
#orbital()

#question 5
def orbital2():
    x = np.linspace(-20,20,100)
    y = np.linspace(-20,20,100)[:,np.newaxis]
    r = np.sqrt(x**2+y**2)
    psi = x*(6-r)*np.exp(-r/3)
    plt.imshow(psi)
    plt.show()
#orbital2()

#question 6
def scatter():
    r = 5
    theta = np.linspace(0,np.pi,50)
    phi = np.linspace(0,2*np.pi,50)[:,np.newaxis]
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    plt.figure(figsize=(10,10))
    ax = plt.axes(projection='3d')
    ax.scatter(x,y,z,s=10,c='m')
    psize = 6.0
    ax.set_xlim(-psize,psize)
    ax.set_ylim(-psize,psize)
    ax.set_zlim(-psize,psize)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('cool scatter plot(hopefully)')
    plt.show()
#scatter()

#question 7
def particles():
    class Particle:
        def __init__(self,x=0.0,y=0.0):
            self.x = x
            self.y = y
    cparts = []
    for x in np.linspace(-5,5,40):
        for y in np.linspace(-5,5,40):
            if np.sqrt(x**2 + y**2) <= 5 and np.sqrt(x**2+y**2)>=3:
                cparts.append(Particle(x,y))
    for p in cparts:
        plt.plot(p.x,p.y,'mo')
    plt.xlabel('x')
    plt.ylabel('y')
    ax = plt.gca()       
    ax.axis('equal')
    plt.show()

    cparts2 = []
    n = 100
    r=10
    for theta in np.linspace(0,2*np.pi,n):
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        cparts2.append(Particle(x,y))
    for p in cparts2:
        plt.plot(p.x,p.y,'mo')
    plt.xlabel('x')
    plt.ylabel('y')
    ax2 = plt.gca()       
    ax2.axis('equal')
    plt.show()
#particles()

#question 8
def right():
    class RightTriangle:
        def __init__(self,l1,l2):
            self.x = l1
            self.y = l2
        def hyp(self):
            h = np.sqrt(self.x**2+self.y**2)
            return h
        def angle1(self):
            theta = np.arctan(self.y/self.x)
            t = theta*180/np.pi
            return t
        def angle2(self):
            theta = np.arctan(self.x/self.y)
            t = theta*180/np.pi
            return t
    t = RightTriangle(2,1)
    print(t.hyp())
    print(t.angle1())
    print(t.angle2())
#right()