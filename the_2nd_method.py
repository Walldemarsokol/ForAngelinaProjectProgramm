import math
from the_3_step import the_3_step

def the_2nd_method(input_list,length):
    g=[]
    k=1
    L=[]
    for i in range(length): 
        g.append(input_list[i])
        a=math.factorial(k)
        k+=1
        z=0
        y=the_3_step(a,g,z)
        L.append(y)
    return L
    