import homcloud.interface as hc  # HomCloudのインターフェス
import numpy as np
import matplotlib.pyplot as plt

filename='test'

pdlist = hc.PDList("{}.pdgm".format(filename))
pd1 = pdlist.dth_diagram(1)
pd1.histogram().plot(colorbar={"type": "log"})
plt.savefig("{}_1.png".format(filename))
np.savetxt('{}_b_1.txt'.format(filename),pd1.births,header='b')
np.savetxt('{}_d_1.txt'.format(filename),pd1.deaths,header='d')
#plt.show()
#plt.figure()
print("end")