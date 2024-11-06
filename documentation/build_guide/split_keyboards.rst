Split keyboards
===============

When not using bluetooth for split keyboards, then both parts of the keyboard
need to talk to the computer. 
The usual way of achieving this is by having on microcontroller in each part
and have them connected via a TRRS jack (Ergogen has this footprint). Finally,
only one of the parts needs to be connected to the computer.

Many split designs also rely on a "reversible" PCB design. 
This lets you use the same circuit board for both the left and right half of the 
keyboard, but introduces some complexity into routing all the traces on the board.
