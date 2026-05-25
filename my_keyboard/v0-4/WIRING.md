# Wiring

ADD HERE PICTURE FOR WIRING

### Rest button

**Reset button must connect the RST and GND pins.**

Both the Supermini nRF52840 and the nice!nano can be set to "bootloader mode" by
quictly shorting the RST and GND pins twice.

[Supermini nRF52840 Aliexpress documentation](https://nl.aliexpress.com/item/1005006035267231.html?gatewayAdapt=usa2nld#nav-specification) states:
> If you want to enter Bootloder, please short RST to GND twice within 0.5S. 
Enter Bootloder, connect to the computer via USB, and a storage device called Nice!Nano will be displayed. 
At this point you can drag in the .uf2 file to burn the program.

[nince!nano official documentation](https://nicekeyboards.com/docs/nice-nano/getting-started/#flashing-firmware-and-bootloaders) states:
> To jump into the bootloader all you need to do is double tap reset. 
You can do this by either double tapping your reset button on your keyboard, 
or you can double tap RST and GND pins on the nice!nano quickly with tweezers.


### Power switch

**Power switch must connect the B+ pin of the microcontroller and the positive 
wire of the battery**


### Supermini nRF52840 board

Write down the pins that can be used for controlling the keys.
Order them so that the routing to the keys is easier.
Write down any special pins that need to be wired in some specific way.

