# Microcontrollers

**Microcontrollers** are the "small brains" of the keyboard.
They run the firmware (or software) that e.g. transmits `A` when both
the `a` and `Shift` key are pressed.

For simplicity, most keyboards use a **microcontroller board**, which is a PCB
with pins and wiring to the microcontroller to simplify wiring in the keyboard.
The microcontroller is just the chip, not the whole PCB or board.

In particular, most keyboards use a microcontroller board that is compatible
with the **Pro Micro** board.

> "The Pro Micro is an Arduino-compatible microcontroller board developed under 
an open hardware license by Sparkfun. "
-- from [Deskthority](https://deskthority.net/wiki/Arduino_Pro_Micro)

Boards pin-compatible with the Pro Mictro have the same pinout layout and dimensions.
Some Pro Micro "clones" can have extra functionality (e.g. Bluetooth support).
The microcontroller determines the available functionality, for example:
- The original Arduino Pro Micro board uses the ATmega32u4 microcontroller with allows
  for connection via a micro-USB type B.
- The nice!nano board uses the nRF52840 microcontroller which allows for both
  USB type-C and Bluetooth 5.

The most common microcontroller boards are: 
- Arduino Pro Micro (~5-10€)
    - Microcontroller: ATmega32u4
- Pro Micro RP2040 (~5-10€)
    - Microcontroller: RP204
- Nice!nano (~25€)
    - Microcontroller: nRF52840 (has bluetooth support)
- nRFMicro clone, named Supermini NRF52840 (~5€)
    - Microcontroller: nRF52840 (has bluetooth support)

[This github repo](https://github.com/joric/nrfmicro/wiki) has a well documented wiki on microcontrollers for keyboards and where to buy them.

*Note that the boards can be found in AliExpress for a cheaper price.
However, they are not so reliable and one can get a damaged/bad board*

Although the firmware will be discussed later, it is important to know that the 
nRF52840 cannot be controlled with the QMK firmware, because of a license incompatibility.
Therefore, if one wants to build a wireless keyboard, one must use the ZMK firmware 
(or other license-permissive alternatives to QMK).

Regarding the pinout layout, the important things to know are:
- **number of pins**, which determine the type of wiring required (direct vs matrix)
depending on the number of keys in the keyboard and if they are split or not.
*How does a microcontroller with 18 pins control more than 18 keys?*
see [this explanation](https://flatfootfox.com/ergogen-part3-pcbs/).
- **pin capabilities**. Some extra features, e.g. displays, require having pins
some specific capabilities. 

Note, that if using ergogen, a consideration is whether the board that one wants
to use can be imported in Ergogen, i.e. one needs its "footprint".
Ergogen already includes the footprint of some common boards.
For example, the footprint of the nice!nano is not included, but can be found in:

- [repo 1](https://github.com/ceoloide/ergogen-footprints/blob/main/mcu_nice_nano.js)
- [repo 2](https://github.com/Giraffasax/SpUnLy58/blob/main/Ergogen/Footprints/nice_nano.js)
- [repo 3](https://github.com/dohn-joh/alias/blob/main/ergogen/footprints/mcu_nice_nano.js)


## nRF52840 boards

As I mentioned previously, I want my keyboard to be wireless, so I will be using
the nRF52840 microcontroller.
In particular, I will use the SuperMini nRF52840 board because

> "SuperMini NRF52840: This is absolutely the best nRFMicro replacement by far, 
full featured, and costs only $3. I strongly recommend buying it."
-- from [joric/nrfmicro](https://github.com/joric/nrfmicro/wiki/Alternatives#supermini-nrf52840)

The options are considered are:
- [nice!nano](https://nicekeyboards.com/nice-nano/)
- [nRFMicro](https://github.com/joric/nrfmicro)
- [SuperMini nRF52840](https://github.com/joric/nrfmicro/wiki/ALternatives#supermini-nrf52840)

