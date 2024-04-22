# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by marku on Mon Apr 22 14:52:34 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=347.578094482422, 
    height=221.472213745117)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='grenland_bridge.odb')
#: Model: C:/Users/marku/Min disk/Skole/Master/Masteroppgave/Buffeting load response/Abaqus/Initial model/grenland_bridge.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       31
#: Number of Node Sets:          37
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1145.71, 
    farPlane=1715.89, width=548.851, height=288.203, cameraPosition=(1098.97, 
    266.591, 1233.19), cameraUpVector=(-0.477297, 0.828159, -0.293837), 
    cameraTarget=(318.827, -20.1811, 74.834))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1158.4, 
    farPlane=1734.15, width=554.93, height=291.395, cameraPosition=(1149.66, 
    -628.292, 1062.52), cameraUpVector=(-0.281096, 0.90786, 0.311088), 
    cameraTarget=(319.007, -23.3636, 74.2271))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1193.63, 
    farPlane=1729.43, width=571.806, height=300.257, cameraPosition=(1211.83, 
    -1087.47, 409.362), cameraUpVector=(-0.200453, 0.545364, 0.813878), 
    cameraTarget=(319.891, -29.8929, 64.9394))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1186.64, 
    farPlane=1738.12, width=568.46, height=298.5, cameraPosition=(1253.6, 
    -1063.93, 367.746), cameraUpVector=(-0.206603, 0.517022, 0.830665), 
    cameraTarget=(320.915, -29.3161, 63.9195))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1157.15, 
    farPlane=1757.35, width=554.333, height=291.081, cameraPosition=(1299.65, 
    -886.975, 648.697), cameraUpVector=(-0.39504, 0.580471, 0.712038), 
    cameraTarget=(322.07, -24.879, 70.9643))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#: Warning: The selected Primary Variable is not available in the current frame for any elements in the current display group.
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1173.29, 
    farPlane=1775.64, width=562.064, height=295.141, cameraPosition=(1197.72, 
    -934.056, 734.254), cameraUpVector=(-0.420772, 0.60678, 0.674366), 
    cameraTarget=(318.647, -26.4598, 73.837))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1157.98, 
    farPlane=1750.82, width=554.732, height=291.291, cameraPosition=(1121.31, 
    -340.944, 1217.97), cameraUpVector=(-0.396592, 0.908616, 0.130887), 
    cameraTarget=(316.121, -6.84915, 89.8306))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1152.47, 
    farPlane=1762.73, width=552.094, height=289.906, cameraPosition=(1169.9, 
    -446.222, 1143.89), cameraUpVector=(-0.45015, 0.852244, 0.266544), 
    cameraTarget=(317.079, -8.92587, 88.3692))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1164.2, 
    farPlane=1768.16, width=557.716, height=292.858, cameraPosition=(1167.11, 
    -764.014, 950.33), cameraUpVector=(-0.350112, 0.800536, 0.486379), 
    cameraTarget=(317.018, -15.8787, 84.1344))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1177.77, 
    farPlane=1769.58, width=564.218, height=296.272, cameraPosition=(1177.18, 
    -977.538, 693.295), cameraUpVector=(-0.291489, 0.673179, 0.679606), 
    cameraTarget=(317.296, -21.7722, 77.04))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1132.99, 
    farPlane=1808.29, width=542.766, height=285.008, cameraPosition=(1408.74, 
    -735.305, 656.685), cameraUpVector=(-0.408967, 0.598754, 0.688651), 
    cameraTarget=(324.833, -13.888, 75.8484))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1139.41, 
    farPlane=1801.87, width=453.369, height=238.065, viewOffsetX=41.874, 
    viewOffsetY=-5.20859)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='NFORC6', outputPosition=ELEMENT_NODAL, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1136.95, 
    farPlane=1804.34, width=544.663, height=286.004, viewOffsetX=43.6876, 
    viewOffsetY=-8.11323)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1136.95, 
    farPlane=1801.4, width=544.664, height=286.004, cameraPosition=(1382.27, 
    -756.822, 674.449), cameraUpVector=(-0.407564, 0.607675, 0.681633), 
    cameraTarget=(322.931, -13.7733, 75.8278), viewOffsetX=43.6877, 
    viewOffsetY=-8.11325)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1168.29, 
    farPlane=1770.05, width=148.401, height=77.9256, viewOffsetX=-36.6464, 
    viewOffsetY=17.7488)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1135.45, 
    farPlane=1783.19, width=144.23, height=75.7354, cameraPosition=(1514.31, 
    -535.614, 643.876), cameraUpVector=(-0.46391, 0.576691, 0.672469), 
    cameraTarget=(321.321, -4.27793, 71.9302), viewOffsetX=-35.6164, 
    viewOffsetY=17.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1133.39, 
    farPlane=1785.25, width=185.91, height=97.6215, viewOffsetX=4.69749, 
    viewOffsetY=6.62099)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=100 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1123.64, 
    farPlane=1778.89, width=322.978, height=169.596, viewOffsetX=1.87108, 
    viewOffsetY=0.0072279)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='NFORC5', outputPosition=ELEMENT_NODAL, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1137.76, 
    farPlane=1764.78, width=129.803, height=68.1599, viewOffsetX=3.4914, 
    viewOffsetY=-44.3565)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1096.97, 
    farPlane=1792.36, width=405.508, height=212.933, viewOffsetX=42.1921, 
    viewOffsetY=-61.2192)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='NFORC6', outputPosition=ELEMENT_NODAL, )
