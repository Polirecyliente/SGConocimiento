
#   UPBGE

#T# UPBGE stands for Uchronia Project Blender Game Engine

#T# Table of contents

#T# bge package

#T# Sensors

#T# Always sensor
#T# Actuator sensor
#T# Collision sensor
#T# Delay sensor
#T# Joystick sensor
#T# Keyboard sensor
#T# Message sensor
#T# Mouse sensor
#T# Near sensor
#T# Property sensor
#T# Radar sensor
#T# Random sensor
#T# Ray sensor

#T# Beginning of content

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

#T# create the collision sensor, it senses when an object collides or touches the sensor. The object must be a rigid body, or if the object is static then it must be an actor, and the sensor must be type sensor and have collision bounds enabled
sensor_collision1 = types.KX_TouchSensor()

#T# set or get the pulse flag, which if true sends a signal each time a new object collides with the sensor, otherwise only the first collision activates the sensor and the sensor deactivates only when all objects stop touching the sensor
sensor_collision1.usePulseCollision = True

#T# set or get what is sensed by the collision sensor, a material, or a property
sensor_collision1.useMaterial = True

#T# set or get the name of the material, or property being sensed for
sensor_collision1.propName = 'material_name1'

#T# get the first object to collide with the sensor
hitObject1 = sensor_collision1.hitObject

#T# get the list of objects that are colliding with the sensor
hitObjectList1 = sensor_collision1.hitObjectList

#T# Delay sensor

#T# create the delay sensor, it waits for a number of logic ticks to then send a positive signal, and after a duration it turns off the signal
sensor_delay1 = types.SCA_DelaySensor()

#T# set or get the delay in logic ticks
sensor_delay1.delay = 60

#T# set or get the duration of the positive signal in logic ticks
sensor_delay1.duration = 20

#T# set or get the repeat flag, which if true repeats the delay duration cycle
sensor_delay1.repeat = True

#T# Joystick sensor

#T# create the joystick sensor, it senses input from a joystick
sensor_joystick1 = types.SCA_JoystickSensor()

#T# set or get the joystick index, between 0 and 7, which identifies the joystick that activates the sensor
sensor_joystick1.index = 7

#T# get the number of axes in the joystick
numAxis1 = sensor_joystick1.numAxis

#T# get a list with the values in each axis
axisValues1 = sensor_joystick1.axisValues

#T# get the number of buttons in the joystick
numButtons1 = sensor_joystick1.numButtons

#T# Keyboard sensor

#T# create the keyboard sensor, it senses input from the keyboard
sensor_keyboard1 = types.SCA_KeyboardSensor()

#T# set or get the main key that activates the sensor
sensor_keyboard1.key = events.EIGHTKEY

#T# set or get the first modifier key to hold while pressing the main key to activate the sensor
sensor_keyboard1.hold1 = events.COMMAKEY

#T# set or get the second modifier key to hold while pressing the first modifier and the main key to activate the sensor
sensor_keyboard1.hold2 = events.LEFTARROWKEY

#T# set or get the use all keys flag, which if true activates the sensor by pressing any key
sensor_keyboard1.useAllKeys = False

#T# set or get the boolean property whose value determines if the keys get logged or not
sensor_keyboard1.toggleProperty = 'boolean_property_name1'

#T# set or get the string property which will act as the key logger storing the entered key strokes
sensor_keyboard1.targetProperty = 'string_property_name1'

#T# get a list of pairs, key pressed and its status, with all the keys simultaneously pressed in a logic tick
events1 = sensor_keyboard1.events

#T# get the press status of a given key
keyStatus1 = sensor_keyboard1.getKeyStatus(events.F10KEY)

#T# Message sensor

#T# create the message sensor, it senses for the arrival of a message that was sent from a message actuator
sensor_message1 = types.KX_NetworkMessageSensor()

#T# set or get the subject of the message that the sensor will wait for
sensor_message1.subject = 'new_subject1'

#T# get the subjects received by the sensor in a logic tick, in case the sensor receives any subjects
subjects1 = sensor_message1.subjects

#T# get the bodies of the messages received by the sensor in a logic tick
bodies1 = sensor_message1.bodies

#T# get the count of messages received by the sensor in a logic tick
frameMessageCount1 = sensor_message1.frameMessageCount

#T# Mouse sensor

#T# create the mouse sensor, it senses
sensor_mouse1 = types.SCA_MouseSensor()

#T# set or get the mode of the mouse event. This is an integer, 1 means Left Button, 2 means Middle Button, 3 means Right Button, 4 means Wheel Up, 5 means Wheel Down, 6 means Movement
sensor_mouse1.mode = 4

#T# set of get the pulse focus flag, which if true sets the mouse to send a pulse each time it goes over an object, even if they overlap. This applies to the Mouse Over Any event
sensor_mouse1.usePulseFocus = False

#T# get the screen position of the mouse, [x,y] with origin at the top left of the game screen and measured in pixels
position1 = sensor_mouse1.position

#T# get the status for any of the three mouse buttons, the returned int has the same meaning as with the keyboard buttons
buttonStatus1 = sensor_mouse1.getButtonStatus(events.LEFTMOUSE)

#T# the following attributes are for the mouse over events

#T# get the object which has the mouse over
hitObject1 = sensor_mouse1.hitObject

#T# get the normal of the face under the mouse as a standardized vector
hitNormal1 = sensor_mouse1.hitNormal

#T# get the global position in which the mouse has intersected an object
hitPosition1 = sensor_mouse1.hitPosition

#T# get the UV coordinates in which the mouse has intersected an object
hitUV1 = sensor_mouse1.hitUV

#T# Near sensor

#T# create the near sensor, it senses for objects near the sensor
sensor_near1 = types.KX_NearSensor()

#T# set or get the name of the property that objects must have when they get near the sensor to activate it
sensor_near1.propName = 'new_property_name1'

#T# set or get the distance (in Blender scene units) from the sensor in which objects will activate it and send a signal
sensor_near1.distance = 3

#T# set or get the distance (in Blender scene units) from the sensor that will reset the sensor after the object leaves
sensor_near1.resetDistance = 3.1

#T# get the first object near the sensor
hitObject1 = sensor_near1.hitObject

#T# get the list of objects near the sensor
hitObjectList1 = sensor_near1.hitObjectList

#T# Property sensor

#T# create the property sensor, it takes the value of a given property and compares it to another value (can be itself), sending a signal according to the result of the comparison
sensor_property1 = types.SCA_PropertySensor()

#T# set or get the name of the property whose value is being sensed for
sensor_property1.propName = 'property_name1'

#T# set or get the mode of evaluation, the evaluation type determines the comparison that will be made, 1 means equal, 2 means not equal, 3 means interval, 4 means changed, 6 means less than, 7 means greater than
sensor_property1.mode = 6

#T# set or get the value that the property is compared against
sensor_property1.value = 120

#T# set or get the minimum and maximum values for the interval evaluation type
sensor_property1.min = 3
sensor_property1.max = 7

#T# Radar sensor

#T# create the radar sensor, it senses for objects near the sensor in a conic shape
sensor_radar1 = types.KX_RadarSensor()

#T# set or get the axis direction, 0 is +x, 1 is +y, 2 is +z, 3 is -x, 4 is -y, 5 is -z
sensor_radar1.axis = 5

#T# set or get the property name that objects must have in order to be detected when entering the radar
sensor_radar1.propName = 'property_name1'

#T# get the angle of the radar cone
angle1 = sensor_radar1.angle

#T# get the distance of the radar cone from apex to the base
distance1 = sensor_radar1.distance

#T# get the first object sensed in the radar cone
hitObject1 = sensor_radar1.hitObject

#T# get the list of objects sensed in the radar cone
hitObjectList1 = sensor_radar1.hitObjectList

#T# get the point of origin of the radar cone
coneOrigin1 = sensor_radar1.coneOrigin

#T# get the point at the center of the base from the radar cone
coneTarget1 = sensor_radar1.coneTarget

#T# Random sensor

#T# create the random sensor, it randomly sends a signal, on average half of the logic ticks the sensor sends a signal, and the other half it doesn't
sensor_random1 = types.SCA_RandomSensor()

#T# set or get the seed for the random number generation
sensor_random1.seed = 220

#T# get the last outcome as a boolean value
lastDraw1 = sensor_random1.lastDraw

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

#T# set or get the name of the material, or property being sensed for
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