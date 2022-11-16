import math
from the_3_step import the_3_step

def the_2nd_method(input_list,length):
    g=[]
    k=1
    for i in range(length): 
        g.append(input_list[i])
        print(f'check I ={i+1}')
        print(g)
        a=math.factorial(k)
        print(f'factorial={a}')
        k+=1
        z=0
        the_3_step(a,g,z)