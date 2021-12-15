import homcloud.interface as hc  # HomCloudのインターフェス
import numpy as np
import matplotlib.pyplot as plt

filename='test'

pdlist = hc.PDList('{}.pdgm'.format(filename))
pd0 = pdlist.dth_diagram(0)
pd0.histogram().plot(colorbar={"type": "log"})
plt.savefig("{}_0.png".format(filename))

np.savetxt("{}_b_0.txt".format(filename),pd0.births,header='b')
np.savetxt("{}_d_0.txt".format(filename),pd0.deaths,header='d')

#plt.show()
plt.figure()
print("end")