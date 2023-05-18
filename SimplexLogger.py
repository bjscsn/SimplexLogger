#
"""
SimplexLogger.py

SimplexLogger is a unidirectional single-threaded logger. The idea was derived from the code found at https://stackoverflow.com/questions/19231465/how-to-make-a-serial-port-sniffer-sniffing-physical-port-using-a-python.
"""
__build__ = "104"
__created__ = "2023-05-18_12-59-19"
__updated__ = "2023-05-18_15-51-34"

# GLOBAL
CRLF = "\n"
NOCRLF = ""

class SimplexLogger():
    """
    """
    def __init__(self, baud_rate:int, com_port:str, log_filename:str):
        self._declare()
        if baud_rate: self.baud_rate = baud_rate
        if com_port: self.com_port = com_port.upper()
        if log_filename: self.log_filename = log_filename
        print("Initialized {}.".format(self.__str__()))

    def _declare(self):
        self.name = "SimplexLogger"
        self.baud_rate = int
        self.com_port = str
        self.log_filename = ""

    def run(self)->None:
        print("Monitor running. Stop with CTRL-C.")
        serial=None
        import serial
        
        listener = serial.Serial(port=self.com_port, baudrate=self.baud_rate)
        
        if self.log_filename:
            with open(self.log_filename, "+a") as log_file:
                try:
                    while True:
                        buffer = listener.read_until()
                        print(buffer.decode('utf-8').strip())
                        log_file.write(buffer.decode('utf-8').strip() + CRLF)
                except KeyboardInterrupt as ki:
                    print("Closing log file '{}'.".format(self.log_filename))
                    log_file.close()
        else:
            try:
                while True:
                    buffer = listener.read_until()
                    print(buffer.decode('utf-8').strip())
            except KeyboardInterrupt as ki:
                print("Closing..")
           
    def __str__(self)->str:
        return("{0} b{4} on com port: {2} with baud rate: {1} to log file: '{3}'".format(self.name, self.baud_rate, self.com_port, self.log_filename, __build__))

if __name__ == "__main__": print("This is not a script file.")
#END