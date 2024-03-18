*******************
SubscribeParameter
*******************

**Grasshopper component**

.. image:: ../images/Subscribe/Sub_parameter.png
    :align: Left

**Radii viewer counterpart**

.. image:: ../images/Subscribe/Sub_parameter22.png

This component is used to subscribe to a parameter that is set in a Radii Viewer, it can then be changed in the Viewer and fed back into the grashopper session.
With the value geometry could for example be modified. 


**Input**

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Connection  Link with the Connect component         Connection
Subscribe   Toggle the subscription                 Boolean
==========  ======================================  ==============

**Output**

==================  ======================================  ==============
Name                Description                             Type
==================  ======================================  ==============
Log                 Documents changes & Data send           Text
Parameter/Boolean   Parameter/Boolean from Radii Viewer     Boolean/Number
==================  ======================================  ==============

  - The more parameters you define in the viewer the more will be on this component
  - the number will be between 0 to 1, you can remap this to any other range

