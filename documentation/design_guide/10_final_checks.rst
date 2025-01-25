Final checks
============

This is a list of the final checks to perform to the final PCB and other files.


PCB in KiCad
------------

1. Run the Design Rule Checker (DRC) in KiCad (checks unconnected components, routes too close to each other, ...)
1. Write down a simplified electrical circuit. Does it make sense?
1. Do the pads&holes for the keyswitches match the ones to install?
1. Do the microcontroller pins in the PCB match the ordering of the microcontroller pins?
1. If the PCB is reversible, does the design work when reversing the PCB?
1. If a case is made, have you forgotten about the holes for securing the PCB?
1. If a logo/text is wanted, have you forgotten to add the silkscreen of it (to both sides, if reversible)?
1. Added a reset button?
1. If wireless, added a power switch?


Gerber file
-----------

1. Open the file in a Gerber viewer (e.g. online viewer) and check that everything looks good
