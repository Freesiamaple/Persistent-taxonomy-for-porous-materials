import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm
from sklearn.cluster import DBSCAN
from scipy.stats import gaussian_kde

filename='test'

Birth=open('{}_b_1.txt'.format(filename),'r')
Death=open('{}_d_1.txt'.format(filename),'r')


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
BD = open('{}_birth_death_pair.txt'.format(filename), 'w')
for i in range(0,L):
    BD.write(str(B[i]))
    BD.write(" ")
    BD.write(str(D[i]))
    BD.write('\n')
BD.close()


x=B
y=D
fig = plt.figure()
ax = fig.add_subplot(111)



H = ax.hist2d(x,y, bins=[np.linspace(-10,80,100),np.linspace(-10,80,100)], norm=matplotlib.colors.LogNorm(), cmap=cm.rainbow)
#H = ax.hist2d(x,y, bins=[np.linspace(x範囲下限,x範囲上限,x方向のメッシュ),np.linspace(y範囲下限,y範囲上限,y方向のメッシュ)], norm=matplotlib.colors.LogNorm(), cmap=cm.jet)

#ax.set_title('title')
ax.set_xlabel('Birth')
ax.set_ylabel('Death')

fig.colorbar(H[3])
plt.savefig("{}__1.png".format(filename))
plt.figure() 
#plt.show()
# 表示する
##################################################
#H値 

#重心
xc=sum(B)/len(B)
yc=sum(D)/len(D)
#print("xc,yc=",xc,yc)

#hmax
hmax=0
for i in range(len(B)):
    hmax=max(hmax,D[i]-B[i])
    

h1=(1/(2**(1/2)))*(yc-xc)
h2=2**(1/2)*xc
Hvalue=(h1**2+h2**2)**(1/2)/hmax
#print("H=",Hvalue)
##############################
C_list=[]

for i in range(len(B)):
  c1=(1/(2**(1/2)))*(D[i]-B[i])
  c2=2**(1/2)*B[i]
  c=(c1**2+c2**2)**(1/2)
  C_list.append(c)
C_list.sort(reverse=True)

ar=np.array(C_list)

plt.hist(ar, bins=100,range=(0,180))

plt.savefig("{}_C.png".format(filename))
#plt.show()
print("end")