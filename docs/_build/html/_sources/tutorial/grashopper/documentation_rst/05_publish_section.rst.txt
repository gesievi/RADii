****************
PublishSection
****************

.. image:: ../images/Publish/Publish_section.png
    :scale: 80 %

**Input**

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Connection  Link with the Connect component         Connection
Section     Plane A plane that will cut the model   Plane/surfaces
Index       Select a plane from a list              Number
==========  ======================================  ==============

    - at the time of writing index only works for a list of surfaces in the input: section plane
    - Rhino clipping planes have to be selected in the menu at -Activate clipping planes-

**Output**

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Log         Documents changes & Data send           Text
Save        Connect to SaveContent for saving       Radii content
==========  ======================================  ==============

**Menu**

==========================  ================================================
Section Duration:           how quickly the section is moving into place
Set duration:               toggle to have a moving clipping plane
Activate clipping planes:   clipping planes from rhino to be selected
==========================  ================================================

**Note:** 

- In Rhino flipping a clipping plane is not recognized by Radii, rotating the plane by 180° however archives the same
- Names of clipping planes are not carried over into the grashopper plugin