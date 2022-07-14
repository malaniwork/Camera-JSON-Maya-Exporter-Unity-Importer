
***Maya to Unity - Camera JSON Maya Exporter & Unity Importer***
by Maysam Al-Ani

Github: 
Tool overview: https://www.malani.work/camera-exporter
Tool demo (video): https://vimeo.com/723169999

***DESCRIPTION

This tool allows users to export animated camera data from Maya to Unity through a JSON file. 
The data can be imported into Unity through a simple C# script attached to the camera. 
This allows for quick camera movement implementations built more conveniently in Maya without having to animate within Unity.

***HOW TO SETUP AND USE

1. Place the folder jsoncamera in this Maya file directory: ~\Documents\maya\2022\scripts

2. In Maya, make a new shelf item and name it. In the video, I named it "Camera JSON export". 
Add this code block from the file MayaPythonBlock.py or simply copy and paste the below under Command in the Shelf Editor window:

###### Please use this script in Maya. This script will run the exportCamera def from the MayaCamera script

import maya.cmds as cmds
import jsoncamera.MayaCamera as mc
from importlib import reload


reload(mc)
mc.exportCamera(camera=cmds.ls(type='camera',sl=True))

3. Set up your cameras as needed. 

4. Once you have your cameras set up and animated the way you're happy with, select the camera, click on the Camera JSON export button on the shelf from step #2,
this will open up a save window for the JSON file.

5. Name and save the JSON file.

6. To prepare the JSON file to be used in Unity, convert your JSON object to a C# class using this website: https://json2csharp.com 
In other words, copy and paste your JSON file date into the translator. The public lists are what you'll use for the Unity C# script.

7. In Unity, import and attach the C# script ImporterGithub.cs to your camera.

8. Import your JSON file and attach it to the public TextAsset called Json on your camera.

9. Press play and watch the camera's movement.

Done!

*** For any issues, questions, or contributions, please post on the Github page.