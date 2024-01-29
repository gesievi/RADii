.. ------Header
    _ Hyperlinks that are written xxxxx_ are collected in the conf.py so they can be modified at any time more easily.

.. |RadiiLogo| image:: ../Radii_Icons/Radii_logo.png
    :height: 50


************************************
Basics & Exploration tutorial
************************************

Length: ca. 15 min

This tutorial, is based on the Setup_ guide.

It will introduce the basics of the Radii Viewer and the Radii Grashopper plugin.
Afterward you will be able to explore a model with Radii and you publish(upload) geometry.



Radii Viewer
======================

|RadiiLogo|


**Keyboard Assignments**

=========== ===================================
Movement    W,A,S,D
Jump        Space
Shift       Sprint
Q Fly       Up
E Fly       Down
Right Mouse Main Menus (open,close)
Left Mouse  `Operation Menu`_ 
=========== ===================================


**1. Open the** `Radii Viewer`_ 

**2. Open the Main Menu**

Right-click to open & close the `Connect Menu`_.

.. image:: /tutorial/Viewer_PC/images/02_Menue.png


**3. Connect to channel**

.. image::  /tutorial/Viewer_PC/images/02_Menu_zuschnitt.png

Connect to the channel, as described in section 3 of the `Connect Menu`_.


**4. Congratulation** 

You are now connected to a channel and can explore the model.

.. ---------------------------------------------------------





====================
Radii grashopper 
====================

This is a short introduction into publishing/uploading your files to RADii.
We advice to make a Radii account as shown in the setup_ under point 2.
Further information about the grashopper plugin can be found in the RadiiGrashopper_ section.

*The following tutorial will publish/upload all the geometry that is present in your rhino file. Use it with care and not with big models.*


**1. How to build a basic file to publish**

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/01_Quick_Guide_Publisher.png

Every RadiiGrashopper_ file starts with the Connect_ component.
To it, you connect the PublishMaterial_ and the PublishGeometry_ , components.
Add a geometry pipeline or any geometry to the later as shown in the picture.





**2. Enter Credentials**

Input your Radii account details and left click on "load account" to log in.

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/02_Quick_Guide_Publisher.png





**3. Choose domain and channel**

Select "username >  My Domain", to publish on your private domain.

For further information about channel addresses go to Connect_.

*IMPORTANT*: you have to publish to the same channel that you are connected with in the viewer - typos leave you stranded.

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/03_Quick_Guide_Publisher_zugeschnitten.png





**4. Connect**

To activate the connection to the channel by turning the Toggle into true.

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/05_Quick_Guide_Publisher_true.png


**Congratulations, your model should now appear in your Radii viewer!**