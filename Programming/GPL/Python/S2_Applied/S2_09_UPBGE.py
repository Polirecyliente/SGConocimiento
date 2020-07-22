
#   UPBGE

#T# UPBGE stands for Uchronia Project Blender Game Engine

#T# Contents
#T# bge package
#T# Sensors
#T# Always sensor
#T# Actuator sensor
#T# Ray sensor

#T# bge package

#T# BGE stands for Blender Game Engine

#T# call as a module, from a Python controller in Blender's logic editor, if the module is named Objects.py, and the function is Player() then call the module with "Objects.Player". The module file must be in the same dir as the .blend file, or it can be packed into the .blend file just by saving

#T# import the logic and events modules from the bge package
from bge import logic
from bge import events

#T# the render module has functions that deal with the render engine
from bge import render

def Player():
#T# get the scene from where the module was called
    scene1 = logic.getCurrentScene()

#T# get a particular object in the scene
    scene_obj1 = scene1.objects['Object_name']

#T# get the controller that called the module
    controller1 = logic.getCurrentController()

#T# get the owner of the controller
    object1 = controller1.owner

#T# get a named actuator connected to the controller
    motion = controller1.actuators['motion_actuator_name1']

#T# get a named sensor connected to the controller
    sensor1 = controller1.sensors['sensor_name1']

#T# get the UPBGE window width and height
    win_width1 = render.getWindowWidth()
    win_height1 = render.getWindowHeight()

#T# an enum dictionary with the keyboard keys can be accessed with
    key = logic.keyboard.events

#T# save the value of interesting keys pressed from the keyboard, 0 not pressed, 1 started, 2 hold, 3 released
    kb_left = key[events.LEFTARROWKEY]
    kb_right = key[events.RIGHTARROWKEY]

    x_pos1 = 480
    y_pos1 = 240
#T# set the mouse position
    render.setMousePosition(x_pos1,y_pos1)
    
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

#T# import the SCA classes and others. SCA stands for Sensor Controller Actuator
from bge import types

#T# Sensors

#T# all sensors have two types of attributes, configuration and status attributes. Configuration attributes may be set or get to change a configuration of the sensor, while status attributes can only be get to see a status of the sensor

#T# all the attributes in the always sensor can be used with any other type of sensor as well

#T# Always sensor

#T# create the always sensor, it sends a continuous positive signal
sensor_always1 = types.SCA_AlwaysSensor()

#T# set or get the tap flag, which turns off the sensor signal right after it is turned on
sensor_always1.tap = True

#T# set or get the invert flag, which inverts the sensor signal between positive and negative
sensor_always1.invert = False

#T# set or get the frequency in which the signal is sent. This is the amount of logic ticks in which no signal is sent. In the following, the signal is sent, for 20 ticks nothing is sent, and then the signal is sent again and the cycle repeats as long as the signal is positive
sensor_always1.frequency = 20

#T# get the name of the sensor
name_sensor_always1 = sensor_always1.name

#T# get the owner of the sensor
owner_sensor_always1 = sensor_always1.owner

#T# get the positive flag to know if the sensor is sending a signal or not
positive_flag_sensor_always1 = sensor_always1.positive

#T# the sensor status has values like those of keys pressed, 0 no signal, 1 starting signal, 2 holding signal, 3 stopping signal
status_sensor_always1 = sensor_always1.status

#T# Actuator sensor

#T# create the actuator sensor, it senses when a given actuator is active
sensor_actuator1 = types.SCA_ActuatorSensor

#T# set or get the actuator that the sensor senses upon
sensor_actuator1.actuator = 'actuator_name1'

#T# Collision sensor

#T# create the collision sensor, it senses
sensor_collision1 = types.KX_TouchSensor()

#T# 
#sensor_collision1.


#T# Ray sensor

#T# create the ray sensor, it senses if a ray intersects the face of an object
sensor_ray1 = types.KX_RaySensor()

#T# set or get axis direction, 0 is +x, 1 is +y, 2 is +z, 3 is -x, 4 is -y, 5 is -z
#T# the following sets the axis to be -y
sensor_ray1.axis = 4

#T# set or get the ray range (the length in which it detects an object)
sensor_ray1.range = 5

#T# set or get what is sensed by the ray, a material, or a property. The following sets the ray to sense for a property
sensor_ray1.useMaterial = False

#T# set or get the name of the material or property being sensed for
sensor_ray1.propName = 'property_name1'

#T# set or get whether the sensor has xrays to see through objects
sensor_ray1.useXRay = True

#T# get the global position of the face intersected by the ray
hitPosition1 = sensor_ray1.hitPosition

#T# get the normal of the face intersected by the ray as a standardized vector
hitNormal1 = sensor_ray1.hitNormal

#T# get the object intersected by the ray
hitObject1 = sensor_ray1.hitObject

#T# get the direction of the ray as a standardized vector
rayDirection1 = sensor_ray1.rayDirection