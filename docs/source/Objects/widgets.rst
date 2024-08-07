.. _widgets:

*********
Widgets
*********

.. image:: ../pictures/banner_widget.png
    :align: center

|

.. _widgetDescription:

Description
============

Widgets work slightly differently then the other objects in the QLabs
Workspaces.
They are special actors that cannot be addressed after they have been spawned;
therefore they cannot be deleted individually, they do not support parenting,
and all actor properties must be set when they are spawned.
The advantage of widgets is that they are highly efficient dynamic actors so
it is possible to spawn thousands of widgets while maintaining performance.

In addition to the visible properties of widgets, widget actors can also
individually contain invisible properties such as mass, a numerical ID tag,
and a general purpose properties string.
Some actors that are designed to interact with widgets include class methods to
read these properties.

If you need the ability to make shapes static or the ability to address,
modify, or parent shapes, see :ref:`Basic Shapes` instead.

See the :ref:`widgetTutorial` to get a better understanding of using people in
Quanser Interactive Labs.


.. _widgetlibrary:

Library
=========

.. autoclass:: qvl.widget.QLabsWidget

.. _widgetConstants:

Constants
============

.. tip::
    See :ref:`widgetTutorial` to see the different flooring options.

.. autoattribute:: qvl.widget.QLabsWidget.CUBE
.. autoattribute:: qvl.widget.QLabsWidget.CYLINDER
.. autoattribute:: qvl.widget.QLabsWidget.SPHERE
.. .. autoattribute:: qvl.widget.QLabsWidget.AUTOCLAVE_CAGE
.. autoattribute:: qvl.widget.QLabsWidget.PLASTIC_BOTTLE
.. autoattribute:: qvl.widget.QLabsWidget.METAL_CAN

.. _widgetMethods:

Methods
=========

.. automethod:: qvl.widget.QLabsWidget.__init__
.. automethod:: qvl.widget.QLabsWidget.spawn
.. automethod:: qvl.widget.QLabsWidget.spawn_degrees
.. automethod:: qvl.widget.QLabsWidget.destroy_all_spawned_widgets
.. automethod:: qvl.widget.QLabsWidget.widget_spawn_shadow

.. _widgetConfig:

Configurations
===============
There are 5 different types of widgets that can be spawned in the widgets
class.

    * 0 - Cube
    * 1 - Cylinder
    * 2 - Sphere
    * 4 - Plastic Bottle
    * 5 - Metal Can

.. image:: ../pictures/configuration_widgets.png


.. _widgetConnect:

Connection Points
==================

There are no connection points for this actor class.

-------------------------------------------------------------------------------

.. _widgetTutorial:

Widget Tutorial
==================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |widgets_tutorial.py|.

            .. |widgets_tutorial.py| replace::
                :download:`Widgets Tutorial (.py) <../../../tutorials/widgets_tutorial.py>`

            .. literalinclude:: ../../../tutorials/widgets_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |widgets_tutorial.m|.

            .. |widgets_tutorial.m| replace::
                :download:`Widgets Tutorial (.m) <../../../tutorials/widgets_tutorial.m>`

            .. literalinclude:: ../../../tutorials/widgets_tutorial.m
                :language: Matlab
                :linenos:

