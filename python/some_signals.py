import numpy as np
from scipy.interpolate import CubicSpline 

def getDynamicSignal(N=1000):
  a=np.arange(0,1,0.1)
  a_interp = np.linspace(a[0], a[-1], N)
  b=(np.random.rand(len(a))-0.5)*0.1+1
  spl = CubicSpline(a,b)
  b_interp = spl(a_interp)
  return a_interp, b_interp
