# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-07.58.56 126354
# Run by pranjalm on Sun Jul 05 18:21:00 2015
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=180.951675415039, 
    height=99.2057342529297)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('5m_subsoil_concrete_grade_variation.cae')
#: The model database "C:\Users\pranjalm\Desktop\summer\5m_subsoil\5m_subsoil_concrete_grade_variation.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['cbl']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Instance type']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Load']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Boundary condition']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Interaction']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Skin']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Display group']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Element type']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=76.0474, 
    farPlane=131.728, width=56.844, height=20.0628, cameraPosition=(70.2379, 
    35.1355, 95.2149), cameraUpVector=(-0.44236, 0.78489, -0.433895), 
    cameraTarget=(1.69692, 1.78123, 25.2919))
session.viewports['Viewport: 1'].view.fitView()
session.printOptions.setValues(vpBackground=ON, compass=ON)
session.printToFile(
    fileName='C:/Users/pranjalm/Desktop/summer/5m_subsoil/elements', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.printToFile(
    fileName='C:/Users/pranjalm/Desktop/summer/5m_subsoil/elements_bc.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#F9EAFF')
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Part']
cmap.updateOverrides(overrides={'fpl':(True, '#FFB200', 'Default', '#FFB200')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
leaf = dgm.Leaf(leafType=ALL_ELEMENTS)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['subsoil-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(cellSeq=cells1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['subsoil-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(cellSeq=cells1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
openMdb(
    pathName='C:/Users/pranjalm/Desktop/summer/tmp/5m_subsoil_concrete_grade_variation.cae')
#: The model database "C:\Users\pranjalm\Desktop\summer\tmp\5m_subsoil_concrete_grade_variation.cae" has been opened.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.7056, 
    farPlane=131.895, width=56.5885, height=19.9727, cameraPosition=(61.4174, 
    48.6704, 95.5377), cameraUpVector=(-0.57735, 0.679105, -0.453303), 
    cameraTarget=(1.69692, 1.78123, 25.2919))
session.viewports['Viewport: 1'].view.setValues(nearPlane=76.5967, 
    farPlane=131.054, width=57.2547, height=20.2078, cameraPosition=(64.3306, 
    44.7025, 95.5377), cameraUpVector=(-0.532294, 0.714968, -0.453303), 
    cameraTarget=(1.70706, 1.76741, 25.2919))
session.viewports['Viewport: 1'].view.fitView()
session.printToFile(
    fileName='C:/Users/pranjalm/Desktop/summer/5m_subsoil/elements.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('subsoil-1', ), vector=(0.0, -2.5, 0.0))
#: The instance subsoil-1 was translated by 0., -2.5, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('fpl-1', ), vector=(0.0, -0.5, 0.0))
#: The instance fpl-1 was translated by 0., -500.E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('fpl-1', ), vector=(0.0, -0.5, 0.0))
#: The instance fpl-1 was translated by 0., -500.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.1999, 
    farPlane=122.742, width=4.72043, height=1.66605, viewOffsetX=-12.4171, 
    viewOffsetY=-2.74022)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('hbl-1', ), vector=(0.0, -0.3, 0.0))
#: The instance hbl-1 was translated by 0., -300.E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('hbl-1', ), vector=(0.0, -0.3, 0.0))
#: The instance hbl-1 was translated by 0., -300.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=74.5962, 
    farPlane=135.526, width=59.5997, height=21.0354, cameraPosition=(61.9618, 
    33.5762, 103.85), cameraUpVector=(-0.57735, 0.752617, -0.316597), 
    cameraTarget=(1.69823, 0.529851, 25.2919))
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.6194, 
    farPlane=137.227, width=60.4172, height=21.324, cameraPosition=(-48.4846, 
    33.5762, 111.107), cameraUpVector=(0.0711759, 0.752617, -0.6546), 
    cameraTarget=(0.982054, 0.529851, 25.339))
session.viewports['Viewport: 1'].view.setValues(nearPlane=73.6486, 
    farPlane=138.777, width=58.8427, height=20.7683, cameraPosition=(2.33106, 
    33.5762, 124.608), cameraUpVector=(-0.267659, 0.752617, -0.601603), 
    cameraTarget=(1.95769, 0.529851, 25.5982))
session.viewports['Viewport: 1'].view.setValues(nearPlane=73.6785, 
    farPlane=138.699, width=58.8667, height=20.7767, cameraPosition=(11.2722, 
    32.2607, 124.608), cameraUpVector=(-0.0575696, 0.796718, -0.601603), 
    cameraTarget=(2.11198, 0.507151, 25.5982))
session.viewports['Viewport: 1'].view.setValues(nearPlane=74.202, 
    farPlane=139.158, width=59.285, height=20.9244, cameraPosition=(11.2722, 
    5.20828, 129.531), cameraUpVector=(-0.0575696, 0.924857, -0.375932), 
    cameraTarget=(2.11198, 0.0462508, 25.6821))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('fpl-1', ), vector=(0.0, -0.5, 0.0))
#: The instance fpl-1 was translated by 0., -500.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.4346, 
    farPlane=124.283, width=24.3086, height=8.57961, cameraPosition=(10.1467, 
    6.00009, 119.724), cameraUpVector=(-0.0575696, 0.922824, -0.380896), 
    cameraTarget=(1.64602, 0.692, 23.3789))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.4319, 
    farPlane=124.37, width=24.2843, height=8.57105, cameraPosition=(8.44662, 
    8.03987, 119.775), cameraUpVector=(-0.299415, 0.874797, -0.380896))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.3377, 
    farPlane=124.849, width=26.7833, height=9.45306, cameraPosition=(22.4558, 
    7.74153, 118.096), cameraUpVector=(-0.351056, 0.874797, -0.333903))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.4531, 
    farPlane=123.215, width=27.2758, height=9.62686, cameraPosition=(49.6272, 
    8.51869, 108.161), cameraUpVector=(-0.435459, 0.874797, -0.212383), 
    cameraTarget=(1.07933, 1.08333, 23.6133))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=74.8837, 
    farPlane=128.224, width=29.4173, height=10.3827, cameraPosition=(47.6158, 
    21.0331, 112.206), cameraUpVector=(-0.621858, 0.753782, -0.212383), 
    cameraTarget=(0.291817, 2.13715, 24.4857))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=74.5555, 
    farPlane=128.363, width=29.9398, height=10.5671, cameraPosition=(44.9536, 
    -22.6598, 112.141), cameraUpVector=(0.182843, 0.959929, -0.212383))
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.0327, 
    farPlane=127.625, width=30.1314, height=10.6347, cameraPosition=(50.1642, 
    -8.26844, 112.141), cameraUpVector=(-0.110426, 0.970928, -0.212383), 
    cameraTarget=(0.233518, 1.67905, 24.4983))
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.1597, 
    farPlane=127.461, width=30.1824, height=10.6527, cameraPosition=(50.8323, 
    -3.95824, 112.141), cameraUpVector=(-0.193148, 0.957909, -0.212383), 
    cameraTarget=(0.233332, 1.67785, 24.4983))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cbl-1', ), vector=(0.0, 0.24, 0.0))
#: The instance cbl-1 was translated by 0., 240.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.776, 
    farPlane=127.711, width=28.1706, height=9.94269, cameraPosition=(51.2586, 
    8.10468, 112.367), cameraUpVector=(-0.193148, 0.923994, -0.330047), 
    cameraTarget=(0.514141, 2.7647, 24.4528))
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.916, 
    farPlane=127.549, width=28.2227, height=9.96106, cameraPosition=(51.3572, 
    7.06565, 112.367), cameraUpVector=(-0.174226, 0.927748, -0.330047), 
    cameraTarget=(0.514233, 2.76373, 24.4528))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.864, 
    farPlane=127.035, width=24.7052, height=8.71959, cameraPosition=(50.6171, 
    10.4853, 112.181), cameraUpVector=(-0.269201, 0.904766, -0.330047), 
    cameraTarget=(0.572727, 0.965868, 24.4098))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=74.607, 
    farPlane=129.7, width=25.2839, height=8.92385, cameraPosition=(21.8052, 
    10.2471, 123.241), cameraUpVector=(-0.156466, 0.904766, -0.396129), 
    cameraTarget=(0.71914, 0.724088, 24.3918))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.5419, 
    farPlane=126.328, width=27.3628, height=9.65758, viewOffsetX=4.87172, 
    viewOffsetY=-0.322816)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.4268, 
    farPlane=126.443, width=29.1952, height=10.3043, viewOffsetX=4.86377, 
    viewOffsetY=-0.322289)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.2727, 
    farPlane=126.597, width=30.269, height=10.6833, viewOffsetX=4.85313, 
    viewOffsetY=-0.321584)
session.printToFile(
    fileName='C:/Users/pranjalm/Desktop/summer/5m_subsoil/elements_dismembered', 
    format=SVG, canvasObjects=(session.viewports['Viewport: 1'], ))
session.printToFile(
    fileName='C:/Users/pranjalm/Desktop/summer/5m_subsoil/elements_dismembered', 
    format=PS, canvasObjects=(session.viewports['Viewport: 1'], ))
session.printToFile(
    fileName='C:/Users/pranjalm/Desktop/summer/5m_subsoil/elements_dismembered', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
session.printToFile(
    fileName='C:/Users/pranjalm/Desktop/summer/5m_subsoil/elements_dismembered', 
    format=TIFF, canvasObjects=(session.viewports['Viewport: 1'], ))
