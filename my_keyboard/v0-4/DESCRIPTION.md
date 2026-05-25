# Description of my custom keyboard

### Choices

- **number of keys** = 34 
    - ergonomics for the fingers (all keys at one key distance from home row)
- **wiring** = direct
    - allowed by number of keys and being split (microcontroller has ?? GPIO pins)
    - simple design and does not require diodes
    - supported by ZMK (firmware)
- **keyboard board** = PCB
    - easier than hand wiring
    - "easily" designed with Ergogen
    - "cheap" when printed by [JLCPCB](https://jlcpcb.com/)
- **wireless** = yes
    - no cables on the table
- **microcontroller** = [SuperMini nRF52840](https://github.com/joric/nrfmicro/wiki/ALternatives#supermini-nrf52840)
    - cheapest option with Bluetooth (for wireless)
- **firmware** = [ZMK](https://zmk.dev/)
    - required for nRF52840 microprocessors
    - allows for [direct wiring](https://zmk.dev/docs/development/hardware-integration): `compatible = "zmk,kscan-gpio-direct"`
    - allows for [homerow modifiers](ihttps://zmk.dev/docs/keymaps/behaviors/hold-tap?utm_source=chatgpt.com&examples=home_row_mods): `zmk,behavior-hold-tap`
    - allows for [layers](https://zmk.dev/docs/keymaps/behaviors/layers)
- **batteries** = yes, [301230 110mAh Lithium battery](https://github.com/joric/nrfmicro/wiki/Batteries#301230) 
    - power for minimum several weeks ([battery life estimator](https://zmk.dev/power-profiler))
    - thin enough (3mm) to be stored below the microcontroller + 3.5mm sockets
- **sockets** = [Dupont-style 3.5 mm tall PBS female headers, 12 pins](https://github.com/joric/nrfmicro/wiki/Sockets)
    - high enough so that the battery can fit inside
    - PBS cover the pins with plastic so that they are not exposed
    - microcontroller has 13 pins on each side, top ones are for the battery
- **switches** = [low-profile kailh choc v1](https://splitkb.com/products/kailh-low-profile-choc-switches)
    - less key travel
- **keycaps** = [MBK low-profile choc v1](https://splitkb.com/products/blank-mbk-choc-low-profile-keycaps?_pos=1&_sid=6599251e8&_ss=r&variant=31811487039565)
    - thinner keyboard
- **hotswappable** = yes, [kailh choc hotswap socket](https://splitkb.com/products/kailh-hotswap-sockets?variant=39472161456205)
    - for reusability of keys
- **split** = yes
    - ergonomics for the shoulders
- **display** = no
    - longer battery life
- **RGB** = no
    - longer battery life
- **keyboard layout** = QWERTY
    - I am used to and it is what all keyboards have
- **keymap** = layers + home-row mods 
    - for fitting everything in 34 keys
    - supported by ZMK (firmware)
- **case** = yes
    - more durability
    - 3D printed


### Estimated Price (without shipping)

- 34 switches (splitkb.com) = 1€ * 34 = 34€ 
- 34 keycaps (packages of 10, splitkb.com) = 4 * 4€ = 16€
- 34 hotswap sockets (packages of 50, splitkb.com) = 8€
- 2 SuperMini NRF52840 (AliExpress) = 2 * 5€ = 10€
- 2 lithium batteries (AliExpress) = ~5-10€
- 2 PCBs (minimum order of 5, JLCPCB) = ~12€
- 2 cases (own 3D printer, 200g of plastic) = ~5€
- 2 reset and power buttons (AliExpress) = 2€ + 1€ = 3€

**TOTAL** = ~95€


## THINGS TO STILL THINK ABOUT

- How to hold the battery in place below the microcontroller? https://www.youtube.com/watch?v=CsANtp6a3YU&t=166s
- Reset button (how to wire it)
- Power button (how to wire it)
- Wiring (add picture)
