import random

import os

mac = [0x00, 0x16, 0x3e,
       random.randint(0x00, 0x7f),
       random.randint(0x00, 0xff),
       random.randint(0x00, 0xff)]

def run():
  
  macaddress = ':'.join(map(lambda x: "%02x" % x, mac))

  os.system("sudo ifconfig en0 ether " + macaddress)

  print("Your MAC Address is now: " + macaddress)
