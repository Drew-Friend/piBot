import bluetooth


class btComm:
    def __init__(self, addr="00:00:00:00:00:00"):
        self.addr = addr
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def scan(self):
        nearby_devices = bluetooth.discover_devices()
        for bdaddr in nearby_devices:
            print(bdaddr)
            if self.addr == bdaddr:
                self.sock.connect((self.addr, self.port))
                self.sock.send("\x1A")
                print("Connected to %s" % (bdaddr))
                break

    # def scan(self):
    #     print("Scanning for bluetooth devices:")
    #     devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    #     number_of_devices = len(devices)
    #     print(number_of_devices, "devices found")
    #     for addr, name, device_class in devices:
    #         print("\n")
    #         print("Device:")
    #         print("Device Name: %s" % (name))
    #         print("Device MAC Address: %s" % (addr))
    #         print("Device Class: %s" % (device_class))
    #         print("\n")
    #         if addr == self.addr:
    #             self.sock.connect((self.addr, self.port))
    #             self.sock.send("\x1A")
    #             print("Connected to %s" % (name))

    def read(self):
        return self.sock.getOutputStream()

    def isConnected(self):
        try:
            self.sock.getpeername()
            return True
        except:
            return False


# Bluetooth stuff
# bd_addr = “20:13:05:30:01:14”
# port = 1
# sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# sock.connect((bd_addr, port))

# 0x1X for straight forward and 0x11 for very slow to 0x1F for fastest
# sock.send(‘\x1A’)
