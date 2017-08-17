"""
//-----Preparar animacao para exportacao. 

Obs.: nao esqueca de remover o "Resample Curves no unity".
"""

import maya.cmds as cmds

# setup
joinRoot = "root_jnt"
constantCurves = ["bim_mouth_JNT_scaleX", "bim_eye_JNT_scaleX"]


# bake transform attribs in joints
startTime = cmds.playbackOptions( q=True, minTime=True )
endTime = cmds.playbackOptions( q=True, maxTime=True )
cmds.select(joinRoot, r=True)
cmds.bakeResults(
	t=(startTime,endTime), 
	simulation=True, 
	disableImplicitControl=True,
	preserveOutsideKeys=True,
	sparseAnimCurveBake=True,
	removeBakedAttributeFromLayer=True,
	removeBakedAnimFromLayer=False,
	bakeOnOverrideLayer=False,
	minimizeRotation=True,
	controlPoints=False,
	shape=True
)

# delete constraints
cmds.delete( cmds.ls(type="constraint") )

# apply constant curves in constantCurves array
cmds.selectKey(clear=True)
cmds.selectKey(constantCurves, add=True, keyframe=True)
cmds.keyTangent(outTangentType="step")

# remove invalids nodes
cmds.select( cmds.ls(typ="unknown")
cmds.delete();

# select joints to export
cmds.select(joinRoot, r=True, hi=True)


