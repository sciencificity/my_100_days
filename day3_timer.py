import time
import os
import winsound

# The print for the timer was not showing on the screen
# I need to print unbuffered - this code from SO: https://stackoverflow.com/questions/107705/disable-output-buffering
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)

def main_timer(minutes):
    seconds = minutes * 60
    while seconds:
        os.system("cls")
        mins = int(seconds / 60)
        secs = round((seconds % 60), 0)
        print(f'{mins:02.0f}:{secs:02.0f}')
        time.sleep(1)
        seconds -= 1 
        
    # One last time print for the timer to go to 00:00!
    os.system("cls")
    mins = int(seconds / 60)
    secs = round((seconds % 60), 0)
    print(f'{mins:02.0f}:{secs:02.0f}')
    
    # Sound a beep
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    print('You completed a stint!\n\n')

# Countdown 20 min
main_timer(1)



