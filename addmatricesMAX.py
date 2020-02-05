# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:12:21 2020

@author: UseR
"""





def main():
    import numpy as np
    a=np.arange(42).reshape(7,6)
    b=np.arange(22).reshape(11,2)
    maxrow=0
    maxcolumn=0
    if (a.shape[0]>b.shape[0]):
        maxrow=a.shape[0]
    else: maxrow=b.shape[0]
    if (a.shape[1]>b.shape[1]):
        maxcolumn=a.shape[1]
    else: maxcolumn=b.shape[1]
    c=np.zeros((maxrow,maxcolumn))
    for row in range(a.shape[0]):
        for column in range(a.shape[1]):
            c[row][column]+= a[row][column]
    for row in range(b.shape[0]):
        for column in range(b.shape[1]):
            c[row][column]+= b[row][column]
    print(c)
    
    
    
    
if __name__ == '__main__':
    main()