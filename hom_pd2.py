import homcloud.interface as hc  # HomCloudのインターフェス
import numpy as np
import matplotlib.pyplot as plt

filename='test'

pdlist = hc.PDList("{}.pdgm".format(filename))
pd2 = pdlist.dth_diagram(2)
pd2.histogram().plot(colorbar={"type": "log"})
plt.savefig("{}_2.png".format(filename))
np.savetxt('{}_b_2.txt'.format(filename),pd2.births,header='b')
np.savetxt('{}_d_2.txt'.format(filename),pd2.deaths,header='d')
#plt.show()
#plt.figure()
print("end")