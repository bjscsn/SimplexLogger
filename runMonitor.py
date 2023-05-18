#
"""
runMonitor.py

Script to run the monitor for a com port.
"""
__build__ = "114"
__created__ = "2023-05-18_13-38-49"
__updated__ = "2023-05-18_22-33-08"

def parameters2dict(parameters)->dict:
    """
    Converts the config-relevant parameters to a dictionary.
    """
    result = dict()

    result["baud_rate"] = parameters.baud_rate
    result["com_port"] = parameters.com_port
    if parameters.log_filename:
        result["log_filename"] = parameters.log_filename
    else:
        result["log_filename"] = ""
    
    return result

def pre():
    """
    Pre-processing and commandline formatting.
    """
    from argparse import ArgumentParser
    commandline_parser = ArgumentParser(description="A simple serial port monitor - https://github.com/bjscsn/SimplexLogger", epilog="This software is available under the unlicense license (https://unlicense.org)")
    commandline_parser.add_argument("-b", "--baud_rate", dest="baud_rate", type=int, default = 9600, help="Baud rate of port.")
    commandline_parser.add_argument("-p", "--com_port", dest="com_port", required="true", help="The COM: port to be used. E.g. 'COM4'. Leave the colon away.")
    commandline_parser.add_argument("-l", "--log_filename", dest="log_filename", help="The log file name that you want to use. Must be a valid filename, or full file path on your platform.")

    parameters = commandline_parser.parse_args()

    return parameters

def execute(baud_rate:int, com_port:str, log_filename:str):
    """
    Core processing.
    """
    import monitor
    monitor.main(baud_rate=baud_rate, com_port=com_port, log_filename=log_filename)

def main()->None:
    parameters = pre()
    execute(baud_rate=int(parameters.baud_rate), com_port=parameters.com_port, log_filename=parameters.log_filename)

if __name__ == "__main__": main()
# END
