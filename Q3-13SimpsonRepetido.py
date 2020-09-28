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

def h(x0,x1,m):
  return (x1-x0)/m

def um_terco_simpson_repetido(x0,x1,m):
  altura = h(x0,x1,m)
  
  i=0
  x=x0
  soma=0
  for i in range(m):
    if (i==0 or i==m):
      c=1
    elif (i%2==0 and i!=0):
      c=2
    elif (i%2==1 and i != 0):
      c=4
    
    soma=soma+c*f(x)
    x=x+altura
    
  Isr = altura/3 * soma
  
  return Isr

def main():
  
  x0 = 0
  x1 = 0.8
  m = 4
  
  print("Solução:",um_terco_simpson_repetido(x0,x1,m))
  
if __name__ == "__main__":
  main()
  
input("Clique para finalizar.")