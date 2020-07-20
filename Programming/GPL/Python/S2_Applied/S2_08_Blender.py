
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