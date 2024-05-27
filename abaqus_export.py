from abaqus import *
from abaqusConstants import *

from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

import os
import sys
import shutil
import numpy as np
from deformation_functions import *

model = "Updated"
output = "Deformation"

job_name = "./Abaqus/" + model + " model/grenland_bridge"

o3 = session.openOdb(name=job_name + '.odb')
odb = session.odbs[job_name + '.odb']

folder = "./Data/" + model + " model/" + output + "/"
name = "grenland_bridge"

get_frequencies(odb, True, name, folder)
get_modeshapes(odb, "BRIDGE_DECK_NODES_1", "BRIDGE_DECK_NODES_2", True, name, folder)
get_modal_mass(odb, True, name, folder)

# print >> sys.__stdout__, get_modal_mass(odb, save=True)
