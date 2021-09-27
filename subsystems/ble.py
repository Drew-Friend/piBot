import bluetooth


class btComm:
    def __init__(self, addr="00:00:00:00:00:00"):
        self.addr = addr
        self.sock = None

    def scan(self):
        nearby_devices = bluetooth.discover_devices()
        target_address = None
        port = 1
        for bdaddr in nearby_devices:
            if self.addr == bdaddr:
                target_address = bdaddr
                break

        if target_address is not None:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((target_address, port))
            self.sock.send("\x1A")

    def read(self):
        return self.sock.getOutputStream()


# Bluetooth stuff
# bd_addr = “20:13:05:30:01:14”
# port = 1
# sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# sock.connect((bd_addr, port))

# 0x1X for straight forward and 0x11 for very slow to 0x1F for fastest
# sock.send(‘\x1A’)
