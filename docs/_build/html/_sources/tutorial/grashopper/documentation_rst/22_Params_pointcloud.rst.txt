**************************
Pointcloud
**************************

.. image:: ../images/Params/Params_Pointcloud.png
    :scale: 60%

This component is a relay that lets you organize your wires more efficiently.


**Optional Input**

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Connection  Link with the Connect component         Connection
==========  ======================================  ==============

**Output**

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Connection  Link with the Connect component         Connection
==========  ======================================  ==============



The Pointcloud component lets you link a pointcloud from your Rhino scene, it also can generate a new pointcloud from a mesh.
The generation works by taking each mesh vertex as a point, the finer your mesh the more detail your cloud will have.
If your mesh is coloured with the color mesh component, the colors will be transferred to the pointcloud.

