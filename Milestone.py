
from math import *
import numpy as np
f = open("/content/Testcase1.txt",'r')
lines = f.readlines()
WaferDia = int(lines[0].split(':')[1])/2
Num = int(lines[1].split(':')[1])
Angle = int(lines[2].split(':')[1])*(2*pi)/360
Points = []
fw = open("Output1.txt",'w')
x= np.linspace(-WaferDia*cos(Angle),WaferDia*cos(Angle),Num)
for i in range(Num):
  Points.append((x[i],tan(Angle)*x[i]))
  fw.write(str(Points[-1])+'\n')
  print(str(Points[-1]))
  
