H_modal = np.zeros((n_modes, n_modes, len(w_interp)), dtype=complex)

for i in range(len(w_interp)):
    H_modal[:,:,i] = np.linalg.inv((-w_interp[i]**2 * M_modal + 1j * w_interp[i] * (C_modal - C_ae_modal) + K_modal - K_ae_modal))