import numpy as np
import sys

def get_frequencies(odb, save=False, name='test', folder='test'):


    # Region
    region = odb.steps['Modal'].historyRegions['Assembly BRIDGE_ASSEMBLY']

    # History outputs
    modal_freqs = region.historyOutputs['EIGFREQ'].data

    # Establish modal data
    f_matrix = np.zeros((len(modal_freqs)), dtype=float)

    for i in range(len(modal_freqs)):

        mode_freq = modal_freqs[i][1]

        f_matrix[i] = mode_freq

    # Save to file
    if save:
        np.savetxt(folder + name + '_frequencies' + '.txt', f_matrix,
                   fmt='%.3f', delimiter='\t')
        np.save(folder + name + '_frequencies' + '.npy', f_matrix)

    return(f_matrix)


def get_modeshapes(odb, node_set_name_1, node_set_name_2, save=False, name='test', folder='test'):


    # Number of modes investigated
    number_of_modes = len(odb.steps['Modal'].frames) - 1

    # Node set
    node_set_1 = odb.rootAssembly.nodeSets[node_set_name_1]
    node_set_2 = odb.rootAssembly.nodeSets[node_set_name_2]
    n_sensor_nodes = len(node_set_1.nodes[0]) + len(node_set_2.nodes[0])

    # Mode shape matrix
    phi_matrix = np.zeros((3, number_of_modes, n_sensor_nodes - 1), dtype=float)

    # Looping through all modes
    for i in range(number_of_modes):

        # Mode
        frame = odb.steps['Modal'].frames[i+1]

        # print >> sys.__stdout__, frame.fieldOutputs['SM'].getSubset(region=node_set_1).values[13]

        # Field output
        displacement_y = frame.fieldOutputs['SM']
        displacement_z = frame.fieldOutputs['SM']
        rotation_x = frame.fieldOutputs['SM']


        # Set
        node_displacement_y_1 = displacement_y.getSubset(region=node_set_1)
        node_displacement_z_1 = displacement_z.getSubset(region=node_set_1)
        node_rotation_x_1 = rotation_x.getSubset(region=node_set_1)

        node_displacement_y_2 = displacement_y.getSubset(region=node_set_2)
        node_displacement_z_2 = displacement_z.getSubset(region=node_set_2)
        node_rotation_x_2 = rotation_x.getSubset(region=node_set_2)

        idx = 0

        # Looping through all nodes in the node set
        for j in range(0, n_sensor_nodes * 2, 2):

            if j < len(node_set_1.nodes[0]) * 2:

                # Field output data
                Y = round(node_displacement_y_1.values[j].data[1], 10)
                Z = round(node_displacement_z_1.values[j].data[0], 10)
                T = round(node_rotation_x_1.values[j].data[2], 10)

                phi_matrix[0,i,idx] = Y
                phi_matrix[1,i,idx] = Z
                phi_matrix[2,i,idx] = T

                # print >> sys.__stdout__, idx, node_displacement_y_1.values[j].nodeLabel

            elif j > len(node_set_1.nodes[0]) * 2:

                # Field output data
                Y = round(node_displacement_y_2.values[j - len(node_set_1.nodes[0]) * 2].data[1], 10)
                Z = round(node_displacement_z_2.values[j - len(node_set_1.nodes[0]) * 2].data[0], 10)
                T = round(node_rotation_x_2.values[j - len(node_set_1.nodes[0]) * 2].data[2], 10)

                phi_matrix[0,i,idx-1] = Y
                phi_matrix[1,i,idx-1] = Z
                phi_matrix[2,i,idx-1] = T
               
                # print >> sys.__stdout__, idx-1, node_displacement_y_2.values[j - len(node_set_1.nodes[0]) * 2].nodeLabel

            else:
                pass

            idx += 1

            phi_matrix[0, i, 358] = round(node_displacement_y_1.values[715].data[1], 10)
            phi_matrix[1, i, 358] = round(node_displacement_z_1.values[715].data[0], 10)
            phi_matrix[2, i, 358] = round(node_rotation_x_1.values[715].data[2], 10)

            phi_matrix[0, i, 608] = round(node_displacement_y_2.values[499].data[1], 10)
            phi_matrix[1, i, 608] = round(node_displacement_z_2.values[499].data[0], 10)
            phi_matrix[2, i, 608] = round(node_rotation_x_2.values[499].data[2], 10)

    # Save to file
    if save:
        # np.savetxt(folder + name + '_modes' + '.txt', phi_matrix,
        #            fmt='%.10f', delimiter='\t')
        np.save(folder + name + '_modes' + '.npy', phi_matrix)

    return(phi_matrix)


def get_modal_mass(odb, save=False, name='test', folder='test'):

    region = odb.steps['Modal'].historyRegions['Assembly BRIDGE_ASSEMBLY']

    modal_mass = region.historyOutputs['GM'].data

    m_matrix = np.zeros((len(modal_mass)), dtype=float)

    for i in range(len(modal_mass)):

        m_matrix[i] = modal_mass[i][1]

    if save:
        np.savetxt(folder + name + '_mass' + '.txt', m_matrix,
                   fmt='%.10f', delimiter='\t')
        np.save(folder + name + '_mass' + '.npy', m_matrix)

    return(m_matrix)    