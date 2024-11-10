Split keyboards and connection to computer
==========================================

Non-split keyboards have a simple connection to the computer. It can be 
either through a wire or via Bluetooth. As there is only a single piece, 
we just need this piece to talk to the computer.

For split keyboards, we have two pieces, but not both of them talk to the computer.
The standard way is to have the left-hand part talk to both the computer and the
right-hand side. In this sense, the left-hand side is the master and the right-
hand side is the slave. As we don't want several wires brigding the two parts,
each piece has its own microcontroller and they communicate using either
through a physical wire or Bluetooth. For the wired case, they are usually connected 
via a TRRS jack (Ergogen has this footprint), although they are connected via
USB to the computer.
Note that when using Bluetooth, the left-hand side has lower battery life because
it needs to do extra processing and communication to the computer.


Reversible PCBs
---------------

Many split designs rely on a "reversible" PCB design. 
This lets you use the same circuit board for both the left and right half of the 
keyboard, but introduces some complexity into routing all the traces on the board. (HOW?)
I still need to look into this...
