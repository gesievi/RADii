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

    - at the time of writing indexing only works for surfaces of section plane input, clipping planes have to be selected in the menu

**Output**

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Log         Documents changes & Data send           Text
Save        Connect to Savecontent for saving       Radii content
==========  ======================================  ==============

**Menu**

==========================  ================================================
Section Duration:           how quickly the section is moving into place
Set duration:               toggle to have a moving clipping plane
Activate clipping planes:   clipping planes from rhino to be selected
==========================  ================================================
