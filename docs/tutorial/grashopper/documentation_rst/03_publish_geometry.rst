******************
PublishGeometry
******************


.. image:: ../images/Publish/Publish_geometry.png
    :scale: 80 %

This component is used to select geometry that should be published to a channel.

**Input**

=========== ================================ ================
Name        Description                         Type
=========== ================================ ================
Connection  Link with the Connect component     Connection
Geometry    Geometry you want to upload         Brep or Mesh
Quality     Mesh Quality for conversion         Settings
=========== ================================ ================

**Quality:** 
To control the quality of your geometry you can use the following components

    - Setting (Speed)
    - Setting (Quality)
    - Setting (Custom)

      - use "Min Edge" to sett the minimal edge length this will make your model low poly if you go to high

**Output**

=====   =====================================   ===================
Name    Description                             Type
=====   =====================================   ===================
Log     Documents changes & data send           Text
Save    Connect to Save component for saving    Radii content
=====   =====================================   ===================


- Log can help identify how much data and what kind of it is send


**Menu:**

==========  =====================================================
Update:     update only changed geometry
Rebuild:    republish everything in the component
Render:     visible/invisible
Collision:  permeable/impermeable
Physics:    objects push on each other
Gravity:    9.807 m/s² pulling on each object
Shared:     collaborative editing of geometry in the viewer
==========  =====================================================

**Video tutorials:**

- `Collaborative content modification <https://www.youtube.com/watch?v=YuBep3x01cE>`_
  
  - activate the "Shared" option in the menu
- `Collaboration  <https://www.youtube.com/watch?v=PVB9a0dsJfQ>`_
-  
