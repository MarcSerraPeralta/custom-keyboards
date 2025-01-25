Designing a custom keyboard layout
==================================

Now that we have a little bit of more knowledge about keyboard and
switch sizes, we can start by designing the custom keyboard layout.

The layout of the keyboard defines where the keys are positioned.
As we have assumed to focus on flat keyboards, each key will have a
:math:`(x,y)` coordinate associated with it.

What is a good way to start designing a custom keyboard layout?

https://www.youtube.com/watch?v=UKfeJrRIcxw

The approach involves: 
(1) using ergopad, 
(2) using pen and paper, 
(3) digitising the layout, 
(4) print and final test.
Pictures and files about the process can be found in ``my_keyboard`` folder.

At the end of this section, you should have a custom keyboard layout with the
:math:`(x,y)` positions of each key. These coordinates values will be used by
Ergogen (a software for designing keyboards) to output the files required to 
manufacter a PCB for the keyboard.


1. Using Ergopad and a tablet
-----------------------------

Ergopad (https://pashutk.com/ergopad/) is a useful website that allows to 
determine the best placement of the keys by simply tapping on a tablet. 

Neverthless, I found that I need to rest my hand on the tablet when tapping it
in order put the hand in the most confortable position (and thus the one I
should be using for the keyboard). 

However, it is useful to see more or less how the keyboard should look like. 


2. Using pen and paper
----------------------

In the end, I designed my custom keyboard layout with a pen and paper following
a little bit the way Ergopad works. I drew it for only my right hand because
I am going to mirror it for the left one. 

It took me several iterations until I found a draft layout that worked quite well. 
Remember that one should put the hand in the same position that they are going to
use when typing (e.g. with wrist support) when testing the custom keyboard layout.
Also take into account the size of the keycaps.


3. Digitising the layout
------------------------

I digitised the layout that I drew with pen on paper using Inkscape. 
This process allows to draw the exact size of the keycaps and also flip/mirror
the keyboard to get the other hand. 
Notes:
- one is not limited to having the same layout for both the left and
right hands in a split keyboard. 
- usually a 0.5mm separation is placed between keys to avoid them touching each
  other. For example, the size of the Choc MBK keycaps is 17.5x16.5mm,
  but the spacing is set up by default to be 18x17mm.


4. Testing
----------

Once finished, I printed it to test again that the layout works for me but now
for both hands. 
