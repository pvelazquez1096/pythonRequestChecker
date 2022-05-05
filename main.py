# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep

import requests as req

vm = "http://10.10.100.195:9000"
desktop = "http://192.168.100.7:9000"
lap = "http://192.168.100.25:9000"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def makeRequest(url):
    return req.post(url, json={"input": "Which roles are being declined mostly?"})


def makeMean(times, url):
    total = 0
    for x in range(times):
        res = makeRequest(url)
        total = total + res.elapsed.total_seconds()
    return total / times


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runTimes = 50
    result = makeMean(runTimes, vm)
    print("Mean time for the prince team VM: " + str(result))
    result = makeMean(runTimes, desktop)
    print("Mean time for the Desktop: " + str(result))
    result = makeMean(runTimes, lap)
    print("Mean time for the Laptop: " + str(result))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
