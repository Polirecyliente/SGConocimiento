
#   Blender

#T# Blender Python API

#T# import the Blender API called bpy (from inside a Blender script)
import bpy

vidIt = "20200515_145050.mp4"
#T# set a clip to use proxy clip as follows:
bpy.context.scene.sequence_editor.sequences_all[vidIt].use_proxy = True

#T# select a clip in the sequence editor as follows:
bpy.data.scenes['Scene'].sequence_editor.sequences_all[vidIt].select = True

#T# rebuild the proxy of selected clip as follows:
bpy.ops.sequencer.rebuild_proxy()

#T# deselect the clip as follows:
bpy.data.scenes['Scene'].sequence_editor.sequences_all[vidIt].select = False

#T# Blender Game Engine BGE

#T# call as a module, from a Python controller in Blender's logic editor, the module file must be in the same dir as the .blend file, if the module is named Objects.py, and the function is Player() then call the module with "Objects.Player"

#T# import the bge module which includes the logic and events modules
from bge import logic
from bge import events

def Player():
#T# get the controller that called the module
    controller1 = logic.getCurrentController()

#T# get the owner of the controller
    object1 = controller1.owner

#T# get the named actuator connected to the controller
    motion = controller1.actuators['movs']

#T# get the enum with the keyboard keys
    key = logic.keyboard.events

#T# save the value of interesting keys pressed from the keyboard, 0 not pressed, 1 started, 2 hold, 3 released
    kb_left = key[events.LEFTARROWKEY]
    kb_right = key[events.RIGHTARROWKEY]
    
#T# the Update() function is common and executes in each frame
    def Update():
        movespd = 0.2
        deltaX = 0
        deltaY = 0
        
        if kb_left > 0:
            deltaX += -movespd
        if kb_right > 0:
            deltaX += movespd

#T# change the location
        motion.dLoc = [deltaX,deltaY,0.0]

#T# activate the actuator connected to the controller
        controller1.activate(motion)
        
    Update()