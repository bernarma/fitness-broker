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

Create SystemD Service (Python)
https://github.com/torfsen/python-systemd-tutorial


Install mosquitto on Raspberry PI
---
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto.service
=======
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


Allow RemoteSigned Scripts - PS1
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

For now this is not needed - NodeGyp (possibly need when creating website/dashboard)
https://github.com/nodejs/node-gyp#on-windows

See for permissions to access ANT+ USB and project to use GPIO in RPI+
https://www.instructables.com/id/Using-Zwift-With-Nearly-Any-Fitness-Device/

In JS Client - to generate PBJS files - .\node_modules\.bin\pbjs

TODO
===
* Test Tacx Ant+ USB
* Fork PyAnt with changes to support Python 3
* Add protobuf implementation into VueJS: https://github.com/fengxianqi/front_end-demos/tree/master/src/vue-protobuf

