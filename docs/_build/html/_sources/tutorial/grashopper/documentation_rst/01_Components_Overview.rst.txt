********************
Grashopper Overview
********************

.. image:: ../images/all_components.png
    :scale: 120 %

There are 6 types of components:

| **Connect** is the fundamental component to connect to a channel, it is always connected to all components that are in use.
| **Params** relay the described datatype 
| **Publishing** components can send data to a channel and its connected receivers.
| **Saving** enables you to save locally to .radii files or on a channel in the cloud.
| **Subscribing** imports data from from a connected channel to your local Rhino Grashopper session. The data can then be further processed or saved.
| **Tools** to modify point clouds 

Grashopper Components
_____________________________

.. the naming in toctree is case sensitive

**Publish Components**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *connect
    *publish*

**Save Content**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Save*

**Subscribe Components**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Subscribe*

**Tool Components & Tips**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Tools*
    *10_Tips*