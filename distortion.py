#!/usr/bin/env python
'''
To produce volumn data (like CHGCAR) to show 
the lattice distortion bewteen too twin structures.
by lmliu@mail.ustc.edu.cn
'''
import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# get lattice parameters
# -----------------------------------------------------------
def read_poscar(file_name):
  poscar = open(file_name, 'r')
  for i in range(2):     # skip 2 rows
    poscar.readline()

  latt = np.zeros((3,3))
  for i in range(3):
    latt[i] = np.array(poscar.readline().split(), dtype=float)

  poscar.readline()      # skip elemental symbol line

  N = np.array(poscar.readline().split(), dtype=int).sum()
  poscar.close()
  #pos = np.loadtxt(file_name, skiprows=9, usecols=(0, 1, 2)[0:N, :]
  return latt, N

# Get grid number
# -------------------------------------------------------------
def get_gridnumber(OUTCAR):
  outcar = open('OUTCAR', 'r')
  for i in outcar.readlines():
    if 'NGXF= ' in i:
      NGX, NGY, NGZ = re.findall('(\d+)', i)
  outcar.close()    
  return NGX, NGY, NGZ

# interpolation
# -------------------------------------------------------------
def interpolator(latt, NGX, NGY, NGZ, ini_pos_cart, diff_s):
  grid = []
  for i in np.linspace(0, np.sqrt(np.dot(latt[2], latt[2].T)), NGZ):
    for j in np.linspace(0, np.sqrt(np.dot(latt[1], latt[1].T)), NGY):
      for k in np.linspace(0, np.sqrt(np.dot(latt[0], latt[0].T)),NGX):
        grid.append([k, j, i])
  grid_array = np.array(grid, dtype='float')
  np.savetxt('grid', grid) 
  return griddata(ini_pos_cart, diff_s, grid_array, method='linear', fill_value=0.)  # only give 0

# MAIN
# ============================================================
ini_latt, ini_N = read_poscar('POSCAR')
ini_pos = np.loadtxt('POSCAR', skiprows=9, usecols=(0, 1, 2))[0:ini_N, :]
ini_pos_cart = np.dot(ini_latt, ini_pos.T).T

fin_latt, fin_N = read_poscar('CONTCAR')
fin_pos = np.loadtxt('CONTCAR', skiprows=9, usecols=(0, 1, 2))[0:fin_N, :]
fin_pos_cart = np.dot(fin_latt, fin_pos.T).T

diff_v = fin_pos_cart - ini_pos_cart
diff_s = np.sqrt(np.dot(diff_v, diff_v.T).diagonal())
np.savetxt('diff_s', diff_s)

#NGX, NGY, NGZ = get_gridnumber('OUTCAR')
NGX, NGY, NGZ = 20,30,50

data = interpolator(ini_latt, NGX, NGY, NGZ, ini_pos_cart, diff_s)

np.savetxt('volumn_data', data.reshape(-1,10))



# plot
# ------------------------------------------------------------
#plt.scatter3D(ini[:,0], ini[:,1], ini[:,2])
#plt.imshow(ip.T, origin='lower', extent=(0, lyz[0,0], 0, lyz[1,1]))
#plt.colorbar()
#plt.savefig('fig.png', dpi=300)
#plt.show()
