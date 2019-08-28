# record(eventName string)
# report() // count in last 5 minutes

'''
time unit? (use seconds)
ring buffer
5min + 1sec

Data:     [(['eventName1','eventName2'], timestamp),[], [], []]
Time:                 0                                  2   3       (index as seconds)

Ring buffer, after you reach the end, you start from the begining
Leave padding to prevent overwrite

using mod-ing for ring buffer?

remaining = Time % 3600
'''

import time

# hour worth of time
time_table = [({}, None)] * 60 * 60
MAX_WINDOW_SECONDS = 5

g_counter = 0


def record(eventName):
    global g_counter
    global time_table

    curr_time = time.time()
    dict_count = {}
    prev_dict, prev_time = time_table[g_counter]

    # Check if less then 1 second
    if prev_time == None or time.time() - prev_time > 1:
        # Goes into next index
        g_counter += 1
        dict_count[eventName] = 1
        time_table[g_counter] = (dict_count, curr_time)

    else:
        # Goes into current index
        if eventName in prev_dict:
            prev_dict[eventName] += 1
        else:
            prev_dict[eventName] = 1

    if g_counter == len(time_table):
        g_counter = 0

    # foo: 5


# bar: 15

# record("foo")
# record("foo")
# record("foo")
# report()
# foo: 3

def report():
    global g_counter
    global time_table
    curr_time = time.time()
    report = []
    second_passed = 0
    while (second_passed < MAX_WINDOW_SECONDS):
        prev_dict, prev_time = time_table[g_counter]
        if prev_time == None:
            return report
        if curr_time - prev_time < MAX_WINDOW_SECONDS:
            for key in prev_dict:
                report.append((key, prev_dict[key]))
        else:
            return report

        g_counter -= 1
        second_passed += 1

    return report


record('test')
record('test')
# print(time_table)
record('test')
record('test')

record('Hello')
record('Hello')
record('World')
record('Hello')
print(report())
print("Sleeping for 6 seconds")
time.sleep(6)
print(report())
