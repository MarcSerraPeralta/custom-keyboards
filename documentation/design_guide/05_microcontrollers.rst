Microcontrollers
================

The computer needs to know when a key (i.e. switch) has been pressed. 
Keyboards are usually connected to the computers via USB or Bluethood, thus
this requires some type of processing of the signals from "triggered switches"
to valid USB or Bluetooth transmission. Such processing is done with 
microcontrollers. 

Microcontrollers can be programmed and are not usually very computationally
powerfull. As the processing is not very complex, microcontrollers are a great
choice because they do not require a lot of power to run (very important when
designing a wireless keyboard). There are lots of microcontrollers available,
however there are some common choices due to their characteristics (functionality, 
number of pins, size, ...) and support on keyboard firmare. 
The firmware is the (customizable) software that processes the signals. 
It is responsible for transmitting "A" instead of "a" when the "a" key is
pressed together with the "Shift" key. Apart from this example, there are 
other functionalities that the firmwares support. The only requirement is that
the firmware can compile the program for the microcontroller one wants to use.

All keyboards (I have seen) use a board with a microcontroller to control the
keyboard (not the microcontroller alone). This simplifies the PCB design.

They are generally either the "Pro Micro" board or compatible with it:

"The Pro Micro is an Arduino-compatible microcontroller board developed under 
an open hardware license by Sparkfun. Clones of the Pro Micro are often used 
as a lower-cost alternative to a Teensy 2.0 as a basis for a DIY keyboard 
controller/converter when a lower number of pins would suffice."
-- from https://deskthority.net/wiki/Arduino_Pro_Micro

Boards pin-compatible with the Pro Mictro have the same pinout layout.
However, keep the following in mind:

"Pin-compatible alternatives for the keyboard community may be longer for extra 
functionality, such as fitting a USB-C port (which is larger), more pins, buzzer 
(for "click") and/or circuitry for a Bluetooth transceiver. 
They will not fit all keyboard PCBs or cases."
-- from https://deskthority.net/wiki/Arduino_Pro_Micro

Although people may call these Pro-Micro-compatible boards "clones", I prefer
to use this term to denote a cheaper version of the original board trying to 
replicate all the functionality. 

The most important things in a board are the pinout layout and the microcontroller.
The microcontroller determines the available functionality, for example:
- The original Arduino Pro Micro board uses the ATmega32u4 microcontroller with allows
  for connection via a micro-USB type B.
- The nice!nano board uses the nRF52840 microcontroller which allows for both
  USB type-C and Bluetooth 5.

The most common microcontrollers are:
- Arduino Pro Micro (~5-10€)
- Pro Micro RP2040 (~5-10€)
- Nice!nano (~25€)
- nRFMicro clone, named Supermini NRF52840 (~5€)

The first two options differ on the microcontroller used (ATmega32u4 vs RP204).
The last two have the same nRF52840 microcontroller.
The first two differ from the bottom two because they do not have Bluetooth.
The last option has been recently released (as per 2024). 
Therefore, the usual option for a non-wireless keyboard is the (Arduino) Pro Micro,
while the "only-option" (until recently) for wireless keyboards was nice!nano.

Note that the boards can be found in AliExpress for a cheaper price.

Although this paragraph is related to the firmware, it is important to know
that the nice!nano cannot be controled with the QMK firmware. The reason is
that the company fabricating the nRF52840 microcontroller has licensed their
"SoftDevice" for Bluetooth Low Energy, which is not compatible with the GNU 
Public licence, making it license-incompatible with QMK. Therefore, if one
wants to build a wireless keyboard, one must use the ZMK firmware (or other
alternatives to QMK).

Regarding the pinout layout, it is important to know how many pins the
board has and what they are capable of. The number of pins and the number of
keys to be controlled by a single microcontroller will determine the type of
wiring required for the keyboard (direct vs matrix). For example, image
a keyboard with 34 keys and a 18 pins, how is the microcontroller able to
process more than 18 keys? We will see that in the next section.
Finally, displays require having pins with some specific capabilities. If one
wants to have a small display in the keyboard, they must make sure that the
microcontroller can control it.


Characteristics of the most common boards
-----------------------------------------

**Arduino Pro Micro**
"The Pro Micro is an Arduino-compatible microcontroller board developed under 
an open hardware license by Sparkfun. Clones of the Pro Micro are often used 
as a lower-cost alternative to a Teensy 2.0 as a basis for a DIY keyboard 
controller/converter when a lower number of pins would suffice."
-- from https://deskthority.net/wiki/Arduino_Pro_Micro

**nice!nano**
"The nice!nano is a microcontroller board with Bluetooth and USB, pin-compatible 
with a 3.3V Pro Micro. It uses the nRF52840 microcontroller from Nordic Semiconductor."
-- from https://deskthority.net/wiki/Nice!nano

**Pro Micro RP4020**
"SparkFun Pro Micro - RP2040 is a microcontroller board in Pro Micro pinout 
with the Raspberry Pi RP2040 microcontroller. It has a USB-C connector, 16 MB 
external Flash memory and a Qwiic connector for I²C."
-- from https://deskthority.net/wiki/Pro_Micro_RP2040

**nRFMicro**
"The nRFMicro is a controller board with Bluetooth Low Energy, which is 
pin-compatible with 3.3V Pro Micro. Unlike some other boards with Bluetooth, 
it has the same small size as a regular Pro Micro. It is based on the nRF52840 
transciever/microcontroller module from CDEBYTE, running an ARM Cortex-M4F MCU.
Has a built-in LiPo charger and a physical on/off switch on board."
-- from https://deskthority.net/wiki/NRFMicro

"Welcome to the nRFMicro wiki!
This is a DIY drop-in Pro Micro controller replacement for converting wired 
Pro Micro-based keyboards to true wireless."
-- from https://github.com/joric/nrfmicro/wiki/

**SuperMini NRF52840**
A comment from the creator of the nRFMicro:
"SuperMini NRF52840: This is absolutely the best nRFMicro replacement by far, 
full featured, and costs only $3. I strongly recommend buying it."
-- from https://github.com/joric/nrfmicro/wiki/Alternatives#supermini-nrf52840

"SuperMini NRF52840 is a Pro Micro alternative development board that is 
compatible with Nice! Nano. Its pins are the same as ProMicro, which means it 
can be used with almost any ProMicro keyboard. The NRF5280 development board has 
a 3.7V lithium battery interface and a software switch that can cut off the 
power of the LED. When turned off, the standby power consumption can reach 1mA."
-- from https://github.com/joric/nrfmicro/wiki/Alternatives#supermini-nrf52840

"(SuperMini) nRF52840 is a high-performance, low-power wireless SoC chip launched by Norwegian 
Nordic Semiconductor. It supports multiple wireless protocols, including Bluetooth 5, 
Thread, Zigbee, ANT, and 2.4GHz. The nRF52840 chip uses an ARM Cortex-M4F processor,
clocked at 64MHz, with built-in 1MB of flash memory and 256KB of RAM. It also has 
a variety of peripherals, including ADC, PWM, SPI, I2C, UART, USB and GPIO, etc.
In addition, nRF52840 also supports a variety of security functions, such as 
AES encryption, SHA-256 hashing and True Random Number Generator (TRNG)."
-- from https://wiki.icbbuy.com/doku.php?id=developmentboard:nrf52840


Pro micro vs NiceNano
---------------------
Comparison from https://www.reddit.com/r/ErgoMechKeyboards/comments/sluweg/pro_micro_vs_nce_nano/:

**Nice!Nano**
- Requires the use of ZMK (firmware) - as some others here already mentioned
    - Slightly higher learning curve, but for what it's worth, I prefer it once I got the hang of working with it
    - Is missing some of the advanced functionality in QMK and does not have the option of the more user-friendly VIA (or VIAL)
- Allows full wireless!
    - I love not having cables, and I don't want to go back
    - Does require that you also fuss about with adding a battery
- Ergogen does not have a footprint for Nice!Nano

Comment: these footprints are used by Ergogen to know the size and characteristics 
of the microcontroller board in order to generate the PCB files. 
Although it does not have a footprint for the Nice!nano, there
are available footprints around GitHub.
https://github.com/ceoloide/ergogen-footprints/blob/main/mcu_nice_nano.js
https://github.com/Giraffasax/SpUnLy58/blob/main/Ergogen/Footprints/nice_nano.js
https://github.com/dohn-joh/alias/blob/main/ergogen/footprints/mcu_nice_nano.js

**Elite-C / pro-micro**
- Uses QMK / VIA (firmware)
    - More common and more richly featured
    - VIA is definitely the most approachable for a newbie to remap keys
- Cheaper
    - Especially true for the pro-micro
- Requires wires to connect the board halves and to the computer
- Ergogen has a footprint for pro-micro
