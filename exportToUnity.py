"""
Criar um botao para setar objeto como colisor
esconder colisores
mostrar colisores
mostrar boundbox dos colisores

_GO - objecto exportado separado
_COL - colider do objeto pai
_PHY - o objeto pai e um objeto fisico
_D1D - o objeto e arrastado em uma direcao
_DROTY - rotacionado no eixo Y
_DROTX - rotacionado no eixi X

Deve registrar posicao, rotacao, escala e hierarquia

{
    name: ""
    position: {x,y,z},
    rotation: {x,y,z},
    mayahierarchy: ""
    children: []
}
"""

import maya.cmds as cmds
import json
import os

"""
def findPath():
    path = maya.cmds.file(q=True, sn=True, un=True)
    for i in range(3):
        path = os.path.dirname(path)
    path += "/Assets/Models/"
    if( not os.path.exists(path) ):
        os.makedirs(path)
    return path
"""
def findPath():
    path = maya.cmds.file(q=True, sn=True, un=True)
    for i in range(4):
        path = os.path.dirname(path)
    path += "/UnityProjects/nefron/Assets/Maya/"
    if( not os.path.exists(path) ):
        os.makedirs(path)
    return path
    
    
globalPath = findPath()
exported = []
    
def exportSelection(path):
    maya.mel.eval('FBXExportSmoothingGroups -v true')
    maya.mel.eval('FBXExportTangents -v true')
    maya.mel.eval('FBXExportTriangulate -v true')
    maya.mel.eval('FBXExportConvertUnitString cm')
    maya.mel.eval('FBXExportReferencedAssetsContent -v true')
    maya.mel.eval('FBXExportSmoothMesh -v true')
    maya.mel.eval('FBXExportAnimationOnly -v false')
    maya.mel.eval('FBXExportCameras -v false')
    maya.mel.eval('FBXExportInputConnections -v false')
    maya.mel.eval('FBXExport -f "%s" -s' % path)

def createData( ob ):
    pos = maya.cmds.xform(ob, q=1, ws=1, rp=1)
    rot = maya.cmds.xform(ob, q=1, ws=1, ro=1)
    lastDivision = ob.rfind('|')
    data = {}
    data['name'] = ob[lastDivision+1:]
    data['position'] = { "x": -pos[0], "y": pos[1], "z": pos[2] }
    data['rotation'] = { "x": rot[0], "y": rot[1], "z": rot[2] }
    data['mayahierarchy'] = ob[:lastDivision+1]
    return data
    
 
def getData( ob ):
    children = maya.cmds.listRelatives(ob, type="transform")
    dataChildren = []
    
    if children:
        for child in children:
            result = getData((ob+"|" if len(ob) > 0 else '')+child)
            if result:
                dataChildren.append(result)
    
    if "_GO" in ob or len(dataChildren) > 0:
        data = createData(ob)
        data['children'] = dataChildren
        return data
    else:
        return None
    
def exportByData(data):
    name = data["name"]
    for child in data["children"]:
        exportByData(child)
    
    index = name.index('_GO') if '_GO' in name else -1
    
    if index != -1:
        if len(data['mayahierarchy']) > 0:
            maya.cmds.parent(data['mayahierarchy']+name, world=True)
        maya.cmds.move(0,0,0,name)
        maya.cmds.rotate(0,0,0,name)
        maya.cmds.select(name)
        exportName = name[:index]
        if not exportName in exported:
            exported.append(exportName)
            maya.cmds.rename(exportName)
            exportSelection(globalPath+exportName+".fbx")
            maya.cmds.rename(name)

    
def writeJSON( jobj ):
    sceneName = cmds.file(q=True, sn=True, shn=True).split('.')[0]
    stringValue = json.dumps(jobj);
    file = open(globalPath+sceneName+".json", 'w')
    file.truncate()
    file.write(stringValue)
    file.close()

def organizeByData(data):
    name = data['name']
    hi = data['mayahierarchy']
    

    if "_GO" in name:   
        if len(hi) > 0:
            maya.cmds.parent( name, hi )
            
        pos = maya.cmds.xform(hi+name, q=1, ws=1, rp=1)
        rot = maya.cmds.xform(hi+name, q=1, r=1, ro=1)
        maya.cmds.xform(hi+name, ws=1, translation=(-data['position']['x']-pos[0], data['position']['y']-pos[1], data['position']['z']-pos[2]))            
        maya.cmds.rotate(data['rotation']['x'],data['rotation']['y'],data['rotation']['z'],hi+name)
        
    for child in data['children']:
        organizeByData(child)

children = maya.cmds.ls(selection=True)
dataList = []
if children:
    for child in children:
        parentPath = maya.cmds.listRelatives(child, allParents=True, fullPath=True)
        childParent = '|'.join(parentPath) if parentPath else ''
        completeName = (childParent+"|" if len(childParent) > 0 else '')+child
        data = getData(completeName)
        exportByData(data)
        organizeByData(data)
        dataList.append(data)

writeJSON({'children': dataList})

print "Complete"
