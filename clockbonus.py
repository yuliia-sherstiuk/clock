import time

def title():
    print(" ")  
    print(" " * 13, " THE CLOCK ", " " * 13)
    print(" ")
    print("With this simple clock you can set the time, ")
    print("the alarm, choose the time format, and turn it on/off ")  
    print(" ")   
    print(" ")  

# Initialize the variables
current_time = (16, 30, 0)
alarm_time = None

# Function that allow user to choose the time format
def choose_time_format():
    while True:
        format_choice = input ("Choose time format, enter 12 or 24 :")
        if format_choice in ["12","24"]:
            time_format = format_choice
        break
    else:
        print("Please enter 12 or 24")

# Function that display the time in the right format
def display_time(current_time):
    hours = f"{current_time[0]:02}"
    minutes = f"{current_time[1]:02}"
    seconds = f"{current_time[2]:02}"
    print(f"{hours} : {minutes} : {seconds}", end="\r")

# Function that update the time every second
def update_time():
    global current_time
    while True:
        display_time(current_time)
        time.sleep(1)
        current_time = (current_time[0], current_time[1], current_time[2]+1)
        if current_time[2] == 60:
            current_time = (current_time[0], current_time[1] + 1 , 0)
        if current_time[1] == 60:
            current_time = (current_time[0] + 1 , 0 , 0)
        if current_time[0] == 24:
            current_time = (0 , 0 , 0)
        check_alarm()
        
# Function that set the current time
def set_time(new_time):
    global current_time
    current_time = new_time
    display_time(current_time)

# Function that set the alarm
def set_alarm(new_alarm_time):
    global alarm_time
    alarm_time = new_alarm_time
    print (f"Alarm time set for {alarm_time[0]:02}:{alarm_time[1]:02}:{alarm_time[2]:02}")

# Function that check if the alarm should ring
def check_alarm():
    if current_time == alarm_time:
        print ("DRING DRING !!! Time to wake up !!!")

# Get User input for time and alarm
def user_input():
    while True:
        try:
            new_time = input("Enter current time as (hh:mm:ss): ")
            hours, minutes, seconds = [int(value) for value in new_time.split(":")]
            set_time((hours, minutes, seconds))
            alarm_time_input = input("Enter alarm time as (hh:mm:ss): ")
            alarm_hours, alarm_minutes, alarm_seconds = [int(value) for value in alarm_time_input.split(":")]
            set_alarm((alarm_hours, alarm_minutes, alarm_seconds))
            break
        except ValueError:
            print("Invalid time format. Please enter time as (hh:mm:ss): ")

# Main function
def main_loop():
    title()
    user_input()
    update_time()
    check_alarm()


main_loop()
