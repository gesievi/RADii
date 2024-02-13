********************************
Tutorial: Collaborative working
********************************

Radii can be used in a linear way, sending commands and geometry from Grashopper to the viewers.

The components in the Subscribe section in Rhino Grashopper Radii can add the reverse diction to the workflow. 
With them we can send data from the viewers through the server into Grashopper.
Because of the amount of possibilities with these components, we will only give a few examples that we found useful. 

1. **Working and assembling geometry together in the viewers on a channel:** 

  Geometry is first send from Grashopper via the PublishGeometry_ to the viewers, it is important that the shared option is selected in the component
  It can then be modified in collaboration and reimported via the `Subscribe Geometry`_ component.
  After baking or internalizing it can be permanently stored.

  Components needed:
  
  - `Connect`_
  - PublishGeometry_
  - PublishMaterial_
  - `Subscribe Geometry`_




2. **Recording the viewers movement and using it to create an animation path.**

    Components needed:

  - `Connect`_
  - `Subscribe User`_
  - Data Recorder
  - Cull Duplicates
  - List Item
  - `Publish Animation`_


.. image:: ../Quick_Guide/4_LV_Subscribe_Images/Recording_Path_viewer_planes_icons_rhino.png
   

