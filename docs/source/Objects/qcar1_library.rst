.. _QCar1_Library:

*******
QCar
*******

.. image:: ../pictures/banner_qcar.png
    :width: 800px
    :align: center

.. _carDescription:

|

Description
=============

QCars are considered "actors" in Quanser Interactive Labs. The QCar library can
be used to acquire sensor data from the virtual environment and controls the
motion of the vehicles.

See the :ref:`QCarTutorial` to get a better understanding of using QCars in
Quanser Interactive Labs.

.. _carLibrary:

Library
=========

.. autoclass:: qvl.qcar.QLabsQCar

.. _carConstants:

Constants
===========

.. autoattribute:: qvl.qcar.QLabsQCar.ID_QCAR

.. note::
    CSI camera resolution is 820x410.


.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_RIGHT
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_BACK
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_LEFT
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_FRONT

.. note::
    RGB and depth resolution is 640x480.

.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_RGB
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_DEPTH

.. note::
    Overhead and trailing cameras support user zoom using the mouse wheel.

.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_OVERHEAD
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_TRAILING


.. _carMemberVars:

Member Variables
=================

.. autoattribute:: qvl.qcar.QLabsQCar.actorNumber

.. _carMethods:

Methods
=========

.. automethod:: qvl.qcar.QLabsQCar.set_transform_and_request_state
.. automethod:: qvl.qcar.QLabsQCar.set_transform_and_request_state_degrees
.. automethod:: qvl.qcar.QLabsQCar.set_velocity_and_request_state
.. automethod:: qvl.qcar.QLabsQCar.set_velocity_and_request_state_degrees
.. automethod:: qvl.qcar.QLabsQCar.possess
.. automethod:: qvl.qcar.QLabsQCar.ghost_mode
.. automethod:: qvl.qcar.QLabsQCar.get_image
.. automethod:: qvl.qcar.QLabsQCar.get_lidar


.. _carParentMethods:

Parent Class (actor.py) Methods
================================

.. automethod:: qvl.qcar.QLabsQCar.__init__
.. automethod:: qvl.qcar.QLabsQCar.spawn
.. automethod:: qvl.qcar.QLabsQCar.spawn_degrees
.. automethod:: qvl.qcar.QLabsQCar.spawn_id
.. automethod:: qvl.qcar.QLabsQCar.spawn_id_degrees
.. automethod:: qvl.qcar.QLabsQCar.destroy
.. automethod:: qvl.qcar.QLabsQCar.destroy_all_actors_of_class
.. automethod:: qvl.qcar.QLabsQCar.ping
.. automethod:: qvl.qcar.QLabsQCar.get_world_transform
.. automethod:: qvl.qcar.QLabsQCar.get_world_transform_degrees

    
.. _carConfig:

Configurations
===============

There is only one configuration of the QCar actor.

.. _carConnect:

Connection Points
===================

.. image:: ../pictures/qcar_connection_points.png
    :scale: 50%
    :align: center

|

.. table::
    :widths: 11, 11, 25, 53
    :align: center

    ====================== ============ ====================================================== ===========
    Reference Frame Number Parent Frame Relative Transform to Parent (Location, Rotation)      Description
    ====================== ============ ====================================================== ===========
    0                                                                                          The base frame is located at ground level, centered between the two rear wheels. This represents the location of the car with no filtering, suspension, or dynamics. Collision detection is connected to this reference frame.
    1                      0            [0,0,0] [0,0,0]                                        The filtered frame is co-located with connection point 0, but it is a filtered position to simulated the suspension and dynamic effects. All the visual elements and sensors of the QCar are connected to this frame.
    ====================== ============ ====================================================== ===========


Component Extrinsics
=======================

"Extrinsics" refer to the external relationship of an object with respect to a
specific frame of reference (in this case the body center of the QCar).
Sometimes it's important to know specific distances and orientation of
extrinsic components, for instance, this can be use for obstacle detection and
camera calibration.
You will find a list of the important extrinsics below.

Distances From Body Center
***************************
The body frame is located between the front and rear axles on the ground plane.
Distances of the QCar in its virtual environment are 10 times larger than on the 
physical system so a QCar spawned at a scale of 1 is equivalent size to a full-scale
automobile. A QCar spawned at a scale of 0.1 will be equivalent to the size of a
physical QCar.


.. image:: ../pictures/qcar_bodyframe.png
    :scale:  65%
    :align: center

.. table::
    :widths: 11, 11, 11, 11
    :align: center

    ========== ====== ====== ======
    Component  x (m)  y (m)  z (m)
    ========== ====== ====== ======
    CG          0.248 -0.074 0.709
    Front axle  1.300  0     0.310
    Rear axle  -1.300  0     0.310
    CSI front   1.930  0     0.953
    CSI left    0.140  0.438 0.953
    CSI rear   -1.650  0     0.953
    CSI right   0.140 -0.674 0.953
    IMU         1.278  0.223 0.895
    RealSense   0.822  0.003 1.582
    RPLIDAR    -0.108 -0.001 1.799
    ========== ====== ====== ======

|

Transformation Matrices
************************

All transformation matrices are built off of the body frame and camera frames
for the QCar.
To read more about this check out our documentation
`here <https://www.quanser.com/products/self-driving-car-studio/>`__
by clicking on Research Resources link and looking inside the zip folder for
src/user_manuals/qcar/user_manual_system_hardware.pdf

.. image:: ../pictures/qcar_extrinsic_matrices.png
    :scale:  65%
    :align: center

-------------------------------------------------------------------------------

.. _QCarTutorial:

QCar Tutorial
===============

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |qcar_tutorial.py|.

            .. |qcar_tutorial.py| replace::
                :download:`QCar Tutorial (.py) <../../../tutorials/qcar_tutorial.py>`

            .. literalinclude:: ../../../tutorials/qcar_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |qcar_tutorial.m|.

            .. |qcar_tutorial.m| replace::
                :download:`QCar Tutorial (.m) <../../../tutorials/qcar_tutorial.m>`

            .. literalinclude:: ../../../tutorials/qcar_tutorial.m
                :language: Matlab
                :linenos:
    

.. **See Also:**
