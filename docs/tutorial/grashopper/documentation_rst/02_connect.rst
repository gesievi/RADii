************
Connect
************

The connect component is the **central component** of the radii plugin, every other component is connected to it, via "Connection" output.
Only those components who are connected will be published, when you switch the Toggle to true.
With it you can select the channel you want to publish to, and log into your Radii account.

**Input**

========    ====================================== ================
Name            Description                            Type 
========    ====================================== ================
Connect        Start the connection to the server     Boolean
Point to       The rhino view is sending a pointer    Boolean
Follow         Everyone follows the rhino view        Boolean
========    ====================================== ================

    `Follow video Demo <https://www.youtube.com/watch?v=h-5thZiZg1Q>`_

**Output**

===========  ================================================== ================
Name            Description                                     Type
===========  ================================================== ================
Connection   All further components have to be connected here   Radii components
===========  ================================================== ================

.. image:: ../images/Connect/Connect_gh.png
    :scale: 80 %

**Right click menu:**

.. image:: ../images/Connect/Connect.1.png

- Give yourself a *nickname* (this will be your name for other user in the viewer)
- input your:
    - User Name
    - Password
- click on "load account"
- if you do not have an account create one on `radii.info`_

Note: If you are part of a group or organization please use the respective email address.

.. image:: ../images/Connect/Connect.11.png



**About channels and subchannels and subsubsubchannels**
The way to write channel addresses in the viewer is channelname.subchannel.sub.sub and can be endlessly extended. 
In Radii grasshopper the same address is reached by logging in, choosing "channelname > My Domain" and then under "-subchannel-" 
typing subchannel.sub.sub 

.. image:: /tutorial/Quick_Guide//1_LV_Explo_Images/Grashopper/03_Quick_Guide_Publisher_zugeschnitten.png


Example:
The channelname "sun" in grasshopper:
-channel-
Sun > My Domain

-subchannel-
hs23.g1

In the Radii viewer:
-channel-
sun.hs23.g1 



