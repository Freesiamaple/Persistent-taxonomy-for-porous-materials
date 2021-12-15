import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename='test'


AZ = open('{}.txt'.format(filename), 'r')#座標のファイル名(txt)
K=[]
while True:
    AZ_datalist = AZ.readline()
    if AZ_datalist=='':
        break
    A=list(map(float,AZ_datalist.split()))
    K.append(A)
AZ.close()
X=[]
Y=[]
Z=[]
R=[]
for i in K:
    X.append(i[0])
    Y.append(i[1])
    Z.append(i[2])
    R.append(i[3])
X=np.array(X)
Y=np.array(Y)
Z=np.array(Z)
R=np.array(R)


fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')
ax.set_xlim([0,1000])
ax.set_ylim([0,1000])
ax.set_zlim([0,1000]) 
A=ax.scatter(X, Y, Z, s = R**(1/2), c=2*R**(1/2) , cmap='jet',vmin=5,vmax=20)
fig.colorbar(A)#colorbar
plt.savefig("{}.png".format(filename))
plt.show()
print("end")