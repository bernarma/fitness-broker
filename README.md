# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

To run tests: python -m unittest test.test_main

To run main program: python -m iot_processor.main -c iot.config


Before running the test - start mosquitto (assume it's localhost 1883)

Ubuntu: install "mosquitto" package

TODO
---
** Create systemd Service **
** Create Web Application based on Vue.js to listen to the MQTT Websocket **
** Add protobuf commands to start and shutdown the processing loop **
** Add configuration file for mosquitto to listen for MQTT and websocket traffic **
** Implement BTLE and ANT+ (support for HRM, Cadence, Speed, Power, ANT-FEC, FTMS) **


Generate protobuf files:

C:\Develop\protoc-3.11.4-win64\bin\protoc.exe --proto_path .\iot_processor\messages -I C:\Develop\mtns_iot iot_processor\messages\*.proto  --python_out=iot_processor\messages

JS framework for Web 3D: https://www.babylonjs.com/

Installing Module on RaspberyPi
---
pip3 -m venv .env

sudo apt-get install libbluetooth-dev
sudo apt-get install python-dev
pip install PyBluez


Bluetooth GATT Services Website
---
https://www.bluetooth.com/specifications/gatt/services/

Gattlib - Python Module/Library
- pip install wheel
- sudo apt-get install libboost-python-dev

ANT+
- TBD

Mosquitto on Raspberry PI
- https://theembeddedlab.com/tutorials/install-mosquitto-on-a-raspberry-pi/


TODO
===
* Test Tacx Ant+ USB
