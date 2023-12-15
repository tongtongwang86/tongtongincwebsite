---
layout: post
title: Revolute Build Guide
date: 2023-11-05 22:07 +0800
categories: [Revolute, Tutorial]
---

Revolute is composed of 2 main parts: The wheel module and the usb connector, and is connected via wire

There are two variations of revolute wheel: V2.0 and V2.1, 2.1 has a ring of magnets to simulate idents for applications where individual clicks are preferred, 2.0 does not have the ring of magnets which makes it easier to make and is better for smooth, linear situations. Build process for these two models are similar.

## Prerequisites

### Tools you will need:
- Soldering iron
- Hot air gun or Hot plate
- multimeter for testing 
- jlink or black magic probe for flashing bootloader
- 3d printer/ or online service to print the 3d models
- pcb manufacturer online service to manufacture pcbs

### Bill of materials

------ **Revolute Wheel Assembly** ------
  + [ ] <a href = "https://github.com/tongtongwang86/Revolute/blob/292de90ef90795bcd5d16035f8713dd0b1a0cff2/Misc/Pictures/Scrollwheel.JPG"> MR0017 Scroll wheel </a>
  + [ ] Wheel cap <a href = "https://github.com/tongtongwang86/Revolute/blob/main/3D%20Prints/V2.1/Cap.stl"> V2.1</a> <a href = "https://github.com/tongtongwang86/Revolute/blob/main/3D%20Prints/V2/Cap.stl"> V2.0</a> (3d printed)
  + [ ] Wheel base <a href = "https://github.com/tongtongwang86/Revolute/blob/main/3D%20Prints/V2.1/Base.stl"> V2.1</a> <a href = "https://github.com/tongtongwang86/Revolute/blob/main/3D%20Prints/V2/Base.stl"> V2.0</a> (3d printed)
  + [ ] <a href = "https://magnet.com.au/products/neodymium-disc-6mm-x-2mm-diametric-n35">  6mm dia x 2mm Diametrically Magnetised neodymium magnet</a> 
  + [ ] 36 x <a href = "https://www.first4magnets.com/us/circular-disc-rod-c34/n42-neodymium-disc-magnet-1mm-dia-x-1mm-thick-0-05lbs-pull-p2675#ps_0_2701|ps_1_494">  diameter 1mm height 1mm neodymium magnet </a> (V2.1 only)
  + [ ] 12 x <a href = "https://www.amazon.nl/-/en/N42-Neodymium-Magnet-Diameter-Pulling/dp/B00TACMMYG">  diameter 1mm height 2mm neodymium magnet </a> (V2.1 only)
  + [ ] <a href = "https://github.com/tongtongwang86/Revolute/blob/main/Hardware/TopPCB/Gerber.zip">  Wheel PCB </a> (order from pcb manufacturer)
    + [ ] 0402 4.7K resistor
    + [ ] 0402 1uF capacitor
    + [ ] 0402 100nF capacitor
    + [ ] <a href = "https://ams.com/en/as5600">  AMS as5600 magnetic encoder </a>

> 6mm dia x 2mm magnet must be Diametrically Magnetized, or else the scrolll wheel will not work. <a href = "https://www.stanfordmagnets.com/what-is-the-magnetization-direction-for-permanent-magnets.html">  Whats the difference? </a> 
{: .prompt-warning }

------ **Revolute USB connector Assembly**  ------
  + [ ] <a href = "https://www.amazon.com/WDONGX-Enameled-Headphone-Ultra-Soft-Insulated/dp/B097GZRTSW?th=1">  4 core enamel wire 1.4mm diameter </a> 
  + [ ] <a href = "https://github.com/tongtongwang86/Revolute/blob/main/3D%20Prints/V2.1/pcbtray.stl">  PCB tray (3d printed) </a> 
  + [ ] <a href = "https://github.com/tongtongwang86/Revolute/blob/main/Hardware/MainPCB/Gerber.zip">  Connector PCB </a>(order from pcb manufacturer)
    + [ ] 0402 12pF capacitor
    + [ ] 0402 100nF capacitor
    + [ ] 0402 1uF capacitor
    + [ ] 0402 4.7uF capacitor
    + [ ] 0402 0.8pF capacitor
    + [ ] 0402 820pF capacitor
    + [ ] 0402 47nF capacitor
    + [ ] 0402 100pF capacitor
    + [ ] 0402 1.5k resistor
    + [ ] 0402 10uH inductor
    + [ ] 0402 15nH inductor
    + [ ] 0603 blue led 
    + [ ] nRF52840_aQFN73
    + [ ] AP2112K-3.3 SOT-23-5
    + [ ] <a href = "https://www.alibaba.com/product-detail/3225-SMD-4-Pin-32-000MHz_60438220481.html">  32MHZ 3225 (3.2*2.5mm) </a>
    + [ ] <a href = "https://www.golledge.com/products/gwx-2012-highly-competitive-2012-package-32.768khz-watch-crystal/c-26/p-762">  32.768 kHz 2012 (2.0*1.2mm) </a>

## Assembling the PCBs

> PCB was designed in KiCad, Which is free and open-source. Ibom was generated using the ibom plugin for KiCad.
{: .prompt-info }

Send out PCBs to manufacturing firm, I personally use JLCPCB. The Wheel PCB is a 2 layered PCB that is 1mm thick, The Connector PCB is 4 layered 1mm thick. There are no requirements for impedance control as.

Assemble PCBs according to interactive bom files:
  - <a href = "https://tongtonginc.com/bom/WheelPCB.html">  Wheel PCB </a>
  - <a href = "https://tongtonginc.com/bom/ConnectorPCB.html">  Connector PCB </a>

> - Soldering process would be easier if stencil and hotplate were used
- Soldering iron cannot practically be used to solder chips with buried pins such as nRF52840
- Make sure polarity of the led is correct, the arrow should be pointing to ground.
- Flux should be used to aid the soldering process, to clean off the excess flux, you can use Isopropyl alcohol and a scrubber.
{: .prompt-tip }
 
## Testing the PCBs

look closely at the pcbs to spot any visible mistakes.

On the connector pcb:

using a multimeter, you can use diode mode to test for gpio pin connection as there are internal protection diodes connected to the gpio pins.
  - place positive probe onto any ground pad 
  - place negative probe onto gpio pin to test
  - all readings should be about the same, if not then theres an issue with the connection.

> Test using diode mode before soldering the wire onto the pcb.
{: .prompt-warning }

> Do not power the system on before you are 100% certain that everything is correct.
{: .prompt-danger }

## Connecting the PCBs


![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/pinout.png){: width="972" height="589" .w-75 .normal} 

Following the pinout diagram above, connect the two boards using the  <a href = "https://www.amazon.com/WDONGX-Enameled-Headphone-Ultra-Soft-Insulated/dp/B097GZRTSW?th=1">  4 core enamel wire </a> 


> to remove the insulative enamel coating, use an soldering iron to tin the end, the coating should burn off. Using the color of the wire connect the right pins to each other, 4 pins on the bottom of the connector pcb directly correlates to the 4 pins on the wheel pcb
{: .prompt-tip }

> Remove just enough coating to create a connection, removing too much will result in short circuits.
{: .prompt-warning }

## Final Assembly 
![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/isoassembly.png){: width="972" height="589" }



- Assemble accoring to this diagram:
    1. Base 3D print
    2. Cap 3D print
    3. V2.1 Ident magnets base
    5. Cap pcb with encoder chip
    6. Diametrically Magnetized magnet
    7. V2.1 Ident magnets cap
    8. Ball bearing
    9. Rubber ring
    10. Wire 

