# Extending B_q and phi for matrix multiplication
B_q_extended = np.zeros((len(x) * 3, len(x) * 2))

for i in range(len(x)):
    B_q_extended[i*3:(i*3)+3, i*2:(i*2)+2] = B_q

phi_extended = np.zeros((3 * len(x), len(x), n_modes))

for i in range(n_modes):
    for j in range(len(x)):

        phi_extended[j*3:(j*3)+3, j, i] = phi[:, i, j]

# Establishing the meshgrid
dxdx = np.abs(np.array([x]) - np.array([x]).T)

for h in range(len(w)):
    
    # One-point spectra for the wind load
    S_v[0::2, 0::2] = Su[h] * np.exp(-C_u * f[h] * dxdx / V)
    S_v[1::2, 1::2] = Sw[h] * np.exp(-C_w * f[h] * dxdx / V)
    
    S_qq = (rho * V * B / 2)**2 * B_q_extended @ S_v @ B_q_extended.T 
    
    for i in range(n_modes):
        for j in range(n_modes):
            
            integrand = phi_extended[:,:,i].T @ S_qq @ phi_extended[:,:,j]
            
            S_Q[i, j, h] = np.trapz(np.trapz(integrand, x), x)