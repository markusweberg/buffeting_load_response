# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by marku on Sat Apr 20 09:50:48 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.17187, 1.18056), width=172.5, 
    height=117.111)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('abaqus_export.py', __main__.__dict__)
#: Model: C:/Users/marku/Min disk/Skole/Master/Masteroppgave/Buffeting load response/./Abaqus/Updated model/grenland_bridge51.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       31
#: Number of Node Sets:          37
#: Number of Steps:              2
print 'RT script done'
#: RT script done
