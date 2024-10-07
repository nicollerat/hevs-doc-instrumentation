import numpy as np
import matplotlib.pyplot as plt

# pip install numpy matplotlib

x=np.array([1, 3, 5])
y=np.array([2,3,5])

S1=3
Sx=np.sum(x)
Sy=np.sum(y)
Sxy=np.sum(x*y)
Sxx=np.sum(x**2)
D=S1*Sxx-Sx**2

print([S1, Sx, Sy, Sxy, Sxx, D])

a=(S1*Sxy-Sx*Sy)/D
b=(Sy*Sxx-Sx*Sxy)/D  

print(f"a={a}, b={b}")

ylin=a*x+b

plt.plot(x,y)
plt.plot(x,ylin)
plt.grid()
plt.show()