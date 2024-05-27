# First draft for calculating the cross-spectral density of the wind load
# Does the same as the code above, but slower

integrand = np.zeros((len(x), len(x)))

S_v = np.zeros((2, 2))
S_Q = np.zeros((n_modes, n_modes, len(w)), dtype=float)

for h in range(len(w)):
    for i in range(n_modes):
        for j in range(n_modes):
            for k in range(len(x)):
                for l in range(len(x)):

                    # One-point spectra for the wind load
                    S_v[0, 0] = Su[h] * np.exp(-C_u * f[h] * np.abs(x[l] - x[k]) / V)
                    S_v[1, 1] = Sw[h] * np.exp(-C_w * f[h] * np.abs(x[l] - x[k]) / V)
      
                    S_qq = (rho * V * B / 2)**2 * B_q @ S_v @ B_q.T 

                    integrand[k, l] = phi[:, i, k].T @ S_qq @ phi[:, j, l] 

            S_Q[i, j, h] = np.trapz(np.trapz(integrand, x), x) 