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