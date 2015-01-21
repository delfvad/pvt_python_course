import time
from twisted.internet import reactor

def blocking_f1():
    print("blocking_f1 before sleep")
    time.sleep(1)
    print("blocking_f1 after sleep")

def blocking_f2():
    print("blocking_f2 before sleep")
    time.sleep(1)
    print("blocking_f2 after sleep")

reactor.callWhenRunning(blocking_f1)
reactor.callWhenRunning(blocking_f2)
reactor.callLater(1, reactor.stop)
reactor.run()
