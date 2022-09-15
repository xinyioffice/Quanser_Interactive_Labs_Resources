from library_qlabs_common import QLabsCommon
from library_qlabs import CommModularContainer

import math
import struct
import cv2
import numpy as np
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsActor:
    """ This the base actor class."""

    FCN_UNKNOWN = 0
    """Function ID is not recognized."""
    FCN_REQUEST_PING = 1
    """Request a response from an actor to test if it is present."""
    FCN_RESPONSE_PING = 2
    """Response from an actor to confirming it is present."""
    FCN_REQUEST_WORLD_TRANSFORM = 3
    """Request a world transform from the actor to read its current location, rotation, and scale."""
    FCN_RESPONSE_WORLD_TRANSFORM = 4
    """Response from an actor with its current location, rotation, and scale."""

    actorNumber = None
    """ The current actor number of this class to be addressed. This can be modified at any time. """
    _qlabs = None
    _verbose = False
    _classID = 0
   
    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       return

    def _is_actor_number_valid(self):
        if self.actorNumber == None:
            if (self._verbose):
                print('actorNumber object variable None. Use a spawn function to assign an actor or manually assign the actorNumber variable.')

            return False
        else:
            return True

    def destroy(self):
        """Find and destroy a specific actor. This is a blocking operation.
        
        :return: The number of actors destroyed. -1 if failed.
        :rtype: int32

        """   
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR
        c.payload = bytearray(struct.pack(">II", self._classID, self.actorNumber))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK)
            if (c == None):
                return -1

            if len(c.payload) == 4:
                num_actors_destroyed, = struct.unpack(">I", c.payload[0:4])
                return num_actors_destroyed
            else:
                return -1
        else:
            return -1            
            
    def _spawn_id(self, actorNumber, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True):
        """Spawns a new actor.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: (Optional) An array of floats for x, y and z coordinates
        :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in radians
        :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used.
        :param configuration: (Optional) Spawn configuration. See class library for configuration options.
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN
        c.payload = bytearray(struct.pack(">IIfffffffffI", self._classID, actorNumber, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()        
                
        if (self._qlabs.send_container(c)):
        
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK)
                if (c == None):
                    return -1
                if len(c.payload) == 1:
                    status, = struct.unpack(">B", c.payload[0:1])
                    return status
                else:
                    return -1
            
            return 0
        else:
            return -1 

    def _spawn(self, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True):
        """Spawns a new actor with the next available actor number for that class

        :param location: (Optional) An array of floats for x, y and z coordinates
        :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in radians
        :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used.
        :param configuration: (Optional) Spawn configuration. See class library for configuration options.
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred. Note that if this is False, the returned actor number will be invalid.
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 3 unknown error, -1 communications error. An actor number to use for future references.
        :rtype: int32, int32

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_NEXT
        c.payload = bytearray(struct.pack(">IfffffffffI", self._classID, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()        
                
        if (self._qlabs.send_container(c)):
        
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_NEXT_RESPONSE)
                if (c == None):
                    return -1
                if len(c.payload) == 5:
                    status, actorNumber, = struct.unpack(">BI", c.payload[0:5])
                    return status, actorNumber
                else:
                    return -1, -1
            
            return 0, -1
        else:
            return -1, -1 
            
    def _spawn_id_and_parent_with_relative_transform(self, actorNumber, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=0, parentClassID=0, parentActorNumber=0, parentComponent=0, waitForConfirmation=True):
        """Spawns a new actor relative to an existing actor and creates an kinematic relationship.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :param location: (Optional) An array of floats for x, y and z coordinates
        :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in radians
        :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used.
        :param configuration: (Optional) Spawn configuration. See class library for configuration options.
        :param parentClassID: See the ID variables in the respective library classes for the class identifier
        :param parentActorNumber: User defined unique identifier for the class actor in QLabs
        :param parentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type actorNumber: uint32
        :type classID: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type parentComponent: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
        :rtype: int32

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE
        c.payload = bytearray(struct.pack(">IIfffffffffIIII", self._classID, actorNumber, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, parentClassID, parentActorNumber, parentComponent))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()        
                
        if (self._qlabs.send_container(c)):
        
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK)
                if (c == None):
                    return -1

                if len(c.payload) == 1:
                    status, = struct.unpack(">B", c.payload[0:1])
                    return status
                else:
                    return -1
            
            return 0
        else:
            return -1                              
            
    def ping(self):
        """Check if an actor of the specified class and actor number is present in the QLabs environment.
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type classID: uint32
        :return: `True` if successful, `False` otherwise
        :rtype: boolean
        """

        c = CommModularContainer()
        c.classID = self._classID
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_REQUEST_PING
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()        
                
        if (self._qlabs.send_container(c)):
        
            c = self._qlabs.wait_for_container(self._classID, self.actorNumber, self.FCN_RESPONSE_PING)
            if (c == None):
                return False

            if c.payload[0] > 0:
                return True
            else:
                return False
        else:
            return False 
    
    def get_world_transform(self):
        """Get the location, rotation, and scale in world coordinates of the specified actor
        
        :return: success, location, rotation, scale
        :rtype: boolean, float array[3], float array[3], float array[3]
        """

        c = CommModularContainer()
        c.classID = self._classID
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_REQUEST_WORLD_TRANSFORM
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        location = [0,0,0]
        rotation = [0,0,0]
        scale = [0,0,0]
        
        self._qlabs.flush_receive()        
                
        if (self._qlabs.send_container(c)):
        
            c = self._qlabs.wait_for_container(self._classID, self.actorNumber, self.FCN_RESPONSE_WORLD_TRANSFORM)
            if (c == None):
                return False, location, rotation, scale

            if len(c.payload) == 36:
                location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], = struct.unpack(">fffffffff", c.payload[0:36])
                return True, location, rotation, scale
            else:
                return False, location, rotation, scale
        else:
            return False, location, rotation, scale