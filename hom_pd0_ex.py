import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm

filename='test'

Birth=open('{}_b_0.txt'.format(filename),'r')
Death=open('{}_d_0.txt'.format(filename),'r')


B=[]
while True:
    B_datalist = Birth.readline()
    if "#" in B_datalist:
        continue
    if B_datalist=='':
        break
    A=float(list(map(str,B_datalist.split()))[0])
    B.append(A)
Birth.close()

D=[]
while True:
    D_datalist = Death.readline()
    if "#" in D_datalist:
        continue
    if D_datalist=='':
        break
    A=float(list(map(str,D_datalist.split()))[0])
    D.append(A)
Death.close()
L=len(B)
l=len(D)
if L!=l:
    print("Num error")



x=B
y=D
fig = plt.figure()
ax = fig.add_subplot(121)



H = ax.hist2d(x,y, bins=[np.linspace(-15,0,30),np.linspace(-15,40,300)], norm=matplotlib.colors.LogNorm(), cmap=cm.rainbow)
#H = ax.hist2d(x,y, bins=[np.linspace(x範囲下限,x範囲上限,x方向のメッシュ),np.linspace(y範囲下限,y範囲上限,y方向のメッシュ)], norm=matplotlib.colors.LogNorm(), cmap=cm.jet)


ax.set_xlabel('Birth')
ax.set_ylabel('Death')

fig.colorbar(H[3])
plt.savefig("{}__0.png".format(filename))
plt.show()
# 表示する

##############################
inf=10**8
Body_dmax=-inf
Body_dmin=inf
Add_dmax=-inf
Add_dmin=inf
for i in range(len(B)):
    if B[i]==-5:
        Body_dmax=max(Body_dmax,D[i])
        Body_dmin=min(Body_dmin,D[i])
    if B[i]==-1:
        Add_dmax=max(Add_dmax,D[i])
        Add_dmin=min(Add_dmin,D[i])

print("end")