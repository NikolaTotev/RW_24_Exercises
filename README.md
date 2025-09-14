# RW_24_Exercises
<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.eu.png" width="88" height="31" alt="by-nc-sa"/>
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/NikolaTotev/RW_24_Exercises">MiniBot Robot Course Exercises</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/NikolaTotev">Nikola Totev</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>


# Instructions

## How to setup flutter
The best way to setup flutter and run the app is by following the official instructions https://docs.flutter.dev/get-started/install

## Setup micropython
To get stared with micropython follow the link here https://projects.raspberrypi.org/en/projects/get-started-pico-w/1

## Sometimes needed - clearing the flash on your pico
Follow these instructions
https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#resetting-flash-memory

# Running Code on the Pi pico

From VS Code, with the pico connected, at the bottom right of your screen there should be a "Run" button from the micropico extension. 

This will run the python file currently focused. 

If you wish to upload the file to run it without the Pico being connected to the computer

```
Ctrl+Shift+P
MicroPico: Upload file to board
```
This will upload the focused file to the board. 

# Connecting to the pico 
When you're ready to connect via wifi, on your phone or computer, find the wireless network creted by the Pico, by default the SSID and Password are:

```
ssid = "MiniBot_AP_6"
password="MiniBot4224"
```
Once you've connected to the network, you can open the Flutter app and start controlling your robot!




