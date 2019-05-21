import numpy as np
import csv

file = open('www.txt','r')
contents = file.readlines()
a = ['time']
b = ['100.0']

for item in contents:
    cont = item.split()
    part = cont[0]
    val = cont[1]
    a.append(cont[0])
    b.append(cont[1])
output = np.row_stack((a, b))
writer = csv.writer(open('qtmd.csv', 'w'))
writer.writerows(output)
print(a)