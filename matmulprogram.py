  
    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




    
def main():
    import numpy as np
    a=np.array([[2,2,1],[1,1,1],[3,2,1],[1,1,1],[1,1,1]])
    b=np.array([[1,2,2,1],[2,1,2,1],[1,1,1,1]])
    c=np.zeros((a.shape[0],b.shape[1]))
    
    print (a)
    print (b)
    size=c.shape
    for row in range(size[0]):
        for column in range(size[1]):
            for mul in range (a.shape[1]):
                c[row][column] += a[row][mul]*b[mul][column]
    print (c)
            
       
           
            
            


if __name__ == '__main__':
    main()
