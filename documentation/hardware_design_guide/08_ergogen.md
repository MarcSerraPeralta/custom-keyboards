# Ergogen

Ergogen is an npm package but can be run online in the following websites:
- [Ergogen ceoloide](https://ergogen.ceoloide.com/)
- [Ergogen cache](https://ergogen.cache.works/)

I recommend the first one as it includes several useful **footprints**,
which correspond to the schematics (both physically and wiring) of hardware parts.
For example, [Ergogen ceoloide github](https://github.com/ceoloide/ergogen-footprints) has the footprints
for the:
- nice!nano, 
- supermini (nice!nano clone), 
- reset switch...


### Custom Footprints

To use custom footprints, one must install ergogen locally, which can be done
using: 
```
npm i -g ergogen
```

Create a directory called ``footprints`` and place the footprints inside.

Important:
> "When working with external footprints, it's required that you use the filename 
config.yaml for your Ergogen config. Secondly, we need to change how we call Ergogen. 
Instead of the usual ergogen config.yaml command, we need to pass our entire folder to Ergogen.
Without further ado, let's fire up Ergogen and provide it with our project folder: `ergogen .`" 
from [flatfootfox](https://flatfootfox.com/ergogen-part4-footprints-cases/)


### Ergogen tutorial

I recommend first looking into [this example guide](https://flatfootfox.com/ergogen-introduction/)
and once the general structure of ergogen is known, then look into the
[official Ergogen documentation](https://docs.ergogen.xyz/).

For a general vibe, I also recommend watching [Ben Vallack's videos](https://www.youtube.com/watch?v=UKfeJrRIcxw).

Also, in my designs, I first started with the Ergogne basics, e.g. keyboard layout,
and then moved into more complex stuff, e.g. wiring microcontroller.
The different versions go in increasing complexity.


### Assigning pins to keys

Consiously assign microcontroller's pins to keys to avoid having traces (wires) in the PCB overlapping
each other.
