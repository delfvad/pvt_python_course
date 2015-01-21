from twisted.internet import reactor, defer

def defer_sleep(seconds):
    d = defer.Deferred()
    reactor.callLater(seconds, d.callback, seconds)
    return d

@defer.inlineCallbacks
def blocking_f1():
    print("blocking_f1 before sleep")
    yield defer_sleep(1)
    print("blocking_f1 after sleep")

@defer.inlineCallbacks
def blocking_f2():
    print("blocking_f2 before sleep")
    yield defer_sleep(1)
    print("blocking_f2 after sleep")

reactor.callWhenRunning(blocking_f1)
reactor.callWhenRunning(blocking_f2)
reactor.callLater(0.5, reactor.stop)
reactor.run()
