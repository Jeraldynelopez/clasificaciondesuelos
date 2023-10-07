import pandas as pd
import matplotlib.path as mpath
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d 

from valoresdeentrada import *


acumulado = [retenido[0]]
for i in range(1, len(retenido)):
    acumulado.append(acumulado[i-1] + retenido[i])
retenido_acumulado = pd.Series(acumulado)

acumulado_porcentaje = [acumulado[-1] - retenido[0]]
for i in range(1, len(retenido)):
    acumulado_porcentaje.append(acumulado_porcentaje[i-1] - retenido[i])
pasa = pd.Series(acumulado_porcentaje)

pasa 

granulometria1 = pd.DataFrame({
    'Malla': malla,
    'Abertura': abertura,
    'Retenido': retenido,
    'Retenido Acumulado': retenido_acumulado,
    'Pasa': pasa,
    
})

peso_total = granulometria1['Retenido'].sum()

porcentaje_pasa = (pasa / peso_total) * 100
granulometria = pd.DataFrame({
    'Malla': malla,
    'Abertura': abertura,
    'Retenido': retenido,
    'Retenido Acumulado': retenido_acumulado,
    'Pasa': pasa,
    '% Pasa': porcentaje_pasa
})

print(granulometria)


TMP= np.array([
    4.750, #Abertura Tamiz 4
    2.000, #Abertura Tamiz 10
    0.850, #Abertura Tamiz 20
    0.425, #Abertura Tamiz 40
    0.250, #Abertura Tamiz 60
    0.106, #Abertura Tamiz 140
    0.075, #Abertura Tamiz 200
    0, #Fondo
])

plt.figure(figsize=(14, 4)) 
plt.plot(TMP, porcentaje_pasa, linestyle='-', marker='o', color='r', fillstyle='none',label='Datos') 
f = interp1d(porcentaje_pasa, TMP)

y1_coord = 60
y2_coord = 30
y3_coord = 10

x1_coord = f(y1_coord)
x2_coord = f(y2_coord)
x3_coord = f(y3_coord)

x1_coord = x1_coord.astype(np.float_)

x1_formatted = '{:.2f}'.format(x1_coord)
x2_formatted = '{:.2f}'.format(x2_coord)
x3_formatted = '{:.2f}'.format(x3_coord)
 
plt.scatter(x1_coord, y1_coord, marker='s', s=50, color='k', label='D60='+x1_formatted)
plt.scatter(x2_coord, y2_coord, marker='<', s=50, color='k', label='D50='+x2_formatted)
plt.scatter(x3_coord, y3_coord, marker='>', s=50, color='k', label='D30='+x3_formatted)

plt.title("",fontsize=12)
plt.xlabel('Diámetro (mm)')
plt.ylabel('Porcentaje pasa acumulado (%)')
plt.title('CURVA GRANULOMETRICA')
plt.legend() 
plt.xscale("log")
plt.xlim(0.075,4.75)
plt.ylim(0,100) 
plt.grid(color='k',lw='0.1',ls='-')

ax1 = plt.gca()
ax1.invert_xaxis()

ax2 = ax1.twiny()
ax2.set_xscale('log')
ax2.set_xticks(TMP)
ax2.set_xticklabels(malla, rotation=90, fontsize=9)

ax2.set_xlabel('Tamices')
ax2.set_xlim(0.075,4.75)
ax2.invert_xaxis()

L_No10 = ([4.75,4.75]) 
L_No20 = ([2,2]) 
L_No40 = ([0.850,0.850]) 
L_No60 = ([0.425,0.425])
L_No140 = ([0.106,0.106])  
L_rango = ([0,100])

plt.plot(L_No10, L_rango, color='grey', lw='0.8', ls='--')
plt.plot(L_No20, L_rango, color='grey', lw='0.8', ls='--') 
plt.plot(L_No40, L_rango, color='grey', lw='0.8', ls='--')
plt.plot(L_No60, L_rango, color='grey', lw='0.8', ls='--')
plt.plot(L_No140, L_rango, color='grey', lw='0.8', ls='--')

plt.text(4.73, 2, 'Grava(Fina)', fontsize=8, rotation=90)
plt.text(1.96, 2, 'Arena(Gruesa)', fontsize=8, rotation=90)
plt.text(0.416, 2, 'Arena(Mediana)', fontsize=8, rotation=90)
plt.text(0.074, 2, 'Arena(Fina)', fontsize=8, rotation=90)

x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
for x in x_values:
    plt.axvline(x=x, color='grey', ls='-', lw='0.4')

plt.show()
     