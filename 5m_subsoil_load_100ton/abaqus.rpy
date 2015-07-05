# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-07.58.56 126354
# Run by pranjalm on Sun Jul 05 21:04:59 2015
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
#: The model database "C:\Users\pranjalm\Desktop\summer\5m_subsoil\5m_subsoil_load_100ton\5m_subsoil_concrete_grade_variation.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['cbl']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
