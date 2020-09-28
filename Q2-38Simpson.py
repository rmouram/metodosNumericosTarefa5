# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:55:00 2020

@author: romul
"""
def f(x):
  r = 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)
  return r

def h(x0,x1):
  return (x1-x0)/3

def um_terco_simpson(x0,x1):
  
  altura = h(x0,x1)
  
  Is = ( (3*altura)/8 ) * ( f(x0) + 3*f(altura) + 3*(f(2*altura)) + f(x1) )
  return Is

def main():
  
  x0 = 0
  x1 = 0.8

  print("Solução:",um_terco_simpson(x0,x1))
if __name__ == "__main__":
  main()
  
input("Clique para finalizar.")