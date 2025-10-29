    import serial as pyserial
    import serial.tools.list_ports as ports
    
    class Radio:
        
        port = ""  # COM port variable
        serial = None
        baudrate = ""
    
        def receive_message():
            ''' Receives the data from the serial port '''
            return Radio.clean_string(str(Radio.serial.readline()))
        
        
        def wait_for_message(message):
            ''' Aspetta un determinato messaggio da Arduino '''
            input_message = ""
        
            while message not in input_message:
                input_message = str(Radio.serial.readline())
            
            return input_message
        
        
        def list_available_ports():
            ''' Lists all the available serial ports '''
            s = []
            for _ in ports.comports():
                if ("n/a" not in _.description.lower()):
                    s.append(f"{_.device} : {_.description}")
            return s
    
        def init():
            ''' Connect with comprehensive error handling '''
            try:
                Radio.serial = pyserial.Serial(Radio.port, Radio.baudrate, timeout=0)
                return Radio.isActive()
                
            except Radio.serial.SerialException as e:
                print(f"Serial port error: {e}")
            except PermissionError:
                print("Permission denied. Fix:")
                print("  Linux: sudo usermod -a -G dialout $USER")
                print("  Windows: Run as administrator")
            except FileNotFoundError:
                print("Port not found. Check:")
                print("  - Device connected and powered")
                print("  - Correct port name")
                print("  - Driver installed")
            
            return None
    
        def isActive():
            ''' Checks if the serial connection is active '''
            return Radio.serial
    
        def setBaudrate(baudrate):
            ''' Sets the baudrate for the serial connection '''
            Radio.baudrate = baudrate
        
        def getBaudrate():
            ''' Gets the baudrate for the serial connection '''
            return Radio.baudrate
    
        def setCOM(port):
            ''' Sets the COM port for the serial connection '''
            Radio.port = port
        
        def getCOM():
            ''' Gets the COM port for the serial connection '''
            return Radio.port
        
        def clean_string(msg):
            ''' Restituisce solo la parte utile di una stringaricevuta tramite connessione seriale '''
            out = msg[2:][:-5]
            return out