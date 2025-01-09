import time
import threading

def title():
    print("\n")  
    print("\033[13C THE CLOCK ")
    print("\n")
    print("With this simple clock you can set the time,\nthe alarm, choose the time format, \nand turn it on/off  ")
    print("\n")  

# Initialize the variables
current_time = (16, 30, 0)
alarm_time = None
clock_running = False 
clock_thread = None  

# Function that allows user to choose the time format
def choose_time_format():
    global time_choice
    while True:
        format_choice = input("Choose time format, enter 12 or 24 : ")
        if format_choice in ["12", "24"]:
            time_choice = format_choice
            break
        print("Please enter 12 or 24")


# Function that displays the time in the right format
def display_time(current_time):
    if time_choice == "12":
        hours = current_time[0] % 12
        hours = hours if hours != 0 else 12
        am_pm = "AM" if current_time[0] < 12 else "PM"
        time.sleep(0.5)
        print(f"\033[s\033[2A\033[100D{hours:02} : {current_time[1]:02} : {current_time[2]:02}  {am_pm}\033[u", end="", flush=True)
    else:
        hours = f"{current_time[0]:02}"
        minutes = f"{current_time[1]:02}"
        seconds = f"{current_time[2]:02}"
        print(f"\033[s\033[2A\033[100D{hours} : {minutes} : {seconds}\033[u", end="", flush=True)

# Function that updates the time every second
def update_time():
    global current_time
    while clock_running:  # Check if the clock is running
        display_time(current_time)
        time.sleep(1)
        current_time = (current_time[0], current_time[1], current_time[2] + 1)
        if current_time[2] == 60:
            current_time = (current_time[0], current_time[1] + 1, 0)
        if current_time[1] == 60:
            current_time = (current_time[0] + 1, 0, 0)
        if current_time[0] == 24:
            current_time = (0, 0, 0)
        check_alarm()


# Function that sets the current time
def set_time(new_time):
    global current_time
    current_time = new_time
    return f"{new_time[0]:02}:{new_time[1]:02}:{new_time[2]:02}"

# Function that sets the alarm
def set_alarm(new_alarm_time):
    global alarm_time
    alarm_time = new_alarm_time
    print(f"Alarm time set for {alarm_time[0]:02}:{alarm_time[1]:02}:{alarm_time[2]:02}")

# Function that checks if the alarm should ring
def check_alarm():
    if current_time == alarm_time:
        print("\n\033[s\033[3A\033[100D DRING DRING !!! Time to wake up !!! \033[u", end="", flush=True)

# Function to start the clock
def start_clock():
    global clock_running, clock_thread
    if not clock_running:
        clock_running = True
        clock_thread = threading.Thread(target=update_time)
        clock_thread.start()
        print("Clock started...")

# Function to stop the clock
def stop_clock():
    global clock_running
    clock_running = False
    print("Clock stopped.")

# Get User input for time and alarm
def user_input():
    while True:
        try:
            new_time = input("Enter current time as (hh:mm:ss): ")
            if not new_time:
                raise ValueError("input cannot be empty")
            hours, minutes, seconds = [int(value) for value in new_time.split(":")]
            if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                raise ValueError("time values must be in the range\nhh(0-23), mm(0-59), ss(0-50)")
            print(f"The new time is: {set_time((hours, minutes, seconds))}")

            alarm_time_input = input("Enter alarm time as (hh:mm:ss): ")
            if not alarm_time_input:
                raise ValueError("input cannot be empty")
            alarm_hours, alarm_minutes, alarm_seconds = [int(value) for value in alarm_time_input.split(":")]
            if not (0 <= alarm_hours < 24 and 0 <= alarm_minutes < 60 and 0 <= alarm_seconds < 60):
                raise ValueError("alarm time values must be in the range\nhh(00-23), mm(0-59), ss(0-50)")
            set_alarm((alarm_hours, alarm_minutes, alarm_seconds))
            break

        except ValueError as error:
            print(f"Invalid time format: {error}.")

# Main function
def main():
    title()
    choose_time_format()
    user_input()

    action = input("Type 'start' to start the clock : ")
    if action == 'start':
            if not clock_running:  
                start_clock()
            else:
                print("\nThe clock is already running.")
    print("\n\n")
    action = input("Type 'stop' to stop the clock : ")
    if action == 'stop':
            if clock_running:  
                stop_clock()
            else:
                print("\nThe clock is already stopped.")
    else:
            print("\nInvalid input. Please type 'start' or 'stop'.")

# Run main 
main()