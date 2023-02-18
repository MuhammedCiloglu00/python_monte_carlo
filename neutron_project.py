# -*- coding: utf-8 -*-
"""
Muhammed Cahit Çiloğlu
"""

import math
import random
import matplotlib.pyplot as plt 
from scipy.stats import binom

l=1;
x= l * random.random();
xd = l;
nr = 0;
nt = 0;
na = 0;
sgt = 0.2;
mu_values = [-1,1];
mu = random.choice(mu_values)
#In this part, we have opened the absorption probability list and other lists to be able to draw graphs.
pa_list = []
sampling_list = []
std_list = []
num_samples = int(input("How many samples do you want?"  ))

for j in range(1,int(num_samples)):
    for i in range(1,11):
        #In this part, we stipulate xd, that is, the maximum path that the neutron will take in the long bar, in two different ways according to the condition of the nu parameter.
        if mu > 0:
            xd = (l-x) / mu;
        else:
            xd = -x / mu; 
        x1 = -math.log(random.random()) / sgt;
        if x1 > xd:
           if mu >0:
               if random.random() > 0.6:
                   nt = nt + 1;
                   mu = random.choice(mu_values)
                   x= l * random.random(); 
               else:
                   x, xd , mu = l, l, -1
           else:
               
               if random.random() > 0.5:
                   nr = nr +1;
                   mu = random.choice(mu_values)

                   x= l * random.random();
               else:
                   x, xd , mu = 0, l, 1
        else :
            na = na + 1;
            mu = random.choice(mu_values)

            x= l * random.random()
        n = nr + na + nt ;
        if n % 10: 
            pa = na / n
            std = math.sqrt(n*pa*(1-pa))
    sampling_list.append(n)
    pa_list.append(pa)
    std_list.append(std)
    continue
    if n==num_samples:
        break
# Now let's get out of the loop and see the lists graphically
pr = nr / n
pt = nt / n  
print("Reflected neutron proportion = ", pr)
print("Absorbed neutron proportion = " , pa)
print("Transmitted neutron propotion = " , pt)
print("Standard deviation = " , std)

opt = int(input("Which chart would you like to look at? Enter 1 for the standard deviation - N graph, Enter 2 for the Pa-N graph and 3 for the Binomial distribution of Pa."))

if opt == 1 :
    plt.plot(sampling_list, std_list,linewidth=1)  
    plt.xlabel('n') 
    plt.ylabel('Std') 
    plt.title('Std - n plot') 
    plt.show() 
elif opt ==2:
    plt.plot(sampling_list, pa_list,linewidth=1)  
    plt.xlabel('n') 
    plt.ylabel('Pa') 
    plt.title('Pa - n plot') 
    plt.show() 
else:
    
    r_values = list(range(n + 1)) 
    dist = [binom.pmf(r, n, pa) for r in r_values ] 
    plt.plot(r_values, dist) 
    plt.title('Binomial distribution') 
    plt.show()