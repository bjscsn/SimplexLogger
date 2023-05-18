#
"""
runMonitor.py

Script to run the monotor for a com port.
"""
__build__ = "102"
__created__ = "2023-05-18_13-38-49"
__updated__ = "2023-05-18_14-48-17"

def pre():
    """
    Pre-p[rocessing and commandline formatting.
    """
    from argparse import ArgumentParser
    commandline_parser = ArgumentParser(prog="Very simple COM port monitor.")
    commandline_parser.add_argument("-b", "--baud_rate", dest="baud_rate", type=int, default=9600, help="Baud rate of port.")
    commandline_parser.add_argument("-p", "--com_port", dest="com_port", required=True, help="The COM: port to be used. E.g. 'COM4'. Leave the colon away.")
    commandline_parser.add_argument("-l", "--log_filename", dest="log_filename", help="The log file name that you want to use. Must be a valid filename, or full file path on your platform.")
    commandline_parser.add_argument("-c", "--config_file", dest="use_config_file", action="store_true", help="Uses the config file instead of arguments. Config file values will take precedence. Config file name is 'monitor.json'. If not config file exists, the first call will generate an empty config file in CWD.")

    parameters = commandline_parser.parse_args()

    import json
    monitorConfig = dict()
    monitorConfig["baud_rate"] = parameters.baud_rate
    monitorConfig["com_port"] = parameters.com_port
    monitorConfig["log_filename"] = parameters.log_filename
    monitorConfig_defaultFilename = "monitor.json"
    monitorConfig_jsonData = json.dumps(monitorConfig, indent=4)
    with open(monitorConfig_defaultFilename, "w") as monitorConfig_defaultFile:
        monitorConfig_defaultFile.write(monitorConfig_jsonData)

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