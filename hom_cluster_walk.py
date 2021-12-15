import random
import math

filename="test"


x_center=500
x_range =500
y_center=500
y_range =500
z_center=500
z_range =500


r_edge=10
r=2
step=r
walk_num=20
cluster_num=1

RO = open(('{}.txt'.format(filename)), 'w')
def random_walk(n):
    random.seed(n+2)#乱数を固定
    x=random.uniform(x_center-x_range,x_center+x_range)
    y=random.uniform(y_center-y_range,y_center+y_range)
    z=random.uniform(z_center-z_range,z_center+z_range)
    RO.write(str(x))
    RO.write(' ')
    RO.write(str(y))
    RO.write(' ')
    RO.write(str(z))
    RO.write(' ')
    RO.write(str((r_edge/2)**2))
    RO.write('\n')
    θ=random.uniform(0,180)
    Φ=random.uniform(0,180)
    x+=(r_edge+step)*math.sin(math.radians(θ))*math.cos(math.radians(Φ))
    y+=(r_edge+step)*math.sin(math.radians(θ))*math.sin(math.radians(Φ))
    z+=(r_edge+step)*math.cos(math.radians(θ))
    RO.write(str(x))
    RO.write(' ')
    RO.write(str(y))
    RO.write(' ')
    RO.write(str(z))
    RO.write(' ')
    RO.write(str((r/2)**2))
    RO.write('\n')

    for i in range(walk_num-1):
        θ=random.uniform(0,180)
        Φ=random.uniform(0,180)
        x+=(step)*math.sin(math.radians(θ))*math.cos(math.radians(Φ))
        y+=(step)*math.sin(math.radians(θ))*math.sin(math.radians(Φ))
        z+=(step)*math.cos(math.radians(θ))
        RO.write(str(x))
        RO.write(' ')
        RO.write(str(y))
        RO.write(' ')
        RO.write(str(z))
        RO.write(' ')
        RO.write(str((r/2)**2))
        RO.write('\n')
    x+=(r_edge+step)*math.sin(math.radians(θ))*math.cos(math.radians(Φ))
    y+=(r_edge+step)*math.sin(math.radians(θ))*math.sin(math.radians(Φ))
    z+=(r_edge+step)*math.cos(math.radians(θ))
    RO.write(str(x))
    RO.write(' ')
    RO.write(str(y))
    RO.write(' ')
    RO.write(str(z))
    RO.write(' ')
    RO.write(str((r_edge/2)**2))
    RO.write('\n')
    
for k in range(cluster_num):
    random_walk(k)



#body
x_center_b=500
x_range_b =500

y_center_b=500
y_range_b =500

z_center_b=500
z_range_b =500

body_num=1000
body_r=25

random.seed(1)#乱数を固定
for j in range(body_num):
    RO.write(str(random.uniform(x_center_b - x_range_b,x_center_b + x_range_b)))
    RO.write(' ')
    RO.write(str(random.uniform(y_center_b - y_range_b,y_center_b + y_range_b)))
    RO.write(' ')
    RO.write(str(random.uniform(z_center_b - z_range_b,z_center_b + z_range_b)))
    RO.write(' ')
    RO.write(str(body_r))
    RO.write('\n')
RO.close()