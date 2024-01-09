.. ------Header
    _ Hyperlinks that are written xxxxx_ are collected in the conf.py so they can be modified at any time more easily.

.. |RadiiLogo| image:: ../Radii_Icons/Radii_logo.png
    :height: 50


************************************
Short Basics & Exploration tutorial
************************************

Length: ca. 20 min

This tutorial, is based on the Setup_ guide.

It will introduce the basics of the Radii Viewer and the Radii Grashopper plugin.
Afterward you will be able to explore a model with Radii and you publish(upload) geometry.


======================
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

Connect to the channel as described in section 3 of the `Connect Menu`_ by writing the Channelname, the Nickname and pressing connect.


**4. Congratulation** 

You are now connected to a channel and can explore the model.

.. ---------------------------------------------------------


====================
Radii grashopper 
====================

This is a short introduction into publishing/uploading your files to RADii.
We advice to make a Radii account at radii.info if you want to have your personal space and more storrage.
More Detail can be found at RadiiGrashopper_ documentation

*The following tool will Publish/Upload all the Geometry in your rhino file. Use it with care and not with big models.*


**1. How to build a basic file to publish**

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/01_Quick_Guide_Publisher.png

Every RadiiGrashopper_ file starts with the Connect_ |Connect| component.
To it, you connect the PublishMaterial_ |PublishMaterial_icon| and the PublishGeometry_ |PublishGeometry_icon|, components.
Add a geometry pipeline or any geometry to the later as shown in the picture.


.. |Connect| image:: /tutorial/Radii_Icons/ConnectParam.png
.. |PublishMaterial_icon| image:: /tutorial/Radii_Icons/Material.png
.. |PublishGeometry_icon| image:: /tutorial/Radii_Icons/Mesh.png


**2. Enter Credentials**

Log in with your Radii.info account and password you have created during the setup_ on Radii.info as shown.
left click on "load account" to log in.
Your private domain will show up under - CHANNEL - and possibly others if you are part of a class or group, we have blanked out our group name in the example image.

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/02_Quick_Guide_Publisher.png



**3. Choose domain and channel**

Right click on the Connect component, there should be a tick next to "username >  My Domain", in this state your would publish your geometry on on your personal channel.

If you want to publish on your groups channel, change the tick to its respective name, in this example that could be sun and should show up as  " sun > My Domain" 
Press Enter to confirm.

More information about channel addresses under Connect_.

*IMPORTANT*: you have to publish to the same channel that you are connected with in the viewer - typos leave you stranded.
If you save your grasshopper file, it will remember your login settings and channel. The viewer will also remember the channel that it was connected to.

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/03_Quick_Guide_Publisher_zugeschnitten.png



**4. Connect**

To activate the connection to the channel double click on the dark "false" on the Boolean Toggle to turn it into true.

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/05_Quick_Guide_Publisher_true.png


**Congratulations, your model should now appear in your Radii viewer!**