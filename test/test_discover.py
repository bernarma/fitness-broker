import sys
import usb.core

sys.stdout.write('Listing USB Devices\n')

# find USB devices
dev = usb.core.find(find_all=True)

# loop through devices, printing vendor and product ids in decimal and hex
for cfg in dev:
  sys.stdout.write('Manufacturer=' + str(cfg.iManufacturer) + '\n')
  sys.stdout.write('Serial Number=' + str(cfg.iSerialNumber) + '\n')
  sys.stdout.write('Product=' + str(cfg.iProduct) + '\n')
  sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
  sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')