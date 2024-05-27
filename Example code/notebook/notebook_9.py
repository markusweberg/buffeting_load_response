# Calculating the cross-spectral density of the response based on the DEFORMATION
# phi_r = phi

phi_r = np.zeros((3 * len(x), n_modes))

for i in range(n_modes):
    for j in range(len(x)):
        phi_r[j*3:(j*3)+3, i] = phi[:, i, j]

# Cross-spectral density of the response
S_rr = np.zeros((3 * len(x), 3 * len(x), len(w_interp)), dtype=complex)

for i in range(len(w_interp)):
    S_rr[:,:,i] = phi_r @ (np.conj(H_modal[:,:,i]) @ S_Q_interp[:,:,i] @ H_modal[:,:,i].T) @ phi_r.T