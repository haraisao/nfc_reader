# nfc_reader
Simple NFC reader 

## Requirements:
- Raspberry Pi 3B(Raspberry Pi OS)
- NFC Card Reader(Sony RC-S-380)

## Quick Start on RaspiOS:
- Install python3
    - sudo apt install python3
- Install python3-pip
    - sudo apt install python3-pip
- Install nfcpy
    - sudo pip3 install nfcpy

- Setting nfcpy
    - sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
    - sudo udevadm control -R
    - sudo reboot

 - Run nfc_reader.py
    - python3 scripts/nfc_reader.py

## Document(in Japanese)
- http://hara-jp.com/_default/ja/Topics/RaspPiCardReader.html
- 
