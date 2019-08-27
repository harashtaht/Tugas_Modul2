import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axis3d

df = pd.read_csv('dataPerokok.csv')
# print(df)

nama_Provinsi = [item for item in df.iloc[:,0]]
data2015 = [item for item in df.iloc[:, 1]]
data2016 = [item for item in df.iloc[:, 2]]

# print(df.describe())
valueNum = list(df.count())[0]


### Plotting 
fig = plt.figure()
ax = plt.axes(projection="3d")

x5 = np.arange(valueNum)
x6 = x5
y5 = [0]*valueNum
y6 = [1]*valueNum
z = [0]*valueNum

dx = [0.5]*valueNum #x-length of the bar
dy = [0.5]*valueNum #y-length of the bar
dz_2015 = data2015
dz_2016 = data2016

ax.bar3d(x5,y5, z, dx, dy, dz_2015)
ax.bar3d(x6,y6, z, dx, dy, dz_2016)

ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.xticks(x5, nama_Provinsi, rotation=45)
plt.yticks([0,1],['2015', '2016'])

plt.show()

