""" startup.py

    Script that run at windows startup to initiate multiple required programs """
import tkinter
import subprocess
from datetime import datetime

BAT = r"""@echo off
cd "C:\Program Files (x86)\Microsoft Office\root\Office16"
start OUTLOOK.EXE

cd "C:\Program Files (x86)\Microsoft\Skype for Desktop"
start Skype.exe

exit
"""

# cd "C:\Program Files (x86)\Microsoft Office\root\Office16"
# start lync.exe

#cd "C:\Program Files (x86)\Common Files\Pulse Secure\JamUI"
#start Pulse.exe -show

TODAY = datetime.today()
WEEKDAY = TODAY.weekday()
if WEEKDAY in range(5) and TODAY.hour < 18:
    FILENAME = 'startup.bat'
    FILE_WP = open(FILENAME, 'w')
    FILE_WP.write(BAT)
    FILE_WP.close()
    subprocess.call([FILENAME])
    #On Windows you have to call through cmd.exe.
    #/c tells cmd to run the follow command
    subprocess.call(['cmd', '/c', 'del', FILENAME])

    #Create a popup on fridays
    if WEEKDAY == 4:
        ROOT = tkinter.Tk()
        FRAME = tkinter.Frame(ROOT)
        FRAME.grid(column=0, row=0)
        LINE = "Fill and Submit this week timesheet"
        _ = tkinter.Label(FRAME, text=LINE, height=10, width=len(LINE)+5).grid(column=0, row=0)
        ROOT.mainloop()

    if TODAY.day == 20:
        ROOT = tkinter.Tk()
        FRAME = tkinter.Frame(ROOT)
        FRAME.grid(column=0, row=0)
        LINE = "Fill and Submit Km Expenses Report"
        _ = tkinter.Label(FRAME, text=LINE, height=10, width=len(LINE)+5).grid(column=0, row=0)
        ROOT.mainloop()
