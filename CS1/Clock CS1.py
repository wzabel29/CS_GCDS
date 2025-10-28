""" from tkinter import*
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=(80), background = "cyan", foreground = "black")
label.pack(anchor = "center")
time()

mainloop()
 """
from datetime import datetime, timedelta

specific_time = datetime(2025, 1, 1, 10, 0, 0) # January 1, 2025, 10:00:00 AM
current_time = datetime.now() # The current date and time

specific_time += timedelta(minutes=5)
print(specific_time.strftime("%H:%M:%S"))

if current_time > specific_time:
    print("The current time is past the specific time.")
elif current_time < specific_time:
    print("The current time is before the specific time.")
else:
    print("The current time is exactly the same as the specific time.")
