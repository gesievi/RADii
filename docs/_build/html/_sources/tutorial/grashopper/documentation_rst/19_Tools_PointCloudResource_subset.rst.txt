******************************************
PointCloudReduce & SubsetPointCloud
******************************************



ReducePointCloud
----------------

.. image:: ../images/Pointcloud/Pointcloudreduce.png

**Input**

=========== ======================================  ==============
Name        Description                             Type
=========== ======================================  ==============
Point Cloud Point Cloud to Reduce                   Point Cloud
Fraction    Fraction of Points to remain            Number
=========== ======================================  ==============

**Output**

===========  ======================================  ==============
Name         Description                              Type
===========  ======================================  ==============
Point Cloud  Reduced Point Cloud                      Point Cloud
===========  ======================================  ==============





SubsetPointCloud
-----------------

.. image:: ../images/Pointcloud/Pointcloudbox.png

**Input**

=============   ======================================  ==============
Name            Description                             Type
=============   ======================================  ==============
Point Cloud     Point Cloud to Reduce                   Point Cloud
Selection box   Volume you want to keep                 Box
=============   ======================================  ==============

**Output**

===========  ======================================  ==============
Name         Description                             Type
===========  ======================================  ==============
Point Cloud  Selection of Point Cloud                Point Cloud
===========  ======================================  ==============

