.. _Environment_Outdoors_Library:

***********************
Outdoor Environment
***********************

.. _environmentOutdoorsDescription:

Description
============

The Environment Outdoors library is used to modify settings of the QLabs actor
environment.
Not all Open World environments support all environmental features.

.. _environmentOutdoorsLibrary:

Outdoor Environment Library
============================

.. autoclass:: qvl.environment_outdoors.QLabsEnvironmentOutdoors

.. _environmentOutdoorsConstants:

Constants
============

.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.ID_ENVIRONMENT_OUTDOORS

.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.CLEAR_SKIES
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.PARTLY_CLOUDY
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.CLOUDY
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.OVERCAST
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.FOGGY
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.LIGHT_RAIN
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.RAIN
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.THUNDERSTORM
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.LIGHT_SNOW
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.SNOW
.. autoattribute:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.BLIZZARD


.. _environmentOutdoorsMethods:

Methods
=========

.. automethod:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.set_time_of_day
.. automethod:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.set_outdoor_lighting
.. automethod:: qvl.environment_outdoors.QLabsEnvironmentOutdoors.set_weather_preset


-------------------------------------------------------------------------------

.. _environmentOutdoorsTutorial:

Weather Tutorial 
==================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |weather_tutorial.py|.

            .. |weather_tutorial.py| replace::
                :download:`Weather Tutorial (.py) <../../../tutorials/weather_tutorial.py>`

            .. literalinclude:: ../../../tutorials/weather_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |weather_tutorial.m|.

            .. |weather_tutorial.m| replace::
                :download:`Weather Tutorial (.m) <../../../tutorials/weather_tutorial.m>`

            .. literalinclude:: ../../../tutorials/weather_tutorial.m
                :language: Matlab
                :linenos:

