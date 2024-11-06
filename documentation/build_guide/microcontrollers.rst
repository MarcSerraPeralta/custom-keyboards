Microcontrollers
================

The two most common microcontrollers are Pro micro and NiceNano.

RP2040 is used in "cheapino" and it is ~1€ in AliExpress, but I need to
check if it has all the options I need in QMK and how to include this
board in Ergogen.
Also note that the Pro Micro can be found in AliExpress for ~3€.

Pro micro vs NiceNano
---------------------
Comparison from https://www.reddit.com/r/ErgoMechKeyboards/comments/sluweg/pro_micro_vs_nce_nano/:

**Nice!Nano**
- Requires the use of ZMK - as some others here already mentioned
    - Slightly higher learning curve, but for what it's worth, I prefer it once I got the hang of working with it
    - Is missing some of the advanced functionality in QMK and does not have the option of the more user-friendly VIA (or VIAL)
- Allows full wireless!
    - I love not having cables, and I don't want to go back
    - Does require that you also fuss about with adding a battery
- Ergogen does not have a footprint for NiceNano

**Elite-C / pro-micro**
- Uses QMK / VIA
    - More common and more richly featured
    - VIA is definitely the most approachable for a newbie to remap keys
- Cheaper
    - Especially true for the pro-micro
- Requires wires to connect the board halves and to the computer
- Ergogen has a footprint for pro-micro
