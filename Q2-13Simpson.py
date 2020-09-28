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

def um_terco_simpson(x0,x1):
  
  xa = (x0+x1)/2
  
  Is = ( h(x0,x1)/3 ) * ( f(x0) + 4*f(xa) + f(x1) )
  
  return Is

def main():
  
  x0 = 0
  x1 = 0.8

  print("Solução:",um_terco_simpson(x0,x1))
if __name__ == "__main__":
  main()
  
input("Clique para finalizar.")