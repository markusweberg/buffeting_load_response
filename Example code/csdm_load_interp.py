w_interp = np.linspace(0.001, 15, 1000)
S_Q_interp = np.zeros((n_modes, n_modes, len(w_interp)))

for i in range(n_modes):
    for j in range(n_modes):

        S_Q_interp[i, j, :] = np.interp(w_interp, w, S_Q[i, j, :])