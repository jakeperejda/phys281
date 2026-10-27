import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from dfit import Dfit
import pandas as pd


def func1(x,p0,p1):
    return p0 + p1*x
def func2(x,p0,p1,p2):
    return p0 +p1*x+p2*(x**2)
def func3(x,p0,p1,p2,p3):
    return p0+p1*x+p2*x**2+p3*x**3
def func4(x,p0,p1,p2,p3,p4):
    return p0+p1*x+p2*x**2+p3*x**3+p4*x**4
def func5(x,p0,p1,p2,p3,p4,p5):
    return p0+p1*x+p2*x**2+p3*x**3+p4*x**4+p5*x**5
def gauss(x,aa,x0,w,bb0,bb1):
    return aa*np.exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x
def gauss2(x,aa,x0,w,bb0,bb1,bb2):
    return aa*np.exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*x**2
def lorentz(x,aa,x0,w,bb0):
    return (aa/(1+(((x-x0)/w)**2)))+bb0
#question 2
def fit():
    data = pd.read_excel('/Users/jakeperejda/course281/datafiles/data2.xlsx')
    c0,c1,c2 = list(data)
    x = data[c0].to_numpy()
    y = data[c1].to_numpy()
    yerr = data[c2].to_numpy()
    myfit = Dfit(func5,x,y,yerr)
    myfit.plotfit(xlabel='x(cm)',ylabel='y(mV)')
    myfit.printfit()
#fit()

#question 3
def fit2():
    data = pd.read_excel('/Users/jakeperejda/course281/datafiles/data3.xlsx')
    x1,y1=list(data)
    x = data[x1].to_numpy()
    y = data[y1].to_numpy()
    myfit=Dfit(func3,x,y)
    myfit.plotfit(xlabel='x(cm)',ylabel='y(mV)')
    myfit.printfit()
#fit2()

#question 4
def fit3():
    p4data = pd.read_excel('/Users/jakeperejda/course281/datafiles/peak4.xlsx')
    print(list(p4data))
    c0,c1 = list(p4data)    # get the column names
    xs = p4data[c0].to_numpy()
    ys = p4data[c1].to_numpy()
    guesses = [1,2,3]   # parameter guesses
    p4fit = Dfit(gauss,xs,ys,p0s=guesses)
    p4fit.plotfit(xlabel=c0,ylabel=c1)
    p4fit.printfit()
#fit3()

#question 5
def fit4():
    p4data = pd.read_excel('/Users/jakeperejda/course281/datafiles/peak4.xlsx')
    print(list(p4data))
    c0,c1 = list(p4data)    # get the column names
    xs = p4data[c0].to_numpy()
    ys = p4data[c1].to_numpy()
    guesses = [2,4,3,1]   # parameter guesses
    p4fit = Dfit(gauss2,xs,ys,p0s=guesses)
    p4fit.plotfit(xlabel=c0,ylabel=c1)
    p4fit.printfit()
#fit4()

#question 6
def fit5():
    p1data = pd.read_excel('/Users/jakeperejda/course281/datafiles/gl1.xlsx')
    p2data = pd.read_excel('/Users/jakeperejda/course281/datafiles/gl2.xlsx')
    c0,c1 = list(p1data)    # get the column names
    x1 = p1data[c0].to_numpy()
    y1 = p1data[c1].to_numpy()
    c3,c4 = list(p2data)    # get the column names
    x2 = p2data[c3].to_numpy()
    y2 = p2data[c4].to_numpy()
    guesses = [2,-1,2,0]   # parameter guesses
    p1fit = Dfit(lorentz,x1,y1,p0s=guesses)
    p1fit.plotfit(xlabel=c0,ylabel=c1)
    p2fit = Dfit(lorentz,x2,y2,p0s=guesses)
    p2fit.plotfit(xlabel=c3,ylabel=c4)
    p1fit.printfit()
    p2fit.printfit()
#fit5()
#data 1 is fit better by the lorentz equation
#data 2 is fit better by the gaussian equation