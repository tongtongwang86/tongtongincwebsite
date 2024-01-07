---
layout: post
title: Flashing Revolute wireless Debugger
date: 2024-01-07 09:05 +0800
categories: [RevoluteWireless]
---

in order to flash the bootloader into revolute wireless, we need to use the debugger. In this post, we will be flashing the black magic probe bootloader and firmware onto the debugger so that we can use it to flash the revolute wireless.

Materials you need: 
- Soldered revolute debugger board
- CP2102 UART to TTL module
- Jumper wires
- Soldering iron

Downloads: 
- <a href="https://github.com/joric/bluetosis/releases/download/0.0.2/blackmagic_dfu.bin">blackmagic_dfu.bin</a> (Blackmagic DFU bootloader)
- <a href="https://github.com/joric/bluetosis/releases/download/0.0.2/blackmagic.bin">blackmagic.bin</a> (Blackmagic firmware 1.6.1, stripped down for 64k)
- <a href="https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm">GNU Arm Embedded Toolchain</a> (arm-none-eabi-gdb, use 8-2018-q4 for blackmagic 1.6.1)
- <a href="https://www.st.com/en/development-tools/flasher-stm32.html">STM32 Flash loader demonstrator</a> (official STM32 flasher)c
- <a href="https://zadig.akeo.ie/">Zadig</a> (USB drivers)

Step1: Set Debugger to bootloader mode (BOOT0 jumper=1, BOOT1 jumper=0), Short the pins as shown in the diagram below



![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/debuggerbootloadermodepin.png){: width="972" height="589" .w-75 .normal} 

Step2: Connect each pin: RX, TX, GND, 5V  From UART module to debugger board.



![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/DebuggerConectPin.png){: width="972" height="589" .w-75 .normal} 

![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/UartAdapter.jpg){: width="972" height="589" .w-75 .normal} 



Step3: Plug in UART adapter to the computer. Run "STM32 Flash loader demonstrator".

Step4: Download to device `blackmagic_dfu.bin` at offset `0x8000000` with "Global Erase" option.

Step5: Download to device `blackmagic.bin` at offset `0x8002000` with "Erase necessary pages" option.

Step6: Put Bluepill jumpers back to the operational mode (BOOT0 jumper=0, BOOT1 jumper=0).


![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/functionalmodepindiagram.png){: width="972" height="589" .w-75 .normal} 


Step7: Remove UART adapter, plug in Bluepill to the computer via its own onboard USB.

Step8: Update USB drivers with libusb-win32 from "Zadig" (Options - List All Devices).

> Make sure you got both "Black Magic GDB server" and "Black Magic UART port", you need GDB port (e.g. COM9).
{: .prompt-warning }

![Desktop View](https://tongtonginc.com/images/Revolute/Documentation/debugger/comports.png){: width="972" height="589" .w-75 .normal} 