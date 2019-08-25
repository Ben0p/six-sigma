import psutil
import multiprocessing
import threading
import time
from datetime import datetime
import os



# Testing
while True:
    cpus = psutil.cpu_percent(interval=1, percpu=True)
    ram = [val for val in psutil.virtual_memory()]
    disk = psutil.disk_io_counters(perdisk=True, nowrap=True)
    disk_usage = psutil.disk_usage('C:/')
    print(cpus)
    print(ram)
    print(disk)
    print(disk_usage)