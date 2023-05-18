#
"""
monitor.py

Monitoring script for COM port.
"""
__build__ = "101"
__created__ = "2023-05-18_13-00-50"
__updated__ = "2023-05-18_15-51-37"

def main(baud_rate:int, com_port:str, log_filename:str):
    from SimplexLogger import SimplexLogger
    this = SimplexLogger(baud_rate=baud_rate, com_port=com_port, log_filename=log_filename)
    this.run()

if __name__ == "__main__": print("This is not a script file.")
# END