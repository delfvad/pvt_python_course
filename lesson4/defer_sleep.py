from twisted.internet import reactor, defer
def defer_sleep(seconds):
    d = defer.Deferred()
    reactor.callLater(seconds, d.callback, seconds)
    return d

@defer.inlineCallbacks
def f():
    yield defer_sleep(5)
    reactor.stop()

reactor.callWhenRunning(f)
reactor.run()
