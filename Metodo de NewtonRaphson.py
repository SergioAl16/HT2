# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
20/07/2023

Metodo de Newton Raphson
"""

from pylab import *
from tabulate import tabulate

def newtonRaphson(f, fprima, x0, n, d):
        """Es un algoritmo numérico para encontrar raíces de funciones continuas y diferenciables. 
        Se basa en utilizar la tangente a la curva de la función en un punto cercano a la raíz 
        como una aproximación lineal de la función. Luego, se encuentra el punto donde esta 
        tangente cruza el eje x y se repite el proceso para obtener una aproximación mejorada. 
        Requiere un valor inicial de aproximación y la derivada de la función en el punto dado."""
    
        xi = float(x0)
        
        tabla = [['i','xi','ea'],[0,xi,]]
        
        for i in range(n):
            
            x = xi
            fxi = eval(f)
            
            fprimaxi = eval(fprima)
            
            xii  = xi - fxi/fprimaxi
            
            ea = abs((xii-xi)/xii)*100
            
            fila = [i+1,xii,ea]
            redondeados = []
            
            for elemento in fila:
                redondeados.append(round(elemento,d))
                
            tabla.append(redondeados)
                
            xi = xii
                
        print(tabulate(tabla))
            
# Ejemplo de uso
# newtonRaphson("e**(-x)-x", "-e**(-x)-1", 1,10,5)

# Problema 3 HT2
# newtonRaphson("-25 + 82*x - 90*(x**2) + 44*(x**3) - 8*(x**4)", "82-180*x+132*(x**2)-32*(x**3)", 0.5, 10, 4)
# newtonRaphson("-25 + 82*x - 90*(x**2) + 44*(x**3) - 8*(x**4)", "82-180*x+132*(x**2)-32*(x**3)", 2.25, 10, 4)

# Problema 4 HT2
# newtonRaphson("2*(x**3) - 11.7*(x**2)+17.7*(x) - 5", "6*(x**2)-23.4*(x) + 17.7", 3.55, 10, 4)