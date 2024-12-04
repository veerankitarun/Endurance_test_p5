import serial
import time

def initialize_serial(port, baud_rate=9600, timeout=1):
    """
    Initialize the serial connection to the Arduino.
    
    Args:
        port (str): The COM port to which the Arduino is connected.
        baud_rate (int): The baud rate for serial communication. Default is 9600.
        timeout (int): Timeout for serial reading in seconds. Default is 1.
    
    Returns:
        serial.Serial: A configured serial object.
    """
    try:
        ser = serial.Serial(port, baud_rate, timeout=timeout)
        print(f"Serial connection established on port {port} at {baud_rate} baud.")
        return ser
    except serial.SerialException as e:
        print(f"Error: Could not establish serial connection. {e}")
        raise

def send_at_command(ser, command, wait_time=0.5):
    """
    Send an AT command to the Arduino and return the response.
    
    Args:
        ser (serial.Serial): The serial object.
        command (str): The AT command to send.
        wait_time (float): Time to wait for a response after sending the command. Default is 0.5 seconds.
    
    Returns:
        str: The response from the Arduino.
    """
    try:
        ser.write((command + "\r\n").encode())  # Send the command with CRLF termination
        time.sleep(wait_time)  # Wait for the Arduino to respond
        response = ser.read_all().decode().strip()  # Read and decode the response
        print(f"Command: {command} → Response: {response}")
        return response
    except Exception as e:
        print(f"Error sending command '{command}': {e}")
        return ""

def parse_pressure_response(response):
    """
    Parse the pressure value from the Arduino response.
    Expects a response like '+SPR:34.7831,24.1309\nOK'.
    
    Args:
        response (str): The response string from the Arduino.
    
    Returns:
        float: The parsed pressure value in mbar, or None if parsing fails.
    """
    try:
        if response.startswith("+SPR:"):
            # Split response to extract pressure value
            values = response.split(":")[1].split(",")
            pressure = float(values[1])  # Extract the second value (pressure in mbar)
            return pressure
        else:
            print(f"Invalid response format: {response}")
            return None
    except (IndexError, ValueError):
        print(f"Error parsing pressure response: {response}")
        return None

def close_serial(ser):
    """
    Safely close the serial connection.
    
    Args:
        ser (serial.Serial): The serial object.
    """
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")
    else:
        print("Serial connection already closed.")
