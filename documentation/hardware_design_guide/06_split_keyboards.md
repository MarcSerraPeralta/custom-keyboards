# Split keyboards

Here I explain some technicalities to be aware when designing a split keyboard

## Connection to the computer

Split keyboards have two microcontrollers, but not both of them talk directly to the computer.

The standard way is that only the left-hand part talks to the computer.
Therefore, it basically acts as a repeater for the right-hand side.
In this sense, the left-hand part is the master and the right-hand one is the slave.

For the wired case, both parts are usually connected via a TRRS jack (Ergogen has this footprint), 
and the left-hand part is connected via USB to the computer.

Note that when using Bluetooth, the left-hand side has lower battery life because
it needs to do extra processing and communication to the computer.


## Reversible PCBs

Many split designs rely on a "reversible" PCB design. 
This lets you use the same circuit board for both the left and right half of the 
keyboard (less expensive), but introduces some complexity into routing all the traces on the board. 
The reason is that the "reversibility" should be done by mirroring the PCB, but 
in our reality we can only flip the board 180 degrees, which is not the same as mirroring.

See the document `06_split_keyboards_reversible_pcb.pdf` for a better description and
solution to the problem.
