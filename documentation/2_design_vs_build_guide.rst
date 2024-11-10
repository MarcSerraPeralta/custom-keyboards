Design and build guide for a custom keyboard
============================================

This manual is for designing and building a custom keyboard. 
Building a keyboard is not a difficult task if one know a little bit about
soldering and coding. However, designing a keyboard is more difficult as one
needs to take into account several restrictions and probably one also wants
to optimize the cost. There exists a very extensive list of existing keyboards
that can be build, so I would recommend searching online in case you find one
that fulfills your requirements.

If no design is required (i.e. assuming that the keyboard and keymaps have 
already been designed), the steps for building the keyboard are:

#. Generate the layout configuration (Ergogen) or copy use an already existing design
#. Print PCB
#. Solder elements in PCB (hotswaps, switches, microcontroller, diodes, ...)
#. Program the keymap
#. Upload the software to the keyboard
#. Optional: build/print case

These steps are described in detail in ``build_guide/``.

In the case one wants to go through the process of designing a keyboard or
has not found an already existing keyboard that they like, they should know that
the design involves several variables, including:
- number of keys 
- split vs no-split
- wireless vs wired
- key wiring (direct vs matrix) 
- keyboard board (PCB vs handsoldering)
- microcontroller 
- firmware 
- batteries 
- switches 
- hotswappable 
- display 

These variables are dependent between each other (e.g. one does not need batteries
if the keyboard is not wireless, some microcontrollers do not support Bluetooth, ...)
Therefore, it can be difficult to find the best design fulfilling your requirements.
These design choices and restrictions are described in ``design_guide/``.
