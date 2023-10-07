import pandas as pd
import matplotlib.path as mpath
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d # herramientas para interlopacion de datos 


from valoresdeentrada import *
from FUNCIONES.granulometria import *
from FUNCIONES.cartadeplasticidad import *



Tamiz_200 = porcentaje_pasa[6]
Tamiz_4 = porcentaje_pasa[0]
CU = int(input("Ingrese el CU: "))
CC = int(input("Ingrese el CC: "))

def CartaPlasticidad():
  LL = int(input("Ingrese el limite liquido: "))
  IP= int(input("Ingrese el indice de plasticidad: "))
  LineaA =0.73*(LL-20)
  LineaU = 0.9*(LL-8)
  if LL > 50:  #Alta plasticidad 
    if 0 < IP < LineaA:
      print("MH")
    elif LineaA < IP < LineaU:
      print("CH")
    else:
      print("EL SUELO NO EXISTE")

  else: #Baja plasticidad
    print("Baja plasticidad")
  CartaPlasticidad(LL,IP)

if Tamiz_200 > 50 :
  CartaPlasticidad()
else: 
  if Tamiz_4 > 50:

    if Tamiz_200<5 :
      if CU > 6 and CC < 3:
        print("SW")
      else:
        print("SP")

    elif 5<Tamiz_200<12 and CC<3:
            if CU > 6 and CC < 3:
             print("SW")
             print(CartaPlasticidad())
            else:
             print("SP")
            CartaPlasticidad()
        
    else: 
      CartaPlasticidad()


  else: 
    print ("Gravas")

