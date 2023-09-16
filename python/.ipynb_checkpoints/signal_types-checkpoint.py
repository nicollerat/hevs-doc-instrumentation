import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import seaborn
from scipy.interpolate import CubicSpline
from sklearn.linear_model import LinearRegression
import numpy as np

import some_signals

a_interp,b_interp = some_signals.getDynamicSignal()


f = plt.figure(figsize=(12, 12))
gs = f.add_gridspec(2, 2)


ax = f.add_subplot(gs[0, 0])
ax.set_xlabel("temps")
ax.set_ylabel("valeur")
ax.set_title("Sortie statique")
ax.grid(True, which='both')
plt.ylim([0.95, 1.05])
plt.plot([0, 1],[1, 1])

ax = f.add_subplot(gs[0, 1])
ax.set_xlabel("temps")
ax.set_ylabel("valeur")
ax.set_title("Sortie dynamique")
ax.grid(True, which='both')
plt.ylim([0.95, 1.05])
ax.plot(a_interp,b_interp)
ax.plot(a, np.ones(len(a)))

a_lot = np.linspace(a[0], a[-1], 1000)
b_lot =(np.random.rand(len(a_lot))-0.5)*0.1+1

ax = f.add_subplot(gs[1, 0])
ax.plot(a_lot,b_lot)
ax.plot(a, np.ones(len(a)))
ax.set_xlabel("temps")
ax.set_ylabel("valeur")
ax.set_title("Sortie bruitée")
ax.grid(True, which='both')

# Sinus
a_time = np.linspace(0, 360, 1000)
b_sin =np.sin(a_time/360*np.pi*10)

ax = f.add_subplot(gs[1, 1])
ax.plot(a_time,b_sin)
ax.set_xlabel("temps")
ax.set_ylabel("valeur")
ax.set_title("Sortie sinusoïdale")
ax.grid(True, which='both')
seaborn.despine(ax=ax, offset=0)
f.tight_layout()
