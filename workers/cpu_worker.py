import psutil
import time


def getTimes():
        cpu_times = {}
        scputimes = psutil.cpu_times()
        
        cpu_times['user'] = scputimes.user
        cpu_times['system'] = scputimes.system
        cpu_times['idle'] = scputimes.idle
        cpu_times['interrupt'] = scputimes.interrupt
        cpu_times['dpc'] = scputimes.dpc

       
        return(cpu_times)



def getAll(q):
    while True:
        cpu = {}
        cpu_times = getTimes()
        cpu['cpu_times'] = cpu_times
        q.put(cpu)




if __name__ == '__main__':
    
    import multiprocessing
    
    import sys
    sys.path.append('..')


    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=getAll, args=(q, ))
    p.start()

    while True:
        line = q.get()
        print(line)


    # python ./workers/cpu_worker.py