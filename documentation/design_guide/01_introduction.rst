Designing a keyboard
====================

As mentioned, there are several variables that need to be considered when designing
a keyboard and they are dependent between each other. One can easily tangled up
in a big problem if they are beginners, thus it is better to first decide the important
variables first, i.e. the ones that restrict more choices later one.
To further simplify this problem, I will assume that we are building a flat 
keyboard (not a 3D one like the Glove80 or the Kinesis Advantage360). Such a 
choice will help the wiring of the keys by using a PCB instead of hand wiring.

The main restrictions come from choosing a wireless or wired keyboard. If one
wants a wireless device, there is only one (commonly used) microcontroller
that supports Bluetooth which cannot be operated using one of the most 
common firmwares. Moreover, wireless keyboards require batteries.

Most of the other variables can be easily tuned thanks to using Ergogen
(a software for designing PCBs for keyboards). However, as everyone also
want to minimize the cost, it should be noted that:
- switches and keycaps account for the most of the fraction of the total price.
  For example, in my 34-key split keyboard, they account for ~50% of the price.
- for split keyboards, one needs to buy two microcontrollers (and two batteries 
  if needed), one for each part. For the case of wireless keyboards, the 
  microcontrollers can be quite expensive (~25€), however there exist cheaper
  clones available in AliExpress (~5€).

A very complete of the different keyboard variables are:
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

In the following sections, we will go through the different options for each
vairable and (if needed) give some background and intuition of possible
restrictions and dependencies.
The different variables are discussed in the following sections (with this intro
being section 1):
- number of keys -> 2
- layout of the keys -> 3
- staggering -> 2
- split vs no-split -> 2
- wireless vs wired
- key wiring 
- keyboard board (not covered as this is only for PCB)
- microcontroller -> 5
- firmware 
- keymap
- batteries
- switches -> 3
- keycaps -> 3
- hotswappable -> 3
- display 
- case
