# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:42:35 2020

@author: romul
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:03:58 2020

@author: romul
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:48:03 2020

@author: romul
"""

def f(x):
  r = 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)
  return r

def h(x0,x1):
  return (x1-x0)/2

def quadratura(x0,x1):
  
  A = 1
  
  xA = h(x0,x1) * (-0.5744) + (x0+x1)/2
  xB = h(x0,x1) * (0.5744) + (x0+x1)/2
  
  
  I2 = h(x0,x1) * ( A*(f(xA)) + A*(f(xB)) )

  return I2

def main():
  
  x0 = 0
  x1 = 0.8
  
  print("Solução:",quadratura(x0,x1))
  
if __name__ == "__main__":
  main()
  
input("Clique para finalizar.")