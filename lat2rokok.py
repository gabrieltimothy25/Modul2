import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure('Ini Persentase Perokok di Indonesia')
ax = plt.subplot(111, projection='3d')


x = []
y = []
z = []
labels = []
with open('Persentase Perokok RI.csv') as a:
    data = csv.reader(a)
    i = 0
    for d in data:
        x.append(i)
        labels.append(d[0])
        y.append(1)
        z.append(d[1])
        i += 1      

x.pop(0)
y.pop(0)
z.pop(0)

dx = [1] * len(x)
dy = [1] * len(z)
dz = np.array(z).astype(float)


kx = np.array(x).astype(float)
ky = np.array(y).astype(float)
kz = [0] * len(dx)

ax.bar3d(kx,ky,kz, 
        dx, dy, dz)
ax.set_xlabel("Provinsi")
ax.set_ylabel("Tahun")
ax.set_zlabel("Persentase Perokok %")
plt.xticks(kx, labels)

x = []
y = []
z = []
labels = []
with open('Persentase Perokok RI.csv') as a:
    data = csv.reader(a)
    i = 0
    for d in data:
        x.append(i) 
        labels.append(d[0])
        y.append(3)
        z.append(d[2])
        i += 1       


x.pop(0)
y.pop(0)
z.pop(0)

dx = [1] * len(x)
dy = [1] * len(z)
dz = np.array(z).astype(float)

kx = np.array(x).astype(float)
ky = np.array(y).astype(float)
kz = [0] * len(dx)

ax.bar3d(kx,ky,kz, 
        dx, dy, dz)
ax.set_xlabel("Provinsi")
ax.set_ylabel("Tahun")
ax.set_zlabel("Persentase Perokok")
plt.xticks(kx, labels,rotation=90)
plt.yticks([1.5, 3.5], [2015, 2016])
plt.show()