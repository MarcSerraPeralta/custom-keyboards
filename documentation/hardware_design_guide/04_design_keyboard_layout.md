# Keyboard layout

The layout of the keyboard defines where the keys are positioned.
As we have assumed to focus on flat keyboards, each key will have a
$(x,y)$ coordinate associated with it.

We also need to know how many keys the keyboard is going to have. 
In my case, I will design a **34-key** layout.

The following video is a good way to start designing a layout:

[“The REAL Ergonomic Keyboard Endgame!” - How To Design & Make A Totally Custom Keyboard, by Ben Vallack](https://www.youtube.com/watch?v=UKfeJrRIcxw)

The approach involves: 
1. using ergopad, 
1. using pen and paper, 
1. digitising the layout, 
1. print and final test.

The output is the $(x, y)$ coordinates for all keys in the keyboard.

These coordinates values will be used by Ergogen (a software for designing keyboards) to output the files required to 
manufacter a PCB for the keyboard.

*Pictures and files about my process can be found in ``my_keyboard/`` directory.*



## 1. Using Ergopad and a tablet

[Ergopad](https://pashutk.com/ergopad/) is a useful website that allows to 
determine the best placement of the keys by simply tapping on a tablet. 

**Notes**: 
- I found that I need to rest my hand on the tablet when tapping it
in order put the hand in the most confortable position (and thus the one I
should be using for the keyboard). 


## 2. Using pen and paper

I designed my custom keyboard layout with a pen and paper following
a little bit the way Ergopad works. 

**Notes**:
- I drew it for only my right hand because I am going to mirror it for the left one. 
- Remember that one should put the hand in the same position that they are going to
use when typing (e.g. with wrist support) when testing the custom keyboard layout.
- Take into account the size of the keycaps.


## 3. Digitising the layout

I digitised the layout that I drew with pen on paper using Inkscape and a picture. 
This process allows to draw the exact size of the keycaps and also flip/mirror
the keyboard to get the other hand. 

**Notes**:
- Usually a 0.5mm separation is placed between keys to avoid them touching each
  other. For example, the size of the Choc MBK keycaps is 17.5x16.5mm,
  but the spacing is set up by default to be 18x17mm.


## 4. Testing

Once finished, I printed it to test again that the layout works for me but now
for both hands. 
