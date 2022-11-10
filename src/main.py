import argparse
from tqdm import tqdm
from time import sleep

parser = argparse.ArgumentParser(description="working mode for timer")

timer_parser = parser.add_mutually_exclusive_group()

timer_parser.add_argument('-s', '--sec', help='seconds to time', choices=range(1, 1000), metavar="[1-1000]", type=int, required=False)
timer_parser.add_argument('-m', '--min', help='minutes to time (default: 9 mins mainly because for the pasta cooking)', choices=range(1, 120), metavar="[1-120]", type=int, required=False, default=9)
timer_parser.add_argument('-ho', '--hour', help='hours to time', choices=range(1,2), metavar="1 or 2", type=int, required=False)
timer_parser.add_argument('-t', '--time', help='time to time', metavar='10:00', type=str, required=False)

args = parser.parse_args()

def timer(duration):
	pbar = tqdm(range(duration))
	pbar.update(duration)
	pbar.refresh()
	while duration:
		sleep(1)
		duration -= 1
		pbar.n = duration
		pbar.refresh()

if args.sec != None:
	remaining_time = args.sec
elif args.min != None:
	remaining_time = args.min * 60
elif args.hour != None:
	remaining_time = args.hour * 3600
timer(remaining_time)

#pbar.update(50)
#pbar.refresh()
#sleep(2)
#pbar.n = 10
#pbar.refresh()
#sleep(2)
#pbar.update(5)
