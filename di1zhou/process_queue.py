#!/usr/bin/env python3

import sys
from multiprocessing import Process,Queue

queue = Queue(maxsize=5)
def f1():
    queue.put('hello shiyanlou')

def f2():
    #if queue.empty() is not True:
    data = queue.get()
    print(data)
    #else:
    #    print('Queue is empty!')

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()
