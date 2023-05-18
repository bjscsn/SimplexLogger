# SimplexLogger

SimplexLogger is a unidirectional single-threaded (i.e. non-duplex) logger. It was written primarily to monitor the output of Arduino-controlled sensors in a microbiology lab.

I did not know how to read from a COM port, so I searched the internet and found a note on stackoverflow. *shshank* illustrated the basic principle at https://stackoverflow.com/questions/19231465/how-to-make-a-serial-port-sniffer-sniffing-physical-port-using-a-python (accessed:2023-05-18). I don't know *shshank*, but if you ever read this, please accept a heartfelt **thank you** and a **virtual beer**.

The code here is obviously different.

## Author

Author: bjscsn@github, https://github.com/bjscsn

## License

This code is licensed under the *unlicense* license.

This code is public domain. Use it, copy it, modify it. I don't care. Just don't complain :-).

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
Library: The SimplexLogger class.

## Expected Behaviour
*runMonitor.py* starts the tool. *runMonitor.py* reads the command line parameters *baud_rate*, *com_port* and *log_filename*. *com_port* must be provided. *baud_rate* can be set to a valid baud rate, it defaults ot 9600. *log_filename* is optional. Records are read from the COM port. Records are expected to be terminated by CRLF. The net record is printed to *stdout* or to *log_filename*.

### Screen Log Mode
If *log_filename* is not provided, the tools prints to **stdout**. The tools announces startup. When port reading starts, the tool logs a session marker consisting of three chervron signs for opening and closing of that marker and a time stamp.
Logging is stopped by pressing CTL-C. When CTL-C is pressed, a session stop marker is logged to screen and the tools exists. The result can then be copied and pasted from the terminal. Only the session start and the stop markers have a time stamp.

### File Log Mode
If *log_filename* is provided, the tool logs to the logfile name provided. The tools logs a time stamp before every record read from COM. There are three types or records logged. A session start marker, the data read from the port and a session stop marker. The time stamp is comma-separated from the record.
The screen output behaviour however is different from the behaviour previously described. The tool announces itself and marks the start of data reading. The tool will also print the data read to screen, to allow monitoring of the data flow. The tool will however not advance the line.
This makes the screen output very compact, which is an advantage during long runs. Logging is stopped by pressing CTL-C. When CTL-C is pressed, a session stop marker is logged to screen and the log file and the tools exists.

## Examples
The following examples use a simple Arduino output simulator.

### Screen Log Mode
```
PS C:\DATA.TEST\SimplexLogger> python runMonitor.py -p COM4
Initialized SimplexLogger b106 on com port: COM4 with baud rate: 9600 with no logging.
Monitor running. Stop with CTRL-C.
>>> Session Start 2023-05-18_21:32:23.106 <<<

Agrifufi Data Processing Unit v1.0
===START OF DATA===
Record_Start_Marker,Record_Number,Relative_Time,Cookies_Thickness,Chocolate_Concentration,Record_End_Marker
DATARECORD,1,1707,DataValue1,DataValue2,DATARECORD_END
DATARECORD,2,3307,DataValue1,DataValue2,DATARECORD_END
DATARECORD,3,4908,DataValue1,DataValue2,DATARECORD_END
DATARECORD,4,6509,DataValue1,DataValue2,DATARECORD_END
DATARECORD,5,8110,DataValue1,DataValue2,DATARECORD_END
>>> Session   End 2023-05-18_21:32:34.345 <<<
Closing..
PS C:\DATA.TEST\SimplexLogger>
```
*Note that everything between session start and session stop origiantes from the Arduino simulator. Your output will of course be different.*

### File Log Mode
```
PS C:\DATA.TEST\SimplexLogger> python runMonitor.py -p COM4 -l logfile.log
Initialized SimplexLogger b106 on com port: COM4 with baud rate: 9600 to log file: 'logfile.log'.
Monitor running. Stop with CTRL-C.
2023-05-18_21:33:39.243: >>> Session Start <<<
2023-05-18_21:33:48.930: DATARECORD,5,8110,DataValue1,DataValue2,DATARECORD_ENDs_Thickness,Chocolate_Concentration,Record_End_Marker
2023-05-18_21:33:50.485: >>> Session End <<<
Closing log file 'logfile.log'.
PS C:\DATA.TEST\SimplexLogger> 
```
*Note that the screen output does not advance, but remains on the same line.*

#### Example logfile.log
```
PS C:\DATA.TEST\SimplexLogger> type logfile.log
2023-05-18_21:33:39.243,>>> Session Start <<<
2023-05-18_21:33:39.244,Value1,DataValue2,DATARECORD_END
2023-05-18_21:33:40.769,
2023-05-18_21:33:40.810,Agrifufi Data Processing Unit v1.0
2023-05-18_21:33:40.831,===START OF DATA===
2023-05-18_21:33:40.934,Record_Start_Marker,Record_Number,Relative_Time,Cookies_Thickness,Chocolate_Concentration,Record_End_Marker
2023-05-18_21:33:42.530,DATARECORD,1,1707,DataValue1,DataValue2,DATARECORD_END
2023-05-18_21:33:44.123,DATARECORD,2,3307,DataValue1,DataValue2,DATARECORD_END
2023-05-18_21:33:45.731,DATARECORD,3,4908,DataValue1,DataValue2,DATARECORD_END
2023-05-18_21:33:47.338,DATARECORD,4,6509,DataValue1,DataValue2,DATARECORD_END
2023-05-18_21:33:48.930,DATARECORD,5,8110,DataValue1,DataValue2,DATARECORD_END
2023-05-18_21:33:50.485,>>> Session End <<<
PS C:\DATA.TEST\SimplexLogger>
```
*Note that all session data is prefixed with a time stamp. The start and stop makers are different. 

## Notes
- You need to install *pyserial*. You can get *pyserial* on pypi: https://pypi.org/project/pyserial.
```
pip install pyserial
```
typically does the trick.
- The logger reads the full line. The line is terminated by \n of the respective platform. (See also: https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.read_until)
- The char conversion from b'string' is done decoding with 'utf-8'. You need to change the code, if you have a different requirement.
- The start and the stop of the session is logged with a ">>> <<<"-enclosed marker. This happens in screen interactive mode and in file logging mode. This should make both result types sufficiently machine-readable.
- The current output format is strictly CSV, using a comma. You need to change the code, if you have a different requirement. If you can control the Arduino output, consider to also write comma-separated values to serial out.

## Futures

- JSON config file
- make some of the above configurable
- Optional silent running with no stdout for batch processing

But no promises at this point.

/END
