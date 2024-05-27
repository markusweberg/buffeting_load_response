# Calculating the cross-spectral density of the wind load 

# Buffeting wind load matrices
B_q = np.array([
    [2 * (D / B)* CD_bar, ((D / B) * CD_prime - CL_bar)],
    [2 * CL_bar, (CL_prime + (D / B) * CD_bar)],
    [2 * B * CM_bar, B * CM_prime]
])

C_ae = - rho * V * B / 2 * np.array([
    [2 * (D / B)* CD_bar, ((D / B) * CD_prime - CL_bar), 0],
    [2 * CL_bar, (CL_prime + (D / B) * CD_bar), 0],
    [2 * B * CM_bar, B * CM_prime, 0]
])

K_ae = rho * V**2 * B / 2 * np.array([
    [0, 0, (D / B) * CD_prime],
    [0, 0, CL_prime],
    [0, 0, B * CM_prime]
])

# Frequency vector
w = np.logspace(-3, 1.5, 100)
f = w / (2 * np.pi)

# Wind turbulence 
Su = (Iu*V)**2*Au*xLu/V / ((1+1.5*Au*f*xLu/V)**(5/3)) / (2 * np.pi)
Sw = (Iw*V)**2*Aw*xLw/V / ((1+1.5*Aw*f*xLw/V)**(5/3)) / (2 * np.pi)

# Extending B_q and phi for matrix multiplication
B_q_extended = np.zeros((len(x) * 3, len(x) * 2))

for i in range(len(x)):
    B_q_extended[i*3:(i*3)+3, i*2:(i*2)+2] = B_q

phi_extended = np.zeros((3 * len(x), len(x), n_modes))

for i in range(n_modes):
    for j in range(len(x)):

        phi_extended[j*3:(j*3)+3, j, i] = phi[:, i, j]