import homcloud.interface as hc  # HomCloudのインターフェス
import numpy as np
import matplotlib.pyplot as plt
import homcloud.paraview_interface as pv


filename='test'


pointcloud = np.loadtxt('{}.txt'.format(filename))
pointcloud.shape
hc.PDList.from_alpha_filtration(pointcloud, save_to="{}.pdgm".format(filename),save_boundary_map=True,weight=True,no_squared=True)
#pv.show([pv.PointCloud.from_array(pointcloud)])
print("end")