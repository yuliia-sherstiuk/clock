import time

# Initialize the variables
current_time = (16, 30, 0)
alarm_time = None

# Function that display the time in the right format
def display_time(current_time):
    hours = f"{current_time[0]:02}"
    minutes = f"{current_time[1]:02}"
    seconds = f"{current_time[2]:02}"
    print(f"{hours} : {minutes} : {seconds}", end='\r')

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

# Function that set the current time
def set_time(new_time):
    global current_time
    current_time = new_time
    display_time(current_time)

# Function that set the alarm
def set_alarm(new_alarm_time):
    global alarm_time
    alarm_time = new_alarm_time
    print (f"Alarm time set for {alarm_time[0]:02} : {alarm_time[1]:02} : {alarm_time[2]:02}")

# Function that check if the alarm should ring
def check_alarm():
    if current_time == alarm_time:
        print ("DRING DRING !!! Time to wake up !!!")


