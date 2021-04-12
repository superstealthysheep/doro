import time
from playsound import playsound
import msvcrt

config = {
	"sound_path": "sounds/little tenor chime.wav",
	"time_list": [5, 3], #[25*60, 5*60, 25*60, 5*60, 25*60, 5*60, 25*60, 15*60]
	"timer_resolution": 1
}

playsound(config["sound_path"])

def timer(duration):
	print("Beginning timer with duration {}".format(duration))
	while duration > 0:
		time.sleep(config["timer_resolution"])
		duration -= config["timer_resolution"]
	
	alarm_sounding = True
	print("Alarm! Spam any key until sound stops")
	while alarm_sounding:
		playsound(config["sound_path"])
		if msvcrt.kbhit():
			alarm_sounding = False #could make this nicer by learning threading
			print("Alarm stopped.")
			input("idk will this fix things")
		
		

def run():
	while True: #just ctrl+c to escape. i'm lazy
		for duration in config["time_list"]:
			timer(duration)
	
run()