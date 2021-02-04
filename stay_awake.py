#! python3
import math
import pyautogui as gui
import sys
import time

x,y = gui.size()
mouse_speed = 1

def move_mouse(n):
    n = math.ceil(n/3) # One loop last about 3 seconds.
    start = time.perf_counter() # start runtime counter
    for i in range(n):
        gui.moveTo(x*0.66, y*0.66, duration=mouse_speed)
        time.sleep(0.5)
        gui.moveTo(x*0.33, y*0.33, duration=mouse_speed)
        time.sleep(0.5)
    end = time.perf_counter() # end runtime counter
    runtime = end - start # calculate loop runtime in seconds
    print(runtime)

def ask_for_time():
    time_length = gui.prompt(text='How many hours do you want your mouse to move?', title='How Long', default='2')
    gui.alert("Movement will last " + time_length + " hour(s)\n\nPress Ctrl-C to end program")
    return time_length

def convert_to_sec(hrs):
    hrs = int(hrs)
    sec_in_hour = 3600
    secs = hrs * sec_in_hour
    return secs

def main():
    num_hours = ask_for_time()
    num_sec = convert_to_sec(num_hours)
    move_mouse(num_sec)

main()