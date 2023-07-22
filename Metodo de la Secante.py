# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
20/07/2023

Metodo de la Secante
"""

from pylab import *
from tabulate import tabulate

def secantMethod(f, x0, x1, n, d):
    
    xi_minus_1 = float(x0)
    xi = float(x1)
    
    tabla = [['i', 'xi', 'ea'], [-1, xi_minus_1, ], [0, xi, ]] 
    
    for i in range(n):
        
        x = xi_minus_1
        f_xi_minus_1 = eval(f)
        
        #print(f_xi_minus_1)
        
        x = xi
        f_xi = eval(f)
        
        #print(f_xi)
        
        xii = xi + f_xi * ((xi_minus_1 -xi) / (f_xi - f_xi_minus_1))
        
        ea = abs((xii - xi) / xii) * 100
        
        fila = [i+1 , xii, ea]
        redondeados = [13]
        
        for elemento in fila:
            redondeados.append(round(elemento, d))
        
        tabla.append(redondeados)
        
        xi_minus_1 = xi
        xi = xii
    
    print(tabulate(tabla))

# Ejemplo de uso
# secantMethod("sin(x)+cos(1+(x**2))-1", 2, 1.9, 10, 5)

# Problema 4 HT2
# secantMethod("2*(x**3) - 11.7*(x**2) + 17.7*(x) - 5",3.55, 3.58, 10, 4)