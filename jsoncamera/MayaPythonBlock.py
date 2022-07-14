###### Please use this script in Maya. This script will run the exportCamera def from the MayaCamera script

import maya.cmds as cmds
import tdcjson.MayaCamera as mc
from importlib import reload


reload(mc)
mc.exportCamera(camera=cmds.ls(type='camera',sl=True))