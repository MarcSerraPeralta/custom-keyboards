Generating the layout configuration file
========================================

This section is about how to go from an idea/drawing of a layout to an actual 
configuration file which can be used to generate the PCB files. 

Ergogen (https://github.com/ergogen/ergogen) allows to generate the PCB files and other
useful files from a configuration format. The project has an interactive website but can 
also be installed from GitHub. It has more than 800 stars in GitHub. 
The documentation can be found in https://docs.ergogen.xyz/metadata. 

A high-level tutorial can be found in: https://www.youtube.com/watch?v=M_VuXVErD6E

(I think it would be useful to explain a full configuration YAML file here)


General concepts for building the layout configuration
------------------------------------------------------

The layout information/configuration is stored in a YAML file. 
The main parts in the layout file are the ``"points"``, the ``"outlines"``,
and the ``"pcbs"``. 
The points part describes the poisition of the keys, the outlines
part describes the PCB outlines, plate and case, and finally the pcbs part
describes the wiring of the keys and the microcontroller used.

Another part is the ``"units"``, which include a description of units to 
be used when describing the points. By default we have the following units:

.. code:

   U: 19.05 # 19.05mm MX spacing
   u: 19 # 19mm MX spacing
   cx: 18 # 18mm Choc X spacing
   cy: 17 # 17mm Choc Y spacing


Points
------

For defining the points, we have several layers of abstractions to make the
process easier. The top layer are the "zones", which correspond to a set of 
points or anchors. Usually, a zone correspond to a column of keys.
The middle layer are the "anchors", which allow to place points from an 
existing starting point (or anchor) through translations and rotations.
Finally, the bottom layer are the points, which correspond to a set of
``x, y, r`` coordinates that is used to specify the center (``x, y``)
and the orientation (``r``) of the keys. 

The YAML file will have the following structure in the points part:

.. code:

   points:
     zones:
       <zone_name>: # A unique key for each zone
         anchor: # Optional anchor to position the zone, default = [0, 0, 0°]
         columns: 
           <column_name>: # A unique key for each column within the zone
             rows:
               <row_name>: <defs> # Key-level attributes set here apply to this key alone
             key: <defs> # Key-level attributes set here apply to the whole column
         rows:
           <row_name>: <defs> # Key-level attributes set here apply to the whole row
         key: <defs> # Key-level attributes set here apply to the whole zone
     key: <defs> # Key-level attributes set here apply to ALL zones


Note that in each zone, we can have multiple columns because sometimes we
want to have several columns at the same level, i.e. all the keys in a 2D grid.
The number of keys in each zone is the product of the number of columns and
the number of rows. By default they correspond to a 2D square grid, but they can be 
staggered or rotated (see below). If one wants different amount of keys in
each column, then one has two define a zone for each of them.

All the configuration is done through the use of ``key``s. They can contain any
metadata as attributes, but only some of them have meaning for layout out positions.
The useful keys can be found in: https://docs.ergogen.xyz/points#keys
An example of how the keys are used to setup the layout can be found in:
https://docs.ergogen.xyz/points#layout

The zones can be rotated (``rotate``) and mirrored (``mirror``) as a whole.

To define the correct size of the keys (e.g. Choc), use the following code:

.. code:
     
   points:
     key:
       width: cx
       height: cy
       spread: cx
       padding: cy
     zones:

As a summary, the width and height determine the size of the rectangles
representing the keys. The spread and padding represent the horizontal and
vertical separation between columns and rows. In this example, if any columns
and rows are added, the output will be a 2D grid without space between keys. 

With these tools in mind (as well as all the keys described in the Ergogen
documentation), one should be able to draw the rectangles in the specific
position one wants. 
The next section (Outlines) describes how to define outlines for the PCB, 
case, ...

Notes:
- When copying the layout from an svg file, Inkscape can display the rotation
  of an object from the XML editor. The angle is reported inside the rotate
  function in the transform attribute.
- When rotating and moving the columns, remember that the ``"spread"``, 
  ``"stagger"`` and ``"splay"`` refer to the horizontal movement with respect 
  to the center of the bottom key in previous the column. And the horizontal
  movement and vertical movement is with respect to a rotated reference system
  given by the previous column.
- The size of the Choc MBK keycaps is 17.5x16.5mm but the spacing is set up by 
  default to be 18x17mm (``cx, cy``) to avoid the keycaps touching each other. 


Outlines
--------

As the name suggest, this part defines the outline of the pcb, case and others. 
We want the keys to be in a single solid shape, i.e. we want them to be in the same board,
therefore we need to add shapes and run boolean operations to get a final outline.

The first part is joining the keys that are "together", e.g. the ones (almost)
touching each other. This is achieved by ``"bind"`` which grows the keys by
the specified amount in each direction to join them when they overlap. 
