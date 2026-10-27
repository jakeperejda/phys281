import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from dfit import Dfit
import pandas as pd

#question 2
def decay():
    data1 = pd.read_excel('/Users/jakeperejda/course281/datafiles/decay1.xlsx')
    data2 = pd.read_excel('/Users/jakeperejda/course281/datafiles/decay2.xlsx')
    t = data1['t (min)'].to_numpy()
    nn = data1['counts/min'].to_numpy()
    t2 = data2['t (min)'].to_numpy()
    nn2 = data2['counts/min'].to_numpy()
    sigma=[]
    sigma2=[]
    for x in nn:
        sigma.append(np.sqrt(float(x)))
    for x in nn2:
        sigma2.append(np.sqrt(float(x)))
    plt.errorbar(t,nn,yerr=sigma)
    plt.yscale('log')
    plt.show()
    plt.errorbar(t2,nn2,yerr=sigma2)
    plt.yscale('log')
    plt.show()
#decay()

#question 3
def dec(t,nn0,bb,tau):
    return nn0*np.exp(-t/tau)+bb
def dec2(t,nn0,tau):
    return nn0*np.exp(-t/tau)+25
def decay2():
    data1 = pd.read_excel('/Users/jakeperejda/course281/datafiles/decay1.xlsx')
    data2 = pd.read_excel('/Users/jakeperejda/course281/datafiles/decay2.xlsx')
    t = data1['t (min)'].to_numpy()
    nn = data1['counts/min'].to_numpy()
    t2 = data2['t (min)'].to_numpy()
    nn2 = data2['counts/min'].to_numpy()
    guesses=[200,25,100]
    guesses3=[200,100]
    g1 = Dfit(dec,t,nn,p0s=guesses)
    g1.plotfit(title='decay 1',xlabel='t',ylabel='nn0')
    g1.printfit()
    g2 = Dfit(dec,t2,nn2,p0s=guesses)
    g2.plotfit(title='decay 2',xlabel='t',ylabel='nn0')
    g2.printfit()
    g3 = Dfit(dec2,t,nn,p0s=guesses3)
    g3.plotfit(title='decay 1(B=25)',xlabel='t',ylabel='nn0')
    g3.printfit()
    g4=Dfit(dec2,t2,nn2,p0s=guesses3)
    g4.plotfit(title='decay 2(B=25)',xlabel='t',ylabel='nn0')
    g4.printfit()
#decay2()

#question 4
def vector():
    u=[2,0]
    v=[1,1]
    ans = u[0]*v[0]+u[1]*v[1]
    u1=np.array([2,0])
    v1=np.array([1,1])
    ans1 = u1@v1
    return f'manual answer:{ans}\nnumpyanswer:{ans1}'
#print(vector())

#question 5
def matrix():
    aa = np.array([[1,3],[2,4],[5,6]],float)
    bb = np.array([[2,1,4],[3,2,1]],float)
    cc = aa@bb
    dd = bb@aa
    print(f'A =\n{aa}\nB=\n{bb}\nA*B=\n{cc}\nB*A=\n{dd}')
#matrix()

#question 6
def matrix2():
    cc = np.array([[1,3,2],[2,4,1],[5,6,5]],float)
    print(cc)
    cc1=scipy.linalg.inv(cc)
    print(f'\n{cc1}')
    print(f'\n{(cc1)@(cc)}')
#matrix2()

#question 7
def linear():
    aa = np.array([[1,4,1],[4,-1,-1],[2,1,3]],float)
    rhs = [-4,3,7]
    aainv=scipy.linalg.inv(aa)
    x = aainv@rhs
    x2 = scipy.linalg.solve(aa,rhs)
    print(x)
    print(x2)
#linear()    

#question 8
def rot(x):
    return np.array([[np.cos(x),-np.sin(x)],[np.sin(x),np.cos(x)]],float)

def rotation():
    t=0
    I=rot(t)@rot(t).T
    print(f'identity of {t} is\n{I}')
    r = np.array([[1],[0]],float)
    r2 = rot(t)@r
    print(f'{r}rotated at {t} radians is\n{r2}')
#rotation()