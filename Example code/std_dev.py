std_dev_y = np.zeros((len(x)), dtype=complex)
std_dev_z = np.zeros((len(x)), dtype=complex)
std_dev_t = np.zeros((len(x)), dtype=complex)

for i in range(len(x)):
    std_dev_y[i] = np.trapz(S_rr[3*i, 3*i, :], w_interp)**0.5
    std_dev_z[i] = np.trapz(S_rr[3*i+1, 3*i+1, :], w_interp)**0.5
    std_dev_t[i] = np.trapz(S_rr[3*i+2, 3*i+2, :], w_interp)**0.5