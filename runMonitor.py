#
"""
runMonitor.py

Script to run the monotor for a com port.
"""
__build__ = "105"
__created__ = "2023-05-18_13-38-49"
__updated__ = "2023-05-18_15-22-51"

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
    Pre-p[rocessing and commandline formatting.
    """
    # TODO: Convert to a hierachical parser.
    from argparse import ArgumentParser
    commandline_parser = ArgumentParser(prog="Very simple COM port monitor.")
    commandline_parser.add_argument("-b", "--baud_rate", dest="baud_rate", type=int, help="Baud rate of port.")
    commandline_parser.add_argument("-p", "--com_port", dest="com_port", help="The COM: port to be used. E.g. 'COM4'. Leave the colon away.")
    commandline_parser.add_argument("-l", "--log_filename", dest="log_filename", help="The log file name that you want to use. Must be a valid filename, or full file path on your platform.")
    commandline_parser.add_argument("-c", "--config_file", dest="use_config_file", action="store_true", help="Uses the config file. Config file name is 'monitor.json'. Parameters will take precedence. If not config file exists, a config file will be created in CWD. If you give the parameters as well, the config file will be updated with those values.")

    parameters = commandline_parser.parse_args()

    if parameters.use_config_file:
        import json, os
        monitorConfig_defaultFilename = "monitor.json"
        
        if os.path.exists(monitorConfig_defaultFilename):
            with open(monitorConfig_defaultFilename, "w") as monitorConfig_defaultFile:
                monitorConfig = json.load(monitorConfig_defaultFile)
                
                # synchronize config with commandline parameters
                if parameters.baud_rate: 
                    monitorConfig["baud_rate"] = parameters.baud_rate
                else:
                    parameters.baud_rate = monitorConfig["baud_rate"]

                if parameters.com_port: 
                    monitorConfig["com_port"] = parameters.com_port
                else:
                    parameters.com_port = monitorConfig["com_port"]

                if parameters.log_filename: 
                    monitorConfig["log_filename"] = parameters.log_filename
                else:
                    parameters.log_filename = monitorConfig["log_filename"]
            
            # Update config file
            monitorConfig_jsonData = json.dumps(monitorConfig, indent=4)

            with open(monitorConfig_defaultFilename, "w") as monitorConfig_defaultFile:
                monitorConfig_defaultFile.write(monitorConfig_jsonData)

        else: # else create a new config file
            monitorConfig = parameters2dict(parameters=parameters)

            monitorConfig_jsonData = json.dumps(monitorConfig, indent=4)
            
            with open(monitorConfig_defaultFilename, "w") as monitorConfig_defaultFile:
                monitorConfig_defaultFile.write(monitorConfig_jsonData)
    
    else: # if use config file is not specified, deal with the defaults here
        if not parameters.baud_rate: parameters.baud_rate = 9600
        if not parameters.com_port: exit("Error. You MUST specify a COM port. Try -h/--help for help.")

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