from iot_processor.ant.core import driver, node

stick = driver.USB2Driver(None, debug=True)
antnode = node.Node(stick)
antnode.start()
capabilities = antnode.getCapabilities()
antnode.stop()

print ('Maximum channels:', capabilities[0])
print ('Maximum network keys:', capabilities[1])
print ('Standard options: %X' % capabilities[2][0])
print ('Advanced options: %X' % capabilities[2][1])
