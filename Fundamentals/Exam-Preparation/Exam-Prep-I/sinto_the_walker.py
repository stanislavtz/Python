import datetime

time, steps, step_time = input().split(':'), int(input()), int(input())
time = list(map(int, time))

start_time = datetime.datetime(1, 1, 1, time[0], time[1], time[2])
time_travel = steps * step_time

arrive_time = start_time + datetime.timedelta(seconds=time_travel)

print(f"Time Arrival: {arrive_time.time()}")