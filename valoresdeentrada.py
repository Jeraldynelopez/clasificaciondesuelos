import pandas as pd
import matplotlib.path as mpath
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d 

malla = pd.Series([
    "#4",  # Tamiz 4
    "#10", # Tamiz 10
    "#20", # Tamiz 20
    "#40", # Tamiz 40
    "#60", # Tamiz 60
    "#140", # Tamiz 140
    "#200", # Tamiz 200
    "fondo" # Fondo
])

abertura = pd.Series([
    "4.750", # Abertura Tamiz 4
    "2.000", # Abertura Tamiz 10
    "0.850", # Abertura Tamiz 20
    "0.425", # Abertura Tamiz 40
    "0.250", # Abertura Tamiz 60
    "0.106", # Abertura Tamiz 140
    "0.075", # Abertura Tamiz 200
    "0" # Fondo
])

retenido = pd.Series([
    95, # Tamiz #4
    84, # Tamiz #10
    58, # Tamiz #20
    35, # Tamiz #40
    18, # Tamiz #60
    9,  # Tamiz #140
    5,  # Tamiz #200
    60  # Fondo
    
])