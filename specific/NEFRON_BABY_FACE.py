"""
Duplicate Nefron Baby Eye
"""

import maya.cmds as cmds


eyeFaces = ["baby_GEO.f[0:79]", "baby_GEO.f[134:149]", "baby_GEO.f[154:155]", "baby_GEO.f[164:183]", "baby_GEO.f[716:773]", "baby_GEO.f[856:935]", "baby_GEO.f[990:1005]", "baby_GEO.f[1010:1011]", "baby_GEO.f[1020:1039]", "baby_GEO.f[1572:1629]"]
cmds.select(eyeFaces)

cmds.polyChipOff( eyeFaces, ch=True, kft=True, dup=True, off=False )
cmds.move(0, 0, 0.00321056, relative=True )

cmds.setAttr( "baby_GEOShape.uvPivot", 0.100078, 0.95086, type="double2" )
cmds.polyEditUV(u=-0.39993, v=0.327127)
cmds.polyEditUV(pu=0.100078, pv=0.95086, su=0.472196, sv=0.472196)


# setup
filePath = "../../sourceimages/characters/bb_face_basecolor.psd"
materialName = "M_Baby_Eye"
attribName = "Eye"
jointName = "baby_Eyes_JNT"
columns = 5
lines = 10
objName = "baby_GEO"

# get current selection - selection is face
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
cmds.connectAttr(file+".outTransparency", material+".transparency", force=True);

# connect file to material
cmds.connectAttr(file+".outColor", material+".color", force=True)

# connect object to material
maya.mel.eval('assignCreatedShader "lambert" "" '+material+' "'+obj+'"')

# create attribute
cmds.addAttr(objName, longName=attribName, attributeType='long', min=0, defaultValue=0 )
cmds.setAttr(objName+'.'+attribName, keyable=True, lock=False)

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
cmds.expression( s=calcOffset+".input2X = floor("+objName+"."+attribName+"%"+str(columns)+")", o=objName, name="calculateColumn")
cmds.expression( s=calcOffset+".input2Y = floor("+objName+"."+attribName+"/"+str(columns)+")", o=objName, name="calculateLine")

# apply utilities result in place2D
cmds.connectAttr(calcOffset+".outputX", place2d+".offsetU", force=True)
cmds.connectAttr(calcOffset+".outputY", place2d+".offsetV", force=True)

# apply attrib value in skelleton 
cmds.connectAttr(objName+'.'+attribName, jointName+".scaleX")




























"""
Duplicate Nefron Baby Mouth
"""

import maya.cmds as cmds

mouthFaces = ["baby_GEO.f[80:133]", "baby_GEO.f[150:153]", "baby_GEO.f[186:191]", "baby_GEO.f[216:217]", "baby_GEO.f[232]", "baby_GEO.f[680:699]", "baby_GEO.f[855]", "baby_GEO.f[936:989]", "baby_GEO.f[1006:1009]", "baby_GEO.f[1042:1047]", "baby_GEO.f[1072:1073]", "baby_GEO.f[1089]", "baby_GEO.f[1536:1555]", "baby_GEO.f[1711]"]
cmds.select(mouthFaces)

cmds.polyChipOff( mouthFaces, ch=True, kft=True, dup=True, off=False )
cmds.move(0, 0, 0.00321056, relative=True )

cmds.setAttr( "baby_GEOShape.uvPivot", 0.100191, 0.350225, type="double2" )
cmds.polyEditUV(u=-0.39981, v=-0.149165)
cmds.polyEditUV(pu=0.100191, pv=0.350225, su=0.61797, sv=0.61797)



# setup
filePath = "../../sourceimages/characters/bb_face_basecolor.psd"
materialName = "M_Baby_Mouth"
attribName = "Mouth"
jointName = "baby_Mouth_JNT"
columns = 5
lines = 10
objName = "baby_GEO"

# get current selection - selection is face
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
cmds.connectAttr(file+".outTransparency", material+".transparency", force=True);

# connect file to material
cmds.connectAttr(file+".outColor", material+".color", force=True)

# connect object to material
maya.mel.eval('assignCreatedShader "lambert" "" '+material+' "'+obj+'"')

# create attribute
cmds.addAttr(objName, longName=attribName, attributeType='long', min=0, defaultValue=0 )
cmds.setAttr(objName+'.'+attribName, keyable=True, lock=False)

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
cmds.expression( s=calcOffset+".input2X = floor("+objName+"."+attribName+"%"+str(columns)+")", o=objName, name="calculateColumn")
cmds.expression( s=calcOffset+".input2Y = floor("+objName+"."+attribName+"/"+str(columns)+")", o=objName, name="calculateLine")

# apply utilities result in place2D
cmds.connectAttr(calcOffset+".outputX", place2d+".offsetU", force=True)
cmds.connectAttr(calcOffset+".outputY", place2d+".offsetV", force=True)

# apply attrib value in skelleton 
cmds.connectAttr(objName+'.'+attribName, jointName+".scaleX")
