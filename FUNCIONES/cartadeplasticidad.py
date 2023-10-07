import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.path as ph
from scipy.interpolate import interp1d
from valoresdeentrada import *

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
Limite_liquido = 60
Indice_plasticidad = 40

plt.plot(Limite_liquido,Indice_plasticidad,'ro')
plt.vlines(Limite_liquido,0,60,'k','--')                                          
plt.annotate('LL',(Limite_liquido,55))
plt.annotate('IP',(20,Indice_plasticidad + 2))
plt.hlines(Indice_plasticidad,0,100,'k','--')
plt.xlim(0,100)
plt.ylim(0,60)
x=np.array([0,100])
LineaA = 0.73*(x-20)
LineaU = 0.9*(x-8)
plt.annotate('LineaA',(90,50),rotation=38)
plt.annotate('LineaU',(60,45),rotation=45) 
plt.plot(x, LineaA, 'darkblue', label = "Linea A" )
plt.plot(x, LineaU, 'k:', label = "Linea U")
plt.hlines(7,15.7,29.5,'m')
plt.hlines(4,12.4,25.5,'m')
plt.annotate('CL-ML',(15,5))
plt.annotate('MH',(80,20))
plt.annotate('CL',(30,15))
plt.annotate('CH',(62,40))
plt.annotate('ML',(35,5))
plt.annotate('NO EXISTE',(15,35))
plt.vlines(50,0,60,'g')
d=[50,50,100,100]
e=[0,22,58,0]
plt.fill(d,e,'pink')
f=[25.5,12.4,8,20,50,50]
g=[4,4,0,0,0,22]
plt.fill(f,g,'lightgray')
h=[50,100,100,75,50]
i=[22,58,60,60,38]
plt.fill(h,i,'lightgreen')
j=[29.5,15.7,12.4,25.5]
k=[7,7,4,4]
plt.fill(j,k,'m')
l=[15.7,29.5,50,50]
m=[7,7,22,38]
plt.fill(l,m,'bisque')
plt.title("Carta de plasticidad",fontsize=10)
plt.xlabel("Limite liquido",fontsize=10)
plt.ylabel("Indice de plasticidad",fontsize=10)
plt.legend()
plt.show()