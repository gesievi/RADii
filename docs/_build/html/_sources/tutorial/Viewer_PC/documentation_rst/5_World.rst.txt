************
World Menu
************
.. image:: /tutorial/Radii_Icons/World.png


.. image:: ../images/World_menu_detail.png
  :align: left

1. **Camera**

   - Field of view - controls the field of view 
   - Sensitivity - mouse sensitivity
   - Speed - movement speed
   **Note:** turn slow when someone is following you through the project

2. **Effects** - turning them off increases performance

   - Motion = motion blur
   - Bloom = makes bright spots bleed at the edges, simulating a real camera
   - DOF = depth of field - distance between closest and furthest part of an image that are in focus
   - Chrom = chromatic effect - adds artifacts to the image, simulating a poor len
   - Vignet = darkening on the edges of images, simulating real cameras
   - Inverse = clipping/sectioning leaves a ghost of the hidden geometry

3. **Point Cloud**

   - Point Size
   - Point near size = increases point sizes near you
   **Note:** point clouds are disabled in IOS/Android viewers because they require a lot of computing power

4. **Weather**

   - Quality = resolution of the sky, above lv3 not significantly better
   - Condition = types of weather: rainy, foggy and sunny
   - Fog density = can hide the horizon but also your model
   **Note:** for better performance: turn weather to sunny, fog off, quality to lowest

5. **Time**
6. **Transform**

   - Rotation = rotates all models around the 0 point
   - Scale



7. **Select Viewer**

   .. image:: /tutorial/Radii_Icons/Viewer.png

   - Standard
	 - Stereo Shutter = for active 3D glasses
	 - Chroma Key = a virtual green screen
	 - Pepper Ghost = displays the model in a virtual box
	 - Augmented Reality (AR) = displays virtual model in a real environment - available on IOs, Android, Oculus

8. **Position**

   .. image:: /tutorial/Radii_Icons/Position.png

   - Tracker Method = for using Pepper Ghost viewer mode
     - Tracking is done with a camera and the external software: `Optitrack <https://github.com/opentrack/opentrack/>`_

9. **Projection**

   .. image:: /tutorial/Radii_Icons/Projection.png

   - Projection = screen size settings
     - you can also edit the overall scale and height of the horizon

10. **Grid** = toggles the default floor
11. **Origin** = toggles the origin point

Video tutorials:

- `Time animation <https://www.youtube.com/watch?v=nheVCJKet8k>`_
- `Scaling <https://www.youtube.com/watch?v=72bPt8c2lzM>`_