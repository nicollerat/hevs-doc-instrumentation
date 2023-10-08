# Exemple de la sonde de Pitot et sa linéarisation
# On cherche à faire une figure qui montre la courbe et le plan linéarisé


from sympy.plotting.plot import unset_show
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib import cm

sp.init_printing() # Permet d'avoir un rendu joli des équations
Pstat, rho, v, k, alpha, H, rho0, Pvit, rho_Hg = sp.symbols('Pstat rho v k alpha H rho0 Pvit rho_Hg')

rho, Ptot, g = sp.symbols('rho Ptot g')
dh=sp.Symbol('\Delta h') # on peut avoir un nom avec un espace si on utilise sp.Symbol !

eq1=sp.Eq(Ptot, Pstat+rho/2*v**2)
eq2=sp.Eq(rho, rho0*(1-k*H)**alpha)
eq3=sp.Eq(Ptot, Pstat +dh*rho_Hg*g)
[eq1, eq2, eq3]

sols=sp.solve([eq1,eq2,eq3],v, Pstat, rho)

v=sp.Lambda((dh, H),sols[1][0])

S_dh=sp.Lambda((dh,H),v(dh,H).diff(dh))
S_H=sp.Lambda((dh,H),v(dh,H).diff(H))

H0, v0=sp.symbols('H0 v0')
dh0 = sp.Symbol("\Delta h0")
vlin=sp.Lambda((dh, H),v0+S_H(dh0,H0)*(H-H0)+S_dh(dh0,H0)*(dh-dh0))

vAlpha = 5.26
vRho0=1.29
vK=22.6e-6
vg=9.81
vRho_Hg=13600

vp=v.subs(g,vg).subs(rho_Hg,vRho_Hg).subs(k,vK).subs(rho0,vRho0).subs(alpha,vAlpha).evalf()
vH0=4000
vdh0=0.0785
vV0=vp(vdh0,vH0)
vlinp=vlin.subs(g,vg).subs(rho_Hg,vRho_Hg).subs(k,vK).subs(rho0,vRho0).subs(alpha,vAlpha).subs(H0,vH0).subs(v0,vV0).subs(dh0,vdh0).evalf()

rdh=np.arange(0,0.1,0.005)
rH =np.arange(0,10000,500)

rV = np.zeros((len(rdh),len(rH)))
rVlin = np.zeros((len(rdh),len(rH)))


# Compute data
for idh in range(len(rdh)):
    for iH in range(len(rH)):
        rV[idh,iH] = vp(rdh[idh],rH[iH])
        rVlin[idh,iH] = vlinp(rdh[idh],rH[iH])

rH, rdh = np.meshgrid(rH, rdh)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface
#ax.plot_surface(rdh, rH, rV, cmap=cm.coolwarm)
ax.plot_wireframe(rdh, rH, rV, color='red')
ax.plot_wireframe(rdh, rH, rVlin, cmap=cm.gray)
ax.scatter(vdh0, vH0, vV0, marker='o')
plt.show()


