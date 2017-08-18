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

