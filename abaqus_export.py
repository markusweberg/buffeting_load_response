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
from functions_py2 import *

job_name = "./Abaqus/Updated model/grenland_bridge51"

o3 = session.openOdb(name=job_name + '.odb')
odb = session.odbs[job_name + '.odb']

folder = "./Data/Updated model/"
name = "grenland_bridge51"

get_frequencies(odb, True, name, folder)
get_modeshapes(odb, "BRIDGE_DECK_NODES_1", "BRIDGE_DECK_NODES_2", True, name, folder)
get_modal_mass(odb, True, name, folder)

# print >> sys.__stdout__, get_modal_mass(odb, save=True)
