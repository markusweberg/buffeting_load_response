# Establishing the spectral density matrices
S_Q = np.zeros((n_modes, n_modes, len(w)), dtype=float)
S_v = np.zeros((len(x) * 2, len(x) * 2))


# Establishing dxdx meshgrid and the integrand matrix
dxdx = np.abs(np.array([x]) - np.array([x]).T)
integrand = np.zeros((len(x), len(x)))

for h in range(len(w)):
    
    # One-point spectra for the wind load
    S_v[0::2, 0::2] = Su[h] * np.exp(-C_u * f[h] * dxdx / V)
    S_v[1::2, 1::2] = Sw[h] * np.exp(-C_w * f[h] * dxdx / V)
    
    S_qq = (rho * V * B / 2)**2 * B_q_extended @ S_v @ B_q_extended.T 
    
    for i in range(n_modes):
        for j in range(n_modes):
            
            integrand = phi_extended[:,:,i].T @ S_qq @ phi_extended[:,:,j]
            
            S_Q[i, j, h] = np.trapz(np.trapz(integrand, x), x)