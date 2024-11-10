Building guide
==============

This guide assumes that one already has a "theoretical" design for the keyboard 
(see ``design_guide/`` if you don't). The "theoretical" part means that it is
designed on paper but one does not have generated the PCBs, firmware, ...
Note that if you have chosen to build an already existing keyboard, you can 
skip some of the building steps as you (should) already have the Gerber files for
the PCBs, the config file for the firmware, ...

As you may have already seen, this is not a general guide for any keyboard, 
but the following assumptions are made:
- The wiring of the switches to the microcontroller is done in a PCB (not
  handwired). This sets the limitation that the keyboard will be flat.
