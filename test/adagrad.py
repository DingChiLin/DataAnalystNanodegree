from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def func(x,y):
  return (y**2-x**2)

def plot_func(xt,yt,c='r'):
  fig = plt.figure()
  ax = fig.gca(projection='3d',
        elev=35., azim=-30)
  X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
  Z = func(X,Y) 
  surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
    cmap=cm.coolwarm, linewidth=0.1, alpha=0.3)
  ax.set_zlim(-50, 50)
  ax.scatter(xt, yt, func(xt,yt),c=c, marker='o' )
  ax.set_title("x=%.5f, y=%.5f, f(x,y)=%.5f"%(xt,yt,func(xt,yt))) 
  plt.show()
  plt.close()

def run_grad():
  xt = 0.001 
  yt = 4 
  eta = 0.3 
  plot_func(xt,yt,'r')
  for i in range(20):
    xt = xt - eta*(-2*xt)
    yt = yt - eta*(2*yt) 
    if xt < -5 or yt < -5 or xt > 5 or yt > 5:
      break
    plot_func(xt,yt,'r')

def run_adagrad():
  xt = 0.001
  yt = 4 
  eta = 1.0 
  Gxt = 0
  Gyt = 0
  plot_func(xt,yt,'b')
  for i in range(20):
    gxt = (-2*xt)
    gyt = (2*yt)
    Gxt += gxt**2
    Gyt += gyt**2
    xt = xt - eta*(1./(Gxt**0.5))*gxt
    yt = yt - eta*(1./(Gyt**0.5))*gyt
    if xt < -5 or yt < -5 or xt > 5 or yt > 5:
      break
    plot_func(xt,yt,'b')

