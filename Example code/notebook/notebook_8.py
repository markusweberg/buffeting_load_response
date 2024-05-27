# Calculating the frequency response function

C_ae_modal = np.zeros((n_modes, n_modes))
K_ae_modal = np.zeros((n_modes, n_modes))
H_modal = np.zeros((n_modes, n_modes, len(w_interp)), dtype=complex)

C_integrand = np.zeros(len(x))
K_integrand = np.zeros(len(x))

for i in range(n_modes):
    for j in range(n_modes):
        for k in range(len(x)):
            C_integrand[k] = phi[:,i,k].T @ C_ae @ phi[:,j,k]
            K_integrand[k] = phi[:,i,k].T @ K_ae @ phi[:,j,k]

        C_ae_modal[i, j] = np.trapz(C_integrand, x)
        K_ae_modal[i, j] = np.trapz(K_integrand, x)

for i in range(len(w_interp)):
    H_modal[:,:,i] = np.linalg.inv((-w_interp[i]**2 * M_modal + 1j * w_interp[i] * (C_modal - C_ae_modal) + K_modal - K_ae_modal))