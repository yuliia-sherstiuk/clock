# clock
## Overview
The clock project is a simple functional application that displays the current time.

## Features
Display the current time in the format hh:mm:ss
Automatically updates the time every second
Alarm feature

## Program Steps
### Initialize the time and alarm
Create a variable to store the current time and another for the alarm time
### Define a function to display the time
Create a function that takes a tuple representing the time 
(hours, minutes, seconds) as a parameter and display the time in the format hh : mm : ss
### Define a function to update the time
Create a function that updates the time every second
Increment the seconds, minutes and hours while handling overflow ( example: 60 seconds become 1 minute)
### Define a function to set the time
Create a function that allows to set the current time by passing a tuple in the format (hours, minutes, seconds)
Call the display_time function to update the display after setting the time
### Define a function to set the alarm
Create a function that allow to set the alarm by passing a tuple in the format (hours, minutes, seconds)
### Define a function to check the alarm
Create a fuction that checks if the current time matches the alarm time
If the hours, minutes, and seconds match, display that the alarm is ringing
### Main loop
Create an infinite loop that calls the update time function
In each iteration, check if the alarm should ring by calling the function that check the alarm