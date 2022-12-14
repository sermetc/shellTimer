import argparse
from tqdm import tqdm
from time import sleep
import datetime
from sys import platform
from subprocess import Popen

parser = argparse.ArgumentParser(description="working mode for timer")


timer_parser = parser.add_mutually_exclusive_group()

timer_parser.add_argument('-s', '--sec', help='seconds to time', choices=range(1, 1000), metavar="[1-1000]", type=int, required=False)
timer_parser.add_argument('-m', '--min', help='minutes to time (default: 9 mins mainly because for the pasta cooking)', choices=range(1, 120), metavar="[1-120]", type=int, required=False, default=9)
timer_parser.add_argument('-ho', '--hour', help='hours to time', choices=range(1,2), metavar="1 or 2", type=int, required=False)
timer_parser.add_argument('-t', '--time', help='time to time', metavar='20:00', type=str, required=False)

args = parser.parse_args()
current_time = [int(i) for i in str(datetime.datetime.now().time()).split('.')[0].split(":")[:2]]

def timer(duration):
	pbar = tqdm(range(duration), desc="timer", colour="green", bar_format="{desc}:|{bar}|{postfix}/{total}s",postfix=duration)
	pbar.update(duration)
	pbar.refresh()
	while duration:
		sleep(1)
		duration -= 1
		pbar.set_postfix_str(str(duration))
		pbar.n = duration
		pbar.refresh()

if args.sec != None:
	remaining_time = args.sec
elif args.hour != None:
	remaining_time = args.hour * 3600
elif args.time != None:
	tt = [int(i) for i in args.time.split(':')]
	hh = tt[0]
	mm = tt[1]
	target_secs = hh*3600 + mm*60
	now_secs = current_time[0]*3600 + current_time[1]*60
	remaining_time = target_secs - now_secs
	if remaining_time <= 0:
		print("Target time is before now, please give a time that is after now.")
		exit(0)
elif args.min != None:
	remaining_time = args.min * 60

print("--"*10)
timer(remaining_time)

if platform == "darwin":
	apple_script = f'display notification "Done!" sound name "Glass" with title "Timer"'
	p = Popen(['osascript', '-e', apple_script])
