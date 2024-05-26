node_set = odb.rootAssembly.nodeSets[node_set]
number_of_modes = len(odb.steps['Modal'].frames) - 1
n_sensor_nodes = len(node_set)

phi_matrix = np.zeros((3, number_of_modes, n_sensor_nodes - 1), dtype=float)

# Looping through all modes
for i in range(number_of_modes):
    idx = 0
    frame = odb.steps['Modal'].frames[i+1]

    displacement_y = frame.fieldOutputs['NFORC6'].getSubset(region=node_set)
    displacement_z = frame.fieldOutputs['NFORC5'].getSubset(region=node_set)
    rotation_x = frame.fieldOutputs['NFORC4'].getSubset(region=node_set)

    # Looping through all nodes in the node set
    for j in range(0, n_sensor_nodes * 2, 2):

        # Field output data
        phi_matrix[0,i,idx] = round(node_displacement_y_1.values[j].data, 10)
        phi_matrix[1,i,idx] = round(node_displacement_z_1.values[j].data, 10)
        phi_matrix[2,i,idx] = round(node_rotation_x_1.values[j].data, 10)

        idx += 1