# SimplexLogger

SimplexLogger is a unidirectional single-threaded (i.e. non-duplex) logger. It was written primarily to monitor the output of an Arduino in a microbiology lab.

I did not know how to read the COM port, so I searched the internet and found a note on stackoverflow. The idea was derived from *shshank's* example found at https://stackoverflow.com/questions/19231465/how-to-make-a-serial-port-sniffer-sniffing-physical-port-using-a-python. (accessed:2023-05-18)
The code is obviously different.

Author: bjscsn@github https://github.com/bjscsn

## License

This code is licensed under the *unlicense* license. (Don't laugh) 

For the folks at my age: This code is public domain. Use it, copy it, modify it. I don't care. Just don't complain :-) .

The original idea obviously remains under the original idea's license CC BY-SA 3.0.

## Command line
```
PS C:\DATA.TEST\SimplexLogger> py .\runMonitor.py --help  
usage: Very simple COM port monitor. [-h] [-b BAUD_RATE] -p COM_PORT [-l LOG_FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -b BAUD_RATE, --baud_rate BAUD_RATE
                        Baud rate of port.
  -p COM_PORT, --com_port COM_PORT
                        The COM: port to be used. E.g. 'COM4'. Leave the colon away.
  -l LOG_FILENAME, --log_filename LOG_FILENAME
                        The log file name that you want to use. Must be a valid filename, or full file path on your platform.
```
## Structure
### runMonitor.py
Command line interface. Use -h/--help for details

### monitor.py
Library: An intermediate abstraction between the CLI and the logger.

### SimplexLogger.py
Library: The SimplexLogger class itself.

## Expected Behaviour
*runMonitor.py* starts the tool. *runMonitor.py* reads the command line parameters *baud_rate*, *com_port* and *logfile name*. *com_port* must be provided. *baud_rate* can be set to a valid baud rate, it defaults ot 9600. *logfile name* is optional.

If *logfile name* is not provided, that tools prints to **stdout**. The tools announces startup. When port reading starts, the tool logs a marker consisting of three chervron signs for opening and closing of that marker and a time stamp.
To stop logging, CTL-C needs to be pressed. When CTL-C is pressed, a stop marker is logged to screen and the tools exists. The result can be copy and pasted from the terminal.

If *logfile name* is provided, the tool logs to the logfile name provided. The tools logs a time stamp before every record. The three record type logged are the start marker, the data read from the port and the stop marker. The time stamp is comma separated.
The screen output behaviour is different from the behaviour previously described. The tool announces itself and markes the start of data reading. The tool will print the data read to screen, to allow monitoring of the data flow, but the tool will not advance the line.
This makes the screen output very compact, which is an advantage during long runs. To stop logging, CTL-C needs to be pressed. When CTL-C is pressed, a stop marker is logged to file and screen and the tools exists.

## Notes
- You need to install *pyserial*. You can get *pyserial* on pypi: https://pypi.org/project/pyserial.
```
pip install pyserial
```
typically does the trick.
- The logger reads the full line. The line is terminated by \n of the respective platform. (See also: https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.read_until)
- The char conversion from b'string' is done decoding with 'utf-8'. You need to change the code, if you have a different requirement.
- The start and the stop of the session is logged with a ">>> <<<" marker. This happens in interactive mode (no file logging) and in file logging mode. This should make both result types machine-processable.
- The current output format is strictly CSV, using a comma. You need to change the code, if you have a different requirement.
- Futures: JSON config file, Optional silent running with no stdout for batch processing, make some of the above configurable - But no promises.

## Examples



/END
