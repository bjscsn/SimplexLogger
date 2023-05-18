# SimplexLogger

SimplexLogger is a unidirectional single-threaded (i.e. non-duplex) logger. 

The idea was derived from the example found at https://stackoverflow.com/questions/19231465/how-to-make-a-serial-port-sniffer-sniffing-physical-port-using-a-python.

Author: bjscsn@github https://github.com/bjscsn

## License

This code is licensed under the *unlicense* license. (Don't laugh) For the folks at my age: This code is public domain. 
Use it, copy it, modify it. I don't care. Just don't complain. 

The original idea remains under the original idea's license CC BY-SA 3.0.

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
Library: Intermediate abstraction.

### SimplexLogger.py
Library: Contains SimplexLogger class.

.
