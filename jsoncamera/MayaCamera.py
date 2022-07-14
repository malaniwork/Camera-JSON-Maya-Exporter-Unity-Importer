###### This script will export selected [1] camera's data as a JSON file

import os, json
import maya.cmds as cmds

def exportCamera(camera=None, fileName=None):

	'''Export Maya Camera to JSON'''

	print ("Camera Exporter Activated")
	# first check if user has a camera in the scene
	if not camera:
		# get the current selection
		selection = cmds.ls(selection=True)

		# if nothing is selected, stop
		if len(selection) == 0:
			print ("You must select a camera to export")
			return -1

		# if the user has selected more than one, stop
		if len(selection) > 1:
			print ("You must select only one camera")
			return -1

		# if there is only one thing selected, lets store it
		camera = selection[0]

		#make sure the selected object is indeed a camera
		if cmds.nodeType(camera) == "transform":
			cameraShape = cmds.listRelatives(camera,children=True)[0]
			#if children are not a camera, then we stop
			if cmds.nodeType(cameraShape) != "camera":
				print ("The selected object is not a camera")
				return -1

	# check if a filename is provided
	if not fileName:
		# then bring up a file dialogue
		basicFilter = "*.json"
		retval = cmds.fileDialog2(dialogStyle=2,fm=0)
		# if a file was selected
		if retval:
			file, ext = os.path.splitext(retval[0])
			# if the extension is not *.json, lets add it
			if ext != ".json":
				fileName = file+".json"
			else:
				fileName = retval[0]
	print(fileName)

	# gather data about the camera
	frameStart = cmds.playbackOptions(q=True, min=True)
	frameEnd = cmds.playbackOptions(q=True, max=True)

	outData = {

				"cameraName":camera,
				"frameStart":frameStart,
				"frameEnd":frameEnd,
				"vfov":cmds.camera(camera,q=True,verticalFieldOfView=True),
				"hfov":cmds.camera(camera,q=True,horizontalFieldOfView=True),
				"frames":{"matrix_world":{}}
			  }


	# loop over all the frames in the timeline + store that data
	for i in range(int(frameStart),int(frameEnd + 1)):
		#set the current frame
		cmds.currentTime(i)
		#get the camera matrix is ws
		outData["frames"]["matrix_world"]["frame_"+str(i)]= cmds.xform(camera,q=True,translation=True,worldSpace=True)
		outData["frames"]["matrix_world"]["frame_"+str(i)] +=  cmds.xform(camera,q=True,rotation=True,worldSpace=True)

	cmds.currentTime(frameStart)
	# save data to json
	fout = open(fileName,'w')
	json.dump(outData,fout,indent=2)
	fout.close()

	print("Exported successfully to %s" % fileName)

