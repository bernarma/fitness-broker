# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

To run tests: python -m unittest test.test_main

To run main program: python -m iot_processor.main -c iot.config


Before running the test - start mosquitto (assume it's localhost 1883)

Ubuntu: install "mosquitto" package


Generate protobuf files:

C:\Develop\protoc-3.11.4-win64\bin\protoc.exe --proto_path .\iot_processor\messages -I C:\Develop\mtns_iot iot_processor\messages\*.proto  --python_out=iot_processor\messages

JS framework for Web 3D: https://www.babylonjs.com/