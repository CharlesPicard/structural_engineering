# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
from scipy import interpolate

def am_3d_square_prism(a,b):
    """
    """
    xi = b/a
    data = np.array([[1.00,0.68],
                     [2.00,0.36],
                     [3.00,0.24],
                     [4.00,0.19],
                     [5.00,0.15],
                     [6.00,0.13],
                     [7.00,0.11],
                     [10.0,0.08]])
    
    x = data[:,0]
    y = data[:,1]
    
    # Define an interpolation function
    interpolation_function = interpolate.interp1d(x,y,
                                                  kind='quadratic',
                                                  bounds_error=False,
                                                  fill_value=(y[0], y[-1]))
    Ca = interpolation_function(xi)
    
    Vr = a**2*b
    
    return Ca,Vr


def am_3d_circular_cylinder(a,b):
    """
    """
    xi = b/(2*a)
    data = np.array([[1.20,0.62],
                     [2.50,0.78],
                     [5.00,0.90],
                     [9.00,0.96],
                     [99.00,1.00]])
    
    x = data[:,0]
    y = data[:,1]
    
    # Define an interpolation function
    interpolation_function = interpolate.interp1d(x,y,
                                                  kind='quadratic',
                                                  bounds_error=False,
                                                  fill_value=(y[0], y[-1]))
    Ca = interpolation_function(xi)
    
    Vr = np.pi*a**2*b
    
    return Ca,Vr
  
def am_3d_rectangular_plates(a,b):
    """
    """
    xi = b/(a)
    data = np.array([[1.00,0.579],
                     [1.25,0.642],
                     [1.50,0.690],
                     [1.59,0.704],
                     [2.00,0.757],
                     [2.50,0.801],
                     [3.00,0.830],
                     [3.17,0.840],
                     [4.00,0.872],
                     [5.00,0.897],
                     [6.25,0.917],
                     [8.00,0.934],
                     [10.0,0.947],
                     [99.0,1.00]])
    
    x = data[:,0]
    y = data[:,1]
    
    # Define an interpolation function
    interpolation_function = interpolate.interp1d(x,y,
                                                  kind='quadratic',
                                                  bounds_error=False,
                                                  fill_value=(y[0], y[-1]))
    Ca = interpolation_function(xi)
    
    Vr = np.pi*a**2*b/4.
    
    return Ca,Vr
  
def am_2d_I_beam(a,b,c):
    """
    """
    xi = b/a
    zi = c/a
    data = np.array([[1.00,0.579],
                     [1.25,0.642],
                     [1.50,0.690],
                     [1.59,0.704],
                     [2.00,0.757],
                     [2.50,0.801],
                     [3.00,0.830],
                     [3.17,0.840],
                     [4.00,0.872],
                     [5.00,0.897],
                     [6.25,0.917],
                     [8.00,0.934],
                     [10.0,0.947],
                     [99.0,1.00]])
    
    x = data[:,0]
    y = data[:,1]
    
    # Define an interpolation function
    interpolation_function = interpolate.interp1d(x,y,
                                                  kind='quadratic',
                                                  bounds_error=False,
                                                  fill_value=(y[0], y[-1]))
    Ca = interpolation_function(xi)
    
    Vr = np.pi*a**2*b/4.
    
    return Ca,Vr



"""
test functions
"""   
print(am_3d_square_prism(4,2))
    
xnew = np.linspace(0, 50, num=1000, endpoint=True)
import matplotlib.pyplot as plt
plt.plot(xnew, am_3d_circular_cylinder(1,xnew)[0], '-')
plt.plot(xnew, am_3d_rectangular_plates(1,xnew)[0], '--')



def am_2d_I_beam(H,B,tp,L):
    """
    """
    #am_2d_I_beam
    c = H-tp
    a = B
    b = tp
    x_1 = np.array([0.1,0.2,0.4,1.0])
    y_1 = np.array([0.5,1.0,1.5,2.0,3.0,4.0])
    z_1 = np.array([[4.7, 2.6 , 1.3 ,np.NAN],
                  [5.2, 3.2 , 1.7 ,0.6],
                  [5.8, 3.7 , 2.0 ,0.7],
                  [6.4, 4.0 , 2.3 ,0.9],
                  [7.2, 4.6 , 2.5 ,1.1],
                  [np.NAN, 4.8 , np.NAN ,np.NAN]])
    
    
    
    
