********************************
Tutorial: Collaborative working
********************************

Radii can be used in a linear way, sending commands and geometry from Grasshopper to the viewers.

The components in the Subscribe section in Rhino Grasshopper Radii can add the reverse diction to the workflow. 
With them we can send data from the viewers through the server into Grasshopper.
Because of the amount of possibilities with these components, we will only give a few examples that we found useful. 

1. **Working and assembling geometry together in the viewers on a channel:** 

  Geometry is first send from Grasshopper with PublishGeometry_ to the viewers, it is important that the shared option is selected in the component.
  The geometry can then be modified in the viewer in collaboration and fed back into Rhino via the `Subscribe Geometry`_ component.
  After baking or internalizing the fed back geometry it can be permanently stored.

  .. image:: ../Quick_Guide/4_LV_Subscribe_Images/Subscribe_Geometry_Grasshopper_viewer.png

  .. image:: ../Quick_Guide/4_LV_Subscribe_Images/Subscribe_Geometry_Grasshopper.png

  Components needed:

  - `Connect`_
  - PublishGeometry_
  - PublishMaterial_
  - `Subscribe Geometry`_




2. **Recording the viewers movement and using it to create an animation path.**
  
  It can be quiet difficult to create a smooth animation path with Rhino, this can be done by recording the movement of the viewer and using it to create an animation path as shown in the example below.

  .. image:: ../Quick_Guide/4_LV_Subscribe_Images/Recording_Path_viewer_planes_icons_rhino.png
  
  Components needed:

  - `Connect`_
  - `Subscribe User`_
  - Data Recorder
  - Cull Duplicates
  - List Item
  - `Publish Animation`_

   

