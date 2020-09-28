# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:18:46 2020

@author: romul
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:00:59 2020

@author: romul
"""

def f(x):
  r = 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)
  return r

def h(x0,x1,m):
  return (x1-x0)/m

def trapezio_repetido(x0,x1,m):
  
  
  
  i = 1
  soma=0
  x=0
  altura = h(x0,x1,m)
  Xant=x0
  
  for i in range(m-1):
    x=Xant+altura
    Xant=Xant+altura
    soma += f(x)

  It = ( altura/2 ) * ( f(x0) + 2*soma + f(x1) )
  return It

def main():
  
  x0 = 0
  x1 = 0.8
  m = 4

  print("Solução:",trapezio_repetido(x0,x1,m))
if __name__ == "__main__":
  main()
  
input("Clique para finalizar.")