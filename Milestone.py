from math import *
import numpy as np
f = open("/content/Testcase1.txt",'r')
lines = f.readlines()
WaferDia = int(lines[0].split(':')[1])//2
DieSize= int(lines[1].split(':')[1].split('x')[0]),int(lines[1].split(':')[1].split('x')[1])
DieShift = int(lines[2].split(':')[1].split(',')[0].split('(')[1]),int(lines[2].split(':')[1].split(',')[1].split(')')[0])
RefShift = int(lines[3].split(':')[1].split(',')[0].split('(')[1]),int(lines[3].split(':')[1].split(',')[1].split(')')[0])
DiePoints = []
fw = open("Output1.txt",'w')
x =-WaferDia//DieSize[0]
for i in range(-WaferDia,WaferDia,DieSize[0]):
  y= -WaferDia//DieSize[1]
  for j in range(-WaferDia,WaferDia,DieSize[1]):
      if i**2 + j**2 <= WaferDia**2:
        val = str((x,y))+':'+str((i,j))+'\n'
        fw.write(val)
      y+=1
  x+=1
