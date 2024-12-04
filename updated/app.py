from datetime import datetime
from utils import initialize_serial, send_at_command, parse_pressure_response, close_serial

def log_cycle_data(cycle, status, pressure, condition, results):
    """
    Log cycle data to a results list.
    
    Args:
        cycle (int): The current cycle number.
        status (str): Pass or Fail.
        pressure (float): The pressure value in mbar.
        condition (str): Condition being tested (on/off).
        results (list): List to store results for all cycles.
    """
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    results.append(f"{timestamp} | Cycle {cycle} | {condition} | Pressure: {pressure} mbar | Status: {status}")

def save_results_to_file(results):
    """
    Save the results to a text file within a folder named by the current date.
    The function creates unique filenames (test_file-1.txt, test_file-2.txt) for each test run.
    
    Args:
        results (list): List of results strings.
    """
    # Get current date as folder name (e.g., "2024-12-04")
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Define the directory path based on the current date
    folder_path = os.path.join("..", "test_results", current_date)
    
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Find the next available file number (test_file-1.txt, test_file-2.txt, ...)
    file_number = 1
    while os.path.exists(os.path.join(folder_path, f"test_file-{file_number}.txt")):
        file_number += 1
    
    # Create the unique filename
    file_name = f"test_file-{file_number}.txt"
    file_path = os.path.join(folder_path, file_name)
    
    try:
        # Write results to the file
        with open(file_path, 'w') as file:
            file.write("\n".join(results))
        print(f"Results saved to {file_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

def main():
    # Configuration
    port = "COM3"  # Replace with your Arduino's port
    cycles = 10
    off_condition_pr = 30.0  # Off condition in mbar
    on_condition_pr = 20.0   # On condition in mbar
    results = []  # List to store cycle results
    output_file = "test_results.txt"  # File to save the results
    commands = {
        "open_valve": "AT+TVALVE=3,1",
        "close_valve": "AT+TVALVE=3,0",
        "get_pressure": "AT+TSPR=1,0"
    }
    
    # Initialize serial communication
    ser = initialize_serial(port)
    
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle} of {cycles}")
        
        # Close valve and read pressure
        response = send_at_command(ser, commands["close_valve"])
        if response != "OK":
            print(f"Error closing valve: {response}")
            log_cycle_data(cycle, "Fail", 0.0, "Close Valve", results)
            continue
        
        response = send_at_command(ser, commands["get_pressure"])
        pressure = parse_pressure_response(response)
        if pressure is None:
            print(f"Error reading pressure: {response}")
            log_cycle_data(cycle, "Fail", 0.0, "Close Valve", results)
            continue
        
        print(f"Closed Valve Pressure: {pressure} mbar")
        status = "Pass" if pressure > off_condition_pr else "Fail"
        log_cycle_data(cycle, status, pressure, "Close Valve", results)
        
        # Open valve and read pressure
        response = send_at_command(ser, commands["open_valve"])
        if response != "OK":
            print(f"Error opening valve: {response}")
            log_cycle_data(cycle, "Fail", 0.0, "Open Valve", results)
            continue
        
        response = send_at_command(ser, commands["get_pressure"])
        pressure = parse_pressure_response(response)
        if pressure is None:
            print(f"Error reading pressure: {response}")
            log_cycle_data(cycle, "Fail", 0.0, "Open Valve", results)
            continue
        
        print(f"Opened Valve Pressure: {pressure} mbar")
        status = "Pass" if pressure < on_condition_pr else "Fail"
        log_cycle_data(cycle, status, pressure, "Open Valve", results)
    
    # Save results to a text file
    save_results_to_file(results, output_file)
    close_serial(ser)
    print("Process completed.")

if __name__ == "__main__":
    main()
