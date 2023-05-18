#
"""
SimplexLogger.py

SimplexLogger is a unidirectional single-threaded logger. The idea was derived from the code found at https://stackoverflow.com/questions/19231465/how-to-make-a-serial-port-sniffer-sniffing-physical-port-using-a-python.
"""
__build__ = "110"
__created__ = "2023-05-18_12-59-19"
__updated__ = "2023-05-18_22-34-06"

# GLOBAL
CRLF = "\n"
CR = "\r"
NOCRLF = ""

class SimplexLogger():
    """
    SimplexLogger

    A simple serial port logger
    """
    def __init__(self, baud_rate:int, com_port:str, log_filename:str)->None:
        """
        Initialize SimplexLogger

        baud_rate:str
            The baud rate to use on COM port.

        com_port:str
            The COM port string in the form "COM#",e.g.: "COM2".

        log_filename:str
            A valid file or filepath to log into.
        """
        self._declare()
        if baud_rate: self.baud_rate = baud_rate
        if com_port: self.com_port = com_port.upper()
        if log_filename: self.log_filename = log_filename
        print("Initialized {}.".format(self.__str__()))

    def _declare(self)->None:
        """
        Declare class variables
        """
        self.name = "SimplexLogger"
        self.version = self.name + " b" + __build__
        self.baud_rate = int
        self.com_port = str
        self.log_filename = ""

    def _getTimeStamp(self)->str:
        """
        Generate a time stamp string in the form 'YYYY-MM-DD_hh:mm:ss.uuu'. Note: The last three digits of the %f microsecond value are cut away, the value is not rounded.
        """
        from datetime import datetime
        timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d_%H:%M:%S.%f")
        return timestamp[:-3]
    
    def _toLogRecord(self, data:str, separator=": ")->str:
        """
        Format the log record.
        """
        result = "{}{}{}".format(self._getTimeStamp(), separator, data)
        return result

    def run(self)->None:
        """
        Monitor the port and (optionally) log to file
        """
        print("Monitor running. Stop with CTRL-C.")
        
        import serial
        monitor = serial.Serial(port=self.com_port, baudrate=self.baud_rate)
        
        if self.log_filename:
            with open(self.log_filename, "+a") as log_file:
                print(self._toLogRecord(data=">>> Session Start <<<"))
                log_file.write(self._toLogRecord(data=">>> Session Start <<<", separator=",") + CRLF)
                try:
                    while True:
                        buffer = monitor.read_until()
                        print(self._toLogRecord(buffer.decode('utf-8').strip()), end=CR)
                        log_file.write(self._toLogRecord(data=buffer.decode('utf-8').strip(), separator=",") + CRLF)
                except KeyboardInterrupt as ki:
                    print()
                    print(self._toLogRecord(data=">>> Session End <<<"))
                    log_file.write(self._toLogRecord(data=">>> Session End <<<", separator=",") + CRLF)
                    print("Closing log file '{}'.".format(self.log_filename))
                    log_file.close()
        else:
            print(">>> Session Start {} <<<".format(self._getTimeStamp()))
            try:
                while True:
                    buffer = monitor.read_until()
                    print(buffer.decode('utf-8').strip())
            except KeyboardInterrupt as ki:
                print(">>> Session   End {} <<<".format(self._getTimeStamp()))
                print("Closing..")
           
    def __str__(self)->str:
        if self.log_filename:
            return("{0} on com port: {2} with baud rate: {1} to log file: '{3}'".format(self.version, self.baud_rate, self.com_port, self.log_filename))
        else:
            return("{0} on com port: {2} with baud rate: {1} with no logging".format(self.version, self.baud_rate, self.com_port, self.log_filename))

if __name__ == "__main__": print("ERROR: This is a library file. Use 'runMonitor' to start monitoring.")
#END
