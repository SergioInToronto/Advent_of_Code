import os
import time

counter = 0 
print("PID:", os.getpid())

while True:
    counter += 1
    time.sleep(1)
