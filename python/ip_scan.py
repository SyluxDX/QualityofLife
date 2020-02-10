""" Search network for ip in pattern x.x.x.0/24 """

import queue
import argparse
import subprocess
from threading import Thread
from datetime import datetime

def ip_work(out_list, work_queue):
    """ Get ip from queue and ping """
    while True:
        try:
            arg = work_queue.get(False)
            cmd = 'ping -w 25 -n 1 %s'%arg
            out = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = out.communicate()
            if 'bytes=' in out[0].decode():
                out_list.append(arg)
                if ARGS.verbose:
                    print('Connected %s'%arg)
            work_queue.task_done()
        except queue.Empty:
            break


def queue_ip():
    """ scan usin queue and threads """

    # setting queue
    ips = queue.Queue()
    out = list()
    for elm in range(2, 255):
        ips.put(ARGS.pattern.replace('*', '%d')%elm)
    print('Scanning %d Ips'%ips.qsize())
    start = datetime.now()
    # creating workers
    for _ in range(ARGS.threads):
        worker = Thread(target=ip_work, args=(out, ips,))
        worker.setDaemon(True)
        worker.start()

    ips.join()
    elapse = datetime.now()-start
    print('Found %d Ips in %s'%(len(out), elapse))
    if not ARGS.verbose:
        for elm in out:
            print('  %s'%elm)

if __name__ == "__main__":
    ARG_PARSER = argparse.ArgumentParser(description='Run UseCase tests')
    ARG_PARSER.add_argument('-t', '--threads'\
        , help='Number of "running" threads, default: 20', type=int, default=20)
    ARG_PARSER.add_argument('-p', '--pattern'\
        , help='Ip pattern for searching, ex: 192.168.1.*', default='192.168.1.*')
    ARG_PARSER.add_argument('-v', '--verbose'\
        , help='Increase output Verbosity, print IP after finding', action='store_true')

    ARGS = ARG_PARSER.parse_args()
    queue_ip()
