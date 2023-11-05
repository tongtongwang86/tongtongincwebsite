---
layout: post
title: Revolute System
date: 2023-11-05 21:59 +0800
categories: [Revolute]
---


## Circuitry

2 Pcb total: one in the wheel, one as usb interface, 

Circuit board in wheel houses the as5600 magnetic angle sensor ic, and connects to the usb board (main board with Microcontroller and additional Circuitry) Through i2c. The main board is then connected to a computer using the USB contacts.

The wire that connects the wheel to the USB plug is composed of For smaller wires, insulated with an enamel coating. Two wires connect power and ground from USB to Wheel, The other two Connect the i2c data lines: SDA and SCL.

The USB board does not have an Wireless antenna, This version of Revolute cannot be used wirelessly Without significant modifications.

## Enclosure

Parts are designed to be 3-D printed
3 3D-printed parts Total : Wheel cap, Wheel base And USB enclosure

Revolute v2.2 Has slots on the perimeter of the wheel for 30 magnets, which provide a snapping, incremental feel. Revolute V2 does not The slots and these magnets giving it A smooth, gliding feel, but it does not allow for precise incrementation, This version is easier to 3d print Compared to v2.2.

a ball bearing Is placed between The wheel cap And the wheel base For Smoother operation, and better structural rigidity

The wheelbase Is designed to be an MX switch compatible key cap, allowing you to easily secure revolute on to any Key on a mechanical keyboard.

Magnetic field of poled magnet placed within the freely rotating wheel cap is sensed by the Magnetic angle sensor.

USB Enclosure ensures that components, do not short circuit in the USB port during regular use. it is placed on the backside of the USB circuit board.

