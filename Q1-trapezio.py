# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:00:59 2020

@author: romul
"""

def f(x):
  r = 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)
  return r

def h(x0,x1):
  return x1-x0

def trapezio(x0,x1):
  It = (h(x0,x1)/2)*(f(x0)+f(x1))
  return It

def main():
  
  x0 = 0
  x1 = 0.8
  m = 4
  
  print("Solução:",trapezio(x0,x1))


if __name__ == "__main__":
  main()
  
input("Clique para finalizar.")