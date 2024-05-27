# Calculating the wind load properties
# NS-EN 1991-1-4

# Mean wind velocity
V_b0 = 23
C_alt = max(1 + (30 - 23)* (55.233 - 900) / (23*(1500-900)) , 1)
C_dir = 1 
C_seas = 1
p = 0.5
C_prob = ((1 - 0.2 * np.log(-np.log(1-p))) / (1 - 0.2 * np.log(-np.log(0.98)))) **0.5
C_0 = 1 
z0 = 0.001
z1 = 10
zmin = 2
L1 = 100
z = 55.233
kr = 0.17
C_r = kr * np.log(z / z0)

V = V_b0 * C_dir* C_seas * C_alt * C_prob * C_0 * C_r

# Wind spectra properties
rho = 1.25
Au = 6.8 
Av = 9.4 
Aw = 9.4 
xLu = L1 * (z / z1)**0.3
xLv = 1 / 4 * xLu
xLw = 1 / 12 * xLu
k_i = 1
Iu = kr * V_b0 * k_i / V
Iv = 3 / 4 * Iu
Iw = 1 / 2 * Iu

# Bridge deck properties
D = 2.6
B = 12
CD_prime = 0
CD_bar = 1.0
CL_prime = 2.22
CL_bar = -0.58
CM_prime = 0.786
CM_bar = -0.017
C_u = 9
C_w = 6 