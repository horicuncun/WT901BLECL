from serial import Serial

class BWT901(Serial):
    def __init__(self, Port):
        self.myserial = super().__init__(Port, baudrate=115200, timeout=1)

    def readData(self):
        try:
            while True:
                data = super(BWT901, self).read(size=20)
                if len(data) > 0:
                    if data[0] != 85:
                        while True:
                            data = super(BWT901, self).read(size=1)
                            if data == b'\x55':
                                super(BWT901, self).read(size=19)
                                break
                        continue
                    axL = data[2]
                    axH = data[3]
                    ayL = data[4]
                    ayH = data[5]
                    azL = data[6]
                    azH = data[7]
                    wxL = data[8]
                    wxH = data[9]
                    wyL = data[10]
                    wyH = data[11]
                    wzL = data[12]
                    wzH = data[13]
                    RollL = data[14]
                    RollH = data[15]
                    PitchL = data[16]
                    PitchH = data[17]
                    YawL = data[18]
                    YawH = data[19]
                    data_dict = {}
                    data_dict["ax"] = ((axH << 8) | axL) / 32768.0 * 16.0
                    data_dict["ay"] = ((ayH << 8) | ayL) / 32768.0 * 16.0
                    data_dict["az"] = ((azH << 8) | azL) / 32768.0 * 16.0
                    data_dict["wx"] = ((wxH << 8) | wxL) / 32768.0 * 2000.0
                    data_dict["wy"] = ((wyH << 8) | wyL) / 32768.0 * 2000.0
                    data_dict["wz"] = ((wzH << 8) | wzL) / 32768.0 * 2000.0
                    data_dict["Roll"] = ((RollH << 8) | RollL) / 32768.0 * 180.0
                    data_dict["Pitch"] = ((PitchH << 8) | PitchL) / 32768.0 * 180.0
                    data_dict["Yaw"] = ((YawH << 8) | YawL) / 32768.0 * 180.0
                    return (data_dict)

        except KeyboardInterrupt:
            super(BWT901, self).close()


if __name__ == "__main__":
    jy_sensor = BWT901("COM3")

    first_open_date = None
    while True:
        data_dict = jy_sensor.readData()
        print(data_dict)