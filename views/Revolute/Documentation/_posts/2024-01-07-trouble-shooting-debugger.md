---
layout: post
title: trouble-shooting-debugger
date: 2024-01-07 20:12 +0800
categories: [RevoluteWireless]
---

## Testing Debugger Power circuitry

**While connected to uart and plugged into computer**, test for 3V, Probe according to the following picture shown below:

Set multimeter to voltage mode: ![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/multimetervoltagemode.JPG){: width="972" height="589" .w-75 .normal} 

Using the pins probe the pads:

![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/test3v.png){: width="972" height="589" .w-75 .normal} 

if it reads 3v then good, if not check soldering around the 3V regulator and uart connection to computer:

![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/3vregulatordebugger.png){: width="972" height="589" .w-75 .normal} 

Using the same multimeter setting as before,Probe the following pads. If voltage reads 5V then its good. Else, check soldering of uart jumper wires, or uart connection to computer:

![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/test5v.png){: width="972" height="589" .w-75 .normal} 



## Testing Debugger Pin Connection