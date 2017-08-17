"""
=>Description
Assign a new material and create a controller for move offset in place2D.

=>Step by Step 
- Create Object
- Organize Texture in columns and lines
- Mapping uv in Object in specific column and line equal zero
- Select Object
- Run Script

=>When Use
Used for animate texture in object. Ex. Eye in texture grid
"""


import maya.cmds as cmds


# setup
filePath = "../sourceimages/characters/nefron_baby_face.png"
materialName = "M_Baby_Eye"
attribName = "Eye"
jointName = "bone"
columns = 5
lines = 10

# get current selection
obj = cmds.ls(selection=True)[0]

# create material
material = cmds.shadingNode("lambert", asShader=True)
shader = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name="lambert2SG")
cmds.connectAttr(material+".outColor", shader+".surfaceShader", force=True)
material = cmds.rename(material, materialName)

# create place2D and file
file = cmds.shadingNode("file", asTexture=True, isColorManaged=True)
place2d = cmds.shadingNode("place2dTexture", asUtility=True)

# connect image to file
cmds.setAttr(file+".fileTextureName", filePath, type="string")

# connections equals between place2D and file
connect = ["coverage", "translateFrame", "rotateFrame", "mirrorU", "mirrorV", "stagger", 
"wrapU", "wrapV", "repeatUV", "noiseUV", "vertexUvOne", "vertexUvTwo", "vertexUvThree",
"vertexCameraOne"]

# connect place2D to file
for elem in connect:
	cmds.connectAttr(place2d+"."+elem, file+"."+elem, force=True)
cmds.connectAttr(place2d+".outUV", file+".uv", force=True)
cmds.connectAttr(place2d+".outUvFilterSize", file+".uvFilterSize", force=True)

# connect file to material
cmds.connectAttr(file+".outColor", material+".color", force=True)

# connect object to material
maya.mel.eval('assignCreatedShader "lambert" "" '+material+' "'+obj+'"')

# create attribute
cmds.addAttr( longName=attribName, attributeType='long', min=0, defaultValue=0 )
cmds.setAttr(obj+'.'+attribName, keyable=True, lock=False)

# create math utilities
calcSize = cmds.shadingNode('multiplyDivide', asUtility=True, n="CalculateSize")
cmds.setAttr( calcSize+'.input1X', 1 )
cmds.setAttr( calcSize+'.input1Y', 1 )
cmds.setAttr( calcSize+'.input2X', columns )
cmds.setAttr( calcSize+'.input2Y', lines )
cmds.setAttr( calcSize+".operation", 2 ) #divide

calcOffset = cmds.shadingNode('multiplyDivide', asUtility=True, n="CalculateOffset")
cmds.connectAttr(calcSize+".outputX", calcOffset+".input1X", force=True)
cmds.connectAttr(calcSize+".outputY", calcOffset+".input1Y", force=True)
cmds.setAttr( calcOffset+".operation", 1 ) #multiply

# expression convert index to column and line
cmds.expression( s=calcOffset+".input2X = floor("+obj+"."+attribName+"%"+str(columns)+")", o=obj, name="calculateColumn")
cmds.expression( s=calcOffset+".input2Y = floor("+obj+"."+attribName+"/"+str(columns)+")", o=obj, name="calculateLine")

# apply utilities result in place2D
cmds.connectAttr(calcOffset+".outputX", place2d+".offsetU", force=True)
cmds.connectAttr(calcOffset+".outputY", place2d+".offsetV", force=True)

# apply attrib value in skelleton 
cmds.connectAttr(obj+'.'+attribName, jointName+".scaleX")
