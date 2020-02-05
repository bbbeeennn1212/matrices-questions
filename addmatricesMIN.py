# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:58:04 2020

@author: UseR
"""




def main():
    import numpy as np
    a=np.arange(42).reshape(7,6)
    b=np.arange(22).reshape(11,2)
    minrow=0
    mincolumn=0
    if (a.shape[0]>b.shape[0]):
        minrow=b.shape[0]
    else: minrow=a.shape[0]
    if (a.shape[1]>b.shape[1]):
        mincolumn=b.shape[1]
    else: mincolumn=a.shape[1]
    c=np.zeros((minrow,mincolumn))
    for row in range(minrow):
        for column in range(mincolumn):
            c[row][column]+=b[row][column]+a[row][column]
    print (c)
    
    
    
    
if __name__ == '__main__':
    main()