# Model for testing
model = "Updated"

# Importing the mode shapes and natural frequencies from Abaqus and calculating the modal system matrices
file_path = "./Data/" + model + " model/Deformation/grenland_bridge"
file_path_moment = "./Data/" + model + " model/Moment/grenland_bridge_modes.npy"

# Bridge length vector
x = np.arange(0, 609, 8)

# Mode shape matrix: 3 x n_modes x len(x)
phi = np.load(file_path + "_modes.npy")
phi = phi[:,:,::8]
phi = phi[:,:20,:]
# phi[0,:,:] = 0
# phi[2,:,:] = 0

# Frequency vector: n_modes x 1
f_n = np.load(file_path + "_frequencies.npy")
w_n = f_n * 2 * np.pi

# Number of modes
n_modes = phi.shape[1]

# Damping 
xi = np.load("damping_ratio.npy")
xi_vector = {"Initial": np.array([1, 3, 5, 7, 13, 11, 14, 17, 20, 24, 27, 34, 43, 37, 59]) - 1,
             "Updated": np.array([1, 2, 5, 6, 9, 11, 14, 17, 21, 24, 26, 34, 41, 35, 53]) - 1}                  
xi_interp_length = np.arange(n_modes)
xi_interp = np.interp(xi_interp_length, xi_vector[model], xi)

# Generalized mass matrix
M_gen = np.load(file_path + "_mass.npy") 
M_gen = M_gen[:20]

# Establishing the system matrices
M_modal = np.diag(M_gen)
K_modal = np.zeros((n_modes, n_modes))
C_modal = np.zeros((n_modes, n_modes))

# Calculating the system matrices
for i in range(n_modes):

    K_modal[i, i] = w_n[i]**2 * M_modal[i, i]

    C_modal[i, i] = 2 * M_modal[i, i] * w_n[i] * xi_interp[i]