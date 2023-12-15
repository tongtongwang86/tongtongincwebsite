---
layout: post
title: Design Choices
date: 2023-11-08 21:32 +0800
categories: [Revolute]
---

## Contactless angle sensing

{how does the magnetic encoder work and how is it different from a normal encoder????}

{will the switches u have on ur kb with the magnetic sensors get afffected by the magnet on the sw???}

Compared to traditional rotary encoders (found within most computer mice), magnetic Potentiometer offers a greater degree of precision, while also Exhibiting the traits of high durability

Traditional encoders work by scraping metal brushes onto a disk, or shining light through a marked disk, neither of which are as reliable. 

Physical contact within metal brushes may fail due to dust/liquid getting into the compartment, corrosion of metal, deformation of the brushes, all of which stop brushes from getting in contact with the plate, which may result in the encoder skipping steps, false activation, which may render it completely useless.

Although having a longer life time than their contact counterparts, Encoders that use light also has a limited lifespan and limited resolution. As they all use similar encoding disks, resolution depends on how small they make each increment, usually more than 10 degrees. Dirt and grime may enter the encoding disk, clogging up holes that the light shines through, and the light/laser diodes used will eventually fail or reduce in brightness. the entire assembly is costly to replace as there is a number of components involved.

However Magnetic Potentiometer solve most of the problems mentioned above. They work by measuring the magnetic field of a horizontally polled magnet using multiple hall effect sensors. this is an analog solution and in a theoretical world, would offer infinite resolution. The AS5600 used in revolute offers up to 1° accuracy, using 4 hall effect sensors, converting the analog input into digital in the form of I2c. The downsides of magnetic Potentiometers is that it could be susceptible to magnetic noise in the surrounding, this will unlikely impact daily use as the strength of magnet is inversely proportional to its distance, meaning that as the magnet gets closer, magnetic strength will increase in the order of magnitudes. no ordinary magnet at a decent distance would have a stronger magnetic field than the one placed directly on top of the sensor, and would have negligible impact on the sensors reading.

![[as5600 magnetic.png]]


{Where does the wire of Revolute go if the thing is on my kb? wouldn’t it affect my typing?????}

the wire of the revolute goes between the space between the keycaps, preferably across the gaps of the row direction so it doesnt have to go through the zig zags of the columns. And no, it would not affect the typing of other keys if it is mounted correctly in the gaps of the keyboard.

{Since ur such a huge fan of the USB-C, why the USB-A and not a USB-C ?????}

we are using a usb a port because the original objective of the design was to make as many of the necessary electrical components and circuitry on the plug for the minimalistic design, and since the usba port is relatively larger in size it has made easier to develop off of. However, we are currently planning to make a version including the feature of the usbc port which we wish you to look forward to!

{Can Revolute work on my ipad or iphone????}

Yes, the revolute does function when connected to a mobile device such as an iphone and the ipad. The revolute would be recognized as a keyboard accordingly to the firmware we are developing the revolute from which would make it highly compatible to a variety of devices. However, you may need a dongle for that connection if the mobile device does not include a usba port

{if the wheel is so big would i still be able to use the original function of the keyswitch like pressing it down? wouldn’t it press the other keys as well??????}

Yes, it does not affect the use of the original key switch of the keyboard and it does not interfere with the function of other keys, meaning you can still use your keyboard for the purpose of typing.




more questions to be answered: 

{can u have functions assigned to different softwares applications without having to reconfigure them everytime u switch to another app so that you can play fortnite and then go to blender without having to change anythin ?????????? }

{Since ur such a huge fan of the USB-C, why the USB-A and not a USB-C ?????}

{Where does the wire of Revolute go if the thing is on my kb? wouldn't it affect my typing?????}

{if the wheel is so big would i still be able to use the original function of the keyswitch like pressing it down? wouldn't it press the other keys as well??????}

{How fast does it respond? i dont want it skipping steps while playing fn????}

{Can Revolute work on my ipad or iphone????}

{what color choices do i have???}

{is it water proof???}

{can u make it wireless}

{why does the wheel have to be sobig}

{wtf does it do}

{why a scroll wheel and not some kind of touch pad that would reach quicker}

{how do u configure its functions to different apps}

{can you make it connect and function the same accross different devices at the same time?? (2 host to one revolute) }

{how can i make my own software for revolute}

{how to setup development environment for revolute}

{how do i upload code to the revolute}

{can i make my own and how do i make my own}

