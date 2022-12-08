from subprocess import run
import os
import time
from datetime import datetime

while True:
	for range in (str(0000)):
		os.system("sensors | grep -E 'k10|temp1|amdgpu|edge'")
		time_now = datetime.now()
		current_time = time_now.strftime("%H:%M:%S")
		print (f"--------------------------------------@----{current_time}----------*")
	time.sleep(5) 