# Buffeting wind load matrices
B_q = np.array([
    [2 * (D / B)* CD_bar, ((D / B) * CD_prime - CL_bar)],
    [2 * CL_bar, (CL_prime + (D / B) * CD_bar)],
    [2 * B * CM_bar, B * CM_prime]
])

# Number of modes
n_modes = phi.shape[1]

# Bridge length vector
x = np.arange(0, 609, 8)

# Frequency vectors
w = np.logspace(-3, 1.2, 100)
f = w / (2 * np.pi)

# Wind turbulence 
Su = (Iu*V)**2*Au*xLu/V / ((1+1.5*Au*f*xLu/V)**(5/3)) / (2 * np.pi)
Sw = (Iw*V)**2*Aw*xLw/V / ((1+1.5*Aw*f*xLw/V)**(5/3)) / (2 * np.pi)