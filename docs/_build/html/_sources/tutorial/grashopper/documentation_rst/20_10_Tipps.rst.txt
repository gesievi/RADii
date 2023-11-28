***************************************************
10 tipps & Tricks for working with geometry
***************************************************



=== ================================================================================    ==================================================================================================
 1  You shall use mesh count wisely                                                     Dont use thousands of vertices on a small door handle Manual: Chapter 4.3 PublishGeometry
 2  You shall not use hidden or duplicate objects and materials                         Purge objects that are never going to be seen by anybody or used by anything
 3  You shall apply level of detail relative to object size, importance and distance    Dont spend time and performance doing high level of detail on objects you will never get close to
 4  You shall keep texture resolutions low and relative object sizes                    Dont use large texture resolution on small objects
 5  You shall trim and subsample point clouds relative to distance and visibility       Dont use millions on points on something that is seen from far away or obscured by other objects
6   You shall only apply collision to objects that auser is required to collide with    Dont put collision on screws, nails, fixtures etc. Manual: Chapter 4.3 PublishGeometry
7   You shall target content to specific viewer platforms                               Dont expect to run a heavy scene on and underpowered platform like a mobile phone or Oculus Standalone
8   You shall watch the scene for places of performance degradation                     Always test the scene for places where the performance drops (no lower than 25-30 fps) and react accordingly with any of the above
9   You shall only publish when needed                                                  Dont spam with content. Use a data dam to control when to send. Use a component for volatile content and another for large static content like context.
10  You shall report bugs                                                               Always report a bug to the radii slack channel
=== ================================================================================    ==================================================================================================
