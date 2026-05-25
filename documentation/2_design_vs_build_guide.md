# Design and build guide for a custom keyboard

This manual is for **designing** and **building** a custom keyboard. 

Building a keyboard is not a difficult task if one know a little bit about
soldering and coding. However, designing a keyboard is more difficult as one
needs to take into account several restrictions and probably one also wants
to optimize the cost. 

There exists a very extensive list of existing keyboards
that can be build, so I would recommend searching online in case you find one
that fulfills your requirements. For building, the steps are:

1. Download the gerber files (which specify the PCB) and the wiring diagrams
1. Print PCB
1. Solder elements in PCB (hotswaps, switches, microcontroller, diodes, ...)
1. Download the keymap (or program it)
1. Upload the software to the keyboard
1. *Optional*: build/print a case

These steps are described in detail in `build_guide/`.

Designing a keyboard involves several variables, including:
- number of keys 
- layout of the keys
- staggering (ortholinear, row stagger, column stagger)
- split vs no-split
- wireless vs wired
- key wiring (direct vs matrix) 
- keyboard board (PCB vs handsoldering)
- microcontroller 
- firmware
- keymap
- batteries 
- switches 
- keycaps
- hotswappable 
- display 
- case
- flat vs curved

These variables are dependent between each other, for example:
- one does not need batteries if the keyboard is not wireless
- some microcontrollers do not support Bluetooth
- curved keyboards cannot use a single (flat) PCB

Therefore, it can be difficult to find the best design fulfilling a set of requirements.
The design choices and restrictions that I have made are described in 
`hardware_design_guide/` and `firmware_design_guide`.
