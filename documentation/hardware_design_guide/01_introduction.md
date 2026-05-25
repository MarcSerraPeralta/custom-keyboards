Designing a keyboard
====================

As mentioned, there are several variables that need to be considered when designing
a keyboard, which are dependent between each other. One can easily tangled up
in a big problem. 

First, we start by deciding the variables that restrict more choices later one.
Also, I know that I want to build a flat keyboard and that I will be using a PCB
to wire the keys.

The main restrictions come from choosing a wireless or wired keyboard. If one
wants a wireless device, there is only one commonly used microcontroller
that supports Bluetooth which cannot be operated using one of the most 
common firmwares. Moreover, wireless keyboards require batteries.

In my case, I want a wireless keyboard to move it around easily and to avoid 
having extra cables on my desk.

Most of the other variables can be easily tuned thanks to using [Ergogen](https://ergogen.xyz/), 
a software for designing PCBs for keyboards. 

As I want to minimize the cost of the keyboard, it should be noted that:
- switches and keycaps account for the most of the fraction of the total price.
  For example, in my 34-key split keyboard, they account for ~50% of the price.
- split keyboards require two microcontrollers (and two batteries 
  if needed), one for each part. For the case of wireless keyboards, the 
  "official" microcontrollers can be quite expensive (nice!nano ~25€), however there exist cheaper
  clones available in AliExpress (~5€).

In the following sections, I will go through the different options for each
vairable and (if needed) give some background and intuition of possible
restrictions and dependencies.
