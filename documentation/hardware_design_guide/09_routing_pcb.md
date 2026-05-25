# Routing the PCB

The output PCB from Ergogen has the information about the wiring but does not have
the physical connections, named **traces**, which need to be (manually) defined.
I will be using [KiCad](https://www.kicad.org/) for that.

In routing/tracing, it is ideal that:
- the PCB is covered with ground planes (with corresponding via stiching)
- the traces are thick (e.g. 0.25 mm for signal traces and 0.50 mm for power ones)
- the traces have a 45 degree angle
- the traces have a good clearance (e.g. 0.20 mm)
- the PCB passes all DRC checks

See sections below for more information.

Some useful tricks when working with KiCad:
- Before starting to route, rotate the PCB so that the traces done by KiCad
(which are vertical, horizontal, and 45 degrees) align well with the PCB.
This can be done by:
    1. Making all layers visible
    1. Selecting all elements: `Cntl + A`
    1. `Shift + M`
    1. Specify angle and click OK

    The PCB can be moved with the mouse by clicking `M`
- Before starting to route, set up the trace thickness, clearance and other properties.
This can be done by going to `File > Board Setup > Design Rules > Net Classes`.
One can define different defaults and set each trace (e.g. `GND`) to a different default.
- Before starting to route, check if the reversibility of the PCB makes sense
- Select the correct layers and use `X` to start routing.
- Load the JLCPCB ruleset for the DRC check.
This can be done by copy-pasting the content of `.kicad_dru` files
into `File > Board Setup > Design Rules > Custom Rules`.
*Note: I could not find any updated ruleset for JLCPCB for Kicad 10.*
- Leave space between the drilled holes and the traces.


### Ground planes

In KiCad, ground planes can be added easily, see the following tutorial

- ["KiCad Ground Planes Tutorial (1m)" by Petras Swissler](https://www.youtube.com/watch?v=DNTgrTukltw)

Some other tips:
- Avoid having islands of copper not connected to `GND` (generated from ground planes).
- Add ground planes to both the top and bottom faces of the PCB.
- Add vias to connect the top and bottom faces (via stitching), 
especially near the microcontroller and board edges. 
- Leave some room between the edge of the PCB and the ground plane (e.g. 0.5 mm).



### Drawings

Silkscreen






https://www.reddit.com/r/AskElectronics/comments/1g9382w/my_first_pcb_ferris_sweep_reversible_with_choc/
